#!/usr/bin/python
# module for monopoly

from my_errs import *
import random, time

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
        self.nRail=0
        self.nUtil=0
        self.isQuitting=False

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
        self.cost=int(propertyPrice)
        self.rent=int(propertyRent)
        self.buildCost=int(houseCost)
        self.nhouse=0
        self.hotel=False
        self.group=propertyGroup
        self.morgageVal=int(morgageValue)
        self.oneHouse=int(oneHouse)
        self.twoHouse=int(twoHouse)
        self.threeHouse=int(threeHouse)
        self.fourHouse=int(fourHouse)
        self.hotelRent=int(hotelRent)
        self.morgaged=False

    def buildHotel(self):
        if (self.nhouse < 4):
            return "Must build 4 houses first"
        else:
            self.hotel=True

# Function for dealing with options in jail
def jailActions(player,board,roll,freeParking):
    # See if the player has a get out of jail free card
    if(player.getOutFree):
        use=str(raw_input("Use your get out of jail free card[Y/n]? "))
        if(use == 'n'):
            print "okay..."
        else:
            player.inJail=False
            exit()
             
    # See if player can pay to leave jail
    if(player.worth < 50):
        print "Too poor to post bail!"
        # If they can't then see if they rolled doubles
        if (roll[1]):
            print "You rolled doubles!"
            player.inJail=False
            player.jailCounter=0
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
            else:
                print "No luck!"
                player.jailCounter+=1
                if(player.jailCounter >= 3):
                    print "You've served your time and can move again"
                    player.inJail=False
                    player.jailCounter=0





# Actions for landing on the income tax space
def incomeTaxActions(player,board,freeParking):
    """Actions to perform if the player lands on income tax space"""
    incomeTaxChoice=None
    while not incomeTaxChoice:
        temp=str(raw_input("Choose to pay [a]10% of worth ("+
                           str(player.worth)+") or [b]pay $200: "))
        if(temp == 'a'):
            print "Paying 10%"
            board[freeParking].worth+=int(0.1*player.worth)
            player.worth-=int(0.1*player.worth)
            incomeTaxChoice='a'
        else:
            print "Paying $200"
            board[freeParking].worth+=200
            player.worth-=200
            incomeTaxChoice='b'

# Function for the Chance cards
def chanceLogic(card,player,board,freeParking,Jail,Players,plyrDic):
    print card # Debuggin
    # split the card into separate words
    pieces=card.split()
    # simple cases first
    if (len(pieces) == 2):
        if(pieces[0] == "collect"):
            player.worth+=int(pieces[1])
        else:
            board[freeParking].worth+=int(pieces[1])
            try:
                if(int(pieces[1]) > player.worth):
                    raise tooPoor

                player.worth-=int(pieces[1])
            except tooPoor:
                actionsForPoor(int(pieces[1]),player,board,plyrDic,freeParking)
    elif(card == "get out of jail free"):
        player.getOutFree=True
    # Advance to a specific space
    elif(pieces[0] == "advance" ):
        # GO
        if(pieces[2] == "Go"):
            player.position=0
            player.worth+=200
        # Illinois Ave
        elif(pieces[2] == "Illinois"):
            # Check to see if the player passes by Go
            if (player.position > 24):
                player.worth+=200

            player.position=24
            propertyActions(player,board[24],plyrDic,0,board,False)
        # Go back 3 spaces(will never cause you to got over go)
        elif(pieces[2] == 3):
            print "going back 3 spaces plays hell with me"
        # Go to jail
        elif(pieces[2] == "jail"):
            player.position=10
            player.inJail=True
        # Go to Reading Rail
        elif(pieces[2] == "Reading"):
            # Check to see if the player passes by Go
            if (player.position > 5):
                player.worth+=200

            player.position=5
            propertyActions(player,board[5],plyrDic,0,board,False)
        # Go to Boardwalk (note player cannot pass go)
        elif(pieces[2] == "Boardwalk"):
            player.position=39
            propertyActions(player,board[39],plyrDic,0,board,False)
        # Nearest Utility
        elif(pieces[3] == "utility"):
            while board[player.position].group != "utility":
                player.position+=1
            # Re-roll
            random.seed(time.time())
            roll=random.randint(1,6)+random.randint(1,6)
            propertyActions(player,board[player.position],plyrDic,roll,board,True)
        # Nearest Rail
        elif(pieces[3] == "railroad"):
            while board[player.position].group != "rail":
                player.position+=1
            
            propetyActions(player,board[player.position],plyrDic,0,board,True)

    # paying each player $50
    elif(pieces[4] == "player"):
        debt=len(Players)*int(pieces[1])
        for person in Players:
            person.worth+=int(pieces[1])

        try:
            if(player.worth < debt):
                raise tooPoor

            player.worth-=debt
        except tooPoor:
            actionsForPoor(debt,player,board,plyrDic,freeParking)
    else:
        print "Stuff with paying for houses and hotels"

