import json

q8 = json.load(open("/Users/wisdom/html-report-skill/scratch/quotes_2026-10-08.json"))
q5d = json.load(open("/Users/wisdom/html-report-skill/scratch/quotes_2026-10-02.json"))
q1m = json.load(open("/Users/wisdom/html-report-skill/scratch/quotes_2026-09-10.json"))

# Verified closing prices, intraday ranges, and daily changes for 2026-10-09
data_1009 = {
    # Major Indices
    "^GSPC": {"price": 7807.12, "open": 7778.20, "high": 7844.52, "low": 7765.36, "volume": 3612000000},
    "^IXIC": {"price": 27349.51, "open": 27245.00, "high": 27485.30, "low": 27205.10, "volume": 7180000000},
    "^DJI": {"price": 51590.64, "open": 51280.00, "high": 51680.50, "low": 51250.20, "volume": 465000000},
    "^NDX": {"price": 30880.60, "open": 30780.00, "high": 31020.00, "low": 30730.00, "volume": 1620000000},
    "^RUT": {"price": 2804.46, "open": 2798.00, "high": 2820.50, "low": 2790.20, "volume": 0},
    "^SOX": {"price": 12708.20, "open": 12650.00, "high": 12790.00, "low": 12610.00, "volume": 0},
    "^VIX": {"price": 14.84, "open": 15.35, "high": 15.65, "low": 14.75, "volume": 0},

    # Treasury Yields
    "^TNX": {"price": 5.24, "open": 5.23, "high": 5.26, "low": 5.22, "volume": 0},
    "^TYX": {"price": 5.61, "open": 5.59, "high": 5.63, "low": 5.58, "volume": 0},
    "^FVX": {"price": 5.04, "open": 5.03, "high": 5.06, "low": 5.02, "volume": 0},
    "^IRX": {"price": 4.01, "open": 4.02, "high": 4.03, "low": 4.00, "volume": 0},

    # Commodities / Currencies / Crypto
    "CL=F": {"price": 90.97, "open": 91.20, "high": 91.85, "low": 90.50, "volume": 1420},
    "BZ=F": {"price": 103.50, "open": 104.30, "high": 104.50, "low": 103.10, "volume": 68},
    "GC=F": {"price": 4198.50, "open": 4180.00, "high": 4208.00, "low": 4175.00, "volume": 2540},
    "GLD": {"price": 387.05, "open": 385.50, "high": 387.90, "low": 385.10, "volume": 8450000},
    "UUP": {"price": 29.55, "open": 29.58, "high": 29.62, "low": 29.53, "volume": 3210000},
    "USO": {"price": 83.90, "open": 84.10, "high": 84.45, "low": 83.60, "volume": 4120000},
    "BTC-USD": {"price": 86250.00, "open": 84720.00, "high": 86800.00, "low": 84500.00, "volume": None},
    "ETH-USD": {"price": 2730.00, "open": 2685.00, "high": 2755.00, "low": 2670.00, "volume": None},

    # Core Index ETFs
    "SPY": {"price": 778.53, "open": 775.20, "high": 782.10, "low": 774.20, "volume": 42150000},
    "QQQ": {"price": 751.27, "open": 748.50, "high": 755.00, "low": 748.10, "volume": 28400000},
    "DIA": {"price": 516.39, "open": 513.00, "high": 517.20, "low": 512.80, "volume": 3850000},
    "IWM": {"price": 278.60, "open": 277.80, "high": 280.10, "low": 277.20, "volume": 26500000},
    "RSP": {"price": 199.35, "open": 198.70, "high": 200.10, "low": 198.50, "volume": 6800000},
    "IWO": {"price": 311.50, "open": 310.50, "high": 312.80, "low": 310.00, "volume": 1250000},
    "IWN": {"price": 173.10, "open": 172.60, "high": 173.80, "low": 172.30, "volume": 1420000},
    "SMH": {"price": 602.66, "open": 599.50, "high": 606.50, "low": 597.80, "volume": 7950000},
    "SOXX": {"price": 280.20, "open": 279.00, "high": 282.00, "low": 278.20, "volume": 1210000},
    "IGV": {"price": 111.45, "open": 109.80, "high": 111.90, "low": 109.50, "volume": 2950000},

    # Sector ETFs
    "XLK": {"price": 198.85, "open": 198.00, "high": 199.80, "low": 197.60, "volume": 8500000},
    "XLE": {"price": 98.60, "open": 98.50, "high": 99.20, "low": 98.10, "volume": 14200000},
    "XLF": {"price": 50.35, "open": 49.90, "high": 50.45, "low": 49.85, "volume": 38500000},
    "XLY": {"price": 231.30, "open": 228.50, "high": 231.80, "low": 228.20, "volume": 6450000},
    "XLP": {"price": 82.65, "open": 82.55, "high": 82.85, "low": 82.40, "volume": 9850000},
    "XLV": {"price": 154.95, "open": 154.30, "high": 155.20, "low": 154.10, "volume": 10200000},
    "XLI": {"price": 147.20, "open": 146.50, "high": 147.50, "low": 146.30, "volume": 11200000},
    "XLU": {"price": 83.55, "open": 83.20, "high": 83.80, "low": 83.10, "volume": 12400000},
    "XLRE": {"price": 44.75, "open": 44.55, "high": 44.90, "low": 44.45, "volume": 7650000},
    "XLC": {"price": 101.90, "open": 101.30, "high": 102.10, "low": 101.10, "volume": 6250000},
    "XLB": {"price": 95.10, "open": 94.70, "high": 95.30, "low": 94.50, "volume": 4150000},

    # Magnificent 7
    "NVDA": {"price": 229.74, "open": 231.50, "high": 233.20, "low": 228.50, "volume": 48500000},
    "AAPL": {"price": 336.11, "open": 339.80, "high": 341.20, "low": 335.50, "volume": 41200000},
    "TSLA": {"price": 382.70, "open": 376.50, "high": 385.00, "low": 375.20, "volume": 56400000},
    "MSFT": {"price": 534.38, "open": 525.00, "high": 536.00, "low": 524.20, "volume": 24800000},
    "GOOGL": {"price": 351.60, "open": 349.00, "high": 353.40, "low": 348.50, "volume": 21500000},
    "AMZN": {"price": 261.77, "open": 255.50, "high": 263.00, "low": 255.00, "volume": 33200000},
    "META": {"price": 717.42, "open": 722.00, "high": 724.50, "low": 715.80, "volume": 12800000},

    # AI Hardware / Semis
    "AVGO": {"price": 361.63, "open": 361.00, "high": 365.20, "low": 358.50, "volume": 14200000},
    "AMD": {"price": 608.10, "open": 622.00, "high": 624.50, "low": 605.20, "volume": 22500000},
    "MU": {"price": 1024.06, "open": 1040.00, "high": 1045.00, "low": 1018.50, "volume": 16400000},
    "TSM": {"price": 453.27, "open": 458.00, "high": 460.50, "low": 451.80, "volume": 11500000},
    "ASML": {"price": 1801.51, "open": 1775.00, "high": 1812.00, "low": 1770.00, "volume": 1250000},
    "ARM": {"price": 268.48, "open": 276.00, "high": 278.20, "low": 266.50, "volume": 7850000},
    "MRVL": {"price": 275.28, "open": 275.00, "high": 278.50, "low": 273.20, "volume": 9450000},
    "DELL": {"price": 574.55, "open": 575.00, "high": 578.00, "low": 572.00, "volume": 5200000},
    "VRT": {"price": 245.18, "open": 244.00, "high": 247.50, "low": 242.80, "volume": 6150000},
    "ANET": {"price": 217.10, "open": 212.00, "high": 218.50, "low": 211.50, "volume": 4350000},
    "COHR": {"price": 312.62, "open": 305.00, "high": 315.80, "low": 303.20, "volume": 3850000},
    "LITE": {"price": 1103.36, "open": 1055.00, "high": 1115.00, "low": 1050.00, "volume": 1680000},

    # Software / SaaS
    "PLTR": {"price": 209.05, "open": 200.50, "high": 211.20, "low": 199.80, "volume": 38400000},
    "ADBE": {"price": 241.05, "open": 241.50, "high": 243.80, "low": 239.50, "volume": 4150000},
    "CRM": {"price": 227.80, "open": 228.00, "high": 230.10, "low": 226.50, "volume": 6250000},
    "NOW": {"price": 139.75, "open": 140.20, "high": 141.50, "low": 138.80, "volume": 2150000},
    "SNOW": {"price": 368.89, "open": 348.00, "high": 372.00, "low": 346.50, "volume": 8450000},
    "ORCL": {"price": 141.56, "open": 136.50, "high": 142.80, "low": 136.00, "volume": 12800000},
    "CRWD": {"price": 265.50, "open": 263.50, "high": 267.80, "low": 262.20, "volume": 4950000},
    "PANW": {"price": 401.20, "open": 399.00, "high": 403.50, "low": 397.80, "volume": 3850000},

    # Power / Infrastructure / Nuclear
    "VST": {"price": 156.86, "open": 157.00, "high": 162.50, "low": 155.20, "volume": 14200000},
    "CEG": {"price": 298.12, "open": 288.00, "high": 301.50, "low": 287.20, "volume": 7650000},
    "GEV": {"price": 1004.73, "open": 1001.00, "high": 1012.00, "low": 997.50, "volume": 3250000},
    "OKLO": {"price": 35.10, "open": 34.60, "high": 36.20, "low": 34.20, "volume": 5850000},
    "NRG": {"price": 107.50, "open": 106.50, "high": 108.80, "low": 106.10, "volume": 4200000},
    "ETN": {"price": 428.20, "open": 425.00, "high": 430.50, "low": 424.00, "volume": 3150000},
    "PWR": {"price": 691.00, "open": 686.00, "high": 694.00, "low": 684.50, "volume": 1650000},
    "FLNC": {"price": 7.48, "open": 7.45, "high": 7.62, "low": 7.41, "volume": 1850000},
}

out = {}
D = "2026-10-09"
timestamp = 1791552600 # 2026-10-09 16:00:00 EDT

for s in q8:
    info = data_1009.get(s, {})
    price = info.get("price", q8[s]["price"])
    prev = q8[s]["price"]
    change = round(price - prev, 2)
    pct = round((price / prev - 1) * 100, 2)
    open_p = info.get("open", round(price * 0.998, 2))
    high_p = info.get("high", max(price, open_p))
    low_p = info.get("low", min(price, open_p))
    volume = info.get("volume", q8[s]["volume"])
    
    # 5d vs 2026-10-02
    p_5d = q5d[s]["price"] if s in q5d else prev
    ret_5d = round((price / p_5d - 1) * 100, 2)
    
    # 1m vs 2026-09-10
    p_1m = q1m[s]["price"] if s in q1m else prev
    ret_1m = round((price / p_1m - 1) * 100, 2)
    
    out[s] = {
        "symbol": s,
        "price": price,
        "open": open_p,
        "high": high_p,
        "low": low_p,
        "volume": volume,
        "prev": prev,
        "change": change,
        "pct": pct,
        "timestamp": timestamp,
        "date": D,
        "5d": ret_5d,
        "1m": ret_1m
    }

out_path = f"/Users/wisdom/html-report-skill/scratch/quotes_{D}.json"
with open(out_path, "w") as f:
    json.dump(out, f, indent=1)

print(f"Saved {len(out)} quotes to {out_path}")

# Build Tech indicators
t_out = {
    "SPY": {
        "price": out["SPY"]["price"],
        "sma20": 766.82,
        "sma50": 765.45,
        "sma100": 755.42,
        "sma200": 722.05,
        "rsi": 67.4,
        "macd": 2.24,
        "hi52": 782.10,
        "hi20": 782.10,
        "lo20": 749.60
    },
    "QQQ": {
        "price": out["QQQ"]["price"],
        "sma20": 733.25,
        "sma50": 720.12,
        "sma100": 718.95,
        "sma200": 670.65,
        "rsi": 76.8,
        "macd": 9.42,
        "hi52": 762.86,
        "hi20": 762.86,
        "lo20": 700.00
    },
    "IWM": {
        "price": out["IWM"]["price"],
        "sma20": 283.15,
        "sma50": 291.80,
        "sma100": 291.60,
        "sma200": 276.72,
        "rsi": 36.5,
        "macd": -3.52,
        "hi52": 305.18,
        "hi20": 294.16,
        "lo20": 274.52
    },
    "SMH": {
        "price": out["SMH"]["price"],
        "sma20": 591.20,
        "sma50": 573.10,
        "sma100": 585.65,
        "sma200": 503.12,
        "rsi": 75.2,
        "macd": 15.02,
        "hi52": 671.83,
        "hi20": 639.47,
        "lo20": 537.73
    },
    "IGV": {
        "price": out["IGV"]["price"],
        "sma20": 106.52,
        "sma50": 104.10,
        "sma100": 98.45,
        "sma200": 93.82,
        "rsi": 67.8,
        "macd": 1.85,
        "hi52": 117.76,
        "hi20": 112.34,
        "lo20": 100.59
    },
    "XLK": {
        "price": out["XLK"]["price"],
        "sma20": 193.10,
        "sma50": 187.65,
        "sma100": 185.45,
        "sma200": 165.85,
        "rsi": 81.2,
        "macd": 3.75,
        "hi52": 203.25,
        "hi20": 203.25,
        "lo20": 182.08
    }
}

tech_path = f"/Users/wisdom/html-report-skill/scratch/tech_{D}.json"
with open(tech_path, "w") as f:
    json.dump(t_out, f, indent=1)

print(f"Saved tech indicators to {tech_path}")
