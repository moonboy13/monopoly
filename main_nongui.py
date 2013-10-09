#!/usr/bin/python
# This is a non gui interface to test out modules and game
# techniques.

from mono_module import *
from my_errs import *
from initialize import *
import random

####

def rollDice():
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
            for item in valid:
                print item
        elif(tokens[piece]):
            piece=None
            print "Piece is taken, please choose another:"
            for item in valid:
                print item
        else:
            cur.piece=piece
            tokens[piece]=True
            
    
    Players.append(cur)

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
    print roll[0]

    # Check to see if the player is in jail first
    if (Players[turn].inJail):
        print "You are in Jail!!"
        # See if player can pay to leave jail
        if(Players[turn].worth < 50):
            print "Too poor to post bail!"
            # If they can't then see if they rolled doubles
            if (roll[1]):
                print "You rolled doubles!"
                Players[turn].inJail=False
                Players[turn].jailCounter=0
                turn+=1
            else:
                print "No luck!"
                Playerso[turn].jailCounter+=1
                # They can leave if they've been in here three turns
                if(Players[turn].jailCounter >= 3):
                    print "You've served your time and can move again"
                    Players[turn].inJail=False
                    Players[turn].jailCounter=0
        else:
            # Check if they want to post bail
            bailAnswer=str(raw_input("Would you like to pay $50 bail[y/N]?"))
            if(bailAnswer.lower() == 'y'):
                print "Payment recieved"
                board[freeParking].value+=50
                Players[turn].worth-=50
                Players[turn].inJail=False
                Players[turn].jailCounter=0
            else:
                print "Trying your luck then"
                if (roll[1]):
                    print "You rolled doubles!"
                    Players[turn].inJail=False
                    Players[turn].jailCounter=0
                    turn+=1
                else:
                    print "No luck!"
                    Players[turn].jailCounter+=1
                    if(Players[turn].jailCounter >= 3):
                        print "You've served your time and can move again"
                        Players[turn].inJail=False
                        Players[turn].jailCounter=0     



           
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
            incomeTaxChoice=None
            while not incomeTaxChoice:
                temp=str(raw_input("Choose to pay [a]10% of worth ("+Players[turn].worth+
                                   ") or [b]pay $200: "))
                if(temp != 'a' or temp != 'b'):
                    print "Invalid Choice!"
                elif(temp == 'a'):
                    board[freeParking].value+=(0.1*Players[turn].worth)
                    Players[turn].worth-=(0.1*Players[turn].worth)
                    incomeTaxChoice='a'
                else:
                    board[freeParking].value+=200
                    Players[turn].worth-=200
                    incomeTaxChoice='b'
         
        elif (board[pos].name == 'Community Chest'):
            # Remove a card, then place it at the bottom
            comCard=comChest.pop(0)
            comChest.append(comCard)
            # Will add logic for cards later
        
        elif (board[pos].name == 'Chance'):
            # Remove a card, then place it at the bottom
            chaCard=chance.pop(0)
            chance.append(chaCard)
            # Will add logic for cards later

        elif (board[pos].name == 'Free Parking'):
            Players[turn].worth+=board[freeParking].value
            board[freeParking].value=500

        elif (board[pos].name == 'Go To Jail'):
            Players[turn].position=jail
            Players[turn].inJail=True

        elif (board[pos].name == 'Jail'):
            print "Just visiting :)"

        elif (board[pos].name == 'Luxury Tax'):
            Players[turn].worth-=75 # Need to check player's worth
            board[freeParking].value+=75

        else: 
            print board[pos].owner
    
    # Check if the player rolled doulbles
    if(not roll[1]):
        turn+=1    
        cntDoubles=0
    else:
        print "You rolled doubles!"
        cntDoubles+=1
        if(cntDoubles >= 3):
            print "Going to jail for speeding!"
            Player[turn].inJail=True
            turn+=1
            cntDoubles=0

    # Go to the first player if last player has gone
    if(turn >= len(Players)):
        turn=0


    # Debugging to keep playing
    keepRolling=str(raw_input("Keep rolling? "))
    if (keepRolling.lower() == "n"):
        PlayGame=False # Here during debug to stop execution
