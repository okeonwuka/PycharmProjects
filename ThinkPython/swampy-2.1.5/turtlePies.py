# Exercise 4.2

import math

try:
    # see if Swampy is installed as a package
    from swampy.TurtleWorld import *
except ImportError:
    # otherwise see if the modules are on the PYTHONPATH
    from TurtleWorld import *


# Instantiate turtle world and turtle
world = TurtleWorld()
bob = Turtle()
# Speed turtle up
bob.delay = 0.1

# Define functions
def polyline(t, n, length, angle):
    """Draws n line segments.

    t: Turtle object
    n: number of line segments
    length: length of each segment
    angle: degrees between segments
    """
    for i in range(n):
        fd(t, length)
        lt(t, angle)

def polygon(t, n, length):
    """Draws a polygon with n sides.

    t: Turtle
    n: number of sides
    length: length of each side.
    """
    angle = 360.0/n
    polyline(t, n, length, angle)

def arc(t, r, angle):
    """Draws an arc with the given radius and angle.

    t: Turtle
    r: radius
    angle: angle subtended by the arc, in degrees
    """
    arc_length = 2 * math.pi * r * abs(angle) / 360
    n = int(arc_length / 4) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n

    # making a slight left turn before starting reduces
    # the error caused by the linear approximation of the arc
    lt(t, step_angle/2)
    polyline(t, n, step_length, step_angle)
    rt(t, step_angle/2)



def turtlePies(thing, numberOfSides, lengthOfSides, angle, numberOfReplicates):
    for i in range(numberOfReplicates):
        polyline(thing, numberOfSides, lengthOfSides, angle)
        lt(thing, 60)




# def multiTriangle(numberOfReplicates):
#     for i in range(numberOfReplicates):
#         polyline(bob, 3, 75, 120)
#         lt(bob, 60)
# multiTriangle(6)

turtlePies(bob, 3, 75, 120, 6)