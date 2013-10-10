#!/usr/bin/python
# module for monopoly

# Definining a class for Pieces
class Player:
    """Class containing the Players information"""
    def __init__(self,playerName):
        self.getOutFree=False
        self.player=playerName
        self.piece=""
        self.worth=2000
        self.properties=[]
        self.space=0
        self.inJail=False
        self.jailCounter=0
        self.position=0

# Generic class for spaces
class Space:
    """Generic place for spaces"""
    def __init__(self,spaceName):
        self.name=spaceName
        if (self.name == 'Free Parking'):
           self.value=500

# Defining a class for the Properties
class Property:
    """Class Containing a Properties information"""
    def __init__(self,propertyName,propertyPrice,houseCost,propertyRent,propertyGroup,
                 morgageValue,oneHouse,twoHouse,threeHouse,fourHouse,hotelRent):
        self.name=propertyName
        self.owner="Bank"
        self.cost=propertyPrice
        self.rent=propertyRent
        self.buildCost=houseCost
        self.nhouse=0
        self.hotel=False
        self.group=propertyGroup
        self.morgageval=morgageValue
        self.oneHouse=oneHouse
        self.twoHouse=twoHouse
        self.threeHouse=threeHouse
        self.fourHouse=fourHouse
        self.hotelRent=hotelRent

    def buildHotel(self):
        if (self.nhouse < 4):
            return "Must build 4 houses first"
        else:
            self.hotel=True

# Function for dealing with options in jail
def jailActions(player,turn,board,roll,freeParking):
    # See if the player has a get out of jail free card
    if(player.getOutFree):
        use=str(raw_input("Use your get out of jail free card[Y/n]? "))
        if(use == 'n'):
            print "okay..."
        else:
            return turn 
    # See if player can pay to leave jail
    if(player.worth < 50):
        print "Too poor to post bail!"
        # If they can't then see if they rolled doubles
        if (roll[1]):
            print "You rolled doubles!"
            player.inJail=False
            player.jailCounter=0
            turn+=1
        else:
            print "No luck!"
            player.jailCounter+=1
            # They can leave if they've been in here three turns
            if(player.jailCounter >= 3):
                print "You've served your time and can move again"
                player.inJail=False
                player.jailCounter=0
    else:
        # Check if they want to post bail
        bailAnswer=str(raw_input("Would you like to pay $50 bail[y/N]?"))
        if(bailAnswer.lower() == 'y'):
            print "Payment recieved"
            board[freeParking].value+=50
            player.worth-=50
            player.inJail=False
            player.jailCounter=0
        else:
            print "Trying your luck then"
            if (roll[1]):
                print "You rolled doubles!"
                player.inJail=False
                player.jailCounter=0
                turn+=1
            else:
                print "No luck!"
                player.jailCounter+=1
                if(player.jailCounter >= 3):
                    print "You've served your time and can move again"
                    player.inJail=False
                    player.jailCounter=0




    return turn

# Actions for landing on the income tax space
def incomeTaxActions(player,board,freeParking):
    """Actions to perform if the player lands on income tax space"""
    incomeTaxChoice=None
    while not incomeTaxChoice:
        temp=str(raw_input("Choose to pay [a]10% of worth ("+
                           str(player.worth)+") or [b]pay $200: "))
        if(temp == 'a'):
            print "Paying 10%"
            board[freeParking].value+=(0.1*player.worth)
            player.worth-=(0.1*player.worth)
            incomeTaxChoice='a'
        else:
            print "Paying $200"
            board[freeParking].value+=200
            player.worth-=200
            incomeTaxChoice='b'

# Function to deal with Community Chest cards
def comChestLogic(card,player,board,freeParking,Jail):
    print card # Debuggin
    pieces=card.split()
    # Take care of the easy situations first
    if (len(pieces) == 2):
        if(pieces[0] == "collect"):
            player.worth+=pieces[1]
        elif(pieces[0] == "pay"):
            board[freeParking]+=pieces[1]
            try:
                if (player.worth < pieces[1]):
                    raise tooPoor

                player.worth-=pieces[1]
            except tooPoor:
                print need to do stuff if poor 
    elif(card == "get out of jail free")
        player.getOutFree=True
    elif(pieces[0] == "advance"):
        if (pieces[3] == "Go"):
            player.position=0
            player.worth+=200
        else:
            player.position=Jail
            player.inJail=True
