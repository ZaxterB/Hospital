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
    _timer = None

    def __init__(self, db, testFileName, parent=None):
        self._db = db
        QMainWindow.__init__(self, parent)
        uic.loadUi('files/mainwindow.ui', self)
        self.setWindowIcon(QtGui.QIcon('src/files/hospital.png'))
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
        for bed in self._beds:
            print("bed:" + str(bed._bedid))
            self.BedUI(bed)
        self.QtTablePopulate(self.findChild(QTableWidget, "tblMonitorTypes"), self._monitortypes)
        self.QtTablePopulate(self.findChild(QTableWidget, "tblModules"), self._modules)
        self.QtTablePopulate(self.findChild(QTableWidget, "tblPatients"), self._patients)
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

    def close(self):
        """shut down timers"""
        self.timer.cancel()

    def alert(self, index):
        """ TODO EXPERIMENTAL
            argmuents: self=MainWindow, index=QModelIndex of clicked """
        print(index.row(), index.column())

    def pulse(self):
        # set the timer off again since
        self.setTimer()
        # TODO
        if self._testfile:
            try:
                data = next(self._testfile)
                # validate
                if len(data) != 3:
                    print('Error in pulse(): Row {} in test data file does not contain exactly three values'.format(data))
                # inject the value
                bed = Beds(self._db).getBed(int(data[0]))
                if not bed:
                    print('Error in pulse(): Column 1 in row {} in test data file does not contain a valid bedid'.format(data))
                bed.setMonitorTypeValue(int(data[1]), int(data[2]))
            except StopIteration:
                # test data file finished, ignore gracefully
                pass
            except:
                exc_type, exc_value, exc_traceback = sys.exc_info()
                raise RuntimeError("Error in main(): {0} at line {1}".
                                   format(str(exc_value), str(exc_traceback.tb_lineno)))

    def setTimer(self):
        """ start a timer to run the pulse function """
        self.timer = threading.Timer(constants.PULSE_TIME, self.pulse)
        self.timer.start()

    def BedUI(self, bed):
        #TODO add bedid into all relevant names and start inserting bed data
        self.BedGroupBox = QtWidgets.QGroupBox(self.layoutWidget)
        self.BedGroupBox.setMinimumSize(QtCore.QSize(849, 120))
        self.BedGroupBox.setObjectName("BedGroupBox")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.BedGroupBox)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(100, 20, 741, 381))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.BedAlarm = QtWidgets.QRadioButton(self.BedGroupBox)
        self.BedAlarm.setGeometry(QtCore.QRect(0, 20, 101, 20))
        self.BedAlarm.setObjectName("BedAlarm")
        self.BedCritAlarm = QtWidgets.QRadioButton(self.BedGroupBox)
        self.BedCritAlarm.setGeometry(QtCore.QRect(0, 40, 101, 20))
        self.BedCritAlarm.setObjectName("BedCritAlarm")
        self.BedAddModule = QtWidgets.QPushButton(self.BedGroupBox)
        self.BedAddModule.setGeometry(QtCore.QRect(0, 60, 101, 32))
        self.BedAddModule.setObjectName("BedAddModule")
        self.verticalLayout.addWidget(self.BedGroupBox)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.BedAlarm.setText(QtCore.QCoreApplication.translate("MainWindow", "Alarm"))
        self.BedCritAlarm.setText(QtCore.QCoreApplication.translate("MainWindow", "CritAlarm"))
        self.BedAddModule.setText(QtCore.QCoreApplication.translate("MainWindow", "Add Module"))
        self.BedGroupBox.setTitle(QtCore.QCoreApplication.translate("MainWindow", "Bed: " + str(bed._bedid)))

        #call children into view
        for mod in bed._modules:
            self.ModuleUI(mod, self.verticalLayout_2)

    def ModuleUI(self, module, VL2):
        # TODO add bedid into all relevant names and start inserting bed data
        self.ModulemonitorsGroupBox = QtWidgets.QGroupBox(self.verticalLayoutWidget)
        self.ModulemonitorsGroupBox.setObjectName("ModulemonitorsGroupBox")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.ModulemonitorsGroupBox)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(0, 20, 761, 361))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.ModulemonitorsGroupBox.setTitle(QtCore.QCoreApplication.translate("MainWindow", module._modulename))
        VL2.addWidget(self.ModulemonitorsGroupBox)
        print(module._modulename)
        print("length " + str(len(module._monitortypes)))
        for monitor in module._monitortypes:
            print(monitor._monitortype._name)
            self.MonitorUI(monitor, self.verticalLayout_3)

    def MonitorUI(self, monitor, VL3):
        # TODO add bedid into all relevant names and start inserting bed data
        self.MonitorGroupBox = QtWidgets.QGroupBox(self.verticalLayoutWidget_2)
        self.MonitorGroupBox.setObjectName("MonitorGroupBox")
        self.MonitorValueScale = QtWidgets.QProgressBar(self.MonitorGroupBox)
        self.MonitorValueScale.setGeometry(QtCore.QRect(0, 20, 118, 23))
        self.MonitorValueScale.setProperty("value", 24)
        self.MonitorValueScale.setObjectName("MonitorValueScale")
        self.MonitorCurrentValue = QtWidgets.QLCDNumber(self.MonitorGroupBox)
        self.MonitorCurrentValue.setGeometry(QtCore.QRect(130, 20, 64, 23))
        self.MonitorCurrentValue.setProperty("value", 30000.0)
        self.MonitorCurrentValue.setObjectName("MonitorCurrentValue")
        self.MonitorUnits = QtWidgets.QTextBrowser(self.MonitorGroupBox)
        self.MonitorUnits.setGeometry(QtCore.QRect(200, 20, 91, 23))
        self.MonitorUnits.setObjectName("MonitorUnits")
        self.MonitorAlarm = QtWidgets.QRadioButton(self.MonitorGroupBox)
        self.MonitorAlarm.setGeometry(QtCore.QRect(300, 20, 100, 20))
        self.MonitorAlarm.setObjectName("MonitorAlarm")
        self.MonitorCritAlarm = QtWidgets.QRadioButton(self.MonitorGroupBox)
        self.MonitorCritAlarm.setGeometry(QtCore.QRect(400, 20, 100, 20))
        self.MonitorCritAlarm.setObjectName("MonitorCritAlarm")
        self.MonitorGroupBox.setTitle(QtCore.QCoreApplication.translate("MainWindow", str(monitor._monitortype._name)))
        VL3.addWidget(self.MonitorGroupBox)