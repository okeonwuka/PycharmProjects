# Exercise 3.5.1
# Solution 2

def PrintUniqueLine1_Once(arg1):
    arg1 = '+ ' + '- ' * 4 + '+ ' + '- ' * 4 + '+'
    print(arg1)


def PrintUniqueLine2_Twice(arg2):
    arg2 = '|' + ' ' * 9 + '|' + ' ' * 9 + '|'
    print(arg2)
    print(arg2)


def PrintUniqueLine2_4Times(f, arg3):
    f(arg3)
    f(arg3)



# Working
def grid2(f, arg4):
    PrintUniqueLine1_Once(arg4)
    PrintUniqueLine2_4Times(f, arg4)
    PrintUniqueLine1_Once(arg4)
    PrintUniqueLine2_4Times(f, arg4)
    PrintUniqueLine1_Once(arg4)

grid2(PrintUniqueLine2_Twice, 'test')


