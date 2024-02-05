//parser generate with: antlr4 -Dlanguage=Python3 -visitor MedicalSmartGlassesParser.g4
//TODO: create test for every command u01-u20
//command requirements: https://git-st.inf.tu-dresden.de/tooz/launcher/-/wikis/Functional-Testcases-Speech

parser grammar MedicalSmartGlassesParser;

options {
    tokenVocab = MedicalSmartGlassesLexer;
}

command: TRIGGER (glasses_command | request_data | protocol | set_medication | request_patient | message) EOF;

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
u11: ACCEPT WS EMERGENCY (WS MODE)?;
u12: LEAVE WS EMERGENCY (WS MODE)?;

u19: (SWITCH WS TO | SHOW) WS MESSAGES;


//request_data
request_data: u13 | u14 ;
u13: SHOW WS data WS interval;
u14: SHOW WS data;
data: . (WS .)*;
interval: OF WS LAST WS time;
time: INT WS TIME_UNIT;

//protocol
protocol: u15;
u15: SET WS NOTE WS note WS END WS NOTE | START WS DOCUMENTATION WS note WS END WS DOCUMENTATION;
note: . (WS .)*;

//medication
set_medication: u16 | u17;
u16: (SET | START) WS MEDICATION WS medication (WS AND WS medication)* WS END WS MEDICATION;
u17: (SET | START) WS MEDICATION WS medication (WS AND WS medication)* WS AT WS timestamp WS END WS MEDICATION;
medication: medicine WS INT WS unit;
medicine: ~INT (WS ~INT)*;
unit: ~INT (WS ~INT)? (WS ~INT)?;
timestamp: INT WS (OCLOCK | PM | AM);

//request_patient: ;
request_patient: u18 ;
u18: CHANGE WS PATIENT WS TO WS patient_name;
patient_name: WORD (WS WORD)? (WS WORD)? (WS WORD)?;

//message: ;
message: u20;
u20: START (WS NEW)? WS MESSAGE WS note WS END (WS NEW)? WS MESSAGE (WS AND)? WS SEND WS IT WS TO WS patient_name;

//content_word: STOP | FRAME | CONTINUE | TURN | ON | OFF | DISPLAY | START | ACCEPT | LEAVE | EMERGENCY
//| SWITCH | SHOW | TO | MESSAGES | OF | LAST | TIME_UNIT | DAY | HOUR | MINUTE | S | SET | NOTE | DOCUMENTATION
//| MEDICATION | AT | OCLOCK | CHANGE | PATIENT | NEW | MESSAGE | SEND | IT | INT | WORD;