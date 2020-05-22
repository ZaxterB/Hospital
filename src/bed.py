#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""MOD005622 TRI2 B01CAM"""
__author__ = "Tim Clarke"
__copyright__ = "Copyright 2020, Tim Clarke/Zach Beed"
__license__ = "Private"
__version__ = "0.0.6"

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

    """private dictionary of all beds and database object"""
    _beds = []
    _db = None

    def __new__(self, *args, **kwargs):
        """singleton override"""
        if not self._instance:
            self._instance = object.__new__(self)
        return self._instance

    def __init__(self, db):
        self._db = db

    def getBeds(self):
        """return all records for display"""
        colnames, data = self._db.query("""
            SELECT bedid, bednumber
            FROM bed
            ORDER BY bednumber""", None)
        if colnames is not None:
            # store all the records individually as objects
            for record in data:
                moduleList = Modules(self._db).getModulesForBed(record[0])
                bed = Bed(self._db, record[0], record[1], constants.BAY_NUMBER, constants.STATION_NUMBER, moduleList)
                self._beds.append(bed)
        return self._beds

    def getBed(self, bedid):
        """get specific bed by id"""
        for bed in self._beds:
            if bed.bedid == bedid:
                return bed

class Bed():
    """Bed object"""
    
    """private attributes"""
    _db = None
    _bedid = None
    _bednumber = None
    _bayid = None
    _stationid= None
    _modules = []
    _alarm = False
    _alarmMonitorTypes = {} # dictionary of alarm states, key is monitortype, value is a dictionary of the value, direction and unit
    _critalarm = False
    _critAlarmMonitorTypes = {} # dictionary of critical alarm states, key is monitortype, value is a dictionary of the value, direction and unit
    _patient = None

    def __init__(self, db, bedid, bednumber, bayid, stationid, modules):
        self._db = db
        self._bedid = bedid
        self._bednumber = bednumber
        self._bayid = bayid
        self._stationid = stationid
        self._modules = modules
        self._patientid = 2

    def addModule(self, module):
        """add a module to the bed"""
        # prevent more than the maximum design number of modules being added 
        if len(self._modules) > MAX_MODULES_PER_BED - 1:
            raise ValueError('cannot have more than {0} modules per bed'.format(MAX_MODULES_PER_BED))
        self._modules.add(module)

    def displayTitles(self):
        """return a list of column names for display"""
        return ['id', 'Bed Number', "Monitors"]

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

    def getBedid(self):
        """return bedid"""
        return self._bedid

    bedid = property(getBedid)

    def getBedNumber(self):
        """return bed number"""
        return self._bednumber

    bednumber = property(getBedNumber)

    def setMonitorTypeValue(self, monitortypeid, newvalue):
        """set the monitortypeid for this bed to newvalue"""
        for module in self._modules:
            if monitortypeid in module.monitortypeids:
                module.setMonitorTypeValue(monitortypeid, newvalue, self)

    def alarmOn(self, monitortypeid, name, value, direction, unit):
        # only possible if there is a patient in the bed
        print("ALARM ON", monitortypeid, type(monitortypeid))
        if self._patientid:
            """receiving function for an alarm"""
            self._alarm = True
            # save the alarm status
            self._alarmMonitorTypes[monitortypeid] = [value, direction, unit]
            # record the event for auditing
            self._recordBedEvent(constants.BEDEVT_ALARM_ON, monitortypeid)

    def resetAlarm(self):
        """cancel a standard alarm"""
        self._alarm = False

    def isAlarmOn(self):
        """return state of alarm"""
        return self._alarm

    isAlarmOn = property(isAlarmOn)

    def alarmOff(self, monitortypeid):
        """receiving function for an alarm"""
        self._alarm = False
        # save the alarm status if this alarm was set
        try:
            del self._alarmMonitorTypes[monitortypeid]
            # record the event for auditing
            _recordBedEvent(constants.BEDEVT_ALARM_OFF, monitortypeid)
        except KeyError:
            # ignore, this alarm was not set
            pass

    def getAlarms(self):
        """return displayable list of current alarms"""
        display = ''
        for key, value in _alarmMonitorTypes.items():
            # assemble the name, the value, the direction and the unit
            display += str(value[0]) + value[1] + ' ' + value[2] + ' '
        return display

    alarms = property(getAlarms)

    def critAlarmOn(self, monitortypeid, name, value, direction, unit):
        # only possible if there is a patient in the bed
        if self._patientid:
            """receiving function for a critical alarm"""
            self._critalarm = True
            # save the alarm status
            self._critAlarmMonitorTypes[monitortypeid] = [value, direction, unit]
            self._recordBedEvent(constants.BEDEVT_CRITALARM_ON, monitortypeid)

    def isCritAlarmOn(self):
        """return state of critical alarm"""
        return self._critalarm

    isCritAlarmOn = property(isCritAlarmOn)

    def critAlarmOff(self, monitortypeid):
        """receiving function for a critical alarm"""
        self._critalarm = False
        # save the alarm status if this alarm was set
        try:
            del self._critAlarmMonitorTypes[monitortypeid]
            # record the event for auditing
            _recordBedEvent(constants.BEDEVT_CRITALARM_OFF, monitortypeid)
        except KeyError:
            # ignore, this alarm was not set
            pass

    def _recordBedEvent(self, bedeventtype, monitortypeid = None):
        """record a bed event in the audit trail in the database"""
        self._db.insert("""
            INSERT INTO public.bedevent (eventtime, eventtype, patientid, bedid, monitortypeid)
            VALUES (now(), %s, %s, %s, %s)""", (bedeventtype, self._patientid, self._bedid, monitortypeid, ))
