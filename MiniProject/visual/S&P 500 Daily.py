import yfinance as yf
import pandas as pd


sp500 = yf.Ticker('^GSPC')
sp500_hist = sp500.history(period='1d')
#sp500_hist.to_csv('sp500_1y.csv')
result = sp500_hist.to_json(orient="records")
print(result)