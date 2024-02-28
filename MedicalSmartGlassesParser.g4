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

u01: STOP (FRAME)?;
u02: CONTINUE (FRAME)?;
u03: TURN OFF (DISPLAY)?;
u04: TURN ON (DISPLAY)?;
u09: START EMERGENCY;
u10: FINISH EMERGENCY;
u11: ACCEPT EMERGENCY (MODE)?;
u12: LEAVE EMERGENCY (MODE)?;
u13: SHOW data interval;
u14: SHOW data;
u15: SET NOTE note FINISH NOTE | START DOCUMENTATION note FINISH DOCUMENTATION;
u16: trig_medication MEDICATION medications FINISH MEDICATION;
u17: trig_medication MEDICATION medications AT timestamp FINISH MEDICATION;
u18: CHANGE PATIENT TO patient_name;
u19: trig_message MESSAGES;
u20: START (NEW)? MESSAGE note FINISH (NEW)? MESSAGE (AND)? SEND IT TO patient_name;

data: . (.)*;
interval: OF LAST time;
time: INT TIME_UNIT;
note: . (.)*;
trig_medication: (SET | START);
medications: medication (AND medication)*;
medication: (medicine INT unit | INT unit OF medicine);
medicine: ~INT (~(INT | AND))*;
unit: ~INT (~INT)? (~INT)?;
timestamp: INT (OCLOCK | PM | AM);
patient_name: WORD (WORD)? (WORD)? (WORD)?;
trig_message: (SWITCH TO | SHOW);
