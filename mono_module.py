#!/usr/bin/python
# module for monopoly

# Definining a class for Pieces
class Player:
    """Class containing the Players information"""
    def __init__(self,playerName):
        self.player=playerName
        self.piece=""
        self.worth=2000
        self.properties=[]
        self.space=0
        self.inJail=False
        self.jailCounter=0
        self.position=0

class Space:
    """Generic place for spaces"""
    def __init__(self,spaceName):
        self.name=spaceName
        if (self.name is 'Free Parking'):
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
