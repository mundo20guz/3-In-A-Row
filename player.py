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
import sys
import os
from board import *
from enum import Enum

######################################################################

class AI_difficulty(Enum):
	""" Chooses AI difficulty """
	EASY = None
	MED = None
	HARD = None

###################### Normal Player #################################

class Player():

	def __init__(self):
		self.board = None
		self.player = None

	def makeMove(self,i_pos,j_pos):
		""" Creates Players next move """
		pass


######################## AI Opponent ##################################

class AI_Player(Player):

	def __init__(self):
		""" Calls super constructor of Player Class """
		super.__init__(self,board,player)

	def makeMove(self,i_pos,j_pos):
		""" Creates AIs next move """
		pass

