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
# N/A

#############################################################################

class GameStatus():
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


class GridState():
	""" Includes states of individual grids
	@EMPTY = Not occupied by either player
	@PLAYER_X = Occupied by Player X
	PLAYER_O = Occupied by Player Z
	"""
	EMPTY_SPACE = ''
	PLAYER_X = 'X'
	PLAYER_O = 'O'


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
	
	##################### Class Methods #########################

	def __init__(self):
		""" Creates a new game board object """
		self.board = self.clearBoard()
		self.status = GameStatus.ACTIVE


	def getGridState(self,row,col):
		""" Return 'X','O', or '' """
		return self.board[row][col]


	def clearBoard(self):
		""" Creates an Empty Tic-Tac-Toe Grid """
		return [[GridState.EMPTY_SPACE,GridState.EMPTY_SPACE,GridState.EMPTY_SPACE],
				[GridState.EMPTY_SPACE,GridState.EMPTY_SPACE,GridState.EMPTY_SPACE],
				[GridState.EMPTY_SPACE,GridState.EMPTY_SPACE,GridState.EMPTY_SPACE]]


	def decideBoardStatus(self):
		""" """
		for row in self.board:
			if self.checkWin(row):
				self.status = self.chooseWinner(row)
				return
		for col in range(3):
			column = [self.board[0][col],self.board[1][col],self.board[2][col]]
			if self.checkWin(column):
				self.status = self.chooseWinner(column)
				return
		diag1 = [self.board[row][col] for row,col in zip(range(3), range(3))]
		diag2 = [self.board[row][col] for row,col in zip(range(3), range(2,-1,-1))]
		if self.checkWin(diag1):
			self.status = self.chooseWinner(diag1)
			return
		if self.checkWin(diag2):
			self.status = self.chooseWinner(diag2)
			return
		if len(self.emptySpaces()) > 0:
			self.status = GameStatus.ACTIVE
		else:
			self.status = GameStatus.DRAW


	def makeMove(self,player,row,col,super=True):
		""" Marks game board with player move
		@param player: Player X or Player O
		@param row: row of move (starting with 0)
		@param col: column of move (starting with 0)
		@param super: determine if normal or super tic tac toe
		"""
		if self.board[row][col] != GridState.EMPTY_SPACE:
			print('Location is already taken.')
			return
		# Mark board either X or O
		self.board[row][col] = player
		self.decideBoardStatus()
		if self.status == GameStatus.DRAW:
			pass
		elif self.status != GameStatus.ACTIVE and not super:
			print('Player {} wins!'.format(
				GridState.PLAYER_X if self.status == GameStatus.X_WIN else GridState.PLAYER_O))


	def checkWin(self,three_in_a_row):
		""" Checks to see if game has ended, otherwise updates game status
		@param three_in_a_row : sequence of 3 squares in a row (vert, horiz, or diag) 
		"""
		check = three_in_a_row[0]
		# if all match first in row, then its a win
		for grid in three_in_a_row:
			if grid != check or grid == GridState.EMPTY_SPACE:
				return False
		else:
			return True


	def chooseWinner(self,three_in_a_row):
		""" Determines who takes victory for 3-In-A-Row """
		return GameStatus.O_WIN if GridState.PLAYER_O in three_in_a_row else GameStatus.X_WIN
	

	def emptySpaces(self):
		""" Returns locations of empty board spaces """
		empty_spaces = []
		for row in range(3):
			for col in range(3):
				if self.board[row][col] == GridState.EMPTY_SPACE:
					empty_spaces.append((row,col))
		return empty_spaces


	def print_board(self):
		""" Prints board to console """
		print_string = ''
		for row in range(3):
			for col in range(3):
				if self.getGridState(row,col) == GridState.EMPTY_SPACE:
					print_string += '_ '
				else:
					print_string += self.getGridState(row,col) + ' '
			print_string += '\n'
		print(print_string)


##################### Super Tic-Tac-Toe Board #############################

