class StudiesGroupPlan():
    def __init__(self, institution_program, program_signature, block, position, class_institution, class_signature):
        self.institution_program = institution_program
        self.program_signature = program_signature
        self.block = block
        self.position = position
        self.class_institution = class_institution
        self.class_signature = class_signature

    def __eq__(self, other):
        if type(other) != StudiesGroupPlan:
            raise TypeError("Not type StudiesGroupPlan")
        return self.institution_program == other.institution_program

    def __gt__(self, other):
        if type(other) != StudiesGroupPlan:
            raise TypeError("Not type StudiesGroupPlan")
        return self.institution_program > other.institution_program

    def __ge__(self, other):
        if type(other) != StudiesGroupPlan:
            raise TypeError("Not type StudiesGroupPlan")
        return self.institution_program >= other.institution_program

    def __str__(self):
        return str({"institution_program": self.institution_program, "program_signature": self.program_signature, "block": self.block, "position": self.position, "class_institution": self.class_institution, "class_signature": self.class_signature})

    def make_array(self):
        return [self.institution_program, self.program_signature, self.block, self.position, self.class_institution, self.class_signature]

    def __iter__(self):
        yield "institution_program", self.institution_program
        yield "program_signature", self.program_signature
        yield "block", self.block
        yield "position", self.position
        yield "class_institution", self.class_institution
        yield "class_signature", self.class_signature