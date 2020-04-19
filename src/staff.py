#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""MOD005622 TRI2 B01CAM"""
__author__ = "Tim Clarke"
__copyright__ = "Copyright 2020, Tim Clarke/Zach Beed"
__license__ = "Private"
__version__ = "0.0.0"

# app-specific database interface class
from db import Db

"""
bed.py

  created by:   Tim Clarke
  date:         16mar2020
  purpose:      staff class
  arguments:
  returns:      TODO
"""


class Staff():
    """private list of staff"""
    __staff__ = {}

    def __init__(self, db):
        colnames, data = db.query('select * from staff', None)
        if colnames is not None:
            self.__staff__['colnames'] = colnames
            self.__staff__['data'] = data

    def getStaff(self):
        return self.__staff__