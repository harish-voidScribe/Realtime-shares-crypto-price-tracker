import requests
import json
import yfinance as yf

crypto_key = "https://api.binance.com/api/v3/ticker/price?symbol="

crypto_symbols = []
stock_symbols = []

while True:
    crypto_symbol = input("Enter cryptocurrency symbol (or 'OK' to move to stocks)[Ex:-BTCUSDT DOGEUSDT]:: ").upper()
    if crypto_symbol == 'OK':
        break
    crypto_symbols.append(crypto_symbol)
  
while (True):
    stock_symbol = input("Enter stock symbol (or 'done' to finish)[Ex:-AAPL GOOGL]::").upper()
    if stock_symbol == 'DONE':
        break
    stock_symbols.append(stock_symbol)

print("Cryptocurrency Prices:")
for symbol in crypto_symbols:
    url = crypto_key + symbol
    response = requests.get(url)
    data = response.json()
    if 'symbol' in data and 'price' in data:
        print(f"{data['symbol']} price is {data['price']}")
    else:
        print(f"Failed to retrieve price information for {symbol}. Please check the cryptocurrency symbol.")

print("\nStock Prices:")
for symbol in stock_symbols:
    try:
        ticker = yf.Ticker(symbol)
        history = ticker.history(period="1d")
        if not history.empty:
            latest_price = history["Close"][-1]
            print(f"{symbol} price is {latest_price}")
        else:
            print(f"Failed to retrieve price information for {symbol}. No data available.")
    except Exception as e:
        print(f"Failed to retrieve price information for {symbol}. Error: {e}")
