import PyQt5
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QImage
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5 import QtCore, QtGui, QtWidgets
import cv2
import sys
import os
from PIL import Image
from extension import *


class HEPP(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.ui = uic.loadUi("main.ui", self)
        self.ui.label_general.setStyleSheet("background-image : url(label_general.png)")
        self.ui.label_headpond.setStyleSheet("background-image : url(label_headpond.png)")
        self.ui.label_generator.setStyleSheet("background-image : url(label_generator.png)")
        self.ui.label_other.setStyleSheet("background-image : url(label_other.png)")
        self.ui.pushButton_general.clicked.connect(self.open_general)
        self.ui.pushButton_generator.clicked.connect(self.open_generator)
        self.ui.pushButton_headpond.clicked.connect(self.open_headpond)
        self.ui.pushButton_other.clicked.connect(self.open_other)

        self.ui.pushButton_trends.clicked.connect(self.open_trends)

        self.ui.scrollArea_trends = QScrollArea()
        self.ui.scrollArea_trends.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.ui.scrollArea_trends.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.ui.scrollArea_trends.setWidgetResizable(True)
        # comboBox_scheme
    def open_general(self):
        self.window_ext = QtWidgets.QMainWindow()
        self.ui1 =ui_mainWindow_ext()
        self.ui1.setup_general(self.window_ext)
        self.window_ext.show()
    def open_generator(self):
        self.window_ext = QtWidgets.QMainWindow()
        self.ui1 = ui_mainWindow_ext()
        self.ui1.setup_generator(self.window_ext)
        self.window_ext.show()
    def open_headpond(self):
        self.window_ext = QtWidgets.QMainWindow()
        self.ui1 = ui_mainWindow_ext()
        self.ui1.setup_headpond(self.window_ext)
        self.window_ext.show()
    def open_other(self):
        self.window_ext = QtWidgets.QMainWindow()
        self.ui1 = ui_mainWindow_ext()
        self.ui1.setup_other(self.window_ext)
        self.window_ext.show()

    def open_trends(self):
        filename = QFileDialog.getOpenFileName(self, 'Open a file', 'Trends/',
                                               'All Image Files (*.png;*.jpg;*.jpeg;*.jpe;*.jfif)')
        self.image = cv2.imread(str(filename[0]))
        if self.image is None:
            return QMainWindow
        frame = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)
        image = QImage(frame, frame.shape[1], frame.shape[0], frame.strides[0], QImage.Format_RGB888)
        self.ui.label_trends.setPixmap(QPixmap.fromImage(image))


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        import time
        splash = QSplashScreen()
        splash.setPixmap(QPixmap('icon.ico'))
        splash.show()
        time.sleep(5)

app = QtWidgets.QApplication(sys.argv)
mainWindow = HEPP()
window = Window()
mainWindow.showMaximized()
sys.exit(app.exec_())
