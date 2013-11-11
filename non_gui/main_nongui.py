#!/usr/bin/python
# This is a non gui interface to test out modules and game
# techniques.

# Import statements. The modules imported with the syntax
# from <name> import * are my personal modules that are
# contained in this same directory
from mono_module import *
from my_errs import *
from initialize import *
import random,time

####

# Roll the two dice and return the value + if the roll was a double.
def rollDice():
    random.seed(time.time()) # use sys time at time of roll to seed random
    a=random.randint(1,6)
    b=random.randint(1,6)
    if (a == b):
        doubles=True
    else:
        doubles=False
    
    output=[(a+b),doubles]
    return output

####

# Intialize the board, these are definded in the initialize.py file
board=makeBoard()
chance=Chance()
comChest=communityChest()

####
nPlayers = None
# Keep asking for input if there isn't a valid number of players 
# provided
while not nPlayers or nPlayers > 8:
    try:
        # ask for, and wait for, user input.
        nPlayers=int(raw_input("Enter the number of players: "))
        if (nPlayers > 8):
            # personal error definced in my_errs.py
            raise TooManyPlayers(nPlayers)
    # Predefinced error provided by python
    except ValueError:
        print "Please enter an integer!"
    # Catching my personal erry
    except TooManyPlayers as e:
        print e.nplayers+" is too many, please only use 8 or less."

# Initializing an empty list
Players=[]
# Initializing a dictionary. A dictionary is a list using strings as the keys instead
# of a number.
tokens={"wheelbarrow": False,"battleship": False,"racecar": False,"thimble": False,
        "boot": False,"dog": False,"hat": False,"cat": False}
# dictionary.keys() returns the keys of a dictionary
valid=tokens.keys()
# Creates a set of the keys
validSet=set(valid)

# Get player and piece info
for player in range(1,nPlayers+1):
    # no input checking, anything can be a players name
    name=str(raw_input("Please enter player "+str(player)+"'s name: "))
    # start an instance of the Player class in mono_modules.py
    cur=Player(name)
    piece=None
    while not piece:
        piece=str(raw_input("Please enter player "+str(player)+"'s piece: "))
        # make the input lowercase and check to see if it is an available piece
        piece=piece.lower()
        if (not piece in validSet):
            piece=None
            print "Please enter a valid piece:"
            print validSet
        elif(tokens[piece]):
            piece=None
            print "Piece is taken, please choose another:"
            print validSet
        else:
            cur.piece=piece
            tokens[piece]=True
            
    
    Players.append(cur)

# Create a dictionary of players
plyrDic={Players[0].player:Players[0]}
for i in range(len(Players)):
    plyrDic[Players[i].player]=Players[i]

# Begin Playing the game
print "Beginning the game!"
PlayGame=True
nSpaces=len(board)
# Some locations of important spaces
freeParking=20
jail=10
cntDoubles=0
turn=0 # whose turn in the player array it is
# Continue playing while people want to play
while PlayGame:
    # Inform users whose turn it is and print some information on them
    print "\nIt is "+Players[turn].player+"'s turn"
    print Players[turn].player+" is worth $"+str(Players[turn].worth)
    keys=Players[turn].properties.keys()
    if len(keys) > 0:
        print Players[turn].player+" owns:"
        for key in keys:
				    print Players[turn].properties[key].name

    else:
        print Players[turn].player+" owns no properties"

    print "\n"

    # Roll Dice and advance player
    roll=rollDice()

    # Check to see if the player is in jail first
    if (Players[turn].inJail):
        print "You are in Jail!!"
        jailActions(Players[turn],board,roll,freeParking)
        next
    else:
        # Advance the player
        Players[turn].position+=roll[0]

        # Check to see if the player passes go
        if (Players[turn].position >= nSpaces):
            Players[turn].position-=nSpaces
            Players[turn].worth+=200

        pos=Players[turn].position # to save typing
        print "You landed on "+board[pos].name # let the player know where they are

        # Actions for spaces that can be landed on
        if (board[pos].name == "Income Tax"):
            incomeTaxActions(Players[turn],board,freeParking) 

        elif (board[pos].name == 'Community Chest'):
            # Remove a card, then place it at the bottom
            comCard=comChest.pop(0)
            comChest.append(comCard)
            # Function with logice for card is in mono_module.py
            comChestLogic(comCard,Players[turn],board,freeParking,jail,Players,plyrDic)

        elif (board[pos].name == 'Chance'):
            # Remove a card, then place it at the bottom
            chaCard=chance.pop(0)
            chance.append(chaCard)
            # Will add logic for cards later
            chanceLogic(chaCard,Players[turn],board,freeParking,jail,Players,plyrDic)

        elif (board[pos].name == 'Free Parking'):
            print "You collect $"+str(board[freeParking].worth)
            Players[turn].worth+=board[freeParking].worth
            board[freeParking].worth=500

        elif (board[pos].name == 'Go To Jail'):
            Players[turn].position=jail
            Players[turn].inJail=True

        elif (board[pos].name == 'Jail'):
            print "Just visiting :)"

        elif (board[pos].name == 'Luxury Tax'):
            try:
                board[freeParking].worth+=75
                if(Players[turn].worth < 75):
                    raise tooPoor
                Players[turn].worth-=75 # Need to check player's worth
            except tooPoor:
                actionsForPoor(75,Players[turn],board,plyrDic,freeParking)            

        elif (board[pos].name == 'Go'):
            print "You landed on GO!"

        else: 
            # Function for handeling what happens when a player lands on 
            # a property
            propertyActions(Players[turn],board[pos],plyrDic,roll[0],board,False)
    

    # Check to see if the player quit
    if(Players[turn].isQuitting):
        print "Goodbye "+Players[turn].player
        del plyrDic[Players[turn].player]
        del Players[turn]

    # Check if the player rolled doulbles
    if(not roll[1]):
        turn+=1    
        cntDoubles=0
    else:
        print "You rolled doubles!"
        cntDoubles+=1
        if(cntDoubles >= 3):
            print "Going to jail for speeding!"
            Players[turn].inJail=True
            turn+=1
            cntDoubles=0

    # Go to the first player if last player has gone
    if(turn >= len(Players)):
        turn=0

    # Condition to end the game
    if(len(Players) == 1):
        print Players[0].player+" has won the game!"
        print "Thanks for playing!"

    # Wait two second before making next roll
    time.sleep(2)

    # Debugging to keep playing
    #keepRolling=str(raw_input("Keep rolling? "))
    #if (keepRolling.lower() == "n"):
    #    PlayGame=False # Here during debug to stop execution
