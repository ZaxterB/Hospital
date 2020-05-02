#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""MOD005622 TRI2 B01CAM"""
__author__ = "Tim Clarke"
__copyright__ = "Copyright 2020, Tim Clarke/Zach Beed"
__license__ = "Private"
__version__ = "0.0.1"

"""
module.py

  created by:   Tim Clarke
  date:         11mar2020
  purpose:      module class
  arguments:
  returns:
"""


class Module():
    """private list of monitor types"""
    __modules__ = {}


    def __init__(self, db):
        colnames, data = db.query("""
            SELECT mo.moduleid, mo.name,  string_agg(mt.name::text, ',') as monitorname
            FROM public.module mo, public.monitortype mt
            WHERE mo.moduleid = mt.moduleid
            GROUP BY 1, 2
            ORDER BY mo.moduleid""", None)
        if colnames is not None:
            self.__modules__['colnames'] = ['id', 'Name', 'Monitor Name']
            self.__modules__['data'] = data

    """return all records for mass operations"""
    def getAllModules(self):
        return self.__modules__

    """get the current monitor values for a given module"""
    def getCurrentValues(self):
      """TODO"""
      pass