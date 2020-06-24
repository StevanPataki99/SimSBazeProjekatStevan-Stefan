class StudentStudies():
    def __init__(self, institution, program_signature, student_from_institution, profession, student_id, school_year, studies_year, block, acceptance_number, acceptance_date, approval_date, espb_start, espb_final):
        self.institution = institution
        self.program_signature = program_signature
        self.student_from_institution = student_from_institution
        self.profession = profession
        self.student_id = student_id
        self.school_year = school_year
        self.studies_year = studies_year
        self.block = block
        self.acceptance_number = acceptance_number
        self.acceptance_date = acceptance_date
        self.approval_date = approval_date
        self.espb_start = espb_start
        self.espb_final = espb_final

     def __eq__(self, other):
        if type(other) != StudentStudies:
            raise TypeError("Not type StudentStudies")
        return self.student_from_institution == other.student_from_institution

    def __gt__(self, other):
        if type(other) != StudentStudies:
            raise TypeError("Not type StudentStudies")
        return self.student_from_institution > other.student_from_institution

    def __ge__(self, other):
        if type(other) != StudentStudies:
            raise TypeError("Not type StudentStudies")
        return self.student_from_institution >= other.student_from_institution

    def __str__(self):
        return str({"institution": self.institution, "program_signature": self.program_signature, "student_from_institution": self.student_from_institution, "profession": self.profession, "student_id": self.student_id, "school_year": self.school_year, "studies_year": self.studies_year, "block": self.block, "acceptance_number": self.acceptance_number, "acceptance_date": self.acceptance_date, "approval_date": self.approval_date, "espb_start": self.espb_start, "espb_final": self.espb_final})

    def make_array(self):
        return [self.institution, self.program_signature, self.student_from_institution, self.profession, self.student_id, self.school_year, self.studies_year, self.block, self.acceptance_number, self.acceptance_date, self.approval_date, self.espb_start, self.espb_final]

    def __iter__(self):
        yield "institution", self.institution
        yield "program_signature", self.program_signature
        yield "student_from_institution", self.student_from_institution
        yield "profession", self.profession
        yield "student_id", self.student_id
        yield "school_year", self.school_year
        yield "studies_year", self.studies_year
        yield "block", self.block
        yield "acceptance_number", self.acceptance_number
        yield "acceptance_date", self.acceptance_date
        yield "approval_date", self.approval_date
        yield "espb_start", self.espb_start
        yield "espb_final", self.espb_final