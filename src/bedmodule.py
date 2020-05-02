#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""MOD005622 TRI2 B01CAM"""
__author__ = "Tim Clarke"
__copyright__ = "Copyright 2020, Tim Clarke/Zach Beed"
__license__ = "Private"
__version__ = "0.0.0"

# app-specific objects
from module import Modules
# app-specific constants
import constants

"""
bed.py

  created by:   Tim Clarke
  date:         11mar2020
  purpose:      module class
  arguments:
  returns:      store the modules for a given bed
"""


class BedModule():
    """private lists of modules for this bed"""
    __modules__ = {}

    def __init__(self, module):
      __modules__

    """return all records for mass operations"""
    def getAllModules(self):
        return self.__modules__

    """query all the beds for their monitor values"""
    def getMonitorValues(self):
        """TODO"""
        pass