#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""MOD005622 TRI2 B01CAM"""
__author__ = "Tim Clarke"
__copyright__ = "Copyright 2020, Tim Clarke/Zach Beed"
__license__ = "Private"
__version__ = "0.0.7"

# app-specific constants
from monitortype import MonitorTypes
from modulemonitor import ModuleMonitors, ModuleMonitor
# PyQt libraries
from PyQt5 import QtCore, QtWidgets

"""
module.py

  created by:   Tim Clarke
  date:         11mar2020
  purpose:      module class
                this subsumes the bedmodule class functionality since they are so closely related
                in the database
"""

class Modules():
    """singleton collection and management of Module data and objects"""
    __instance__ = None

    """private list of modules"""
    _modules = []
    _db = None

    def __new__(self, *args, **kwargs):
        """singleton override"""
        if not self.__instance__:
            self.__instance__ = object.__new__(self)
        return self.__instance__

    def __init__(self, db):
        if len(self._modules) != 0:
            return
        self.db = db

    def getModules(self):
        """TODO"""
        if len(self._modules) == 0:
            colnames, data = self.db.query("""
                SELECT mo.moduleid, mo.name, string_agg(mt.name::text, ',') as monitorname
                FROM public.module mo,public.modulemonitor mm, public.monitortype mt
                WHERE mo.moduleid = mm.moduleid AND mm.monitortypeid = mt.monitortypeid
                GROUP BY 1, 2
                ORDER BY mo.moduleid""", None) #kinda legacy function here TODO: simplify
            if colnames is not None:
                # store all the records individually as objects
                for record in data:
                    # create a module object from moduleid, modulename, monitors[]
                    module = Module(record[0], record[1], ModuleMonitors(self.db).getModuleMonitorForModule(record[0]))
                    self._modules.append(module)
        return self._modules

    def getModulesForBed(self, bedid):
        """get all modules installd on a bed"""
        colnames, data = self.db.query("""
            SELECT mo.moduleid, mo.name
            FROM public.module mo, public.bedmodule bm
            WHERE mo.moduleid = bm.moduleid AND
                bm.bedid = %s""", (bedid, ))
        modules = []
        if colnames is not None:
            for counter, record in enumerate(data):
                # create a module object from moduleid, modulename, monitors[]
                module = Module(record[0], record[1], ModuleMonitors(self.db).getModuleMonitorForModule(record[0]))
                modules.append(module)
        return modules

class Module():
    """module object"""

    """private attributes"""
    _moduleid = None
    _modulename = None
    _monitortypes = []

    def __init__(self, moduleid, modulename, monitortypes):
        self._moduleid = moduleid
        self._modulename = modulename
        self._monitortypes = monitortypes

    def displayTitles(self):
        """return a list of column names for display"""
        return ['id', 'Name', 'Monitor Name']

    def display(self):
        """return a displayable list of columns"""
        return self._moduleid, self._modulename, self.staticDisplay()

    def displayLive(self):
        """return a displayable list of columns"""
        return self._moduleid, self._modulename, self.shortDisplay()

    def staticDisplay(self):
        """return just a string representing this object - name only"""
        modulemonitorlist = []
        for modulemonitor in self._monitortypes:
            modulemonitorlist.append(modulemonitor.staticValues)
        return '\n'.join(modulemonitorlist)

    def shortDisplay(self):
        """return just a string representing this object - active values"""
        modulemonitorlist = []
        for modulemonitor in self._monitortypes:
            modulemonitorlist.append(modulemonitor.currentValues)
        return '\n'.join(modulemonitorlist)

    def getCurrentValues(self):
        """get the current monitor values for a given module"""
        """TODO"""
        pass

    def getMonitortypeids(self):
        """return a list of all the monitortypes in this module"""
        monitortypeids = []
        for monitortype in self._monitortypes:
            monitortypeids.append(monitortype.monitortypeid)
        return monitortypeids

    monitortypeids = property(getMonitortypeids)

    def setMonitorTypeValue(self, monitortypeid, newvalue, bed):
        """search this module for the monitortype, if found set the value
            pass the bed object down so the alarms can be set if necessary"""
        for modulemonitor in self._monitortypes:
            if modulemonitor.monitortypeid == monitortypeid:
                modulemonitor.setCurrentValue(newvalue, bed)

    def UI(self, parentWidget):
            ModuleGroupBox = QtWidgets.QGroupBox(parentWidget)
            ModuleGroupBox.setObjectName("ModuleGroupBox" + str(self._moduleid))
            ModuleGroupBox.setTitle(QtCore.QCoreApplication.translate("MainWindow", self._modulename))
            ModuleGroupBox.setContentsMargins(0, 0, 0, 0)
            verticalLayoutWidget = QtWidgets.QWidget(ModuleGroupBox)
            verticalLayoutWidget.setGeometry(QtCore.QRect(0, 20, 761, 0))
            verticalLayoutWidget.setObjectName("verticalLayoutWidget" + str(self._moduleid))
            verticalLayoutWidget.setContentsMargins(0, 0, 0, 0)
            verticalLayout = QtWidgets.QVBoxLayout(verticalLayoutWidget)
            verticalLayout.setContentsMargins(0, 0, 0, 0)
            verticalLayout.setSpacing(0)
            verticalLayout.setObjectName("verticalLayout" + str(self._moduleid))
            # call children
            for monitor in self._monitortypes:
                verticalLayout.addWidget(monitor.UI(verticalLayoutWidget))
            # resize after adding children
            heights = sum(
                x.frameGeometry().height() for x in iter(
                    verticalLayoutWidget.findChildren(QtWidgets.QGroupBox)
                )
            )  # ugly as sin generator to sum heights of children
            verticalLayoutWidget.setFixedHeight(heights)
            ModuleGroupBox.setFixedHeight(heights + 25)

            return ModuleGroupBox
