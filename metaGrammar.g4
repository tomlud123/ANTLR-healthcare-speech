grammar metaGrammar;

file: grammarDecl options? rule+ EOF;
grammarDecl: 'parser grammar ' ID ';';
options: 'options' '{' option+ '}';
option: 'tokenVocab' '=' ID ';' ;
rule: ruleName ':' ruleBody ';';
ruleName: ID;
ruleBody: command | phrase;
command: abstractCMD | concreteCMD;
abstractCMD: phrase* '(' command ( '|' command )+ ')' ( '*' | '+' | '?' )? phrase*;
concreteCMD: phrase* '('? ( phrase+ ( '|' phrase+ )* ) ')'? ( '*' | '+' | '?' )? phrase*;
phrase : ID | TOKEN | '.' | '~' phrase | phrase phrase | phrase '|' phrase | '(' phrase ')' | phrase ('*' | '+' | '?') ;

TOKEN: [A-Z]+;
WS : [ \t\r\n]+ -> skip;
COMMENT : '//' ~[\r\n]* -> skip ;
ID : [a-zA-Z_] [a-zA-Z0-9_]* ;
