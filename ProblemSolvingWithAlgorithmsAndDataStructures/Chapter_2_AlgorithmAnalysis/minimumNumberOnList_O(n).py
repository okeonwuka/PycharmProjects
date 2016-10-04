# Input sample List
sampleList = [81, 500, 89, 25, 67, 24, 56, 90, 23, 54, 222, 66, 77, 88, 433, 556745, 3475368, 24523, ]

# Sort the sample list
# Python doesnt all you to apply the sort() method to a list and assign it to a variable
# at the same time. ie you cant do M = sampleList.sort(). This is because the sort() method
# does not return anything (or returns 'none') and so it cannot be used to assign anything
# to a variable. On the other hand, methods like sampleList.pop() can be used because it
# does produce a return value. The reverse parameter arrange sampleList in descending order
sampleList.sort(reverse=True)

# select minimum element
# pop() method selects and returns last element on a list
MinElt = sampleList.pop()

print(MinElt)
