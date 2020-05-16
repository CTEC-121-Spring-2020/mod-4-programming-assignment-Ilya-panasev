# Module 5
#   Programming Assignment 6
#       Prob-3.py

# Ilya Panasevich

from graphics import *

def main():
    win = GraphWin("Prob 3", 400, 400)
    circ1 = Circle(Point(200, 200), 140)
    circ1.setFill("white")
    circ1.draw(win)

    circ2 = Circle(Point(200, 200), 110)
    circ2.setFill("black")
    circ2.draw(win)

    circ3 = Circle(Point(200, 200), 80)
    circ3.setFill("blue")
    circ3.setOutline("blue")
    circ3.draw(win)

    circ4 = Circle(Point(200, 200), 50)
    circ4.setFill("red")
    circ4.setOutline("red")
    circ4.draw(win)
    
    circ5 = Circle(Point(200, 200), 20)
    circ5.setFill("yellow")
    circ5.setOutline("yellow")
    circ5.draw(win)
    
    input()

main()    