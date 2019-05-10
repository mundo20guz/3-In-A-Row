#  ____      _____                         _____                
# |___ \    |_   _|             /\        |  __ \               
#   __) |_____| |  _ __ ______ /  \ ______| |__) |_____      __ 
#  |__ <______| | | '_ \______/ /\ \______|  _  // _ \ \ /\ / / 
#  ___) |    _| |_| | | |    / ____ \     | | \ \ (_) \ V  V /  
# |____/    |_____|_| |_|   /_/    \_\    |_|  \_\___/ \_/\_/   
#                                                                                                                              
#
# Game.py
#  
# Includes code for developing game board. Includes initial mash up of game board
# and states of possible moves.
#
# Dependencies
import sys
import os
from board import *
from player import *
from minimax import *

###############################################################################

class Game(object):

	@property
	def numMoves(self):
		return self.__numMoves

	@numMoves.setter
	def numMoves(self,val):
		self.__numMoves = val
	
	def __init__(self,board,playerX,playerO):
		""" Constructor for start of new game """
		self.board = board
		self.player_X = playerX
		self.player_O = playerO
		self.numMoves = 0

	def startGame(self):
		""" Create Logic to start and play a game """
		while self.board.status == GameStatus.ACTIVE:
			self.player_X.makeMove(self.board,self)
			if self.board.status != GameStatus.ACTIVE:
				break
			self.player_O.makeMove(self.board,self)
			self.numMoves += 1
		return self.board.status

	def getRandomMove(self,player):
		Player(playerName=player)
		player.makeMove(self.board)

