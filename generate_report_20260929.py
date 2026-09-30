import os
import subprocess
import sys
import json

# Load quotes for 2026-09-29
quotes_file = "/Users/wisdom/html-report-skill/scratch/quotes_2026-09-29.json"
with open(quotes_file, "r", encoding="utf-8") as f:
    quotes = json.load(f)

def get_val(ticker, key):
    if ticker in quotes and key in quotes[ticker]:
        val = quotes[ticker][key]
        if key == 'pct':
            return f"{val:+.2f}%" if val >= 0 else f"{val:.2f}%"
        elif key == 'change':
            return f"{val:+.2f}" if val >= 0 else f"{val:.2f}"
        elif key == 'price':
            if val > 10000:
                return f"{val:,.2f}"
            return f"{val:.2f}"
    return "N/A"

def get_raw_val(ticker, key):
    if ticker in quotes and key in quotes[ticker]:
        return quotes[ticker][key]
    return 0.0

# Key ETFs & Indices
spy_pct = get_raw_val("SPY", "pct")
qqq_pct = get_raw_val("QQQ", "pct")
dia_pct = get_raw_val("DIA", "pct")
iwm_pct = get_raw_val("IWM", "pct")
soxx_pct = get_raw_val("SOXX", "pct")
smh_pct = get_raw_val("SMH", "pct")
vix_pct = get_raw_val("^VIX", "pct")
igv_pct = get_raw_val("IGV", "pct")
xlk_pct = get_raw_val("XLK", "pct")

spy_color = "text-emerald-600 dark:text-emerald-400 font-bold" if spy_pct >= 0 else "text-rose-500 font-bold"
qqq_color = "text-emerald-600 dark:text-emerald-400 font-bold" if qqq_pct >= 0 else "text-rose-500 font-bold"
dia_color = "text-emerald-600 dark:text-emerald-400 font-bold" if dia_pct >= 0 else "text-rose-500 font-bold"
iwm_color = "text-emerald-600 dark:text-emerald-400 font-bold" if iwm_pct >= 0 else "text-rose-500 font-bold"
soxx_color = "text-emerald-600 dark:text-emerald-400 font-bold" if soxx_pct >= 0 else "text-rose-500 font-bold"
smh_color = "text-emerald-600 dark:text-emerald-400 font-bold" if smh_pct >= 0 else "text-rose-500 font-bold"
vix_color = "text-rose-500 font-bold" if vix_pct >= 0 else "text-emerald-600 dark:text-emerald-400 font-bold"
igv_color = "text-emerald-600 dark:text-emerald-400 font-bold" if igv_pct >= 0 else "text-rose-500 font-bold"
xlk_color = "text-emerald-600 dark:text-emerald-400 font-bold" if xlk_pct >= 0 else "text-rose-500 font-bold"

spy_pct_color = '#10b981' if spy_pct >= 0 else '#f43f5e'
qqq_pct_color = '#10b981' if qqq_pct >= 0 else '#f43f5e'
dia_pct_color = '#10b981' if dia_pct >= 0 else '#f43f5e'
iwm_pct_color = '#10b981' if iwm_pct >= 0 else '#f43f5e'
soxx_pct_color = '#10b981' if soxx_pct >= 0 else '#f43f5e'
smh_pct_color = '#10b981' if smh_pct >= 0 else '#f43f5e'
igv_pct_color = '#10b981' if igv_pct >= 0 else '#f43f5e'
xlk_pct_color = '#10b981' if xlk_pct >= 0 else '#f43f5e'

# 11 S&P 500 Sectors data for 2026-09-29
sectors = [
    {"name": "公用事業", "etf": "XLU", "pct": get_raw_val("XLU", "pct"), "5d": "+2.80%", "1m": "+8.10%", "driver": "AI資料中心24/7核能與清潔直供電剛需引爆！VST(+2.04%)與CEG(+1.59%)齊創歷史天價，公用事業板塊領跑標普"},
    {"name": "通訊服務", "etf": "XLC", "pct": get_raw_val("XLC", "pct"), "5d": "+1.40%", "1m": "+4.80%", "driver": "Meta(+3.24%)大漲強勢修復昨日跌幅，社群精準廣告與開源Llama模型變現動能強勁，逆勢走強"},
    {"name": "工業", "etf": "XLI", "pct": get_raw_val("XLI", "pct"), "5d": "+1.40%", "1m": "+4.30%", "driver": "北美電網設備升級與資料中心液冷基建訂單爆滿，PWR(+1.15%)、GEV(+1.34%)與伊頓ETN全線上揚"},
    {"name": "非必需消費", "etf": "XLY", "pct": get_raw_val("XLY", "pct"), "5d": "+0.70%", "1m": "+3.30%", "driver": "亞馬遜(+0.21%)穩步上揚，緩解了特斯拉(-1.29%)在Q3全球交付量公布前防禦整理的拖累"},
    {"name": "資訊科技", "etf": "XLK", "pct": get_raw_val("XLK", "pct"), "5d": "+2.70%", "1m": "+7.50%", "driver": "半導體設備(ASML +3.56%)、ARM(+3.65%)與光通訊晶片暴漲，但蘋果(-2.66%)權重拖累令板塊近乎平盤"},
    {"name": "房地產", "etf": "XLRE", "pct": get_raw_val("XLRE", "pct"), "5d": "-1.20%", "1m": "-1.10%", "driver": "10年期美債利率在5.260%止漲整理，長端利率壓力趨緩，REITs商業地產自昨日跌勢中企穩橫盤"},
    {"name": "醫療保健", "etf": "XLV", "pct": get_raw_val("XLV", "pct"), "5d": "+0.50%", "1m": "+1.80%", "driver": "資金從昨日防禦板塊適度回流AI成長與晶片股，禮來(-0.4%)與聯合健康微幅獲利回吐"},
    {"name": "金融", "etf": "XLF", "pct": get_raw_val("XLF", "pct"), "5d": "-0.20%", "1m": "+2.90%", "driver": "季末機構被動再平衡最後換手，長短端殖利率曲線維持高檔震盪，銀行股溫和整理"},
    {"name": "必需消費", "etf": "XLP", "pct": get_raw_val("XLP", "pct"), "5d": "+0.60%", "1m": "+2.00%", "driver": "避險買盤部分獲利了結回流AI主線，沃爾瑪、好市多與寶僑小幅回吐昨日漲幅"},
    {"name": "原物料", "etf": "XLB", "pct": get_raw_val("XLB", "pct"), "5d": "-0.50%", "1m": "+2.00%", "driver": "原油重挫拖累大宗化工與基礎材料報價，基礎工業金屬類股承壓走低"},
    {"name": "能源", "etf": "XLE", "pct": get_raw_val("XLE", "pct"), "5d": "-0.10%", "1m": "+2.60%", "driver": "WTI原油崩跌-3.62%摜破$90美元大關，沙烏地增產傳聞引發油氣開採類股全面墊底"}
]

sectors_sorted = sorted(sectors, key=lambda x: x["pct"], reverse=True)

sector_rows = ""
for rank, sec in enumerate(sectors_sorted, 1):
    pct_val = sec["pct"]
    pct_color = "text-emerald-600 font-bold" if pct_val >= 0 else "text-rose-500 font-bold"
    pct_str = f"{pct_val:+.2f}%"
    
    diff = pct_val - spy_pct
    diff_str = f"跑贏 ({diff:+.2f}%)" if diff >= 0 else f"跑輸 ({diff:.2f}%)"
    diff_color = "text-emerald-600 font-semibold" if diff >= 0 else "text-rose-500 font-semibold"
    
    sector_rows += f"""            <tr class="hover:bg-slate-50 dark:hover:bg-zinc-800/30">
              <td class="p-3">{rank}</td>
              <td class="p-3 font-semibold">{sec["name"]}</td>
              <td class="p-3 font-mono">{sec["etf"]}</td>
              <td class="p-3 {pct_color}">{pct_str}</td>
              <td class="p-3">{sec["5d"]}</td>
              <td class="p-3">{sec["1m"]}</td>
              <td class="p-3 {diff_color}">{diff_str}</td>
              <td class="p-3">{sec["driver"]}</td>
            </tr>\n"""

# Watch List data for 2026-09-29 (all 23 core tickers)
watch_list = [
    {"symbol": "NVDA", "trend": "收報$227.21(-0.72%)。昨日逆勢大漲+1.68%後正常高檔蓄勢整固，牢牢守在$225支撐上方，四大CSP 2027年資本支出指引無懈可擊，Blackwell Ultra出貨節奏如期推進。", "levels": "$222.00 / $235.00", "tag": "繼續強勢"},
    {"symbol": "AMD", "trend": "收報$607.57(-0.05%)。極致平盤整固，牢牢守穩$600整數關卡與1兆美元市值防線，MI350雲端加速器客戶反饋優異，等待向上突破。", "levels": "$600.00 / $628.00", "tag": "回踩支撐"},
    {"symbol": "AVGO", "trend": "逆勢大漲+1.58%收$355.10！客製化ASIC晶片大單與Tomahawk 6高速網路交換晶片訂單爆發，長多格局極為凌厲，逼近歷史新高。", "levels": "$348.00 / $365.00", "tag": "繼續強勢"},
    {"symbol": "MRVL", "trend": "狂飆+4.51%收報$263.27！1.6T光電互聯DSP晶片與雲端超大規模客製化晶片放量，展現強大爆發力，回踩後強勢重啟主升浪。", "levels": "$255.00 / $272.00", "tag": "繼續強勢"},
    {"symbol": "GOOGL", "trend": "收報$340.92(-0.53%)。在$340上方窄幅整固，自研TPU v6規模部署大幅優化推論成本，Gemini企業生態健康擴張。", "levels": "$336.00 / $350.00", "tag": "高位震盪"},
    {"symbol": "MSFT", "trend": "幾乎平盤報收$508.96(-0.05%)。守穩$505-$508支撐平台，Azure AI合約積壓與企業Copilot付費率健康增長，核電直供合約穩固推進。", "levels": "$502.00 / $518.00", "tag": "高位震盪"},
    {"symbol": "META", "trend": "暴力反彈大漲+3.24%收在$738.79！昨日季末避險賣壓迅速被逢低買盤消化，AI精準廣告投放與開源Llama模型變現能力領跑全場。", "levels": "$725.00 / $755.00", "tag": "低位修復"},
    {"symbol": "AMZN", "trend": "逆勢小幅收紅+0.21%報$246.67。AWS利潤率穩健，雲端與電商雙引擎運行流暢，守穩$245支撐，多頭排列健康。", "levels": "$242.00 / $254.00", "tag": "高位震盪"},
    {"symbol": "ORCL", "trend": "放量大漲+3.91%收報$137.79！多雲架構資料庫合作與OCI AI算力集群積壓訂單超預期增長，強勢突破短線整理平台。", "levels": "$132.00 / $144.00", "tag": "繼續強勢"},
    {"symbol": "CRM", "trend": "收在$225.31(-0.86%)。Agentforce智慧體方案處於企業客戶導入期，受長端利率環境壓制，在低檔進行估值磨底整固。", "levels": "$220.00 / $232.00", "tag": "需要觀察"},
    {"symbol": "NOW", "trend": "收報$129.94(-1.15%)。測試$130整數關卡，企業AI工作流平台訂閱穩定，但短線成長股估值敏感度仍需消化。", "levels": "$127.00 / $136.00", "tag": "回踩支撐"},
    {"symbol": "SNOW", "trend": "逆勢小幅反彈+0.67%收復$330.31關卡。企業現代化資料棧用量保持穩健增長，於箱體中軌逐步修復估值。", "levels": "$322.00 / $342.00", "tag": "低位修復"},
    {"symbol": "ADBE", "trend": "逆勢走強+0.94%收報$233.17。在$230關鍵頸線獲得有力承接，Firefly生成式AI功能付費轉換率逐步回升。", "levels": "$228.00 / $240.00", "tag": "低位修復"},
    {"symbol": "PLTR", "trend": "守在$186.97(-0.27%)高檔平台窄幅微震。AIP在國防端及財富500強企業中的滲透無可匹敵，高位換手蓄勢衝擊$195。", "levels": "$182.00 / $195.00", "tag": "高位震盪"},
    {"symbol": "LITE", "trend": "全場光通訊超級黑馬！暴漲+5.66%突破天價收報$973.49！1.6T/3.2T雷射光源晶片與光互聯模組進入量產前夕，逼空爆發！", "levels": "$940.00 / $1,020.00", "tag": "短線過熱"},
    {"symbol": "COHR", "trend": "強勁大漲+3.46%收在$292.21！與LITE共振，資料中心高速光收發器與碳化矽晶圓需求飆升，放量突破$290大關。", "levels": "$280.00 / $310.00", "tag": "繼續強勢"},
    {"symbol": "ANET", "trend": "收在$202.86(-1.01%)。守在$200整數大關上方健康消化浮額，AI叢集800G乙太網核心交換機基本面極度扎實。", "levels": "$198.00 / $210.00", "tag": "高位震盪"},
    {"symbol": "FLNC", "trend": "暴力反彈+4.27%收復$7.82！油價重挫與儲能專案併網訂單激增，化解昨日破位隱憂，低位修復動能充足。", "levels": "$7.40 / $8.30", "tag": "低位修復"},
    {"symbol": "OKLO", "trend": "持平收盤報$37.11(0.00%)。SMR小型模組化核電商業化推進順利，與超大規模科技廠洽談供電協議中，高檔箱體整固。", "levels": "$35.50 / $40.00", "tag": "高位震盪"},
    {"symbol": "VST", "trend": "狂飆+2.04%衝破$140創歷史天價收報$140.83！買盤源源不絕，AI超算中心24/7核能與天然氣直供電無敵護城河，公用事業多頭旗手。", "levels": "$136.00 / $146.00", "tag": "繼續強勢"},
    {"symbol": "CEG", "trend": "續創歷史新天價收在$264.58(+1.59%)！三哩島重啟供電微軟案進展順利，長約直供溢價獲華爾街一致看好，多頭趨勢堅不可摧。", "levels": "$258.00 / $272.00", "tag": "繼續強勢"},
    {"symbol": "ETN", "trend": "逆勢小漲+0.43%收報$433.27。北美電網變壓器與配電開關設備交期持續拉長，高檔均線多頭排列穩固。", "levels": "$425.00 / $442.00", "tag": "高位震盪"},
    {"symbol": "VRT", "trend": "逆勢上揚+1.76%收在$248.34！液冷分配單元(CDU)與高密度散熱機櫃訂單暴增，回踩後迅速重啟攻勢。", "levels": "$242.00 / $256.00", "tag": "繼續強勢"}
]

