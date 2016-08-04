from pprint import pprint

x = range(10)             # list of integer
y = [xx**2 for xx in x]   # iterate through x, square every item, built list

print(y)


# Built list w/ list comprehension, link to key
trace = dict(y=[xx**9 for xx in x])

print(trace)

# Use list comprehension to build list of dictionaries
data = [dict(y=[xx**a for xx in x]) for a in range(5)]

pprint(data)

# Iterate through my_x, square item if even
y2 = [xx**2 for xx in x if xx%2==0]

print(y2)


# Iterate through my_x, add 0 to my_y3 if x<5 add 1 if x>=5
y3 = [0 if xx<5 else 1 for xx in x]

print(y3)
