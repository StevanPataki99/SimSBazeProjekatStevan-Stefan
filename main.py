from PySide2.QtWidgets import QApplication, QSplashScreen, QStyleFactory, QLabel
from PySide2.QtGui import QPixmap, QMovie
from customWidgets.main_window import MainWindow
from PySide2 import QtGui
import sys
import time
from pyside_material import apply_stylesheet

if __name__ == "__main__":
    app = QApplication(sys.argv)
    pixmap = QPixmap("img/xlnk-transparent.png")
    splash = QSplashScreen(pixmap)
    splash.show()
    time.sleep(1)
    window = MainWindow()
    apply_stylesheet(app, theme='dark_teal.xml')
    app.exec_()
    app.exit()
