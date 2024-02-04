import json

from antlr4 import *
from antlr4.tree.Trees import Trees

from gen.MedicalSmartGlassesLexer import MedicalSmartGlassesLexer
from gen.MedicalSmartGlassesParser import MedicalSmartGlassesParser
from gen.MedicalSmartGlassesParserVisitor import MedicalSmartGlassesParserVisitor

# Master thesis solution

json_dict = {}

class CaisMeVisitor(MedicalSmartGlassesParserVisitor):
    def visitU01(self, ctx):
        json_dict['type'] = 'GLASSES_COMMAND'
        json_dict['content'] = 'STOP_FRAME'

    def visitU02(self, ctx):
        json_dict['type'] = 'GLASSES_COMMAND'
        json_dict['content'] = 'CONTINUE_FRAME'

    def visitU03(self, ctx):
        json_dict['type'] = 'GLASSES_COMMAND'
        json_dict['content'] = 'TURN_OFF'

    def visitU04(self, ctx):
        json_dict['type'] = 'GLASSES_COMMAND'
        json_dict['content'] = 'TURN_ON'

    def visitU05(self, ctx):
        json_dict['type'] = 'GLASSES_COMMAND'
        json_dict['content'] = 'START_SESSION'

    def visitU06(self, ctx):
        json_dict['type'] = 'GLASSES_COMMAND'
        json_dict['content'] = 'STOP_SESSION'

    def visitU07(self, ctx):
        json_dict['type'] = 'GLASSES_COMMAND'
        json_dict['content'] = 'JOIN_SESSION'

    def visitU08(self, ctx):
        json_dict['type'] = 'GLASSES_COMMAND'
        json_dict['content'] = 'LEAVE_SESSION'

    def visitU09(self, ctx):
        json_dict['type'] = 'GLASSES_COMMAND'
        json_dict['content'] = 'START_EMERGENCY'

    def visitU10(self, ctx):
        json_dict['type'] = 'GLASSES_COMMAND'
        json_dict['content'] = 'END_EMERGENCY'

    def visitU11(self, ctx):
        json_dict['type'] = 'GLASSES_COMMAND'
        json_dict['content'] = 'ACCEPT_EMERGENCY'

    def visitU12(self, ctx):
        json_dict['type'] = 'GLASSES_COMMAND'
        json_dict['content'] = 'LEAVE_EMERGENCY'

    def visitU13(self, ctx):
        json_dict['type'] = 'REQUEST_DATA'
        json_dict['content'] = ctx.data().getText()
        time_interval = ctx.interval().time().getText()
        json_dict['interval'] = time_interval.replace(" hours", "h").replace(" minutes", "m").replace(" days", "d")

    def visitU14(self, ctx):
        json_dict['type'] = 'REQUEST_DATA'
        json_dict['content'] = ctx.data().getText()

    def visitU15(self, ctx):
        json_dict['type'] = 'PROTOCOL'
        json_dict['content'] = ctx.note().getText()

    def visitU16(self, ctx):
        json_dict['type'] = 'MEDICATION'
        elements = len(ctx.medication())
        content = []
        for i in range(elements):
            medication = {}
            node = ctx.medication()[i]
            medication['medicine'] = node.medicine().getText()
            medication['quantity'] = node.INT().getText()
            medication['unit'] = node.unit().getText()
            content.append(medication)
        json_dict['content'] = content

    def visitU17(self, ctx):
        json_dict['type'] = 'MEDICATION'
        time = ctx.timestamp().getText().replace(" oclock", ":00")
        json_dict['time'] = time
        elements = len(ctx.medication())
        content = []
        for i in range(elements):
            medication = {}
            node = ctx.medication()[i]
            medication['medicine'] = node.medicine().getText()
            medication['quantity'] = node.INT().getText()
            medication['unit'] = node.unit().getText()
            content.append(medication)
        json_dict['content'] = content

    def visitU18(self, ctx):
        json_dict['type'] = 'REQUEST_PATIENT'
        json_dict['content'] = ctx.patient_name().getText().title()

    def visitU19(self, ctx):
        json_dict['type'] = 'REQUEST_PATIENT'
        json_dict['content'] = 'SHOW_MESSAGES'

    def visitU20(self, ctx):
        json_dict['type'] = 'REQUEST_PATIENT'
        json_dict['to'] = ctx.patient_name().getText().title()
        json_dict['content'] = ctx.note().getText()


# Function to parse an input string
def parse(input_string):
    input_stream = InputStream(input_string)
    lexer = MedicalSmartGlassesLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = MedicalSmartGlassesParser(stream)
    tree = parser.command()  # Assuming 'command' is the root rule
    # Print the entire parse tree
    print("Parse tree: "+Trees.toStringTree(tree, None, parser))
    return tree


def get_output():
    return json.dumps(json_dict, indent=4)


if __name__ == "__main__":
    tree = parse("ok glasses set note blabla bla blabla 123 hour oclock end note")
    visitor = CaisMeVisitor()
    visitor.visit(tree)
    print("\nOutput:\n" + get_output())
