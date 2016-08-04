from pprint import pprint

splts = range(1, 5)  # list of subplot number ids
print(splts)

axes_ids = []  # initialize list of axes ids

for splt in splts:
    axes_ids += [('x'+str(splt), 'y'+str(splt))]  # append list of tuples  a += b  means a=a+b

print(axes_ids)


# Loop through subplots,
# convert to string for layout key and 'title' value
layout = {'xaxis{}'.format(splt): {'title': 'X axis ' + str(splt)} for splt in splts}
pprint(layout)

# or

layout = {'xaxis{}'.format(splt): dict(title='X axis '+str(splt))for splt in splts}
pprint(layout)

# Note
# would not work as expressions are not identifiers
# (recall the dict constructor only accepts identifiers
# on the left-hand side of the equals sign).
# layout = dict(xaxis{}.format(splt)=dict(title='X axis '+str(splt)) for splt in splts)


# String continuation from line to line is made with the \ character,
# numbers can be formatted using the % character and the appropriate
# conversion code. Here's an example:
mu = 75       # some numbers representing the
sig = 6.7123  # mean and the standard deviation

# Formatted strings, 5 chars with 2 decimals and 5 chars with 3 decimals
text = '\
<br><b>Mean</b>: %5.2f\
<br><b>Standard deviation</b>: %5.3f' % (mu, sig)

print(text)

