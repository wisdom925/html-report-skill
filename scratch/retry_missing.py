import urllib.request
import urllib.parse
import json
import time
import random
from datetime import datetime
import zoneinfo

ny_tz = zoneinfo.ZoneInfo("America/New_York")
target_date = "2026-09-29"

missing = ["SOXX", "QQQ", "XLI", "TSLA", "MRVL", "TSM", "VRT", "CRM", "SNOW", "PANW", "PWR", "GEV", "OKLO", "COHR", "ETH-USD", "^TNX", "BZ=F"]

with open("/Users/wisdom/html-report-skill/scratch/quotes_2026-09-29.json", "r", encoding="utf-8") as f:
    results = json.load(f)

prev_quotes = {}
try:
    with open("/Users/wisdom/html-report-skill/scratch/quotes_2026-09-28.json", "r", encoding="utf-8") as f:
        prev_quotes = json.load(f)
except Exception as e:
    pass

USER_AGENTS = [
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_4_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.4.1 Safari/605.1.15",
]

def fetch_ticker(ticker):
    subdomains = ["query1", "query2"]
    encoded_ticker = urllib.parse.quote(ticker)
    
    for attempt in range(8):
        sub = subdomains[attempt % len(subdomains)]
        url = f"https://{sub}.finance.yahoo.com/v8/finance/chart/{encoded_ticker}?interval=1d&range=10d"
        ua = random.choice(USER_AGENTS)
        req = urllib.request.Request(url, headers={'User-Agent': ua})
        try:
            time.sleep(random.uniform(0.3, 0.8))
            with urllib.request.urlopen(req, timeout=12) as response:
                data = json.loads(response.read().decode())
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
                        prev = valid_pts[target_idx - 1]
                        prev_close = prev['close']
                    elif ticker in prev_quotes and 'price' in prev_quotes[ticker]:
                        prev_close = prev_quotes[ticker]['price']
                    elif 'chartPreviousClose' in meta:
                        prev_close = meta['chartPreviousClose']
                    else:
                        prev_close = cur['close']
                    
                    change = cur['close'] - prev_close
                    pct = (change / prev_close) * 100 if prev_close else 0.0
                    
                    return {
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
                elif len(valid_pts) >= 1:
                    cur = valid_pts[-1]
                    prev_close = valid_pts[-2]['close'] if len(valid_pts) >= 2 else meta.get('chartPreviousClose', cur['close'])
                    if ticker in prev_quotes and 'price' in prev_quotes[ticker]:
                        prev_close = prev_quotes[ticker]['price']
                    change = cur['close'] - prev_close
                    pct = (change / prev_close) * 100 if prev_close else 0.0
                    return {
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
        except Exception as e:
            time.sleep(0.5 + attempt * 0.5)
    return None

for t in missing:
    res = fetch_ticker(t)
    if res:
        results[t] = res
        print(f"Successfully fetched {t}: {res['price']} ({res['pct']}%)")
    else:
        print(f"Failed again: {t}")

with open("/Users/wisdom/html-report-skill/scratch/quotes_2026-09-29.json", "w", encoding="utf-8") as f:
    json.dump(results, f, ensure_ascii=False, indent=2)

print(f"Total quotes now: {len(results)}")
