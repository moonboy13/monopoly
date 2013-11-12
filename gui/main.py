#!/urs/bin/python

# This module handles the execution of the monopoly game

# Window handling module
import Tkinter as Tk

# Importing of my modules
import start_screen as startScreen
import player_select as playerSelect

# Begin the game
def main():
    start_root=Tk.Tk()
    startScreen.startMenu(start_root)
    start_root.mainloop()

if __name__ == '__main__':
    main()
