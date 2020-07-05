from PySide2.QtWidgets import QTableWidgetItem, QMainWindow, QApplication, QAction, QPushButton, QToolBar, QSplashScreen, QDockWidget, QFileSystemModel, QTreeView, QStatusBar, QWidget, QVBoxLayout, QTabWidget, QTableView, QTableWidget, QTableWidgetItem, QAbstractItemView, QLabel, QMessageBox, QToolTip
from PySide2.QtGui import QKeySequence, QPixmap, QIcon, QPicture
from PySide2.QtWidgets import QInputDialog, QLineEdit
from PySide2.QtCore import Qt, QDir, QObject, Signal
import sys
from customWidgets.models.abstract_table_model import AbstractTableModel
from customWidgets.models.abstract_subtable_model import AbstractSubtableModel
from customWidgets.table_input_dialog import InsertOneForm



class LandingPageWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.main_layout = QVBoxLayout()
        # QLabel
        self.qlabel = QLabel(self)
        self.qlabel.setText("Welcome to XLNK.")
        self.qlabel.pixmap()
        self.main_layout.addWidget(self.qlabel)
        
        

