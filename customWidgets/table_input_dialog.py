from PySide2 import QtGui, QtCore
from PySide2.QtWidgets import *
import sys
import asyncio


class InsertOneForm(QDialog):
    def __init__(self, metadata_columns, on_add_handler=None):
        super(InsertOneForm, self).__init__()
        self.temp_instance = None
        self.metadata_columns = metadata_columns
        self.data_asigned = []
        self.createFormGroupBox()
        self.on_add_handler = on_add_handler

        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.formGroupBox)
        # mainLayout.addWidget(buttonBox)
        self.setLayout(mainLayout)
        self.setWindowTitle("Insert Data To The Table")
        #self.final_data = []

    def createFormGroupBox(self):
        print(self.metadata_columns)
        self.formGroupBox = QGroupBox(
            "Populate the data needed for this table.")
        self.layout = QFormLayout()
        # metadata_columns = ["a", "b", "c", "d"]

        collect_button = QPushButton(self)
        collect_button.setText("Submit data")
        # TODO Srediti dugme i kupljenje podataka iz instanci koje se nalaze u ovom arrayu.
        self.input_array = []
        for column in self.metadata_columns:
            self.layout.addRow(QLabel(column),
                               self.append_instance(self.input_array))
        self.formGroupBox.setLayout(self.layout)
        self.layout.addRow(collect_button)

        collect_button.clicked.connect(
            lambda: self.assign_value(self.data_asigned))

    def assign_value(self, data_asigned):
        data_asigned = self.process_input_fields()

    def append_instance(self, metadata_columns):
        metadata_columns.append(self.create_QLineEdit_Instance())
        return self.temp_instance

    def create_QLineEdit_Instance(self):
        self.temp_instance = QLineEdit()
        return self.temp_instance

    # TODO Srediti porovjeru i ispravnost podataka, ne smije biti prazan string itd...
    def process_input_fields(self):
        final_data = []
        for input in range(0, len(self.input_array)):
            final_data.append(
                {self.metadata_columns[input]: self.input_array[input].displayText()})

        self.final_data = final_data
        self.on_add_handler()
        # for column_name in self.metadata_columns:
        #     if self.before_check_data[column_name] == "":
        #         popup_message = QMessageBox()
        #         popup_message.setWindowModality(QtCore.Qt.ApplicationModal)
        #         popup_message.setIcon(QMessageBox.Warning)
        #         popup_message.setText(
        #             "Input does not support an empty string. Please provide an appropriate value.")
        #         self.layout.addRow(popup_message)
        #         break


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = InsertOneForm(metadata_columns=["a", "b", "c", "d"])
    sys.exit(dialog.exec_())
