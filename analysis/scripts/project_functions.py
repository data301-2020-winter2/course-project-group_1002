import altair as alt
import vega_datasets as vg
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib
from ast import literal_eval
# %matplotlib inline
# %reload_ext autoreload
# %autoreload 2


# Some code to style plots

import matplotlib.pyplot as plt
import seaborn as sns

# Functions
def load_and_process(url): 
    #load
    data = pd.read_csv(url)
    
    #clean
    df = (data.
            dropna().
            reset_index().
            drop(columns={'index','release_date','id', 'count'}, axis=1, errors='ignore')  
         )
    
    #sort by year if it exists
    if 'year' in data.columns:
        df = df.sort_values(by='year')

    #data.to_csv('../data/processed/data.csv')    #we are going to save the files manually since there are so many of them and to avoid errors happening when overwriting
    return df

# since some column values are stored as arrays in string format, we need to convert that to lists and break it up for analysis 
def convert_and_explode(column, dataframe):
    dataframe[column] = dataframe[column].astype(str).apply(literal_eval)
    dataframe = dataframe.explode(column)
    
    return dataframe



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