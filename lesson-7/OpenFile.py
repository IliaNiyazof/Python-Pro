#!/usr/bin/python3
# -*- coding: utf-8 -*-
import argparse
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import (QMainWindow, QAction, QFileDialog, QApplication)
from PyQt5.QtGui import QPixmap, QIcon
from client.start_dialog import UserNameDialog

class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('-n', '--name', default=None, nargs='?')
        namespace = parser.parse_args(sys.argv[1:])
        client_name = namespace.name

        self.lbl = QtWidgets.QLabel(self)
        self.setGeometry(300, 300, 400, 300)

        openFile = QAction(QIcon('Python_pro\\OpenFile\\open.png'), 'Open', self)
        openFile.triggered.connect(self.showDialog)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('Фото')
        fileMenu.addAction(openFile)

        self.setWindowTitle(f'Фото профиля для - {client_name}')
        self.show()

    def showDialog(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', '/home')[0]
        pixmap = QPixmap(fname)
        self.lbl.resize(300, 300)
        self.lbl.setPixmap(pixmap)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
