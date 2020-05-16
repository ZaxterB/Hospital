#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""MOD005622 TRI2 B01CAM"""
__author__ = "Tim Clarke"
__copyright__ = "Copyright 2020, Tim Clarke/Zach Beed"
__license__ = "Private"
__version__ = "0.0.3"

"""
monitortype.py

  created by:   Tim Clarke
  date:         11mar2020
  purpose:      monitortype class
                this subsumes the modulemonitor class functionality since they are so closely related
                in the database
"""

class MonitorTypes(object):
    """singleton collection and management of MonitorType data and objects"""
    __instance__ = None
    """private list of monitor types and database connection"""
    __monitortypes__ = []
    __db__ = None

    def __new__(self, *args, **kwargs):
        """singleton override"""
        if not self.__instance__:
            self.__instance__ = object.__new__(self)
        return self.__instance__

    def __init__(self, db):
        if len(self.__monitortypes__) != 0:
            return
        self.__db__ = db
        colnames, data = self.__db__.query("""
            SELECT monitortypeid, name, unit, defaultmax, defaultmin, dangermax, dangermin
            FROM monitortype
            ORDER BY monitortypeid""", None)
        if colnames is not None:
            # store all the records individually as objects
            for counter, record in enumerate(data):
                monitortype = MonitorType(record[0], record[1], record[2], record[3], record[4], record[5], record[6])
                self.__monitortypes__.append(monitortype)

    def getMonitorTypes(self):
        """return all records for mass operations"""
        return self.__monitortypes__

    def getMonitorTypeForModule(self, monitortypeid):
        """return the record"""
        colnames, data = self.__db__.query("""
            SELECT mt.monitortypeid, mt.name, mt.unit, mt.defaultmax, mt.defaultmin, mt.dangermax, mt.dangermin
            FROM monitortype mt
            WHERE mt.monitortypeid = %s""", (monitortypeid, ))
        if colnames is not None:
            # store all the records individually as objects
            for record in data:
                monitortype = MonitorType(record[0], record[1], record[2], record[3], record[4], record[5], record[6])
        return monitortype

class MonitorType():
    """MonitorType object"""

    """private attributes"""
    _monitortypeid = None
    _name = None
    _unit = None
    _defaultmax = None
    _defaultmin = None
    _dangerMax = None
    _dangerMin = None

    def __init__(self, monitortypeid, name, unit, defaultmax, defaultmin, dangermax, dangermin):
        self._monitortypeid = monitortypeid
        self._name = name
        self._unit = unit
        self._defaultmax = defaultmax
        self._defaultmin = defaultmin
        self._dangerMax = dangermax
        self._dangerMin = dangermin

    def displayTitles(self):
        """return a list of column names for display"""
        return ['id', 'Name', 'Unit', 'Default Max', 'Default Min', 'Danger Max', 'Danger Min']

    def display(self):
        """return a displayable list of columns"""
        return self._monitortypeid, self._name, self._unit, self._defaultmax, self._defaultmin, self._dangerMax, self._dangerMin

    def get_name(self):
        return self._name

    name = property(get_name)
