class Institution():
    def __init__(self, signature, name, address):
        self.signature = signature
        self.name = name
        self.address = address

    def __eq__(self, other):
        if type(other) != Institution:
            raise TypeError("Not type Institution")
        return self.signature == other.signature

    def __gt__(self, other):
        if type(other) != Institution:
            raise TypeError("Not type Institution")
        return self.signature > other.signature

    def __ge__(self, other):
        if type(other) != Institution:
            raise TypeError("Not type Institution")
        return self.signature >= other.signature

    def __str__(self):
        return str({"signature": self.signature, "name": self.name, "address": self.address})

    def make_array(self):
        return [self.signature, self.name, self.address]

    def __iter__(self):
        yield "signature", self.signature
        yield "name", self.name
        yield "address", self.address
