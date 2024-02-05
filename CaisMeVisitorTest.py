import unittest
from commandToJson import *

visitor = CaisMeVisitor()


class CommandToJsonTest(unittest.TestCase):

    def test_trigger(self):
        output = get_json("")
        self.assertEqual(output, {})
        output = get_json("asd asd  l 8394y tp9284 p9y qp9t8yp98y 89y2p 87y 23t9tyg ")
        self.assertEqual(output, {})
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
        output = get_json("ok glasses set note    10g  end note")
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


if __name__ == '__main__':
    unittest.main()
