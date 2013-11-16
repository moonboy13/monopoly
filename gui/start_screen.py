#!/usr/bin/python

# Opening screen. Display buttons to start the game
# and monopoly logo


# Image modules
from PIL import Image, ImageTk
import Tkinter as Tk
import ttk

# Personal modules
import player_select as PS
from strings import univStrings, startStrings

# Initialize string class
glbStrings=univStrings()
strings=startStrings()

class startMenu(Tk.Frame):
    def __init__(self,parent):
        Tk.Frame.__init__(self,parent)
        self.parent=parent
        self.initUI()

    # Center the window
    def centerWindow(self):
        w, h=self.image.size
        h+=50
        sw=self.parent.winfo_screenwidth()
        sh=self.parent.winfo_screenheight()

        x=(sw-w)/2
        y=(sh-h)/2
        self.parent.geometry('%dx%d+%d+%d' % (w, h, x, y))

    # Create the user interface
    def initUI(self):
        self.parent.title(strings.title)
        self.style=ttk.Style()
        self.style.theme_use(glbStrings.STYLE)

        # Create a frame for the logo
        frame=Tk.Frame(self,relief=Tk.RAISED,borderwidth=1)
        frame.pack(fill=Tk.BOTH,expand=1)
        # Open the photo and put it in its frame
        self.image=Image.open(strings.logo)
        tatras=ImageTk.PhotoImage(self.image)
        label=Tk.Label(frame,image=tatras)
        label.img=tatras
        label.pack()

        # Pack everything up and center
        self.pack(fill=Tk.BOTH,expand=1)
        self.centerWindow()

        # Add buttons
        closeButton=ttk.Button(self, text=strings.exitButton, command=self.quit)
        closeButton.pack(side=Tk.RIGHT, padx=5, pady=5)
        strtButton=ttk.Button(self, text=strings.startButton, 
                          command=lambda: self.startClick(self.parent))
        strtButton.pack(side=Tk.RIGHT)
        
    def startClick(self,root):
        # Start the player selection menu
        root.withdraw()
        plrSelRoot=Tk.Toplevel()
        plrWin=PS.nPlayersScreen(plrSelRoot)
        plrSelRoot.mainloop()
        plrSelRoot.destroy()
        root.deiconify()
