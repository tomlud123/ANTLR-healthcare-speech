import argparse
import re
import sys

#Works. Input: g4 and (dict of synonyms + terminal input synonym). Output: save modified g4
def save_g4_file(file_path, content):
    try:
        with open(file_path, 'w') as file:
            file.write(content)
        print("File saved successfully.")
    except IOError as e:
        print(f"Error writing to file {file_path}: {e}")


def read_g4_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        return content
    except IOError as e:
        print(f"Error reading file {file_path}: {e}")
        return None


def replace_with_synonyms(text, synonym_dict):
    for synonym, word in synonym_dict.items():
        if synonym in text:
            print("Skipped word '" + synonym + "' (is already in grammar vocabulary)\n")
            continue

        # Check if word is in parentheses
        regex = r"\([^()]*'{}'[^()]*\)".format(word)
        matches = re.findall(regex, text)

        # Replace words inside parentheses differently
        # forces antlr g4 to use literals only in token rules and to use parentheses there only for alternatives
        for match in matches:
            replacement = match.replace(f"'{word}'", f"'{word}' | '{synonym}'")
            text = text.replace(match, replacement)

        # Replace words outside of parentheses
        if synonym not in text:
            text = text.replace(f"'{word}'", f"('{word}' | '{synonym}')")

    return text


def add_terminal_input():
    try:
        if len(sys.argv) < 3: #1 script call + 2 dict args
            return  # no enough arguments
        parser = argparse.ArgumentParser(description="Process input strings.")
        # First input string argument
        parser.add_argument("input_string1", type=str, help="The first input string to be processed.")
        # Second input string argument
        parser.add_argument("input_string2", type=str, help="The second input string to be processed.")
        args = parser.parse_args()
        synonyms[args.input_string1] = args.input_string2
        print(synonyms)
    except SystemExit:
        # Catching SystemExit exception
        print("Terminal arguments not found")


synonyms = {
    "stój": "stop",
    # Add more pairs as needed
}

if __name__ == "__main__":
    add_terminal_input()
    path = "MedicalSmartGlassesLexer.g4"
    antlr_file_content = read_g4_file(path)
    if antlr_file_content is not None:
        fixed_content = replace_with_synonyms(antlr_file_content, synonyms)
        print(fixed_content)
        input("\nPress Enter to save...\n")
        save_g4_file(path, fixed_content)