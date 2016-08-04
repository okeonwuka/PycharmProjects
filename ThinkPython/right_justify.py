# Exercise 3.16 in Think Python
# Exercise 3.3
# Function that prints a string such that its last letter is in col 70

def right_justify(item):
    lenghtOfArg = len(item)
    numberOfSpacesNeeded = 70 - lenghtOfArg
    s = numberOfSpacesNeeded * ' ' + item
    print(s)


#Test code
testRightJustify = right_justify('Dami Onwuka')


