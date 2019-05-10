from board import *
from player import *
from game import *
from minimax import *

S = Super_Board()
MiniMax = AlphaBetaAgent(GridState.PLAYER_X)
HumanPlayer = HumanPlayer(GridState.PLAYER_O)
game = Game(S,MiniMax,HumanPlayer)
game.startGame()
