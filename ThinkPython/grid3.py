# Exercise 3.5.1
# Solution 3

def PrintUniqueLine1_Once(arg1):
    arg1 = '+ ' + '- ' * 4 + '+ ' + '- ' * 4 + '+'
    print(arg1)


def PrintUniqueLine2_Twice(arg2):
    arg2 = '|' + ' ' * 9 + '|' + ' ' * 9 + '|'
    print(arg2)
    print(arg2)



def grid3(f1, f2, arg4):
    f1(arg4)
    f2(arg4)
    f2(arg4)
    f1(arg4)
    f2(arg4)
    f2(arg4)
    f1(arg4)


# Test
grid3(PrintUniqueLine1_Once, PrintUniqueLine2_Twice, 'test')