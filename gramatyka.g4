// define a grammar called Hello
grammar gramatyka;

// Main rule
command: stop_frame | continue_frame | request_data;

// Sub-rules
stop_frame: ('halt' | 'stop' | 'pause' | 'cease') frame_keyword EOF;
continue_frame: ('continue' | 'resume' | 'proceed') frame_keyword EOF;

frame_keyword: 'frame' | 'session';

request_data: verb ('the')? data_type EOF;

verb: show_verb | give_verb | get_verb | present_verb | display_verb;

//synonyms
show_verb: ('show' | 'visualize' | 'illustrate' | 'demonstrate');
give_verb: ('give' | 'provide' | 'supply' | 'furnish' | 'deliver');
get_verb: ('get' | 'acquire' | 'retrieve' | 'obtain');
present_verb: ('present' | 'offer' | 'introduce' | 'submit');
display_verb: ('display' | 'exhibit');

data_type: WORD+ | data_type_synonyms;

data_type_synonyms: ('temperature' | 'temp') | ('pressure' | 'press') | ('velocity' | 'speed');

WORD: [a-zA-Z0-9]+;
WS: [ \t\r\n]+ -> skip;