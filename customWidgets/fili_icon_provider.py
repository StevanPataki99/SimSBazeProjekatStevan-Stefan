from PySide2.QtWidgets import QMainWindow, QApplication, QAction, QPushButton, QToolBar, QSplashScreen, QDockWidget, QFileSystemModel, QTreeView, QStatusBar, QLabel, QMessageBox, QFileIconProvider
from PySide2.QtGui import QKeySequence, QPixmap, QIcon
from PySide2.QtCore import Qt, QDir, QFileInfo
import sys
import os
from customWidgets.workspace_widget import WorkSpaceWidget


class FileIconProvider(QFileIconProvider):
    def icon(self, parameter):
        if isinstance(parameter, QFileInfo):
            info = parameter
            if info.suffix() == "":
                return QIcon("img/bfiles_icon.png")
        return super(FileIconProvider, self).icon(parameter)