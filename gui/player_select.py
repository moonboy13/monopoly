#!/usr/bin/python

# Window to handle the selection of players and their pieces

# Imaging Imports
from PIL import Image, ImageTk
import Tkinter as Tk
import ttk

# My modules
from strings import *

# String references
glbStrings=univStrings()
strings=selectStrings()

# Constants
WIDTH=225
HEIGHT=70
MAX_PLAYERS=8
MIN_PLAYERS=2
BORDER_WIDTH=1

# Quick screen to select the number of players
class nPlayersScreen(Tk.Frame):
    def __init__(self,parent):
        Tk.Frame.__init__(self,parent)
        self.parent=parent
        self.initUI()

    # The window itself
    def initUI(self):
        self.parent.title(strings.title)
        # Set the theme and pack the window. Not much difference
        # between the themes
        self.style=ttk.Style()
        self.style.theme_use(glbStrings.STYLE)
        self.pack(fill=Tk.BOTH,expand=0)
        frame=ttk.Frame(self,relief=Tk.RAISED,borderwidth=BORDER_WIDTH)
        frame.pack(fill=Tk.BOTH,expand=1)
        self.centerWindow()

        # Create the slider bar
        nPlayerSlider=ttk.Scale(frame,from_=MIN_PLAYERS,to=MAX_PLAYERS,
                                command=self.onScale)
        nPlayerSlider.grid(row=1,columnspan=2,sticky=Tk.W+Tk.E)

        # Variable for the number of players
        self.nPlayersDisplay=Tk.IntVar() # For displaying
        self.nPlayersDisplay.set(MIN_PLAYERS)
        self.PlayersLabel=ttk.Label(frame,text=0,textvariable=self.nPlayersDisplay)
        self.PlayersLabel.grid(row=1,column=2)

        # Instructions text
        self.instructions=Tk.StringVar()
        self.instructions.set(strings.sliderText)
        self.instructionsLabel=ttk.Label(frame,text=0,textvariable=self.instructions)
        self.instructionsLabel.grid(row=0,columnspan=3)

        # Buttons
        okButton=ttk.Button(frame, text=strings.ok, command=self.onOK)
        okButton.grid(row=2,column=0)
        cancelButton=ttk.Button(frame,text=strings.cancel,command=self.quit)
        cancelButton.grid(row=2,column=2)

    # Handle moving the slider
    def onScale(self,val):
        n=int(float(val))
        self.nPlayersDisplay.set(n)

    # Handle clicking OK
    def onOK(self):
        nPlayers=self.nPlayersDisplay.get()
        print nPlayers

    # Center the window
    def centerWindow(self):
        sw=self.parent.winfo_screenwidth()
        sh=self.parent.winfo_screenheight()
        x=(sw-WIDTH)/2
        y=(sh-HEIGHT)/2
        self.parent.geometry('%dx%d+%d+%d' % (WIDTH, HEIGHT, x, y))

root=Tk.Tk()
plyrSelect=nPlayersScreen(root)
root.mainloop()
