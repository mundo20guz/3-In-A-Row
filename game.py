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
# Includes code for creating a Game. Creates board, and 2 players. Includes logic to
# create sequence of game. Will determine winner.

# Dependencies
from board import *
from player import *

###############################################################################

class Game(object):

	""" Property Getters """
	@property
	def numMoves(self):
		return self.__numMoves

	""" Property Setters """
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

