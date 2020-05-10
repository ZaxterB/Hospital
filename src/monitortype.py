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
            SELECT monitortypeid, name, unit, defaultmax, defaultmin, dangermax, dangermin
            FROM monitortype
            ORDER BY monitortypeid""", None) #removed moduleid,
        if colnames is not None:
            # store the raw data
            self.__monitortypesraw__['colnames'] = ['id', 'Name', 'Unit', 'Default Max', 'Default Min', 'Danger Max', 'Danger Min']
            self.__monitortypesraw__['data'] = data
            # store all the records individually as objects
            for record in data:
                monitortype = MonitorType(record[0], record[1], record[2], record[3], record[4], record[5], record[6]) # removed , record[7]
                self.__monitortypes__.append(monitortype)

    """return all records for mass operations"""
    def getMonitorTypes(self):
        return self.__monitortypes__

class MonitorType():
    """MonitorType object"""

    """private attributes"""
    __monitortypeid__ = None
    __name__ = None
    __unit__ = None
    __defaultmax__ = None
    __defaultmin__ = None
    __dangerMax = None
    __dangerMin = None

    def __init__(self, monitortypeid, name, unit, defaultmax, defaultmin, dangermax, dangermin):
        self.__monitortypeid__ = monitortypeid
        self.__name__ = name
        self.__unit__ = unit
        self.__defaultmax__ = defaultmax
        self.__defaultmin__ = defaultmin
        self.__dangerMax = dangermax
        self.__dangerMin = dangermin

    def displayTitles(self):
        """return a list of column names for display"""
        return ['id', 'Name', 'Unit', 'Default Max', 'Default Min', 'Danger Max', 'Danger Min']

    def display(self):
        """return a displayable list of columns"""
        return self.__monitortypeid__, self.__name__, self.__unit__, self.__defaultmax__, self.__defaultmin__, self.__dangerMax, self.__dangerMin