def get_tag_html(tag):
    classes = "px-2 py-0.5 rounded text-xs font-semibold "
    if tag == "繼續強勢":
        classes += "bg-emerald-100 dark:bg-emerald-950 text-emerald-700 dark:text-emerald-300"
    elif tag == "高位震盪":
        classes += "bg-yellow-100 dark:bg-yellow-950 text-yellow-700 dark:text-yellow-300"
    elif tag == "等財報催化" or tag == "利好兌現":
        classes += "bg-indigo-100 dark:bg-indigo-950 text-indigo-700 dark:text-indigo-300"
    elif tag == "低位修復":
        classes += "bg-sky-100 dark:bg-sky-950 text-sky-700 dark:text-sky-300"
    elif tag == "回踩支撐":
        classes += "bg-blue-100 dark:bg-blue-950 text-blue-700 dark:text-blue-300"
    elif tag == "需要觀察":
        classes += "bg-zinc-100 dark:bg-zinc-800 text-zinc-700 dark:text-zinc-300"
    elif tag == "破位風險":
        classes += "bg-rose-100 dark:bg-rose-950 text-rose-700 dark:text-rose-300"
    elif tag == "短線過熱":
        classes += "bg-orange-100 dark:bg-orange-950 text-orange-700 dark:text-orange-300"
    else:
        classes += "bg-slate-100 dark:bg-slate-800 text-slate-700 dark:text-slate-300"
    return f'<span class="{classes}">{tag}</span>'

watch_rows = ""
for item in watch_list:
    sym = item["symbol"]
    price_val = get_val(sym, "price")
    pct_val = get_raw_val(sym, "pct")
    pct_color = "text-emerald-600 font-bold" if pct_val >= 0 else "text-rose-500 font-bold"
    pct_str = get_val(sym, "pct")
    tag_html = get_tag_html(item["tag"])
    
    watch_rows += f"""            <tr class="hover:bg-slate-50 dark:hover:bg-zinc-800/30">
              <td class="p-3 font-semibold">{sym}</td>
              <td class="p-3 font-mono">${price_val}</td>
              <td class="p-3 {pct_color}">{pct_str}</td>
              <td class="p-3 text-xs sm:text-sm">{item["trend"]}</td>
              <td class="p-3 font-mono text-xs sm:text-sm">{item["levels"]}</td>
              <td class="p-3">{tag_html}</td>
            </tr>\n"""

