#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""MOD005622 TRI2 B01CAM"""
__author__ = "Tim Clarke/Zach Beed"
__copyright__ = "Copyright 2020, Tim Clarke/Zach Beed"
__license__ = "Private"
__version__ = "0.0.4"

"""
constants.py

  created by:   Tim Clarke

  date:         4mar2020
  purpose:      application constants
  arguments:
  returns:
"""

DBLOCATION = 'localhost'
DBNAME = 'hospital'

# graphical component files location
GRAPHICAL_FILES = 'src/files/'
# current design maximum of beds in a bay
MAX_BEDS_PER_BAY = 8
# current design maximum of modules per bed
MAX_MODULES_PER_BED = 4
# only one bay for the current functionality
BAY_NUMBER = 1
# only one monitoring station for the current functionality
STATION_NUMBER = 1
# pulse time (seconds)
PULSE_TIME = 1.0
# bed event types
BEDEVT_PATIENT_IN = 1       # patient added
BEDEVT_PATIENT_OUT = 2      # patient removed
BEDEVT_MON_ADD = 3          # monitor added
BEDEVT_MON_REM = 4          # monitor removed
BEDEVT_ALARM_ON = 5         # alarm set on
BEDEVT_ALARM_CANC = 6       # alarm cancelled by user
BEDEVT_ALARM_OFF = 7        # alarm set off
BEDEVT_CRITALARM_ON = 8     # critical alarm set on
BEDEVT_CRITALARM_OFF = 9    # critical alarm set off

# staff types
STAFFTYPE_NURSE = 1         # staff - nurse
STAFFTYPE_CONSULTANT = 2    # staff - consultant