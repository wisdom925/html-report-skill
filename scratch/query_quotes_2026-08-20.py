import urllib.request
import json
import time
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor, as_completed

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
target_date = '2026-08-20'

def fetch_ticker(ticker):
    url = f"https://query1.finance.yahoo.com/v8/finance/chart/{ticker}?interval=1d&range=5d"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        with urllib.request.urlopen(req, timeout=5) as response:
            data = json.loads(response.read().decode())
            meta = data['chart']['result'][0]['meta']
            quotes = data['chart']['result'][0]['indicators']['quote'][0]['close']
            timestamps = data['chart']['result'][0]['timestamp']
            
            valid = []
            for t, c in zip(timestamps, quotes):
                if c is not None:
                    dt = datetime.fromtimestamp(t)
                    date_str = dt.strftime('%Y-%m-%d')
                    valid.append((t, c, date_str))
            
            target_idx = -1
            for i, (t, c, date_str) in enumerate(valid):
                if date_str == target_date:
                    target_idx = i
                    break
            
            if target_idx == -1 and len(valid) >= 1:
                last_date = valid[-1][2]
                if last_date in [target_date]:
                    target_idx = len(valid) - 1
            
            if target_idx >= 1:
                latest_time, latest_close, date_str = valid[target_idx]
                prev_time, prev_close, prev_date_str = valid[target_idx - 1]
                
                change = latest_close - prev_close
                pct = (change / prev_close) * 100
                return ticker, {
                    'symbol': ticker,
                    'price': round(latest_close, 2),
                    'prev': round(prev_close, 2),
                    'change': round(change, 2),
                    'pct': round(pct, 2),
                    'timestamp': latest_time,
                    'date': date_str
                }
            elif len(valid) >= 2:
                latest_time, latest_close, date_str = valid[-1]
                prev_time, prev_close, prev_date_str = valid[-2]
                change = latest_close - prev_close
                pct = (change / prev_close) * 100
                return ticker, {
                    'symbol': ticker,
                    'price': round(latest_close, 2),
                    'prev': round(prev_close, 2),
                    'change': round(change, 2),
                    'pct': round(pct, 2),
                    'timestamp': latest_time,
                    'date': date_str
                }
    except Exception as e:
        print(f"Error {ticker}: {e}")
    return ticker, None

print("Fetching quotes in parallel for 2026-08-20...")
with ThreadPoolExecutor(max_workers=15) as executor:
    futures = {executor.submit(fetch_ticker, t): t for t in tickers}
    for fut in as_completed(futures):
        ticker = futures[fut]
        try:
            res = fut.result()
            if res and res[1] is not None:
                results[res[0]] = res[1]
        except Exception as exc:
            print(f"{ticker} generated an exception: {exc}")

print("Sample results:")
for t in ["SPY", "QQQ", "^VIX", "NVDA", "BTC-USD"]:
    if t in results:
        print(f"{t}: {results[t]}")
    else:
        print(f"{t} not found in results")

with open("/Users/wisdom/html-report-skill/scratch/quotes_2026-08-20.json", "w", encoding="utf-8") as f:
    json.dump(results, f, ensure_ascii=False, indent=2)

print(f"Quotes for 2026-08-20 written to scratch/quotes_2026-08-20.json. Total count: {len(results)}")
