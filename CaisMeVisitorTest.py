import unittest
from commandToJson import *

visitor = CaisMeVisitor()


class CommandToJsonTest(unittest.TestCase):

    def test_trigger(self):
        output = get_json("stop frame")
        self.assertEqual(output, None)

    def test_trigger_2(self):
        output = get_json("hello patient now ok glasses stop frame")
        self.assertEqual(output['type'], "GLASSES_COMMAND")
        self.assertEqual(output['content'], "STOP_FRAME")

    def test_U01_1(self):
        output = get_json("ok glasses stop frame")
        self.assertEqual(output['type'], "GLASSES_COMMAND")
        self.assertEqual(output['content'], "STOP_FRAME")

    def test_U01_2(self):
        output = get_json("ok glasses stop")
        self.assertEqual(output['type'], "GLASSES_COMMAND")
        self.assertEqual(output['content'], "STOP_FRAME")

    def test_U01_3(self):
        output = get_json("ok glasses stops")
        self.assertEqual(output, None)


def get_json(command_str):
    visitor.visit(parse(command_str))
    return visitor.get_json_dict()


if __name__ == '__main__':
    unittest.main()
