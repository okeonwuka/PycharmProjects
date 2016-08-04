# Exercise 4.3
# 4.3.5

from TurtleWorld import *
from math import *

# For some reason we need to initialise TurtleWorld() otherwise
# error
world = TurtleWorld()
bob = Turtle()
# Speed things up by reducing delay
bob.delay = 0.1


def polygon(thing, lengthOfSide, numberOfSides):
    thing = Turtle()
    for i in range(numberOfSides):
        fd(thing, lengthOfSide)
        lt(thing, 360/numberOfSides)


















def circle2(thing, radius):
    polygon(thing, (2*pi*radius/40), 40)


def arc(thing, radius, angle):
    # from length of arc maths formula
    # replace lengthOfSide to (angle/360)*(2*pi*radius/40)
    polygon(thing, (angle/360)*(2*pi*radius/40), 40)




# Run

arc(bob, 50, 270)


