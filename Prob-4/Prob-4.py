# Module 5
#   Programming Assignment 6
#       Prob-4.py

# Ilya Panasevich

from graphics import *

def main():
    win = GraphWin("House", 600, 600)
    p1 = win.getMouse()
    p2 = win.getMouse()
    Rect = Rectangle(Point(p1.getX(), p1.getY()), Point(p2.getX(), p2.getY()))
    Rect.draw(win)
    
    p3 = win.getMouse()
    widthOfDoor = (p2.getX() - p1.getX()) // 5
    halfDoorWidth = widthOfDoor // 2
    
    Rect2 = Rectangle(Point(p3.getX()-halfDoorWidth, p1.getY()), Point(p3.getX()+halfDoorWidth, p3.getY()))
    Rect2.draw(win)

    partDoorWidth = halfDoorWidth // 2
    p4 = win.getMouse()
    Rect3 = Rectangle(Point(p4.getX()-partDoorWidth, p4.getY()+partDoorWidth), Point(p4.getX()+partDoorWidth, p4.getY()-partDoorWidth))
    Rect3.draw(win)

    p5 = win.getMouse()
    line1 = Line(Point(p5.getX(), p5.getY()), Point(p2.getX(), p2.getY()))
    line1.draw(win)
    
    line2 = Line(Point(p1.getX(), p2.getY()), Point(p5.getX(), p5.getY()))
    line2.draw(win)
    
    input()

main()