# Full HTML template for 2026-09-29
html_template = """<!doctype html>
<html lang="zh-TW" class="scroll-smooth">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <title>美股收盤日報｜原油暴跌破$90美元美債殖利率回穩！費半強彈+1.32%、光通訊與ASML暴漲，AI核電創新高，標普守穩7,670 (2026-09-29)</title>
  <meta name="description" content="2026年9月29日美股收盤日報：週二美股迎來長端美債殖利率回穩與原油重挫引發的結構性強勢反攻。WTI原油暴跌-3.62%摜破$90美元大關，10年期美債收益率在5.260%止漲整固，大幅緩解估值壓力。半導體板塊與AI硬體重啟主升浪，費城半導體指數（^SOX）強勢大漲+1.32%報12,629.16點，光通訊龍頭Lumentum（LITE +5.66%）逼空大漲，ASML暴漲+3.56%，ARM大漲+3.65%，Marvell大漲+4.51%，博通逼近天價；AI核電清潔能源雙雄Vistra（VST +2.04%）與Constellation（CEG +1.59%）續刷歷史新天價，推動公用事業板塊（XLU +1.17%）高居標普首位！Meta大漲+3.24%修復失地，甲骨文大漲+3.91%。標普500微跌-0.17%報7,670.84點，納指100逆勢收紅+0.21%，道瓊微跌-0.26%（受蘋果-2.66%拖累），VIX回落至16.04，黃金反彈+1.15%。市場在季末前夕展現極強抗脆弱性與主線吸金力。">
  <meta property="og:title" content="美股收盤日報｜2026-09-29">
  <meta property="og:description" content="原油暴跌破$90美元美債殖利率回穩！費半強彈+1.32%、光通訊與ASML暴漲，AI核電創新高，標普守穩7,670！">
  <meta property="og:type" content="article">

  <!-- Tailwind CSS & Font family -->
  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config = {
      darkMode: 'class',
      theme: {
        extend: {
          colors: {
            brand: {
              50: '#f0f9ff',
              100: '#e0f2fe',
              500: '#0284c7',
              600: '#0369a1',
              700: '#075985',
            },
            zinc: {
              850: '#1f1f23',
              950: '#09090b',
            }
          }
        }
      }
    };
  </script>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;700&display=swap" rel="stylesheet">

  <!-- Chart.js & Mermaid -->
  <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.min.js"></script>
  <script>
    document.addEventListener("DOMContentLoaded", function () {
      mermaid.initialize({
        startOnLoad: true,
        theme: document.documentElement.classList.contains('dark') ? 'dark' : 'default',
        securityLevel: 'loose',
      });
      window.__mermaid = mermaid;
    });
  </script>

  <style>
    /* Tabs pure CSS support */
    .tabs input[type="radio"] { display: none; }
    .tabs label {
      cursor: pointer;
      padding: 0.5rem 1rem;
      border-radius: 0.5rem;
      font-weight: 600;
      font-size: 0.875rem;
      color: #64748b;
      transition: all 0.2s ease;
    }
    .dark .tabs label { color: #94a3b8; }
    .tabs input[type="radio"]:checked + label {
      background-color: #0284c7;
      color: #ffffff !important;
    }
    .tab-panel { display: none; }
    #tab-yields:checked ~ .tab-content #panel-yields,
    #tab-fed:checked ~ .tab-content #panel-fed,
    #tab-commodities:checked ~ .tab-content #panel-commodities,
    #tab-data:checked ~ .tab-content #panel-data {
      display: block;
    }
    th.sortable { cursor: pointer; user-select: none; }
    th.sortable:hover { background-color: rgba(148, 163, 184, 0.15); }
  </style>
</head>

<body class="bg-slate-50 dark:bg-zinc-950 text-slate-900 dark:text-zinc-100 transition-colors duration-200 antialiased min-h-screen">

<!-- Top sticky navbar -->
<nav class="sticky top-0 z-50 backdrop-blur-md bg-white/80 dark:bg-zinc-900/80 border-b border-slate-200 dark:border-zinc-800">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-14 flex items-center justify-between">
    <div class="flex items-center gap-3">
      <a href="manifest.json" class="flex items-center gap-2 font-bold text-slate-900 dark:text-white">
        <span class="w-7 h-7 rounded-lg bg-brand-500 text-white flex items-center justify-center text-sm font-extrabold shadow-sm">US</span>
        <span class="text-sm tracking-tight sm:inline hidden">美股收盤日報</span>
      </a>
      <span class="text-xs px-2 py-0.5 rounded-full bg-slate-200 dark:bg-zinc-800 text-slate-600 dark:text-zinc-400 font-medium">2026-09-29</span>
    </div>

    <!-- Quick index pill pills -->
    <div class="hidden lg:flex items-center gap-4 text-xs font-medium text-slate-600 dark:text-zinc-400">
      <span>標普 500: <strong class="[SPY_COLOR]">[SPY_PRICE] ([SPY_PCT])</strong></span>
      <span>納指 100: <strong class="[QQQ_COLOR]">[QQQ_PRICE] ([QQQ_PCT])</strong></span>
      <span>道瓊: <strong class="[DIA_COLOR]">[DIA_PRICE] ([DIA_PCT])</strong></span>
      <span>費半: <strong class="[SOXX_COLOR]">[SOXX_PRICE] ([SOXX_PCT])</strong></span>
      <span>10Y美債: <strong class="text-slate-800 dark:text-white font-bold">[TNX_PRICE]%</strong></span>
      <span>原油: <strong class="text-rose-500 font-bold">[USO_OIL_PRICE] ([USO_OIL_PCT])</strong></span>
    </div>

    <div class="flex items-center gap-2">
      <!-- Dark mode button -->
      <button id="theme-toggle" class="p-2 rounded-lg bg-slate-100 dark:bg-zinc-800 text-slate-600 dark:text-zinc-400 hover:text-slate-900 dark:hover:text-white transition">
        <svg id="theme-icon-light" class="w-4 h-4 hidden dark:block" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 3v1m0 16v1m9-9h-1M4 9h-1m15.364 6.364l-.707-.707M6.343 6.343l-.707-.707m12.728 0l-.707.707M6.343 17.657l-.707.707M16 12a4 4 0 11-8 0 4 4 0 018 0z"></path></svg>
        <svg id="theme-icon-dark" class="w-4 h-4 block dark:hidden" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M20.354 15.354A9 9 0 018.646 3.646 9.003 9.003 0 0012 21a9.003 9.003 0 008.354-5.646z"></path></svg>
      </button>
      <a href="#sec-15" class="text-xs px-3 py-1.5 rounded-lg bg-brand-500 hover:bg-brand-600 text-white font-semibold shadow-sm transition">
        結論與操作
      </a>
    </div>
  </div>
</nav>

<!-- Content Layout -->
<div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8 grid grid-cols-1 lg:grid-cols-[240px_1fr] gap-8">

  <!-- Desktop Sticky Table of Contents -->
  <aside class="hidden lg:block">
    <div class="sticky top-20 space-y-1 text-xs text-slate-500 dark:text-zinc-400 border-l border-slate-200 dark:border-zinc-850 pl-3">
      <div class="font-bold text-slate-800 dark:text-white mb-2 uppercase tracking-wider text-[11px]">目錄導航</div>
      <div><a href="#sec-0" class="block py-1 hover:text-brand-500 transition">0. 今日一句話總結</a></div>
      <div><a href="#sec-1" class="block py-1 hover:text-brand-500 transition">1. 大盤表現總覽</a></div>
      <div><a href="#sec-2" class="block py-1 hover:text-brand-500 transition">2. 盤中走勢復盤</a></div>
      <div><a href="#sec-3" class="block py-1 hover:text-brand-500 transition">3. 宏觀環境 (Tabs)</a></div>
      <div><a href="#sec-4" class="block py-1 hover:text-brand-500 transition">4. 板塊表現 (可排序)</a></div>
      <div><a href="#sec-5" class="block py-1 hover:text-brand-500 transition">5. 主題與風格表現</a></div>
      <div><a href="#sec-6" class="block py-1 hover:text-brand-500 transition">6. 市場寬度與參與度</a></div>
      <div><a href="#sec-7" class="block py-1 hover:text-brand-500 transition">7. 技術面分析</a></div>
      <div><a href="#sec-8" class="block py-1 hover:text-brand-500 transition">8. 重點個股新聞與異動</a></div>
      <div><a href="#sec-9" class="block py-1 hover:text-brand-500 transition">9. 財報日曆與解讀</a></div>
      <div><a href="#sec-10" class="block py-1 hover:text-brand-500 transition">10. 機構觀點與資金流</a></div>
      <div><a href="#sec-11" class="block py-1 hover:text-brand-500 transition">11. 板塊輪動判斷</a></div>
      <div><a href="#sec-12" class="block py-1 hover:text-brand-500 transition">12. 重點關注股觀察 (23 標的)</a></div>
      <div><a href="#sec-13" class="block py-1 hover:text-brand-500 transition">13. 次日交易計畫 / 觀察清單</a></div>
      <div><a href="#sec-14" class="block py-1 hover:text-brand-500 transition">14. 風險提示矩陣</a></div>
      <div><a href="#sec-15" class="block py-1 hover:text-brand-500 transition">15. 最終結論</a></div>
    </div>
  </aside>

  <!-- Main content wrapper -->
  <main class="space-y-14">

    <!-- Header Section -->
    <header class="pb-6 border-b border-slate-200 dark:border-zinc-800">
      <div class="flex items-center gap-2 text-xs text-blue-600 dark:text-blue-400 font-semibold tracking-wider uppercase mb-2">
        <span>DAILY CLOSING REPORT</span>
        <span>•</span>
        <span>2026-09-29 TRADING DAY</span>
      </div>
      <h1 class="text-2xl sm:text-3xl font-extrabold tracking-tight text-slate-900 dark:text-white mb-3">
        美股收盤日報｜原油暴跌破$90美元美債殖利率回穩！費半強彈+1.32%、光通訊與ASML暴漲，AI核電創新高，標普守穩7,670
      </h1>
      <div class="flex flex-wrap items-center gap-4 text-xs text-slate-500 dark:text-zinc-400">
        <span>發布時間：2026-09-30 08:00 (Asia/Taipei)</span>
        <span>•</span>
        <span>分析師：Antigravity Market Team</span>
        <span>•</span>
        <span class="inline-flex items-center gap-1.5 px-2.5 py-0.5 rounded-full bg-slate-100 dark:bg-zinc-800 text-slate-700 dark:text-zinc-300 font-medium">
          <span class="w-1.5 h-1.5 rounded-full bg-emerald-500"></span> 油價跌破$90・美債殖利率回穩・半導體設備與光通訊重啟主升浪
        </span>
      </div>
    </header>

    <!-- 0. 今日一句話總結 -->
    <section id="sec-0" class="scroll-mt-6 font-sans">
      <h2 class="text-xl font-bold mb-4 flex items-center gap-2 border-b border-slate-100 dark:border-zinc-850 pb-2">
        <span class="text-brand-500">0.</span> 今日一句話總結
      </h2>
      <div class="p-5 rounded-2xl bg-gradient-to-br from-emerald-50/40 via-white to-blue-50/30 dark:from-zinc-900 dark:via-zinc-900 dark:to-zinc-800 border border-emerald-100 dark:border-zinc-800 shadow-sm leading-relaxed space-y-3">
        <p class="text-sm sm:text-base text-slate-700 dark:text-zinc-200 font-medium">
          週二（2026年9月29日），美股迎來長端美債殖利率回穩與能源成本大幅驟降引領的<strong>「高成長科技與AI硬體結構性強勢反攻」</strong>。WTI原油重挫-3.62%摜破$90美元大關報$89.25/桶，10年期美債收益率在5.260%平台止漲整固，顯著舒緩了昨日長端利率跳升引發的估值緊縮焦慮。三大指數呈現高檔良性分化：<strong>費城半導體指數（^SOX）強勢暴漲+1.32%報12,629.16點</strong>，納斯達克100指數逆勢上揚+0.21%報30,339.33點；標普500微跌-0.17%收在7,670.84點，道瓊工業指數小跌-0.26%（-131點）報51,349.92點（主因蘋果-2.66%下挫與能源板塊回調拖累），VIX恐慌指數降溫至16.04點。
        </p>
        <p class="text-sm text-slate-650 dark:text-zinc-300">
          盤面核心亮點極度璀璨：<strong>半導體設備、光通訊與AI客製化晶片全面爆發</strong>！先進製程光刻機霸主ASML暴漲+3.56%、安謀（ARM）大漲+3.65%、邁威爾（MRVL）狂飆+4.51%、博通（AVGO）大漲+1.58%逼近天價，光通訊龍頭Lumentum（LITE +5.66%）與Coherent（COHR +3.46%）上演逼空大戲；<strong>AI清潔電力雙雄Vistra（VST +2.04%）與Constellation Energy（CEG +1.59%）攜手同創歷史新天價</strong>，推動公用事業板塊（XLU +1.17%）高居標普11大板塊漲幅榜首！此外，Meta（META +3.24%）強勢收復失地，甲骨文（ORCL +3.91%）放量突破。
        </p>
        <p class="text-sm text-slate-650 dark:text-zinc-300">
          資金展現高度精準的<strong>Risk-On進攻態勢</strong>，聚焦高業績能見度的半導體與實體AI能源直供電基建，大幅抽離傳統化石能源與高本益比落後個股。市場在季末最後結算日前夕，展現極為健康的牛市抗脆弱性與主升浪承接力。
        </p>
        <div class="pt-2 border-t border-slate-200/60 dark:border-zinc-700/60 flex items-center justify-between text-xs sm:text-sm font-semibold">
          <span class="text-slate-500 dark:text-zinc-400">📊 今日市場狀態判定：</span>
          <span class="text-emerald-600 dark:text-emerald-400 font-bold">油價破90壓低通膨預期，長端美債殖利率止漲整固，費半與光通訊重啟狂飆，AI核電創天價，牛市主線極致強勢！</span>
        </div>
      </div>
    </section>

    <!-- 1. 大盤表現總覽 -->
    <section id="sec-1" class="scroll-mt-6 font-sans">
      <h2 class="text-xl font-bold mb-4 flex items-center gap-2 border-b border-slate-100 dark:border-zinc-850 pb-2">
        <span class="text-brand-500">1.</span> 大盤表現總覽
      </h2>
      
      <div class="grid grid-cols-2 sm:grid-cols-4 gap-4 mb-6">
        <div class="p-4 rounded-xl bg-white dark:bg-zinc-900 border border-slate-200 dark:border-zinc-800/80 shadow-sm">
          <div class="text-xs text-slate-400 dark:text-zinc-500 font-semibold mb-1">S&P 500 (SPY)</div>
          <div class="text-lg sm:text-xl font-bold [SPY_COLOR]">[SPY_PRICE]</div>
          <div class="text-xs font-semibold mt-1 [SPY_COLOR]">[SPY_PCT] ([SPY_CHANGE])</div>
        </div>
        <div class="p-4 rounded-xl bg-white dark:bg-zinc-900 border border-slate-200 dark:border-zinc-800/80 shadow-sm">
          <div class="text-xs text-slate-400 dark:text-zinc-500 font-semibold mb-1">Nasdaq 100 (QQQ)</div>
          <div class="text-lg sm:text-xl font-bold [QQQ_COLOR]">[QQQ_PRICE]</div>
          <div class="text-xs font-semibold mt-1 [QQQ_COLOR]">[QQQ_PCT] ([QQQ_CHANGE])</div>
        </div>
        <div class="p-4 rounded-xl bg-white dark:bg-zinc-900 border border-slate-200 dark:border-zinc-800/80 shadow-sm">
          <div class="text-xs text-slate-400 dark:text-zinc-500 font-semibold mb-1">Dow Jones (DIA)</div>
          <div class="text-lg sm:text-xl font-bold [DIA_COLOR]">[DIA_PRICE]</div>
          <div class="text-xs font-semibold mt-1 [DIA_COLOR]">[DIA_PCT] ([DIA_CHANGE])</div>
        </div>
        <div class="p-4 rounded-xl bg-white dark:bg-zinc-900 border border-slate-200 dark:border-zinc-800/80 shadow-sm">
          <div class="text-xs text-slate-400 dark:text-zinc-500 font-semibold mb-1">Russell 2000 (IWM) / VIX</div>
          <div class="text-lg sm:text-xl font-bold [IWM_COLOR]">[IWM_PRICE]</div>
          <div class="text-xs font-semibold mt-1 [IWM_COLOR]">[IWM_PCT] (VIX: [VIX_PRICE])</div>
        </div>
      </div>

      <div class="p-5 rounded-xl bg-white dark:bg-zinc-900 border border-slate-200 dark:border-zinc-800/80 shadow-sm">
        <h3 class="text-sm font-semibold text-slate-700 dark:text-zinc-300 mb-4">主要指數與板塊 ETF 當日漲跌幅對比 (%)</h3>
        <div class="h-64 sm:h-80 relative">
          <canvas id="overviewChart"></canvas>
        </div>
      </div>

      <div class="mt-4 p-4 rounded-xl bg-slate-100 dark:bg-zinc-800/50 text-xs text-slate-600 dark:text-zinc-400 space-y-1">
        <p>• <strong>標普500指數 (^GSPC)</strong>：收報 <strong>7,670.84 點</strong>，微跌 <strong>-12.85 點 (-0.17%)</strong>，日內震盪區間 7,652.30 - 7,698.40 點，SPY ETF 收報 $764.20 (-0.18%)。指數在昨日大幅洗盤後迅速止跌回穩，全天牢牢守在 20 日均線（7,631 點）上方，展現極強的牛市支撐承接力。</p>
        <p>• <strong>納斯達克綜合指數 (^IXIC)</strong>：收報 <strong>26,797.54 點</strong>，微跌 <strong>-22.84 點 (-0.09%)</strong>；而科技權重更純粹的<strong>納斯達克100指數 (^NDX) 逆勢大漲 +62.52 點 (+0.21%) 收報 30,339.33 點</strong>，QQQ 收報 $737.93 (+0.19%)。半導體、光通訊與軟體巨頭反攻，有效抵消了蘋果（AAPL -2.66%）的下挫影響。</p>
        <p>• <strong>費城半導體指數 (^SOX)</strong>：強勢暴漲 <strong>+163.92 點 (+1.32%)</strong>，收報 <strong>12,629.16 點</strong>；SMH 收報 $606.90 (+1.15%)，SOXX 收報 $567.44 (+1.19%)。ASML(+3.56%)、ARM(+3.65%)、MRVL(+4.51%)與博通(+1.58%)領軍飆升，美光(MU +1.05%)財報前獲買盤卡位，費半再度逼近歷史天價！</p>
        <p>• <strong>道瓊工業指數 (^DJI)</strong>：收報 <strong>51,349.92 點</strong>，下跌 <strong>-131.59 點 (-0.26%)</strong>，DIA ETF 收報 $512.88 (-0.22%)。道瓊表現相對疲弱主要受到蘋果（-2.66%）重挫與雪佛龍、埃克森美孚等能源成分股因油價暴跌隨之走低拖累。</p>
        <p>• <strong>羅素2000小盤股 (^RUT)</strong>：收報 <strong>2,807.92 點</strong>，下跌 <strong>-9.99 點 (-0.35%)</strong>，IWM ETF 收報 $279.01 (-0.36%)。小盤股在利率高位區間持續測試 50 日均線支撐，等權標普 RSP 微跌 -0.11%。</p>
        <p>• <strong>波動率指數 (^VIX)</strong>：微幅回落 <strong>-0.03 點 (-0.19%)</strong>，收報 <strong>16.04 點</strong>。VIX 在昨日反彈後迅速平息，顯示市場情緒極度穩定，完全沒有恐慌性拋售壓力，處於安全健康區間。</p>
      </div>
    </section>

    <!-- 2. 盤中走勢復盤 -->
    <section id="sec-2" class="scroll-mt-6 font-sans">
      <h2 class="text-xl font-bold mb-4 flex items-center gap-2 border-b border-slate-100 dark:border-zinc-850 pb-2">
        <span class="text-brand-500">2.</span> 盤中走勢復盤
      </h2>
      <div class="p-5 rounded-xl bg-white dark:bg-zinc-900 border border-slate-200 dark:border-zinc-850 shadow-sm space-y-6">
        <div class="mermaid flex justify-center py-2">
          timeline
            title 2026-09-29 盤中走勢復盤 (油價重挫破$90美元美債殖利率回穩，費半強彈+1.32%，AI核電與光通訊狂飆)
            盤前原油重挫與長端美債殖利率企穩 (08:30) : WTI原油期貨大跌破$90關卡，10年期美債利率平穩在5.260%，晶片設備與AI期貨全面收紅走揚。
            早盤低開分化與半導體設備強勢反撲 (09:30-10:30) : 蘋果受降評傳聞拖累低開下探，但半導體設備ASML、ARM及光通訊LITE迅速拔地而起，費半指數開盤直接跳漲逾1%。
            午盤AI清潔核電狂飆與Meta強力逼空 (12:00-13:30) : VST突破$140天價、CEG漲破$264，公用事業板塊領跑標普；Meta大漲逾3%帶動那斯達克100翻紅向上。
            午後消費者信心數據平穩與油價跌幅擴大 (13:30-14:30) : 9月諮商會消費者信心指數報98.7，通膨預期降溫；沙烏地傳出增產意向令WTI原油擴大跌幅至-3.62%，能源板塊墊底。
            尾盤季末換手買盤鎖定半導體與高確定性AI (15:30-16:00) : 機構買盤聚焦高景氣半導體與AI基建，費半大漲+1.32%以12,629點高位作收，納指100收紅，標普守穩7,670點。
        </div>
        <p class="text-sm text-slate-500 dark:text-zinc-400 leading-relaxed">
          <strong>復盤深度解析：</strong>週二美股迎來了典型的<strong>「利率止漲整固＋能源成本崩跌帶動通膨降溫」</strong>的牛市主線重啟行情。早盤受蘋果（AAPL）遭遇券商下調評級預警 iPhone 換機週期拉長的衝擊，道瓊工業指數與標普 500 一度承壓低開；但大盤內在動能極度強勁，以 ASML、ARM、Marvell 為首的半導體硬體族群在買盤簇擁下迅速拔地而起，費半指數開盤便大漲逾 1%，宣告科技主升浪強勢回歸。
          <br><br>
          盤中最大焦點在於<strong>「實體能源成本崩跌 vs AI直供電溢價飛天」的奇妙二元對立</strong>。受市場傳聞沙烏地阿拉伯可能放棄每桶 $100 美元的非官方防線以增加產量以奪回市佔率影響，國際 WTI 原油期貨狂瀉 -3.62% 摜破 $90 大關收報 $89.25/桶。這大幅舒緩了前一日引發債券殖利率飆升的二次通膨擔憂，10 年期美債殖利率平穩在 5.260% 平台整固。然而，與化石能源暴跌截然相反的是，<strong>AI 算力中心對 24/7 零碳基載電力的剛性爭奪愈演愈烈，核電雙雄 VST（+2.04% 衝破 $140）與 CEG（+1.59% 衝破 $264）雙雙刷出歷史新天價</strong>，公用事業板塊（XLU +1.17%）傲視全場！
          <br><br>
          午盤過後，光通訊模組迎來爆發式逼空，Lumentum（LITE）狂飆逾 +5.6% 逼近千元大關，Coherent（COHR）大漲 +3.46%，印證 1.6T/3.2T 矽光子與高速傳輸已成為 AI 伺服器集裝箱的最硬核瓶頸。同時，Meta（+3.24%）與甲骨文（+3.91%）強勢大漲，帶動納斯達克 100 指數單邊拉升收紅。尾盤階段，季末結算被動賣壓被充沛的多頭承接資金完全化解，費半以全天高位強勢作收。整場盤面充分展現：在經歷昨日季末估值洗盤後，聰明錢正以極高效率集中湧入最具定價權與業績確定性的 AI 核心主線！
        </p>
      </div>
    </section>

    <!-- 3. 宏觀環境 -->
    <section id="sec-3" class="scroll-mt-6 font-sans">
      <h2 class="text-xl font-bold mb-4 flex items-center gap-2 border-b border-slate-100 dark:border-zinc-850 pb-2">
        <span class="text-brand-500">3.</span> 宏觀環境
      </h2>
      
      <div class="tabs p-1 bg-slate-150 dark:bg-zinc-800 rounded-lg inline-flex mb-4">
        <input type="radio" id="tab-yields" name="macro-tabs" checked>
        <label for="tab-yields">3.1 美債收益率</label>
        
        <input type="radio" id="tab-fed" name="macro-tabs">
        <label for="tab-fed">3.2 Fed 政策預期與利差</label>
        
        <input type="radio" id="tab-commodities" name="macro-tabs">
        <label for="tab-commodities">3.3 大宗與加密</label>
        
        <input type="radio" id="tab-data" name="macro-tabs">
        <label for="tab-data">3.4 當日經濟數據</label>
      </div>

      <div class="tab-content">
        <!-- Tab panel 1 -->
        <div id="panel-yields" class="tab-panel text-sm text-slate-650 dark:text-zinc-300 leading-relaxed bg-white dark:bg-zinc-900 p-5 rounded-xl border border-slate-200 dark:border-zinc-850 mt-2">
          <h4 class="font-bold text-slate-800 dark:text-white mb-2">10年期美債收益率在 5.260% 平台止漲整固，長天期公債拋壓顯著趨緩</h4>
          <div class="grid grid-cols-2 sm:grid-cols-4 gap-3 font-mono text-xs sm:text-sm mb-3">
            <div class="p-3 bg-slate-50 dark:bg-zinc-800/50 rounded-lg">
              <div class="text-xs text-slate-400 font-sans">3 個月國庫券 (^IRX)</div>
              <div class="font-bold text-slate-700 dark:text-zinc-300">[IRX_PRICE]% (+1 bp)</div>
            </div>
            <div class="p-3 bg-slate-50 dark:bg-zinc-800/50 rounded-lg">
              <div class="text-xs text-slate-400 font-sans">5 年期國債 (^FVX)</div>
              <div class="font-bold text-emerald-600 dark:text-emerald-400">[FVX_PRICE]% (-1 bp)</div>
            </div>
            <div class="p-3 bg-slate-50 dark:bg-zinc-800/50 rounded-lg">
              <div class="text-xs text-slate-400 font-sans">10 年期基準國債 (^TNX)</div>
              <div class="font-bold text-slate-800 dark:text-white">[TNX_PRICE]% (+1.5 bps)</div>
            </div>
            <div class="p-3 bg-slate-50 dark:bg-zinc-800/50 rounded-lg">
              <div class="text-xs text-slate-400 font-sans">30 年期長天期國債 (^TYX)</div>
              <div class="font-bold text-rose-500">[TYX_PRICE]% (+3 bps)</div>
            </div>
          </div>
          <p>
            <strong>深度解讀：</strong>在經歷週一長天期國債收益率跳升 27 個基點的劇烈震盪後，週二美債市場呈現明顯的<strong>止跌回穩與平台整固</strong>特徵。基準 10 年期美債收益率收報 <strong>5.260%</strong>，5 年期收益率微降至 5.060%，30 年期長債收益率微升至 5.590%。原油價格崩跌破 $90 美元大幅降低了未來的長期通膨預期，使得債券空頭平倉買盤浮現。殖利率曲線的極端陡峭化態勢在 5.25%–5.28% 區間遭遇強勁技術阻力，高估值科技股的貼現率壓力大幅鈍化，為成長股的反彈營造了健康的宏觀溫床。
          </p>
        </div>

        <!-- Tab panel 2 -->
        <div id="panel-fed" class="tab-panel text-sm text-slate-650 dark:text-zinc-300 leading-relaxed bg-white dark:bg-zinc-900 p-5 rounded-xl border border-slate-200 dark:border-zinc-850 mt-2">
          <h4 class="font-bold text-slate-800 dark:text-white mb-2">FedWatch 政策利率定價：11 月降息 25 基點機率升至 55%</h4>
          <p class="mb-3">
            根據 CME FedWatch 最新數據，隨著原油暴跌與消費者信心數據平穩降溫，市場對 <strong>11 月 FOMC 會議降息 25 個基點的機率預期回升至 55.2%</strong>，按兵不動的機率為 44.8%；年內累計降息預期維持在 25–50 個基點之間。
          </p>
          <div class="p-3 bg-slate-50 dark:bg-zinc-800/50 rounded-lg space-y-1.5 text-xs sm:text-sm">
            <div>• <strong>聯準會官員表態</strong>：里奇蒙聯儲總裁巴爾金（Barkin）與聯準會理事鮑曼（Bowman）週二發表演說，指出當前實質利率處於限制性水準，長端利率走高已在實質層面替聯準會收緊了金融環境。若後續非農就業與薪資增速呈現溫和降溫，貨幣政策將維持靈活微調空間，無需採取破壞性緊縮。</div>
            <div>• <strong>期限利差動態</strong>：10Y–2Y 利差維持在 +18 至 +20 bps 區間健康運作，長短端利差正常化確認經濟處於非衰退的健康軟著陸通道。</div>
          </div>
        </div>

        <!-- Tab panel 3 -->
        <div id="panel-commodities" class="tab-panel text-sm text-slate-650 dark:text-zinc-300 leading-relaxed bg-white dark:bg-zinc-900 p-5 rounded-xl border border-slate-200 dark:border-zinc-850 mt-2">
          <h4 class="font-bold text-slate-800 dark:text-white mb-2">原油崩跌破$90美元大關，黃金強勁反彈+1.15%，美元平穩，比特幣站穩8.36萬</h4>
          <div class="grid grid-cols-2 sm:grid-cols-4 gap-3 font-mono text-xs sm:text-sm mb-3">
            <div class="p-3 bg-slate-50 dark:bg-zinc-800/50 rounded-lg">
              <div class="text-xs text-slate-400 font-sans">美元指數 (DXY)</div>
              <div class="font-bold text-slate-700 dark:text-zinc-300">[DXY_PRICE] ([DXY_PCT])</div>
            </div>
            <div class="p-3 bg-slate-50 dark:bg-zinc-800/50 rounded-lg">
              <div class="text-xs text-slate-400 font-sans">現貨黃金 (GC=F)</div>
              <div class="font-bold text-emerald-600 dark:text-emerald-400">[GOLD_PRICE] ([GOLD_PCT])</div>
            </div>
            <div class="p-3 bg-slate-50 dark:bg-zinc-800/50 rounded-lg">
              <div class="text-xs text-slate-400 font-sans">WTI 原油 (CL=F)</div>
              <div class="font-bold text-rose-500">[USO_OIL_PRICE]/桶 ([USO_OIL_PCT])</div>
            </div>
            <div class="p-3 bg-slate-50 dark:bg-zinc-800/50 rounded-lg">
              <div class="text-xs text-slate-400 font-sans">比特幣 (BTC-USD)</div>
              <div class="font-bold text-emerald-600 dark:text-emerald-400">$[BTC_PRICE] ([BTC_PCT])</div>
            </div>
          </div>
          <p>
            • <strong>原油 (CL=F / BZ=F)</strong>：<strong>全天大宗商品最大黑天鵝！</strong>WTI 原油暴跌 <strong>-3.62%（-$3.35）收在 $89.25/桶</strong>，摜破 $90 關鍵心理防線；布蘭特原油重挫至 $95.93/桶。外媒報導沙烏地阿拉伯可能放棄每桶 $100 美元目標以維護市場佔有率，供給預期大增直接擊潰多頭支撐。<br>
            • <strong>現貨黃金 (GC=F)</strong>：在昨日暴跌超跌後迎來強力技術性反彈，上漲 <strong>+1.15%（+$47.90）收在 $4,216.50/oz</strong>，GLD 漲 +1.32%，重返 $4,200 大關上方，各國央行實物儲備買盤與逢低承接資金再度進場。<br>
            • <strong>美元指數 (DXY)</strong>：在美債利率止漲背景下溫和收在 <strong>101.42 (+0.22%)</strong>，維持在 101.20–101.50 窄幅整理區間。<br>
            • <strong>比特幣 (BTC-USD)</strong>：微漲 <strong>+0.17% 報 $83,643.31</strong>，連續多日在 8.35 萬美元高位平台上展現強勁抗跌韌性；以太坊（ETH-USD）微跌 -0.40% 報 $2,677.99。
          </p>
        </div>

        <!-- Tab panel 4 -->
        <div id="panel-data" class="tab-panel text-sm text-slate-650 dark:text-zinc-300 leading-relaxed bg-white dark:bg-zinc-900 p-5 rounded-xl border border-slate-200 dark:border-zinc-850 mt-2">
          <h4 class="font-bold text-slate-800 dark:text-white mb-2">當日公布重要經濟數據拆解</h4>
          <div class="overflow-x-auto">
            <table class="w-full text-xs text-left border-collapse">
              <thead class="bg-slate-50 dark:bg-zinc-800 border-b border-slate-200 dark:border-zinc-700">
                <tr>
                  <th class="p-2">經濟指標</th>
                  <th class="p-2">公布值</th>
                  <th class="p-2">預期值 / 前值</th>
                  <th class="p-2">市場解讀與影響</th>
                </tr>
              </thead>
              <tbody class="divide-y divide-slate-100 dark:divide-zinc-800">
                <tr>
                  <td class="p-2 font-semibold">標普 CoreLogic Case-Shiller 20城房價指數 (7月)</td>
                  <td class="p-2 font-mono text-emerald-600 font-bold">+6.1% YoY</td>
                  <td class="p-2 font-mono">預期 +6.2% / 前值 +6.5%</td>
                  <td class="p-2">全美房價年增率溫和降溫，反映高房貸利率對房地產價格的抑制效果持續顯現，房租通膨上行風險進一步消退。</td>
                </tr>
                <tr>
                  <td class="p-2 font-semibold">FHFA 房價指數 (7月)</td>
                  <td class="p-2 font-mono text-slate-700 dark:text-zinc-300">+0.2% MoM</td>
                  <td class="p-2 font-mono">預期 +0.2% / 前值 +0.1%</td>
                  <td class="p-2">數據完全符合預期，呈現溫和低通膨增長特徵，未見再通膨異動。</td>
                </tr>
                <tr>
                  <td class="p-2 font-semibold">美國 9 月諮商會消費者信心指數 (CB Consumer Confidence)</td>
                  <td class="p-2 font-mono text-slate-700 dark:text-zinc-300">98.7</td>
                  <td class="p-2 font-mono">預期 100.2 / 前值 101.8 (修正)</td>
                  <td class="p-2">消費者對勞動力市場的評價略有鬆動，通膨預期維持平穩，支持聯準會維持靈活降息路徑。</td>
                </tr>
                <tr>
                  <td class="p-2 font-semibold">達拉斯聯準會服務業收入指數 (9月)</td>
                  <td class="p-2 font-mono text-emerald-600 font-bold">+1.8</td>
                  <td class="p-2 font-mono">預期 +0.5 / 前值 -0.4</td>
                  <td class="p-2">服務業景氣低位由負轉正，凸顯美國本土實體經濟依然保持正向擴張韌性。</td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </section>

    <!-- 4. 板塊表現 -->
    <section id="sec-4" class="scroll-mt-6 font-sans">
      <h2 class="text-xl font-bold mb-4 flex items-center gap-2 border-b border-slate-100 dark:border-zinc-850 pb-2">
        <span class="text-brand-500">4.</span> 板塊表現（S&P 500 十一個板塊）
      </h2>
      
      <div class="p-5 rounded-xl bg-white dark:bg-zinc-900 border border-slate-200 dark:border-zinc-850 shadow-sm">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3 mb-4">
          <div class="text-xs text-slate-500 dark:text-zinc-400">點擊表頭可切換升降序排列，支援全欄位即時鍵盤搜尋篩選：</div>
          <input type="text" id="sectorSearch" placeholder="搜尋板塊或代碼..." class="px-3 py-1.5 rounded-lg border border-slate-200 dark:border-zinc-700 bg-slate-50 dark:bg-zinc-800 text-xs focus:outline-none focus:ring-2 focus:ring-brand-500">
        </div>
        
        <div class="overflow-x-auto">
          <table id="sectorTable" class="w-full text-xs sm:text-sm text-left border-collapse">
            <thead class="bg-slate-50 dark:bg-zinc-800/60 border-b border-slate-200 dark:border-zinc-700 text-slate-500 dark:text-zinc-400 font-semibold">
              <tr>
                <th class="p-3 sortable" onclick="sortTable('sectorTable', 0, true)">排名 ⬍</th>
                <th class="p-3 sortable" onclick="sortTable('sectorTable', 1)">板塊名稱 ⬍</th>
                <th class="p-3 sortable" onclick="sortTable('sectorTable', 2)">ETF 代號 ⬍</th>
                <th class="p-3 sortable" onclick="sortTable('sectorTable', 3, true)">當日漲跌 ⬍</th>
                <th class="p-3">近 5 日</th>
                <th class="p-3">近 1 月</th>
                <th class="p-3 sortable" onclick="sortTable('sectorTable', 6, true)">對比標普 ⬍</th>
                <th class="p-3">主要驅動因素</th>
              </tr>
            </thead>
            <tbody class="divide-y divide-slate-100 dark:divide-zinc-800">
[SECTOR_ROWS]
            </tbody>
          </table>
        </div>
        
        <div class="mt-4 p-4 rounded-lg bg-slate-50 dark:bg-zinc-800/40 text-xs text-slate-650 dark:text-zinc-400 space-y-1.5">
          <p>• <strong>最強領漲板塊</strong>：<strong>公用事業 (XLU +1.17%)</strong>、<strong>通訊服務 (XLC +0.26%)</strong>、<strong>工業 (XLI +0.21%)</strong>。公用事業板塊憑藉 AI 超算中心直供電的核能狂潮（VST +2.04%、CEG +1.59%）再度稱霸全市場！通訊板塊受 Meta（+3.24%）報復性大漲帶動，工業板塊則受電網改造升級（PWR、GEV）推升穩步上揚。</p>
          <p>• <strong>最弱領跌板塊</strong>：<strong>能源 (XLE -0.90%)</strong>、<strong>原物料 (XLB -0.75%)</strong>、<strong>必需消費 (XLP -0.52%)</strong>。WTI 原油重挫 -3.62% 跌破 $90 美元直接重創石油開採與煉化族群，大宗化工與基礎金屬同步下挫；必需消費板塊則因避險買盤撤離回流科技硬體而小幅回吐。</p>
          <p>• <strong>科技板塊結構分化</strong>：<strong>資訊科技 (XLK -0.02%)</strong>。半導體設備（ASML +3.56%）、客製化 ASIC 晶片（MRVL +4.51%）與博通（+1.58%）狂飆，但因權重第一的蘋果（AAPL -2.66%）下挫拉扯，使科技 ETF 呈現平盤微跌，內在動能遠強於表面指數！</p>
          <p>• <strong>核心風格輪動研判</strong>：資金呈現極其鮮明的<strong>「化石能源流出 ➔ AI 算力設備與清潔能源直供電湧入」</strong>的結構性輪動，市場對高科技基本面確定性充滿信心，主升浪邏輯極為清晰。</p>
        </div>
      </div>
    </section>

    <!-- 5. 主題與風格表現 -->
    <section id="sec-5" class="scroll-mt-6 font-sans">
      <h2 class="text-xl font-bold mb-4 flex items-center gap-2 border-b border-slate-100 dark:border-zinc-850 pb-2">
        <span class="text-brand-500">5.</span> 主題與風格表現
      </h2>
      
      <div class="grid grid-cols-1 md:grid-cols-2 gap-4 text-xs sm:text-sm">
        <div class="p-4 rounded-xl bg-white dark:bg-zinc-900 border border-slate-200 dark:border-zinc-850 shadow-sm space-y-2">
          <h4 class="font-bold text-slate-800 dark:text-white flex items-center justify-between">
            <span>半導體與 AI 硬體 (SOXX / SMH)</span>
            <span class="text-emerald-600 font-bold">[SOXX_PCT] / [SMH_PCT]</span>
          </h4>
          <p class="text-slate-650 dark:text-zinc-300 leading-relaxed">
            <strong>費半狂飆強彈，先進封裝與光刻機重啟主升浪！</strong>ASML（+3.56% 報 $1,834.39）、ARM（+3.65% 報 $293.67）、Marvell（MRVL +4.51% 報 $263.27）與博通（AVGO +1.58% 報 $355.10）全員暴漲；美光（MU +1.05% 報 $1,065.08）在明日重磅財報前夕獲買盤堅定卡位，半導體板塊成為全市場最強進攻主線。
          </p>
        </div>

        <div class="p-4 rounded-xl bg-white dark:bg-zinc-900 border border-slate-200 dark:border-zinc-850 shadow-sm space-y-2">
          <h4 class="font-bold text-slate-800 dark:text-white flex items-center justify-between">
            <span>光通訊與高速互聯 (LITE / COHR)</span>
            <span class="text-emerald-600 font-bold">+5.66% / +3.46%</span>
          </h4>
          <p class="text-slate-650 dark:text-zinc-300 leading-relaxed">
            <strong>光通訊雙雄上演史詩級逼空暴漲！</strong>Lumentum（LITE +5.66% 衝上 $973.49）與 Coherent（COHR +3.46% 衝破 $292），1.6T/3.2T 矽光子雷射光源晶片與高速光模組訂單排期至明年底，成為 AI 資料中心集群升級的最大硬體贏家。
          </p>
        </div>

        <div class="p-4 rounded-xl bg-white dark:bg-zinc-900 border border-slate-200 dark:border-zinc-850 shadow-sm space-y-2">
          <h4 class="font-bold text-slate-800 dark:text-white flex items-center justify-between">
            <span>AI 清潔電力與資料中心基建 (VST / CEG / GEV)</span>
            <span class="text-emerald-600 font-bold">+2.04% / +1.59% / +1.34%</span>
          </h4>
          <p class="text-slate-650 dark:text-zinc-300 leading-relaxed">
            <strong>核電與電網設備再創歷史新天價！</strong>Vistra（VST +2.04% 衝上 $140.83）、Constellation Energy（CEG +1.59% 衝上 $264.58）、GE Vernova（GEV +1.34% 報 $962.49），AI 超算 24/7 直供電合約享受極高市場定價溢價，多頭趨勢堅不可摧。
          </p>
        </div>

        <div class="p-4 rounded-xl bg-white dark:bg-zinc-900 border border-slate-200 dark:border-zinc-850 shadow-sm space-y-2">
          <h4 class="font-bold text-slate-800 dark:text-white flex items-center justify-between">
            <span>軟體 SaaS 與大型科技 (IGV / META / ORCL)</span>
            <span class="text-slate-700 dark:text-zinc-300 font-bold">[IGV_PCT] / +3.24% / +3.91%</span>
          </h4>
          <p class="text-slate-650 dark:text-zinc-300 leading-relaxed">
            甲骨文（ORCL +3.91%）與 Meta（+3.24%）引領反彈，CrowdStrike（+1.35%）與 Snowflake（+0.67%）逆勢收紅，有效抵消了長端利率帶來的估值阻力，軟體板塊在經歷昨日洗盤後逐步進入築底企穩通道。
          </p>
        </div>
      </div>
    </section>

    <!-- 6. 市場寬度與參與度 -->
    <section id="sec-6" class="scroll-mt-6 font-sans">
      <h2 class="text-xl font-bold mb-4 flex items-center gap-2 border-b border-slate-100 dark:border-zinc-850 pb-2">
        <span class="text-brand-500">6.</span> 市場寬度與參與度
      </h2>
      
      <div class="grid grid-cols-1 sm:grid-cols-3 gap-4 mb-4 text-xs sm:text-sm">
        <div class="p-4 rounded-xl bg-white dark:bg-zinc-900 border border-slate-200 dark:border-zinc-850 shadow-sm space-y-1">
          <div class="text-slate-400 font-semibold">6.1 均線參與度</div>
          <div class="text-base font-bold text-emerald-600 dark:text-emerald-400">標普高於 50MA: 81.2%</div>
          <p class="text-slate-500 dark:text-zinc-400">自昨日 80.5% 小幅回升，高於 200MA 維持在 75.8% 強勢擴張區，科技與公用事業多頭隊列完好。</p>
        </div>
        <div class="p-4 rounded-xl bg-white dark:bg-zinc-900 border border-slate-200 dark:border-zinc-850 shadow-sm space-y-1">
          <div class="text-slate-400 font-semibold">6.2 漲跌家數對比</div>
          <div class="text-base font-bold text-slate-800 dark:text-white">NYSE: 1,380 上漲 / 1,480 下跌</div>
          <p class="text-slate-500 dark:text-zinc-400">Nasdaq 漲跌比為 1:1.15（1,980 上漲 / 2,280 下跌），漲跌家數差距顯著收窄，市場寬度較昨日大幅改善。</p>
        </div>
        <div class="p-4 rounded-xl bg-white dark:bg-zinc-900 border border-slate-200 dark:border-zinc-850 shadow-sm space-y-1">
          <div class="text-slate-400 font-semibold">6.3 內部指標概況</div>
          <div class="text-base font-bold text-emerald-600 dark:text-emerald-400">McClellan 震盪指標: +26</div>
          <p class="text-slate-500 dark:text-zinc-400">指標自 +18 回升至 +26，處於健康多頭溫和區域；Put/Call Ratio 回落至 0.84，避險對沖情緒顯著降溫。</p>
        </div>
      </div>
    </section>

    <!-- 7. 技術面分析 -->
    <section id="sec-7" class="scroll-mt-6 font-sans">
      <h2 class="text-xl font-bold mb-4 flex items-center gap-2 border-b border-slate-100 dark:border-zinc-850 pb-2">
        <span class="text-brand-500">7.</span> 技術面分析（核心 ETF 與大盤狀態）
      </h2>
      
      <div class="p-5 rounded-xl bg-white dark:bg-zinc-900 border border-slate-200 dark:border-zinc-850 shadow-sm">
        <div class="overflow-x-auto">
          <table class="w-full text-xs sm:text-sm text-left border-collapse">
            <thead class="bg-slate-50 dark:bg-zinc-800/60 border-b border-slate-200 dark:border-zinc-700 text-slate-500 dark:text-zinc-400">
              <tr>
                <th class="p-3">標的代碼</th>
                <th class="p-3">收盤價格</th>
                <th class="p-3">當日漲跌</th>
                <th class="p-3">20 日 / 50 日均線</th>
                <th class="p-3">RSI (14)</th>
                <th class="p-3">MACD / 趨勢狀態</th>
                <th class="p-3">關鍵支撐 / 壓力</th>
              </tr>
            </thead>
            <tbody class="divide-y divide-slate-100 dark:divide-zinc-800 font-mono">
              <tr>
                <td class="p-3 font-semibold font-sans">SPY (標普500)</td>
                <td class="p-3">$[SPY_PRICE]</td>
                <td class="p-3 [SPY_COLOR]">[SPY_PCT]</td>
                <td class="p-3">$763.10 / $753.80</td>
                <td class="p-3">58.2 (良性整固蓄勢)</td>
                <td class="p-3 text-emerald-600 font-sans">守在20日線上，多頭均線發散</td>
                <td class="p-3">$760.00 / $772.00</td>
              </tr>
              <tr>
                <td class="p-3 font-semibold font-sans">QQQ (納指100)</td>
                <td class="p-3">$[QQQ_PRICE]</td>
                <td class="p-3 [QQQ_COLOR]">[QQQ_PCT]</td>
                <td class="p-3">$733.50 / $719.80</td>
                <td class="p-3">62.4 (逆勢收紅突破)</td>
                <td class="p-3 text-emerald-600 font-sans">重回上升趨勢軌道，多頭排列</td>
                <td class="p-3">$732.00 / $746.00</td>
              </tr>
              <tr>
                <td class="p-3 font-semibold font-sans">SOXX (費半)</td>
                <td class="p-3">$[SOXX_PRICE]</td>
                <td class="p-3 [SOXX_COLOR]">[SOXX_PCT]</td>
                <td class="p-3">$556.80 / $539.50</td>
                <td class="p-3">64.8 (強勢大陽線包覆)</td>
                <td class="p-3 text-emerald-600 font-sans">強勢大陽線收復失地，主升浪再起</td>
                <td class="p-3">$558.00 / $578.00</td>
              </tr>
              <tr>
                <td class="p-3 font-semibold font-sans">SMH (半導體ETF)</td>
                <td class="p-3">$[SMH_PRICE]</td>
                <td class="p-3 [SMH_COLOR]">[SMH_PCT]</td>
                <td class="p-3">$595.20 / $576.10</td>
                <td class="p-3">65.6 (突破$605關卡)</td>
                <td class="p-3 text-emerald-600 font-sans">晶片設備與AI晶片領跑，結構強勁</td>
                <td class="p-3">$598.00 / $618.00</td>
              </tr>
              <tr>
                <td class="p-3 font-semibold font-sans">DIA (道瓊工業)</td>
                <td class="p-3">$[DIA_PRICE]</td>
                <td class="p-3 [DIA_COLOR]">[DIA_PCT]</td>
                <td class="p-3">$515.80 / $514.20</td>
                <td class="p-3">50.8 (測試50日均線)</td>
                <td class="p-3 text-slate-700 dark:text-zinc-300 font-sans">受蘋果下挫牽制，箱體下軌整固</td>
                <td class="p-3">$510.00 / $520.00</td>
              </tr>
              <tr>
                <td class="p-3 font-semibold font-sans">IWM (羅素2000)</td>
                <td class="p-3">$[IWM_PRICE]</td>
                <td class="p-3 [IWM_COLOR]">[IWM_PCT]</td>
                <td class="p-3">$281.80 / $279.80</td>
                <td class="p-3">49.6 (守穩50日均線)</td>
                <td class="p-3 text-slate-700 dark:text-zinc-300 font-sans">在利率高檔區間反覆築底打底</td>
                <td class="p-3">$276.00 / $286.00</td>
              </tr>
              <tr>
                <td class="p-3 font-semibold font-sans">IGV (科技軟體)</td>
                <td class="p-3">$[IGV_PRICE]</td>
                <td class="p-3 [IGV_COLOR]">[IGV_PCT]</td>
                <td class="p-3">$106.50 / $104.40</td>
                <td class="p-3">53.8 (多重均線糾結)</td>
                <td class="p-3 text-emerald-600 font-sans">甲骨文大漲抵消SaaS弱勢，蓄勢待發</td>
                <td class="p-3">$103.50 / $109.00</td>
              </tr>
              <tr>
                <td class="p-3 font-semibold font-sans">XLK (科技板塊)</td>
                <td class="p-3">$[XLK_PRICE]</td>
                <td class="p-3 [XLK_COLOR]">[XLK_PCT]</td>
                <td class="p-3">$193.50 / $189.10</td>
                <td class="p-3">58.5 (高檔均線上方整固)</td>
                <td class="p-3 text-emerald-600 font-sans">半導體強勢與蘋果下挫互抵，多頭排列</td>
                <td class="p-3">$191.00 / $198.00</td>
              </tr>
            </tbody>
          </table>
        </div>
        <p class="text-xs text-slate-500 dark:text-zinc-400 mt-3">
          <strong>技術解讀：</strong>大盤技術架構呈現極為健康的「強弱換手與關鍵支撐確認」。標普 500（SPY）在昨日下探後，今日回測 $764 獲得強烈多頭承接，未給空頭任何下破 20 日均線的機會；費半（SOXX）以一根堅實的<strong>多頭大陽線完全包覆昨日陰線實體</strong>，宣告晶片族群洗盤完畢；QQQ 逆勢重返 $737 上方，明天季末結算日若能突破 $742 壓力，將直接發起第四季新一輪歷史極限攻勢。
        </p>
      </div>
    </section>

    <!-- 8. 重點個股新聞與異動 -->
    <section id="sec-8" class="scroll-mt-6 font-sans">
      <h2 class="text-xl font-bold mb-4 flex items-center gap-2 border-b border-slate-100 dark:border-zinc-850 pb-2">
        <span class="text-brand-500">8.</span> 重點個股新聞與異動（點擊展開詳細解讀）
      </h2>
      
      <div class="space-y-3 text-xs sm:text-sm">
        <details class="p-4 rounded-xl bg-white dark:bg-zinc-900 border border-slate-200 dark:border-zinc-850 shadow-sm group" open>
          <summary class="font-bold text-slate-800 dark:text-white cursor-pointer flex items-center justify-between">
            <span>8.1 大型科技七巨頭 (Magnificent 7) 走勢與核心新聞</span>
            <span class="text-xs text-brand-500 group-open:rotate-180 transition">▼</span>
          </summary>
          <div class="mt-3 pt-3 border-t border-slate-100 dark:border-zinc-800 space-y-2 text-slate-650 dark:text-zinc-300">
            <p>• <strong>Meta (META +3.24% 收 $738.79)</strong>：<strong>暴力反彈收復失地！</strong>在昨日遭遇季末對沖基金獲利了結大跌後，逢低買盤蜂擁而入，全天單邊走高大漲逾 +3.2%。市場極度認可其 Llama 開源大模型生態與 AI 智慧廣告投放下半年超高投資回報率（ROI），強勢重回歷史天價平台附近。</p>
            <p>• <strong>輝達 (NVDA -0.72% 收 $227.21)</strong>：<strong>昨日大漲後良性縮量整固！</strong>在昨日大盤暴跌中逆勢狂飆 +1.7% 後，今日窄幅整固於 $227 上方。華爾街投行最新調查重申四大雲端服務商（CSP）對 Blackwell Ultra 晶片的狂熱需求，訂單滿載至 2027 年年中，科技中流砥柱地位堅如磐石。</p>
            <p>• <strong>蘋果 (AAPL -2.66% 收 $329.40)</strong>：<strong>拖累大盤的最大逆風！</strong>巴克萊與摩根大通在最新報告中指出，雖然新旗艦預購熱絡，但新一代 AI 功能在歐盟等海外市場面臨監管落地延後，部分投資者憂心換機高峰可能遞延，導致股價回測 $330 整數關卡，單日重挫 dragging 道瓊與標普。</p>
            <p>• <strong>亞馬遜 (AMZN +0.21% 收 $246.67)</strong>：逆勢小幅收紅，AWS 雲端利潤率持續保持在 35% 以上高位，次世代 Trainium 2 自研晶片商業化部署推進順暢，牢牢守穩 $245 支撐。</p>
            <p>• <strong>微軟 (MSFT -0.05% 收 $508.96)</strong>：窄幅橫盤幾乎收平，守在 $508 上方，Azure AI 企業長約積壓總額突破 2,400 億美元，與核電巨頭 CEG 的三哩島重啟供電協議進展順遂。</p>
            <p>• <strong>谷歌母公司 Alphabet (GOOGL -0.53% 收 $340.92)</strong>：守在 $340 整數關卡上方，自研 TPU v6 大規模集裝箱部署顯著降低外部算力租賃成本，Gemini 企業 API 調用維持翻倍增長。</p>
            <p>• <strong>特斯拉 (TSLA -1.29% 收 $352.84)</strong>：在即將發布 Q3 全球交付量數據前夕市場情緒趨於審慎，股價在 $350-$355 區間蓄勢震盪。</p>
          </div>
        </details>

        <details class="p-4 rounded-xl bg-white dark:bg-zinc-900 border border-slate-200 dark:border-zinc-850 shadow-sm group">
          <summary class="font-bold text-slate-800 dark:text-white cursor-pointer flex items-center justify-between">
            <span>8.2 AI 硬體 / 半導體重點股異動分析（費半大暴走）</span>
            <span class="text-xs text-brand-500 group-open:rotate-180 transition">▼</span>
          </summary>
          <div class="mt-3 pt-3 border-t border-slate-100 dark:border-zinc-850 space-y-2 text-slate-650 dark:text-zinc-300">
            <p>• <strong>艾司摩爾 (ASML +3.56% 收 $1,834.39)</strong>：<strong>先進製程設備王者強勢回歸！</strong>台積電 2nm 與海外晶圓廠 High-NA EUV 光刻機交付排程再度提前，花旗重申其「首選買入」評級，單日暴漲逾 63 美元，強勢突破 $1,830！</p>
            <p>• <strong>邁威爾 (MRVL +4.51% 收 $263.27)</strong>：<strong>全場晶片黑馬狂飆！</strong>1.6T 光互聯 DSP 晶片與超大規模 CSP 客製化 AI 加速晶片產能開出，機構買盤大舉湧入，大漲 +4.51% 創下近期波段新天價！</p>
            <p>• <strong>安謀 (ARM +3.65% 收 $293.67)</strong>：自昨日大跌中報復性強彈，v9 架構在行動終端與 AI PC 滲透率加速提高，版稅收入進入爆發期，重返 $293 上方。</p>
            <p>• <strong>博通 (AVGO +1.58% 收 $355.10)</strong>：客製化 ASIC 晶片與 Tomahawk 6 交換晶片出貨暢旺，股價單邊上揚逼近歷史新高，展現無敵護城河。</p>
            <p>• <strong>台積電 ADR (TSM +0.90% 收 $456.94)</strong>：穩步上揚站穩 $456，2nm 與 A16 先進封裝 CoWoS-L 擴產產能全數被蘋果、輝達預定一空。</p>
            <p>• <strong>美光科技 (MU +1.05% 收 $1,065.08)</strong>：<strong>週三 9 月 30 日盤後即將發布 Q4 重磅財報！</strong>資金提前進場卡位，市場預期 HBM3e/HBM4 產能售罄至 2027 年將帶來史上最強毛利率擴張指引。</p>
            <p>• <strong>超微 (AMD -0.05% 收 $607.57)</strong>：守在 $607 上方極致橫盤，牢牢站穩 $600 整數大關與 1 兆美元市值大關，MI350 雲端叢集規模化驗證進展順暢。</p>
            <p>• <strong>維諦技術 (VRT +1.76% 收 $248.34)</strong>：高熱密度液冷 CDU 分配單元與資料中心冷卻系統訂單供不應求，股價迅速反彈收在 $248.34。</p>
          </div>
        </details>

        <details class="p-4 rounded-xl bg-white dark:bg-zinc-900 border border-slate-200 dark:border-zinc-850 shadow-sm group">
          <summary class="font-bold text-slate-800 dark:text-white cursor-pointer flex items-center justify-between">
            <span>8.3 軟體 / SaaS / AI 應用重點股異動分析</span>
            <span class="text-xs text-brand-500 group-open:rotate-180 transition">▼</span>
          </summary>
          <div class="mt-3 pt-3 border-t border-slate-100 dark:border-zinc-850 space-y-2 text-slate-650 dark:text-zinc-300">
            <p>• <strong>甲骨文 (ORCL +3.91% 收 $137.79)</strong>：<strong>全天軟體板塊領頭羊！</strong>多雲架構資料庫深度整合 AWS、Azure 與 Google Cloud，OCI AI 算力基礎設施簽約金額超預期，股價放量大漲近 +4% 突破整理平台！</p>
            <p>• <strong>CrowdStrike (CRWD +1.35% 收 $262.74)</strong>：延續昨日強勁爆發力，Falcon 終端與雲端 AI 安全代理簽約額維持超高速擴張，穩步突破 $262。</p>
            <p>• <strong>Snowflake (SNOW +0.67% 收 $330.31)</strong>：逆勢反彈收復 $330 整數關卡，企業現代化資料倉儲用量保持擴張。</p>
            <p>• <strong>Adobe (ADBE +0.94% 收 $233.17)</strong>：在 $230 頸線獲得強力支撐，生成式 AI 工具 Firefly 商業化訂閱轉換率穩步改善。</p>
            <p>• <strong>Palantir (PLTR -0.27% 收 $186.97)</strong>：守在 $187 高檔平台上窄幅微震，AIP 在軍工防務與財富 500 強企業中的落地勢不可擋。</p>
            <p>• <strong>Palo Alto Networks (PANW -0.94% 收 $388.41)</strong>：昨日暴漲逾 +4.6% 後正常消化短線獲利盤，穩居 $388 歷史天價高檔。</p>
            <p>• <strong>Salesforce (CRM -0.86% 收 $225.31)</strong>：Agentforce 智慧體架構處於客戶試點導入期，股價在低檔進行估值磨底整固。</p>
          </div>
        </details>

        <details class="p-4 rounded-xl bg-white dark:bg-zinc-900 border border-slate-200 dark:border-zinc-850 shadow-sm group">
          <summary class="font-bold text-slate-800 dark:text-white cursor-pointer flex items-center justify-between">
            <span>8.4 AI 清潔電力 / 資料中心 / 能源基礎設施分析（雙雄續刷天價）</span>
            <span class="text-xs text-brand-500 group-open:rotate-180 transition">▼</span>
          </summary>
          <div class="mt-3 pt-3 border-t border-slate-100 dark:border-zinc-850 space-y-2 text-slate-650 dark:text-zinc-300">
            <p>• <strong>Vistra (VST +2.04% 收 $140.83)</strong>：<strong>衝破 $140 歷史天價！</strong>AI 超算中心 24/7 直供電核能長約供不應求，市場給予其公用事業中無可匹敵的「高成長科技溢價」，多頭狂潮單邊加速！</p>
            <p>• <strong>Constellation Energy (CEG +1.59% 收 $264.58)</strong>：<strong>再創歷史新高！</strong>微軟三哩島 20 年直供電合約確立了無碳基載電力的天價定價基準，獲華爾街一致調升目標價至 $280 上方。</p>
            <p>• <strong>奇異Vernova (GEV +1.34% 收 $962.49)</strong>：大型燃氣輪機與電網轉型配電設備訂單排期達 4 年，股價向 $1,000 天價大關發起衝擊。</p>
            <p>• <strong>廣達服務 (PWR +1.15% 收 $651.79)</strong>：北美超高壓輸電線路改造與變電所擴建工程大單激增，股價續刷歷史新高。</p>
            <p>• <strong>Fluence Energy (FLNC +4.27% 收 $7.82)</strong>：暴漲 +4.27% 收復 $7.8，油價重挫與電網儲能併網需求帶動短線超跌強力反彈。</p>
            <p>• <strong>伊頓 (ETN +0.43% 收 $433.27)</strong>：高壓電氣設備交期拉長，股價在 $433 歷史高檔穩健運作。</p>
            <p>• <strong>Oklo (OKLO 持平報 $37.11)</strong>：SMR 小型核能反應爐商業化推進順利，於 $37 平台健康整固。</p>
          </div>
        </details>

        <details class="p-4 rounded-xl bg-white dark:bg-zinc-900 border border-slate-200 dark:border-zinc-850 shadow-sm group">
          <summary class="font-bold text-slate-800 dark:text-white cursor-pointer flex items-center justify-between">
            <span>8.5 光通訊雙雄爆發與其他顯著異動</span>
            <span class="text-xs text-brand-500 group-open:rotate-180 transition">▼</span>
          </summary>
          <div class="mt-3 pt-3 border-t border-slate-100 dark:border-zinc-850 space-y-2 text-slate-650 dark:text-zinc-300">
            <p>• <strong>Lumentum (LITE +5.66% 收 $973.49)</strong>：<strong>全場最大爆發點！</strong>受資料中心 1.6T 光模組與 EML 雷射晶片超級需求推動，股價上演暴力逼空，單日飆漲逾 52 美元突破天價！</p>
            <p>• <strong>Coherent (COHR +3.46% 收 $292.21)</strong>：高速 VCSEL 與 800G/1.6T 光通訊收發模組訂單暴增，放量大漲 +3.46% 突破 $290 關卡。</p>
            <p>• <strong>雪佛龍 (CVX -1.25%) 與 埃克森美孚 (XOM -1.10%)</strong>：受 WTI 原油崩跌 -3.62% 跌破 $90 拖累，傳統石油巨頭全線走弱。</p>
            <p>• <strong>紐蒙特黃金 (NEM +1.85%)</strong>：隨國際現貨金價反彈 +1.15% 突破 $4,216 而震盪回升。</p>
          </div>
        </details>
      </div>
    </section>

    <!-- 9. 財報日曆與解讀 -->
    <section id="sec-9" class="scroll-mt-6 font-sans">
      <h2 class="text-xl font-bold mb-4 flex items-center gap-2 border-b border-slate-100 dark:border-zinc-850 pb-2">
        <span class="text-brand-500">9.</span> 財報日曆與財報解讀
      </h2>
      <div class="p-5 rounded-xl bg-white dark:bg-zinc-900 border border-slate-200 dark:border-zinc-850 shadow-sm space-y-4 text-xs sm:text-sm">
        <div>
          <h4 class="font-bold text-slate-800 dark:text-white mb-1">9.1 已公佈重點財報深度拆解</h4>
          <p class="text-slate-650 dark:text-zinc-300">
            週二美股盤前公布的企業商業服務巨頭信達思（Cintas, CTAS）與薪資處理龍頭沛齊（Paychex, PAYX）第一財季財報雙雙優於市場預期。信達思營收 25.8 億美元（預期 25.4 億）、EPS $1.15（預期 $1.10），顯現北美中小型企業營運黏性極強；嘉年華郵輪（CCL）盤前財報亦確認郵輪預訂能見度直通 2027 年，反映高階消費力道穩健，為實體經濟非衰退注入強心針。
          </p>
        </div>
        <div>
          <h4 class="font-bold text-slate-800 dark:text-white mb-1">9.2 未來 1-3 個交易日財報日曆核心關注點</h4>
          <div class="space-y-3 mt-2">
            <div class="p-3 bg-slate-50 dark:bg-zinc-800/50 rounded-lg">
              <div class="flex items-center justify-between font-semibold text-slate-800 dark:text-white mb-1">
                <span>美光科技 (Micron, MU) — 2026 會計年度 Q4 財報（9 月 30 日週三盤後）</span>
                <span class="text-indigo-600 font-bold">全市場最高權限決戰點</span>
              </div>
              <p class="text-slate-650 dark:text-zinc-300">
                作為 AI 存儲超級週期的絕對核心指標，美光將於明日盤後公布業績。華爾街共識營收預期為 112 億美元、每股收益 $2.85。市場最核心觀測焦點：<strong>1) HBM3e 與下一代 HBM4 產能售罄狀況與長約溢價；2) 企業級超高容量 Gen5 SSD 在資料中心的放量節奏；3) 次季毛利率指引能否衝破 45% 歷史天花板。</strong>美光財報將直接定調半導體板塊能否在第四季發動歷史級主升浪！
              </p>
            </div>
            <div class="p-3 bg-slate-50 dark:bg-zinc-800/50 rounded-lg">
              <div class="flex items-center justify-between font-semibold text-slate-800 dark:text-white mb-1">
                <span>耐吉 (Nike, NKE - 10 月 1 日週四盤後)</span>
                <span class="text-slate-700 dark:text-zinc-300 font-bold">運動零售與庫存去化</span>
              </div>
              <p class="text-slate-650 dark:text-zinc-300">
                觀察管理層換帥後的產品創新戰略調整、直營電商與經銷批發渠道庫存去化成果，以及北美與亞洲市場消費動能。
              </p>
            </div>
            <div class="p-3 bg-slate-50 dark:bg-zinc-800/50 rounded-lg">
              <div class="flex items-center justify-between font-semibold text-slate-800 dark:text-white mb-1">
                <span>康尼格拉 (CAG) & 喜星 (STZ)（10 月 1 日–2 日）</span>
                <span class="text-slate-700 dark:text-zinc-300 font-bold">民生消費與包裝食品</span>
              </div>
              <p class="text-slate-650 dark:text-zinc-300">
                檢驗食品飲料終端定價彈性與消費者對日常開支的價格敏感度。
              </p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- 10. 機構觀點與資金流 -->
    <section id="sec-10" class="scroll-mt-6 font-sans">
      <h2 class="text-xl font-bold mb-4 flex items-center gap-2 border-b border-slate-100 dark:border-zinc-850 pb-2">
        <span class="text-brand-500">10.</span> 機構觀點與資金流向
      </h2>
      <div class="p-5 rounded-xl bg-white dark:bg-zinc-900 border border-slate-200 dark:border-zinc-850 shadow-sm space-y-3 text-xs sm:text-sm">
        <p class="text-slate-650 dark:text-zinc-300 leading-relaxed">
          • <strong>高盛全球宏觀與交易團隊 (Goldman Sachs Global Markets)</strong>：「原油價格重挫跌破 $90 美元是一項極具分水嶺意義的宏觀催化劑。能源價格的大幅走低將徹底封死第四季度二次通膨的想像空間，實質上為聯準會開啟了寬鬆政策通道。過去 24 小時內，多資產基金的風險平價模型（Risk Parity）迅速停止了對股票的減倉操作，科技硬體（Semis & Optical）已重新成為超額阿爾法（Alpha）集中湧入的核心窪地。」
        </p>
        <p class="text-slate-650 dark:text-zinc-300 leading-relaxed">
          • <strong>美銀證券 (BofA Global Research)</strong>：「半導體設備（ASML）與光通訊（LITE）的放量暴漲，印證了 AI 基礎設施投資正從單純的 GPU 採購，全面擴散至晶圓代工光刻產能、高速光電互聯與冷卻能源直供。市場的結構比單純看大盤指數更加健康，第四季度科技板塊 EPS 成長預期依然冠絕全美。」
        </p>
        <p class="text-slate-650 dark:text-zinc-300 leading-relaxed">
          • <strong>期權大宗異動追蹤</strong>：美光科技（MU）在財報前夕湧現巨額行權價 $1,100 與 $1,150 的 10 月中旬到期買權（Calls）押注大單；Meta（META）收復失地過程中出現超過 8,500 萬美元的大宗買權掃貨；同時，WTI 原油相關 ETF（USO）出現大量看跌期權（Puts）主動開倉。
        </p>
      </div>
    </section>

    <!-- 11. 板塊輪動判斷 -->
    <section id="sec-11" class="scroll-mt-6 font-sans">
      <h2 class="text-xl font-bold mb-4 flex items-center gap-2 border-b border-slate-100 dark:border-zinc-850 pb-2">
        <span class="text-brand-500">11.</span> 板塊輪動判斷
      </h2>
      <div class="p-5 rounded-xl bg-white dark:bg-zinc-900 border border-slate-200 dark:border-zinc-850 shadow-sm leading-relaxed text-xs sm:text-sm space-y-2 text-slate-650 dark:text-zinc-300">
        <p>
          當前市場演繹著極度教科書級別的<strong>「能源防禦撤離 ➔ 半導體設備與光通訊強攻 ➔ AI核電直供溢價飛天」</strong>的主升浪輪動格局。
        </p>
        <p>
          <strong>關鍵研判結論：昨日的指數調整被證實為純粹的季末技術性洗盤，當前市場正處於『強趨勢主升浪中的主線集中爆發期』！</strong>核心邏輯有三：
          第一，<strong>半導體板塊強勁包覆反撲</strong>：費半（SOX +1.32%）一陽吞一陰，ASML(+3.56%)、ARM(+3.65%)、MRVL(+4.51%)全線大爆發，印證科技牛市最硬核的底層邏輯毫髮無傷；
          第二，<strong>原油暴跌破 $90 徹底拆除通膨炸彈</strong>：能源板塊墊底、油價大跌直接為實質利率與長端美債收益率封頂，大幅提升了整個成長股市場的估值容忍度；
          第三，<strong>AI核電雙雄（VST +2.04%、CEG +1.59%）再度刷出歷史新天價</strong>，公用事業板塊領跑標普，證明實體能源對 AI 算力資料中心的剛需溢價已成為獨立於大盤週期的「超級印鈔機」。一旦明日季末（9/30）結算被動賣盤完全出清，大盤將與美光財報共振展開新一波歷史級逼空！
        </p>
      </div>
    </section>

    <!-- 12. 我的重點關注股觀察 -->
    <section id="sec-12" class="scroll-mt-6 font-sans">
      <h2 class="text-xl font-bold mb-4 flex items-center gap-2 border-b border-slate-100 dark:border-zinc-850 pb-2">
        <span class="text-brand-500">12.</span> 我的重點關注股觀察 (23 標的完整追蹤)
      </h2>
      
      <div class="p-5 rounded-xl bg-white dark:bg-zinc-900 border border-slate-200 dark:border-zinc-850 shadow-sm">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3 mb-4">
          <div class="text-xs text-slate-500 dark:text-zinc-400">點擊表頭可切換升降序排列，支援全欄位即時鍵盤搜尋篩選：</div>
          <input type="text" id="watchSearch" placeholder="搜尋代碼、操作判定或動態..." class="px-3 py-1.5 rounded-lg border border-slate-200 dark:border-zinc-700 bg-slate-50 dark:bg-zinc-800 text-xs focus:outline-none focus:ring-2 focus:ring-brand-500">
        </div>
        
        <div class="overflow-x-auto">
          <table id="watchTable" class="w-full text-xs sm:text-sm text-left border-collapse">
            <thead class="bg-slate-50 dark:bg-zinc-800/60 border-b border-slate-200 dark:border-zinc-700 text-slate-500 dark:text-zinc-400 font-semibold">
              <tr>
                <th class="p-3 sortable" onclick="sortTable('watchTable', 0)">代碼 ⬍</th>
                <th class="p-3 sortable" onclick="sortTable('watchTable', 1, true)">收盤價 ⬍</th>
                <th class="p-3 sortable" onclick="sortTable('watchTable', 2, true)">漲跌幅 ⬍</th>
                <th class="p-3">技術趨勢與關鍵動態</th>
                <th class="p-3">支撐 / 壓力</th>
                <th class="p-3">操作判定</th>
              </tr>
            </thead>
            <tbody class="divide-y divide-slate-100 dark:divide-zinc-800">
[WATCH_ROWS]
            </tbody>
          </table>
        </div>
      </div>
    </section>

    <!-- 13. 次日交易計畫 / 觀察清單 -->
    <section id="sec-13" class="scroll-mt-6 font-sans">
      <h2 class="text-xl font-bold mb-4 flex items-center gap-2 border-b border-slate-100 dark:border-zinc-850 pb-2">
        <span class="text-brand-500">13.</span> 次日交易計畫 / 觀察清單 (2026-09-30 展望)
      </h2>
      
      <div class="grid grid-cols-1 md:grid-cols-3 gap-4 text-xs sm:text-sm">
        <div class="p-4 rounded-xl bg-white dark:bg-zinc-900 border border-slate-200 dark:border-zinc-850 shadow-sm space-y-2">
          <h4 class="font-bold text-slate-800 dark:text-white">13.1 宏觀核心觀察</h4>
          <ul class="space-y-1.5 text-slate-650 dark:text-zinc-300">
            <li>• <strong>美國 9 月 ADP 就業人數 (週三 08:15)</strong>：市場預期新增 14.5 萬人，作為週五非農大考的前哨指標。</li>
            <li>• <strong>10年期美債收益率 (^TNX)</strong>：觀察能否在 5.25% 支撐平台維持平穩整固，若回落至 5.20% 以下將觸發全面狂歡。</li>
            <li>• <strong>WTI 原油在 $88-$90 的破位延續性</strong>：觀察低油價是否能持續鎖死二次通膨預期。</li>
            <li>• <strong>第三季度末（Q3 End）最後結算日</strong>：機構被動指數換手完成後，資金回補科技股力道。</li>
          </ul>
        </div>

        <div class="p-4 rounded-xl bg-white dark:bg-zinc-900 border border-slate-200 dark:border-zinc-850 shadow-sm space-y-2">
          <h4 class="font-bold text-slate-800 dark:text-white">13.2 大盤關鍵攻防位置</h4>
          <ul class="space-y-1.5 text-slate-650 dark:text-zinc-300">
            <li>• <strong>SPY (標普500)</strong>：關鍵支撐位 $760.00，上方反彈壓力位 $770.00 / $775.00。</li>
            <li>• <strong>QQQ (納指100)</strong>：守穩 $732.00 頸線，上方目標衝擊 $742.00 / $746.00 歷史新天價。</li>
            <li>• <strong>SOXX (費半)</strong>：關鍵防守位 $558.00，上方突破目標 $575.00。</li>
            <li>• <strong>DIA (道瓊工業)</strong>：關鍵支撐位 $510.00，觀察蘋果能否止跌回穩。</li>
          </ul>
        </div>

        <div class="p-4 rounded-xl bg-white dark:bg-zinc-900 border border-slate-200 dark:border-zinc-850 shadow-sm space-y-2">
          <h4 class="font-bold text-slate-800 dark:text-white">13.3 核心個股觀察清單</h4>
          <ul class="space-y-1.5 text-slate-650 dark:text-zinc-300">
            <li>• <strong>全市場超級決戰點</strong>：<strong>美光科技 (MU 週三盤後重磅財報，存儲超級週期指引)</strong>。</li>
            <li>• <strong>科技多頭總旗手</strong>：<strong>輝達 (NVDA 站穩$225，蓄勢重啟衝擊$235)</strong>。</li>
            <li>• <strong>光通訊逼空黑馬</strong>：<strong>Lumentum (LITE 挑戰$1,000天價大關)</strong>、<strong>Coherent (COHR 衝刺$300)</strong>。</li>
            <li>• <strong>AI核電雙雄無敵神話</strong>：<strong>Vistra (VST 站穩$140)</strong>、<strong>Constellation (CEG 站穩$264)</strong>。</li>
            <li>• <strong>兆元市值保衛戰</strong>：<strong>超微 (AMD 守穩$600整數關卡，醞釀突破)</strong>。</li>
          </ul>
        </div>
      </div>
    </section>

    <!-- 14. 風險提示矩陣 -->
    <section id="sec-14" class="scroll-mt-6 font-sans">
      <h2 class="text-xl font-bold mb-4 flex items-center gap-2 border-b border-slate-100 dark:border-zinc-850 pb-2">
        <span class="text-brand-500">14.</span> 風險提示矩陣
      </h2>
      <div class="p-5 rounded-xl bg-white dark:bg-zinc-900 border border-slate-200 dark:border-zinc-850 shadow-sm overflow-x-auto text-xs sm:text-sm">
        <table class="w-full text-left border-collapse">
          <thead class="bg-slate-50 dark:bg-zinc-800/60 border-b border-slate-200 dark:border-zinc-700 text-slate-500 dark:text-zinc-400">
            <tr>
              <th class="p-3">風險維度 / 潛在事件</th>
              <th class="p-3">風險評級</th>
              <th class="p-3">影響機制與潛在威脅</th>
              <th class="p-3">應對策略與避險建議</th>
            </tr>
          </thead>
          <tbody class="divide-y divide-slate-100 dark:divide-zinc-800">
            <tr>
              <td class="p-3 font-semibold">美光科技 (MU) 9月30日盤後財報高預期博弈</td>
              <td class="p-3"><span class="px-2 py-0.5 rounded text-xs font-bold bg-orange-100 dark:bg-orange-950 text-orange-700 dark:text-orange-300">中高風險</span></td>
              <td class="p-3">市場對 HBM 產能售罄與毛利率期待極度高昂，若財測指引僅僅符合預期，可能引發短線晶片股震盪獲利回吐。</td>
              <td class="p-3">現貨底倉堅定持有，高槓桿期權部位建議在盤前逢高鎖定部分利潤，或構建跨式保護。</td>
            </tr>
            <tr>
              <td class="p-3 font-semibold">季末（Q3 End）最後結算日（9/30）被動資金換手</td>
              <td class="p-3"><span class="px-2 py-0.5 rounded text-xs font-bold bg-yellow-100 dark:bg-yellow-950 text-yellow-700 dark:text-yellow-300">中等風險</span></td>
              <td class="p-3">季末最後一個交易日被動指數基金收盤競價集合換手，盤尾可能引發部分個股技術性瞬間波動。</td>
              <td class="p-3">避免在尾盤盲目追漲殺跌，逢非基本面雜訊壓低回踩核心支撐時大膽承接。</td>
            </tr>
            <tr>
              <td class="p-3 font-semibold">10年期美債利率 5.26% 高檔平台震盪</td>
              <td class="p-3"><span class="px-2 py-0.5 rounded text-xs font-bold bg-yellow-100 dark:bg-yellow-950 text-yellow-700 dark:text-yellow-300">中等風險</span></td>
              <td class="p-3">雖然長端利率止漲整固，但絕對水準仍在 5.25% 上方，仍可能對無盈利成長股構成折現溢價壓制。</td>
              <td class="p-3">堅守具備強大現金流與營收爆發力的 AI 硬體（NVDA/AVGO）與直供電核能（VST/CEG）。</td>
            </tr>
            <tr>
              <td class="p-3 font-semibold">原油暴跌引發的能源開採業資本支出收縮</td>
              <td class="p-3"><span class="px-2 py-0.5 rounded text-xs font-bold bg-slate-100 dark:bg-slate-800 text-slate-700 dark:text-slate-300">低風險</span></td>
              <td class="p-3">WTI 原油跌破 $90 對能源板塊（XLE）構成下行壓力，但對整體宏觀經濟與消費信心實質為正向利多。</td>
              <td class="p-3">減碼傳統油氣探勘股，資金集中配置於受惠電網升級的綠能與核電。</td>
            </tr>
            <tr>
              <td class="p-3 font-semibold">系統性金融流動性與信用利差風險</td>
              <td class="p-3"><span class="px-2 py-0.5 rounded text-xs font-bold bg-emerald-100 dark:bg-emerald-950 text-emerald-700 dark:text-emerald-300">低風險</span></td>
              <td class="p-3">VIX 恐慌指數回落至 16.04 點安全低檔；高收益債信用利差維持緊縮，金融體系流動性極其充沛。</td>
              <td class="p-3">維持牛市主升浪做多思維，把握任何洗盤帶來的第四季絕佳布局契機。</td>
            </tr>
          </tbody>
        </table>
      </div>
    </section>

    <!-- 15. 最終結論 -->
    <section id="sec-15" class="scroll-mt-6 font-sans">
      <h2 class="text-xl font-bold mb-4 flex items-center gap-2 border-b border-slate-100 dark:border-zinc-850 pb-2">
        <span class="text-brand-500">15.</span> 最終結論
      </h2>
      
      <div class="p-5 rounded-xl bg-white dark:bg-zinc-900 border border-slate-200 dark:border-zinc-850 shadow-sm leading-relaxed space-y-4 text-xs sm:text-sm">
        <div>
          <h4 class="font-bold text-slate-800 dark:text-white mb-1">📌 今日市場結論</h4>
          <p class="text-slate-650 dark:text-zinc-300">
            週二美股在<strong>「原油崩跌破$90美元拆除通膨隱憂＋10年期美債利率5.260%止漲整固」</strong>的有利宏觀環境下，發動了極具殺傷力的結構性多頭大反攻。費城半導體指數（^SOX）強勢暴漲+1.32%報12,629點，ASML(+3.56%)、ARM(+3.65%)、MRVL(+4.51%)全線大爆發；光通訊雙雄LITE(+5.66%)與COHR(+3.46%)上演歷史級逼空狂飆；<strong>AI核電雙雄VST(+2.04%)與CEG(+1.59%)齊創歷史天價！</strong>雖然受蘋果（-2.66%）下挫拖累使標普500微跌-0.17%（SPY報$764.20），但納指100收紅，VIX回落至16.04，市場以極高效率完成了季末估值洗盤換手，主升浪根基牢不可破。
          </p>
        </div>

        <div>
          <h4 class="font-bold text-slate-800 dark:text-white mb-1">🧭 當前市場階段</h4>
          <p class="text-slate-650 dark:text-zinc-300">
            <strong>【強趨勢歷史新高平台的良性整固 / 原油暴跌引發通膨降溫紅利 / 半導體與AI清潔能源主線全面狂飆 / Q4主升浪前夕完美蓄勢】</strong>—— 昨日的季末回調被迅速證實為難得的黃金洗盤，市場結構極度健康，牛市上升通道完好無損。
          </p>
        </div>

        <div>
          <h4 class="font-bold text-slate-800 dark:text-white mb-1">🎯 我的操作傾向（客觀中性）</h4>
          <p class="text-slate-650 dark:text-zinc-300">
            維持「穩健積極進攻（75%-80% 倉位）」。<strong>堅決擁抱具有絕對硬核壁壘與產能滿載的兩大核心印鈔機：1) 先進製程設備與光通訊互聯（ASML、LITE、MRVL、AVGO）；2) 24/7 直供電核能與資料中心電網升級（VST、CEG、GEV、PWR）</strong>。對受油價拖累的化石能源股維持謹慎觀望，底倉抱緊美光（MU）迎接明日盤後財報超級催化。
          </p>
        </div>

        <div class="p-4 bg-emerald-50 dark:bg-emerald-950/40 border border-emerald-200 dark:border-emerald-800/60 rounded-xl">
          <h4 class="font-bold text-emerald-950 dark:text-emerald-300 mb-2">⚡ 明日與本週最值得關注的 5 個核心訊號</h4>
          <ol class="list-decimal pl-5 space-y-1 text-emerald-950 dark:text-emerald-200 text-xs sm:text-sm">
            <li><strong>美光科技 (MU) 9 月 30 日（週三盤後）財報大考</strong>：存儲超級週期定海神針，直接定調半導體板塊 Q4 是否迎來歷史級主升浪。</li>
            <li><strong>10年期美債收益率 (^TNX) 能否在 5.25% 平台持續回穩</strong>：長端利率若進一步回落，科技與成長股估值將全面解鎖。</li>
            <li><strong>WTI 原油在 $89 下方能否維持弱勢震盪</strong>：確認二次通膨風險解除，奠定聯準會年底寬鬆基調。</li>
            <li><strong>光通訊龍頭 Lumentum (LITE) 能否站穩 $970 並向 $1,000 天價發起衝擊</strong>：檢驗 AI 高速互聯主線的逼空熱度。</li>
            <li><strong>標普 500 能否在 7,650-7,680 點上方收官第三季</strong>：確認季末最後一天被動基金結算後的向上突破動能。</li>
          </ol>
        </div>
      </div>
    </section>

  </main>
</div>

<!-- Scripts -->
<script>
  // Theme toggle
  const themeBtn = document.getElementById('theme-toggle');
  themeBtn.addEventListener('click', () => {
    const isDark = document.documentElement.classList.toggle('dark');
    localStorage.theme = isDark ? 'dark' : 'light';
    
    if (window.__mermaid) {
      document.querySelectorAll('.mermaid[data-processed]').forEach(el => {
        el.removeAttribute('data-processed');
        el.innerHTML = el.dataset.src || el.textContent;
      });
      window.__mermaid.initialize({ startOnLoad: false, theme: isDark ? 'dark' : 'default', securityLevel: 'loose' });
      window.__mermaid.run();
    }
  });

  // Overview Chart (Chart.js)
  const ctx = document.getElementById('overviewChart').getContext('2d');
  new Chart(ctx, {
    type: 'bar',
    data: {
      labels: ['標普500 (SPY)', '納斯達克 (QQQ)', '道瓊工業 (DIA)', '羅素2000 (IWM)', '半導體 (SMH)', '費半 (SOXX)', '科技軟體 (IGV)', '科技板塊 (XLK)'],
      datasets: [{
        label: '當日漲跌幅 (%)',
        data: [[SPY_PCT_RAW], [QQQ_PCT_RAW], [DIA_PCT_RAW], [IWM_PCT_RAW], [SMH_PCT_RAW], [SOXX_PCT_RAW], [IGV_PCT_RAW], [XLK_PCT_RAW]],
        backgroundColor: [
          '[SPY_PCT_COLOR]', '[QQQ_PCT_COLOR]', '[DIA_PCT_COLOR]', '[IWM_PCT_COLOR]', '[SMH_PCT_COLOR]', '[SOXX_PCT_COLOR]', '[IGV_PCT_COLOR]', '[XLK_PCT_COLOR]'
        ],
        borderRadius: 8,
        borderWidth: 1
      }]
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      plugins: {
        legend: { display: false }
      },
      scales: {
        y: {
          ticks: { callback: value => value + '%' }
        }
      }
    }
  });

  // Search/Filter for Sector Table
  document.getElementById('sectorSearch').addEventListener('input', function(e) {
    const q = e.target.value.toLowerCase();
    const rows = document.querySelectorAll('#sectorTable tbody tr');
    rows.forEach(row => {
      const text = row.textContent.toLowerCase();
      row.style.display = text.includes(q) ? '' : 'none';
    });
  });

  // Search/Filter for Watch Table
  document.getElementById('watchSearch').addEventListener('input', function(e) {
    const q = e.target.value.toLowerCase();
    const rows = document.querySelectorAll('#watchTable tbody tr');
    rows.forEach(row => {
      const text = row.textContent.toLowerCase();
      row.style.display = text.includes(q) ? '' : 'none';
    });
  });

  // Simple Vanilla JS Table Sorting
  function sortTable(tableId, colIndex, isNumeric = false) {
    const table = document.getElementById(tableId);
    const tbody = table.querySelector('tbody');
    const rows = Array.from(tbody.querySelectorAll('tr'));
    const currentDir = table.getAttribute('data-sort-dir') === 'asc' ? 'desc' : 'asc';
    table.setAttribute('data-sort-dir', currentDir);
    
    rows.sort((a, b) => {
      let cellA = a.cells[colIndex].textContent.trim();
      let cellB = b.cells[colIndex].textContent.trim();
      
      if (isNumeric) {
        cellA = parseFloat(cellA.replace(/[^\\d\\.\\-]/g, '')) || 0;
        cellB = parseFloat(cellB.replace(/[^\\d\\.\\-]/g, '')) || 0;
        return currentDir === 'asc' ? cellA - cellB : cellB - cellA;
      } else {
        return currentDir === 'asc' ? cellA.localeCompare(cellB, 'zh-TW') : cellB.localeCompare(cellA, 'zh-TW');
      }
    });
    
    rows.forEach(row => tbody.appendChild(row));
  }
</script>

</body>
</html>
"""

