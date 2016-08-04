# Doc string for Polygon, arc and circle
from TurtleWorld import *
from math import *

# For some reason we need to initialise TurtleWorld() otherwise
# error
world = TurtleWorld()
bob = Turtle()
# Speed things up by reducing delay
bob.delay = 0.1




def polygon(thing, lengthOfSide, numberOfSides):
    """
    This function takes a turtle, length of side and
    draws a polygon with the number of sides
    """
    thing = Turtle()
    for i in range(numberOfSides):
        fd(thing, lengthOfSide)
        lt(thing, 360/numberOfSides)


def arc(thing, radius, angle):
    """
    This function takes a turtle, radius and
    draws an arc with the angles given
    """
    polygon(thing, (angle/360)*(2*pi*radius/40), 40)



def circle2(thing, radius):
    """
    This function takes a turtle, radius and
    draws a circle using the polygon function
    """
    polygon(thing, (2*pi*radius/40), 40)