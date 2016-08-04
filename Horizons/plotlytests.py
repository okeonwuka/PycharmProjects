"""
This program publishes a graph to a stand alone html web browser using localhost as web server.

"""

import plotly
print (plotly.__version__ ) # version >1.9.4 required
from plotly.graph_objs import Scatter, Layout
plotly.offline.plot({
"data": [
    Scatter(x=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], y=[4, 1, 3, 7, -3, 5, 4, 1, 3, 7, -3, 5, 4, 1, 3, 7, -3, 5, 0])
],
"layout": Layout(
    title="Hello world. Welcome"
)
})

