# Exercies 4.1.2

from TurtleWorld import *
from math import *

# For some reason we need to initialise TurtleWorld() otherwise error
world = TurtleWorld()
bob = Turtle()

# Speed things up by reducing delay
bob.delay = 0.1




# polygon description
def polygon(thing, lengthOfSide, numberOfSides):
    print(" Loop creates the edges")
    for i in range(numberOfSides):
        print('Turtle moves in the forward direction by length of side =', lengthOfSide, 'units')
        fd(thing, lengthOfSide)
        print('Turtle makes a slight left by 360 divided by number of sides =', numberOfSides, ', which is', 360/numberOfSides, 'degrees')
        lt(thing, 360/numberOfSides)


def circle3(thing, radius):
    print('This function creates a circle')
    print('Initializing program.....')
    print('The radius input by user is radius =', radius)
    print('Calculating C, circumference of circle...... C = 2 * pi*', radius)
    circumference = 2 * pi * radius
    print('The circumference C is:', circumference)
    print('Determining number of sides, n ')
    n = int(circumference/3) + 1
    print('The number of sides n is:', n, '.This was calculated by getting an integer from:', circumference/3, '+1.')
    print('Calculating length of sides, L by circumference =', circumference, 'divided by number of sides n =', n)
    length = circumference/n
    print('Length of sides, L is:', length)
    print('Calling the Polygon function')
    polygon(thing, lengthOfSide=length, numberOfSides=n)
    print('The circle has been created')
    print('End of Program')
    print('Goodbye')


# Run
circle3(bob, 200)
