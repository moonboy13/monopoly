#!/usr/bin/python
# module for monopoly

from my_errs import *

# Definining a class for Pieces
class Player:
    """Class containing the Players information"""
    def __init__(self,playerName):
        self.hasHouses=False
        self.getOutFree=False
        self.player=playerName
        self.piece=""
        self.worth=2000
        self.properties={}
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
           self.worth=500

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
        self.morgageVal=morgageValue
        self.oneHouse=oneHouse
        self.twoHouse=twoHouse
        self.threeHouse=threeHouse
        self.fourHouse=fourHouse
        self.hotelRent=hotelRent
        self.morgaged=False

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
            board[freeParking].worth+=50
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
            board[freeParking].worth+=(0.1*player.worth)
            player.worth-=(0.1*player.worth)
            incomeTaxChoice='a'
        else:
            print "Paying $200"
            board[freeParking].worth+=200
            player.worth-=200
            incomeTaxChoice='b'

# Function to deal with Community Chest cards
def comChestLogic(card,player,board,freeParking,Jail,Players,plyrDic):
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
                actionsForPoor(pieces[1],player,"Free Parking",board,plyrDic,freeParking) 
    elif(card == "get out of jail free"):
        player.getOutFree=True
    elif(pieces[0] == "advance"):
        if (pieces[3] == "Go"):
            player.position=0
            player.worth+=200
        else:
            player.position=Jail
            player.inJail=True
    elif(pieces[4] == "player"):
        player.worth+=(pieces[1]*len(Players))
        for plry in Players:
            plry.worth-=pieces[1]
    else:
        print "pay for houses"

# Function for quiting
def quitFunction(player):
    """This function destroys the player and returns their properites to the bank when they
       quit"""
    for prop in player.properties.keys()
        player.properties[prop].owner="Bank"
        player.properties[prop].nhouse=0
        player.properties[prop].hotel=False

    del player


# Function to deal with the poor
def actionsForPoor(debt,player,debtor,board,plyrDic,freeParking):
    # first determine who is getting payed
    if (debtor == "Free Parking"):
        board[freeParking].worth+=debt
    else:
        plyrDic[debtor].worth+=debt

    # Figure out how to pay the debt
    remainingDebt=debt-player.worth
    player.worth=0
    # Ask the player if they want to quit
    quit=str(raw_input("Do you want to quit[y/N]?"))
    if(quit == 'y'):
        quitFunction(player)
    else:
        while remainingDebt > 0:
            print "You owe "+str(remainingDebt)
            # First remove houses
            if(player.hasHouses):
                houseChoice=str(raw_input("Do you want to remove houses[y/N]? "))
                if(houseChoice == 'y'):
                    optionsHouses=[]
                    print "Choose a property to remove houses from"
                    for propHouses in player.properties.keys():
                        if(player.properties[propHouses].hasHouses):
                            optionsHouses.push(propHouses)
                            print propHouses+" has "+str(player.properties[propHouses].nHouses)+" houses"
                            print "Each worth $"+str(player.properties[propHouses].buildCost)

                    setOptionsHouses=set(optionsHouses)
                    # First choose a property to remove pieces from
                    removalChoice=None
                    while not removalChoice:
                        removalChoice=str(raw_input(": "))
                        if (not removalChoice in setOptionsHouses):
                            removalChoice=None
                            print "not a valid choice"
                            print setOptionsHouses

                    # Now select the number of houses to remove
                    removalNumber=None
                    while not removalNumber:
                        removalNumber=int(raw_input("How many houses to remove? ")
                        if(removalNumber > player.properties[removalChoice].nHouses):
                            print "Removing all houses on "+removalChoice
                            removalNumber=player.properties[removalChoice].nHouses

                    # Update the number of properties on the house
                    player.properties[removalChoice].nHouses-=removalNumber 
                    valueHouses=removalNumber*player.properties[removalChoice].buildCost
                    # See how much of the debt is left
                    if(valueHouses >= remainingDebt):
                        player.worth=valueHouses-remainingDebt
                        remainingDebt=0
                    else:
                        remainingDebt-=valueHouses

            # If you don't want to sell back houses
            else:
                optionsMorgages=[]
                # Display morgagable properties
                print "Choose a property to morgage"
                for propMorgage in player.properties.keys():
                    if(not player.properties[propMorgage].hasHouses and 
                       not player.properties[propMorgage].morgaged ):
                        optionsMorgages.append(propMorgage)
                        print propMorgage+" can be morgaged for $"+str(player.properties[propMorgage].morgageVal

                # Check that there really are morgageable properties
                if (len(optionsMorgages) == 0):
                    print "No properties can be morgaged"
                else:
                    # Get the player's choice in morgage
                    setOptionsMorgages=set(optionsMorgages)
                    morgageChoice=None
                    while not morgageChoice:
                        morgageChoice=str(raw_input("Please enter EXACT name (case sensitive) of 
                                                     the property to be morgaged: "))
                        if(not morgageChoice in setOptionsMorgages):
                            morgageChoice=None
                            print "Invalid property name"
                            print setOptionsMorgages

                    # Can't let them morgage the same property twice
                    player.properties[morgageChoice].morgaged=True
                    # Update debt
                    if(player.properties[morgageChoice].morgageVal >= remainingDebt):
                        player.worth=player.properties[morgageChoice].morgageVal-remainingDebt
                        remainingDebt=0
                    else:
                        remainingDebt-=player.properties[morgageChoice].morgageVale
