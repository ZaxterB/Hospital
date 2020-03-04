#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""MOD005622 TRI2 B01CAM"""
__author__ = "Tim Clarke/Zach Beed"
__copyright__ = "Copyright 2020, Tim Clarke/Zach Beed"
__license__ = "Private"
__version__ = "0.0.5"

import sys
import psycopg2
from psycopg2 import extras

"""
db.py

  created by:   Tim Clarke

  date:         29feb2020
  purpose:      singleton database connection and query execution
"""


class Db(object):
    __modulename__ = 'Db'
    __instance__ = None
    __conn__ = ''  # psycopg2 database connection
    __cursor__ = ''  # psycopg2 database cursor

    def __new__(self, *args, **kwargs):
        """singleton override"""
        if not self.__instance__:
            self.__instance__ = object.__new__(self)
        return self.__instance__

    def __init__(self, host, database):
        __functionname__ = '__init__'
        try:
            self.__conn__ = psycopg2.connect(host=host, database=database)
            self.__cursor__ = self.__conn__.cursor(cursor_factory=psycopg2.extras.DictCursor)
            return
        except Exception:
            exc_type, exc_value, exc_traceback = sys.exc_info()
            raise RuntimeError("Error in {0}.{1}(): {2} at line {3}".
                               format(self.__modulename__, __functionname__,
                                      str(exc_value),
                                      str(exc_traceback.tb_lineno)))

    def query(self, sql, *args):
        """execute sql statement with variable number of arguments"""
        __functionname__ = 'query'

        try:
            if len(sql) < 1:
                raise RuntimeError('Empty query statement given')
            self.__cursor__.execute(sql, *args)
            if self.__cursor__.rowcount < 1:
                return None
            else:
                # get column names from query
                colnames = [desc[0] for desc in self.__cursor__.description]
                return colnames, self.__cursor__.fetchall()
        except Exception:
            exc_type, exc_value, exc_traceback = sys.exc_info()
            raise RuntimeError("Error in {0}.{1}(): {2} at line {3}".
                               format(self.__modulename__, __functionname__,
                                      str(exc_value),
                                      str(exc_traceback.tb_lineno)))
