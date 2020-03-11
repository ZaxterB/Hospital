#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""MOD005622 TRI2 B01CAM"""
__author__ = "Tim Clarke/Zach Beed"
__copyright__ = "Copyright 2020, Tim Clarke/Zach Beed"
__license__ = "Private"
__version__ = "0.0.1"

import sys
# app-specific constants
import constants
# app-specific database interface class
from db import Db
# app model classes
from bed import Bed
from module import Module
from monitortype import Monitortype
from patient import Patient

"""
fetchStartupData.py

  created by:   Tim Clarke
  date:         11mar2020
  purpose:      read all data from database required for system initialisation
"""


def fetchStartupData():
    try:
        # initialise database connection class
        db = Db(constants.DBLOCATION, constants.DBNAME)

        db.query('set search_path to public;')
        beds = db.query('select * from bed', None)
        bedevent = db.query('select * from bedevent', None)
        monitortypes = db.query('select * from monitortype', None)
        patient = db.query('select * from patient', None)
        staff = db.query('select * from staff', None)
        staffevent = db.query('select * from staffevent', None)
    except Exception as e:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        print("Error in fetchStartupData(): {0} at line {1}".format(str(exc_value),
                                                                    str(exc_traceback.tb_lineno)))
        quit()
