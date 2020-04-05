from predmet import Predmet


class NepolozeniPredmet(Predmet):
    def __init__(self, naziv, silabus, broj_pokusaja=1):
        super().__init__(naziv, silabus)
        self.broj_pokusaja = broj_pokusaja