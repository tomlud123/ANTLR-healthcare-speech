import unittest
from commandToJson import *

visitor = CaisMeVisitor()


class CommandToJsonTest(unittest.TestCase):

    def test_general(self):
        output = get_json("")
        self.assertEqual(output, {})
        very_long_input = "ok glasses"*1000
        output = get_json(very_long_input)
        self.assertEqual(output, {})
        output = get_json(very_long_input+" stop frame")
        self.assertEqual(output['content'], "STOP_FRAME")
        output = get_json("asd asd  l 8394y tp9284 p9y qp9t8yp98y 89y2p 87y 23t9tyg ")
        self.assertEqual(output, {})

    def test_trigger(self):
        output = get_json("okay glasses")
        self.assertEqual(output, {})
        output = get_json("okay glasses stop frame okay glasses")
        self.assertEqual(output, {})
        output = get_json("stop frame")
        self.assertEqual(output, {})
        output = get_json("stop frame ok glasses")
        self.assertEqual(output, {})

    def test_preprocess(self):
        output = get_json("okay glasses STOP frame!!!")
        self.assertEqual(output['type'], "GLASSES_COMMAND")
        self.assertEqual(output['content'], "STOP_FRAME")
        output = get_json("Hello patient!?}{,./♣:?>`ó1»┘ĺ<$%&$ Now, okay glasses stop frame")
        self.assertEqual(output['type'], "GLASSES_COMMAND")
        self.assertEqual(output['content'], "STOP_FRAME")
        output = get_json("ok glasses patient John ok glasses ok glasses ok glasses ok glasses ok glasses ok "
                          "glasses ok ok glasses ok glasses ok glasses 123 lorem ipsum ok glasses... stop frame")
        self.assertEqual(output['type'], "GLASSES_COMMAND")
        self.assertEqual(output['content'], "STOP_FRAME")
        output = get_json("ok glasses set note    10g  finish note")
        self.assertEqual(output['content'], "10 g")

    def test_U01(self):
        output = get_json("okay glasses stop frame")
        assert isinstance(output, dict)
        self.assertEqual(output['type'], "GLASSES_COMMAND")
        self.assertEqual(output['content'], "STOP_FRAME")
        self.assertEqual(json.dumps(output, indent=4).count('\n'), 3)
        output = get_json("ok glasses stop")
        self.assertEqual(output['type'], "GLASSES_COMMAND")
        self.assertEqual(output['content'], "STOP_FRAME")

    def test_U02(self):
        output = get_json("ok glasses continue")
        self.assertEqual(output['type'], "GLASSES_COMMAND")
        self.assertEqual(output['content'], "CONTINUE_FRAME")
        output = get_json("ok glasses continue frame")
        self.assertEqual(output['type'], "GLASSES_COMMAND")
        self.assertEqual(output['content'], "CONTINUE_FRAME")

    def test_U03(self):
        output = get_json("ok glasses turn off display")
        self.assertEqual(output['type'], "GLASSES_COMMAND")
        self.assertEqual(output['content'], "TURN_OFF")
        output = get_json("ok glasses turn off")
        self.assertEqual(output['type'], "GLASSES_COMMAND")
        self.assertEqual(output['content'], "TURN_OFF")

    def test_U04(self):
        output = get_json("okay glasses turn on display")
        self.assertEqual(output['type'], "GLASSES_COMMAND")
        self.assertEqual(output['content'], "TURN_ON")
        output = get_json("ok glasses turn on")
        self.assertEqual(output['type'], "GLASSES_COMMAND")
        self.assertEqual(output['content'], "TURN_ON")

    def test_U09(self):
        output = get_json("okay glasses start emergency")
        self.assertEqual(output['type'], "GLASSES_COMMAND")
        self.assertEqual(output['content'], "START_EMERGENCY")

    def test_U10(self):
        output = get_json("okay glasses leave emergency")
        self.assertEqual(output['type'], "GLASSES_COMMAND")
        self.assertEqual(output['content'], "LEAVE_EMERGENCY")

    def test_U11(self):
        output = get_json("okay glasses accept emergency")
        self.assertEqual(output['type'], "GLASSES_COMMAND")
        self.assertEqual(output['content'], "ACCEPT_EMERGENCY")
        output = get_json("okay glasses accept emergency mode")
        self.assertEqual(output['type'], "GLASSES_COMMAND")
        self.assertEqual(output['content'], "ACCEPT_EMERGENCY")

    def test_U12(self):
        output = get_json("okay glasses leave emergency")
        self.assertEqual(output['type'], "GLASSES_COMMAND")
        self.assertEqual(output['content'], "LEAVE_EMERGENCY")
        output = get_json("okay glasses leave emergency mode")
        self.assertEqual(output['type'], "GLASSES_COMMAND")
        self.assertEqual(output['content'], "LEAVE_EMERGENCY")

    def test_U13(self):
        output = get_json("ok glasses show some data about John of last 10 minutes")
        self.assertEqual(output['type'], "REQUEST_DATA")
        self.assertEqual(output['content'], "some data about john")
        self.assertEqual(output['interval'], "10m")
        output = get_json("OK Glasses, show temperature of John (of last 3 days)")
        self.assertEqual(output['type'], "REQUEST_DATA")
        self.assertEqual(output['content'], "temperature of john")
        self.assertEqual(output['interval'], "3d")

    def test_U14(self):
        output = get_json("okay glasses show name")
        self.assertEqual(output['type'], "REQUEST_DATA")
        self.assertEqual(output['content'], "name")
        output = get_json("okay glasses show pulse of the patient 2 times ")
        self.assertEqual(output['type'], "REQUEST_DATA")
        self.assertEqual(output['content'], "pulse of the patient 2 times")

    def test_U15(self):
        output = get_json("okay glasses set note 0")
        self.assertEqual(output, {})
        output = get_json("okay glasses set note patient is sick finish note")
        self.assertEqual(output['type'], "PROTOCOL")
        self.assertEqual(output['content'], "patient is sick")
        output = get_json("okay glasses start documentation bed 12 is empty finish documentation")
        self.assertEqual(output['type'], "PROTOCOL")
        self.assertEqual(output['content'], "bed 12 is empty")

    def test_U16(self):
        output = get_json("OK Glasses, set medication fresh water, 200 millilitres, and pill of ibuprofen 600mg, finish medication")
        self.assertEqual(output['type'], "MEDICATION")
        self.assertEqual(len(output['content']), 2)
        self.assertEqual(output['content'][0]['medicine'], "fresh water")
        self.assertEqual(output['content'][0]['quantity'], "200")
        self.assertEqual(output['content'][0]['unit'], "millilitres")
        self.assertEqual(output['content'][1]['medicine'], "pill of ibuprofen")
        self.assertEqual(output['content'][1]['quantity'], "600")
        output = get_json("OK Glasses, set medication fresh water, 200 millilitres, and a pill of ibuprofen 600mg ok glasses, finish medication")
        self.assertEqual(output, {})
        output = get_json("OK Glasses, set medication vitamins 1 pill finish medication")
        self.assertEqual(output['content'][0]['medicine'], "vitamins")
        output = get_json("OK Glasses, set medication vitamins 1 pill and lek 20 g and aspirin 2 liters finish medication")
        self.assertEqual(output['content'][2]['quantity'], "2")
        output = get_json("ok glasses set medication dada 2 pills and 1 cup of water finish medication")
        self.assertEqual(output['content'][1]['medicine'], "water")
        self.assertEqual(output['content'][1]['unit'], "cup")


    def test_U17(self):
        output = get_json("OK Glasses, set medication water, 1 cup, and pill of ibuprofen 600mg at 11 o'clock, finish medication")
        self.assertEqual(output['type'], "MEDICATION")
        self.assertEqual(output['time'].startswith("11"), True)
        self.assertEqual(len(output['content']), 2)
        self.assertEqual(output['content'][0]['medicine'], "water")
        self.assertEqual(output['content'][0]['quantity'], "1")
        self.assertEqual(output['content'][0]['unit'], "cup")
        self.assertEqual(output['content'][1]['medicine'], "pill of ibuprofen")
        self.assertEqual(output['content'][1]['quantity'], "600")
        output = get_json("OK Glasses, set medication vitamins 1000 pills at 5 o'clock finish medication")
        self.assertEqual(output['content'][0]['medicine'], "vitamins")
        self.assertEqual(output['time'].startswith("5"), True)
        output = get_json("OK Glasses, set medication vitamins 1 pill and lek 20 g and aspirin 2 liters at 2 PM finish medication")
        self.assertEqual(output['time'].startswith("2"), True)
        self.assertEqual(output['content'][2]['quantity'], "2")
        self.assertEqual(len(output['content']), 3)
        output = get_json("OK Glasses, set medication nimm zwei 12 pieces at 4 AM finish medication")
        self.assertEqual(output['time'].startswith("4"), True)
        self.assertEqual(len(output['content']), 1)

    def test_U18(self):
        output = get_json("OK Glasses, change patient to Susann")
        self.assertEqual(output['type'], "REQUEST_PATIENT")
        self.assertEqual(output['content'].title(), "susann".title())
        output = get_json("OK Glasses, change patient to John Kowalski van Bommel")
        self.assertEqual(output['type'], "REQUEST_PATIENT")
        self.assertEqual(output['content'].title(), "John Kowalski van Bommel".title())

    def test_U19(self):
        output = get_json("ok glasses switch to messages")
        self.assertEqual(output['type'], "GLASSES_COMMAND")
        self.assertEqual(output['content'], "SHOW_MESSAGES")

    def test_U20(self):
        output = get_json("ok glasses start message hello finish message send it to John")
        self.assertEqual(output['type'], "MESSAGE")
        self.assertEqual(output['to'].title(), "john".title())
        self.assertEqual(output['content'], "hello")
        output = get_json("ok glasses start new message hello what's up patient 1 James is fine finish new message send it to John Kowal Kowalski")
        self.assertEqual(output['type'], "MESSAGE")
        self.assertEqual(output['to'].title(), "john kowal kowalski".title())
        self.assertEqual(output['content'], normalize("hello what's up patient 1 James is fine"))


if __name__ == '__main__':
    unittest.main()
