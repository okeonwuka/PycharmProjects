from TurtleWorld import *
from math import *

# For some reason we need to initialise TurtleWorld() otherwise error
world = TurtleWorld()
bob = Turtle()

# Speed things up by reducing delay
bob.delay = 0.1


# polygon description
def polygon(thing, lengthOfSide, numberOfSides):
    for i in range(numberOfSides):
        fd(thing, lengthOfSide)
        lt(thing, 360/numberOfSides)


def circle3(thing, radius):
    circumference = 2 * pi * radius
    n = int(circumference/3) + 1
    length = circumference/n
    polygon(thing, lengthOfSide=length, numberOfSides=n)


circle3(bob, 30)


