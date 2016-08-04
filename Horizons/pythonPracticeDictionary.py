import pprint

my_dict = {'2': 'stuff', 1: 77.7, 'id': ['more', 'stuff']}
pprint.pprint(my_dict)
pprint.pprint(my_dict['2'])


# One can also define dictionaries using the following syntax (the dict constructor way):
my_dict2 = dict(company='plotly', api='python', ipython=True)
pprint.pprint(my_dict2)


# To add new key-values pair in a given dictionary, either
# assign values to keys or use the update() method:
my_dict2['version'] = '1.0'           # add 'version': '1.0' to my_dict2
my_dict2.update({'ipython-nb': True}) # update my_dict2 with another dictionary
my_dict2.update(dict(team='Jack & co.'))  # similarly
pprint.pprint(my_dict2)


# With the same techniques, one can modify values of existing keys:
my_dict2['api'] = 'python 2.7+'                # modify value of 'api' key
my_dict2.update({'company': 'plotly graphs'})  # overwrite value of 'company' key

# Update dictionary with key linking to another dictionary
my_dict2.update(dict(
    team=dict(
        eng=['Chris', 'Ben', 'Marianne', 'Alex V', 'Andrew', 'Jody'],
        ceo='Jack',
        coo='Matt',
        cto='Alex J'
    )
))
pprint.pprint(my_dict2)

# This updates the nested key in dictionary
my_dict2['team'].update({'ceo': 'Jack P'})
pprint.pprint(my_dict2)


