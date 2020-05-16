#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""MOD005622 TRI2 B01CAM"""
__author__ = "Tim Clarke"
__copyright__ = "Copyright 2020, Tim Clarke/Zach Beed"
__license__ = "Private"
__version__ = "0.0.2"


"""
bed.py

  created by:   Tim Clarke
  date:         16mar2020
  purpose:      staff class
"""

class Staffs():
    """collection and management of Staff data and objects (sorry about the nasty plural)"""

    """private list of staff"""
    __staff__ = []

    def __init__(self, db):
        colnames, data = db.query("""
            SELECT staffid, name, email, telnumber, case when stafftype=1 then 'Nurse' else 'Consultant' end as stafftype
            FROM staff
            ORDER BY staffid""", None)
        if colnames is not None:
            # store all the records individually as objects
            for record in data:
                staff = Staff(record[0], record[1], record[2], record[3], record[4])
                self.__staff__.append(staff)

    def getStaff(self):
        """return all records for mass operations"""
        return self.__staff__

class Staff():
    """Staff object (singular!)"""

    """private attributes"""
    _staffid = None
    _name = None
    _email = None
    _telnumber = None
    _stafftype = None

    def __init__(self, staffid, name, email, telnumber, stafftype):
        self._staffid = staffid
        self._name = name
        self._email = email
        self._telnumber = telnumber
        self._stafftype = stafftype

    def displayTitles(self):
        """return a list of column names for display"""
        return ['id', 'Name', 'Email', 'Tel Number', 'Type']

    def display(self):
        """return a displayable list of columns"""
        return self._staffid, self._name, self._email, self._telnumber, self._stafftype
