from PySide2.QtWidgets import QTableWidgetItem, QMainWindow, QApplication, QAction, QPushButton, QToolBar, QSplashScreen, QDockWidget, QFileSystemModel, QTreeView, QStatusBar, QWidget, QVBoxLayout, QTabWidget, QTableView, QTableWidget, QTableWidgetItem, QAbstractItemView, QLabel, QMessageBox, QToolTip
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
        self.delete_action_tb = QAction("Delete Table Row", self)
        self.delete_action_tb.setStatusTip("Delete Selected Table Row")
        self.delete_action_tb.triggered.connect(self.delete_table_row_tb)
        self.delete_action_tb.setIcon(QIcon("img/delete_icon.png"))
        self.delete_action_tb.priority()
        self.delete_action_tb.setStatusTip("Select the row to delete and press this button to delete it.")
        self.delete_action_tb.setWhatsThis("Select the row to delete and press this button to delete it.")
        self.delete_action_tb.setShortcut(QKeySequence.Delete)
        self.toolbar.addAction(self.delete_action_tb)
        
        # ADD ONE TOOLBAR BUTTON
        self.add_one_action_tb = QAction("Add Table Row", self)
        self.add_one_action_tb.setStatusTip("Add Single Table Row")
        self.add_one_action_tb.setToolTip("Add Table Row")
        self.add_one_action_tb.triggered.connect(self.add_table_row_handler)
        self.add_one_action_tb.setIcon(QIcon("img/add_row_icon.png"))
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
            

    def handleSubtables(self):
        index=(self.main_table.selectionModel().currentIndex().row())

        self.tabs = [QLabel("label1"), QLabel("label1"), QLabel("label1")]
        counter = 1
        for tab in self.tabs:
            self.subtables_tabwidget.addTab(tab, str(counter))
            counter += 1 
        print("Widget added")


    # TODO Srediti da funkcija bise element iz tabele klikom na dugme delete u ToolBar-u.
    def delete_table_row_tb(self):
        index=(self.main_table.selectionModel().currentIndex().row())
        if index == -1:
            self.choose_record_to_delete = QMessageBox()
            self.choose_record_to_delete.setIcon(QMessageBox.Warning)
            self.choose_record_to_delete.setWindowTitle("Message")
            self.choose_record_to_delete.setText("You have to select the record from the table which you want to be deleted.")
            self.choose_record_to_delete.setInformativeText("Then click 'DELETE TABLE ROW' button again.")
            okay_button = self.choose_record_to_delete.exec_()
            return
        else:
            print("You have chosen a record with number {}".format(index))    
            self.delete_message_box = QMessageBox()
            self.delete_message_box.setIcon(QMessageBox.Warning)
            self.delete_message_box.setWindowTitle("Warning!")
            self.delete_message_box.setText("Are you sure that you want to delete this record?")
            self.delete_message_box.setInformativeText("It will be deleted permanently.")
            self.delete_message_box.addButton(QMessageBox.StandardButton.Yes)
            self.delete_message_box.addButton(QMessageBox.StandardButton.No)
            self.delete_message_box.setDefaultButton(QMessageBox.StandardButton.No)
            button_pressed = self.delete_message_box.exec_()
            
            if button_pressed == QMessageBox.No:
                print("User doesn't want to delete a selected record from the table.")
            else:
                print("User wants to delete a selected record from the table. ")    
                # self.abstract_table_model.file_handler.delete_one(index)
                self.abstract_table_model.file_handler.delete_one(self.abstract_table_model.file_handler.data[index][self.abstract_table_model.file_handler.metadata[0]['key']])
                print("Record number {} successfuly deleted.".format(index))

    #?Works fine.
    def add_table_row_handler(self):
        self.addWindow = InsertOneForm(
            self.abstract_table_model.file_handler.metadata[0]["columns"], self.check_data)
        self.main_layout.addWidget(self.addWindow)
        self.add_one_action_tb.setEnabled(False)   

    # data validation
    #? Proveara kod unosa podataka
    def check_data(self):
        self.return_data = self.addWindow.final_data
        self.return_metadata = self.addWindow.metadata_columns
        not_valid = False                                      
        i = 0
        for data in self.return_data:
            if data.get(self.return_metadata[i]) == "" or data.get(self.return_metadata[i].strip()) == "" or data.get(self.return_metadata[i]) == None:
                not_valid = True
            else:
                print("Data input is valid.")
            i += 1

        if not_valid != True:
            #?Dict where user input data will be stored.
            to_add_dictionary = {}

            counter = 0
            while counter < len(self.addWindow.metadata_columns):
                print(self.addWindow.metadata_columns[counter])
                to_add_dictionary[self.addWindow.metadata_columns[counter]] = self.return_data[counter][self.addWindow.metadata_columns[counter]]
                counter += 1     

            #?Letting the file handler to insert that new instance which user provided input data for.
            self.abstract_table_model.file_handler.insert(to_add_dictionary)

            #?QMessageBox for alerting the user about successful adding of the new instance to the table.
            self.message_box = QMessageBox()
            self.message_box.setWindowTitle("Success!")
            self.message_box.setText("Successfuly added a record to the table.")
            self.message_box.setIcon(QMessageBox.Information)
            #?Showing QMessageBox.
            x = self.message_box.exec_()

            self.main_layout.removeWidget(self.addWindow)
            self.addWindow.deleteLater()
            self.addWindow = None

            #?Making the AddRow Action Enabled again after the new record is added to the table.
            self.add_one_action_tb.setEnabled(True)
        else:
            not_valid_box = QMessageBox()
            not_valid_box.setWindowTitle("Warning!")
            not_valid_box.setText("Input fields must have value and can not be empty.")
            not_valid_box.setIcon(QMessageBox.Information)
            show_not_valid_box = not_valid_box.exec_()

            self.main_layout.removeWidget(self.addWindow)
            self.addWindow.deleteLater()
            self.addWindow = None    
            self.add_one_action_tb.setEnabled(True)

    def check_database_type_and_run(self):
        if self.database_type == "serial" or self.database_type == "sequential":
            self.create_table()
        else:
            # TODO Obraditi izuzetak.
            pass

    def create_tab_widget(self):
        self.tab_widget = QTabWidget(self)
        self.tab_widget.setTabsClosable(True)
        self.tab_widget.isMovable()

        # makes responsive tabel sizes
    def create_table(self):
        self.main_table = QTableView(self.tab_widget)
        self.main_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.main_table.setSelectionMode(QAbstractItemView.SingleSelection)
        self.main_table.setModel(self.abstract_table_model)
        max_width = 1620 // self.abstract_table_model.column_number()
        for width in range(self.abstract_table_model.column_number()):
            self.main_table.setColumnWidth(width, max_width)

            

       
