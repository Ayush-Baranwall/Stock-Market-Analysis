#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install yfinance')


# In[2]:


import yfinance as yf


# In[3]:


import matplotlib.pyplot as plt


# In[4]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[6]:


import pandas as pd


# In[7]:


stock=pd.read_csv("C:/Users/djnag/Downloads/istanbul_stock_exchange.csv",encoding = "ISO-8859-1")


# In[8]:


stock.head()


# In[9]:


stock[["DAX"]].plot()


# In[13]:


import plotly.graph_objects as go

fig = go.Figure(data=go.Ohlc(x=stock['date'],
        open=stock['SP'],
        high=stock['DAX'],
        low=stock['FTSE'],
        close=stock['BOVESPA']))
fig.show()


# In[ ]:




