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

class BedModules():
    """collection and management of BedModule data and objects"""

    """private lists of modules for this bed"""
    __modulesraw__ = {}
    __modules__ = []

    def __init__(self, module):
      __modules__
        # populate the other class attributes
        colnames, data = db.query("""
            SELECT moduleid
            FROM bedmodule
            WHERE bedid = %s""", (bed[0], ))
        if colnames is not None:
            # store the raw data
            self.__modules__['colnames'] = ['id']
            self.__modules__['data'] = data
            # store all the records individually as objects
            for record in data:
                bedmodule = BedModule()


    """return all records for mass operations"""
    def getDisplayBedModules(self):
        return self.__modules__

class BedModule():
    """BedModule object"""
    
    """private attributes"""
    __bedmoduleid__ = None
    __bedid__ = None
    __moduleid__ = None

    def __init__(self, bedmoduleid, bedid, moduleid):
        __bedmoduleid__ = bedmoduleid
        __bedid__ = bedid
        __moduleid__ = moduleid

    """query all the beds for their monitor values"""
    def getMonitorValues(self):
        """TODO"""
        pass