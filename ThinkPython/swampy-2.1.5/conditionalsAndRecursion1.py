# # nested conditional example
#
# x = 10
# y = 11
#
#
# if x==y:
#     print('x and y are equal')
# else:
#     if x < y:
#         print('x is less than y')
#     else:
#         print('x is greater than y')


# Recursion

def countdown(n):
    if n <= 0:
        print('Blast off!')
    else:
        print(n)
        countdown(n-1)


def print_n(s, n):
    if n <= 0:
        return
    print(s)
    print_n(s, n-1)


# countdown(997)
print_n(90, 400)

