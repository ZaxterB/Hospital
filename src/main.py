#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""MOD005622 TRI2 B01CAM"""
__author__ = "Tim Clarke/Zach Beed"
__copyright__ = "Copyright 2020, Tim Clarke/Zach Beed"
__license__ = "Private"
__version__ = "0.0.9"

import sys
if sys.version_info[0] < 3 or sys.version_info[1] < 7:
  raise Exception("Must be run using Python 3.7 or above")

import os
# app-specific constants
import constants
# app-specific database interface class
from db import Db
# core application window class
from coreWindow import coreWindow
# main PyQt library
from PyQt5.QtWidgets import QApplication

"""
main.py

  created by:   Tim Clarke

    Icons originally made by Freepik from www.flaticon.com

  date:         8jan2020
  purpose:      starting/control module
"""

window = None

def closeWindow():
    """shut down main window (and its timers)"""
    window.close()

if __name__ == '__main__':
    try:
        # change to the application root directory so we can get all files
        appDir = os.path.dirname(os.path.realpath(__file__))
        if appDir != os.getcwd():
            os.chdir(appDir)
            os.chdir('..')

        # check arguments
        testFileName = None
        if len(sys.argv) == 2:
            testFileName = sys.argv[1]
        elif len(sys.argv) != 1:
            raise RuntimeError('Startup arguments incorrect. Please optionally provide a test data file name')

        # start a Qt windowing application
        app = QApplication([])

        # initialise database connection class
        db = Db(constants.DBLOCATION, constants.DBNAME)
        db.query('set search_path to public;')

        window = coreWindow(db, testFileName)
        # set up trap to close main window (for timers)
        app.aboutToQuit.connect(closeWindow)

        # show the main window
        window.show()

    except Exception:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        raise RuntimeError("Error in main(): {0} at line {1}".
                           format(str(exc_value), str(exc_traceback.tb_lineno)))

    sys.exit(app.exec_())
