#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""MOD005622 TRI2 B01CAM"""
__author__ = "Tim Clarke"
__copyright__ = "Copyright 2020, Tim Clarke/Zach Beed"
__license__ = "Private"
__version__ = "0.0.6"

import sys
import psycopg2
from psycopg2 import extras

"""
db.py

  created by:   Tim Clarke

  date:         29feb2020
  purpose:      singleton database connection and query execution
  arguments:    instantion: host and database strings
  returns:      (see methods)
"""


class Db(object):
    """singleton database interaction interface"""
    # private variables
    _modulename = 'Db'
    _instance = None
    _conn = ''  # psycopg2 database connection
    _cursor = ''  # psycopg2 database cursor

    def __new__(self, *args, **kwargs):
        """singleton override"""
        if not self._instance:
            self._instance = object.__new__(self)
        return self._instance

    def __init__(self, host, database):
        _functionname = '__init__'
        try:
            self._conn = psycopg2.connect(host=host, database=database)
            self._cursor = self._conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        except Exception:
            exc_type, exc_value, exc_traceback = sys.exc_info()
            raise RuntimeError("Error in {0}.{1}(): {2} at line {3}".
                               format(self._modulename, _functionname,
                                      str(exc_value),
                                      str(exc_traceback.tb_lineno)))

    def query(self, sql, *args):
        """execute select statement with variable number of arguments
            returns: list of column names, list of lists of row data
            """
        _functionname = 'query'

        try:
            if len(sql) < 1:
                raise RuntimeError('Empty query statement given')
            self._cursor.execute(sql, args)
            if self._cursor.rowcount < 1:
                return None, None
            else:
                # get column names from query
                colnames = [desc[0] for desc in self._cursor.description]
                return colnames, self._cursor.fetchall()
        except Exception:
            exc_type, exc_value, exc_traceback = sys.exc_info()
            raise RuntimeError("Error in {0}.{1}(): {2} at line {3}".
                               format(self._modulename, _functionname,
                                      str(exc_value),
                                      str(exc_traceback.tb_lineno)))

    def insert(self, sql, *args):
        """execute insert statement with variable number of arguments
            returns: nothing
            """
        _functionname = 'insert'

        try:
            if len(sql) < 1:
                raise RuntimeError('Empty insert statement given')
            self._cursor.execute(sql, args)
            self._conn.commit()
        except Exception:
            exc_type, exc_value, exc_traceback = sys.exc_info()
            raise RuntimeError("Error in {0}.{1}(): {2} at line {3}".
                               format(self._modulename, _functionname,
                                      str(exc_value),
                                      str(exc_traceback.tb_lineno)))