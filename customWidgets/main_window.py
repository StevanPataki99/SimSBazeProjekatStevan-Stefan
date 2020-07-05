from PySide2.QtWidgets import QMainWindow, QApplication, QAction, QPushButton, QToolBar, QSplashScreen, QDockWidget, QFileSystemModel, QTreeView, QStatusBar, QLabel, QMessageBox, QFileIconProvider
from PySide2.QtGui import QKeySequence, QPixmap, QIcon
from PySide2.QtCore import Qt, QDir
import sys
import os
from customWidgets.workspace_widget import WorkSpaceWidget
from customWidgets.fili_icon_provider import FileIconProvider


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # SET => App Icon
        self.icon = QIcon("img/iconXLNK.png")
        # End

        self.tree_view = None
        self.file_system_model = None
        # SET => Window Icon
        self.setWindowIcon(self.icon)
        # End
        # WSET => Window Title
        self.setWindowTitle("XLNK | Data Manager")
        # End

        # Menus
        self.menu = self.menuBar()
        self.file_menu = self.menu.addMenu("&File")
        self.edit_menu = self.menu.addMenu("&Edit")
        self.view_menu = self.menu.addMenu("&View")
        self.help_menu = self.menu.addMenu("&Help")
        # End

        # ===================
        # Menu Button Actions
        
        # Exit QAction File Menu
        exit_action = QAction("Exit", self)
        exit_action.setShortcut(QKeySequence.Quit)
        exit_action.triggered.connect(self.close)
        self.file_menu.addAction(exit_action)

        toggle_docker_action = QAction("Show/Hide Docker View")
        toggle_docker_action.setShortcut(QKeySequence.WhatsThis)
        toggle_docker_action.triggered.connect(self.toggle_docker_widget)
        self.file_menu.addAction(toggle_docker_action)
        

        


        # Dock Widget
        dock_widget = QDockWidget("EXPLORER", self)
        # File System Model
        self.file_system_model = QFileSystemModel()
        #Setting icons for binary files.
        self.file_system_model.setIconProvider(FileIconProvider())


        self.file_system_model.setRootPath(QDir.currentPath())
        # SET => Tree View MOdel
        self.tree_view = QTreeView()
        self.tree_view.setModel(self.file_system_model)
        self.tree_view.setRootIndex(
            self.file_system_model.index(QDir.currentPath() + "/data"))
        
        self.tree_view.clicked.connect(self.file_clicked_handler)
        dock_widget.setWidget(self.tree_view)
        dock_widget.setFloating(False)
        self.addDockWidget(Qt.LeftDockWidgetArea, dock_widget)

        # QLabel
        qlabel = QLabel(self)
        qlabel.setText("Welcome to XLNK.")

        # Central Widget
        self.clicked_file = None

        self.setCentralWidget(qlabel)

        self.showMaximized()
    def toggle_docker_widget(self):
            pass
    # ToolBar Functions
    # TODO
    def delete_table_row_tb(self):
        print("Ugraditi funkciju za brisanje reda iz tabele.")

    def file_clicked_handler(self, index):
        index = self.tree_view.currentIndex()
        file_clicked_param = os.path.basename(
            self.file_system_model.filePath(index))
        self.clicked_file = file_clicked_param
        self.status_bar = QStatusBar(self)
        self.status_bar.showMessage(
            "File Selected: {}".format(file_clicked_param), 3000)
        self.setStatusBar(self.status_bar)
        self.workspace_widget = WorkSpaceWidget(self, self.clicked_file)
        self.setCentralWidget(self.workspace_widget)
