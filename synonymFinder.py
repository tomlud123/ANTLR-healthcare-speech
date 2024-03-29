import re

from antlr4 import InputStream, CommonTokenStream
from antlr4.error.ErrorListener import ErrorListener

from gen.MedicalSmartGlassesLexer import MedicalSmartGlassesLexer
from gen.MedicalSmartGlassesParser import MedicalSmartGlassesParser


#input: invalid_commands and grammar_words. Output: synonym suggestions
#Not perfect idea. continue frame rule needs only CONTINUE WS so everything can be synonym

class MyErrorListener(ErrorListener):
    def __init__(self):
        super(MyErrorListener, self).__init__()
        self.errors = False

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        self.errors = True



def preprocess_command(input_text):
    # Convert to lowercase
    lowercased = input_text.lower()

    # Replace specific abbreviations
    replaced = re.sub(r'\bml\b', 'milliliters', lowercased)
    replaced = re.sub(r'\bmg\b', 'milligrams', replaced)
    replaced = re.sub(r'\bok\b', 'okay', replaced)

    # Remove punctuation
    no_punctuation = re.sub(r'[^\w\s]', '', replaced)

    # Cut off text before 'okay glasses'
    final_text = re.split('okay glasses', no_punctuation)[-1].strip()

    return final_text



# Function to check if the command fits the current grammar
def check_command(input_str, entry_rule):
    # Convert input string to ANTLR InputStream
    input_stream = InputStream(input_str)

    # Lexical analysis
    lexer = MedicalSmartGlassesLexer(input_stream)
    stream = CommonTokenStream(lexer)

    # Syntactic analysis
    parser = MedicalSmartGlassesParser(stream)
    parser.removeErrorListeners()
    error_listener = MyErrorListener()
    parser.addErrorListener(error_listener)

    # Dynamically call the entry rule
    parse_tree = getattr(parser, entry_rule)()

    # Return True if the parsing was successful, False if errors occurred
    return not error_listener.errors


# Modify the find_synonyms function to include the entry rule
def find_synonyms(invalid_commands, grammar_words):
    synonyms = {}
    for command, classification in invalid_commands.items():
        command = preprocess_command(command)
        words = command.split()
        if check_command(command, classification): #if command already valid
            continue
        for i, word in enumerate(words):
            # if check_command(command.replace(' xyz ', ' '), classification): # checks for word deletion
            #     synonyms[word] = ' '
            #     continue
            for grammar_word in grammar_words:
                if word != grammar_word:
                    # Replace the word and check if the command becomes valid
                    new_command = words[:i] + [grammar_word] + words[i+1:]
                    new_command_str = ' '.join(new_command)
                    if check_command(new_command_str, classification):
                        synonyms[word] = grammar_word
    return synonyms

# Invalid commands with their classifications
invalid_commands = {
    # "Please display blood pressure": "request_data",
    # "Show the medication of patient Thomas Mustermann": "request_data",
    # "Continue frame": "continue_frame",
    # "Security alert unauthorized access in the pharmacy": "start_emergency",
    # "Attention please start emergency": "start_emergency",
    "Agree emergency": "u11",
    "Pause the frame": "u01",
    "Resume the current frame": "u02",
    "turn on the display": "u04",
}

# Extract unique words from the grammar
grammar_words = {'stop', 'accept', 'frame', 'continue', 'request', 'show', 'give', 'get', 'present', 'display', 'session', 'turn'}


if __name__ == "__main__":
    synonyms = find_synonyms(invalid_commands, grammar_words)
    print(synonyms)