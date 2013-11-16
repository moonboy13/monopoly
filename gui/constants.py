#!/usr/bin/python

# File to hold all the constant variables in different classes

# Class for global variables
class globalVars():
    def __init__(self):
        # List for Human and AI player instances
        self.humanPlayers=list()
        self.AIPlayers=list()
        # Dictionary for player, piece associations
        self.playerPieces=dict()
        # List of available pieces
        self.avaliablePieces=[True, True, True, True, True, True,
                              True, True, True]

# Number of players slection
class nPlayersCnsts():
    def __init__(self):
        self.WIDTH=225
        self.HEIGHT=78
        self.MAX_PLAYERS=9
        self.MIN_PLAYERS=2
        self.BORDER_WIDTH=5

# Player information constants
class playerInfoCnsts():
    def __init__(self):
        #self.WIDTH=500
        #self.HEIGHT=500
        self.BORDER_WIDTH=5
        self.N_BUTTONS=9
