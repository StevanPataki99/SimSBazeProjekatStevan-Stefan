from random import randint
class Student:

    def __init__(self, broj_indeksa, ime_prezime, polozeni_predmeti=[], nepolozeni_predmeti=[], id=None):
        self.broj_indeksa = broj_indeksa
        self.ime_prezime = ime_prezime
        self.polozeni_predmeti = polozeni_predmeti
        self.nepolozeni_predmeti = nepolozeni_predmeti
        # self.godina_upisa = self.broj_indeksa.split("/")[0]
        self.id = int(self.broj_indeksa.replace('/',''))

    def __eq__(self, other):
        return self.id == other.id

    def __gt__(self, other):
        return self.id > other.id

    def __ge__(self, other):
        return self.id >= other.id

    def __lt__(self, other):
        return self.id < other.id   
        
    def __str__(self):
        return str({"broj_indeksa":self.id, "ime_prezime":self.ime_prezime})        

        
    

