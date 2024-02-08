#!/usr/bin/env bash

grammar_name="MedicalSmartGlasses"

# Clear the specified folder
find "./gen/" -mindepth 1 -delete

## Run the command that generates files in the base directory
antlr4 -Dlanguage=Python3 ${grammar_name}Lexer.g4
antlr4 -Dlanguage=Python3 -visitor -o "./gen" ${grammar_name}Parser.g4

## Move the generated files to the specified folder (assuming they are directly in the base directory)
mv "${grammar_name}Lexer.interp" "./gen"
mv "${grammar_name}Lexer.tokens" "./gen"
mv "${grammar_name}Lexer.py" "./gen"

read -p "${grammar_name}-grammar compilation finished. Press any key"
