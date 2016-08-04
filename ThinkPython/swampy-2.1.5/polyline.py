from TurtleWorld import *
from math import *

# For some reason we need to initialise TurtleWorld() otherwise error
world = TurtleWorld()
bob = Turtle()

# Speed things up by reducing delay
bob.delay = 0.1


# Define polyline
def polyline(thing, numberOfSides, lengthOfSides, angle):
    for i in range(numberOfSides):
        fd(thing, lengthOfSides)
        lt(thing, angle)


polyline(thing=bob, numberOfSides=20, lengthOfSides=100, angle=160)
