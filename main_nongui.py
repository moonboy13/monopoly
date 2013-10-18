#!/usr/bin/python
# This is a non gui interface to test out modules and game
# techniques.

from mono_module import *
from my_errs import *
from initialize import *
import random,time

####

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

# Intialize the board
board=makeBoard()
chance=Chance()
comChest=communityChest()

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
for i in range(1,len(Players)-1):
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
    # Inform users whose turn it is
    print "It is "+Players[turn].player+"'s turn"

    # Roll Dice and advance player
    roll=rollDice()

    # Check to see if the player is in jail first
    if (Players[turn].inJail):
        print "You are in Jail!!"
        turn=jailActions(Players[turn],turn,board,roll,freeParking)
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
            # Will add logic for cards later
            comChestLogic(comCard,Players[turn],board,freeParking,Jail,Players,plyrDic)
        
        elif (board[pos].name == 'Chance'):
            # Remove a card, then place it at the bottom
            chaCard=chance.pop(0)
            chance.append(chaCard)
            # Will add logic for cards later

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
            propertyActions(Players[turn],space,plyrDic,roll[0],board)r
    
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


    # Debugging to keep playing
    keepRolling=str(raw_input("Keep rolling? "))
    if (keepRolling.lower() == "n"):
        PlayGame=False # Here during debug to stop execution
