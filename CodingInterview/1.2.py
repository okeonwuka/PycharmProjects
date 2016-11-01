# code to reverse a string
# Implementation 1

def reverse_a_string_slowly(a_string):
    new_string = ''
    index = len(a_string)
    while index:
        index -= 1  # index = index - 1
        new_string += a_string[index]  # new_string = new_string + character
    return new_string


print(reverse_a_string_slowly('boy'))

print('======Another Implementation================================================')


def reversed_string(a_string):
    return a_string[::-1]


print(reversed_string('boy'))
