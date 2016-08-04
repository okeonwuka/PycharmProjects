# (*) To communicate with Plotly's server, sign in with credentials file
import plotly.plotly as py

# (*) Useful Python/Plotly tools
import plotly.tools as tls

# (*) Graph objects to piece together plots
from plotly.graph_objs import *

import numpy as np  # (*) numpy for math functions and arrays

# Embed an existing Plotly streaming plot
tls.embed('streaming-demos', '6')

# Note that the time point correspond to internal clock of the servers,
# that is UTC time.
