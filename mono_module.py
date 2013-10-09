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

# Defining a class for the Properties
class Property:
    """Class Containing a Properties information"""
    def __init__(self,propertyName,propertyPrice,houseCost,propertyRent,propertyGroup,
                 morgageValue,oneHouse,twoHouse,threeHouse,fourHouse,hotelRent):
        self.name=proptertyName
        self.owner="Bank"
        self.cost=propertyPrice
        self.rent=propertyRent
        self.buildCost=houseCost
        self.nhouse=0
        self.hotel=False
        self.group=propteryGroup
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
