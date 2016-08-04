# Exercise 4.3
# 4.3.1b

from TurtleWorld import *

# For some reason we need to initialise TurtleWorld() otherwise
# error
world = TurtleWorld()
bob = Turtle()


# Function that draws a square
def square():
    t = Turtle()
    for i in range(4):
        fd(t, 100)
        lt(t)



# 'Square' function that takes an argument
def squareBob(t):
    t = Turtle()
    for i in range(4):
        fd(t, 100)
        lt(t)


# Run program ie function call
squareBob(bob)