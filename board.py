#
#  ____      _____                         _____                
# |___ \    |_   _|             /\        |  __ \               
#   __) |_____| |  _ __ ______ /  \ ______| |__) |_____      __ 
#  |__ <______| | | '_ \______/ /\ \______|  _  // _ \ \ /\ / / 
#  ___) |    _| |_| | | |    / ____ \     | | \ \ (_) \ V  V /  
# |____/    |_____|_| |_|   /_/    \_\    |_|  \_\___/ \_/\_/   
#                                                                                                                              
#
# Board.py
#  
# Includes code for developing game board. Includes initial mash up of original 
# tic-tac-toe game board. Also includes code for super tic-tac-toe board.
#
# Dependencies
import sys
import os
from enum import Enum

#############################################################################

class GridState(Enum):
	""" Includes states of individual grids
	@EMPTY = Not occupied by either player
	@PLAYER_X = Occupied by Player X
	PLAYER_O = Occupied by Player Z
	"""
	EMPTY = ''
	PLAYER_X = 'X'
	PLAYER_O = 'O'


class GameStatus(Enum):
	""" Includes status of individual games
	@ACTIVE = Game still in progress
	@DRAW = Game resulted in a draw
	@X_WIN = Player X wins game
	@O_WIN = Player O wins game
	"""
	ACTIVE = 0
	DRAW = 1
	X_WIN = 2
	O_WIN = 3


##################### Normal Tic-Tac-Toe Board #############################

class Normal_Board():
	""" Creates normal 3x3 tic-tac-toe grid """

	""" Property Getters """

	@property
	def status(self):
		""" Returns Status of Current Game """
		return self.__status

	""" Property Setters """ 

	@status.setter
	def status(self,game_status):
		""" Sets Status of Current Game to 'game_status' """
		self.__status = game_status
	

	def __init__(self):
		""" Creates a new game board """
		self.create_board(self.clear_board())
		status = GameStatus.ACTIVE


	def create_board(self,game_board):
		""" Creates GUI for game board """
		pass


	def clear_board(self):
		""" Creates an Empty Tic-Tac-Toe Grid """
		return [[GridStates.EMPTY] [GridStates.EMPTY] [GridStates.EMPTY],
				[GridStates.EMPTY] [GridStates.EMPTY] [GridStates.EMPTY],
				[GridStates.EMPTY] [GridStates.EMPTY] [GridStates.EMPTY]]


	def check_for_win(self):
		""" Checks to see if game has ended, otherwise updates game status """
		pass


	def makeMove(self,player,i_pos,j_pos):
		""" Marks game board with player move
		@param player: Player X or Player O
		@param i_pos: row of move (starting with 0)
		@param j_pos: column of move (starting with 0)
		"""
		pass

	def empty_spaces(self):
		""" Returns locations of empty board spaces """
		return empty_spaces


##################### Super Tic-Tac-Toe Board #############################

class Super_Board(Normal_Board):
	""" Creates Super Tic-Tac-Toe Board """

	def __init__(self):
		pass

	def clear_board(self):
		""" Creates an Empty Super Tic-Tac-Toe Board """
		return 

	def create_board(self,game_board):
		""" Creates GUI for game board """
		pass

	def check_for_win(self):
		""" Checks to see if game has ended, otherwise updates game status """
		pass

	def makeMove(self,player,i_pos,j_pos):
		""" Marks game board with player move
		@param player: Player X or Player O
		@param i_pos: row of move (starting with 0)
		@param j_pos: column of move (starting with 0)
		"""
		pass

	def empty_spaces(self):
		""" Returns locations of empty board spaces """
		return empty_spaces

	def getNextGrid(self):
		""" Returns the next grid that must be played in.
		Follows the rules of Super Tic-Tac-Toe 
		"""
		pass




