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
            self.BedUI(bed)
        # self.BedUI(self._beds[0])
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
        BedGroupBox = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        BedGroupBox.setFixedWidth(849)
        BedGroupBox.setObjectName("BedGroupBox" + str(bed._bedid))
        BedGroupBox.setTitle(QtCore.QCoreApplication.translate("MainWindow", "Bed: " + str(bed._bedid)))
        verticalLayoutWidget = QtWidgets.QWidget(BedGroupBox)
        verticalLayoutWidget.setGeometry(QtCore.QRect(100, 20, 741, 0))
        verticalLayoutWidget.setObjectName("verticalLayoutWidget" + str(bed._bedid))
        verticalLayout_2 = QtWidgets.QVBoxLayout(verticalLayoutWidget)
        verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        verticalLayout_2.setObjectName("verticalLayout" + str(bed._bedid))
        BedAlarm = QtWidgets.QRadioButton(BedGroupBox)
        BedAlarm.setGeometry(QtCore.QRect(0, 20, 101, 20))
        BedAlarm.setObjectName("BedAlarm" + str(bed._bedid))
        BedAlarm.setText(QtCore.QCoreApplication.translate("MainWindow", "Alarm"))
        BedCritAlarm = QtWidgets.QRadioButton(BedGroupBox)
        BedCritAlarm.setGeometry(QtCore.QRect(0, 40, 101, 20))
        BedCritAlarm.setObjectName("BedCritAlarm" + str(bed._bedid))
        BedCritAlarm.setText(QtCore.QCoreApplication.translate("MainWindow", "CritAlarm"))
        BedAddModule = QtWidgets.QPushButton(BedGroupBox)
        BedAddModule.setGeometry(QtCore.QRect(0, 60, 101, 32))
        BedAddModule.setObjectName("BedAddModule" + str(bed._bedid))
        BedAddModule.setText(QtCore.QCoreApplication.translate("MainWindow", "Add Module"))
        #call children into view
        for mod in bed._modules:
            self.ModuleUI(mod, verticalLayout_2, verticalLayoutWidget)
        # resize after adding children
        heights = sum(
            x.frameGeometry().height() for x in iter(
                verticalLayoutWidget.findChildren(QtWidgets.QGroupBox)
            )
        )  # ugly as sin generator to sum heights of children
        if heights > 0:
            verticalLayoutWidget.setMinimumHeight(heights)
        else:
            verticalLayoutWidget.setMinimumHeight(75)
        BedGroupBox.setMinimumHeight(
            BedGroupBox.findChild( #propagate height change to parent
                QtWidgets.QWidget,"verticalLayoutWidget" + str(bed._bedid)
            ).frameGeometry().height() + 25  # magic number padding is quick and dirty...
        )
        #appending to elements from module.ui
        self.verticalLayout.addWidget(BedGroupBox)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)



    def ModuleUI(self, module, BedLayout, BedLayoutWidget):
        ModulemonitorsGroupBox = QtWidgets.QGroupBox(BedLayoutWidget)
        ModulemonitorsGroupBox.setObjectName("ModulemonitorsGroupBox" + str(module._moduleid))
        ModulemonitorsGroupBox.setTitle(QtCore.QCoreApplication.translate("MainWindow", module._modulename))
        verticalLayoutWidget = QtWidgets.QWidget(ModulemonitorsGroupBox)
        verticalLayoutWidget.setGeometry(QtCore.QRect(0, 20, 761, 0))
        verticalLayoutWidget.setObjectName("verticalLayoutWidget" + str(module._moduleid))
        verticalLayout = QtWidgets.QVBoxLayout(verticalLayoutWidget)
        verticalLayout.setContentsMargins(0, 0, 0, 0)
        verticalLayout.setObjectName("verticalLayout" + str(module._moduleid))
        #call children
        for monitor in module._monitortypes:
            self.MonitorUI(monitor, verticalLayout, verticalLayoutWidget)
        # resize after adding children
        heights = sum(
            x.frameGeometry().height() for x in iter(
                verticalLayoutWidget.findChildren(QtWidgets.QGroupBox)
            )
        )# ugly as sin generator to sum heights of children
        verticalLayoutWidget.setMinimumHeight(heights)
        #add self to parent
        BedLayout.addWidget(ModulemonitorsGroupBox)

    def MonitorUI(self, monitor, ModuleLayout, ModuleLayoutWidget):
        # TODO add bedid into all relevant names and start inserting bed data
        MonitorGroupBox = QtWidgets.QGroupBox(ModuleLayoutWidget)
        MonitorGroupBox.setObjectName("MonitorGroupBox" + str(monitor._modulemonitorid))
        MonitorGroupBox.setFixedHeight(45)
        MonitorGroupBox.setTitle(QtCore.QCoreApplication.translate("MainWindow", str(monitor._monitortype._name)))
        MonitorValueScale = QtWidgets.QProgressBar(MonitorGroupBox)
        MonitorValueScale.setGeometry(QtCore.QRect(0, 20, 118, 23))
        MonitorValueScale.setProperty("value", 24)
        MonitorValueScale.setObjectName("MonitorValueScale" + str(monitor._modulemonitorid))
        MonitorCurrentValue = QtWidgets.QLCDNumber(MonitorGroupBox)
        MonitorCurrentValue.setGeometry(QtCore.QRect(130, 20, 64, 23))
        MonitorCurrentValue.setProperty("value", 30000.0)
        MonitorCurrentValue.setObjectName("MonitorCurrentValue" + str(monitor._modulemonitorid))
        MonitorUnits = QtWidgets.QTextBrowser(MonitorGroupBox)
        MonitorUnits.setGeometry(QtCore.QRect(200, 20, 91, 23))
        MonitorUnits.setObjectName("MonitorUnits" + str(monitor._modulemonitorid))
        MonitorAlarm = QtWidgets.QRadioButton(MonitorGroupBox)
        MonitorAlarm.setGeometry(QtCore.QRect(300, 20, 100, 20))
        MonitorAlarm.setObjectName("MonitorAlarm" + str(monitor._modulemonitorid))
        MonitorCritAlarm = QtWidgets.QRadioButton(MonitorGroupBox)
        MonitorCritAlarm.setGeometry(QtCore.QRect(400, 20, 100, 20))
        MonitorCritAlarm.setObjectName("MonitorCritAlarm" + str(monitor._modulemonitorid))
        ModuleLayout.addWidget(MonitorGroupBox)