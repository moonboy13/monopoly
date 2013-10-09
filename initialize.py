#!/usr/bin/python
# Stuff to run on startup

from mono_module import *
import random

def makeBoard():
    propFile=open("textfiles/properties.txt",'r')
    lines=propFile.readlines()
    lines=lines[1:]
    props=[]
    for line in lines:
        line=line.strip()
        vals=line.split('|')
        props.append(Property(vals[0],vals[1],vals[2],vals[3],vals[4],
                                  vals[5],vals[6],vals[7],vals[8],vals[9],
                                  vals[10]))

    # Define the board
    board=[Space('Go'),props[0],Space('Community Chest'),props[1],Space('Income Tax'),
           props[22],props[2],Space('Chance'),props[3],props[4],Space('Jail'),props[5],
           props[26],props[6],props[7],props[19],props[8],Space('Community Chest'),
           props[9],props[10],Space('Free Parking'),props[11],Space('Chance'),
           props[12],props[13],props[24],props[14],props[15],props[27],props[16],
           Space('Go To Jail'),props[17],props[18],Space('Community Chest'),props[19],
           props[25],Space('Chance'),props[20],Space('Luxury Tax'),props[21]]
    return board

def communityChest():
    """Read in and return the community chest deck"""
    comFile=open("textfiles/community_chest.txt",'r')
    lines=comFile.readlines()
    comChest=list()
    for line in lines:
        line=line.strip()
        comChest.append(line)

    random.shuffle(comChest)
    return comChest


def Chance():
    """Read in and return the chance deck"""
    chaFile=open("textfiles/chance.txt",'r')
    lines=chaFile.readlines()
    chance=list()
    for line in lines:
        line=line.strip()
        chance.append(line)

    random.shuffle(chance)
    return chance
