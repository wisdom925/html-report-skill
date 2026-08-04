import urllib.request
import json

tickers = ["SPY", "QQQ", "IWM", "SMH", "IGV", "XLK"]
for ticker in tickers:
    url = f"https://query1.finance.yahoo.com/v8/finance/chart/{ticker}?interval=1d&range=100d"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode())
            closes = data['chart']['result'][0]['indicators']['quote'][0]['close']
            # Filter out None values
            valid_closes = [c for c in closes if c is not None]
            if len(valid_closes) >= 50:
                ma20 = sum(valid_closes[-20:]) / 20
                ma50 = sum(valid_closes[-50:]) / 50
                price = valid_closes[-1]
                print(f"{ticker}: Close={price:.2f}, 20MA={ma20:.2f}, 50MA={ma50:.2f}")
    except Exception as e:
        print(f"Error {ticker}: {e}")