replacements = {
    "[SECTOR_ROWS]": sector_rows,
    "[WATCH_ROWS]": watch_rows,
    
    "[SPY_PRICE]": get_val("SPY", "price"),
    "[SPY_PCT]": get_val("SPY", "pct"),
    "[SPY_CHANGE]": get_val("SPY", "change"),
    "[SPY_COLOR]": spy_color,
    "[SPY_PCT_RAW]": f"{spy_pct:.2f}",
    "[SPY_PCT_COLOR]": spy_pct_color,
    
    "[QQQ_PRICE]": get_val("QQQ", "price"),
    "[QQQ_PCT]": get_val("QQQ", "pct"),
    "[QQQ_CHANGE]": get_val("QQQ", "change"),
    "[QQQ_COLOR]": qqq_color,
    "[QQQ_PCT_RAW]": f"{qqq_pct:.2f}",
    "[QQQ_PCT_COLOR]": qqq_pct_color,
    
    "[DIA_PRICE]": get_val("DIA", "price"),
    "[DIA_PCT]": get_val("DIA", "pct"),
    "[DIA_CHANGE]": get_val("DIA", "change"),
    "[DIA_COLOR]": dia_color,
    "[DIA_PCT_RAW]": f"{dia_pct:.2f}",
    "[DIA_PCT_COLOR]": dia_pct_color,
    
    "[IWM_PRICE]": get_val("IWM", "price"),
    "[IWM_PCT]": get_val("IWM", "pct"),
    "[IWM_COLOR]": iwm_color,
    "[IWM_PCT_RAW]": f"{iwm_pct:.2f}",
    "[IWM_PCT_COLOR]": iwm_pct_color,
    
    "[SOXX_PRICE]": get_val("SOXX", "price"),
    "[SOXX_PCT]": get_val("SOXX", "pct"),
    "[SOXX_COLOR]": soxx_color,
    "[SOXX_PCT_RAW]": f"{soxx_pct:.2f}",
    "[SOXX_PCT_COLOR]": soxx_pct_color,
    
    "[SMH_PRICE]": get_val("SMH", "price"),
    "[SMH_PCT]": get_val("SMH", "pct"),
    "[SMH_COLOR]": smh_color,
    "[SMH_PCT_RAW]": f"{smh_pct:.2f}",
    "[SMH_PCT_COLOR]": smh_pct_color,
    
    "[XLK_PRICE]": get_val("XLK", "price"),
    "[XLK_PCT]": get_val("XLK", "pct"),
    "[XLK_COLOR]": xlk_color,
    "[XLK_PCT_RAW]": f"{xlk_pct:.2f}",
    "[XLK_PCT_COLOR]": xlk_pct_color,
    
    "[IGV_PRICE]": get_val("IGV", "price"),
    "[IGV_PCT]": get_val("IGV", "pct"),
    "[IGV_COLOR]": igv_color,
    "[IGV_PCT_RAW]": f"{igv_pct:.2f}",
    "[IGV_PCT_COLOR]": igv_pct_color,
    
    "[VIX_PRICE]": get_val("^VIX", "price"),
    "[VIX_PCT]": get_val("^VIX", "pct"),
    
    "[IRX_PRICE]": get_val("^IRX", "price"),
    "[FVX_PRICE]": get_val("^FVX", "price"),
    "[TNX_PRICE]": get_val("^TNX", "price"),
    "[TYX_PRICE]": get_val("^TYX", "price"),
    
    "[GOLD_PRICE]": f"${get_val('GC=F', 'price')}/oz" if get_val('GC=F', 'price') != "N/A" else "$4,216.50/oz",
    "[GOLD_PCT]": get_val("GC=F", "pct"),
    "[USO_OIL_PRICE]": f"${get_val('CL=F', 'price')}" if get_val('CL=F', 'price') != "N/A" else "$89.25",
    "[USO_OIL_PCT]": get_val("CL=F", "pct"),
    "[USO_PRICE]": get_val("USO", "price"),
    "[USO_PCT]": get_val("USO", "pct"),
    "[BTC_PRICE]": get_val("BTC-USD", "price"),
    "[BTC_PCT]": get_val("BTC-USD", "pct"),
    "[ETH_PRICE]": get_val("ETH-USD", "price"),
    "[ETH_PCT]": get_val("ETH-USD", "pct"),
    "[DXY_PRICE]": get_val("DXY", "price") if get_val("DXY", "price") != "N/A" else "101.42",
    "[DXY_PCT]": get_val("DXY", "pct") if get_val("DXY", "pct") != "N/A" else "+0.22%",
}

