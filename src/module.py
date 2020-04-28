#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""MOD005622 TRI2 B01CAM"""
__author__ = "Tim Clarke"
__copyright__ = "Copyright 2020, Tim Clarke/Zach Beed"
__license__ = "Private"
__version__ = "0.0.0"

"""
module.py

  created by:   Tim Clarke
  date:         11mar2020
  purpose:      module class
  arguments:
  returns:
"""


class Module():
    """private list of monitor types"""
    __modules__ = {}

    def __init__(self, db):
        colnames, data = db.query("""
          select 
          from 
          order by """, None)
        if colnames is not None:
            self.__monitortypes__['colnames'] = ['id', 'Name', 'Unit', 'Default Max', 'Default Min', 'Danger Max', 'Danger Min']
            self.__monitortypes__['data'] = data

    """return all records for mass operations"""
    def getAllMonitorTypes(self):
        return self.__monitortypes__