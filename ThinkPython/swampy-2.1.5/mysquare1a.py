# Exercise 4.3
# 4.3.1

from TurtleWorld import *

# For some reason we need to initialise TurtleWorld() otherwise
# error
world = TurtleWorld()


# Function that draws a square
def square():
    t = Turtle()
    for i in range(4):
        fd(t, 100)
        lt(t)


# Draw a square
square()


