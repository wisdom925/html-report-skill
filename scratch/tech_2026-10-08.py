import json, urllib.request, time, socket

# Force IPv4 to avoid IPv6 "No route to host"
orig_getaddrinfo = socket.getaddrinfo
def getaddrinfo_ipv4(*args, **kwargs):
    responses = orig_getaddrinfo(*args, **kwargs)
    ipv4 = [r for r in responses if r[0] == socket.AF_INET]
    return ipv4 if ipv4 else responses
socket.getaddrinfo = getaddrinfo_ipv4

out = {}
Q = json.load(open("/Users/wisdom/html-report-skill/scratch/quotes_2026-10-08.json"))

def sma(c, n):
    return sum(c[-n:]) / n

for s in ["SPY", "QQQ", "IWM", "SMH", "IGV", "XLK"]:
    for h in ("query1", "query2"):
        try:
            req = urllib.request.Request(
                f"https://{h}.finance.yahoo.com/v8/finance/chart/{s}?range=1y&interval=1d",
                headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"}
            )
            r = json.loads(urllib.request.urlopen(req, timeout=5).read().decode())["chart"]["result"][0]
            q = r["indicators"]["quote"][0]
            closes = q["close"]
            highs = q["high"]
            lows = q["low"]
            if closes[-1] is None:
                closes[-1] = Q[s]["price"]
                highs[-1] = Q[s]["high"]
                lows[-1] = Q[s]["low"]
            c = [x for x in closes if x is not None]
            h_clean = [x for x in highs if x is not None]
            l_clean = [x for x in lows if x is not None]
            
            g = [c[i] - c[i-1] for i in range(len(c)-14, len(c))]
            au = sum(x for x in g if x > 0) / 14
            ad = -sum(x for x in g if x < 0) / 14
            rsi = 100 - 100 / (1 + au / ad) if ad else 100
            def ema(n):
                k = 2 / (n + 1)
                e = c[0]
                for x in c[1:]:
                    e = x * k + e * (1 - k)
                return e
            hi = max(h_clean)
            hi20 = max(h_clean[-20:])
            lo20 = min(l_clean[-20:])
            out[s] = dict(
                price=c[-1],
                sma20=sma(c, 20),
                sma50=sma(c, 50),
                sma100=sma(c, 100),
                sma200=sma(c, 200),
                rsi=rsi,
                macd=ema(12) - ema(26),
                hi52=hi,
                hi20=hi20,
                lo20=lo20
            )
            print(f"Computed tech for {s}: price={c[-1]:.2f}, RSI={rsi:.1f}")
            break
        except Exception as e:
            print(f"Error {s} on {h}: {e}")
            time.sleep(0.3)

json.dump(out, open("/Users/wisdom/html-report-skill/scratch/tech_2026-10-08.json", "w"), indent=1)
print(f"Saved tech_2026-10-08.json with {len(out)} items")
