import json,urllib.request,time
out={}
def sma(c,n): return sum(c[-n:])/n
for s in ["SPY","QQQ","IWM","SMH","IGV","XLK"]:
    for h in ("query1","query2","query1"):
        try:
            r=json.loads(urllib.request.urlopen(urllib.request.Request(f"https://{h}.finance.yahoo.com/v8/finance/chart/{s}?range=1y&interval=1d",headers={"User-Agent":"Mozilla/5.0"}),timeout=8).read())["chart"]["result"][0]
            q=r["indicators"]["quote"][0];c=[x for x in q["close"] if x]
            g=[c[i]-c[i-1] for i in range(len(c)-14,len(c))]
            au=sum(x for x in g if x>0)/14;ad=-sum(x for x in g if x<0)/14
            rsi=100-100/(1+au/ad) if ad else 100
            def ema(n):
                k=2/(n+1);e=c[0]
                for x in c[1:]: e=x*k+e*(1-k)
                return e
            hi=max(x for x in q["high"] if x);hi20=max(x for x in q["high"][-20:] if x);lo20=min(x for x in q["low"][-20:] if x)
            out[s]=dict(price=c[-1],sma20=sma(c,20),sma50=sma(c,50),sma100=sma(c,100),sma200=sma(c,200),rsi=rsi,macd=ema(12)-ema(26),hi52=hi,hi20=hi20,lo20=lo20)
            break
        except Exception as e: time.sleep(2)
    time.sleep(1.5)
json.dump(out,open("/Users/wisdom/html-report-skill/scratch/tech_2026-10-05.json","w"),indent=1)
print(json.dumps(out,indent=1))
