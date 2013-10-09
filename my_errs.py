#!/usr/bin/python
# module to contain my personal errors

class TooManyPlayers(Exception):
    def __init__(self,players):
        self.nplayers=str(players)
