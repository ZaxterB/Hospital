#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""MOD005622 TRI2 B01CAM"""
__author__ = "Tim Clarke"
__copyright__ = "Copyright 2020, Tim Clarke/Zach Beed"
__license__ = "Private"
__version__ = "0.0.0"

# python modules
import sys
import csv

"""
testfile.py

  created by:   Tim Clarke
  date:         16may2020
  purpose:      testfile hander class
  detail:       a test file supplied to the application will be a csv file of 3 columns:
                    bedid, monitortypeid, reading
                each row of the file will be read once per program pulse and at that pulse,
                the monitortype for the bed in question will be set to the supplied reading.
"""

class TestFile():
    """singleton class to manage the test data file"""
    _instance = None

    """private file reader and rows of file"""
    _filereader = None
    _rows = None

    def __new__(self, *args, **kwargs):
        """singleton override"""
        if not self._instance:
            self._instance = object.__new__(self)
        return self._instance

    def __init__(self, testFileName):
        """set up a csv file reader for the test data file"""
        try:
            with open(testFileName, newline='') as csvfile:
                _filereader = csv.reader(csvfile, delimiter=',', quotechar='"')
                self._rows = []
                for row in _filereader:
                    self._rows.append(row)
        except Exception:
            exc_type, exc_value, exc_traceback = sys.exc_info()
            raise RuntimeError("Error in main(): {0} at line {1}".
                               format(str(exc_value), str(exc_traceback.tb_lineno)))

    def __iter__(self):
        """iterator definition"""
        return self

    def __next__(self):
        """iterator definition"""

        # make sure we have some data left
        if not len(self._rows):
            raise StopIteration
        else:
            # return next row of data and delete it from the stack
            row = self._rows[0]
            del self._rows[0]
            return row