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
  arguments:
  returns:      TODO
"""

class Patients():
    """collection and management of Patient data and objects"""

    """private list of patients"""
    __patientsraw__ = {}
    __patients__ = []

    def __init__(self, db):
        colnames, data = db.query("""
            SELECT patientid, name
            FROM patient
            ORDER BY patientid""", None)
        if colnames is not None:
            # store the raw data
            self.__patientsraw__['colnames'] = ['id', 'Name']
            self.__patientsraw__['data'] = data
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
    __patientid__ = None
    __name__ = None

    def __init__(self, patientid, name):
        __patientid__ = patientid
        __name__ = name