from pprint import pprint

range(10)  # list of integers of unit step
pprint(range(10))


for i in range(10):    #  i iterates over list of integers, : at end of statement!
    print('item: ', i)  #  print string and value of i

my_dict2 = {'api': 'python 2.7+',
 'company': 'plotly graphs',
 'ipython': True,
 'ipython-nb': True,
 'team': {'ceo': 'Jack Parmer'},
 'version': '1.0'}

pprint(my_dict2)


for k in ['api', 'ipython', 'ipython-nb', 'version']:  # iterate through list of keys
    my_dict2.pop(k, None)  # delete key if exist, do nothing if key does not exist

pprint(my_dict2)


# zip function
my_iter1 = [1, 4, 10]  # iterable object 1
my_iter2 = [2, 3, 9]   # iterable object 2

list_new = []  # initialize a new list

for (x,y) in zip(my_iter1, my_iter2):  # zip 2 list together, name 2 item variables
    list_new += [[x, y]]               # append list to list_new

print(list_new)



