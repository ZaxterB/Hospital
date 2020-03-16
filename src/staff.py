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
  returns:
"""


class Staff():
    """private list of staff"""
    __staff__ = []

    def __init__(self, db):
        colnames, data = db.query('select * from staff', None)
        self.__staff__ = colnames
        self.__staff__.append(data)
