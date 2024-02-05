#!/usr/bin/env bash

grammar_name="MedicalSmartGlasses"

# Clear the specified folder
find "./gen/" -mindepth 1 -delete

## Run the command that generates files in the base directory
antlr4 -Dlanguage=Python3 MedicalSmartGlassesLexer.g4
antlr4 -Dlanguage=Python3 -visitor -o "./gen" MedicalSmartGlassesParser.g4

## Move the generated files to the specified folder (assuming they are directly in the base directory)
mv "${grammar_name}Lexer.interp" "./gen"
mv "${grammar_name}Lexer.tokens" "./gen"
mv "${grammar_name}Lexer.py" "./gen"

read -p "Press enter to continue"
