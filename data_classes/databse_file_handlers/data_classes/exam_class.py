class ExamClass():
    def __init__(self, institution, signature, name, espb):
        self.institution = institution
        self.signature = signature
        self.name = name
        self.espb = espb

    def __eq__(self, other):
        if type(other) != ExamClass:
            raise TypeError("Not type ExamClass")
        return self.signature == other.signature

    def __gt__(self, other):
        if type(other) != ExamClass:
            raise TypeError("Not type ExamClass")
        return self.signature > other.signature

    def __ge__(self, other):
        if type(other) != ExamClass:
            raise TypeError("Not type ExamClass")
        return self.signature >= other.signature

    def __str__(self):
        return str({"institution": self.institution, "signature": self.signature, "name": self.name,  "espb": self.espb})

    def make_array(self):
        return [self.institution, self.signature, self.name, self.espb]

    def __iter__(self):
        yield "institution", self.institution
        yield "signature", self.signature
        yield "name", self.name,
        yield "espb", self.espb