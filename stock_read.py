# %%
import pandas as pd
import datetime, requests
from requests.exceptions import ConnectionError
from bs4 import BeautifulSoup

def web_content_div(web_content, class_path):
    print('inside webcontent div')
    # web_content_div = web_content.find_all('div', {'class': class_path})
    # print(web_content, web_content_div)
    
    spans = web_content.find_all()
    texts = [span.get_text() for span in spans]
    return texts

def real_time_price(stock):
    url = 'https://finance.yahoo.com/quote/' + stock + '?p=' + stock + '&.tsrc=fin-srch'
    try:
        r = requests.get(url)
        web_content = BeautifulSoup(r.text, 'html.parser')
        texts = web_content_div(web_content, "My(6px) Pos(r) smartphone_Mt(6px) W(100%) ")
        # if texts != []:
            # price, change = texts[0], texts[1]
            # soup.find('div', {'class': 'D(ib) Mend(20px)'}).find_all()[0].text
            # print('success', price, change)
        volume = []
        targetPrice = []
        for count, vol in enumerate(texts):
            if vol == 'Volume':
                volume.append(texts[count+1])
            elif vol == '1y Target Est':
                targetPrice.append(texts[count+1])
        print(volume[1], targetPrice[1])
            # elif vol == 'regularMarketPrice':
            #     print(texts[count+1])
            # elif vol == 'Change':
            #     print(texts[count+1])

    except ConnectionError:
        price, change = [], []
    # return price, change
    
    


Stock = 'META'
real_time_price(Stock)




# %%
# Web Scrapping from Pandas Datareader
import pandas as pd
import pandas_datareader.data as web
import matplotlib.pyplot as plt
from datetime import date, timedelta
import streamlit as st
today = date.today()

d1 = today.strftime("%Y/%m/%d")
end_date = d1
d2 = date.today() - timedelta(days=360)
d2 = d2.strftime("%Y/%m/%d")
start_date = d2

st.title("Real-time Stock Price Data")
# a = st.text_input("Enter Any Company >>:")
a = 'META'
data = web.DataReader(name=a, data_source='yahoo', start=start_date, end=end_date)
fig, ax = plt.subplots() 
ax = data["Close"].plot(figsize=(12, 8), title=a+" Stock Prices", fontsize=20, label="Close Price")
plt.legend()
plt.grid()
st.pyplot(fig)

# %%
# Using yfinance
import yfinance
# Valid periods: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max
# Valid intervals: 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo
tickers = ['META']
data_1m = yfinance.download(tickers=tickers, period='1d', interval='1m')
# %%
data_1m.to_csv('META.csv', mode='a', header=False)

# %%
fig, ax = plt.subplots() 
ax = data_1m["Adj Close"].plot(figsize=(12, 8), title=a+" Stock Prices", fontsize=20, label="Adj Close Price")
plt.legend()
plt.grid()
st.pyplot(fig)
# %%
fig, ax = plt.subplots() 
ax = data_1m["Volume"].plot(figsize=(12, 8), title=a+" Volumes", fontsize=20, label="Volume")
plt.legend()
plt.grid()
st.pyplot(fig)
# %%
