
def my_func(x):    # define function (notice the :)
    return x + 1   # return value (scope of function is indented)

print(my_func(1))       # call my_func() with position argument = s1



def my_func2(a, b, c=3):  # 2 positional arguments and 1 keyword argument
    return a + b + c

print(my_func2(1, 2))            # call my_func2 with 2 positional arguments


my_func2(1, 2, 4)  # overwrite keyword argument with 4 (evaluates 1+2+4)
print(my_func2(1, 2, 4))

print(my_func2(1, 2, c=5))  # overwrite keyword argument (c) with 5 (evaluates 1+2+5)

def my_func3(a, b, c=3, d=4):  # 2 positional arguments and 2 keyword arguments
    return d, a + b + c + d    # return a tuple (more below)

my_func3(1, 2, d=5)  # use c default, overwrite d (evaluates 1+2+3+5)
print(my_func3(1, 2, d=5))


def my_func4(x):                # take in 1 argument
    return (x, x+1, x*2, x**2)  # output 4 numbers, inside a tuple

print(my_func4(3))


x = [1, 2]         # variables outside
y = [1, 4]         #   of make_trace()
color = '#de2d26'  #   scope

def make_trace(x, y):  # function with 2 positional arguments
    return dict(
        x=x,     # x is a function argument
        y=y,     # so is y
        line=dict(color=color)  # (!) not defined inside function scope
    )

print(make_trace([1, 2, 3], [1, 4, 9]))



