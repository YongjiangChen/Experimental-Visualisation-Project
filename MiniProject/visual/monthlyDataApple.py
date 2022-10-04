import json
import requests

url = 'https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY&symbol=AAPL&apikey=TF572P5Y3TV79I7T'
r = requests.get(url)
data = r.json()
print(data['Monthly Time Series']['2022-10-03'])