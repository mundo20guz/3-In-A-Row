# This Python file uses the following encoding: utf-8
from PySide2 import QtCore
from PySide2 import QtWidgets
from tile_qt import Tile

class board(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)

        #Declare rows/columns:
        self.rows = 3
        self.cols = 3

        #The board just represents a simple grid
        self.resize(200, 200)
        self.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.grid = QtWidgets.QGridLayout()

        #Initialize tiles
        self.tiles = [ [Tile() for j in range(self.cols)] for i in range(self.rows) ]
        for i in range(self.rows):
            for j in range(self.cols):
                self.grid.addWidget(self.tiles[i][j], i, j)

        self.setLayout(self.grid)

    def setMarker(self, marker, boardRow, boardCol, tileRow, tileCol):
        self.tiles[boardRow][boardCol].setMarker(marker, tileRow, tileCol)

    def getTileAt(self, i, j):
        return self.tiles[i][j]


