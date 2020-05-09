#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""MOD005622 TRI2 B01CAM"""
__author__ = "Tim Clarke"
__copyright__ = "Copyright 2020, Tim Clarke/Zach Beed"
__license__ = "Private"
__version__ = "0.0.2"

"""
monitortype.py

  created by:   Tim Clarke
  date:         11mar2020
  purpose:      monitortype class
  arguments:
  returns:      TODO
"""

class MonitorTypes():
    """collection and management of MonitorType data and objects"""

    """private list of monitor types"""
    __monitortypesraw__ = {}
    __monitortypes__ = []

    def __init__(self, db):
        colnames, data = db.query("""
            SELECT monitortypeid, moduleid, name, unit, defaultmax, defaultmin, dangermax, dangermin
            FROM monitortype
            ORDER BY monitortypeid""", None)
        if colnames is not None:
            # store the raw data
            self.__monitortypesraw__['colnames'] = ['id', 'Name', 'Unit', 'Default Max', 'Default Min', 'Danger Max', 'Danger Min']
            self.__monitortypesraw__['data'] = data
            # store all the records individually as objects
            for record in data:
                monitortype = MonitorType(record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7])
                self.__monitortypes__.append(monitortype)

    """return all records for mass operations"""
    def getDisplayMonitorTypes(self):
        return self.__monitortypesraw__

class MonitorType():
    """MonitorType object"""

    """private attributes"""
    __monitortypeid__ = None
    __moduleid__ = None
    __name__ = None
    __unit__ = None
    __defaultmax__ = None
    __defaultmin__ = None
    __dangerMax = None
    __dangerMin = None

    def __init__(self, monitortypeid, moduleid, name, unit, defaultmax, defaultmin, dangermax, dangermin):
        __monitortypeid__ = monitortypeid
        __moduleid__ = moduleid
        __name__ = name
        __unit__ = unit
        __defaultmax__ = defaultmax
        __defaultmin__ = defaultmin
        __dangerMax = dangermax
        __dangerMin = dangermin
