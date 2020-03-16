#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""MOD005622 TRI2 B01CAM"""
__author__ = "Tim Clarke"
__copyright__ = "Copyright 2020, Tim Clarke/Zach Beed"
__license__ = "Private"
__version__ = "0.0.0"

import sys
# app-specific constants
import constants
# app-specific database interface class
from db import Db
# app-specific objects
from bed import Bed
from monitortype import MonitorType
from patient import Patient
from staff import Staff
# PyQt libraries
from PyQt5 import QtGui, uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget

"""
coreWindow.py

  created by:   Tim Clarke
  date:         11mar2020
  purpose:      main window control module
  arguments:    instantion: none
  returns:      (see methods)
"""

beds = None
monitorTypes = None
patients = None
staff = None

class coreWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        uic.loadUi('files/mainwindow.ui', self)
        self.setWindowIcon(QtGui.QIcon('files/hospital.png'))
        self.setHandlers()

    def setHandlers(self):
        tblWidget = self.findChild(QTableWidget, 'tblShifts')
        if tblWidget is not None:
            tblWidget.setEnabled(False)
            tblWidget.clicked.connect(self.alert)

    def alert(self, index):
        """ argments: self=MainWindow, index=QModelIndex of clicked """
        print(index.row(), index.column())
