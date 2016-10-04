# Function to test if xters in string is unique

test_string = 'abcdd'


def uniqueStringChecker(test_string):
    # If the number of characters in test_string is more than 256, which is the max
    # number of ASCII characters, then we know automatically that there are duplicates
    if len(test_string) > 256:
        print('There are duplicate characters in test_string')
    else:
        pass

    # Now check if count of individual characters in string is greater than 1
    for a_char in test_string:
        if test_string.count(a_char) > 1:
            print('There are duplicate characters in test_string')
        else:
            print('There are unique characters')


uniqueStringChecker(test_string)

print(len(test_string))
