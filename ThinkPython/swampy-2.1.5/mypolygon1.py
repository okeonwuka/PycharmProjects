# Exercise 4.3
# 4.3.3

from TurtleWorld import *

# For some reason we need to initialise TurtleWorld() otherwise
# error
world = TurtleWorld()
bob = Turtle()

#
# Rough polygon description
# def polygon(t, length, n):
#     t = Turtle()
#     for i in range(n):
#         fd(t, length)
#         lt(t, 360/n) # I got an error when i did lt(360/n). But it ran when
#                      # I did lt(t,360/n). From TurtleWorld.py>Turtle(Animal)
#                      # >lt(self,angle=90)...you can see lt()takes 2 arg. But
#                      # it still worked when only the 1st arg was given...'self'


# Refined polygon description
def polygon(thing, lengthOfSide, numberOfSides):
    thing = Turtle()
    for i in range(numberOfSides):
        fd(thing, lengthOfSide)
        lt(thing, 360/numberOfSides)

# Function call
polygon(bob, 70, 9)

# another function call format
polygon(thing=bob, lengthOfSide=70, numberOfSides=9)