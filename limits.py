import yfinance as yf
import pandas as pd
from coinbase.wallet.client import Client
# import json
# import time
# import websocket
import datetime as dt
# import numpy as np
# import math
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt
import importlib  
from config import API_KEY, SECRET_KEY
daily_price_high_low = importlib.import_module("daily-price-high-low")

COLOR_RED = "\033[31m"
COLOR_GREEN = "\033[32m"
COLOR_YELLOW = "\033[33m"
COLOR_RESET = "\033[0m"

# Coinbase API
api_key = API_KEY
api_secret = SECRET_KEY
client = Client(api_key, api_secret)

user = client.get_current_user()
accounts = client.get_accounts()
currencies = client.get_currencies()
payment_method = client.get_payment_methods()[0]
account = client.get_primary_account()

currency_pair = 'BTC-USD'
buy_price = client.get_buy_price(currency_pair = 'BTC-USD')
sell_price = client.get_sell_price(currency_pair = 'BTC-USD')

high, low, close = daily_price_high_low.main()

def main(n):
    if n > high:
        print(COLOR_GREEN + "SELL" + COLOR_RESET, high, low, close)
    elif n < low:
        print(COLOR_RED + "BUY" + COLOR_RESET, high, low, close)
    else:
        print(COLOR_YELLOW + "HOLD" + COLOR_RESET, high, low, close)
