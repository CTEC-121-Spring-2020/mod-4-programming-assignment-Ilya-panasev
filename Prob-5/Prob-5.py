# Module 5
#   Programming Assignment 6
#       Prob-5.py

# Ilya Panasevich

from graphics import *

def main():
    win = GraphWin("car", 1000, 1000)
    Rect = Rectangle(Point(300, 600), Point(800, 500))
    Rect.setFill("red")
    Rect.setOutline("red")
    Rect.draw(win)

    Rect2 = Rectangle(Point(400, 500), Point(700, 400))
    Rect2.setFill("red")
    Rect2.setOutline("red")
    Rect2.draw(win)

    Rect3 = Rectangle(Point(550, 500), Point(680, 420))
    Rect3.setOutline("cyan")
    Rect3.setFill("cyan")
    Rect3.draw(win)

    Rect4 = Rectangle(Point(420, 420), Point(550, 500))
    Rect4.setOutline("cyan")
    Rect4.setFill("cyan")
    Rect4.draw(win)

    line1 = Line(Point(550, 600), Point(550, 400))
    line1.draw(win)

    Circ = Circle(Point(700, 600), 40)
    Circ.setFill("black")
    Circ.draw(win)

    Circ2 = Circle(Point(400, 600), 40)
    Circ2.setFill("black")
    Circ2.draw(win)

    Poly = Polygon(Point(790, 510), Point(770, 530), Point(790, 550))
    Poly.setOutline("yellow")
    Poly.setFill("yellow")
    Poly.draw(win)

    Rect5 = Rectangle(Point(790, 605), Point(810, 580))
    Rect5.setOutline("gray")
    Rect5.setFill("gray")
    Rect5.draw(win)

    Rect6 = Rectangle(Point(290, 605), Point(310, 580))
    Rect6.setOutline("gray")
    Rect6.setFill("gray")
    Rect6.draw(win)
    
    input()

main()