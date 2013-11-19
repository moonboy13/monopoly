#!/usr/bin/python

# Retrieve the player information

# Image Imports
from PIL import Image, ImageTk
import Tkinter as Tk
import ttk

# My Imports
from strings import univStrings, infoStrings, pieceStrings
from constants import globalVars, playerInfoCnsts

# Strings references
glbStrings=univStrings()
pieceStrings=pieceStrings()
strings=infoStrings()

# Constants
globalVars=globalVars()
CONSTANTS=playerInfoCnsts()

# Class to get the players information
class playerInfo(Tk.Frame):
    def __init__(self,parent,nPlayers):
        Tk.Frame.__init__(self,parent)
        self.parent=parent
        self.nPlayers=nPlayers
        # Do this once for each player
        for i in range(self.nPlayers):
            self.initUI()

    def initUI(self):
        # Basic window setup
        self.parent.title(strings.title)
        self.style=ttk.Style()
        self.style.theme_use(glbStrings.STYLE)
        self.pack(fill=Tk.BOTH,expand=1)
        self.frame=ttk.Frame(self,relief=Tk.RAISED,borderwidth=CONSTANTS.BORDER_WIDTH)
        self.frame.pack(fill=Tk.BOTH,expand=1)

        # Name input instructions and field
        self.nameInstructions=Tk.StringVar()
        self.nameInstructions.set(strings.name)
        self.nameInstructionsLabel=ttk.Label(self.frame,text=0,textvariable=self.nameInstructions)
        self.nameInstructionsLabel.grid(row=0,columnspan=3)
        self.plyrName=Tk.StringVar()
        self.plyrName.set('')
        self.nameEntry=ttk.Entry(self,textvariable=self.plyrName)
        self.nameEntry.grid(row=1,columnspan=2,sticky=Tk.W+Tk.E)

        # Get image references for all of the piece icons
        self.imgOneFile=Image.open(pieceStrings.pieceOneImg)
        self.imgOne=ImageTk.PhotoImage(self.imgOneFile)
        self.imgOneName=Tk.StringVar()
        self.imgOneName.set(pieceStrings.pieceOne)
        self.imgOneNameLabel=ttk.Label(self.frame,text=0,textvariable=self.imgOneName)
        self.imgTwoFile=Image.open(pieceStrings.pieceTwoImg)
        self.imgTwo=ImageTk.PhotoImage(self.imgTwoFile)
        self.imgTwoName=Tk.StringVar()
        self.imgTwoName.set(pieceStrings.pieceTwo)
        self.imgTwoNameLabel=ttk.Label(self.frame,text=0,textvariable=self.imgTwoName)
        self.imgThreeFile=Image.open(pieceStrings.pieceThreeImg)
        self.imgThree=ImageTk.PhotoImage(self.imgThreeFile)
        self.imgThreeName=Tk.StringVar()
        self.imgThreeName.set(pieceStrings.pieceThree)
        self.imgThreeNameLabel=ttk.Label(self.frame,text=0,textvariable=self.imgThreeName)
        self.imgFourFile=Image.open(pieceStrings.pieceFourImg)
        self.imgFour=ImageTk.PhotoImage(self.imgFourFile)
        self.imgFourName=Tk.StringVar()
        self.imgFourName.set(pieceStrings.pieceFour)
        self.imgFourNameLabel=ttk.Label(self.frame,text=0,textvariable=self.imgFourName)
        self.imgFiveFile=Image.open(pieceStrings.pieceFiveImg)
        self.imgFive=ImageTk.PhotoImage(self.imgFiveFile)
        self.imgFiveName=Tk.StringVar()
        self.imgFiveName.set(pieceStrings.pieceFive)
        self.imgFiveNameLabel=ttk.Label(self.frame,text=0,textvariable=self.imgFiveName)
        self.imgSixFile=Image.open(pieceStrings.pieceSixImg)
        self.imgSix=ImageTk.PhotoImage(self.imgSixFile)
        self.imgSixName=Tk.StringVar()
        self.imgSixName.set(pieceStrings.pieceSix)
        self.imgSixNameLabel=ttk.Label(self.frame,text=0,textvariable=self.imgSixName)
        self.imgSevenFile=Image.open(pieceStrings.pieceSevenImg)
        self.imgSeven=ImageTk.PhotoImage(self.imgSevenFile)
        self.imgSevenName=Tk.StringVar()
        self.imgSevenName.set(pieceStrings.pieceSeven)
        self.imgSevenNameLabel=ttk.Label(self.frame,text=0,textvariable=self.imgSevenName)
        self.imgEightFile=Image.open(pieceStrings.pieceEightImg)
        self.imgEight=ImageTk.PhotoImage(self.imgEightFile)
        self.imgEightName=Tk.StringVar()
        self.imgEightName.set(pieceStrings.pieceEight)
        self.imgEightNameLabel=ttk.Label(self.frame,text=0,textvariable=self.imgEightName)
        self.imgNineFile=Image.open(pieceStrings.pieceNineImg)
        self.imgNine=ImageTk.PhotoImage(self.imgNineFile)
        self.imgNineName=Tk.StringVar()
        self.imgNineName.set(pieceStrings.pieceNine)
        self.imgNineNameLabel=ttk.Label(self.frame,text=0,textvariable=self.imgNineName)

        # Create all of the radio buttons for the Icons
        self.plyrPiece=Tk.StringVar()
        self.oneButton=Tk.Radiobutton(self.frame,image=self.imgOne,variable=self.plyrPiece,
                                      value=self.imgOneName)
        self.twoButton=Tk.Radiobutton(self.frame,image=self.imgTwo,variable=self.plyrPiece,
                                      value=self.imgOneName)
        self.threeButton=Tk.Radiobutton(self.frame,image=self.imgThree,variable=self.plyrPiece,
                                        value=self.imgThreeName)
        self.fourButton=Tk.Radiobutton(self.frame,image=self.imgFour,variable=self.plyrPiece,
                                       value=self.imgFourName)
        self.fiveButton=Tk.Radiobutton(self.frame,image=self.imgFive,variable=self.plyrPiece,
                                       value=self.imgFiveName)
        self.sixButton=Tk.Radiobutton(self.frame,image=self.imgSix,variable=self.plyrPiece,
                                      value=self.imgSixName)
        self.sevenButton=Tk.Radiobutton(self.frame,image=self.imgSeven,variable=self.plyrPiece,
                                        value=self.imgSevenName)
        self.eightButton=Tk.Radiobutton(self.frame,image=self.imgEight,variable=self.plyrPiece,
                                        value=self.imgEightName)
        self.nineButton=Tk.Radiobutton(self.frame,image=self.imgNine,variable=self.plyrPiece,
                                       value=self.imgNineName)
 
        # Lists of button and name references
        self.radioButtons=(self.oneButton,self.twoButton,self.threeButton,self.fourButton,
                           self.fiveButton,self.sixButton,self.sevenButton,self.eightButton,
                           self.nineButton)
        self.imgNameLabels=(self.imgOneNameLabel,self.imgTwoNameLabel,self.imgThreeNameLabel,
                            self.imgFourNameLabel,self.imgFiveNameLabel,self.imgSixNameLabel,
                            self.imgSevenNameLabel,self.imgEightNameLabel,self.imgNineNameLabel)

        # Place the buttons for the available pieces into a grid and provide the instructions
        self.buttonInstructions=Tk.StringVar()
        self.buttonInstructions.set(strings.pieces)
        self.buttonInstructionsLabel=ttk.Label(self.frame,text=0,
                                               textvariable=self.buttonInstructions)
        self.buttonInstructionsLabel.grid(row=2,columnspan=3)
        self.row=3
        self.column=0
        for i in range(CONSTANTS.N_BUTTONS):
            print i
            if globalVars.avaliablePieces[i]:
                self.imgNameLabels[i].grid(row=self.row,column=self.column)
                self.radioButtons[i].grid(row=(self.row+1),column=self.column)
                if self.column == 2:
                    self.row+=2
                    self.column=0
                else: 
                    self.column+=1

        # Create the confirm and cancel buttons
        self.okButton=ttk.Button(self.frame,text=strings.confirm,command=self.confirm)
        self.okButton.grid(row=(self.row+1),column=0)
        self.cancelButton=ttk.Button(self.frame,text=strings.cancel,command=self.quit)
        self.cancelButton.grid(row=(self.row+1),column=2)


        self.centerWindow()

    # Confirm Function
    def confirm(self):
        self.plyrName=self.Entry.get() 
        print self.plyrName+" will play as "+self.plyrPiece
        self.update()

    # Center the window
    def centerWindow(self):
        w=self.parent.winfo_width()
        h=self.parent.winfo_height()
        sw=self.parent.winfo_screenwidth()
        sh=self.parent.winfo_screenheight()

        x=(w-sw)/2
        y=(h-sh)/2
        self.parent.geometry('%dx%d+%d+%d' % (w, h, sw, sh))
