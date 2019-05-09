# This Python file uses the following encoding: utf-8
import sys
from PySide2 import QtCore, QtGui, QtWidgets
from board import board

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.initializeBoard()

    #Initialize the board. This modifies the window with basic settings.
    def initializeBoard(self):
        self.setWindowTitle("Board")
        self.resize(805, 507)

        self.setCentralWidget(board())


    def fillBoard():
        #Donothingyet
        self.layout






if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

