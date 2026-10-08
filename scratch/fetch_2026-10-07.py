import json, urllib.request, urllib.parse, time, datetime, zoneinfo
from concurrent.futures import ThreadPoolExecutor

R = "/Users/wisdom/html-report-skill/scratch/"
D = "2026-10-07"
ny = zoneinfo.ZoneInfo("America/New_York")
base_quotes = json.load(open(R + "quotes_2026-10-06.json"))
syms = list(base_quotes.keys())
out = {}

def get(s):
    url = f"https://query1.finance.yahoo.com/v8/finance/chart/{urllib.parse.quote(s)}?range=3mo&interval=1d"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    for attempt in range(3):
        try:
            with urllib.request.urlopen(req, timeout=6) as resp:
                data = json.loads(resp.read().decode())
            r = data["chart"]["result"][0]
            q = r["indicators"]["quote"][0]
            m = r["meta"]
            pts = []
            n = len(r["timestamp"])
            for k, (t, o, hh, l, c, v) in enumerate(zip(r["timestamp"], q["open"], q["high"], q["low"], q["close"], q["volume"])):
                if c is None and k == n - 1 and m.get('regularMarketTime', 0) >= t:
                    c = m.get('regularMarketPrice')
                    hh = m.get('regularMarketDayHigh') or c
                    l = m.get('regularMarketDayLow') or c
                    o = o or c
                if c is not None:
                    pts.append((datetime.datetime.fromtimestamp(t, ny).strftime("%Y-%m-%d"), o or c, hh or c, l or c, c, v or 0, t))
            if not pts:
                return None
            dates = [p[0] for p in pts]
            if D in dates:
                i = dates.index(D)
            else:
                i = len(pts) - 1
            cur = pts[i]
            prev = pts[i-1][4] if i > 0 else cur[4]
            def back(num):
                return round((cur[4]/pts[i-num][4]-1)*100, 2) if i>=num else None
            return dict(
                symbol=s,
                price=round(cur[4], 2),
                open=round(cur[1], 2),
                high=round(cur[2], 2),
                low=round(cur[3], 2),
                volume=cur[5],
                prev=round(prev, 2),
                change=round(cur[4]-prev, 2),
                pct=round((cur[4]/prev-1)*100, 2),
                timestamp=cur[6],
                date=cur[0],
                **{"5d": back(5), "1m": back(21)}
            )
        except Exception as e:
            time.sleep(0.5)
    return None

with ThreadPoolExecutor(4) as ex:
    results = list(ex.map(get, syms))
    for s, res in zip(syms, results):
        if res:
            out[s] = res
        else:
            print(f"FAILED: {s}", flush=True)

# Fallback for any missing from base_quotes
for s in syms:
    if s not in out:
        print(f"Using fallback for {s}")
        out[s] = base_quotes[s]

json.dump(out, open(R + f"quotes_{D}.json", "w"), indent=1)
print(f"Successfully saved {len(out)} quotes for {D}")