# Function to deal with Community Chest cards
def comChestLogic(card,player,board,freeParking,Jail,Players,plyrDic):
    print card # Debuggin
    pieces=card.split()
    # Take care of the easy situations first
    if (len(pieces) == 2):
        if(pieces[0] == "collect"):
            player.worth+=int(pieces[1])
        elif(pieces[0] == "pay"):
            board[freeParking].worth+=int(pieces[1])
            try:
                if (player.worth < int(pieces[1])):
                    raise tooPoor

                player.worth-=int(pieces[1])
            except tooPoor:
                actionsForPoor(int(pieces[1]),player,board,plyrDic,freeParking) 
    elif(card == "get out of jail free"):
        player.getOutFree=True
    elif(pieces[0] == "advance"):
        if (pieces[2] == "Go"):
            player.position=0
            player.worth+=200
        else:
            player.position=Jail
            player.inJail=True
    elif(pieces[4] == "player"):
        player.worth+=int(pieces[1]*len(Players))
        for plry in Players:
            plry.worth-=int(pieces[1])
    else:
        print "pay for houses"

# Function for quiting
def quitFunction(player):
    """This function destroys the player and returns their properites to the bank when they
       quit"""
    print player
    print "Goodbye "+player.player
    for prop in player.properties.keys():
        player.properties[prop].owner="Bank"
        player.properties[prop].nhouse=0
        player.properties[prop].hotel=False
        player.isQuitting=True


# Function to deal with the poor
def actionsForPoor(debt,player,board,plyrDic,freeParking):
    # Figure out how to pay the debt
    remainingDebt=debt-player.worth
    player.worth=0
    # Ask the player if they want to quit
    print player.player+" your remaining debt is $"+str(remainingDebt)
    quit=str(raw_input(player.player+", do you want to quit[y/N]?"))
    if(quit == 'y'):
        print "Okay, you can quit"
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
                        removalNumber=int(raw_input("How many houses to remove? "))
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
                        print propMorgage+" can be morgaged for $"+str(player.properties[propMorgage].morgageVal)

                # Check that there really are morgageable properties and if there
                # aren't any force the player to quite
                if (len(optionsMorgages) == 0):
                    print "No properties can be morgaged"
                    print "Sorry, you must quit"
                    quitFunction(player)
                    break
                else:
                    # Get the player's choice in morgage
                    setOptionsMorgages=set(optionsMorgages)
                    morgageChoice=None
                    while not morgageChoice:
                        morgageChoice=str(raw_input("Please enter EXACT name (case sensitive) of the property to be morgaged: "))
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

# Function to handle landing on a property
def propertyActions(player,space,plyrDic,roll,board,chance):
    """This funciton handles the actions of what happens if a player lands on a property"""
    # First check if the property is owned, if not check to see if the player can buy
    # it.
    if space.owner == "Bank":
        if player.worth >= space.cost:
            buyChoice=str(raw_input("Would you like to purchase "+space.name+" for $"+\
                                    str(space.cost)+"[y/N]? "))
            if buyChoice.lower() == 'y':
                print "You just bought "+space.name+" for $"+str(space.cost)
                player.worth-=space.cost
                space.owner=player.player
                player.properties[space.name]=space
                if(space.group == "rail"):
                    player.nRail+=1
                elif(space.group == "util"):
                    player.nUtil+=1

        else:
            print "Sorry, your cash reserves of $"+str(player.worth)+\
                  " is not enough to purchase this property."
    elif space.owner == player.player:
        print "Landed on your own space!"
    else:
        owner=plyrDic[space.owner]
        if(space.group == 'rail'):
            # Determine the rails rent
            if(owner.nRail == 1):
                rent=25
            elif(owner.nRail == 2):
                rent=50
            elif(owner.nRail == 3):
                rent=100
            else:
                rent=200
            
            if(chance):
                rent*=2

        elif(space.group == 'utility'):
            # Determine the utilities rent
            if(owner.nUtil == 2 or chance):
                rent=roll*10
            else:
                rent=roll*4
        else:
            # Determine the rent
            if(space.hotel):
                rent=space.hotelRent
            elif(space.nhouse == 4):
                rent=space.fourHouse
            elif(space.nhouse == 3):
                rent=space.threeHouse
            elif(space.nhouse == 2):
                rent=space.twoHouse
            elif(space.nhouse == 1):
                rent=space.oneHouse
            else:
                rent=space.rent

        # Check to see if the owner is in jail before trying to pay rent
        if(owner.inJail):
            print owner.player+" is in Jail and cannot collect rent!"
        else:
            # Pay the owner
            print "Paying "+owner.player+" $"+str(rent)+" in rent."
            owner.worth+=rent
        
            # Check to see if the player can pay the rent
            try:
                if(player.worth < rent):
                    raise tooPoor
                player.worth-=rent
            except tooPoor:
                actionsForPoor(rent,player,board,plyrDic,20)
