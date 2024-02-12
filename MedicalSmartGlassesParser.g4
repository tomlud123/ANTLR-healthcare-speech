//command requirements: https://git-st.inf.tu-dresden.de/tooz/launcher/-/wikis/Functional-Testcases-Speech

parser grammar MedicalSmartGlassesParser;

options {
    tokenVocab = MedicalSmartGlassesLexer;
}

command: TRIGGER (glasses_command | request_data | protocol | set_medication | request_patient | message) EOF;

//commands U05-U08 from doc are skipped (need not determined)
glasses_command: frame | switch | emergency | u19;
frame: u01 | u02;
switch: u03 | u04;
emergency: emergency_launch | emergency_acceptation;
emergency_launch: u09 | u10;
emergency_acceptation: u11 | u12;
request_data: u13 | u14 ;
protocol: u15;
set_medication: u16 | u17;
request_patient: u18 ;
message: u20;

u01: STOP (WS FRAME)?;
u02: CONTINUE (WS FRAME)?;
u03: TURN WS OFF (WS DISPLAY)?;
u04: TURN WS ON (WS DISPLAY)?;
u09: START WS EMERGENCY;
u10: END WS EMERGENCY;
u11: ACCEPT WS EMERGENCY (WS MODE)?;
u12: LEAVE WS EMERGENCY (WS MODE)?;
u13: SHOW WS data WS interval;
u14: SHOW WS data;
u15: SET WS NOTE WS note WS END WS NOTE | START WS DOCUMENTATION WS note WS END WS DOCUMENTATION;
u16: trig_medication WS MEDICATION medications WS END WS MEDICATION;
u17: trig_medication WS MEDICATION medications WS AT WS timestamp WS END WS MEDICATION;
u18: CHANGE WS PATIENT WS TO WS patient_name;
u19: (SWITCH WS TO | SHOW) WS MESSAGES;
u20: START (WS NEW)? WS MESSAGE WS note WS END (WS NEW)? WS MESSAGE (WS AND)? WS SEND WS IT WS TO WS patient_name;

data: . (WS .)*;
interval: OF WS LAST WS time;
time: INT WS TIME_UNIT;
note: . (WS .)*;
trig_medication: (SET | START);
medications: WS medication (WS AND WS medication)*;
medication: medicine WS INT WS unit;
medicine: ~INT (WS ~(INT | AND))*;
unit: ~INT (WS ~INT)? (WS ~INT)?;
timestamp: INT WS (OCLOCK | PM | AM);
patient_name: WORD (WS WORD)? (WS WORD)? (WS WORD)?;
