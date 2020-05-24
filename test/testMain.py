#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""MOD005622 TRI2 B01CAM"""
__author__ = "Tim Clarke"
__copyright__ = "Copyright 2020, Tim Clarke/Zach Beed"
__license__ = "Private"
__version__ = "0.0.0"

import unittest

import sys, os
if sys.version_info[0] < 3 or sys.version_info[1] < 7:
  raise Exception("Must be run using Python 3.7 or above")

# app-specific classes
sys.path.append('src')
import constants
from db import Db
from bed import Beds, Bed

# declare a database connection object for use in all test
db = None

def bed_alarm_high(self):
    """set monitor type to high value
        return alarm status"""
    beds = Beds(db).getBeds()
    beds[0].setMonitorTypeValue(monitortypeid = 1, newvalue = 9999)
    return beds[0].isAlarmOn

class hospitaltests(unittest.TestCase):
    def test(self):
        self.assertEqual(bed_alarm_high, True)

if __name__ == '__main__':
    # change to the application root directory so we can get all files
    appDir = os.path.dirname(os.path.realpath(__file__))
    print("appDir", appDir)
    if appDir != os.getcwd():
        os.chdir(appDir)
        os.chdir('..')

    # initialise database connection class
    db = Db(constants.DBLOCATION, constants.DBNAME)
    db.query('set search_path to public;')

    unittest.main()
