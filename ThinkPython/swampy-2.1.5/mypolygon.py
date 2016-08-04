# Working directly from Swampy folder to access all the files.
# As a result I do not have to use the swampy package from pycharm
# so import statement is "from TurtleWorld import * " and not "swampy.TurtleWorld import *"

from TurtleWorld import *

world = TurtleWorld()
bob = Turtle()
print(bob)


# Draw a square
# fd(bob, 100)
# lt(bob)
# fd(bob, 100)
# lt(bob)
# fd(bob, 100)
# lt(bob)
# fd(bob, 100)


# For loop example
for i in range(4):
    print('Hello!')


# Draw a square using for loop
for i in range(4):
    fd(bob, 100)
    lt(bob)


#wait_for_user()

