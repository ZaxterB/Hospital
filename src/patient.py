#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""MOD005622 TRI2 B01CAM"""
__author__ = "Tim Clarke"
__copyright__ = "Copyright 2020, Tim Clarke/Zach Beed"
__license__ = "Private"
__version__ = "0.0.0"

"""
patient.py

  created by:   Tim Clarke
  date:         11mar2020
  purpose:      patient class
  arguments:
  returns:
"""


class Patient():
    """private list of patients"""
    __patients__ = []

    def __init__(self, db):
        colnames, data = db.query('select * from patient', None)
        self.__patients__ = colnames
        self.__patients__.append(data)