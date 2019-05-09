# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'board.ui',
# licensing of 'board.ui' applies.
#
# Created: Wed May  8 22:37:39 2019
#      by: pyside2-uic  running on PySide2 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Board(object):
    def setupUi(self, Board):
        Board.setObjectName("Board")
        Board.resize(912, 545)
        Board.setStyleSheet("background-color: rgb(255, 255, 255);")

        #Set up the central widget.
        self.centralWidget = QtWidgets.QWidget(Board)
        self.centralWidget.setAutoFillBackground(False)
        self.centralWidget.setStyleSheet("background-color:rgb(0, 0, 0)")
        self.centralWidget.setObjectName("centralWidget")

        #Add the grid layout to the central widget
        self.gridLayout = QtWidgets.QGridLayout(self.centralWidget)
        self.gridLayout.setContentsMargins(9, -1, -1, -1)
        self.gridLayout.setObjectName("gridLayout")


        self.retranslateUi(Board)
        QtCore.QMetaObject.connectSlotsByName(Board)

    def retranslateUi(self, Board):
        Board.setWindowTitle(QtWidgets.QApplication.translate("Board", "Form", None, -1))

