#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""MOD005622 TRI2 B01CAM"""
__author__ = "Tim Clarke"
__copyright__ = "Copyright 2020, Tim Clarke/Zach Beed"
__license__ = "Private"
__version__ = "0.0.0"

"""
monitortype.py

  created by:   Tim Clarke
  date:         11mar2020
  purpose:      monitortype class
  arguments:
  returns:
"""


class MonitorType():
    """private list of monitor types"""
    __monitortypes__ = []

    def __init__(self, db):
        colnames, data = db.query('select * from monitortype', None)
        self.__beds__ = colnames
        self.__beds__.append(data)