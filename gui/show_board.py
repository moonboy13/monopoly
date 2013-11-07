#!/usr/bin/python

#-------------------------------#
# This file is to initially show
# the monopoly game board
#-------------------------------#

#from PIL import *
#from Tkinter import *
from PIL import Image, ImageTk
from Tkinter import Tk, Frame, Label

class Board(Frame):
    def __init__(self,parent):
        Frame.__init__(self,parent)
        self.parent=parent
        self.parent.title("Monopoly")
        self.initBoard()
        self.centerWindow()

    # Set the board as the background
    def initBoard(self):
        self.brd=Image.open("imgs/blank_board.jpg")
        tatras=ImageTk.PhotoImage(self.brd,height=self.parent.winfo_screenheight())
        label=Label(self,image=tatras)
        label.image=tatras
        label.pack()
        self.pack()

    # Create the geometry for the window
    def centerWindow(self):
        w,h=self.brd.size
        sw=self.parent.winfo_screenwidth()
        sh=self.parent.winfo_screenheight()
        x=(sw-w)/2
        y=(sh-h)/2
        self.parent.geometry('%dx%d+%d+%d' % (w, h, x, y))

# Create the base window for the board
root=Tk()
brd=Board(root)
brd.centerWindow()
root.mainloop()
