#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""MOD005622 TRI2 B01CAM"""
__author__ = "Tim Clarke"
__copyright__ = "Copyright 2020, Tim Clarke/Zach Beed"
__license__ = "Private"
__version__ = "0.0.2"

"""
patient.py

  created by:   Tim Clarke
  date:         11mar2020
  purpose:      patient class
"""

class Patients():
    """singleton collection and management of Patient data and objects"""
    __instance__ = None

    """private list of patients"""
    __patients__ = []
    __db__ = None

    def __new__(self, *args, **kwargs):
        """singleton override"""
        if not self.__instance__:
            self.__instance__ = object.__new__(self)
        return self.__instance__

    def __init__(self, db):
        if len(self.__patients__) != 0:
            return
        colnames, data = db.query("""
            SELECT patientid, name
            FROM patient
            ORDER BY patientid""", None)
        if colnames is not None:
            # store all the records individually as objects
            for record in data:
                patient = Patient(record[0], record[1])
                self.__patients__.append(patient)

    def getPatients(self):
        """return all records for mass operations"""
        return self.__patients__

class Patient():
    """Patient object"""
    
    """private attributes"""
    _patientid = None
    _name = None

    def __init__(self, patientid, name):
        _patientid = patientid
        _name = name