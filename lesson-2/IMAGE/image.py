#!/usr/bin/python3
# -*- coding: utf-8 -*-

import random
from PIL import Image, ImageDraw #Подключим необходимые библиотеки.
from PIL.ImageQt import ImageQt

import sys
from PyQt5.QtWidgets import (QWidget, QHBoxLayout,
    QLabel, QApplication)
from PyQt5.QtGui import QPixmap, QImage, qRgb


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):
        print("Выберите эффект: 0 - Оттенки серого, 1 - Негатив, 2 - Чёрно — белое изображение")
        mode = int(input('mode:'))
        image = Image.open("image.jpg")
        draw = ImageDraw.Draw(image)
        width = image.size[0]
        height = image.size[1]
        pix = image.load()

        if (mode == 0):
            for i in range(width):
                for j in range(height):
                    a = pix[i, j][0]
                    b = pix[i, j][1]
                    c = pix[i, j][2]
                    S = (a + b + c) // 3
                    draw.point((i, j), (S, S, S))
        if (mode == 1):
            for i in range(width):
                for j in range(height):
                    a = pix[i, j][0]
                    b = pix[i, j][1]
                    c = pix[i, j][2]
                    draw.point((i, j), (255 - a, 255 - b, 255 - c))
        if (mode == 2):
            factor = int(input('выберите на сколько черным должно быть(чем больше тем чернее):'))
            for i in range(width):
                for j in range(height):
                    a = pix[i, j][0]
                    b = pix[i, j][1]
                    c = pix[i, j][2]
                    S = a + b + c
                    if (S > (((255 + factor) // 2) * 3)):
                        a, b, c = 255, 255, 255
                    else:
                        a, b, c = 0, 0, 0
                    draw.point((i, j), (a, b, c))

        img_tmp = ImageQt(image.convert('RGBA'))

        hbox = QHBoxLayout(self)
        pixmap = QPixmap.fromImage(img_tmp)

        lbl = QLabel(self)
        lbl.setPixmap(pixmap)

        hbox.addWidget(lbl)
        self.setLayout(hbox)

        self.move(300, 200)
        self.setWindowTitle('Example')
        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
