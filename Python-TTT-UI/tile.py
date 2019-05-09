# This Python file uses the following encoding: utf-8
from PySide2 import QtCore
from PySide2 import QtWidgets

class tile(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)

        #Create the tile grid. Remember, the tile is a 3 x 3 tic tac toe grid.
        #The board contains 9 of these in total.
        self.grid = QtWidgets.QGridLayout()

        #Create the "boxes" (labels) of the tile.



        self.grid.addWidget( QtWidgets.QLabel("1"), 0, 1 )
        self.grid.addWidget( QtWidgets.QLabel("2"), 0, 2 )

        self.setLayout(self.grid)


    def createBoxes():
        rows = 3
        cols = 3

        #create and assign 2D array of labels.

