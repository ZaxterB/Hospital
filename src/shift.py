#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""MOD005622 TRI2 B01CAM"""
__author__ = "Tim Clarke"
__copyright__ = "Copyright 2020, Tim Clarke/Zach Beed"
__license__ = "Private"
__version__ = "0.0.1"

from staff import Staffs

"""
shift.py

  created by:   Tim Clarke
  date:         16may2020
  purpose:      shift class
"""

class Shifts():
    """singleton collection and management of Shift data and objects"""
    _instance = None

    """private list of shift"""
    _shifts = []
    _db = None

    def __new__(self, *args, **kwargs):
        """singleton override"""
        if not self._instance:
            self._instance = object.__new__(self)
        return self._instance

    def __init__(self, db):
        self._db = db

    def getShifts(self):
        """return all active records for mass operations"""
        colnames, data = self._db.query("""
            SELECT shiftid, staffid, start, currentend
            FROM public.shift
            WHERE currentend > now()
            ORDER BY start desc""", None)
        if colnames is not None:
            # store all the records individually as objects
            for record in data:
                shift = Shift(record[0], Staffs(self._db).getStaffbyID(record[1]), record[2], record[3])
                self._shifts.append(shift)
        return self._shifts

class Shift():
    """Staff object (singular!)"""

    """private attributes"""
    _shiftid = None
    _staff = None
    _start = None
    _currentend = None

    def __init__(self, shiftid, staff, start, currentend):
        self._shiftid = shiftid
        self._staff = staff
        self._start = start
        self._currentend = currentend

    def displayTitles(self):
        """return a list of column names for display"""
        return ['id', 'Staff', 'Start', 'End', 'Hours']

    def display(self):
        """return a displayable list of columns"""
        return self._shiftid, self._staff.name, self._start, self._currentend, self._currentend - self._start
