# (*) To communicate with Plotly's server, sign in with credentials file

# (*) Useful Python/Plotly tools
import plotly.tools as tls

# (*) Graph objects to piece together plots

# Embed an existing Plotly streaming plot
tls.embed('streaming-demos', '6')

# Note that the time point correspond to internal clock of the servers,
# that is UTC time.
