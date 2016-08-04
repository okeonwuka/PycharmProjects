# Exercise 4.3
# 4.3.4

from TurtleWorld import *
from math import *

# For some reason we need to initialise TurtleWorld() otherwise
# error
world = TurtleWorld()
bob = Turtle()
# Speed things up by reducing delay
bob.delay = 0.1


# Refined polygon description
def polygon(thing, lengthOfSide, numberOfSides):
    thing = Turtle()
    for i in range(numberOfSides):
        fd(thing, lengthOfSide)
        lt(thing, 360/numberOfSides)


# circle1() function
def circle1():
    t = Turtle()
    r = 200
    polygon(bob, (2*pi*r/40), 40)

# Run
circle1()


# more useful form
def circle2(thing, radius):
    polygon(thing, (2*pi*radius/40), 40)


# Run
circle2(bob, 100)


