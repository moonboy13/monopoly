#!/urs/bin/python

# Begin the execution of the game 

# Window handling module
import Tkinter as Tk

# Importing of my modules
import start_screen as startScreen

# Begin the game
def main():
    start_root=Tk.Tk()
    beginScreen=startScreen.startMenu(start_root)
    start_root.mainloop()

if __name__ == '__main__':
    main()
