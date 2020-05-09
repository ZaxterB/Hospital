#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""MOD005622 TRI2 B01CAM"""
__author__ = "Tim Clarke"
__copyright__ = "Copyright 2020, Tim Clarke/Zach Beed"
__license__ = "Private"
__version__ = "0.0.2"

"""
module.py

  created by:   Tim Clarke
  date:         11mar2020
  purpose:      module class
  arguments:
  returns:
"""


class Modules():
    """collection and management of Module data and objects"""

    """private list of monitor types"""
    __modulesraw__ = {}
    __modules__ = []


    def __init__(self, db):
        colnames, data = db.query("""
            SELECT mo.moduleid, mo.name,  string_agg(mt.name::text, ',') as monitorname
            FROM public.module mo, public.monitortype mt
            WHERE mo.moduleid = mt.moduleid
            GROUP BY 1, 2
            ORDER BY mo.moduleid""", None)
        if colnames is not None:
            # store the raw data
            self.__modulesraw__['colnames'] = ['id', 'Name', 'Monitor Name']
            self.__modulesraw__['data'] = data
            # store all the records individually as objects
            for record in data:
                module = Module(record[0], record[1])
                self.__modules__.append(module)

    def getDisplayModules(self):
        return self.__modulesraw__

class Module():
    """module object"""

    """private attributes"""
    __moduleid__ = None
    __modulename__ = None

    def __init__(self, moduleid, modulename):
        self.__moduleid__ = moduleid
        self.__modulename__ = modulename

    """get the current monitor values for a given module"""
    def getCurrentValues(self):
      """TODO"""
      pass
