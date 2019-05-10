# This Python file uses the following encoding: utf-8
from PySide2 import QtCore
from PySide2 import QtWidgets
from PySide2 import QtGui

class TileStates():
    EMPTY = ' '
    PLAYER_X = 'X'
    PLAYER_O = 'O'

class TileDecision():
    ACTIVE = 0
    DRAW = 1
    WON_X = 2
    WON_O = 3




class Tile(QtWidgets.QWidget):
    def __init__(self):

        #Create an empty tile
        self.rows = 3
        self.cols = 3
        self.initializeTile()

        #Give the status of the tile in the current state.
        self.state = TileDecision.ACTIVE




    def initializeTile(self):
        QtWidgets.QWidget.__init__(self)

        #Create the tile grid. Remember, the tile is a 3 x 3 tic tac toe grid.
        #The board contains 9 of these in total.
        self.grid = QtWidgets.QGridLayout()

        #Create the "boxes" (labels) of the tile.
        self.boxes = []
        self.createBoxes()
        self.initializeBoxes()
        self.setLayout(self.grid)


    def createBoxes(self):
        #create and assign 2D array of labels.
        self.boxes = [ [QtWidgets.QLabel("Empty") for j in range(self.cols)] for i in range(self.rows) ]

    def initializeBoxes(self):
        #Set the font layout of the boxes
        boxFont = QtGui.QFont()
        boxFont.setFamily("Leelawadee UI")
        boxFont.setPointSize(15)
        boxFont.setWeight(75)
        boxFont.setBold(True)

        for i in range(self.rows):
            for j in range(self.cols):
                self.grid.addWidget( self.boxes[i][j], i, j )
                self.boxes[i][j].setFont(boxFont)
                self.boxes[i][j].setText(TileStates.EMPTY)
                self.boxes[i][j].setAlignment(QtCore.Qt.AlignCenter)



    def setMarker(self, marker, i, j):

        #First check if this tile is even able to be played.
        if self.isActive() == False:
            return


        if(self.boxes[i][j].text() == TileStates.EMPTY):
            if(marker.upper() == TileStates.PLAYER_X):
                self.boxes[i][j].setText(TileStates.PLAYER_X)
            else:
                self.boxes[i][j].setText(TileStates.PLAYER_O)
        else:
            print('Spot at ' + str(i) + ',' + str(j) + ' is already taken.')


    def checkWin(self, placeOne, placeTwo, placeThree):
        if len(set([placeOne, placeTwo, placeThree])) == 1 and placeOne != TileStates.EMPTY:
            return True
        else:
            return False

    #Checks the win of a given tile (tic-tac-toe) board
    def checkTileWin(self):

        #check rows
        for i in range(self.rows):
                if self.checkWin(self.boxes[i][0].text(), self.boxes[i][1].text(), self.boxes[i][2].text()):
                    print(self.boxes[i][0].text() + ' wins!')
                    return True
        #check columns
        for i in range(self.cols):
                if self.checkWin(self.boxes[0][i].text(), self.boxes[1][i].text(), self.boxes[2][i].text()):
                    print(self.boxes[0][i].text() + ' wins!')
                    return True

        #check diagonals
        if self.checkWin(self.boxes[0][0].text(), self.boxes[1][1].text(), self.boxes[2][2].text()):
                print(self.boxes[0][0].text() + ' wins!')
                return True
        elif self.checkWin(self.boxes[0][2].text(), self.boxes[1][1].text(), self.boxes[2][0].text()):
                print(self.boxes[0][2].text() + ' wins!')
                return True

        return False

    #Checks to see if the tile is full.
    def isFull(self):

        for i in range (self.rows):
            for j in range (self.cols):
                if self.boxes[i][j].text() == TileStates.EMPTY:
                    return False
        return True

    def isActive(self):
        return self.state == TileDecision.ACTIVE


