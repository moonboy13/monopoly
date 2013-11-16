#!/usr/bin/python

# Module to define all strings. Similar to Android practice

IMG_DIR="imgs/"

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
        self.logo=IMG_DIR+"logo.jpeg"

# Strings specific to the player selection menu
class selectStrings():
    def __init__(self):
        self.title="Player Information"
        self.sliderText="How many players?"
        self.ok="OK"
        self.cancel="Cancel"

# Player info strings
class infoStrings():
    def __init__(self):
        self.title="Player Information"
        self.name="Player Name?"
        self.pieces="Which piece would you like?"
        self.confirm="Confirm"
        self.cancel="Cancel"

# Strings Associated with the pieces
class pieceStrings():
    def __init__(self):
        self.imgDir=IMG_DIR
        self.pieceOne="Dog"
        self.pieceOneImg=self.imgDir+"dog.png"
        self.pieceTwo="Cat"
        self.pieceTwoImg=self.imgDir+"monopcat.png"
        self.pieceThree="Battleship"
        self.pieceThreeImg=self.imgDir+"battleship.png"
        self.pieceFour="Cannon"
        self.pieceFourImg=self.imgDir+"cannon.png"
        self.pieceFive="Car"
        self.pieceFiveImg=self.imgDir+"car.png"
        self.pieceSix="Hat"
        self.pieceSixImg=self.imgDir+"hat.png"
        self.pieceSeven="Shoe"
        self.pieceSevenImg=self.imgDir+"shoe.png"
        self.pieceEight="Thimble"
        self.pieceEightImg=self.imgDir+"thimble.png"
        self.pieceNine="Wheelbarrow"
        self.pieceNineImg=self.imgDir+"wheelbarrow.png"
