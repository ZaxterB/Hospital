#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""MOD005622 TRI2 B01CAM"""
__author__ = "Tim Clarke/Zach Beed"
__copyright__ = "Copyright 2020, Tim Clarke/Zach Beed"
__license__ = "Private"
__version__ = "0.0.1"

"""
integrumfeed.py

  created by:   Tim Clarke
  date:         8jan2020
  change log:
  purpose:      test pyqt

                pseudo-code:
                  

  returns:
  errors:
  assumes:      
  side effects:
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

#Custom designed pyqtwidgets
#Daryl W. Bennett --kd8bny@gmail.com
#Purpose is to have a custom UI

#R1

from PyQt5.QtGui import QWidget


class speedowidget(QtGui.QWidget):

    speedChange = QtCore.pyqtSignal(int)

    def __init__(self, parent=None):
        super(speedowidget, self).__init__(parent)

        self.speedChange.connect(self.update)
        self.speedChange.connect(self.updateValue)

        self.setWindowTitle(QtCore.QObject.tr(self, "kd8bny Speedometer"))
        self.resize(200, 200)

        self.rect = QtCore.QRect(-50,-50,100,100)
        self.startAngle = 0 * 16
        self.spanAngle = 180 * 16     

        self.needle = QtGui.QPolygon([
            QtCore.QPoint(1, 0),
            QtCore.QPoint(0, 1),
            QtCore.QPoint(-1, 0),
            QtCore.QPoint(0, -50)
            ])

        self.backColor = QtGui.QColor('white')
        self.needleColor = QtGui.QColor('orange')
        self.tickColor = QtGui.QColor('red')

        self.speed = 0    

    def paintEvent(self, event):
        side = min(self.width(), self.height()) 
        qtpaint = QtGui.QPainter()

        qtpaint.begin(self)

        qtpaint.setRenderHint(QtGui.QPainter.Antialiasing)
        qtpaint.translate(self.width()/2, self.height()/2)
        qtpaint.scale(side / 120.0, side / 120.0)

        #Background
        qtpaint.setPen(QtGui.QColor('black'))
        qtpaint.setBrush(QtGui.QBrush(self.backColor))

        qtpaint.drawChord(self.rect, self.startAngle, self.spanAngle)
        qtpaint.save()

        #Needle
        qtpaint.setPen(QtCore.Qt.NoPen)
        qtpaint.setBrush(QtGui.QBrush(self.needleColor))
        qtpaint.rotate(-90 + (self.speed/10) * 15)
        
        qtpaint.drawConvexPolygon(self.needle)
        qtpaint.restore()

        #Tick marks
        qtpaint.setPen(self.tickColor)

        qtpaint.rotate(-15.0)
        for i in range(0, 11):
            qtpaint.drawLine(50, 0, 47, 0)
            qtpaint.rotate(-15.0)

        qtpaint.end()

        return

    @QtCore.pyqtSlot(int)
    def updateValue(self, speed):
        if speed >= 0 and speed <= 120:
            self.speed = speed
            self.update()

        return

if __name__ == "__main__":
    import sys

    app = QtGui.QApplication(sys.argv)
    widget = speedowidget()
    widget.show()
    widget.speedChange.emit(60)
    sys.exit(app.exec_())

def window():
   app = QApplication(sys.argv)
   widget = QWidget()
   
   button1 = QPushButton(widget)
   button1.setText("Button1")
   button1.move(64,32)
   button1.clicked.connect(button1_clicked)

   button2 = QPushButton(widget)
   button2.setText("Button2")
   button2.move(64,64)
   button2.clicked.connect(button2_clicked)

   widget.setGeometry(50,50,320,200)
   widget.setWindowTitle("PyQt5 Button Click Example")
   widget.show()
   sys.exit(app.exec_())


def button1_clicked():
   print("Button 1 clicked")

def button2_clicked():
   print("Button 2 clicked")   
   
if __name__ == '__main__':
   window()
