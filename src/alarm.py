#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""MOD005622 TRI2 B01CAM"""
__author__ = "Tim Clarke"
__copyright__ = "Copyright 2020, Tim Clarke/Zach Beed"
__license__ = "Private"
__version__ = "0.0.0"

"""
alarm.py

  created by:   Tim Clarke
  date:         20may2020
  purpose:      alarm class
"""

class Alarm():
    """singleton collection and management of alarm functionality"""
    _instance = None

    def __new__(self, *args, **kwargs):
        """singleton override"""
        if not self._instance:
            self._instance = object.__new__(self)
        return self._instance

    def __init__(self):
        """TODO needed?"""
        pass
        
    def sendSMS(self):
        """TODO"""
        pass

    def sendEmail(self):
        """TODO"""
        pass