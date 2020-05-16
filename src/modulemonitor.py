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
                print("modulemonitor", )
                monitortype = MonitorTypes(self.db).getMonitorTypeForModule(record[1])
                modulemonitor = ModuleMonitor(record[0], monitortype, record[2], record[3])
                modulemonitors.append(modulemonitor)
        return modulemonitors

class ModuleMonitor():
    """MonitorType object"""

    """private attributes"""
    _modulemonitorid = None
    _monitortype = None
    _minval = None
    _maxval = None

    def __init__(self, modulemonitorid, monitortype, minval, maxval):
        self._modulemonitorid = modulemonitorid
        self._monitortype = monitortype
        self._minval = minval
        self._maxval = maxval

    def getMonitorTypeName(self):
        """return names of monitortypes"""
        return self._monitortype.get_name()