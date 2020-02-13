#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""MOD005622 TRI2 B01CAM"""
__author__ = "Tim Clarke/Zach Beed"
__copyright__ = "Copyright 2020, Tim Clarke/Zach Beed"
__license__ = "Private"
__version__ = "0.0.1"

"""
test.py

  created by:   Tim Clarke
  date:         8jan2020
  change log:
  purpose:      testing of pyqt

                pseudo-code:
                  

  returns:
  errors:
  assumes:      
  side effects:
"""

import sys
from PyQt5 import QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QGridLayout, QWidget, QPushButton, \
     QLabel, QTableWidget, QTableWidgetItem, QInputDialog, QSizeGrip
from PyQt5.QtGui import QPainter, QBrush, QColor, QIcon
from PyQt5.QtCore import Qt, QPoint 
from PyQt5.QtGui import QIcon
# from PyQt5.QtCore import pyqtSlot



def open_calculator():
    value, ok = QInputDialog.getDouble(
        window, # parent widget
        'Tax Calculator', # window title
        'Yearly Income:', # entry label
        min=0.0,
        max=1000000.0,
    )
    if not ok:
        return
    yearly_income.setText('Yearly Income: ${:,.2f}'.format(value))
    if value <= 9700:
        rate = 10.0
    elif value <= 39475:
        rate = 12.0
    elif value <= 84200:
        rate = 22.0
    elif value <= 160725:
        rate = 24.0
    elif value <= 204100:
        rate = 32.0
    tax_rate.setText('Highest Marginal Tax Rate: {}%'.format(rate))



if __name__ == '__main__':
   app = QApplication([])
   app.setStyle('Windows')

   window = QMainWindow()

   screen = QWidget()
   layout = QGridLayout()
   screen.setLayout(layout)

   yearly_income = QLabel()
   yearly_income.setText('Income: $0.00')
   layout.addWidget(yearly_income, 0, 0)

   tax_rate = QLabel()
   tax_rate.setText('Highest Marginal Tax Rate: 0%')
   layout.addWidget(tax_rate, 0, 1)

   button = QPushButton()
   button.setText('Calculator')
   button.clicked.connect(open_calculator)
   layout.addWidget(button, 1, 0, 1, 2)

   # Data table
   columns = ('Week', 'Hours Worked', 'Hourly Rate', 'Earned Income')

   table_data = [
       [7, 40.0, 100.0],
       [8, 37.5, 85.0],
       [9, 65, 150.0],
   ]

   table = QTableWidget()
   table.setColumnCount(len(columns))
   table.setHorizontalHeaderLabels(columns)
   table.setRowCount(len(table_data))
   for row_index, row in enumerate(table_data):
       # Set each column value in the table
       for column_index, value in enumerate(row):
           item = QTableWidgetItem(str(value))
           table.setItem(row_index, column_index, item)
       # Calculate the total and add it as another column
       table.setItem(row_index, 3, QTableWidgetItem(str(row[1] * row[2])))
   layout.addWidget(table, 2, 0, 1, 2)   
   window.setCentralWidget(screen)
   window.setWindowTitle('Hospital Bed Monitor')
   window.setMinimumSize(500, 200)

   window.showMaximized()
   window.show()

   sys.exit(app.exec_())
