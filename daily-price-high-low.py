import yfinance as yf
from datetime import datetime, timedelta

ticker_symbol = "BTC-USD"

end_date = datetime.now().date() - timedelta(days=1)
start_date = end_date - timedelta(days=1)

data = yf.download(ticker_symbol, start=start_date, end=end_date)

def get_yesterday_data(data):
    yesterday_data = data.iloc[-1]
    return yesterday_data

def main():
    yesterday_data = get_yesterday_data(data)
    closing_price = yesterday_data["Close"]
    high_price = yesterday_data["High"]
    low_price = yesterday_data["Low"]
    return high_price, low_price, closing_price