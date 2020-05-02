#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""MOD005622 TRI2 B01CAM"""
__author__ = "Tim Clarke"
__copyright__ = "Copyright 2020, Tim Clarke/Zach Beed"
__license__ = "Private"
__version__ = "0.0.0"

# app-specific constants
import constants

"""
bed.py

  created by:   Tim Clarke
  date:         11mar2020
  purpose:      bed class
  arguments:
  returns:      TODO
"""


class Bed():
    """private lists of beds, modules per bed, bays for the beds, monitoring stations for the bays and
      patients for each bed"""
    __beds__ = {}
    __modules__ = {}
    __bays__ = []
    __stations__ = []
    __patients__ = []

    def __init__(self, db):
        colnames, data = db.query("""
            SELECT bedid, bednumber
            FROM bed
            ORDER BY bednumber""", None)
        if colnames is not None:
            self.__beds__['colnames'] = ['id', 'Bed Number']
            self.__beds__['data'] = data
            # populate the other class attributes
            for bed in data:
                data.query = db.query("""
                    SELECT moduleid
                    FROM bedmodule
                    WHERE bedid = %s""", bed[0])
                self.__bays__.append(constants.BAY_NUMBER)
                self.__stations__.append(constants.STATION_NUMBER)
                self.__patients__.append(None)

    """return all records for mass operations"""
    def getAllBeds(self):
        return self.__beds__

    """query all the beds for their monitor values"""
    def getMonitorValues(self):
        """TODO"""
        pass