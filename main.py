from PySide2.QtWidgets import QApplication, QSplashScreen, QStyleFactory
from PySide2.QtGui import QPixmap
from customWidgets.main_window import MainWindow
from PySide2 import QtGui
import sys
import time

if __name__ == "__main__":
    app = QApplication(sys.argv)
    pixmap = QPixmap("img/xlnk-transparent.png")
    splash = QSplashScreen(pixmap)
    splash.show()
    time.sleep(1)
    window = MainWindow()
    app.exec_()
    app.exit()
