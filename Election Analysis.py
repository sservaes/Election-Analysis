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
poll_df.drop('Question Iteration', axis = 1, inplace = True)

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

# %% time analysis

poll_df.head()
poll_df[['Trump', 'Clinton', 'Undecided']].plot(linestyle = '', marker = 'o', figsize = (20, 8))

# %% Calculate difference

from datetime import datetime

poll_df['Difference'] = (poll_df['Trump'] - poll_df['Clinton'])/100

poll_df.head()

# %% group Difference

poll_df_group = poll_df.groupby(['Start Date'], as_index = False).mean()

poll_df_group.head()

# %% plot Difference

poll_df_group.plot('Start Date', 'Difference', figsize = (20,4), marker = 'o', linestyle = '-', color = 'blue')

# %% look at october 2012
row_in = 0
xlimit = []

for date in poll_df_group['Start Date']:
    if date[0:7] == '2016-10':
        xlimit.append(row_in)
        row_in += 1
    else:
        row_in += 1

print(min(xlimit))
print(max(xlimit))

# %% plot october 2012

poll_df_group.plot('Start Date', 'Difference', figsize = (20,4), marker = 'o', linestyle = '-', color = 'blue', xlim = (232, 262))
plt.axvline(x = 232 + 2, linewidth = 4, color = 'red')
plt.axvline(x = 232 + 10, linewidth = 4, color = 'red')
plt.axvline(x = 232 + 21, linewidth = 4, color = 'red')
