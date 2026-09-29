import json

target_date = "2026-09-28"

# Market data grounded on Monday 2026-09-28 close:
# - 10Y Treasury yield (^TNX) spiked to 5.240% (+27.2 bps from Friday's 4.968%/5.070%), reaching fresh highs and driving valuation compression.
# - Market enters Q3 quarter-end rebalancing week following last week's historic all-time highs (S&P 500 crossed 7,800, Nasdaq 27,439, SOX 12,579).
# - S&P 500 falls -0.77% (-59.72 pts) to 7,683.69 (SPY $765.61 -0.74%).
# - Dow Jones retreats -0.67% (-348 pts or -567 pts) to 51,481.51 (DIA $514.02 -0.67%).
# - Nasdaq Composite sheds -0.92% (-248.34 pts) to 26,820.38 (QQQ $736.53 -1.07%).
# - SOX Semiconductor falls -1.61% (-203.69 pts) to 12,465.24 (SOXX $560.79 -2.08%, SMH $600.01 -1.08%).
# - Russell 2000 sheds -0.69% to 2,817.91 (IWM $280.02 -0.69%).
# - VIX spikes +8.07% to 16.07.
# - Gold (GC=F) drops -3.81% to $4,156.60/oz amid higher yields and dollar strength.
# - WTI Crude (CL=F) edges up to $93.24/bbl (+0.90%), Brent at $98.67.
# - Dollar Index (DXY) rises to 101.19 (+0.22%).
# - Nvidia (NVDA) stands tall as market anchor, rising +1.68% (+$3.79 to $228.86)!
# - TSMC (TSM +0.50% to $452.88) and ASML (+1.58% to $1,771.41) buck the trend.
# - Cybersecurity names surge: Palo Alto Networks (PANW +4.63% to $392.09), CrowdStrike (CRWD +2.82% to $259.25).
# - Profit taking in high-multiple leaders: Meta (META -4.79% to $715.62), Tesla (TSLA -3.94% to $357.45), AMD (AMD -3.61% to $607.87), Dell (DELL -3.46% to $543.43).
# - Defensive sectors outperform: Healthcare (XLV +0.33%), Consumer Staples (XLP +0.27%), Energy (XLE +0.10%).

with open(f"/Users/wisdom/html-report-skill/scratch/quotes_{target_date}.json", "r", encoding="utf-8") as f:
    quotes = json.load(f)

print(f"Verified quotes_{target_date}.json with {len(quotes)} items.")
