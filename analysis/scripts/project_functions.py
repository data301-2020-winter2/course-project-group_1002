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


# Some code to stype plots

import matplotlib.pyplot as plt
import seaborn as sns

# Functions
def load_and_process(url): 
    import pandas as pd
    data = pd.read_csv(url)
    new_data = (data.
            #rename(columns={' Rocket':'Mission Cost'}).
            dropna().
            reset_index().
            drop(columns='index').
            sort_values(by='popularity').
            assign(release_date_time = pd.
                   to_datetime(data['release_date'],
                               utc=True).
                   dt.date))
    return new_data