#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""MOD005622 TRI2 B01CAM"""
__author__ = "Tim Clarke"
__copyright__ = "Copyright 2020, Tim Clarke/Zach Beed"
__license__ = "Private"
__version__ = "0.0.1"

# app-specific constants
import constants
from module import Modules, Module

"""
bed.py

  created by:   Tim Clarke
  date:         11mar2020
  purpose:      bed class
  arguments:
  returns:      TODO
"""

class Beds():
    """collection and management of Bed data and objects"""

    """private dictionary of all beds, bays for the beds, monitoring stations for the bays and
      patients for each bed"""
    __bedsraw__ = {}
    __beds__ = []

    def __init__(self, db):
        colnames, data = db.query("""
            SELECT bedid, bednumber
            FROM bed
            ORDER BY bednumber""", None)
        if colnames is not None:
            # store the raw data
            self.__bedsraw__['colnames'] = ['id', 'Bed Number']
            self.__bedsraw__['data'] = data
            # store all the records individually as objects
            for record in data:
                bed = Bed(record[0], record[1], constants.BAY_NUMBER, constants.STATION_NUMBER)
                self.__beds__.append(bed)

    """return all records for display"""
    def getDisplayBeds(self):
        return self.__bedsraw__

class Bed():
    """Bed object"""
    
    """private attributes"""
    __bedid__ = None
    __bednumber__ = None
    __bayid__ = None
    __stationid__= None
    __modules__ = []

    def __init__(self, bedid, bednumber, bayid, stationid):
        self.__bedid__ = bedid
        self.__bednumber__ = bednumber
        self.__bayid__ = bayid
        self.__stationid__ = stationid
        self.__modules__ = Modules.getModulesForBed(bedid)

    """add a module to the bed"""
    def addModule(self, module):
        self.__modules__.add(module)

    """query all the beds for their monitor values"""
    def getMonitorValues(self):
        """TODO"""
        pass