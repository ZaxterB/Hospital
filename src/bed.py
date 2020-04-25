#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""MOD005622 TRI2 B01CAM"""
__author__ = "Tim Clarke"
__copyright__ = "Copyright 2020, Tim Clarke/Zach Beed"
__license__ = "Private"
__version__ = "0.0.0"

"""
bed.py

  created by:   Tim Clarke
  date:         11mar2020
  purpose:      bed class
  arguments:
  returns:      TODO
"""


class Bed():
    """private list of beds"""
    __beds__ = {}

    def __init__(self, db):
        colnames, data = db.query("""
          select bedid, number
          from bed
          order by bedid""", None)
        if colnames is not None:
            self.__beds__['colnames'] = ['id', 'Bed Number']
            self.__beds__['data'] = data

    """return all records for mass operations"""
    def getAllBeds(self):
        return self.__beds__