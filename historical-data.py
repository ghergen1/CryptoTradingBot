import yfinance as yf
from datetime import datetime, timedelta

ticker_symbol = "BTC-USD"

end_date = datetime.now().date() - timedelta(days=30)
start_date = end_date - timedelta(days=30)

data = yf.download(ticker_symbol, start=start_date, end=end_date)

def get_historical_data():
    return data["Close"]

print(get_historical_data(data))