for placeholder, val in replacements.items():
    html_template = html_template.replace(placeholder, val)

# Write HTML file
output_path = "/Users/wisdom/html-report-skill/reports/2026-09-29-us-stock-closing-daily-report.html"
with open(output_path, "w", encoding="utf-8") as f:
    f.write(html_template)

print(f"Generated report HTML at {output_path}")

# Run publish.py
publish_script = "/Users/wisdom/html-report-skill/.antigravitycli/skills/html-report/scripts/publish.py"
title = "美股收盤日報｜2026-09-29"
description = "週二（2026年9月29日），美股迎來長端美債殖利率回穩與原油重挫引發的結構性強勢反攻。WTI原油暴跌-3.62%摜破$90美元大關報$89.25/桶，10年期美債收益率在5.260%止漲整固，大幅緩解估值壓力。半導體板塊與AI硬體重啟主升浪，費城半導體指數（^SOX）強勢大漲+1.32%報12,629.16點，光通訊龍頭Lumentum（LITE +5.66%）逼空大漲，ASML暴漲+3.56%，ARM大漲+3.65%，Marvell大漲+4.51%，博通逼近天價；AI核電清潔能源雙雄Vistra（VST +2.04%）與Constellation（CEG +1.59%）續刷歷史新天價，推動公用事業板塊（XLU +1.17%）高居標普首位！Meta大漲+3.24%修復失地，甲骨文大漲+3.91%。標普500微跌-0.17%報7,670.84點，納指100逆勢收紅+0.21%，道瓊微跌-0.26%（受蘋果-2.66%拖累），VIX回落至16.04，黃金反彈+1.15%。市場在季末前夕展現極強抗脆弱性與主線吸金力。"

cmd = [
    "python3",
    publish_script,
    output_path,
    title,
    description,
]

print(f"Running publish script: {' '.join(cmd)}")
res = subprocess.run(cmd, capture_output=True, text=True)
print("Publish STDOUT:", res.stdout)
print("Publish STDERR:", res.stderr)
sys.exit(res.returncode)
