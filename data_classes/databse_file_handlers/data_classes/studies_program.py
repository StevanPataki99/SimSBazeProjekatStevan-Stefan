class StudiesProgram():
    def __init__(self, institution, level, program_signature, program_name):
        self.institution = institution
        self.level = level
        self.program_signature = program_signature
        self.prgram_name = prgram_name
    
    def __eq__(self, other):
        if type(other) != StudiesProgram:
            raise TypeError("Not type StudiesProgram")
        return self.program_signature == other.program_signature

    def __gt__(self, other):
        if type(other) != StudiesProgram:
            raise TypeError("Not type StudiesProgram")
        return self.program_signature > other.program_signature

    def __ge__(self, other):
        if type(other) != StudiesProgram:
            raise TypeError("Not type StudiesProgram")
        return self.program_signature >= other.program_signature

    def __str__(self):
        return str({"institution": self.institution, "level": self.level, "program_signature": self.program_signature, "program_name": self.program_name})

    def make_array(self):
        return [self.institution, self.level, self.program_signature, self.program_name]

    def __iter__(self):
        yield "institution", self.institution
        yield "level", self.level
        yield "program_signature", self.program_signature
        yield "program_name", self.program_name
