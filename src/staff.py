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
        colnames, data = db.query("""
          SELECT staffid, name, email, "number", type
          FROM public.staff;""", None)
        if colnames is not None:
            self.__staff__['colnames'] = ['id', 'Name', 'Email', 'Number', 'Type']
            self.__staff__['data'] = data

    """return all records for mass operations"""
    def getAllStaff(self):
        return self.__staff__