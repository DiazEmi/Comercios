# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 22:17:45 2021

@author: emili
"""
import pandas as pd
import numpy as np
from binance import Client, ThreadedWebsocketManager, ThreadedDepthCacheManager
client = Client('ZGNAShcASqQDdL9ik97h6P9DmhhX6KzcwFf4aYpn4LCqgfgoEV6WEeGeMFrvf8zY', 'CMDczymGSkYxsXtFW5XJB98LpxE1wdg7Ki065bz4NqyiWLAEbGmPIRcRsPC45eU2', testnet=True)

k=[0,0,0,0,0,0,0,0,0,0]
info = pd.DataFrame()


aa=0
import time
while True:
    a = time.strftime("%S")
    if a != aa:
        aa=a
        btc_price = client.get_symbol_ticker(symbol="BTCUSDT")
        k = (btc_price['price'])
        print(k)