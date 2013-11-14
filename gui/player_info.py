#!/usr/bin/python

# Retrieve the player information

# Image Imports
from PIL import Image, ImageTk
import Tkinter as Tk
import ttk

# My Imports
from strings import *

# Strings references
glbSrings=univStrings()
strings=infoStrings()


# Class to get the players information
class playerInfo(Tk.Frame):
    def __init__(self,parent,nPlayers):
        Tk.Frame.__init__(self,frame)
        self.parent=parent
        self.nPlayers=nPlayers
