#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""MOD005622 TRI2 B01CAM"""
__author__ = "Zach Beed"
__copyright__ = "Copyright 2020, Tim Clarke/Zach Beed"
__license__ = "Private"
__version__ = "0.0.5"

from monitortype import MonitorTypes, MonitorType
# PyQt libraries
from PyQt5 import QtGui, uic, QtCore, QtWidgets

"""
modulemonitor.py

  created by:   Zach Beed
  date:         11mar2020
  purpose:      modulemonitor class
"""

class ModuleMonitors():
    """collection and management of MonitorType data and objects"""

    def __init__(self, db):
        self.db = db

    def getModuleMonitorForModule(self, moduleid):
        modulemonitors = []
        colnames, data = self.db.query("""
            SELECT modulemonitorid, monitortypeid,  minval, maxval
            FROM modulemonitor mm
            WHERE moduleid = %s""", (moduleid, ))
        if colnames is not None:
            # store all the records individually as objects
            for record in data:
                monitortype = MonitorTypes(self.db).getMonitorTypeForModule(record[1])
                modulemonitor = ModuleMonitor(record[0], monitortype, record[2], record[3])
                modulemonitors.append(modulemonitor)
        return modulemonitors

class ModuleMonitor():
    """MonitorType object"""

    """private attributes"""
    _modulemonitorid = None
    _monitortype = None # object
    _minval = None
    _maxval = None
    _current = None
    _parentWidget = None

    def __init__(self, modulemonitorid, monitortype, minval, maxval):
        self._modulemonitorid = modulemonitorid
        self._monitortype = monitortype
        self._minval = minval
        self._maxval = maxval

    def getMonitorTypeName(self):
        """return names of monitortypes"""
        return self._monitortype.name

    def getStaticValues(self):
        """return a displayable string of current values"""
        return self._monitortype.name

    staticValues = property(getStaticValues)

    def getCurrentValues(self):
        """return a displayable string of current values"""
        return self._monitortype.name + ': ' + str(self._current) + ' (' + str(self._maxval) + '/' + str(self._minval) + ')'

    currentValues = property(getCurrentValues)

    def setCurrentValue(self, value, bed):
        """set the current monitortype's value"""
        self._current = value
        alarmstatus = None
        if self._current <= self._minval:
            """raise alarm"""
            bed.alarmOn(self._monitortype.id, self._monitortype.name, value, 'under', self._monitortype.unit)
            alarmstatus = "alarm"
        elif self._current >= self._maxval:
            """raise alarm"""
            bed.alarmOn(self._monitortype.id, self._monitortype.name, value, 'over', self._monitortype.unit)
            alarmstatus = "alarm"
        else:
            """cancel alarm"""
            bed.alarmOff(self._monitortype.id)

        if self._current <= self._monitortype.dangerMin:
            """raise critical alarm"""
            bed.critAlarmOn(self._monitortype.id, self._monitortype.name, value, 'under', self._monitortype.unit)
            print(str(value) + "under" + str(self._monitortype.dangerMin))
            alarmstatus = "critalarm"
        elif self._current >= self._monitortype.dangerMax:
            """raise critical alarm"""
            bed.critAlarmOn(self._monitortype.id, self._monitortype.name, value, 'over', self._monitortype.unit)
            print(str(value) + "over" + str(self._monitortype.dangerMax))
            alarmstatus = "critalarm"
        else:
            """cancel critical alarm"""
            bed.critAlarmOff(self._monitortype.id)

        self.updateUI(alarmstatus)

    def getmonitortypeid(self):
        return self._monitortype.id

    monitortypeid = property(getmonitortypeid)

    def updateUI(self, alarmstatus):
        """update ui when values change so that changes are reflected"""
        #assign relevant components to variable
        MonitorCurrentValue = self._parentWidget.findChild(QtWidgets.QLabel, "MonitorCurrentValue" + str(self._modulemonitorid))
        #TODO: debug segfaults from updating this component
        # MonitorValueScale = self._parentWidget.findChild(QtWidgets.QProgressBar, "MonitorValueScale" + str(self._modulemonitorid))
        MonitorAlarm = self._parentWidget.findChild(QtWidgets.QCheckBox, "MonitorAlarm" + str(self._modulemonitorid))
        MonitorCritAlarm = self._parentWidget.findChild(QtWidgets.QCheckBox, "MonitorCritAlarm" + str(self._modulemonitorid))
        # update current value ui to reflect current value
        MonitorCurrentValue.setText(str(self._current))
        # MonitorValueScale.setValue(self._current)
        #change stylings of components depenting on alarm status
        if alarmstatus != None:
            if alarmstatus == "alarm":
                MonitorAlarm.setChecked(True)
                MonitorCurrentValue.setStyleSheet('color: yellow')
            elif alarmstatus == "critalarm":
                MonitorCritAlarm.setChecked(True)
                MonitorCurrentValue.setStyleSheet('color: red')
        else:
            MonitorAlarm.setChecked(False)
            MonitorCritAlarm.setChecked(False)
            MonitorCurrentValue.setStyleSheet('color: black')

    def UI(self, parentWidget):
        """create a QtWidget with all the monitor related ui components required"""
        #allocate parent to variable for ease of access later
        self._parentWidget = parentWidget
        #create groupbox to hold controls and readouts
        MonitorGroupBox = QtWidgets.QGroupBox(parentWidget)
        MonitorGroupBox.setObjectName("MonitorGroupBox" + str(self._modulemonitorid))
        MonitorGroupBox.setFixedHeight(43)
        MonitorGroupBox.setTitle(QtCore.QCoreApplication.translate("MainWindow", str(self._monitortype._name)))
        MonitorGroupBox.setContentsMargins(0, 0, 0, 0)
        MonitorGroupBox.setAlignment(QtCore.Qt.AlignCenter)
        #TODO debug why this element causes segmentation faults
        # MonitorValueScale = QtWidgets.QProgressBar(MonitorGroupBox)
        # MonitorValueScale.setGeometry(QtCore.QRect(0, 20, 118, 23))
        # MonitorValueScale.setRange(self._monitortype.dangerMin - 5, self._monitortype.dangerMax + 5)
        # MonitorValueScale.setValue(self._monitortype.dangerMin)
        # MonitorValueScale.setObjectName("MonitorValueScale" + str(self._modulemonitorid))
        #create lable to display current value
        MonitorCurrentValue = QtWidgets.QLabel(MonitorGroupBox)
        MonitorCurrentValue.setGeometry(QtCore.QRect(130, 20, 64, 23))
        MonitorCurrentValue.setText(str(self._monitortype.dangerMin))
        MonitorCurrentValue.setObjectName("MonitorCurrentValue" + str(self._modulemonitorid))
        #create lable for currentvalues scientific units
        MonitorUnits = QtWidgets.QLabel(MonitorGroupBox)
        MonitorUnits.setGeometry(QtCore.QRect(200, 20, 51, 23))
        MonitorUnits.setObjectName("MonitorUnits" + str(self._modulemonitorid))
        MonitorUnits.setText(self._monitortype._unit)
        MonitorUnits.setAutoFillBackground(True)
        #create checkbox to indicate alarm
        MonitorAlarm = QtWidgets.QCheckBox(MonitorGroupBox)
        MonitorAlarm.setGeometry(QtCore.QRect(300, 20, 100, 20))
        MonitorAlarm.setObjectName("MonitorAlarm" + str(self._modulemonitorid))
        MonitorAlarm.setText("alarm")
        #create checkbox to indicate critical alarm
        MonitorCritAlarm = QtWidgets.QCheckBox(MonitorGroupBox)
        MonitorCritAlarm.setGeometry(QtCore.QRect(400, 20, 100, 20))
        MonitorCritAlarm.setObjectName("MonitorCritAlarm" + str(self._modulemonitorid))
        MonitorCritAlarm.setText("critical alarm")

        return MonitorGroupBox
