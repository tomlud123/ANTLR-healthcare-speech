import argparse
import json
import logging
import re
import sys

from antlr4 import *
from antlr4.error.ErrorStrategy import DefaultErrorStrategy
from antlr4.error.Errors import InputMismatchException
from antlr4.tree.Trees import Trees

from CaisMeVisitor import CaisMeVisitor
from gen.MedicalSmartGlassesLexer import MedicalSmartGlassesLexer
from gen.MedicalSmartGlassesParser import MedicalSmartGlassesParser
from gen.MedicalSmartGlassesParserVisitor import MedicalSmartGlassesParserVisitor

# Master thesis solution


class ExceptionThrowingErrorStrategy(DefaultErrorStrategy):
    def beginErrorCondition(self, recognizer):
        raise RecognitionException




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
    input = "OK Glasses, set medication fresh water 1 cup and aspirin 200 milliliters at 10 oclock end medication"
    if len(sys.argv) > 1:
        input = sys.argv[1]
    json_dict = get_json(input)
    print("\nOutput:\n" + json.dumps(json_dict, indent=4))
