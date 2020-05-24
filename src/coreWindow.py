#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""MOD005622 TRI2 B01CAM"""
__author__ = "Tim Clarke"
__copyright__ = "Copyright 2020, Tim Clarke/Zach Beed"
__license__ = "Private"
__version__ = "0.0.8"

# python modules
import sys
import threading
from datetime import datetime, timedelta
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
from shift import Shifts, Shift
from testfile import TestFile
from alarm import Alarm
# PyQt libraries
from PyQt5 import QtGui, uic, QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem

"""
coreWindow.py

  created by:   Tim Clarke
  date:         11mar2020
  purpose:      main window control module
"""

class coreWindow(QMainWindow):
    """private variables"""
    _db = None # database object
    _beds = None
    _monitorTypes = None
    _modules = None
    _patients = None
    _staff = None
    _shifts = None
    _testfile = None
    _alarm = None
    _timer = None

    def __init__(self, db, testFileName, parent=None):
        self._db = db
        QMainWindow.__init__(self, parent)
        uic.loadUi(constants.GRAPHICAL_FILES + 'mainwindow.ui', self)
        self.setWindowIcon(QtGui.QIcon(constants.GRAPHICAL_FILES + 'hospital.png'))

        # initially load all classes from database
        self.loadTables(db)

        # show them to the user
        self.populateTables()

        # set up user interaction mechanisms
        self.setHandlers()

        # open test file if supplied

        if testFileName is not None:
            self._testfile = TestFile(testFileName)

        # now begin to react
        self.setTimer()
        self._alarm = Alarm()

    def loadTables(self, db):
        """initial load of all database data"""
        self._beds = Beds(db).getBeds()
        self._monitortypes = MonitorTypes(db).getMonitorTypes()
        self._modules = Modules(db).getModules()
        self._patients = Patients(db).getPatients()
        self._staff = Staffs(db).getStaff()
        self._shifts = Shifts(db).getShifts()

    def populateTables(self):
        """initial load of all database data into display tables"""
        # self.QtTablePopulate(self.findChild(QTableWidget, "tblBeds"), self._beds)
        self.bedsPopulate(self._beds)
        self.QtTablePopulate(self.findChild(QTableWidget, "tblMonitorTypes"), self._monitortypes)
        self.QtTablePopulate(self.findChild(QTableWidget, "tblModules"), self._modules)
        # self.QtTablePopulate(self.findChild(QTableWidget, "tblPatients"), self._patients)
        self.QtTablePopulate(self.findChild(QTableWidget, "tblStaff"), self._staff)
        self.QtTablePopulate(self.findChild(QTableWidget, "tblShifts"), self._shifts)

    def QtTablePopulate(self, widget, data):
        """given a Qt window widget object and a one of our data objects, display the latter in the former"""
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
            widget.resizeRowsToContents()

    def setHandlers(self):
        """set up the window event handler functions"""
        tblWidget = self.findChild(QTableWidget, 'tblShifts')
        if tblWidget is not None:
            tblWidget.setEnabled(False)
            tblWidget.clicked.connect(self.alert)
        self.findChild(QtWidgets.QPushButton, "Register").clicked.connect(self.createregistrationDialog)

    def close(self):
        """shut down timers"""
        self._timer.cancel()

    def alert(self, index):
        """ TODO EXPERIMENTAL
            argmuents: self=MainWindow, index=QModelIndex of clicked """
        print(index.row(), index.column())

    def pulse(self):
        # set the timer off again
        self.setTimer()

        # if we have test file data, process the next row
        if self._testfile:
            try:
                data = next(self._testfile)
                # validate
                if len(data) != 3:
                    print('Error in pulse(): Row {} in test data file does not contain exactly three values'.format(data))
                # find the bed
                bed = Beds(self._db).getBed(int(data[0]))
                if not bed:
                    print('Error in pulse(): Column 1 in row {} in test data file does not contain a valid bedid'.format(data))
                # inject the test data value into the monitor
                print("setting monitortypeid = " + data[1] + " newvalue = " + data[2])
                bed.setMonitorTypeValue(monitortypeid = int(data[1]), newvalue = int(data[2]))
            except StopIteration:
                # test data file finished, ignore gracefully
                pass
            except:
                exc_type, exc_value, exc_traceback = sys.exc_info()
                raise RuntimeError("Error in main(): {0} at line {1}".
                                   format(str(exc_value), str(exc_traceback.tb_lineno)))

    def setTimer(self):
        """ start a timer to run the pulse function """
        self._timer = threading.Timer(constants.PULSE_TIME, self.pulse)
        self._timer.start()

    def bedsPopulate(self, beds):
        for bed in beds:
            self.verticalLayout.addWidget(bed.UI(self.scrollAreaWidgetContents))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

    def createregistrationDialog(self):
        Dialog = registrationDialog(self)
        Dialog.show()

class registrationDialog(QtWidgets.QDialog):
    """private variables"""
    _db = None  # database object
    _staff = None



    def __init__(self, parent):
        self._db = parent._db
        self._staff = parent._staff
        QtWidgets.QDialog.__init__(self, parent)
        uic.loadUi(constants.GRAPHICAL_FILES + 'shift.ui', self)
        self.setWindowIcon(QtGui.QIcon(constants.GRAPHICAL_FILES + 'hospital.png'))
        self.UI()

    def submit(self):
        start = self.findChild(QtWidgets.QDateTimeEdit, "dteStart").dateTime().toPyDateTime()
        end = self.findChild(QtWidgets.QDateTimeEdit, "dteEnd").dateTime().toPyDateTime()
        staffname = self.findChild(QtWidgets.QComboBox,"cboStaff").currentText()
        staffid = staffname.split(":")[0] # this feels crude but people need to see their name and id
        self._db.insert("""
                    INSERT INTO public.shift (staffid, start, currentend)
                    VALUES ({id}, '{start}', '{end}')
                    """.format(id=staffid, start=str(start), end=str(end)))

    def calculateHrs(self):
        startTime = self.findChild(QtWidgets.QDateTimeEdit, "dteStart")
        endTime = self.findChild(QtWidgets.QDateTimeEdit, "dteEnd")
        delta = endTime.dateTime().toPyDateTime() - startTime.dateTime().toPyDateTime()
        if delta.total_seconds() < 0: # time travelers are better employed in physics institutes than medical ones
            startTime.setDateTime(QtCore.QDateTime.currentDateTime())
            endTime.setDateTime(QtCore.QDateTime.currentDateTime())
        else:
            self.findChild(QtWidgets.QLabel, "lblHours").setText(str(delta))


    def UI(self):
        staffList = self.findChild(QtWidgets.QComboBox, "cboStaff")
        staffList.addItems(str(staff._staffid) + ":" + staff._name for staff in self._staff)
        startTime = self.findChild(QtWidgets.QDateTimeEdit, "dteStart")
        startTime.setDateTime(QtCore.QDateTime.currentDateTime())
        startTime.dateTimeChanged.connect(self.calculateHrs)
        endTime = self.findChild(QtWidgets.QDateTimeEdit, "dteEnd")
        endTime.setDateTime(QtCore.QDateTime.currentDateTime())
        endTime.dateTimeChanged.connect(self.calculateHrs)
        buttonbox = self.findChild(QtWidgets.QDialogButtonBox, "buttonBox")
        buttonbox.accepted.connect(self.submit)
        buttonbox.rejected.connect(self.close)