import urllib.request
import json
import time

symbols = [
    "SPY", "QQQ", "DIA", "IWM", "SMH", "SOXX", "VIX", "^VIX", "XLK", "IGV",
    "XLF", "XLV", "XLE", "XLI", "XLB", "XLRE", "XLU", "XLC", "XLY", "XLP",
    "NVDA", "AAPL", "MSFT", "GOOGL", "AMZN", "META", "TSLA", "SPCX",
    "AMD", "AVGO", "MRVL", "MU", "TSM", "ASML", "ARM", "DELL", "VRT", "ANET",
    "CRM", "NOW", "SNOW", "ORCL", "ADBE", "PANW", "CRWD", "PLTR",
    "CEG", "VST", "NRG", "ETN", "PWR", "GEV", "OKLO", "LITE", "COHR", "FLNC",
    "BTC-USD", "ETH-USD", "USO", "GLD", "DXY", "UUP", "^TNX", "^TYX", "^FVX"
]

def fetch_quote(sym):
    url = f"https://query1.finance.yahoo.com/v8/finance/chart/{sym}?interval=1d&range=1d"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    try:
        with urllib.request.urlopen(req, timeout=5) as r:
            res = json.loads(r.read())
            result = res["chart"]["result"][0]
            meta = result["meta"]
            price = meta.get("regularMarketPrice")
            prev = meta.get("chartPreviousClose")
            if price is None:
                # Try getting from indicators
                adjclose = result["indicators"]["adjclose"][0]["adjclose"][-1]
                price = adjclose
            change = price - prev if price is not None and prev is not None else 0
            pct = (change / prev * 100) if prev else 0
            return {
                "symbol": sym,
                "price": price,
                "prev": prev,
                "change": change,
                "pct": pct
            }
    except Exception as e:
        return {"symbol": sym, "error": str(e)}

results = {}
for sym in symbols:
    res = fetch_quote(sym)
    results[sym] = res
    print(f"{sym}: {res}")
    time.sleep(0.05)

with open("/Users/wisdom/html-report-skill/scratch/quotes_2026-06-23.json", "w") as f:
    json.dump(results, f, indent=2)