class Super_Board(Normal_Board):
	""" Creates Super Tic-Tac-Toe Board """

	""" Property Getters """

	@property
	def status(self):
		""" Returns Status of Current Game """
		return self.__status

	@property
	def nextGrid(self):
		""" Returns location of next grid location """
		return self._nextGrid
	
	""" Property Setters """

	@status.setter
	def status(self,game_status):
		""" Sets Status of Current Game to 'game_status' """
		self.__status = game_status

	@nextGrid.setter
	def nextGrid(self,location):
		""" Returns location of next grid location """
		self._nextGrid = [location[0],location[1]]


	######################## Class Methods #############################

	def __init__(self):
		""" Constructor for Super Tic-Tac-Toe Board """
		self.board = self.clearBoard()
		self.nextGrid = [None,None]
		self.status = GameStatus.ACTIVE


	def clearBoard(self):
		""" Creates an Empty Super Tic-Tac-Toe Board """
		return [[Normal_Board(), Normal_Board(), Normal_Board()],
				[Normal_Board(), Normal_Board(), Normal_Board()],
				[Normal_Board(), Normal_Board(), Normal_Board()]]


	def decideBoardStatus(self):
		""" Determine Game Status, usually called after a player move """
		for row in self.board:
			if self.checkWin(row):
				self.status = self.chooseWinner(row)
				return
		for col in range(3):
			column = [self.board[0][col],self.board[1][col],self.board[2][col]]
			if self.checkWin(column):
				self.status = self.chooseWinner(column)
				return
		diag1 = [self.board[row][col] for row,col in zip(range(3),range(3))]
		diag2 = [self.board[row][col] for row,col in zip(range(3),range(2,-1,-1))]
		if self.checkWin(diag1):
			self.status = self.chooseWinner(diag1)
			return
		if self.checkWin(diag2):
			self.status = self.chooseWinner(diag2)
			return
		self.status = GameStatus.DRAW
		for row in range(3):
			for col in range(3):
				if self.board[row][col].status == GameStatus.ACTIVE:
					self.status = GameStatus.ACTIVE


	def makeMove(self,player,board_row,board_col,row,col):
		""" Marks game board with player move
		@param player: Player X or Player O
		@param board_row: row of board (starting with 0)
		@param board_col: column of board (starting with 0)
		@param row: row of move (starting with 0)
		@param col: column of move (starting with 0)
		"""
		board = self.board[board_row][board_col]
		if board.status != GameStatus.ACTIVE:
			print('Board is not active.')
			return
		board.makeMove(player,row,col)
		self.decideBoardStatus()
		if self.status == GameStatus.DRAW:
			print('Draw!')
			self.nextGrid = [None,None]
		elif self.status != GameStatus.ACTIVE:
			print('Player {} wins!'.format(
				GridState.PLAYER_X if self.status == GameStatus.X_WIN else GridState.PLAYER_O))
			self.nextGrid = [None,None]
		else:
			nextBoard = self.board[row][col]
			self.nextGrid = [row,col] if nextBoard.status == GameStatus.ACTIVE else [None,None]


	def checkWin(self,three_in_a_row):
		""" Checks to see if game has ended, otherwise updates game status
		@param three_in_a_row : sequence of 3 squares in a row (vert, horiz, or diag) 
		"""
		check = three_in_a_row[0].status

		for board in three_in_a_row:
			if board.status != check or board.status == GameStatus.ACTIVE:
				return False
		else:
			return True


	def chooseWinner(self,three_in_a_row):
		""" Determines who takes victory for 3-In-A-Row """
		return GameStatus.O_WIN if GameStatus.O_WIN == three_in_a_row[0].status else GameStatus.X_WIN


	def emptySpaces(self,location):
		""" Returns locations of empty board spaces """
		grid = self.board[location[0]][location[1]]
		return grid.emptySpaces()


	def availableBoards(self):
		""" Determine which boards in Super Board are still playable """
		availableBoards = []
		for row in range(3):
			for col in range(3):
				if self.board[row][col].status == GameStatus.ACTIVE:
					availableBoards.append((row,col))
		return availableBoards


	def print_board(self, option=1):
		""" Prints board to the console """
		print_string = ''
		for row in range(3):
			for inner_row in range(3):
				for col in range(3):
					for inner_col in range(3):
						if self.board[row][col].board[inner_row][inner_col] == GridState.EMPTY_SPACE:
							print_string += '_ '
						else:
							print_string += self.board[row][col].board[inner_row][inner_col] + ' '
					print_string += ' '
				print_string += '\n'
			print_string += '\n'
		print(print_string)

