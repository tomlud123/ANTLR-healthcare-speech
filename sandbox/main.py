import argparse
import json
import re

from antlr4 import CommonTokenStream, InputStream
from antlr4.tree.Trees import Trees

from gen.MedicalSmartGlassesLexer import MedicalSmartGlassesLexer
from gen.MedicalSmartGlassesParser import MedicalSmartGlassesParser
from synonymFinder import check_command

# script for experiments
def print_tree(input_text):
    # Set up the lexer and parser
    lexer = MedicalSmartGlassesLexer(InputStream(input_text))
    stream = CommonTokenStream(lexer)
    parser = MedicalSmartGlassesParser(stream)

    # Parse the input
    tree = parser.command()

    # Print the entire parse tree
    print(Trees.toStringTree(tree, None, parser))
def preprocess_command(input_text):
    # Convert to lowercase
    lowercased = input_text.lower()

    # Replace specific abbreviations
    replaced = re.sub(r'\bml\b', 'milliliters', lowercased)
    replaced = re.sub(r'\bmg\b', 'milligrams', replaced)
    replaced = re.sub(r'\bokay\b', 'ok', replaced)

    # Remove punctuation
    no_punctuation = re.sub(r'[^\w\s]', '', replaced)

    # Cut off text BEFORE 'ok glasses'
    final_text = "ok glasses " + re.split('ok glasses', no_punctuation)[-1].strip()

    return final_text


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Process an input string.")
    parser.add_argument("input_string", type=str, help="The input string to be processed.")
    command = parser.parse_args().input_string
    command = preprocess_command(command)
    print("PREP: "+command)
    command = "ok glasses set note lala babababababa end note"#TODO usu
    result = print_tree(command)
