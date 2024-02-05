import unittest
from commandToJson import *

visitor = CaisMeVisitor()


class CommandToJsonTest(unittest.TestCase):
    def testU01(self):
        parse_tree = parse("ok glasses stop frame")
        visitor.visit(parse_tree)
        output = visitor.get_json_dict()
        self.assertEqual(output.type, "GLASSES_COMMAND")  # add assertion here


if __name__ == '__main__':
    # visitor = CaisMeVisitor()
    unittest.main()
