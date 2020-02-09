#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""MOD005622 TRI2 B01CAM"""
__author__ = "Tim Clarke/Zach Beed"
__copyright__ = "Copyright 2020, Tim Clarke/Zach Beed"
__license__ = "Private"
__version__ = "0.0.1"

"""
test.py

  created by:   Tim Clarke
  date:         8jan2020
  change log:
  purpose:      testing of pyqt

                pseudo-code:
                  

  returns:
  errors:
  assumes:      
  side effects:
"""

import sys
from PyQt5 import QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel
from PyQt5.QtGui import QPainter, QBrush, QColor
from PyQt5.QtCore import Qt, QPoint 
# from PyQt5.QtGui import QIcon
# from PyQt5.QtCore import pyqtSlot


class MainWindow(QWidget):
   def __init__(self):
      super().__init__()
      self.initWindow()

   def initWindow(self):
      self.setGeometry(100,100,400,280)
      self.setWindowTitle("PyQt5 testbed")
      self.show()

   def paintEvent(self, event):
      qp = QPainter()
      qp.begin(self)
      app.setStyle('Fusion')
      widget = QWidget(self)
      
      button1 = QPushButton(widget)
      button1.setText("Button1")
      button1.move(64,32)
      button1.clicked.connect(button1_clicked)

      button2 = QPushButton(widget)
      button2.setText("Button2")
      button2.move(64,64)
      button2.clicked.connect(button2_clicked)

      label = QLabel(widget)
      font = QtGui.QFont()
      font.setBold(True)
      label.setFont(font)
      label.setText('example')

      qp = QPainter(widget)
      qp.begin(self)
      colour = QColor(0, 0, 0)
      colour.setNamedColor('#d4d4d4')
      qp.setPen(colour)
      qp.setBrush(QColor(200, 0, 0))
      qp.drawRect(250, 100, 50, 50)
      qp.end()

      widget.show()



def button1_clicked():
   print("Button 1 clicked")



def button2_clicked():
   print("Button 2 clicked")



if __name__ == '__main__':
   app = QApplication(sys.argv)
   ex = MainWindow()
   sys.exit(app.exec_())
