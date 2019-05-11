#  ____      _____                         _____                
# |___ \    |_   _|             /\        |  __ \               
#   __) |_____| |  _ __ ______ /  \ ______| |__) |_____      __ 
#  |__ <______| | | '_ \______/ /\ \______|  _  // _ \ \ /\ / / 
#  ___) |    _| |_| | | |    / ____ \     | | \ \ (_) \ V  V /  
# |____/    |_____|_| |_|   /_/    \_\    |_|  \_\___/ \_/\_/   
#                                                        
# main.py

# Dependencies
from board import *
from player import *
from game import *

###################################################

# Create Game Board
S = Super_Board()
# Create 2 Players
MiniMax = MiniMaxPlayer(GridState.PLAYER_X)
HumanPlayer = HumanPlayer(GridState.PLAYER_O)
# Create Game
game = Game(S,MiniMax,HumanPlayer)
game.startGame()
