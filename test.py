#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""MOD005622 TRI2 B01CAM"""
__author__ = "Tim Clarke/Zach Beed"
__copyright__ = "Copyright 2020, Tim Clarke/Zach Beed"
__license__ = "Private"
__version__ = "0.0.1"

"""
integrumfeed.py

  created by:   Tim Clarke
  date:         8jan2020
  change log:
  purpose:      test tkinter

                pseudo-code:
                  

  returns:
  errors:
  assumes:      
  side effects:
"""

from tkinter import *

class Window(Frame):
  def __init__(self, master=None):
    Frame.__init__(self, master)
    self.master = master
    # widget can take all window
    self.pack(fill=BOTH, expand=1)

    # create button, link it to clickExitButton()
    exitButton = Button(self, text="Exit", command=self.clickExitButton)

    # place button at (0,0)
    exitButton.place(x=0, y=0)

  def clickExitButton(self):
    quit()

root = Tk()
app = Window(root)

# set window title
root.wm_title("Tkinter button")
root.geometry("320x200")

# show window
root.mainloop()
