from PySide2 import QtWidgets, QtGui, QtCore
from student import Student
from polozeni_predmet import PolozeniPredmet
from nepolozeni_predmet import NepolozeniPredmet
from student_model import StudentModel
from polozeni_predmet_model import PolozeniPredmetModel
from nepolozeni_predmet_model import NepolozeniPredmetModel
from serial_file_handler import SerialFileHandler


class WorkspaceWidget(QtWidgets.QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.main_layout = QtWidgets.QVBoxLayout()
        self.tab_widget = None
        self.create_tab_widget()

        self.student_model = self.create_student_dummy_model()
        # FIXME: privremeno kao atribut, posle se dobavlja na klik
        #self.polozeni_predmeti_model = self.create_polozeni_predmeti_model(self.student_model.students[0]) # za prvog studenta

        # tabele kao atributi a ne kao lokalne promenljive
        self.table1 = QtWidgets.QTableView(self.tab_widget)
        self.table1.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.table1.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.table1.setModel(self.student_model)

        self.subtable1 = QtWidgets.QTableView(self.tab_widget)
        self.subtable1.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.subtable1.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.table1.clicked.connect(self.student_selected)

        self.subtable2 = QtWidgets.QTableView(self.tab_widget)

        self.tab_widget.addTab(self.subtable1, QtGui.QIcon("icons8-edit-file-64.png"), "Polozeni predmeti")
        self.tab_widget.addTab(self.subtable2, QtGui.QIcon("icons8-edit-file-64.png"), "Nepolozeni predmeti")
    
        self.main_layout.addWidget(self.table1)
        self.main_layout.addWidget(self.tab_widget)
        self.setLayout(self.main_layout)

    def student_selected(self, index):
        model = self.table1.model()
        student = model.get_element(index)

        polozeni_predmeti_model = self.create_polozeni_predmeti_model(student)
        self.subtable1.setModel(polozeni_predmeti_model)

        nepolozeni_predmeti_model = self.create_nepolozeni_predmeti_model(student)
        self.subtable2.setModel(nepolozeni_predmeti_model)

        self.tab_widget.addTab(self.subtable1, QtGui.QIcon("icons8-edit-file-64.png"), "Polozeni predmeti")
        self.tab_widget.addTab(self.subtable2, QtGui.QIcon("icons8-edit-file-64.png"), "Nepolozeni predmeti")
        
    def create_table(self, rows, columns):
        table_widget = QtWidgets.QTableWidget(rows, columns, self)

        for i in range(rows):
            for j in range(columns):
                table_widget.setItem(i, j, QtWidgets.QTableWidgetItem("Celija " + str(i) + str(j)))
        labels = []
        for i in range(columns):
            labels.append("Kolona" + str(i))
        table_widget.setHorizontalHeaderLabels(labels)
        return table_widget   

    def create_tab_widget(self):
        self.tab_widget = QtWidgets.QTabWidget(self)
        self.tab_widget.setTabsClosable(True)
        self.tab_widget.tabCloseRequested.connect(self.delete_tab)

    def delete_tab(self, index):
        self.tab_widget.removeTab(index)

    def create_student_dummy_model(self):

        student_model = StudentModel()
        if len(student_model.students.get_all()) == 0:

            student_model.students.insert_many([
                    Student("2018270000", "Marko Markovic", [
                        PolozeniPredmet("SIMS","1", 10),
                        PolozeniPredmet("BP","11", 8),
                        PolozeniPredmet("TS","33", 9)
                    ],
                    [
                        NepolozeniPredmet("AR","ne", 1),
                        NepolozeniPredmet("WD","ef", 2),
                        NepolozeniPredmet("WP","efefe", 9)
                    ]),
                    Student("2018270001", "Janko Jankovic", [
                        PolozeniPredmet("OP","", 10),
                        PolozeniPredmet("OOP1","", 8),
                        PolozeniPredmet("OOP2","", 9)
                    ],
                    [
                        NepolozeniPredmet("SIMS","", 1),
                        NepolozeniPredmet("WD","", 2),
                        NepolozeniPredmet("TS","", 3)
                    ]),
                    Student("2018270002", "Petar Petrovic", [
                        PolozeniPredmet("AR","", 10),
                        PolozeniPredmet("WP","", 8),
                        PolozeniPredmet("WD","", 9)
                    ],
                    [
                        NepolozeniPredmet("OP","", 1),
                        NepolozeniPredmet("OOP1","", 2),
                        NepolozeniPredmet("OOP2","", 9)
                    ]),
                    Student("2018270003", "Sima Simic", [
                        PolozeniPredmet("DM","", 10),
                        PolozeniPredmet("EJ1","", 8),
                        PolozeniPredmet("MEN","", 9)
                    ]),
                    Student("2018270004", "Lazar Lazarevic")
                ])

        return student_model

    def create_polozeni_predmeti_model(self, student):
        """
        Za odabranog studenta pravi model za tabelu polozenih predmeta
        """
        polozeni_predmeti_model = PolozeniPredmetModel(self.student_model.students)
        polozeni_predmeti_model.polozeni_predmeti = student.polozeni_predmeti

        return polozeni_predmeti_model

    def create_nepolozeni_predmeti_model(self, student):
        """
        Za odabranog studenta pravi model za tabelu nepolozenih predmeta
        """
        nepolozeni_predmeti_model = NepolozeniPredmetModel(self.student_model.students)
        nepolozeni_predmeti_model.nepolozeni_predmeti = student.nepolozeni_predmeti

        return nepolozeni_predmeti_model