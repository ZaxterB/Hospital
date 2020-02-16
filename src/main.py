#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""MOD005622 TRI2 B01CAM"""
__author__ = "Tim Clarke/Zach Beed"
__copyright__ = "Copyright 2020, Tim Clarke/Zach Beed"
__license__ = "Private"
__version__ = "0.0.2"

"""
test.py

  created by:   Tim Clarke

    Icons made by <a href="https://www.flaticon.com/authors/freepik" title="Freepik">Freepik</a> from
      <a href="https://www.flaticon.com/" title="Flaticon"> www.flaticon.com</a>

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
from PyQt5.QtWidgets import QApplication, QMainWindow


class mine(QMainWindow):
  def __init__(self, parent=None):
    QMainWindow.__init__(self, parent)
    uic.loadUi('files/mainwindow.ui', self)
    self.setWindowIcon(QtGui.QIcon('files/hospital.png'))

if __name__ == '__main__':
  app = QApplication([])

  window = mine()
  window.show()

  tblWidgets = window.findChildren(QtWidgets.QTableWidget)
  for wdg in tblWidgets:
    print(wdg.objectName())
  
  sys.exit(app.exec_())
