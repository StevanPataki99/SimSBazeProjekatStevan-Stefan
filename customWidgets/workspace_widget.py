from PySide2.QtWidgets import QTableWidgetItem, QMainWindow, QApplication, QAction, QPushButton, QToolBar, QSplashScreen, QDockWidget, QFileSystemModel, QTreeView, QStatusBar, QWidget, QVBoxLayout, QTabWidget, QTableView, QTableWidget, QTableWidgetItem, QAbstractItemView, QLabel
from PySide2.QtGui import QKeySequence, QPixmap, QIcon
from PySide2.QtWidgets import QInputDialog, QLineEdit
from PySide2.QtCore import Qt, QDir, QObject, Signal
import sys
from customWidgets.models.abstract_table_model import AbstractTableModel
from customWidgets.models.abstract_subtable_model import AbstractSubtableModel
from customWidgets.table_input_dialog import InsertOneForm


class WorkSpaceWidget(QWidget):
    def __init__(self, parent, file_clicked):
        super().__init__(parent)
        self.main_layout = QVBoxLayout()
        # Tool Bar
        self.toolbar = QToolBar(self)
        # delete action on toolbar
        self.delete_action_tb = QAction("DELETE TABLE ROW", self)
        self.delete_action_tb.setStatusTip("Obrisi Red U Tabeli")
        self.delete_action_tb.triggered.connect(self.delete_table_row_tb)
        self.toolbar.addAction(self.delete_action_tb)

        # ADD ONE TOOLBAR BUTTON
        self.add_one_action_tb = QAction("ADD TABLE ROW", self)
        self.add_one_action_tb.setStatusTip("ADD SINGLE ROW TO TABLE")
        self.add_one_action_tb.triggered.connect(self.add_table_row_handler)
        self.toolbar.addAction(self.add_one_action_tb)

        self.setLayout(self.main_layout)
        self.file_clicked = file_clicked
        self.abstract_table_model = AbstractTableModel(self.file_clicked)
        self.database_type = self.abstract_table_model.database_type
        self.linked_files_lenght = len(self.abstract_table_model.file_handler.metadata[0]["linked_files"])
        self.create_tab_widget()
        self.check_database_type_and_run()
        self.tab_widget.addTab(self.main_table, QIcon(
            "img/iconXLNK.png"), self.file_clicked)
        self.main_layout.addWidget(self.toolbar)
        self.main_layout.addWidget(self.tab_widget)

        if self.linked_files_lenght != 0:
            self.init_tabs = False
            self.subtables_tabwidget = QTabWidget(self)
            self.subtables_tabwidget.setTabsClosable(True)  
            #! Row click Event Handler
            self.main_table.clicked.connect(self.getSubtableTabs)   
            self.main_layout.addWidget(self.subtables_tabwidget) 

    def getSubtableTabs(self):   
        for i in range(self.linked_files_lenght):
            self.subtables_tabwidget.removeTab(0)
        index = (self.main_table.selectionModel().currentIndex().row())

        for sub_tabel in self.abstract_table_model.file_handler.metadata[0]["linked_files"]:
            subtable_model = AbstractSubtableModel(sub_tabel, self.abstract_table_model.data_recieved[index])
            table = QTableView(self.subtables_tabwidget)
            table.setSelectionBehavior(QAbstractItemView.SelectRows)
            table.setSelectionMode(QAbstractItemView.SingleSelection)
            table.setModel(subtable_model)
            max_width = 1620 // subtable_model.column_number()
            for width in range(self.abstract_table_model.column_number()):
                table.setColumnWidth(width, max_width)
            self.subtables_tabwidget.addTab(table, sub_tabel)
            

    # TODO Srediti da funkcija bise element iz tabele klikom na dugme delete u ToolBar-u.
    def delete_table_row_tb(self):
        print("Ugraditi funkciju za brisanje reda iz tabele.")

    # TODO srediti dodavnje u tabelu.
    def add_table_row_handler(self):
        self.addWindow = InsertOneForm(
            self.abstract_table_model.file_handler.metadata[0]["columns"], self.check_data)
        self.main_layout.addWidget(self.addWindow)

        # chekiranje validnosti podataka
    
    #? Proveara kod unosa podataka
    def check_data(self):
        self.return_data = self.addWindow.final_data
        self.return_metadata = self.addWindow.metadata_columns
        not_valid = False
        i = 0
        for data in self.return_data:
            if data.get(self.return_metadata[i]) == "" or data.get(self.return_metadata[i]) == " " or data.get(self.return_metadata[i]) == None:
                print("Nije uredu")
                not_valid = True
            else:
                print("sve ok")
            i += 1

        if not_valid != True:
            self.new_instanc = SmartPhone(self.return_data[0]["brand"], self.return_data[1]["model"], self.return_data[2]["price"],
                                          self.return_data[3]["made_in"], self.return_data[4]["dealer"], self.return_data[5]["imei_code"], self.return_data[6]["stores"])
            self.abstract_table_model.file_handler.insert(self.new_instanc)

    def check_database_type_and_run(self):
        if self.database_type == "serial" or self.database_type == "sequential":
            self.create_table()
        else:
            # TODO Obraditi izuzetak.
            pass

    def create_tab_widget(self):
        self.tab_widget = QTabWidget(self)
        self.tab_widget.setTabsClosable(True)

        # makes responsive tabel sizes
    def create_table(self):
        self.main_table = QTableView(self.tab_widget)
        self.main_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.main_table.setSelectionMode(QAbstractItemView.SingleSelection)
        self.main_table.setModel(self.abstract_table_model)
        max_width = 1620 // self.abstract_table_model.column_number()
        for width in range(self.abstract_table_model.column_number()):
            self.main_table.setColumnWidth(width, max_width)

            

       
