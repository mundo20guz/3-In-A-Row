#  ____      _____                         _____                
# |___ \    |_   _|             /\        |  __ \               
#   __) |_____| |  _ __ ______ /  \ ______| |__) |_____      __ 
#  |__ <______| | | '_ \______/ /\ \______|  _  // _ \ \ /\ / / 
#  ___) |    _| |_| | | |    / ____ \     | | \ \ (_) \ V  V /  
# |____/    |_____|_| |_|   /_/    \_\    |_|  \_\___/ \_/\_/   
#                                                                                                                              
#
# Player.py
#  
# Includes code for Player. Creates both User and AI players.
#
# Dependencies
import random
from board import *

######################################################################

class AI_difficulty():
	""" Chooses AI difficulty """
	EASY = None
	MED = None
	HARD = None

###################### Normal Player #################################

class RandomPlayer():

	def __init__(self,playerName):
		self.playerName = playerName


	def makeMove(self,board,game=None):
		# Next Grid is unspecified (i.e. first move or playing after grid was won)
		if board.nextGrid == [None,None]:
			# Choose at random to play another open grid
			openBoards = board.availableBoards()
			if openBoards:
				nextGrid = random.choice(openBoards)
				nextMove = random.choice(board.emptySpaces(nextGrid))
				board.makeMove(self.playerName,nextGrid[0],nextGrid[1],nextMove[0],nextMove[1])
		else:
			nextMove = random.choice(board.emptySpaces(board.nextGrid))
			board.makeMove(self.playerName,board.nextGrid[0],board.nextGrid[1],nextMove[0],nextMove[1])

######################## AI Opponent ##################################
class HumanPlayer():

	def __init__(self,playerName):
		self.playerName = playerName


	def makeMove(self,board,game=None):
		# Next Grid is unspecified (i.e. first move or playing after grid was won)
		if board.nextGrid == [None,None]:
			# Choose at random to play another open grid
			openBoards = board.availableBoards()
			if openBoards:
				board.print_board()
				print(openBoards)
				nextGrid = input('Choose which grid to play on..').split()
				board.board[int(nextGrid[0])][int(nextGrid[1])].print_board()
				nextMove = input('Where would you like to go?').split()
				board.makeMove(self.playerName,int(nextGrid[0]),int(nextGrid[1]),int(nextMove[0]),int(nextMove[1]))
		else:
			board.print_board()
			print('Your move will be on grid {}'.format(board.nextGrid))
			board.board[board.nextGrid[0]][board.nextGrid[1]].print_board()
			nextMove = input('Where would you like to go?').split()
			#nextMove = random.choice(board.emptySpaces(board.nextGrid))
			board.makeMove(self.playerName,board.nextGrid[0],board.nextGrid[1],int(nextMove[0]),int(nextMove[1]))

