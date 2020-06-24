class Student():
    def __init__(self, institution, profession, student_id, surname, parent_name, name, gender, address, phone_number, id_number, birth_date):
        self.institution = institution
        self.profession = profession
        self.student_id = student_id
        self.surname = surname
        self.parent_name = parent_name
        self.name = name
        self.gender = gender
        self.address = address
        self.phone_number = phone_number
        self.id_number = id_number
        self.birth_date = birth_date

    def __eq__(self, other):
        if type(other) != Student:
            raise TypeError("Not type Student")
        return self.student_id == other.student_id

    def __gt__(self, other):
        if type(other) != Student:
            raise TypeError("Not type Student")
        return self.student_id > other.student_id

    def __ge__(self, other):
        if type(other) != Student:
            raise TypeError("Not type Student")
        return self.student_id >= other.student_id

    def __str__(self):
        return str({"institution": self.institution, "profession": self.profession, "student_id": self.student_id, "surname": self.surname, "parent_name": self.parent_name, "name": self.name, "gender": self.gender, "address": self.address, "phone_number": self.phone_number, "id_number": self.id_number, "birth_date": self.birth_date})

    def make_array(self):
        return [self.institution, self.profession, self.student_id, self.surname, self.parent_name, self.name, self.gender, self.address, self.phone_number, self.id_number, self.birth_date]

    def __iter__(self):
        yield "institution", self.institution
        yield "profession", self.profession
        yield "student_id", self.student_id
        yield "surname", self.surname
        yield "parent_name", self.parent_name
        yield "name", self.name
        yield "gender", self.gender
        yield "address", self.address
        yield "phone_number", self.phone_number
        yield "id_number", self.id_number
        yield "birth_date", self.birth_date