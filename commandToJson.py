import argparse
import json
import logging
import re
import sys

from antlr4 import *
from antlr4.error.ErrorStrategy import DefaultErrorStrategy
from antlr4.error.Errors import InputMismatchException
from antlr4.tree.Trees import Trees

from gen.MedicalSmartGlassesLexer import MedicalSmartGlassesLexer
from gen.MedicalSmartGlassesParser import MedicalSmartGlassesParser
from gen.MedicalSmartGlassesParserVisitor import MedicalSmartGlassesParserVisitor

# Master thesis solution


class ExceptionThrowingErrorStrategy(DefaultErrorStrategy):
    def beginErrorCondition(self, recognizer):
        raise RecognitionException


class CaisMeVisitor(MedicalSmartGlassesParserVisitor):

    def __init__(self):
        self.json_dict = {}  # Initialize json_dict as an instance variable

    def visitU01(self, ctx):
        self.json_dict['type'] = 'GLASSES_COMMAND'
        self.json_dict['content'] = 'STOP_FRAME'

    def visitU02(self, ctx):
        self.json_dict['type'] = 'GLASSES_COMMAND'
        self.json_dict['content'] = 'CONTINUE_FRAME'

    def visitU03(self, ctx):
        self.json_dict['type'] = 'GLASSES_COMMAND'
        self.json_dict['content'] = 'TURN_OFF'

    def visitU04(self, ctx):
        self.json_dict['type'] = 'GLASSES_COMMAND'
        self.json_dict['content'] = 'TURN_ON'

    def visitU05(self, ctx):
        self.json_dict['type'] = 'GLASSES_COMMAND'
        self.json_dict['content'] = 'START_SESSION'

    def visitU06(self, ctx):
        self.json_dict['type'] = 'GLASSES_COMMAND'
        self.json_dict['content'] = 'STOP_SESSION'

    def visitU07(self, ctx):
        self.json_dict['type'] = 'GLASSES_COMMAND'
        self.json_dict['content'] = 'JOIN_SESSION'

    def visitU08(self, ctx):
        self.json_dict['type'] = 'GLASSES_COMMAND'
        self.json_dict['content'] = 'LEAVE_SESSION'

    def visitU09(self, ctx):
        self.json_dict['type'] = 'GLASSES_COMMAND'
        self.json_dict['content'] = 'START_EMERGENCY'

    def visitU10(self, ctx):
        self.json_dict['type'] = 'GLASSES_COMMAND'
        self.json_dict['content'] = 'END_EMERGENCY'

    def visitU11(self, ctx):
        self.json_dict['type'] = 'GLASSES_COMMAND'
        self.json_dict['content'] = 'ACCEPT_EMERGENCY'

    def visitU12(self, ctx):
        self.json_dict['type'] = 'GLASSES_COMMAND'
        self.json_dict['content'] = 'LEAVE_EMERGENCY'

    def visitU13(self, ctx):
        self.json_dict['type'] = 'REQUEST_DATA'
        self.json_dict['content'] = ctx.data().getText()
        time_interval = ctx.interval().time().getText()
        self.json_dict['interval'] = time_interval.replace(" hours", "h").replace(" minutes", "m").replace(" days", "d")

    def visitU14(self, ctx):
        self.json_dict['type'] = 'REQUEST_DATA'
        self.json_dict['content'] = ctx.data().getText()

    def visitU15(self, ctx):
        self.json_dict['type'] = 'PROTOCOL'
        self.json_dict['content'] = ctx.note().getText()

    def visitU16(self, ctx):
        self.json_dict['type'] = 'MEDICATION'
        elements = len(ctx.medications().medication())
        content = []
        for i in range(elements):
            medication = {}
            node = ctx.medications().medication()[i]
            medication['medicine'] = node.medicine().getText()
            medication['quantity'] = node.INT().getText()
            medication['unit'] = node.unit().getText()
            content.append(medication)
        self.json_dict['content'] = content

    def visitU17(self, ctx):
        self.json_dict['type'] = 'MEDICATION'
        time = ctx.timestamp().getText().replace(" oclock", ":00")
        self.json_dict['time'] = time
        elements = len(ctx.medications().medication())
        content = []
        for i in range(elements):
            medication = {}
            node = ctx.medications().medication()[i]
            medication['medicine'] = node.medicine().getText()
            medication['quantity'] = node.INT().getText()
            medication['unit'] = node.unit().getText()
            content.append(medication)
        self.json_dict['content'] = content

    def visitU18(self, ctx):
        self.json_dict['type'] = 'REQUEST_PATIENT'
        self.json_dict['content'] = ctx.patient_name().getText().title()

    def visitU19(self, ctx):
        self.json_dict['type'] = 'GLASSES_COMMAND'
        self.json_dict['content'] = 'SHOW_MESSAGES'

    def visitU20(self, ctx):
        self.json_dict['type'] = 'MESSAGE'
        self.json_dict['to'] = ctx.patient_name().getText().title()
        self.json_dict['content'] = ctx.note().getText()

    def visit(self, tree):
        if tree is None:
            return
        self.json_dict = {}  # Reset or initialize json_dict for this visit, if needed
        super().visit(tree)  # Correctly call the parent class's visit method, passing the tree

    def get_json_dict(self):
        return self.json_dict


# Function to parse an input string
def parse(input_string):
    input_stream = InputStream(input_string)
    lexer = MedicalSmartGlassesLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = MedicalSmartGlassesParser(stream)
    parser._errHandler = ExceptionThrowingErrorStrategy()
    tree = parser.command()  # Assuming 'command' is the root rule
    # Print the entire parse tree
    logging.info("Parse tree: "+Trees.toStringTree(tree, None, parser))
    return tree


def preprocess(input_text):
    #conversion of numbers written with letters into usual numbers notation is missing
    TRIGGER = "ok glasses"
    input_text = input_text.lower()
    input_text = re.sub(r'[^\w\s]', '', input_text)

    # Cut off text BEFORE 'ok glasses'
    input_text = input_text.replace("okay", "ok")
    if TRIGGER in input_text:
        input_text = TRIGGER + " " + re.split(TRIGGER, input_text)[-1].strip()

    # Split words and numbers
    input_text = re.sub(r'(\d)(?=\D)|(\D)(?=\d)', r'\1\2 ', input_text)

    # Unify multiple whitespaces into a single whitespace
    input_text = re.sub(r'\s+', ' ', input_text)

    return input_text


def get_json(command_str):
    visitor = CaisMeVisitor()
    try:
        parse_tree = parse(preprocess(command_str))
    except RecognitionException:
        logging.info("Provided input doesn't match the grammar")
        parse_tree = None
    visitor.visit(parse_tree)
    return visitor.get_json_dict()


if __name__ == "__main__":
    input = "OK Glasses, show weather information of last 2 days"
    if len(sys.argv) > 1:
        input = sys.argv[1]
    json_dict = get_json(input)
    print("\nOutput:\n" + json.dumps(json_dict, indent=4))
