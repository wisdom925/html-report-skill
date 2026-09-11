import subprocess
import json
import time
import urllib.parse
from datetime import datetime
import zoneinfo

ny_tz = zoneinfo.ZoneInfo("America/New_York")

target_date = "2026-09-10"
quotes_file = f"/Users/wisdom/html-report-skill/scratch/quotes_{target_date}.json"

with open(quotes_file, "r", encoding="utf-8") as f:
    results = json.load(f)

prev_quotes = {}
try:
    with open("/Users/wisdom/html-report-skill/scratch/quotes_2026-09-09.json", "r", encoding="utf-8") as f:
        prev_quotes = json.load(f)
except Exception as e:
    print("Could not load prev quotes:", e)

tickers = [
    # Indices
    "SPY", "QQQ", "DIA", "IWM", "SMH", "SOXX", "VIX", "^VIX", "^GSPC", "^IXIC", "^DJI", "^RUT", "^NDX", "^SOX",
    # Sectors & Styles
    "XLK", "IGV", "XLF", "XLV", "XLE", "XLI", "XLB", "XLRE", "XLU", "XLC", "XLY", "XLP", "RSP", "IWO", "IWN",
    # Mega-caps
    "NVDA", "AAPL", "MSFT", "GOOGL", "AMZN", "META", "TSLA",
    # Semis & Hardware
    "AMD", "AVGO", "MRVL", "MU", "TSM", "ASML", "ARM", "DELL", "VRT", "ANET",
    # Software & SaaS
    "CRM", "NOW", "SNOW", "ORCL", "ADBE", "PANW", "CRWD", "PLTR",
    # AI Power / Infra / Energy
    "CEG", "VST", "NRG", "ETN", "PWR", "GEV", "OKLO", "LITE", "COHR", "FLNC",
    # Macro / Commodities / Crypto
    "BTC-USD", "ETH-USD", "USO", "GLD", "DXY", "UUP", "^TNX", "^TYX", "^FVX", "^IRX", "CL=F", "GC=F"
]

missing = [t for t in tickers if t not in results]
print(f"Missing {len(missing)} tickers: {missing}")

for t in missing:
    time.sleep(0.6)
    encoded = urllib.parse.quote(t)
    url = f"https://query2.finance.yahoo.com/v8/finance/chart/{encoded}?interval=1d&range=5d"
    cmd = ["curl", "-s", "-A", "Mozilla/5.0 (Windows NT 10.0; Win64; x64)", url]
    try:
        proc = subprocess.run(cmd, capture_output=True, text=True, timeout=8)
        if not proc.stdout.strip() or "Too Many Requests" in proc.stdout:
            print(f"Failed/Rate limited for {t}")
            continue
        data = json.loads(proc.stdout)
        res = data['chart']['result'][0]
        meta = res.get('meta', {})
        quotes = res['indicators']['quote'][0]
        timestamps = res['timestamp']
        
        valid_pts = []
        for idx, (ts, o, h, l, c, v) in enumerate(zip(timestamps, quotes['open'], quotes['high'], quotes['low'], quotes['close'], quotes['volume'])):
            dt = datetime.fromtimestamp(ts, tz=ny_tz).strftime('%Y-%m-%d')
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
                    'timestamp': ts
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
            elif t in prev_quotes and 'price' in prev_quotes[t]:
                prev_close = prev_quotes[t]['price']
            elif 'chartPreviousClose' in meta:
                prev_close = meta['chartPreviousClose']
            else:
                prev_close = cur['close']
            
            change = cur['close'] - prev_close
            pct = (change / prev_close) * 100 if prev_close else 0.0
            
            results[t] = {
                'symbol': t,
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
            print(f"Fetched {t}: {cur['close']} ({pct:+.2f}%)")
        elif len(valid_pts) >= 1:
            cur = valid_pts[-1]
            prev_close = valid_pts[-2]['close'] if len(valid_pts) >= 2 else meta.get('chartPreviousClose', cur['close'])
            if t in prev_quotes and 'price' in prev_quotes[t]:
                prev_close = prev_quotes[t]['price']
            change = cur['close'] - prev_close
            pct = (change / prev_close) * 100 if prev_close else 0.0
            results[t] = {
                'symbol': t,
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
            print(f"Fetched {t} (last pt): {cur['close']} ({pct:+.2f}%)")
    except Exception as e:
        print(f"Error {t}: {e}")

if "^VIX" in results and "VIX" not in results:
    results["VIX"] = results["^VIX"]
if "VIX" in results and "^VIX" not in results:
    results["^VIX"] = results["VIX"]

with open(quotes_file, "w", encoding="utf-8") as f:
    json.dump(results, f, ensure_ascii=False, indent=2)

print(f"Done. Total quotes now: {len(results)}")
