#!/usr/bin/python

# Module to define all strings. Similar to Android practice

# Global strings
class univStrings():
    def __init__(self):
        self.DEVS="Kyle Conlon"
        self.STYLE="alt"

# Strings specific to start menu
class startStrings():
    def __init__(self):
        self.title="Monopoly Start Menu!"
        self.startButton="Begin Game!"
        self.exitButton="Exit"
        self.logo="imgs/logo.jpeg"
        self.nextMenu="./player_select.py"

# Strings specific to the player selection menu
class selectStrings():
    def __init__(self):
        self.title="Player Information"
        self.sliderText="How many players?"
        self.ok="OK"
        self.cancel="Cancel"
