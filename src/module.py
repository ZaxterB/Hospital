#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""MOD005622 TRI2 B01CAM"""
__author__ = "Tim Clarke"
__copyright__ = "Copyright 2020, Tim Clarke/Zach Beed"
__license__ = "Private"
__version__ = "0.0.2"

from modulemonitor import ModuleMonitor, ModuleMonitors
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
        self.db = db
        colnames, data = self.db.query("""
            SELECT mo.moduleid, mo.name, string_agg(mt.name::text, ',') as monitorname
            FROM public.module mo,public.modulemonitor mm, public.monitortype mt
            WHERE mo.moduleid = mm.moduleid AND mm.monitortypeid = mt.monitortypeid
            GROUP BY 1, 2
            ORDER BY mo.moduleid""", None) #kinda legacy function here TODO: simplify
        if colnames is not None:
            # store the raw data
            self.__modulesraw__['colnames'] = ['id', 'Name', 'Monitor Name']
            self.__modulesraw__['data'] = data
            # store all the records individually as objects
            for record in data:
                print(record)
                module = Module(record[0], record[1])
                self.__modules__.append(module)

    def getDisplayModules(self):
        return self.__modulesraw__

    def getModulesForBed(self, bedid):
        colnames, data = self.db.query("""
            SELECT bm.bedmoduleid, mo.moduleid, mo.name
            FROM public.module mo, public.bedmodule bm
            WHERE mo.moduleid = bm.moduleid AND
                bm.bedid = %s""", (bedid, ))
        if colnames is not None:
            for record in data:
                MonitorList = ModuleMonitors(self.db).getModuleMonitorForModule(record[1])
                module = Module(record[1], record[2], MonitorList)
                self.__modules__.append(module)

class Module():
    """module object"""

    """private attributes"""
    __moduleid__ = None
    __modulename__ = None
    __monitors__ = []

    def __init__(self, moduleid, modulename, monitors):
        self.__moduleid__ = moduleid
        self.__modulename__ = modulename
        self.__monitors__ = monitors

    """get the current monitor values for a given module"""
    def getCurrentValues(self):
      """TODO"""
      pass
