import urllib.request
import json
import time

tickers = [
    "SPY", "QQQ", "DIA", "IWM", "SMH", "SOXX", "VIX", "^VIX",
    "XLK", "IGV", "XLF", "XLV", "XLE", "XLI", "XLB", "XLRE", "XLU", "XLC", "XLY", "XLP",
    "NVDA", "AAPL", "MSFT", "GOOGL", "AMZN", "META", "TSLA", "SPCX",
    "AMD", "AVGO", "MRVL", "MU", "TSM", "ASML", "ARM", "DELL", "VRT", "ANET",
    "CRM", "NOW", "SNOW", "ORCL", "ADBE", "PANW", "CRWD", "PLTR",
    "CEG", "VST", "NRG", "ETN", "PWR", "GEV", "OKLO", "LITE", "COHR", "FLNC",
    "BTC-USD", "ETH-USD", "USO", "GLD", "DXY", "UUP", "^TNX", "^TYX", "^FVX"
]

results = {}

for ticker in tickers:
    url = f"https://query1.finance.yahoo.com/v8/finance/chart/{ticker}?interval=1d&range=5d"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode())
            meta = data['chart']['result'][0]['meta']
            quotes = data['chart']['result'][0]['indicators']['quote'][0]['close']
            timestamps = data['chart']['result'][0]['timestamp']
            
            # get recent non-null closes
            valid = [(t, c) for t, c in zip(timestamps, quotes) if c is not None]
            if len(valid) >= 2:
                latest_time, latest_close = valid[-1]
                prev_time, prev_close = valid[-2]
                change = latest_close - prev_close
                pct = (change / prev_close) * 100
                results[ticker] = {
                    'symbol': ticker,
                    'price': round(latest_close, 2),
                    'prev': round(prev_close, 2),
                    'change': round(change, 2),
                    'pct': round(pct, 2),
                    'timestamp': latest_time
                }
                print(f"{ticker}: {results[ticker]}")
    except Exception as e:
        print(f"Error {ticker}: {e}")

with open("/Users/wisdom/html-report-skill/scratch/quotes_2026-07-30.json", "w", encoding="utf-8") as f:
    json.dump(results, f, ensure_ascii=False, indent=2)

print("Quotes for 2026-07-30 written to scratch/quotes_2026-07-30.json")
