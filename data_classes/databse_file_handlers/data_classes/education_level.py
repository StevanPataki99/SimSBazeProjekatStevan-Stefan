class EducationLevel():
    def __init__(self, signature, name):
        self.signature = signature
        self.name = name

    def __eq__(self, other):
        if type(other) != EducationLevel:
            raise TypeError("Not type EducationLevel")
        return self.signature == other.signature

    def __gt__(self, other):
        if type(other) != EducationLevel:
            raise TypeError("Not type EducationLevel")
        return self.signature > other.signature

    def __ge__(self, other):
        if type(other) != EducationLevel:
            raise TypeError("Not type EducationLevel")
        return self.signature >= other.signature

    def __str__(self):
        return str({"signature": self.signature, "name": self.name})

    def make_array(self):
        return [self.signature, self.name]

    def __iter__(self):
        yield "signature", self.signature
        yield "name", self.name
