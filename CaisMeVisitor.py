from gen.MedicalSmartGlassesParserVisitor import MedicalSmartGlassesParserVisitor


class CaisMeVisitor(MedicalSmartGlassesParserVisitor):

    def readNode(self, ctx):
        if ctx.getChildCount() == 0:
            return ctx.getText() #empty string
        text = ""
        for child in ctx.getChildren():
            text = text + self.readNode(child) + " "
        return text[:-1]

    def __init__(self):
        self.json_dict = {}  # Initialize json_dict as an instance variable

    def visitU01(self, ctx):
        self.json_dict['type'] = 'GLASSES_COMMAND'
        self.json_dict['content'] = 'STOP_FRAME'

    def visitU02(self, ctx):
        self.json_dict['type'] = 'GLASSES_COMMAND'
        self.json_dict['content'] = 'CONTINUE_FRAME'

    def visitU03(self, ctx):
        self.json_dict['type'] = 'GLASSES_COMMAND'
        self.json_dict['content'] = 'TURN_OFF'

    def visitU04(self, ctx):
        self.json_dict['type'] = 'GLASSES_COMMAND'
        self.json_dict['content'] = 'TURN_ON'

    def visitU05(self, ctx):
        self.json_dict['type'] = 'GLASSES_COMMAND'
        self.json_dict['content'] = 'START_SESSION'

    def visitU06(self, ctx):
        self.json_dict['type'] = 'GLASSES_COMMAND'
        self.json_dict['content'] = 'STOP_SESSION'

    def visitU07(self, ctx):
        self.json_dict['type'] = 'GLASSES_COMMAND'
        self.json_dict['content'] = 'JOIN_SESSION'

    def visitU08(self, ctx):
        self.json_dict['type'] = 'GLASSES_COMMAND'
        self.json_dict['content'] = 'LEAVE_SESSION'

    def visitU09(self, ctx):
        self.json_dict['type'] = 'GLASSES_COMMAND'
        self.json_dict['content'] = 'START_EMERGENCY'

    def visitU10(self, ctx):
        self.json_dict['type'] = 'GLASSES_COMMAND'
        self.json_dict['content'] = 'END_EMERGENCY'

    def visitU11(self, ctx):
        self.json_dict['type'] = 'GLASSES_COMMAND'
        self.json_dict['content'] = 'ACCEPT_EMERGENCY'

    def visitU12(self, ctx):
        self.json_dict['type'] = 'GLASSES_COMMAND'
        self.json_dict['content'] = 'LEAVE_EMERGENCY'

    def visitU13(self, ctx):
        self.json_dict['type'] = 'REQUEST_DATA'
        # self.json_dict['content'] = ctx.data().getText()
        self.json_dict['content'] = self.readNode(ctx.data())
        time_interval = self.readNode(ctx.interval().time())
        self.json_dict['interval'] = (time_interval.replace(" hours", "h")
                                      .replace(" minutes", "m").replace(" days", "d"))

    def visitU14(self, ctx):
        self.json_dict['type'] = 'REQUEST_DATA'
        self.json_dict['content'] = self.readNode(ctx.data())

    def visitU15(self, ctx):
        self.json_dict['type'] = 'PROTOCOL'
        self.json_dict['content'] = self.readNode(ctx.note())

    def visitU16(self, ctx):
        self.json_dict['type'] = 'MEDICATION'
        elements = len(ctx.medications().medication())
        content = []
        for i in range(elements):
            medication = {}
            node = ctx.medications().medication()[i]
            medication['medicine'] = self.readNode(node.medicine())
            medication['quantity'] = self.readNode(node.INT())
            medication['unit'] = self.readNode(node.unit())
            content.append(medication)
        self.json_dict['content'] = content

    def visitU17(self, ctx):
        self.json_dict['type'] = 'MEDICATION'
        time = self.readNode(ctx.timestamp()).replace(" oclock", ":00")
        self.json_dict['time'] = time
        elements = len(ctx.medications().medication())
        content = []
        for i in range(elements):
            medication = {}
            node = ctx.medications().medication()[i]
            medication['medicine'] = self.readNode(node.medicine())
            medication['quantity'] = self.readNode(node.INT())
            medication['unit'] = self.readNode(node.unit())
            content.append(medication)
        self.json_dict['content'] = content

    def visitU18(self, ctx):
        self.json_dict['type'] = 'REQUEST_PATIENT'
        self.json_dict['content'] = self.readNode(ctx.patient_name()).title()

    def visitU19(self, ctx):
        self.json_dict['type'] = 'GLASSES_COMMAND'
        self.json_dict['content'] = 'SHOW_MESSAGES'

    def visitU20(self, ctx):
        self.json_dict['type'] = 'MESSAGE'
        self.json_dict['to'] = self.readNode(ctx.patient_name()).title()
        self.json_dict['content'] = self.readNode(ctx.note())

    def visit(self, tree):
        if tree is None:
            return
        self.json_dict = {}  # Reset or initialize json_dict for this visit, if needed
        super().visit(tree)  # Correctly call the parent class's visit method, passing the tree

    def get_json_dict(self):
        return self.json_dict
