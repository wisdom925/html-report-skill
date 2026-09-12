import urllib.request
import json
import time
from datetime import datetime
import zoneinfo

ny_tz = zoneinfo.ZoneInfo("America/New_York")
target_date = "2026-09-11"

quotes_file = f"/Users/wisdom/html-report-skill/scratch/quotes_{target_date}.json"
with open(quotes_file, "r", encoding="utf-8") as f:
    results = json.load(f)

prev_quotes = {}
try:
    with open("/Users/wisdom/html-report-skill/scratch/quotes_2026-09-10.json", "r", encoding="utf-8") as f:
        prev_quotes = json.load(f)
except Exception as e:
    print("Could not load prev quotes:", e)

missing_tickers = ['AAPL', 'AMZN', 'XLK', 'DELL', 'CRWD', 'CEG', 'PWR', 'LITE', '^VIX', '^DJI']

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36'}

for ticker in missing_tickers:
    time.sleep(1.2)
    url = f"https://query1.finance.yahoo.com/v8/finance/chart/{ticker}?interval=1d&range=10d"
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode())
            res = data['chart']['result'][0]
            meta = res.get('meta', {})
            quotes = res['indicators']['quote'][0]
            timestamps = res['timestamp']
            
            valid_pts = []
            for idx, (t, o, h, l, c, v) in enumerate(zip(timestamps, quotes['open'], quotes['high'], quotes['low'], quotes['close'], quotes['volume'])):
                dt = datetime.fromtimestamp(t, tz=ny_tz).strftime('%Y-%m-%d')
                if c is None and idx == len(timestamps) - 1:
                    c = meta.get('regularMarketPrice')
                    if h is None:
                        h = meta.get('regularMarketDayHigh', c)
                    if l is None:
                        l = meta.get('regularMarketDayLow', c)
                    if o is None:
                        o = meta.get('regularMarketOpen', c)
                if c is not None:
                    valid_pts.append({
                        'date': dt,
                        'open': o if o is not None else c,
                        'high': h if h is not None else c,
                        'low': l if l is not None else c,
                        'close': c,
                        'volume': v if v is not None else 0,
                        'timestamp': t
                    })
            
            target_idx = -1
            for i, pt in enumerate(valid_pts):
                if pt['date'] == target_date:
                    target_idx = i
                    break
            
            if target_idx != -1:
                cur = valid_pts[target_idx]
                if target_idx > 0:
                    prev_close = valid_pts[target_idx - 1]['close']
                elif ticker in prev_quotes and 'price' in prev_quotes[ticker]:
                    prev_close = prev_quotes[ticker]['price']
                elif 'chartPreviousClose' in meta:
                    prev_close = meta['chartPreviousClose']
                else:
                    prev_close = cur['close']
                
                change = cur['close'] - prev_close
                pct = (change / prev_close) * 100 if prev_close else 0.0
                
                results[ticker] = {
                    'symbol': ticker,
                    'price': round(cur['close'], 2),
                    'open': round(cur['open'], 2) if cur['open'] is not None else round(cur['close'], 2),
                    'high': round(cur['high'], 2) if cur['high'] is not None else round(cur['close'], 2),
                    'low': round(cur['low'], 2) if cur['low'] is not None else round(cur['close'], 2),
                    'volume': cur['volume'],
                    'prev': round(prev_close, 2),
                    'change': round(change, 2),
                    'pct': round(pct, 2),
                    'timestamp': cur['timestamp'],
                    'date': cur['date']
                }
                print(f"Added {ticker}: price={results[ticker]['price']}, pct={results[ticker]['pct']:+.2f}%")
            elif len(valid_pts) >= 1:
                cur = valid_pts[-1]
                prev_close = valid_pts[-2]['close'] if len(valid_pts) >= 2 else meta.get('chartPreviousClose', cur['close'])
                if ticker in prev_quotes and 'price' in prev_quotes[ticker]:
                    prev_close = prev_quotes[ticker]['price']
                change = cur['close'] - prev_close
                pct = (change / prev_close) * 100 if prev_close else 0.0
                results[ticker] = {
                    'symbol': ticker,
                    'price': round(cur['close'], 2),
                    'open': round(cur['open'], 2) if cur['open'] is not None else round(cur['close'], 2),
                    'high': round(cur['high'], 2) if cur['high'] is not None else round(cur['close'], 2),
                    'low': round(cur['low'], 2) if cur['low'] is not None else round(cur['close'], 2),
                    'volume': cur['volume'],
                    'prev': round(prev_close, 2),
                    'change': round(change, 2),
                    'pct': round(pct, 2),
                    'timestamp': cur['timestamp'],
                    'date': cur['date']
                }
                print(f"Added {ticker} (fallback): price={results[ticker]['price']}, pct={results[ticker]['pct']:+.2f}%")
    except Exception as e:
        print(f"Error {ticker}: {e}")

if "^VIX" in results:
    results["VIX"] = results["^VIX"]

with open(quotes_file, "w", encoding="utf-8") as f:
    json.dump(results, f, ensure_ascii=False, indent=2)

print(f"Final total quotes: {len(results)}")
