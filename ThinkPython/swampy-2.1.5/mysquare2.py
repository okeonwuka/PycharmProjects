# Exercise 4.3
# 4.3.2

from TurtleWorld import *

# For some reason we need to initialise TurtleWorld() otherwise
# error
world = TurtleWorld()
bob = Turtle()


# 'SquareWithLength' function that takes 2 arguments
def squareWithLength(t,length):
    t = Turtle()
    for i in range(4):
        fd(t, length)
        lt(t)


# Function call
squareWithLength(bob,150)