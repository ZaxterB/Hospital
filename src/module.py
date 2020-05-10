#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""MOD005622 TRI2 B01CAM"""
__author__ = "Tim Clarke"
__copyright__ = "Copyright 2020, Tim Clarke/Zach Beed"
__license__ = "Private"
__version__ = "0.0.2"

from modulemonitor import ModuleMonitor, ModuleMonitors
"""
module.py

  created by:   Tim Clarke
  date:         11mar2020
  purpose:      module class
  arguments:
  returns:
"""


class Modules():
    """collection and management of Module data and objects"""

    def __init__(self, db):
        self.db = db

    def getModulesForBed(self, bedid):
        modules = []
        colnames, data = self.db.query("""
            SELECT bm.bedmoduleid, mo.moduleid, mo.name
            FROM public.module mo, public.bedmodule bm
            WHERE mo.moduleid = bm.moduleid AND
                bm.bedid = %s""", (bedid, ))
        if colnames is not None:
            for record in data:
                MonitorList = ModuleMonitors(self.db).getModuleMonitorForModule(record[1])
                module = Module(record[1], record[2], MonitorList)
                modules.append(module)
        return modules

class Module():
    """module object"""

    """private attributes"""
    __moduleid__ = None
    __modulename__ = None
    __modulemonitors__ = []

    def __init__(self, moduleid, modulename, monitors):
        self.__moduleid__ = moduleid
        self.__modulename__ = modulename
        self.__modulemonitors__ = monitors

    def displayTitles(self):
        """return a list of column names for display"""
        return ['id', 'Name', 'Monitor Name']

    def display(self):
        """return a displayable list of columns"""
        """TODO finish call and return of monitors"""
        return self.__moduleid__, self.__modulename__, ""

    def getCurrentValues(self):
        """get the current monitor values for a given module"""
        """TODO"""
        pass
