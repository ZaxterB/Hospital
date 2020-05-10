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
    __modulemonitorsraw__ = {}
    __modulemonitors__ = []

    def __init__(self, db):
        self.db = db
        # colnames, data = db.query("""
        #     SELECT modulemonitorid, monitortypeid, moduleid, minval, maxval
        #     FROM modulemonitor
        #     ORDER BY monitortypeid""", None)
        # if colnames is not None:
        #     # store the raw data
        #     self.__monitortypesraw__['colnames'] = ['id', 'Name', 'Unit', 'Default Max', 'Default Min', 'Danger Max', 'Danger Min']
        #     self.__monitortypesraw__['data'] = data
        #     # store all the records individually as objects
        #     for record in data:
        #         monitortype = MonitorType(record[0], record[1], record[2], record[3], record[4], record[5], record[6]) # removed , record[7]
        #         self.__monitortypes__.append(monitortype)

    """return all records for mass operations"""
    def getDisplayMonitorTypes(self):
        return self.__modulemonitorsraw__

    def getModuleMonitorForModule(self, moduleid):
        colnames, data = self.db.query("""
            SELECT modulemonitorid, monitortypeid,  minval, maxval
            FROM modulemonitor
            WHERE moduleid = %s""", (moduleid, ))
        if colnames is not None:
            # store all the records individually as objects
            for record in data:
                monitortype = MonitorTypes(self.db).getMonitorTypesForModule(record[1])
                modulemonitor = ModuleMonitor(record[0], monitortype, record[2], record[3])
                self.__modulemonitors__.append(modulemonitor)
        return self.__modulemonitors__

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
