#!/usr/bin/python
# This is a non gui interface to test out modules and game
# techniques.

from mono_module import *
from my_errs import *
from initialize import *
import random

####

####
nPlayers = None
while not nPlayers or nPlayers > 8:
    try:
        nPlayers=int(raw_input("Enter the number of players: "))
        if (nPlayers > 8):
            raise TooManyPlayers(nPlayers)
    except ValueError:
        print "Please enter an integer!"
    except TooManyPlayers as e:
        print e.nplayers+" is too many, please only use 8 or less."

Players=[]
tokens={"wheelbarrow": False,"battleship": False,"racecar": False,"thimble": False,
        "boot": False,"dog": False,"hat": False,"cat": False}
valid=tokens.keys()
validSet=set(valid)

# Get player and piece info
for player in range(1,nPlayers+1):
    name=str(raw_input("Please enter player "+str(player)+"'s name: "))
    cur=Player(name)
    piece=None
    while not piece:
        piece=str(raw_input("Please enter player "+str(player)+"'s piece: "))
        piece=piece.lower()
        if (not piece in validSet):
            piece=None
            print "Please enter a valid piece:"
            for item in valid:
                print item
        elif(tokens[piece]):
            piece=None
            print "Piece is taken, please choose another:"
            for item in valid:
                print item
        else:
            print cur.player+" will play as the "+piece
            cur.piece=piece
            tokens[piece]=True
            
    
    Players.append(cur)
