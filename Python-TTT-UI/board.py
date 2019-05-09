# This Python file uses the following encoding: utf-8
from PySide2 import QtCore
from PySide2 import QtWidgets
from tile import tile

class board(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)

        #The board just represents a simple grid
        self.resize(200, 200)
        self.setStyleSheet("background-color: rgb(25, 45, 66);")
        self.grid = QtWidgets.QGridLayout()
        self.grid.addWidget( tile(), 1, 0 )
        self.setLayout(self.grid)
