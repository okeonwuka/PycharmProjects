#Functions

def PrintUniqueLine1_OnceB(arg1):
    arg1 = '+ ' + '- ' * 5 + '+ ' + '- ' * 5 + '+'
    print(arg1)

def PrintUniqueLine2_TwiceB(arg2):
    arg2 = '|' + ' ' * 14 + ' ' * 9 + '|'
    print(arg2)
    print(arg2)

def PrintUniqueLine2_4TimesB(f, arg3):
    f(arg3)
    f(arg3)


def PrintStackBoxA(f1,  f2,  f3,  arg4, n):
    for i in range(n):
        f1(arg4)
        f3(f2, arg4)
        f1(arg4)

# Run
PrintStackBoxA(PrintUniqueLine1_OnceB, PrintUniqueLine2_TwiceB, PrintUniqueLine2_4TimesB, 'test', 4)
