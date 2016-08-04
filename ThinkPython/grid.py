# Exercise 3.5.1

# Solution 1
def UniqueLineA():
    print('+', '- ' * 4, '+', '- ' * 4, '+')

def UniqueLineB():
    print('|          ' * 3)

def grid1():
    UniqueLineA()
    UniqueLineB()
    UniqueLineB()
    UniqueLineB()
    UniqueLineB()
    UniqueLineA()
    UniqueLineB()
    UniqueLineB()
    UniqueLineB()
    UniqueLineB()
    UniqueLineA()

grid1()
