#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""MOD005622 TRI2 B01CAM"""
__author__ = "Tim Clarke"
__copyright__ = "Copyright 2020, Tim Clarke/Zach Beed"
__license__ = "Private"
__version__ = "0.0.1"

"""
patient.py

  created by:   Tim Clarke
  date:         11mar2020
  purpose:      patient class
  arguments:
  returns:      TODO
"""


class Patient():
    """private list of patients"""
    __patients__ = {}

    def __init__(self, db):
        colnames, data = db.query("""
          SELECT patientid, name
          FROM patient
          ORDER BY patientid""", None)
        if colnames is not None:
            self.__patients__['colnames'] = ['id', 'Name']
            self.__patients__['data'] = data

    """return all records for mass operations"""
    def getAllPatients(self):
        return self.__patients__