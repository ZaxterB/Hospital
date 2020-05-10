#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""MOD005622 TRI2 B01CAM"""
__author__ = "Tim Clarke"
__copyright__ = "Copyright 2020, Tim Clarke/Zach Beed"
__license__ = "Private"
__version__ = "0.0.5"

# python modules
import sys
import threading
# app-specific constants
import constants
# app-specific database interface class
from db import Db
# app-specific objects
from bed import Beds, Bed
from module import Modules, Module
from monitortype import MonitorTypes, MonitorType
from patient import Patients, Patient
from staff import Staffs, Staff
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

class coreWindow(QMainWindow):
    beds = None
    monitorTypes = None
    modules = None
    patients = None
    staff = None
    timer = None

    def __init__(self, db, parent=None):
        QMainWindow.__init__(self, parent)
        uic.loadUi('files/mainwindow.ui', self)
        self.setWindowIcon(QtGui.QIcon('files/hospital.png'))
        # initially load all classes from database
        self.loadTables(db)
        # show them to the user
        self.populateTables()
        # set up user interaction mechanisms
        self.setHandlers()
        # now begin to react
        self.setTimer()

    def loadTables(self, db):
        """initial load of all database data"""
        self.beds = Beds(db).getBeds()
        self.monitortypes = MonitorTypes(db).getMonitorTypes()
        self.modules = Modules(db).getModules()
        self.patients = Patients(db).getPatients()
        self.staff = Staffs(db).getStaff()

    def populateTables(self):
        """initial load of all database data into display tables"""
        self.QtTablePopulate(self.findChild(QTableWidget, "tblBed"), self.beds)
        self.QtTablePopulate(self.findChild(QTableWidget, "tblMonitorTypes"), self.monitortypes)
        self.QtTablePopulate(self.findChild(QTableWidget, "tblModules"), self.modules)
        self.QtTablePopulate(self.findChild(QTableWidget, "tblPatients"), self.patients)
        self.QtTablePopulate(self.findChild(QTableWidget, "tblStaff"), self.staff)

    def QtTablePopulate(self, widget, data):
        if data is not None and len(data):
            # display column titles
            widget.setHorizontalHeaderLabels(data[0].displayTitles())

            for rowNum, row in enumerate(data):
                # add a row to the display widget
                widget.setRowCount(widget.rowCount() + 1)

                # now iterate over the columns for the object
                for colNum, element in enumerate(row.display()):
                    item = QTableWidgetItem(str(element))
                    widget.setItem(rowNum, colNum, item)
            widget.resizeColumnsToContents()

    def setHandlers(self):
        """set up the window event handler functions"""
        tblWidget = self.findChild(QTableWidget, 'tblShifts')
        if tblWidget is not None:
            tblWidget.setEnabled(False)
            tblWidget.clicked.connect(self.alert)

    def close(self):
        """shut down timers"""
        self.timer.cancel()

    def alert(self, index):
        """ TODO EXPERIMENTAL
            argmuents: self=MainWindow, index=QModelIndex of clicked """
        print(index.row(), index.column())

    def pulse(self):
        print('test')
        self.setTimer()

    def setTimer(self):
        self.timer = threading.Timer(2.0, self.pulse)
        self.timer.start()