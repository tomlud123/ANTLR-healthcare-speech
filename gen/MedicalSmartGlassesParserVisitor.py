# Generated from MedicalSmartGlassesParser.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .MedicalSmartGlassesParser import MedicalSmartGlassesParser
else:
    from MedicalSmartGlassesParser import MedicalSmartGlassesParser

# This class defines a complete generic visitor for a parse tree produced by MedicalSmartGlassesParser.

class MedicalSmartGlassesParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MedicalSmartGlassesParser#command.
    def visitCommand(self, ctx:MedicalSmartGlassesParser.CommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MedicalSmartGlassesParser#glasses_command.
    def visitGlasses_command(self, ctx:MedicalSmartGlassesParser.Glasses_commandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MedicalSmartGlassesParser#frame.
    def visitFrame(self, ctx:MedicalSmartGlassesParser.FrameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MedicalSmartGlassesParser#u01.
    def visitU01(self, ctx:MedicalSmartGlassesParser.U01Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MedicalSmartGlassesParser#u02.
    def visitU02(self, ctx:MedicalSmartGlassesParser.U02Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MedicalSmartGlassesParser#switch.
    def visitSwitch(self, ctx:MedicalSmartGlassesParser.SwitchContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MedicalSmartGlassesParser#u03.
    def visitU03(self, ctx:MedicalSmartGlassesParser.U03Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MedicalSmartGlassesParser#u04.
    def visitU04(self, ctx:MedicalSmartGlassesParser.U04Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MedicalSmartGlassesParser#emergency.
    def visitEmergency(self, ctx:MedicalSmartGlassesParser.EmergencyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MedicalSmartGlassesParser#emergency_launch.
    def visitEmergency_launch(self, ctx:MedicalSmartGlassesParser.Emergency_launchContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MedicalSmartGlassesParser#emergency_acceptation.
    def visitEmergency_acceptation(self, ctx:MedicalSmartGlassesParser.Emergency_acceptationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MedicalSmartGlassesParser#u09.
    def visitU09(self, ctx:MedicalSmartGlassesParser.U09Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MedicalSmartGlassesParser#u10.
    def visitU10(self, ctx:MedicalSmartGlassesParser.U10Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MedicalSmartGlassesParser#u11.
    def visitU11(self, ctx:MedicalSmartGlassesParser.U11Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MedicalSmartGlassesParser#u12.
    def visitU12(self, ctx:MedicalSmartGlassesParser.U12Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MedicalSmartGlassesParser#u19.
    def visitU19(self, ctx:MedicalSmartGlassesParser.U19Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MedicalSmartGlassesParser#request_data.
    def visitRequest_data(self, ctx:MedicalSmartGlassesParser.Request_dataContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MedicalSmartGlassesParser#u13.
    def visitU13(self, ctx:MedicalSmartGlassesParser.U13Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MedicalSmartGlassesParser#u14.
    def visitU14(self, ctx:MedicalSmartGlassesParser.U14Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MedicalSmartGlassesParser#data.
    def visitData(self, ctx:MedicalSmartGlassesParser.DataContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MedicalSmartGlassesParser#interval.
    def visitInterval(self, ctx:MedicalSmartGlassesParser.IntervalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MedicalSmartGlassesParser#time.
    def visitTime(self, ctx:MedicalSmartGlassesParser.TimeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MedicalSmartGlassesParser#protocol.
    def visitProtocol(self, ctx:MedicalSmartGlassesParser.ProtocolContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MedicalSmartGlassesParser#u15.
    def visitU15(self, ctx:MedicalSmartGlassesParser.U15Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MedicalSmartGlassesParser#note.
    def visitNote(self, ctx:MedicalSmartGlassesParser.NoteContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MedicalSmartGlassesParser#set_medication.
    def visitSet_medication(self, ctx:MedicalSmartGlassesParser.Set_medicationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MedicalSmartGlassesParser#u16.
    def visitU16(self, ctx:MedicalSmartGlassesParser.U16Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MedicalSmartGlassesParser#u17.
    def visitU17(self, ctx:MedicalSmartGlassesParser.U17Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MedicalSmartGlassesParser#medication.
    def visitMedication(self, ctx:MedicalSmartGlassesParser.MedicationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MedicalSmartGlassesParser#medicine.
    def visitMedicine(self, ctx:MedicalSmartGlassesParser.MedicineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MedicalSmartGlassesParser#unit.
    def visitUnit(self, ctx:MedicalSmartGlassesParser.UnitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MedicalSmartGlassesParser#timestamp.
    def visitTimestamp(self, ctx:MedicalSmartGlassesParser.TimestampContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MedicalSmartGlassesParser#request_patient.
    def visitRequest_patient(self, ctx:MedicalSmartGlassesParser.Request_patientContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MedicalSmartGlassesParser#u18.
    def visitU18(self, ctx:MedicalSmartGlassesParser.U18Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MedicalSmartGlassesParser#patient_name.
    def visitPatient_name(self, ctx:MedicalSmartGlassesParser.Patient_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MedicalSmartGlassesParser#message.
    def visitMessage(self, ctx:MedicalSmartGlassesParser.MessageContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MedicalSmartGlassesParser#u20.
    def visitU20(self, ctx:MedicalSmartGlassesParser.U20Context):
        return self.visitChildren(ctx)



del MedicalSmartGlassesParser