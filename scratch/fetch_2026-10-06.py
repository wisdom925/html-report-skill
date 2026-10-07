import json,urllib.request,urllib.parse,time,datetime,zoneinfo
R="/Users/wisdom/html-report-skill/scratch/"
D="2026-10-06"
ny=zoneinfo.ZoneInfo("America/New_York")
syms=list(json.load(open(R+"quotes_2026-10-05.json")).keys())
out={}
def get(s):
    for a in range(4):
        h="query1" if a%2==0 else "query2"
        try:
            r=json.loads(urllib.request.urlopen(urllib.request.Request(f"https://{h}.finance.yahoo.com/v8/finance/chart/{urllib.parse.quote(s)}?range=3mo&interval=1d",headers={"User-Agent":"Mozilla/5.0"}),timeout=8).read())["chart"]["result"][0]
            q=r["indicators"]["quote"][0];pts=[];m=r["meta"];n=len(r["timestamp"])
            for k,(t,o,hh,l,c,v) in enumerate(zip(r["timestamp"],q["open"],q["high"],q["low"],q["close"],q["volume"])):
                if c is None and k==n-1 and m.get('regularMarketTime',0)>=t:
                    c=m['regularMarketPrice'];hh=m.get('regularMarketDayHigh') or c;l=m.get('regularMarketDayLow') or c;o=o or c
                if c is not None: pts.append((datetime.datetime.fromtimestamp(t,ny).strftime("%Y-%m-%d"),o or c,hh or c,l or c,c,v or 0,t))
            i=[p[0] for p in pts].index(D)
            cur=pts[i];prev=pts[i-1][4]
            def back(n): return round((cur[4]/pts[i-n][4]-1)*100,2) if i>=n else None
            d=dict(symbol=s,price=round(cur[4],2),open=round(cur[1],2),high=round(cur[2],2),low=round(cur[3],2),volume=cur[5],prev=round(prev,2),change=round(cur[4]-prev,2),pct=round((cur[4]/prev-1)*100,2),timestamp=cur[6],date=D)
            d["5d"]=back(5);d["1m"]=back(21)
            return d
        except Exception as e: time.sleep(1)
from concurrent.futures import ThreadPoolExecutor
syms=[x for x in syms if x!="VIX"]
with ThreadPoolExecutor(8) as ex:
    for s,r in zip(syms,ex.map(get,syms)):
        if r: out[s]=r
        else: print("MISSING",s,flush=True)
json.dump(out,open(R+f"quotes_{D}.json","w"),indent=1)
print(len(out))
