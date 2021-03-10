import altair as alt
import vega_datasets as vg
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib

# %matplotlib inline
# %reload_ext autoreload
# %autoreload 2


# Some code to style plots

import matplotlib.pyplot as plt
import seaborn as sns

# Functions
def load_and_process(url): 
    import pandas as pd
    data = pd.read_csv(url)
    new_data = (data.
            dropna().
            reset_index().
            drop(columns='index').
            sort_values(by='popularity').
            assign(release_date_time = pd.
                   to_datetime(data['release_date'],
                               utc=True).
                   dt.date))
    return new_data

# Sorting in orders
def sort_descending(string, data):
    return data.sort_values(by=string, ascending=False)

def sort_ascending(string, data):
    return data.sort_values(by=string, ascending=True)


# Plotting with altair
def scatter_chart(x1, y1, data):
    chart = (alt.Chart(data, width=500, height=300)
          .mark_circle(color='red', size=10, opacity=0.3).encode(
              x=(str)(x1), 
              y=(str)(y1))
          .properties(title='Scatter plot ' + (str)(x1) + ' vs ' + (str)(y1) + ' for different songs'))
    return chart

def bar_chart(x1, y1, data):
    chart = (alt.Chart(data, width=500, height=300)
          .mark_bar(color='red', size=10, opacity=0.3).encode(
              x=alt.X((str)(x1), bin=alt.Bin(maxbins=100)), 
              y=(str)(y1))
            )
    return chart

def line_chart(x1, y1, data):
    chart = (alt.Chart(data, width=500, height=300)
          .mark_line(color='red', size=80, opacity=0.3).encode(
              x=(str)(x1), 
              y=(str)(y1))
            )
    return chart