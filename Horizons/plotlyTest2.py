import plotly.plotly as py

# (1) Two lists of numbers
x1 = [1, 2, 3, 5, 6]
y1 = [1, 4.5, 7, 24, 38]

# (2) Make dictionary linking x and y coordinate lists to 'x' and 'y' keys
trace1 = dict(x=x1, y=y1)

# (3) Make list of 1 trace, to be sent to Plotly
data = [trace1]

# (@) Call the plot() function of the plotly.plotly submodule,
#     save figure as 's0_first_plot'
py.plot(data, filename='s0_first_plot')
