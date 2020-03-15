#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""MOD005622 TRI2 B01CAM"""
__author__ = "Tim Clarke/Zach Beed"
__copyright__ = "Copyright 2020, Tim Clarke/Zach Beed"
__license__ = "Private"
__version__ = "0.0.6"

import sys
import os
# app-specific constants
import constants
# app-specific database interface class
from db import Db
# read all data from database required for system initialisation
from fetchStartupData import fetchStartupData
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


if __name__ == '__main__':
    try:
        # change to the application directory so we can get all files
        appDir = os.path.dirname(os.path.realpath(__file__))
        if appDir != os.getcwd():
            os.chdir(appDir)

        # start a Qt windowing application
        app = QApplication([])

        # initialise database connection class
        db = Db(constants.DBLOCATION, constants.DBNAME)
        fetchStartupData()

        # show the main window
        window = coreWindow()
        window.show()

    except Exception:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        raise RuntimeError("Error in main(): {0} at line {1}".
                           format(str(exc_value), str(exc_traceback.tb_lineno)))

    sys.exit(app.exec_())
