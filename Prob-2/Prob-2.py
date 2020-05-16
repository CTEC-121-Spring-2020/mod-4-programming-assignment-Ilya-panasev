# Module 5
#   Programming Assignment 6
#       Prob-2.py

# Ilya Panasevich

from graphics import *

def main():
     # draws the first red square
     win = GraphWin()
     shape = Rectangle(Point(50,50), Point(80,20))
     shape.setOutline("red")
     shape.setFill("red")
     shape.draw(win)
     
     # creates a shape starting in the lower left corner of where you click
     # runs 5 times
     
     for i in range(5):
          p = win.getMouse()
          p2 = Point(p.getX()+30, p.getY()-30)
          shape = Rectangle(p, p2)
          shape.setOutline("red")
          shape.setFill("red")
          shape.draw(win)
     
     # Bonus: creates a shape in the center of where you click
     # runs 5 times
     for i in range(5):
          p = win.getMouse()
          p2 = Point(p.getX()+15, p.getY()-15)
          p3 = Point(p.getX()-15, p.getY()+15)
          shape = Rectangle(p2, p3)
          shape.setOutline("red")
          shape.setFill("red")
          shape.draw(win)

     # closes the window
     win.getMouse()
     close = "Click again to quit"
     text = Text(Point(100, 100), close).draw(win)
     win.getMouse()
     win.close()

main()