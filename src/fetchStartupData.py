#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""MOD005622 TRI2 B01CAM"""
__author__ = "Tim Clarke/Zach Beed"
__copyright__ = "Copyright 2020, Tim Clarke/Zach Beed"
__license__ = "Private"
__version__ = "0.0.0"

import sys
# app-specific constants
import constants
# app-specific database interface class
from db import Db

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

    except Exception as e:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        print("Error in fetchStartupData(): {0} at line {1}".format(str(exc_value),
                                                                    str(exc_traceback.tb_lineno)))
        quit()
