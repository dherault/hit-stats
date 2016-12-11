#!/usr/bin/python3.5
import pandas as pd
import matplotlib.ticker as ticker

df = pd.read_csv('hits.csv', header=None, names=['date', 'hits'], parse_dates=['date'])

ax = df.plot()
ticklabels = [date.strftime('%b %d') for date in df.date]
ax.xaxis.set_major_formatter(ticker.FixedFormatter(ticklabels))
fig = ax.get_figure()
fig.savefig('hits.png')
