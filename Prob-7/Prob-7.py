# Module 5
#   Programming Assignment 6
#       Prob-7.py

# Ilya Panasevich

from graphics import *

def main():
    win = GraphWin("face", 500, 500)
    rect = Rectangle(Point(185, 100), Point(200, 175))
    rect.setFill(color_rgb(249, 228, 183))
    rect.draw(win)

    rect2 = Rectangle(Point(300, 100), Point(315, 175))
    rect2.setFill(color_rgb(249, 228, 183))
    rect2.draw(win)

    line1 = Line(Point(210, 100), Point(210, 50))
    line1.draw(win)
    for i in range(8):
        line1 = line1.clone()
        line1.move(10, 0)
        line1.draw(win)

    oval1 = Oval(Point(190, 70), Point(310, 200))
    oval1.setFill(color_rgb(249, 228, 183))
    oval1.draw(win)

    circ1 = Circle(Point(225, 115), 10)
    circ1.setFill("white")
    circ1.draw(win)

    circ2 = Circle(Point(275, 115), 10)
    circ2.setFill("white")
    circ2.draw(win)

    circ3 = Circle(Point(230, 115), 5)
    circ3.setFill("black")
    circ3.draw(win)

    circ4 = Circle(Point(280, 115), 5)
    circ4.setFill("black")
    circ4.draw(win)

    Poly = Polygon(Point(250, 130), Point(250, 150), Point(280, 150))
    Poly.draw(win)

    Poly2 = Polygon(Point(255, 150), Point(260, 145), Point(265, 150))
    Poly2.setFill("black")
    Poly2.draw(win)

    line1 = Line(Point(220, 170), Point(280, 170))
    line1.draw(win)
    
    Rect3 = Rectangle(Point(240, 170), Point(248, 178))
    Rect3.setFill("white")
    Rect3.draw(win)

    Rect4 = Rectangle(Point(260, 170), Point(268, 178))
    Rect4.setFill("white")
    Rect4.draw(win)
    
    input()

main()