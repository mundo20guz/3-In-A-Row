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
# Includes code for 3 different types of Players. First a human player, then 
# a random player, and finally a player backed by the minimax algorithm.
#
# Dependencies
import random
import copy
from board import *

######################################################################

class AI_difficulty():
	""" Chooses AI difficulty """
	EASY = None
	MED = None
	HARD = None

###################### Random Player #################################

class RandomPlayer():

	def __init__(self,playerName):
		self.playerName = playerName


	def makeMove(self,board,game=None):
		""" Perform a move
		@param board:
		@param game:
		"""
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


######################## Human Opponent ##################################

class HumanPlayer():

	def __init__(self,playerName):
		self.playerName = playerName


	def makeMove(self,board,game=None):
		""" Performs a move
		@param board
		@param game
		"""
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
				board.makeMove(self.playerName,int(nextGrid[0]),int(nextGrid[1]),
					int(nextMove[0]),int(nextMove[1]))
		else:
			board.print_board()
			print('Your move will be on grid {}'.format(board.nextGrid))
			board.board[board.nextGrid[0]][board.nextGrid[1]].print_board()
			nextMove = input('Where would you like to go?').split()
			#nextMove = random.choice(board.emptySpaces(board.nextGrid))
			board.makeMove(self.playerName,board.nextGrid[0],board.nextGrid[1],
				int(nextMove[0]),int(nextMove[1]))


################### MiniMax AI #############################################

class MiniMaxPlayer():

	def __init__(self, playerName,evalFn = None, depth = 3):
		self.index = 0
		self.depth = depth
		self.playerName = playerName


	def makeMove(self,board,game):
		""" Performs a move
		@param board:
		@param game
		"""
		self.getAction(board,game)


	def getAction(self, board, game):
		""" Minimax algorithm to choose alpha and beta """
		# Return a random move for first 25 moves
		if game.numMoves < 25:
			player = RandomPlayer(self.playerName)
			return player.makeMove(board)

		alph0 = (-float('Inf'), (-1,-1))
		beta0 = (+float('Inf'), (-1,-1))
		utility, action = self.minimax(board, self.playerName, self.depth, alph0, beta0)
		if action != (-1,-1):
			if board.nextGrid == [None,None]:
					openBoards = board.availableBoards()
					if openBoards:
						nextGrid = random.choice(openBoards)
						board.makeMove(self.playerName,nextGrid[0],nextGrid[1],action[0],action[1])
					else:
						pass
			else:
				# print("minimax made move" + str(gameState.getNumMoves()/2))
				board.makeMove(self.playerName,board.nextGrid[0],board.nextGrid[1],action[0],action[1])
		else:
			player = RandomPlayer(self.playerName)
			return player.makeMove(board)


	def minimax(self,board, player,depth, alpha, beta):
		""" Minimax algorithm to choose alpha and beta """
		if depth == 3:
			if board.nextGrid == [None,None]:
				openBoards = board.availableBoards()
				if openBoards:
					nextGrid = random.choice(openBoards)
					moves = board.emptySpaces(nextGrid)
			else:
				moves = board.emptySpaces(board.nextGrid)
		elif depth == 2:
			moves = board.emptySpaces()	
		else:
			moves = board

		if player == GridState.PLAYER_X:
			ans = (-float('Inf'),(-1,-1))
			for action in moves:
				ans = max(ans, (self.minimax(self.generateSuccessor(board,action), 
						GridState.PLAYER_O, depth - 1, alpha, beta)[0], action))
				alpha = max(alpha, ans)
				if alpha >= beta:
					break
			return alpha
		else:
			ans = (float('Inf'),(-1,-1))
			for action in moves:
				ans = min(ans, (self.minimax(self.generateSuccessor(board,action), 
						GridState.PLAYER_O, depth - 1, alpha, beta)[0], action))
				beta = min(beta, ans)
				if alpha >= beta:
					break
			return beta


	def generateSuccessor(self,board, action):
		""" Generates a child board to investigate """
		newGame = copy.deepcopy(board)
		newGame = board.board[action[0]][action[1]]
		return newGame