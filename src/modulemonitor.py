#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""MOD005622 TRI2 B01CAM"""
__author__ = "Zach Beed"
__copyright__ = "Copyright 2020, Tim Clarke/Zach Beed"
__license__ = "Private"
__version__ = "0.0.2"

from monitortype import MonitorTypes, MonitorType
"""
monitortype.py

  created by:   Zach Beed
  date:         11mar2020
  purpose:      modulemonitor class
  arguments:
  returns:      TODO
"""

class ModuleMonitors():
    """collection and management of MonitorType data and objects"""

    """private list of monitor types"""

    def __init__(self, db):
        self.db = db

    """return all records for mass operations"""

    def getModuleMonitorForModule(self, moduleid):
        modulemonitors = []
        colnames, data = self.db.query("""
            SELECT modulemonitorid, monitortypeid,  minval, maxval
            FROM modulemonitor
            WHERE moduleid = %s""", (moduleid, ))
        if colnames is not None:
            # store all the records individually as objects
            for record in data:
                monitortype = MonitorTypes(self.db).getMonitorTypesForModule(record[1])
                modulemonitor = ModuleMonitor(record[0], monitortype, record[2], record[3])
                modulemonitors.append(modulemonitor)
        return modulemonitors

class ModuleMonitor():
    """MonitorType object"""

    """private attributes"""
    __modulemonitorid__ = None
    __monitortype__ = None
    __minval__ = None
    __maxval__ = None

    def __init__(self, modulemonitorid, monitortype, minval, maxval):
        self.__modulemonitorid__ = modulemonitorid
        self.__monitortype__ = monitortype
        self.__minval__ = minval
        self.__maxval__ = maxval
