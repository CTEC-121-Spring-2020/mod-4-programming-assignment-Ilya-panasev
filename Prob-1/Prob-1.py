# Module 5
#   Programming Assignment 6
#       Prob-1.py

# Ilya Panasevich

# INSTRUCTIONS:
#   Insert a comment above each line of code in the program below to describe
#   what the code does


# imports the graphics library
from graphics import *

def main():
     # creates a window where it draws your object
     win = GraphWin()
     # sets the circle at the indicated point long with the indicated size
     shape = Circle(Point(50,50), 20)
     # sets the outline of the circle to be red
     shape.setOutline("red")
     # sets the interior of the circle to be red
     shape.setFill("red")
     # draws the circle
     shape.draw(win)
     # used to repeat the code for 5 clicks
     for i in range(5):
          # pauses and waits for a mouse click
          p = win.getMouse()
          # returns the center point of the circle/shape
          c = shape.getCenter()
          # returns the X point of where the mouse was clicked, 
          # which is then subtracted by the X point of the center of the circle/shape.
          dx = p.getX() - c.getX()
          # returns the Y point of where the mouse was clicked, 
          # which is then subtracted by the Y point of the center of the circle/shape.
          dy = p.getY() - c.getY()
          # moves the circle/shape to the new coordinates created by dx and dy.
          shape.move(dx,dy)
     # closes the window
     win.close()

main()