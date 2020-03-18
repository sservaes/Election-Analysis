# %% Import modules

import pandas as pd
import numpy as np
from pandas import Series, DataFrame
import matplotlib.pyplot as plt
import seaborn as sns
import requests
from io import StringIO
sns.set_style('whitegrid')

# %% grab data from the web

url = "http://elections.huffingtonpost.com/pollster/2016-general-election-trump-vs-clinton.csv"

source = requests.get(url).text
poll_data = StringIO(source)
poll_df = pd.read_csv(poll_data)

# %% get info

poll_df.info()

# %% get first rows

poll_df.head()

# %% plot affiliation

sns.catplot('Affiliation', data = poll_df, kind = 'count')

# %% plot affiliation with population

sns.catplot('Affiliation', data = poll_df, kind = 'count', hue = 'Population')

# %% look at the averages

avg = pd.DataFrame(poll_df.mean())

avg.drop('Number of Observations', axis = 0, inplace = True)

std = pd.DataFrame(poll_df.std())

std.drop('Number of Observations', axis = 0, inplace = True)

avg.head()

# %% plot the averages

avg.plot(yerr = std, kind = 'bar', legend = False)

# %% undecided factor

poll_avg = pd.concat([avg, std], axis = 1)
poll_avg.columns = ['Average', 'STD']

poll_avg.head()
