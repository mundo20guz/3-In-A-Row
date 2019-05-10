import tictactoe
import random
from minimax import AlphaBetaAgent
from randomAgent import RandomAgent
import time

#UI modules
import sys
from main import MainBoard
from PySide2 import QtCore, QtGui, QtWidgets
from board_qt import board
from tile_qt import TileStates

# agentNames = ['Random', 'Minimax', 'MCTS', 'DQN', 'Hybrid']
agentNames = ['Random', 'Minimax']
agents = [RandomAgent(), AlphaBetaAgent(depth=2)]
f = open("results.txt", "w")

#UI global variables



def simulateGames(agent1, agent2, n = 10):
    wins1 = 0
    wins2 = 0

    for i in range(n):

        #Instantiate a new UI board.
        gameLogic = MainBoard()
        gameLogic.show()
        time.sleep(1)

        #Initialize the board
        gameLogic.initializeBoard()

        #Pass in the UI board with the tic tac toe game
        myGame = tictactoe.Game(gameLogic)
        myGame.currPlayer = 1 # First player to move (count = 0) is agent 1
        while(myGame.getMoves() and not myGame.isEnd()):
            time.sleep(1)
            if myGame.getNumMoves() % 2 == 0:
                myGame.move(agent1.getAction(myGame))
            else:
                myGame.move(agent2.getAction(myGame))

            if myGame.getWinner() == 1:
                wins1 += 1
            elif myGame.getWinner() == -1:
                wins2 += 1

        #Close the UI board (delete it)
        gameLogic.close()

    print('Player 1 won {} games, player 2 won {} games, {} ties'.format(wins1, wins2, n-wins1-wins2))
    f.write('{},{},{}\n'.format(wins1, wins2, n-wins1-wins2))

def mainRun():#gameLogic, gameUI):
    for i, agentName1 in enumerate(agentNames):
        for j, agentName2 in enumerate(agentNames):
            agent1 = agents[i]
            agent2 = agents[j]
            a = time.time()
            print('{} (Player 1) vs {} (Player 2)'.format(agentName1, agentName2))
            simulateGames(agent1, agent2)#, gameLogic, gameUI)
            print('Runtime: {} seconds'.format(time.time() - a))
    f.close()


def mainWrap():
    app = QtWidgets.QApplication()
    mainRun()
    sys.exit(app.exec_())


mainWrap()

