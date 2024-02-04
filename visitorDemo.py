import json

from antlr4 import *
from antlr4.tree.Trees import Trees

from gen.MedicalSmartGlassesLexer import MedicalSmartGlassesLexer
from gen.MedicalSmartGlassesParser import MedicalSmartGlassesParser
from gen.MedicalSmartGlassesParserVisitor import MedicalSmartGlassesParserVisitor

# Master thesis solution

class CaisMeVisitor(MedicalSmartGlassesParserVisitor):
    def visitU01(self, ctx):
        output_json['type'] = 'GLASSES_COMMAND'
        output_json['content'] = 'STOP_FRAME'

    def visitU02(self, ctx):
        output_json['type'] = 'GLASSES_COMMAND'
        output_json['content'] = 'CONTINUE_FRAME'

    def visitU03(self, ctx):
        output_json['type'] = 'GLASSES_COMMAND'
        output_json['content'] = 'TURN_OFF'

    def visitU04(self, ctx):
        output_json['type'] = 'GLASSES_COMMAND'
        output_json['content'] = 'TURN_ON'

    def visitU05(self, ctx):
        output_json['type'] = 'GLASSES_COMMAND'
        output_json['content'] = 'START_SESSION'

    def visitU06(self, ctx):
        output_json['type'] = 'GLASSES_COMMAND'
        output_json['content'] = 'STOP_SESSION'

    def visitU07(self, ctx):
        output_json['type'] = 'GLASSES_COMMAND'
        output_json['content'] = 'JOIN_SESSION'

    def visitU08(self, ctx):
        output_json['type'] = 'GLASSES_COMMAND'
        output_json['content'] = 'LEAVE_SESSION'

    def visitU09(self, ctx):
        output_json['type'] = 'GLASSES_COMMAND'
        output_json['content'] = 'START_EMERGENCY'

    def visitU10(self, ctx):
        output_json['type'] = 'GLASSES_COMMAND'
        output_json['content'] = 'END_EMERGENCY'

    def visitU11(self, ctx):
        output_json['type'] = 'GLASSES_COMMAND'
        output_json['content'] = 'ACCEPT_EMERGENCY'

    def visitU12(self, ctx):
        output_json['type'] = 'GLASSES_COMMAND'
        output_json['content'] = 'LEAVE_EMERGENCY'

    def visitU13(self, ctx):
        output_json['type'] = 'REQUEST_DATA'
        output_json['content'] = ctx.data().getText()
        time_interval = ctx.interval().time().getText()
        output_json['interval'] = time_interval.replace(" hours", "h").replace(" minutes", "m").replace(" days", "d")

    def visitU14(self, ctx):
        output_json['type'] = 'REQUEST_DATA'
        output_json['content'] = ctx.data().getText()

    def visitU15(self, ctx):
        output_json['type'] = 'PROTOCOL'
        output_json['content'] = ctx.note().getText()

    def visitU16(self, ctx):
        output_json['type'] = 'MEDICATION'
        elements = len(ctx.medication())
        content = []
        for i in range(elements):
            medication = {}
            node = ctx.medication()[i]
            medication['medicine'] = node.medicine().getText()
            medication['quantity'] = node.INT().getText()
            medication['unit'] = node.unit().getText()
            content.append(medication)
        output_json['content'] = content

    def visitU17(self, ctx):
        output_json['type'] = 'MEDICATION'
        time = ctx.timestamp().getText().replace(" oclock", ":00")
        output_json['time'] = time
        elements = len(ctx.medication())
        content = []
        for i in range(elements):
            medication = {}
            node = ctx.medication()[i]
            medication['medicine'] = node.medicine().getText()
            medication['quantity'] = node.INT().getText()
            medication['unit'] = node.unit().getText()
            content.append(medication)
        output_json['content'] = content

    def visitU18(self, ctx):
        output_json['type'] = 'REQUEST_PATIENT'
        output_json['content'] = ctx.patient_name().getText().title()

    def visitU19(self, ctx):
        output_json['type'] = 'REQUEST_PATIENT'
        output_json['content'] = 'SHOW_MESSAGES'

    def visitU20(self, ctx):
        output_json['type'] = 'REQUEST_PATIENT'
        output_json['to'] = ctx.patient_name().getText().title()
        output_json['content'] = ctx.note().getText()

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


if __name__ == "__main__":
    walker = ParseTreeWalker()
    input_string = ("ok glasses start new message wychludzic kibel and come later to patient Max Meier end message and send it to twoja stara")
    tree = parse(input_string)
    output_json = {}
    visitor = CaisMeVisitor()
    visitor.visit(tree)

    json_string = json.dumps(output_json, indent=4)  # `indent=4` for pretty printing
    print("\nOutput:\n"+json_string)