//DEPRECATED
//DEPRECATED
//DEPRECATED
//DEPRECATED
//DEPRECATED
//DEPRECATED
//DEPRECATED
//DEPRECATED
//DEPRECATED
//DEPRECATED - now are extra parser and lexer .g4 files

grammar MedicalSmartGlasses;

command: TRIGGER (glasses_command | request_data | protocol | medication | request_patient | message) EOF;

//glasses_command, commands U05-U08 from doc are skipped (need not determined)
glasses_command: frame | switch | emergency | u19;

frame: u01 | u02;
u01: STOP (WS FRAME)?;
u02: CONTINUE (WS FRAME)?;

switch: u03 | u04;
u03: TURN WS OFF (WS DISPLAY)?;
u04: TURN WS ON (WS DISPLAY)?;

emergency: emergency_launch | emergency_acceptation;
emergency_launch: u09 | u10;
emergency_acceptation: u11 | u12;
u09: START WS EMERGENCY;
u10: END WS EMERGENCY;
u11: ACCEPT WS EMERGENCY;
u12: LEAVE WS EMERGENCY;

u19: (SWITCH WS TO | SHOW ) WS MESSAGES;


//request_data
request_data: u13 | u14 ;
u13: SHOW WS data;
u14: SHOW WS data WS interval;
data: WORD (WS WORD)*;
interval: OF WS LAST WS time;
time: INT WS TIME_UNIT;


//protocol
protocol: u15;
u15: SET WS NOTE WS note WS END WS NOTE | START WS DOCUMENTATION WS note WS END WS DOCUMENTATION;
note: content_word (WS content_word)*;

//medication: ;
medication: u16 | u17;
u16: (SET | START) WS MEDICATION WS note WS END WS MEDICATION;
u17: (SET | START) WS MEDICATION WS note WS AT WS INT WS OCLOCK WS END WS MEDICATION;

//request_patient: ;
request_patient: u18 ;
u18: CHANGE WS PATIENT WS TO WS patient_name;
patient_name: WORD (WS WORD)? (WS WORD)? (WS WORD)?;

//message: ;
message: u20;
u20: START WS NEW? WS MESSAGE WS SEND WS IT WS TO WS patient_name WS PLEASE WS note WS END WS NEW? WS MESSAGE;


content_word: WORD | STOP | FRAME | CONTINUE | TURN | ON | OFF | DISPLAY | START | ACCEPT | LEAVE | EMERGENCY
| SWITCH | SHOW | TO | MESSAGES | OF | LAST | TIME_UNIT | DAY | HOUR | MINUTE | S | SET | NOTE | DOCUMENTATION
| MEDICATION | AT | OCLOCK | CHANGE | PATIENT | NEW | MESSAGE | SEND | IT | INT | WORD;

TRIGGER: 'ok glasses ';

//glasses_command
STOP: 'stop';
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
EMERGENCY: 'emergency';
SWITCH: 'switch';
SHOW: 'show';
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
AT: 'at';
OCLOCK: 'oclock';

//request_patient
CHANGE: 'change';
PATIENT: 'patient';

//message
NEW: 'new';
MESSAGE: 'message';
SEND: 'send';
IT: 'it';
PLEASE: 'please';

INT: [0-9]+;
WORD: [a-zA-Z]+;
WS : [ \t\r\n]+;