#This Python file uses the following encoding: utf-8
import sys
from PySide2 import QtCore, QtGui, QtWidgets
from board_qt import board
from tile_qt import TileStates


#May not need these
from random import randint

class MainBoard(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.initializeBoard()


    #Initialize the board. This modifies the window with basic settings.
    def initializeBoard(self):
        self.setWindowTitle("Board")
        self.resize(1000, 800)
        self.setStyleSheet("background-color: rgb(90, 180, 180);")

        self.gameBoard = board()
        self.setCentralWidget(self.gameBoard)

    def makeMove(self, marker, boardRow, boardCol, tileRow, tileCol):
        self.gameBoard.setMarker(marker, boardRow, boardCol, tileRow, tileCol)

    def getGameBoard(self):
        return self.gameBoard




#if __name__ == "__main__":


#    app = QtWidgets.QApplication([])
#    game = MainBoard()
#    game.show()
#    sys.exit(app.exec_())

#    gameBoard = game.getGameBoard()
#    main()
#    testTile = gameBoard.getTileAt(0,0)
#    print('hi')

#    counter = 0;
#    print(counter)
#    print(testTile.isFull())

#    while testTile.isFull() is not True:
#        x = randint(0, 2)
#        y = randint(0, 2)
#        testTile.setMarker(TileStates.PLAYER_X, x, y)
#        if testTile.checkTileWin():
#            break

#        x = randint(0, 2)
#        y = randint(0, 2)
#        testTile.setMarker(TileStates.PLAYER_O, x, y)
#        if testTile.checkTileWin():
#            break


    #sys.exit(app.exec_())

