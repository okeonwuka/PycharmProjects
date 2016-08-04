# Exercise 3.5.2
# Solution

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




# PrintUniqueLine2_4Times(PrintUniqueLine2_Twice, 'test')


# Not working
# def grid2(f, arg4):
#     f = PrintUniqueLine2_Twice(arg4)
#     PrintUniqueLine1_Once(arg4)
#     PrintUniqueLine2_4Times(f, arg4)
#     PrintUniqueLine1_Once(arg4)
#     PrintUniqueLine2_4Times(f, arg4)
#     PrintUniqueLine1_Once(arg4)


def grid4(f,arg4):
    PrintUniqueLine1_Once(arg4)
    PrintUniqueLine2_4Times(PrintUniqueLine2_Twice, arg4)
    PrintUniqueLine1_Once(arg4)
    PrintUniqueLine2_4Times(PrintUniqueLine2_Twice, arg4)
    PrintUniqueLine1_Once(arg4)

#grid4(PrintUniqueLine1_Once, 'test')



def grid5(f,arg5):
    grid4(PrintUniqueLine1_Once, arg5)
    grid4(PrintUniqueLine1_Once, arg5)
    grid4(PrintUniqueLine1_Once, arg5)
    grid4(PrintUniqueLine1_Once, arg5)



grid5(PrintUniqueLine1_Once, 'test')


