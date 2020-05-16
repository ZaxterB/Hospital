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
    _instance = None

    """private list of patients"""
    _patients = []
    _db = None

    def __new__(self, *args, **kwargs):
        """singleton override"""
        if not self._instance:
            self._instance = object.__new__(self)
        return self._instance

    def __init__(self, db):
        self._db = db
        if len(self._patients) != 0:
            return
        colnames, data = db.query("""
            SELECT patientid, name
            FROM patient
            ORDER BY patientid""", None)
        if colnames is not None:
            # store all the records individually as objects
            for record in data:
                patient = Patient(record[0], record[1])
                self._patients.append(patient)

    def getPatients(self):
        """return all records for mass operations"""
        return self._patients

class Patient():
    """Patient object"""
    
    """private attributes"""
    _patientid = None
    _name = None

    def __init__(self, patientid, name):
        _patientid = patientid
        _name = name