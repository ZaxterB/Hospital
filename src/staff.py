#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""MOD005622 TRI2 B01CAM"""
__author__ = "Tim Clarke"
__copyright__ = "Copyright 2020, Tim Clarke/Zach Beed"
__license__ = "Private"
__version__ = "0.0.1"

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

class Staffs():
    """collection and management of Staff data and objects (sorry about the nasty plural)"""

    """private list of staff"""
    __staffraw__ = {}
    __staff__ = []

    def __init__(self, db):
        colnames, data = db.query("""
            SELECT staffid, name, email, telnumber, case when stafftype=1 then 'Nurse' else 'Consultant' end as stafftype
            FROM staff
            ORDER BY staffid""", None)
        if colnames is not None:
            # store the raw data
            self.__staffraw__['colnames'] = ['id', 'Name', 'Email', 'Tel Number', 'Type']
            self.__staffraw__['data'] = data
            # store all the records individually as objects
            for record in data:
                staff = Staff(record[0], record[1], record[2], record[3], record[4])
                self.__staff__.append(staff)

    """return all records for mass operations"""
    def getDisplayStaff(self):
        return self.__staffraw__

class Staff():
    """Staff object (singular!)"""

    """private attributes"""
    __staffid__ = None
    __name__ = None
    __email__ = None
    __telnumber__ = None
    __stafftype__ = None

    def __init__(self, staffid, name, email, telnumber, stafftype):
        __staffid__ = staffid
        __name__ = name
        __email__ = email
        __telnumber__ = telnumber
        __stafftype__ = stafftype