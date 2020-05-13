from PySide2 import QtWidgets, QtCore
from serial_file_handler import SerialFileHandler


class PolozeniPredmetModel(QtCore.QAbstractTableModel):
    def __init__(self,studenti, parent=None):
        super().__init__(parent)
        self.students = studenti
        self.polozeni_predmeti = [] # ovo je osnovna lista modela

    def get_element(self, index):
        # vratiti studenta na datom redu
        return self.polozeni_predmeti[index.row()]

    # metode za redefisanje read-only modela
    def rowCount(self, index):
        return len(self.polozeni_predmeti)

    def columnCount(self, index):
        return 3 # zbog broja atributa koje prikazujemo o polozenom predmetu

    def data(self, index, role=QtCore.Qt.DisplayRole):
        polozeni_predmet = self.get_element(index)
        if index.column() == 0 and role == QtCore.Qt.DisplayRole:
            return polozeni_predmet.naziv
        elif index.column() == 1 and role == QtCore.Qt.DisplayRole:
            return polozeni_predmet.silabus
        elif index.column() == 2 and role == QtCore.Qt.DisplayRole:
            return polozeni_predmet.ocena


    def headerData(self, section, orientation, role=QtCore.Qt.DisplayRole):
        # section u zavisnosti od orijentacije je red ili kolona
        # orijentacija je vertikalna ili horizontalna
        if section == 0 and orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return "Naziv"
        elif section == 1 and orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return "Silabus"
        elif section == 2 and orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return "Ocena"

    # ove metode definisu editabilni model
    def setData(self, index, value, role=QtCore.Qt.EditRole):
        polozeni_predmet = self.get_element(index)
        if value == "":
            return False
        if index.column() == 0 and role == QtCore.Qt.EditRole: #broj indeksa
            polozeni_predmet.naziv = value
            self.students.edit(index, polozeni_predmet)
            return True
        elif index.column() == 1 and role == QtCore.Qt.EditRole: #broj indeksa
            polozeni_predmet.silabus = value
            self.students.edit(index, polozeni_predmet)
            return True
        elif index.column() == 2 and role == QtCore.Qt.EditRole: #broj indeksa
            polozeni_predmet.ocena = value
            self.students.edit(index, polozeni_predmet)
            return True
        return False

    def flags(self, index):
        return super().flags(index) | QtCore.Qt.ItemIsEditable #ili nad bitovima