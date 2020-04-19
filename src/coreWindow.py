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
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem

"""
coreWindow.py

  created by:   Tim Clarke
  date:         11mar2020
  purpose:      main window control module
  arguments:    TODO instantion: none
  returns:      (TODO see methods)
"""

"""TODO"""
class QtTablePopulate():
    def __init__(self, widget, data):
        if data is not None and len(data):
            widget.setHorizontalHeaderLabels(data['colnames'])
            for rowNum, row in enumerate(data['data']):
                for colNum, element in enumerate(row):
                    item = QTableWidgetItem(element)
                    widget.setItem(colNum, rowNum, item)
            widget.resizeColumnsToContents()

class coreWindow(QMainWindow):
    beds = None
    monitorTypes = None
    modules = None
    patients = None
    staff = None

    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        uic.loadUi('files/mainwindow.ui', self)
        self.setWindowIcon(QtGui.QIcon('files/hospital.png'))
        self.setHandlers()

    """initial load of all database data into display tables"""
    def populateTables(self):
        QtTablePopulate(self.findChild(QTableWidget, "tblBed"), self.beds)
        QtTablePopulate(self.findChild(QTableWidget, "tblMonitorTypes"), self.monitortypes)
        QtTablePopulate(self.findChild(QTableWidget, "tblModules"), self.modules)
        QtTablePopulate(self.findChild(QTableWidget, "tblPatients"), self.patients)
        QtTablePopulate(self.findChild(QTableWidget, "tblStaff"), self.staff)

    """set up the window event handler functions"""
    def setHandlers(self):
        tblWidget = self.findChild(QTableWidget, 'tblShifts')
        if tblWidget is not None:
            tblWidget.setEnabled(False)
            tblWidget.clicked.connect(self.alert)

    def alert(self, index):
        """ argments: self=MainWindow, index=QModelIndex of clicked """
        print(index.row(), index.column())
