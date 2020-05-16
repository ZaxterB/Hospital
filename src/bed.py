#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""MOD005622 TRI2 B01CAM"""
__author__ = "Tim Clarke"
__copyright__ = "Copyright 2020, Tim Clarke/Zach Beed"
__license__ = "Private"
__version__ = "0.0.3"

# app-specific constants
import constants
from module import Modules

"""
bed.py

  created by:   Tim Clarke
  date:         11mar2020
  purpose:      bed class
"""

class Beds():
    """singleton collection and management of Bed data and objects"""
    _instance = None

    """private dictionary of all beds, bays for the beds, monitoring stations for the bays and
      patients for each bed"""
    _beds = []
    _db = None

    def __new__(self, *args, **kwargs):
        """singleton override"""
        if not self._instance:
            self._instance = object.__new__(self)
        return self._instance

    def __init__(self, db):
        self._db = db

    """return all records for display"""
    def getBeds(self):
        colnames, data = self._db.query("""
            SELECT bedid, bednumber
            FROM bed
            ORDER BY bednumber""", None)
        if colnames is not None:
            # store all the records individually as objects
            for record in data:
                moduleList = Modules(self._db).getModulesForBed(record[0])
                bed = Bed(record[0], record[1], constants.BAY_NUMBER, constants.STATION_NUMBER, moduleList)
                self._beds.append(bed)
        return self._beds

class Bed():
    """Bed object"""
    
    """private attributes"""
    _bedid = None
    _bednumber = None
    _bayid = None
    _stationid= None
    _modules = []

    def __init__(self, bedid, bednumber, bayid, stationid, modules):
        self._bedid = bedid
        self._bednumber = bednumber
        self._bayid = bayid
        self._stationid = stationid
        self._modules = modules

    def addModule(self, module):
        """add a module to the bed"""
        # prevent more than the maximum deisng number of modules being added 
        if len(self._modules) > MAX_MODULES_PER_BED - 1:
            raise ValueError('cannot have more than {0} modules per bed'.format(MAX_MODULES_PER_BED))
        self._modules.add(module)

    def displayTitles(self):
        """return a list of column names for display"""
        return ['id', 'Bed Number']

    def display(self):
        """return a displayable list of columns"""
        modules = []
        for module in self._modules:
            modules.append(module.shortDisplay())
        return self._bedid, self._bednumber, '\n'.join(modules)

    def getMonitorValues(self):
        """query all the beds for their monitor values"""
        """TODO"""
        pass