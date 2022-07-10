# %%
# Data Sources
from yahoofinancials import YahooFinancials

# Raw packages
import pandas as pd
import numpy as np
import stockquotes
import requests
from bs4 import BeautifulSoup
import ast
# Visualizer
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objs as go
# %%
tickers = ['META']

yahoo_get = YahooFinancials(tickers)
data = yahoo_get.get_stock_price_data()
current_df = pd.DataFrame(data)
print(current_df.loc['regularMarketPrice'])

# %%
current_df.loc[['regularMarketPrice', 'regularMarketChange', 'regularMarketChangePercent', 'regularMarketVolume']]
# %%







# %%




# %%
