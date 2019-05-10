import random
import copy
from player import RandomPlayer
from board import GridState
# This evaluation function takes up the number of mini wins of 'x' minus
# the number of mini wins of 'o'

class AlphaBetaAgent():
	def __init__(self, playerName,evalFn = None, depth = 3):
		self.index = 0
		self.depth = depth
		self.playerName = playerName

	def makeMove(self,board,game):
		self.getAction(board,game)


	def getAction(self, board, game):
		"""
		Returns the minimax action using self.depth and self.evaluationFunction
		"""

		# Return a random move for first fifthteen moves
		if game.numMoves < 15:
			player = RandomPlayer(self.playerName)
			return player.makeMove(board)

		def recurse(board, player,depth, alpha, beta):
			if depth == 6:
				if board.nextGrid == [None,None]:
					openBoards = board.availableBoards()
					if openBoards:
						nextGrid = random.choice(openBoards)
						moves = board.emptySpaces(nextGrid)
				else:
					moves = board.emptySpaces(board.nextGrid)
			elif depth == 5:
				moves = board.emptySpaces()	
			else:
				moves = board

			if player == GridState.PLAYER_X:
				ans = (-float('Inf'),(-1,-1))
				for action in moves:
					ans = max(ans, (recurse(self.generateSuccessor(board,action), 
							GridState.PLAYER_O, depth - 1, alpha, beta)[0], action))
					alpha = max(alpha, ans)
					if alpha >= beta:
						break
				return alpha
			else:
				ans = (float('Inf'),(-1,-1))
				for action in moves:
					ans = min(ans, (recurse(self.generateSuccessor(board,action), 
							GridState.PLAYER_O, depth - 1, alpha, beta)[0], action))
					beta = min(beta, ans)
					if alpha >= beta:
						break
				return beta
		alph0 = (-float('Inf'), (-1,-1))
		beta0 = (+float('Inf'), (-1,-1))
		utility, action = recurse(board, self.playerName, 2*self.depth, alph0, beta0)
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

	def generateSuccessor(self,board, action):
		newGame = copy.deepcopy(board)
		newGame = board.board[action[0]][action[1]]
		return newGame