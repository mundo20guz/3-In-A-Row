# Super Tic-Tac-Toe
# author: Andrew Nguyen
#
from turtle import *
import random
def main():
    print("Main loop start")
board1 = [['','',''],['','',''],['','','']]
board2 = [['','',''],['','',''],['','','']]
board3 = [['','',''],['','',''],['','','']]
board4 = [['','',''],['','',''],['','','']]
board5 = [['','',''],['','',''],['','','']]
board6 = [['','',''],['','',''],['','','']]
board7 = [['','',''],['','',''],['','','']]
board8 = [['','',''],['','',''],['','','']]
board9 = [['','',''],['','',''],['','','']]
turtle = Turtle()

def drawBoard():
    turtle.clear()
    turtle.color("black")
    turtle.pensize(5)

    #horizontal
    for i in range(2):
        turtle.pu()
        turtle.goto(-150,50-100*i)
        turtle.setheading(0)
        turtle.pd()
        turtle.forward(300)

    #vertical
    for i in range(2):
        turtle.pu()
        turtle.goto(-50+100*i,150)
        turtle.setheading(270)
        turtle.pd()
        turtle.forward(300)
# TODO
# def makeMove():
#
#

if __name__ == "main":
    main()