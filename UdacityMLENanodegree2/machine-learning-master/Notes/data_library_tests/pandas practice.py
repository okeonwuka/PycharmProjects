"""
https://github.com/pandas-dev/pandas/blob/master/doc/cheatsheet/Pandas_Cheat_Sheet.pdf
http://nikgrozev.com/2015/12/27/pandas-in-jupyter-quickstart-and-useful-snippets/
"""

import pandas as pd

# Create dataframe
df = pd.DataFrame({
    "a": [35, 6, 78, 45],
    "b": [55, 23, 83, 90],
    "c": [23, 12, 67, 4]
})

df.head()
