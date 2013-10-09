#!/usr/bin/python
# Stuff to run on startup

from mono_module import *

def makeBoard():
    # Open file and read in the properties
    propFile=open("properties.txt",'r')
    props=[]
    for line in propFile:
        line=line.strip()
        vals=line.split('|')
        if (vals[0] is '# Name'):
            next
        else:
            props.append(Property(vals[0],vals[1],vals[2],vals[3],vals[4],
                                  vals[5],vals[6],vals[7],vals[8],vals[9],
                                  vals[10]))

    return props

makeBoard() 
