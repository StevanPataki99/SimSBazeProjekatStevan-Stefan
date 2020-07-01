from PySide2.QtWidgets import QHBoxLayout, QMainWindow, QApplication, QAction, QPushButton, QToolBar, QSplashScreen, QDockWidget, QFileSystemModel, QTreeView, QStatusBar, QWidget, QVBoxLayout, QTabWidget, QTableView, QTableWidget, QTableWidgetItem, QAbstractItemView, QLabel
from PySide2.QtGui import QKeySequence, QPixmap, QIcon
from PySide2.QtWidgets import QInputDialog, QLineEdit
from PySide2.QtCore import Qt, QDir
import sys



class SubtablesWidget(QWidget):
    def __init__(self, parent, row_index, abs_table_model):
        super().__init__(parent)
        self.main_layout = QVBoxLayout()
        self.abs_table_model = abs_table_model
        self.metadata = self.abs_table_model.file_handler.metadata
        self.data = self.abs_table_model.data_recieved
        self.linked_files_length = len(self.metadata[0]["linked_files"])
        self.tabs = [QLabel("label1"), QLabel("label1"), QLabel("label1")]
        self.tab_widget = QTabWidget(self)
        self.tab_widget.setTabsClosable(True)
        self.asd()
        self.main_layout.addWidget(self.tab_widget)

    def asd(self):
        counter = 1
        for tab in self.tabs:
            self.tab_widget.addTab(tab, str(counter))
            counter += 1   
        






        


        

