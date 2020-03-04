#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""MOD005622 TRI2 B01CAM"""
__author__ = "Tim Clarke/Zach Beed"
__copyright__ = "Copyright 2020, Tim Clarke/Zach Beed"
__license__ = "Private"
__version__ = "0.0.4"

import sys
# app-specific constants
import constants
# app-specific database interface class
from db import Db
from PyQt5 import QtGui, uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget

"""
main.py

  created by:   Tim Clarke

    Icons originally made by Freepik from www.flaticon.com

  date:         8jan2020
  purpose:      starting/control module
"""


# TODO useful in debugging, remove for live
def dump(obj):
    for attr in dir(obj):
        print("obj.%s = %r" % (attr, getattr(obj, attr)))


class mine(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        uic.loadUi('files/mainwindow.ui', self)
        self.setWindowIcon(QtGui.QIcon('files/hospital.png'))
        self.setHandlers()

    def setHandlers(self):
        tblWidget = self.findChild(QTableWidget, 'tblShifts')
        if tblWidget is not None:
            tblWidget.setEnabled(False)
            tblWidget.clicked.connect(self.alert)

    def alert(self, index):
        """ argments: self=MainWindow, index=QModelIndex of clicked """
        print(index.row(), index.column())


if __name__ == '__main__':
    app = QApplication([])
    db = Db(constants.DBLOCATION, constants.DBNAME)

    window = mine()
    window.show()

    db.query('set search_path to public;')
    retval = db.query('select * from bed where bedid = %s', [1])

    sys.exit(app.exec_())
