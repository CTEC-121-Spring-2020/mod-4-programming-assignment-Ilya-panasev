# Module 5
#   Programming Assignment 6
#       Prob-6.py

# Ilya Panasevich

from graphics import *

def main():
    win = GraphWin("Legos", 1100, 1000)
    # draw basic brick
    blueBrick = Rectangle(Point(10, 280), Point(510, 100))
    blueBrick.setFill("blue")
    blueBrick.setOutline("black")
    blueBrick.setWidth(5)
    blueBrick.draw(win)
    # draw first nib
    blueBrickNib = Rectangle(Point(35, 100), Point(85, 80))
    blueBrickNib.setFill("blue")
    blueBrickNib.setOutline("black")
    blueBrickNib.setWidth(5)
    blueBrickNib.draw(win)
    # test
    for i in range(1, 5):
        blueBrickNextNib = blueBrickNib.clone()
        blueBrickNextNib.move(100 *i, 0)
        blueBrickNextNib.draw(win)
    
    # green brick
    greenBrick = blueBrick.clone()
    greenBrick.move(580, 0)
    greenBrick.setFill("green")
    greenBrick.draw(win)
   
    greenBrickNib = blueBrickNib.clone()
    greenBrickNib.move(580, 0)
    greenBrickNib.setFill("green")
    greenBrickNib.draw(win)
    
    for i in range(1, 5):
        NextGreenNib = greenBrickNib.clone()
        NextGreenNib.move(100 * i, 0)
        NextGreenNib.draw(win)
    
    # yellow brick
    yellowBrick = blueBrick.clone()
    yellowBrick.move(0, 300)
    yellowBrick.setFill("yellow")
    yellowBrick.draw(win)

    yellowBrickNib = blueBrickNib.clone()
    yellowBrickNib.move(0, 300)
    yellowBrickNib.setFill("yellow")
    yellowBrickNib.draw(win)

    for i in range(1, 5):
        NextYellowNib = yellowBrickNib.clone()
        NextYellowNib.move(100 * i, 0)
        NextYellowNib.draw(win)
    
    # red brick
    redBrick = greenBrick.clone()
    redBrick.move(0, 300)
    redBrick.setFill("red")
    redBrick.draw(win)

    redBrickNib = greenBrickNib.clone()
    redBrickNib.move(0, 300)
    redBrickNib.setFill("red")
    redBrickNib.draw(win)

    for i in range(1, 5):
        NextRedNib = redBrickNib.clone()
        NextRedNib.move(100 * i, 0)
        NextRedNib.draw(win)
    
    # cyan brick
    cyanBrick = yellowBrick.clone()
    cyanBrick.move(0, 300)
    cyanBrick.setFill("cyan")
    cyanBrick.draw(win)

    cyanBrickNib = yellowBrickNib.clone()
    cyanBrickNib.move(0, 300)
    cyanBrickNib.setFill("cyan")
    cyanBrickNib.draw(win)

    for i in range(1, 5):
        NextCyanNib = cyanBrickNib.clone()
        NextCyanNib.move(100 * i, 0)
        NextCyanNib.draw(win)

    # black brick
    blackBrick = redBrick.clone()
    blackBrick.move(0, 300)
    blackBrick.setFill("black")
    blackBrick.setOutline(color_rgb(120, 0, 0))
    blackBrick.draw(win)

    blackBrickNib = redBrickNib.clone()
    blackBrickNib.move(0, 300)
    blackBrickNib.setFill("black")
    blackBrickNib.setOutline(color_rgb(120, 0, 0))
    blackBrickNib.draw(win)

    for i in range(1, 5):
        NextBlackNib = blackBrickNib.clone()
        NextBlackNib.move(100 * i, 0)
        NextBlackNib.draw(win)
   
    input()

main()