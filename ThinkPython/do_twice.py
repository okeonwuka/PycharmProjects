# Exercise 3.16 in Think Python
# Exercise 3.4


# Exercise 3.4.1
# def do_twice(f):
#     f()
#     f()

# def print_spam():
#     print('spam')
#
# Test
# do_twice(print_spam)



# Exercise 3.4.2
def do_twice(f, val):
    f(val)
    f(val)



# Exercise 3.4.3
def print_twice(s):
    print(s)
    print(s)


# Exercise 3.4.4
# To make sense of this solution, start with the outer loop. do_twice takes
# a function and a value as arguments. do_twice will, by definition, place the
# value argument into its function argument. So, by the structure, 'testman'
# is placed in 'print_twice' function by do_twice

do_twice(print_twice, 'testman')



# Exercise 3.4.5
# def do_four(f, val):
#     do_twice(f, val)
#     do_twice(f, val)
#
# do_four(print_twice('spam'), 'test')



