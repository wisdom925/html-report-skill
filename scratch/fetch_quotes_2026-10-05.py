import json, time, urllib.request, urllib.parse, datetime
from concurrent.futures import ThreadPoolExecutor
D = "2026-10-05"
B = "/Users/wisdom/html-report-skill/scratch/"
old = json.load(open(B + "quotes_2026-10-02.json"))
syms = [s for s in old if s not in ("VIX", "DXY")]
import os
F=B+"quotes_2026-10-05.json"
out = json.load(open(F)) if os.path.exists(F) else {}
syms=[x for x in syms if x not in out]
print("todo",len(syms),flush=True)

def work(s):
    for host in ("query1", "query2", "query1"):
        url = "https://%s.finance.yahoo.com/v8/finance/chart/%s?interval=1d&range=1mo" % (host, urllib.parse.quote(s))
        try:
            r = json.loads(urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"}), timeout=6).read())["chart"]["result"][0]
            ts = r["timestamp"]; q = r["indicators"]["quote"][0]
            off = r["meta"].get("gmtoffset", 0)
            days = [datetime.datetime.fromtimestamp(t + off, datetime.timezone.utc).strftime("%Y-%m-%d") for t in ts]
            if D not in days:
                print("nodate", s, days[-1], flush=True); return
            i = days.index(D)
            closes = q["close"]
            if closes[i] is None: closes[i]=r['meta']['regularMarketPrice']
            if q['open'][i] is None: q['open'][i]=q['high'][i]=q['low'][i]=closes[i]
            c = closes[i]; prev = closes[i - 1]
            d = dict(symbol=s, price=round(c, 2), open=round(q["open"][i] or 0, 2), high=round(q["high"][i] or 0, 2),
                     low=round(q["low"][i] or 0, 2), volume=q["volume"][i], prev=round(prev, 2),
                     change=round(c - prev, 2), pct=round((c - prev) / prev * 100, 2), timestamp=ts[i], date=D)
            if i >= 5 and closes[i - 5]: d["5d"] = round((c / closes[i - 5] - 1) * 100, 2)
            first = next(x for x in closes if x)
            d["1m"] = round((c / first - 1) * 100, 2)
            out[s] = d; return
        except Exception as e:
            err = e; time.sleep(2)
    print("fail", s, err, flush=True)

with ThreadPoolExecutor(2) as ex:
    list(ex.map(work, syms))
out["VIX"] = out.get("^VIX", {}); out["DXY"] = out.get("DX-Y.NYB", {})
out={k:v for k,v in out.items() if v}
json.dump(out, open(B + "quotes_2026-10-05.json", "w"), indent=2)
print(len(out), flush=True)
for k in ["^GSPC", "^IXIC", "^DJI", "^NDX", "^RUT", "^SOX", "^VIX", "^TNX", "^TYX", "^FVX", "^IRX", "GC=F", "CL=F", "BZ=F", "BTC-USD", "ETH-USD", "DX-Y.NYB", "SPY", "QQQ"]:
    print(k, out.get(k))
