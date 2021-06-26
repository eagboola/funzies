#!/usr/bin/env python
# first line is super special deluxe thing, SHEBANG (actually): a scripting convention that tells os what kind of language file was written in and specifies which interpreter to use

'''
1: get to: run program and print string 'Hello' to terminal
2: start up, create line object, print coordinates to screen

'''


import os   # built-in python module
import cairo
import math
import random

class Line:
    x0 = 0
    y0 = 0
    x1 = 0
    y1 = 0
    # bag of shit with 4 variables
    def __init__(self, x0, y0, x1, y1):
        self.x0 = x0
        self.y0 = y0
        self.x1 = x1
        self.y1 = y1
    
    # create method to convert line to string and print
    def toString(self):
        return 'the x coordinate is ' + str(self.x0) + ', the y coordinate is ' + str(self.y0) + ', the second x coordinate is ' + str(self.x1) + ', the second y coordinate is ' + str(self.y1)

def lineToString(line):
    return 'the x coordinate is ' + str(line.x0) + ', the y coordinate is ' + str(line.y0) + ', the second x coordinate is ' + str(line.x1) + ', the second y coordinate is ' + str(line.y1)

# generate random lines using origin and length
def generateRandomLine(isVertical):
    length = random.randint(1, 8)/10
    originX1 = random.randint(0, 10)/10
    originY1 = random.randint(0, 10)/10
    originX2 = 0
    originY2 = 0
    if isVertical:
        originX2 = originX1
        originY2 = originY1 + length
    else:
        originY2 = originY1
        originX2 = originX1 + length
    newLine = Line(originX1, originY1, originX2, originY2)
    return newLine
    

def chooseOrientation():
    isVertical = random.choice([True, False])
    return isVertical

def isWithinBounds(line):
    return line.x0 >= 1/10 and line.x0 <= 9/10 and line.y0 >= 1/10 and line.y1 <= 9/10


    


if __name__ == "__main__":
    print('sup world')
    width, height = 256, 256


    lines = []

    # write gatekeeping function(s) - coordinates, length, edge distance ... eventually boxiness
    isHorizontal = True
    
    # randomization: generate rando lines, then filter into horiz./vert.

    # transfromation
    # filter: 50% chance horix/vert line
    
    counter = 0
    goodLines = 0
    while goodLines <= 12:
        newLine = generateRandomLine(chooseOrientation())
        if isWithinBounds(newLine):
            lines.append(newLine)
            goodLines += 1
        counter += 1

    
    

    # print(myLine.toString())
    theirLine = Line(1, 4, 12, 20)
    # print(lineToString(theirLine))
    print(str(counter))

    #le cairo ish for make some imugiz
    
    surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, width, height)
    cr = cairo.Context(surface)
    cr.save() #why you do dat?
    # draw some ish
    cr.scale(width, height)
    cr.set_line_width(0.004)
    # cr.move_to(0.5, 0.1)
    # cr.line_to(0.9, 0.9)
    for l in lines:
        cr.move_to(l.x0, l.y0)
        cr.line_to(l.x1, l.y1)

    cr.set_source_rgb(0, 0, 1)
    cr.stroke()
    cr.restore() # why you do dat?
    # save this... using try-cath
    try:
        os.makedirs(os.path.join("_build", "png"))
    except EnvironmentError:
        pass
    filename = os.path.join("_build", "png", "%s.png" % "thing")
    surface.write_to_png(filename) 