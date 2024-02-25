lexer grammar MedicalSmartGlassesLexer;

TRIGGER: ('ok glasses '|'okay glasses ');

//glasses_command
STOP: ('stop' | 'hold');
FRAME: 'frame';
CONTINUE: 'continue';
TURN: 'turn';
ON: 'on';
OFF: 'off';
DISPLAY: 'display';
START: 'start';
END: 'end';
ACCEPT: 'accept';
LEAVE: 'leave';
MODE: 'mode';
EMERGENCY: 'emergency';
SWITCH: 'switch';
SHOW: ('show' | 'present');
TO: 'to';
MESSAGES: 'messages';

//request_data
OF: 'of';
LAST: 'last';
TIME_UNIT: (DAY | HOUR | MINUTE)+S?;
DAY: 'day';
HOUR: 'hour';
MINUTE: 'minute';
S: 's';

//protocol
SET: 'set';
NOTE: 'note';
DOCUMENTATION: 'documentation';

//medication
MEDICATION: 'medication';
AND: 'and';
AT: 'at';
OCLOCK: 'oclock';
PM: 'pm';
AM: 'am';

//request_patient
CHANGE: 'change';
PATIENT: 'patient';

//message
NEW: 'new';
MESSAGE: 'message';
SEND: 'send';
IT: 'it';

INT: [0-9]+;
WORD: [a-zA-Z]+;
WS : [ \t\r\n]+ -> skip;
PLEASE: 'please' -> skip ;
THE : 'the' -> skip ;
A : 'a' -> skip ;
I_WANT_TO : 'i want to' -> skip ;