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
from PyQt5 import QtGui, QtWidgets, uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QGridLayout, QWidget, QPushButton, \
     QLabel, QTableWidget, QTableWidgetItem, QInputDialog
from PyQt5.QtGui import QPainter, QBrush, QColor
from PyQt5.QtCore import Qt, QPoint 
# from PyQt5.QtGui import QIcon
# from PyQt5.QtCore import pyqtSlot


class mine(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        uic.loadUi('/tmp/qttest/mainwindow.ui', self)

if __name__ == '__main__':
   app = QApplication([])

   window = mine()
   window.show()

   sys.exit(app.exec_())
