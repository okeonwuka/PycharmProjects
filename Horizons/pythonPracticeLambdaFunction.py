# Python functions can be defined as expressions using the lambda keyword
# instead of statements using def .Function expressions can be useful when
# working with functions that require a function as one of their arguments.


# For example, the map() built-in Python function applies a given function to
# each item of a list. So, instead of defining this given function in a
# separate statement, the lambda keyword allows you to embed a function
# expression inside the map() call. Consider

y = [1, 2, 3]  # some list of number
map(lambda x: x+1, y)  # add 1 to every number in y

print(map(lambda x: x+1, y))

# Instead of
def add_one(x):
    return x + 1

map(add_one, y)

print(map(add_one, y))

