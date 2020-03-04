#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""MOD005622 TRI2 B01CAM"""
__author__ = "Tim Clarke/Zach Beed"
__copyright__ = "Copyright 2020, Tim Clarke/Zach Beed"
__license__ = "Private"
__version__ = "0.0.4"

import sys
import psycopg2
from psycopg2 import extras
import traceback  # for error tracing

"""
db.py

  created by:   Tim Clarke

  date:         29feb2020
  purpose:      database connection and query execution
"""


class Db():
    __modulename__ = 'Db'
    __instance__ = None
    __conn__ = ''  # psycopg2 database connection
    __cursor__ = ''  # psycopg2 database cursor

    @staticmethod
    def getInstance():
        """static accessor"""
        if Db.__instance__ == None:
            Db()
        return Db.__instance__

    def __init__(self, host, database):
        """constructor"""
        __functionname__ = '__init__'

        """singleton constructor"""
        if Db.__instance__ != None:
            raise Exception("This class is a singleton!")
        else:
            Db.__instance__ = self

        try:
            self.__conn__ = psycopg2.connect(host=host, database=database)
            self.__cursor__ = self.__conn__.cursor(cursor_factory=psycopg2.extras.DictCursor)
        except Exception as e:
            exc_type, exc_value, exc_traceback = sys.exc_info()
            raise RuntimeError("Error in {0}.{1}(): {2} at line {3}".
                               format(self.__modulename__, __functionname__,
                                      str(exc_value),
                                      str(exc_traceback.tb_lineno)))

    def query(self, sql, *args):
        """TODO execute sql statement with variable number of arguments"""
        __functionname__ = 'query'

        try:
            if len(sql) < 1:
                raise RuntimeError('Empty query statement given')
            self.__cursor__.execute(sql, *args)
        except Exception as e:
            exc_type, exc_value, exc_traceback = sys.exc_info()
            raise RuntimeError("Error in {0}.{1}(): {2} at line {3}".
                               format(self.__modulename__, __functionname__,
                                      str(exc_value),
                                      str(exc_traceback.tb_lineno)))
            return
"""
      try {
        // SQL statement
        $statement = $this->PDO->prepare ($query);
      }
      catch (\PDOException $e) {
        throw new \Exception ('Could not prepare query statement');
        return false;
      }
      foreach ($args as $i => $arg) {
        // Bind each value to placeholder
        try {
          (array)$arg = $this->pdoCast ($arg);
          if( is_array( $arg[0] ) ) {
            // open the binary stream
            $picstream = fopen( $arg[0]['tmp_name'], 'rb');
            $statement->bindValue (($i+1), $picstream, $arg[1]);
          } else {
            $statement->bindValue (($i+1), $arg[0], $arg[1]);
          }
        }
        catch (\PDOException $e) {
          throw new \Exception ('Could not bind argument '.($i+1).' to query');
          return false;
        }
      }
      try {
        // Execute SQL statement
        $statement->execute ( );
      }
      catch (\PDOException $e) {
        // Execution failed
        throw new \Exception ($e->getMessage());
        return false;
      }
      try {
        // Execution OK, fetch data (if any was returned)
        $array_assoc = $statement->fetchAll (\PDO::FETCH_ASSOC);
      }
      catch (\PDOException $e) {
        // Execution OK but no data fetched
        return true;
      }
      $statement->closeCursor ( );
      return $array_assoc;
"""
