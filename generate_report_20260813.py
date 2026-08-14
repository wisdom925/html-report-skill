import os
import subprocess
import sys
import json

# Load quotes
with open("/Users/wisdom/html-report-skill/scratch/quotes_2026-08-13.json", "r", encoding="utf-8") as f:
    quotes = json.load(f)

# Helper to get formatted string for prices
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

# Prepare values
spy_pct = get_raw_val("SPY", "pct")
qqq_pct = get_raw_val("QQQ", "pct")
dia_pct = get_raw_val("DIA", "pct")
iwm_pct = get_raw_val("IWM", "pct")
soxx_pct = get_raw_val("SOXX", "pct")
vix_pct = get_raw_val("^VIX", "pct")
igv_pct = get_raw_val("IGV", "pct")
xle_pct = get_raw_val("XLE", "pct")

spy_color = "text-emerald-600 dark:text-emerald-400" if spy_pct >= 0 else "text-rose-500"
qqq_color = "text-emerald-600 dark:text-emerald-400" if qqq_pct >= 0 else "text-rose-500"
dia_color = "text-emerald-600 dark:text-emerald-400" if dia_pct >= 0 else "text-rose-500"
iwm_color = "text-emerald-600 dark:text-emerald-400" if iwm_pct >= 0 else "text-rose-500"
soxx_color = "text-emerald-600 dark:text-emerald-400" if soxx_pct >= 0 else "text-rose-500"
vix_color = "text-rose-500 font-bold" if vix_pct >= 0 else "text-emerald-600 dark:text-emerald-400"

# Sectors data for 2026-08-13
sectors = [
    {"name": "通訊服務", "etf": "XLC", "pct": get_raw_val("XLC", "pct"), "5d": "+0.90%", "1m": "-0.50%", "driver": "大型通訊巨頭 Meta（META +1.60%）大漲，推動通訊板塊收漲 1.56% 領跑大盤。"},
    {"name": "能源板塊", "etf": "XLE", "pct": get_raw_val("XLE", "pct"), "5d": "+8.00%", "1m": "+7.50%", "driver": "WTI 原油價格持穩於 $81.25，能源板塊在機構資金淨流入和油價回補的支撐下上漲 1.31%。"},
    {"name": "科技板塊", "etf": "XLK", "pct": get_raw_val("XLK", "pct"), "5d": "+5.20%", "1m": "+1.60%", "driver": "軟體 SaaS 龍頭（ADBE +4.53%、CRM +3.27%）與晶片股（AMD +2.39%、DELL +2.50%）強勢走高，抵消了光通訊板塊（LITE -5.60%、COHR -7.99%）的獲利回吐，推升板塊收漲 1.28%。"},
    {"name": "房地產板塊", "etf": "XLRE", "pct": get_raw_val("XLRE", "pct"), "5d": "+0.05%", "1m": "+1.85%", "driver": "PPI 批發通膨數據降溫加強了聯準會 9 月降息的預期，10年期美債殖利率回落至 4.64%，激勵利率敏感的房地產板塊收漲 1.18%。"},
    {"name": "非必需消費", "etf": "XLY", "pct": get_raw_val("XLY", "pct"), "5d": "+0.75%", "1m": "+1.10%", "driver": "特斯拉（TSLA +2.59%）大漲提振板塊，抵消了亞馬遜（AMZN -0.80%）的疲弱表現，板塊整體上漲 0.45%。"},
    {"name": "醫療保健", "etf": "XLV", "pct": get_raw_val("XLV", "pct"), "5d": "+3.20%", "1m": "+3.90%", "driver": "部分防禦性資金持續回流，醫藥股整體持平微升，板塊收漲 0.22%。"},
    {"name": "公用事業", "etf": "XLU", "pct": get_raw_val("XLU", "pct"), "5d": "-0.40%", "1m": "-1.80%", "driver": "重電與發電基建股如 GE Vernova（GEV +1.74%）與 OKLO（+3.10%）維持強勢，帶動板塊微漲 0.19%。"},
    {"name": "必需消費", "etf": "XLP", "pct": get_raw_val("XLP", "pct"), "5d": "+0.40%", "1m": "-0.10%", "driver": "通膨壓力減輕對必需消費品利好，板塊在平穩買氣中微升 0.10%。"},
    {"name": "金融板塊", "etf": "XLF", "pct": get_raw_val("XLF", "pct"), "5d": "+0.55%", "1m": "+1.35%", "driver": "美債殖利率回落，銀行股盤中整理，板塊微幅收漲 0.03%。"},
    {"name": "工業板塊", "etf": "XLI", "pct": get_raw_val("XLI", "pct"), "5d": "+0.21%", "1m": "+0.91%", "driver": "電網設備伊頓（ETN -1.40%）高位回調，限制了工業板塊漲幅，最終僅微漲 0.01%。"},
    {"name": "原物料板塊", "etf": "XLB", "pct": get_raw_val("XLB", "pct"), "5d": "+0.20%", "1m": "+0.70%", "driver": "大宗商品價格回落，金價下跌 -1.30% 拖累金礦與基礎材料股，XLB 收跌 0.70%。"},
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

# Watch List data for 2026-08-13
watch_list = [
    {"symbol": "NVDA", "trend": "收漲0.48%報$225.17，突破前高後高位橫盤整理，守穩短期均線", "levels": "$218.00 / $232.00", "tag": "繼續強勢"},
    {"symbol": "AMD", "trend": "收漲2.39%報$494.47，長陽突破短期均線，型態走強", "levels": "$480.00 / $510.00", "tag": "繼續強勢"},
    {"symbol": "AVGO", "trend": "收漲2.39%報$426.01，放量反彈突破均線，底部平台修復完成", "levels": "$415.00 / $435.00", "tag": "繼續強勢"},
    {"symbol": "MRVL", "trend": "收漲4.56%報$226.99，放量大漲，突破阻力區間，短線動能強勁", "levels": "$218.00 / $235.00", "tag": "繼續強勢"},
    {"symbol": "GOOGL", "trend": "微漲0.13%報$343.97，在$340關口上方築底止跌，形態企穩", "levels": "$340.00 / $355.00", "tag": "低位修復"},
    {"symbol": "MSFT", "trend": "微漲0.32%報$494.02，守住下軌支撐，高位震盪整理", "levels": "$488.00 / $505.00", "tag": "高位震盪"},
    {"symbol": "META", "trend": "大漲1.60%報$588.14，多頭重啟上攻，重新站上短線均線", "levels": "$575.00 / $600.00", "tag": "繼續強勢"},
    {"symbol": "AMZN", "trend": "收跌0.80%報$265.13，弱勢整理，考驗下軌支撐平台", "levels": "$262.00 / $272.00", "tag": "需要觀察"},
    {"symbol": "ORCL", "trend": "下跌3.69%報$147.62，創新高後獲利回吐，回踩短期均線", "levels": "$145.00 / $155.00", "tag": "回踩支撐"},
    {"symbol": "CRM", "trend": "大漲3.27%報$199.64，長陽拉升，SaaS板塊反轉信號強烈", "levels": "$192.00 / $205.00", "tag": "繼續強勢"},
    {"symbol": "NOW", "trend": "上漲1.72%報$127.09，隨軟體板塊回升，守住均線支撐", "levels": "$124.00 / $130.00", "tag": "繼續強勢"},
    {"symbol": "SNOW", "trend": "上漲1.12%報$335.98，底部放量反彈，開啟低位建構", "levels": "$328.00 / $345.00", "tag": "低位修復"},
    {"symbol": "ADBE", "trend": "暴漲4.53%報$270.47，長陽突破，啟動底部修復行情", "levels": "$260.00 / $278.00", "tag": "低位修復"},
    {"symbol": "PLTR", "trend": "上漲0.56%報$172.00，高位強勢整理，守住支撐平台", "levels": "$168.00 / $178.00", "tag": "等財報催化"},
    {"symbol": "LITE", "trend": "大跌5.60%報$880.25，暴漲後技術性回吐，回踩均線支撐", "levels": "$860.00 / $910.00", "tag": "回踩支撐"},
    {"symbol": "COHR", "trend": "大跌7.99%報$327.22，獲利盤湧出，隨板塊回撤，暫需整理", "levels": "$318.00 / $345.00", "tag": "需要觀察"},
    {"symbol": "ANET", "trend": "下跌3.27%報$203.62，高位回踩，確認前高突破有效性", "levels": "$198.00 / $212.00", "tag": "回踩支撐"},
    {"symbol": "FLNC", "trend": "下跌1.51%報$13.00，儲能板塊低位弱勢震盪", "levels": "$12.50 / $13.50", "tag": "需要觀察"},
    {"symbol": "OKLO", "trend": "上漲3.10%報$46.55，隨核能反彈，均線上方震盪整理", "levels": "$44.00 / $49.00", "tag": "繼續強勢"},
    {"symbol": "VST", "trend": "上漲1.02%報$148.18，發電龍頭多頭延續，緩步創收盤新高", "levels": "$144.00 / $152.00", "tag": "繼續強勢"},
    {"symbol": "CEG", "trend": "微跌0.09%報$278.43，高位窄幅震盪，形態健康", "levels": "$272.00 / $285.00", "tag": "高位震盪"},
    {"symbol": "ETN", "trend": "下跌1.40%報$453.52，重電龍頭高位回吐，回踩支撐", "levels": "$448.00 / $465.05", "tag": "回踩支撐"},
    {"symbol": "VRT", "trend": "上漲1.15%報$291.68，伺服器散熱需求火爆，放量創歷史收盤新高", "levels": "$284.00 / $300.00", "tag": "繼續強勢"},
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
        classes += "bg-slate-100 dark:bg-slate-800 text-slate-700 dark:text-slate-350"
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
              <td class="p-3">{item["trend"]}</td>
              <td class="p-3 font-mono">{item["levels"]}</td>
              <td class="p-3">{tag_html}</td>
            </tr>\n"""

# Format background colors for chart datasets
spy_pct_color = '#10b981' if spy_pct >= 0 else '#f43f5e'
qqq_pct_color = '#10b981' if qqq_pct >= 0 else '#f43f5e'
dia_pct_color = '#10b981' if dia_pct >= 0 else '#f43f5e'
iwm_pct_color = '#10b981' if iwm_pct >= 0 else '#f43f5e'
soxx_pct_color = '#10b981' if soxx_pct >= 0 else '#f43f5e'
igv_pct_color = '#10b981' if igv_pct >= 0 else '#f43f5e'
xle_pct_color = '#10b981' if xle_pct >= 0 else '#f43f5e'

html_content = f"""<!doctype html>
<html lang="zh-TW" class="scroll-smooth">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <title>美股收盤日報｜PPI通膨續降溫，標普再創歷史新高！科技巨頭Meta大漲，軟體SaaS全線爆發，但光通訊面臨回調，Cisco財報後大跌</title>
  <meta name="description" content="2026年8月13日美股收盤日報：美股在PPI數據超預期降溫後上攻，標普500收漲0.65%再創歷史新高，收報7,798.99點。軟體SaaS板塊大反攻，Adobe大漲4.53%，CRM大漲3.27%。然而，前日暴漲的光通訊板塊遭遇獲利回吐，Lumentum下跌5.60%，Arista跌3.27%。思科（CSCO）因保守指引大跌8.4%。">
  <meta property="og:title" content="美股收盤日報｜2026-08-13">
  <meta property="og:description" content="PPI批發通膨數據降溫強化降息預期，標普500再創歷史新高，軟體SaaS全線反彈，光通訊獲利回吐。">
  <meta property="og:type" content="article">

  <!-- Tailwind CSS & Font family -->
  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config = {{
      darkMode: 'class',
      theme: {{
        extend: {{
          colors: {{
            brand: {{
              50: '#f0f9ff',
              100: '#e0f2fe',
              500: '#0ea5e9',
              600: '#0284c7',
              700: '#0369a1',
            }}
          }},
          fontFamily: {{
            sans: ['Inter', 'Outfit', 'system-ui', '-apple-system', 'BlinkMacSystemFont', 'sans-serif']
          }}
        }}
      }}
    }};
    if (localStorage.theme === 'dark' || (!('theme' in localStorage) && matchMedia('(prefers-color-scheme: dark)').matches)) {{
      document.documentElement.classList.add('dark');
    }}
  </script>

  <!-- Highlight.js -->
  <link id="hljs-theme" rel="stylesheet" href="https://cdn.jsdelivr.net/gh/highlightjs/cdn-release@11/build/styles/github-dark.min.css">
  <script src="https://cdn.jsdelivr.net/gh/highlightjs/cdn-release@11/build/highlight.min.js"></script>

  <!-- Chart.js -->
  <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>

  <!-- Mermaid.js -->
  <script type="module">
    import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs';
    const isDark = document.documentElement.classList.contains('dark');
    mermaid.initialize({{ startOnLoad: true, theme: isDark ? 'dark' : 'default', securityLevel: 'loose' }});
    window.__mermaid = mermaid;
  </script>

  <!-- KaTeX -->
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.10/dist/katex.min.css">
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.10/dist/katex.min.js"></script>
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.10/dist/contrib/auto-render.min.js"
    onload='renderMathInElement(document.body, {{ delimiters: [
      {{left:"$$",right:"$$",display:true}},
      {{left:"$",right:"$",display:false}},
      {{left:"\\\\(",right:"\\\\)",display:false}},
      {{left:"\\\\[",right:"\\\\]",display:true}}
    ]}})'></script>

  <style>
    @media (prefers-reduced-motion: reduce) {{ * {{ animation: none !important; transition: none !important; }} }}
    @media print {{
      .no-print {{ display: none !important; }}
      body {{ color: #000; background: #fff; }}
      a {{ color: inherit; text-decoration: underline; }}
      details {{ display: block; }} details > summary {{ display: none; }}
    }}
    pre code.hljs {{ border-radius: .5rem; padding: 1rem; font-size: .85rem; }}
    details > summary {{ cursor: pointer; user-select: none; }}
    details > summary::marker {{ content: "▸ "; }}
    details[open] > summary::marker {{ content: "▾ "; }}
    
    .toc a {{ display: block; padding: .25rem 0; opacity: .6; transition: opacity .15s, color .15s; }}
    .toc a:hover, .toc a.active {{ opacity: 1; color: #0284c7; }}
    .dark .toc a:hover, .dark .toc a.active {{ color: #38bdf8; }}
    .toc a.active {{ font-weight: 600; border-left: 2px solid #0284c7; padding-left: 0.5rem; margin-left: -0.5rem; }}
    .dark .toc a.active {{ border-color: #38bdf8; }}
    
    .tabs {{ display: flex; flex-wrap: wrap; }}
    .tabs > input[type="radio"] {{ display: none; }}
    .tabs > label {{
      cursor: pointer; padding: .5rem 1.25rem;
      border-bottom: 2px solid transparent;
      font-size: .9rem; font-weight: 500;
      color: #6b7280; transition: color .15s, border-color .15s;
    }}
    .tabs > label:hover {{ color: #111; }}
    .dark .tabs > label:hover {{ color: #f4f4f5; }}
    .tabs > input:checked + label {{ border-color: #0284c7; color: #0284c7; font-weight: 600; }}
    .dark .tabs > input:checked + label {{ border-color: #38bdf8; color: #38bdf8; }}
    .tabs > .tab-panel {{ display: none; width: 100%; padding-top: 1rem; }}
    
    .tabs > input:nth-of-type(1):checked ~ .tab-panel:nth-of-type(1),
    .tabs > input:nth-of-type(2):checked ~ .tab-panel:nth-of-type(2),
    .tabs > input:nth-of-type(3):checked ~ .tab-panel:nth-of-type(3),
    .tabs > input:nth-of-type(4):checked ~ .tab-panel:nth-of-type(4) {{ display: block; }}

    th.sortable {{ cursor: pointer; user-select: none; position: relative; }}
    th.sortable::after {{ content: ' ⇅'; opacity: 0.5; font-size: 0.8em; }}
  </style>
</head>

<body class="bg-slate-50 text-slate-800 dark:bg-zinc-950 dark:text-zinc-100 transition-colors duration-200 antialiased min-h-screen">

<!-- Floating controls -->
<div class="fixed top-4 right-4 z-50 flex gap-2 no-print">
  <button id="theme-toggle" class="px-3 py-1.5 rounded-lg border border-slate-300 dark:border-zinc-700 bg-white/80 dark:bg-zinc-900/80 backdrop-blur text-sm font-medium hover:bg-slate-100 dark:hover:bg-zinc-800 transition-all shadow-sm">
    ☼ / ☾
  </button>
  <button onclick="window.print()" class="px-3 py-1.5 rounded-lg border border-slate-300 dark:border-zinc-700 bg-white/80 dark:bg-zinc-900/80 backdrop-blur text-sm font-medium hover:bg-slate-100 dark:hover:bg-zinc-800 transition-all shadow-sm">
    列印 / PDF
  </button>
</div>

<div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-10 lg:grid lg:grid-cols-[220px_minmax(0,1fr)] lg:gap-10">

  <!-- Sticky TOC -->
  <aside class="toc lg:sticky lg:top-10 self-start text-sm mb-8 lg:mb-0 no-print border-l border-slate-200 dark:border-zinc-800 pl-4 space-y-1">
    <div class="font-bold mb-3 text-slate-400 dark:text-zinc-500 uppercase tracking-wider text-xs">目錄導航</div>
    <a href="#sec-0">0. 一句話總結</a>
    <a href="#sec-1">1. 大盤表現總覽</a>
    <a href="#sec-2">2. 盤中走勢復盤</a>
    <a href="#sec-3">3. 宏觀環境</a>
    <a href="#sec-4">4. 板塊表現</a>
    <a href="#sec-5">5. 主題與風格</a>
    <a href="#sec-6">6. 市場寬度與參與度</a>
    <a href="#sec-7">7. 技術面分析</a>
    <a href="#sec-8">8. 重點個股新聞</a>
    <a href="#sec-9">9. 財報解讀日曆</a>
    <a href="#sec-10">10. 機構觀點與資金流</a>
    <a href="#sec-11">11. 板塊輪動判斷</a>
    <a href="#sec-12">12. 重點關注股觀察</a>
    <a href="#sec-13">13. 明日交易計畫</a>
    <a href="#sec-14">14. 風險提示矩陣</a>
    <a href="#sec-15">15. 最終結論</a>
  </aside>

  <!-- Main content wrapper -->
  <main class="space-y-14">

    <!-- Header Section -->
    <header class="pb-6 border-b border-slate-200 dark:border-zinc-800">
      <div class="flex items-center gap-2 text-xs text-sky-600 dark:text-sky-400 font-semibold tracking-wider uppercase mb-2">
        <span>Daily Market Analysis</span>
        <span>•</span>
        <span>美股交易日：<strong>2026-08-13</strong></span>
      </div>
      <h1 class="text-3xl font-extrabold tracking-tight text-slate-900 dark:text-white sm:text-4xl mb-4 font-sans">
        美股收盤日報｜PPI通膨續降溫，標普再創歷史新高！科技巨頭Meta大漲，軟體SaaS全線爆發，但光通訊面臨回調，Cisco財報後大跌！
      </h1>
      <p class="text-base text-slate-500 dark:text-zinc-400 leading-relaxed max-w-4xl font-sans">
        週四（2026年8月13日），美股大盤在美國7月PPI批發通膨數據超預期溫和降溫後持續走高，市場對降息路徑充滿信心。標普500指數收漲0.65%（報7,798.99點），盤中與收盤同步再創歷史新高；納斯達克綜合指數上漲0.81%，道瓊工業指數小幅上漲0.13%，小盤股Russell 2000上漲0.25%。軟體SaaS板塊出現報復性大反彈，Adobe（ADBE）暴漲4.53%，Salesforce（CRM）大漲3.27%，ServiceNow（NOW）上漲1.72%。大型科技股以Meta（META）上揚1.60%及特斯拉（TSLA）大漲2.59%為首。然而，前日暴漲的光通訊板塊遭遇顯著的「利多出盡」獲利回吐，Lumentum（LITE）大跌5.60%，Arista（ANET）下跌3.27%，Coherent（COHR）重挫7.99%。同時思科（CSCO）因發布保守指引在財報公佈後暴跌8.4%。
      </p>
    </header>

    <!-- 0. 今日一句話總結 -->
    <section id="sec-0" class="scroll-mt-6 font-sans">
      <h2 class="text-xl font-bold mb-4 flex items-center gap-2 border-b border-slate-100 dark:border-zinc-850 pb-2">
        <span class="text-brand-500">0.</span> 今日一句話總結
      </h2>
      <div class="p-5 rounded-xl bg-white dark:bg-zinc-900 border border-slate-200 dark:border-zinc-800/80 shadow-sm leading-relaxed space-y-3">
        <ul class="list-disc pl-5 space-y-2 text-slate-600 dark:text-zinc-300 text-sm sm:text-base">
          <li><strong>大盤狀態</strong>：PPI數據溫和激勵多頭買盤，標普再創歷史收盤新高，三大指數全線收高，市場呈現穩健的 Risk-on 狀態。</li>
          <li><strong>驅動因素</strong>：7月 PPI 環比持平（0.0%）低於預期，核心 PPI 同比降至 4.7%，顯示通膨正受控制；美債殖利率下降，提振了利率敏感的軟體與房地產板塊。</li>
          <li><strong>資金態度</strong>：資金從前日過熱的光通訊板塊（LITE、COHR）中流出，精準輪動到估值較具性價比的軟體 SaaS（ADBE、CRM）及電力 GEV，寬度逐步擴散。</li>
        </ul>
        <div class="p-3.5 bg-emerald-50 dark:bg-emerald-950/40 border border-emerald-250 dark:border-emerald-805/50 rounded-lg text-emerald-800 dark:text-emerald-300 text-xs sm:text-sm font-semibold">
          ✅ 今日市場狀態：指數創高、寬度健康，SaaS與晶片龍頭再度走強，高位光網絡板塊適度回調，整體多頭趨勢不變。
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
          <div class="text-lg sm:text-xl font-bold {spy_color}">{get_val("SPY", "price")}</div>
          <div class="text-xs font-semibold mt-1 {spy_color}">{get_val("SPY", "pct")} ({get_val("SPY", "change")} 點)</div>
        </div>
        <div class="p-4 rounded-xl bg-white dark:bg-zinc-900 border border-slate-200 dark:border-zinc-800/80 shadow-sm">
          <div class="text-xs text-slate-400 dark:text-zinc-500 font-semibold mb-1">Nasdaq 100 (QQQ)</div>
          <div class="text-lg sm:text-xl font-bold {qqq_color}">{get_val("QQQ", "price")}</div>
          <div class="text-xs font-semibold mt-1 {qqq_color}">{get_val("QQQ", "pct")} ({get_val("QQQ", "change")} 點)</div>
        </div>
        <div class="p-4 rounded-xl bg-white dark:bg-zinc-900 border border-slate-200 dark:border-zinc-800/80 shadow-sm">
          <div class="text-xs text-slate-400 dark:text-zinc-500 font-semibold mb-1">Dow Jones (DIA)</div>
          <div class="text-lg sm:text-xl font-bold {dia_color}">{get_val("DIA", "price")}</div>
          <div class="text-xs font-semibold mt-1 {dia_color}">{get_val("DIA", "pct")} ({get_val("DIA", "change")} 點)</div>
        </div>
        <div class="p-4 rounded-xl bg-white dark:bg-zinc-900 border border-slate-200 dark:border-zinc-800/80 shadow-sm">
          <div class="text-xs text-slate-400 dark:text-zinc-500 font-semibold mb-1">Russell 2000 (IWM) / VIX</div>
          <div class="text-lg sm:text-xl font-bold {iwm_color}">{get_val("IWM", "price")}</div>
          <div class="text-xs font-semibold mt-1 {vix_color}">{get_val("IWM", "pct")} (VIX: {get_val("VIX", "price")})</div>
        </div>
      </div>

      <div class="p-5 rounded-xl bg-white dark:bg-zinc-900 border border-slate-200 dark:border-zinc-800/80 shadow-sm">
        <h3 class="text-sm font-semibold text-slate-700 dark:text-zinc-300 mb-4">主要指數與 ETF 當日漲跌幅對比 (%)</h3>
        <div class="h-64 sm:h-80 relative">
          <canvas id="overviewChart"></canvas>
        </div>
      </div>
    </section>

    <!-- 2. 盤中走勢復盤 -->
    <section id="sec-2" class="scroll-mt-6 font-sans">
      <h2 class="text-xl font-bold mb-4 flex items-center gap-2 border-b border-slate-100 dark:border-zinc-850 pb-2">
        <span class="text-brand-500">2.</span> 盤中走勢復盤
      </h2>
      <div class="p-5 rounded-xl bg-white dark:bg-zinc-900 border border-slate-200 dark:border-zinc-800/80 shadow-sm space-y-6">
        <div class="mermaid flex justify-center py-2">
          timeline
            title 2026-08-13 盤中走勢大事記
            盤前階段 : 盤前 8:30 公布美國 7 月 PPI 生產者物價指數，環比為 0.0% 低於市場預期的 0.2%，核心 PPI 下探 0.2% 同樣溫和。美債 10 年期殖利率應聲下跌至 4.64%，三大期指跳高。
            開盤走勢 : 標普500指數高開高走，特斯拉（TSLA）及 Meta 強勢反彈。然而思科（CSCO）盤前公佈財報後暴跌 8%，拖累網路設備板塊。
            早盤交易 : 資金開始輪動，從昨日暴漲的 Lumentum (LITE) 和 Arista (ANET) 等光通訊股流出，大幅湧入超跌的軟體 SaaS 板塊，Adobe（ADBE）漲幅超過 4%。
            午盤波動 : 大盤在高位持穩，標普 500 指數重啟升勢，突破前日高點，再創歷史新高。能源板塊（XLE）在大宗商品買盤支撐下放量走高。
            尾盤收盤 : 尾盤多頭維持優勢，標普收報 7,798.99 點，創下收盤新高。思科最終收跌 8.4%。光通訊板塊（LITE -5.60%）跌幅有所收斂，以回踩支撐為主。
        </div>
        <p class="text-sm text-slate-500 dark:text-zinc-400 leading-relaxed">
          <strong>復盤解析：</strong>今日盤面呈現非常健康的「良性板塊輪動」。盤前 PPI 批發通膨數據的降溫，進一步加深了市場對 9 月降息的把握。殖利率的滑落直接解鎖了高估值板塊的買氣，特別是先前承壓的軟體 SaaS 板塊（ADBE +4.53%、CRM +3.27%），今日吸引了大量避險與估值回補資金。同時，昨日創下歷史新高的 Arista（ANET）及光通訊龍頭 Lumentum（LITE）則在開盤後引來獲利回吐盤，資金呈階段性休整。然而，這並不代表 AI 主線崩潰，而是資金靈活流向性價比更高的軟體端與算力電力基建（GEV、OKLO）。尾盤收高反映出多頭格局依舊佔據主導。
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
        <label for="tab-fed">3.2 Fed 降息預期</label>
        
        <input type="radio" id="tab-commodities" name="macro-tabs">
        <label for="tab-commodities">3.3 大宗與加密</label>
        
        <input type="radio" id="tab-data" name="macro-tabs">
        <label for="tab-data">3.4 重要經濟數據</label>
        
        <!-- Tab panel 1 -->
        <div class="tab-panel text-sm text-slate-655 dark:text-zinc-300 leading-relaxed bg-white dark:bg-zinc-900 p-5 rounded-xl border border-slate-200 dark:border-zinc-800/80 mt-2">
          <h4 class="font-bold text-slate-800 dark:text-white mb-2">PPI數據溫和引導國債殖利率下行，長端債息趨勢走軟</h4>
          <p class="mb-3">
            在生產者物價指數（PPI）如預期走低後，美債殖利率面臨下行壓力：
          </p>
          <ul class="list-disc pl-5 space-y-1 font-mono text-xs sm:text-sm">
            <li><strong>5年期國債殖利率 (FVX)</strong>：收報 <strong>{get_raw_val("^FVX", "price")}%</strong>，日跌 -0.91%（至 4.34%）。</li>
            <li><strong>10年期國債殖利率 (TNX)</strong>：收報 <strong>{get_raw_val("^TNX", "price")}%</strong>，跌 -0.85%（至 4.64%）。</li>
            <li><strong>30年期國債殖利率 (TYX)</strong>：收報 <strong>{get_raw_val("^TYX", "price")}%</strong>，跌 -0.38%（至 5.23%）。</li>
          </ul>
          <p class="mt-3 text-slate-500 text-xs font-sans">
            殖利率全面回落，解除市場對通膨頑固的擔憂。國債殖利率的下行直接為高倍數的 SaaS 軟體與地產股釋放了估值壓力。
          </p>
        </div>
        
        <!-- Tab panel 2 -->
        <div class="tab-panel text-sm text-slate-655 dark:text-zinc-300 leading-relaxed bg-white dark:bg-zinc-900 p-5 rounded-xl border border-slate-200 dark:border-zinc-800/80 mt-2">
          <h4 class="font-bold text-slate-800 dark:text-white mb-2">9月預期暫停加息或降息機率趨於穩健</h4>
          <p class="mb-3">
            延續昨日 CPI 的利好，今日溫和的 PPI 進一步固化了降息預期：
          </p>
          <ul class="list-disc pl-5 space-y-1">
            <li><strong>利率目標區間機率 (CME FedWatch)</strong>：9月份暫停利率變更（維持政策穩定）的機率上升至 <strong>65.0%</strong>，市場預期聯準會將採取更具彈性的貨幣政策，避免實體經濟過度承壓。</li>
            <li><strong>背景解析</strong>：年內預期降息次數穩健維持在 2 次左右。在經濟數據不差且通膨逐步受控的背景下，「軟著陸」的底層敘事在華爾街得到了進一步的認同。</li>
          </ul>
        </div>
        
        <!-- Tab panel 3 -->
        <div class="tab-panel text-sm text-slate-655 dark:text-zinc-300 leading-relaxed bg-white dark:bg-zinc-900 p-5 rounded-xl border border-slate-200 dark:border-zinc-855 mt-2">
          <h4 class="font-bold text-slate-800 dark:text-white mb-2">美元持穩，黃金高位回落，比特幣震盪</h4>
          <p class="mb-3">
            宏觀通膨定價落地後，大宗商品及加密貨幣走勢如下：
          </p>
          <ul class="list-disc pl-5 space-y-2">
            <li><strong>黃金現貨 (GLD)</strong>：<strong>下跌 -1.30%</strong> 報 399.66 美元，受多頭短線獲利了結與通膨預期下滑影響。</li>
            <li><strong>原油 (USO)</strong>：<strong>下跌 -0.63%</strong> 報 126.50 美元，WTI原油微跌至 $81.25/桶，地緣風險溢價稍微收窄。</li>
            <li><strong>美元指數 (DXY)</strong>：<strong>持平</strong> 於 99.95，UUP 收於 28.20，市場情緒轉向穩定。</li>
            <li><strong>比特幣 (BTC-USD)</strong>：微跌 -0.19% 報 63,408.00 美元；以太坊 (ETH-USD) 反彈 <strong>+0.92%</strong> 報 1,897.00 美元。</li>
          </ul>
        </div>
        
        <!-- Tab panel 4 -->
        <div class="tab-panel text-sm text-slate-655 dark:text-zinc-300 leading-relaxed bg-white dark:bg-zinc-900 p-5 rounded-xl border border-slate-200 dark:border-zinc-800/80 mt-2">
          <h4 class="font-bold text-slate-800 dark:text-white mb-2">美國 7 月 PPI 經濟數據發布詳情</h4>
          <div class="overflow-x-auto my-3">
            <table class="min-w-full text-xs font-mono text-left">
              <thead>
                <tr class="bg-slate-100 dark:bg-zinc-800 text-slate-700 dark:text-zinc-300">
                  <th class="p-2 border-b">數據項目</th>
                  <th class="p-2 border-b">實際值 (2026-08-13)</th>
                  <th class="p-2 border-b">市場預期值</th>
                  <th class="p-2 border-b">前值 (6月)</th>
                  <th class="p-2 border-b">市場解讀</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td class="p-2 border-b font-sans font-semibold">7月 PPI 年率 (YoY)</td>
                  <td class="p-2 border-b font-bold text-emerald-600">4.7%</td>
                  <td class="p-2 border-b">4.9%</td>
                  <td class="p-2 border-b">5.5%</td>
                  <td class="p-2 border-b font-sans">低於預期。較前值大幅放緩，批發端通膨明顯降溫。</td>
                </tr>
                <tr>
                  <td class="p-2 border-b font-sans font-semibold">7月 PPI 月率 (MoM)</td>
                  <td class="p-2 border-b font-bold text-emerald-600">0.0%</td>
                  <td class="p-2 border-b">0.2%</td>
                  <td class="p-2 border-b">0.2%</td>
                  <td class="p-2 border-b font-sans">大幅優於預期。環比無增長，意味著未來消費端CPI具備進一步下行基礎。</td>
                </tr>
                <tr>
                  <td class="p-2 border-b font-sans font-semibold">7月 核心PPI月率 (YoY)</td>
                  <td class="p-2 border-b font-bold text-emerald-600">0.2%</td>
                  <td class="p-2 border-b">0.3%</td>
                  <td class="p-2 border-b">0.4%</td>
                  <td class="p-2 border-b font-sans">符合預期。顯示工廠端原材料與核心服務成本擴張有所收縮。</td>
                </tr>
              </tbody>
            </table>
          </div>
          <p class="text-xs text-slate-500 mt-2 font-sans">
            <strong>宏觀解讀：</strong>PPI數據是一次「通膨溫和」的強力佐證。CPI和PPI的雙重降溫，為市場下半年降息與美股多頭的延續鋪平了道路。
          </p>
        </div>
      </div>
    </section>

    <!-- 4. 板塊表現 -->
    <section id="sec-4" class="scroll-mt-6 font-sans">
      <h2 class="text-xl font-bold mb-4 flex items-center gap-2 border-b border-slate-100 dark:border-zinc-850 pb-2">
        <span class="text-brand-500">4.</span> 板塊表現
      </h2>
      
      <div class="mb-4 flex flex-col sm:flex-row gap-2 no-print">
        <input type="text" id="sectorSearch" placeholder="搜尋板塊名稱或代碼..." class="px-4 py-2 text-sm rounded-lg border border-slate-300 dark:border-zinc-800 bg-white dark:bg-zinc-900 focus:outline-none focus:ring-2 focus:ring-sky-500 w-full sm:w-72">
      </div>

      <div class="p-5 rounded-xl bg-white dark:bg-zinc-900 border border-slate-200 dark:border-zinc-800/80 shadow-sm overflow-x-auto">
        <table class="w-full text-left text-sm text-slate-650 dark:text-zinc-300" id="sectorTable" data-sort-dir="none">
          <thead class="text-xs uppercase bg-slate-150 dark:bg-zinc-800 text-slate-700 dark:text-zinc-200">
            <tr>
              <th class="p-3 sortable" onclick="sortTable('sectorTable', 0, true)">排名</th>
              <th class="p-3 sortable" onclick="sortTable('sectorTable', 1)">板塊</th>
              <th class="p-3 sortable" onclick="sortTable('sectorTable', 2)">ETF</th>
              <th class="p-3 sortable" onclick="sortTable('sectorTable', 3, true)">當日漲跌幅</th>
              <th class="p-3 sortable" onclick="sortTable('sectorTable', 4, true)">近5日</th>
              <th class="p-3 sortable" onclick="sortTable('sectorTable', 5, true)">近1月</th>
              <th class="p-3">跑贏/跑輸標普</th>
              <th class="p-3">主要驅動</th>
            </tr>
          </thead>
          <tbody class="divide-y divide-slate-200 dark:divide-zinc-800">
{sector_rows}          </tbody>
        </table>
      </div>
      <p class="text-xs text-slate-400 dark:text-zinc-500 font-semibold mt-2">* 點擊表頭可以對各列數據進行排序。數據已去除偏離空值。</p>
    </section>

    <!-- 5. 主題與風格 -->
    <section id="sec-5" class="scroll-mt-6 font-sans">
      <h2 class="text-xl font-bold mb-4 flex items-center gap-2 border-b border-slate-100 dark:border-zinc-850 pb-2">
        <span class="text-brand-500">5.</span> 主題與風格表現
      </h2>
      <div class="p-5 rounded-xl bg-white dark:bg-zinc-900 border border-slate-200 dark:border-zinc-800/80 shadow-sm leading-relaxed text-sm text-slate-655 dark:text-zinc-300 space-y-4">
        <p>
          今日市場風格呈現<strong>「軟體SaaS大爆發、半導體晶片股穩健上揚、光通訊板塊高位劇烈回調、思科拖累網路設備」</strong>的特徵：
        </p>
        <ul class="list-disc pl-5 space-y-2">
          <li><strong>軟體與 SaaS (IGV)</strong>：強勢崛起，IGV 大漲 <strong>+1.50%</strong>。Adobe（ADBE）大漲 <strong>+4.53%</strong>，Salesforce（CRM）暴漲 <strong>+3.27%</strong>，SaaS板塊出現底部反轉信號。</li>
          <li><strong>晶片與半導體 (SOXX/SMH)</strong>：延續漲勢，SOXX 上揚 <strong>+0.76%</strong>，SMH 上漲 <strong>+0.72%</strong>。超微（AMD +2.39%）與博通（AVGO +2.39%）大幅修復均線，戴爾（DELL +2.50%）續創新高。</li>
          <li><strong>光通訊與 AI 高速互聯 (LITE/COHR/ANET)</strong>：高位承壓回退。Lumentum (LITE) 獲利了結大跌 <strong>-5.60%</strong>，Coherent (COHR) 大跌 <strong>-7.99%</strong>，Arista (ANET) 回踩短期均線收跌 <strong>-3.27%</strong>。</li>
          <li><strong>網路設備與企業 IT (CSCO)</strong>：思科因發布保守季度指引大跌 <strong>-8.40%</strong>，拖累部分硬體估值。</li>
        </ul>
      </div>
    </section>

    <!-- 6. 市場寬度與參與度 -->
    <section id="sec-6" class="scroll-mt-6 font-sans">
      <h2 class="text-xl font-bold mb-4 flex items-center gap-2 border-b border-slate-100 dark:border-zinc-850 pb-2">
        <span class="text-brand-500">6.</span> 市場寬度與參與度
      </h2>
      <div class="grid grid-cols-1 md:grid-cols-3 gap-6 text-xs sm:text-sm">
        <div class="p-5 rounded-xl bg-white dark:bg-zinc-900 border border-slate-200 dark:border-zinc-800/80 shadow-sm space-y-3">
          <h4 class="font-bold text-slate-800 dark:text-white flex items-center gap-1.5">
            <span class="w-2.5 h-2.5 rounded-full bg-yellow-500"></span> 均線參與度
          </h4>
          <ul class="space-y-2 font-mono">
            <li class="flex justify-between"><span>標普500高於50MA比例：</span><span class="font-semibold text-emerald-600">62.8%</span></li>
            <li class="flex justify-between"><span>納指100高於50MA比例：</span><span class="font-semibold text-emerald-600">56.5%</span></li>
            <li class="flex justify-between"><span>標普500高於200MA比例：</span><span class="font-semibold text-emerald-600">68.5%</span></li>
          </ul>
          <p class="text-slate-400 text-xs font-sans">多數股票位於中期均線之上，市場上漲結構健康，並非輝達單隻股票的獨角戲。</p>
        </div>

        <div class="p-5 rounded-xl bg-white dark:bg-zinc-900 border border-slate-200 dark:border-zinc-800/80 shadow-sm space-y-3">
          <h4 class="font-bold text-slate-800 dark:text-white flex items-center gap-1.5">
            <span class="w-2.5 h-2.5 rounded-full bg-yellow-500"></span> 漲跌家數與新高/新低
          </h4>
          <ul class="space-y-2 font-mono">
            <li class="flex justify-between"><span>NYSE 漲/跌家數：</span><span>1,820 / 1,210</span></li>
            <li class="flex justify-between"><span>Nasdaq 漲/跌家數：</span><span>2,530 / 1,690</span></li>
            <li class="flex justify-between"><span>NYSE 52周新高/新低：</span><span>62 / 10</span></li>
            <li class="flex justify-between"><span>Nasdaq 52周新高/新低：</span><span>51 / 18</span></li>
          </ul>
          <p class="text-slate-400 text-xs font-sans">多頭交易所上漲家數擴大，52週新高比新低顯著多，顯示資金做多動能依然充沛。</p>
        </div>

        <div class="p-5 rounded-xl bg-white dark:bg-zinc-900 border border-slate-200 dark:border-zinc-800/80 shadow-sm space-y-3">
          <h4 class="font-bold text-slate-800 dark:text-white flex items-center gap-1.5">
            <span class="w-2.5 h-2.5 rounded-full bg-yellow-500"></span> 內部指標觀察
          </h4>
          <ul class="space-y-2 font-mono">
            <li class="flex justify-between"><span>McClellan Oscillator：</span><span class="font-semibold text-emerald-600">+15</span></li>
            <li class="flex justify-between"><span>Put/Call Ratio：</span><span class="font-semibold text-emerald-600">0.62</span></li>
            <li class="flex justify-between"><span>VIX 期限結構：</span><span class="font-semibold text-emerald-600">平穩，VIX維持在14.69</span></li>
          </ul>
          <p class="text-slate-400 text-xs font-sans">麥克連指標進一步走強，期權PCR比值偏低，市場避險投機意願維持低谷。</p>
        </div>
      </div>
    </section>

    <!-- 7. 技術面分析 -->
    <section id="sec-7" class="scroll-mt-6 font-sans">
      <h2 class="text-xl font-bold mb-4 flex items-center gap-2 border-b border-slate-100 dark:border-zinc-850 pb-2">
        <span class="text-brand-500">7.</span> 技術面分析
      </h2>
      <div class="p-5 rounded-xl bg-white dark:bg-zinc-900 border border-slate-200 dark:border-zinc-800/80 shadow-sm overflow-x-auto">
        <table class="w-full text-left text-sm text-slate-655 dark:text-zinc-300" id="techTable">
          <thead class="text-xs uppercase bg-slate-150 dark:bg-zinc-800 text-slate-700 dark:text-zinc-200">
            <tr>
              <th class="p-3">指數 / ETF</th>
              <th class="p-3 font-mono">收盤價格</th>
              <th class="p-3 font-mono">20日均線</th>
              <th class="p-3 font-mono">50日均線</th>
              <th class="p-3 font-mono">RSI (14)</th>
              <th class="p-3">MACD狀態</th>
              <th class="p-3">關鍵支撐 / 壓力</th>
            </tr>
          </thead>
          <tbody class="divide-y divide-slate-200 dark:divide-zinc-800 font-mono text-xs sm:text-sm">
            <tr class="hover:bg-slate-50 dark:hover:bg-zinc-800/30">
              <td class="p-3 font-semibold font-sans">SPY (標普500 ETF)</td>
              <td class="p-3 font-bold text-emerald-600">{get_val("SPY", "price")}</td>
              <td class="p-3">762.30</td>
              <td class="p-3">752.40</td>
              <td class="p-3">63</td>
              <td class="p-3 text-emerald-600 font-sans">收盤創歷史新高，均線呈現完美多頭排列</td>
              <td class="p-3">772.00 / 785.00</td>
            </tr>
            <tr class="hover:bg-slate-50 dark:hover:bg-zinc-800/30">
              <td class="p-3 font-semibold font-sans">QQQ (納指100 ETF)</td>
              <td class="p-3 font-bold text-emerald-600">{get_val("QQQ", "price")}</td>
              <td class="p-3">714.20</td>
              <td class="p-3">714.90</td>
              <td class="p-3">59</td>
              <td class="p-3 text-emerald-600 font-sans">突破並站穩50日均線，短期趨勢重回強勢</td>
              <td class="p-3">724.00 / 740.00</td>
            </tr>
            <tr class="hover:bg-slate-50 dark:hover:bg-zinc-800/30">
              <td class="p-3 font-semibold font-sans">IWM (羅素2000 ETF)</td>
              <td class="p-3 font-bold text-emerald-600">{get_val("IWM", "price")}</td>
              <td class="p-3">297.10</td>
              <td class="p-3">290.00</td>
              <td class="p-3">59</td>
              <td class="p-3 font-sans text-emerald-600">小幅攀升，守穩短期上升通道下軌</td>
              <td class="p-3">299.00 / 309.00</td>
            </tr>
            <tr class="hover:bg-slate-50 dark:hover:bg-zinc-800/30">
              <td class="p-3 font-semibold font-sans">SMH (費半半導體 ETF)</td>
              <td class="p-3 text-emerald-600 font-bold">{get_val("SMH", "price")}</td>
              <td class="p-3">563.40</td>
              <td class="p-3">548.10</td>
              <td class="p-3">58</td>
              <td class="p-3 font-sans text-emerald-600">長陽反彈後高位整固，均線支撐依然強大</td>
              <td class="p-3">580.00 / 602.00</td>
            </tr>
            <tr class="hover:bg-slate-50 dark:hover:bg-zinc-800/30">
              <td class="p-3 font-semibold font-sans">IGV (科技軟體 ETF)</td>
              <td class="p-3 font-bold text-emerald-600">{get_val("IGV", "price")}</td>
              <td class="p-3">101.20</td>
              <td class="p-3">97.10</td>
              <td class="p-3">59</td>
              <td class="p-3 text-emerald-600 font-sans">大反彈並吞併前日陰線，突破高位平台阻力</td>
              <td class="p-3">102.50 / 107.00</td>
            </tr>
            <tr class="hover:bg-slate-50 dark:hover:bg-zinc-800/30">
              <td class="p-3 font-semibold font-sans">XLK (科技 ETF)</td>
              <td class="p-3 text-emerald-600 font-bold">{get_val("XLK", "price")}</td>
              <td class="p-3">185.10</td>
              <td class="p-3">180.10</td>
              <td class="p-3">62</td>
              <td class="p-3 font-sans text-emerald-600">連續兩日大漲，技術指標呈現突破前高姿態</td>
              <td class="p-3">188.00 / 195.00</td>
            </tr>
          </tbody>
        </table>
      </div>
      <p class="text-xs text-slate-500 dark:text-zinc-400 mt-3 leading-relaxed">
        <strong>技術評語：</strong>標普指數（SPY +0.70%）在 PPI 數據後強勢上行並創下收盤新高。QQQ 收復並企穩 50MA（714.90），確認短期多頭結構已經修復。軟體板塊（IGV +1.50%）出現長陽包絡，顯示出強烈的資金回流跡象，是今日最強的主題。半導體（SMH）在高位穩定整理。目前多頭結構穩健，應維持逢低做多操作。
      </p>
    </section>

    <!-- 8. 重點個股新聞與異動 -->
    <section id="sec-8" class="scroll-mt-6 font-sans">
      <h2 class="text-xl font-bold mb-4 flex items-center gap-2 border-b border-slate-100 dark:border-zinc-850 pb-2">
        <span class="text-brand-500">8.</span> 重點個股新聞與異動
      </h2>
      <div class="space-y-4">
        
        <details class="group bg-white dark:bg-zinc-900 p-4 rounded-xl border border-slate-200 dark:border-zinc-800" open>
          <summary class="font-bold text-slate-800 dark:text-white flex justify-between items-center text-sm sm:text-base">
            <span>8.1 大型科技七巨頭 (Magnificent 7)</span>
          </summary>
          <div class="mt-3 text-sm space-y-3 leading-relaxed text-slate-655 dark:text-zinc-350 font-sans">
            <p><strong>META (Meta) +1.60%</strong>：收報 $588.14。隨大盤科技板塊大漲，多頭重啟上攻，重新站穩均線，技術型態極佳。</p>
            <p><strong>TSLA (特斯拉) +2.59%</strong>：收報 $335.99。放量突破 10MA，馬斯克宏觀政策預期與散戶情緒共振提振股價。</p>
            <p><strong>AAPL (蘋果) +0.37%</strong>：收報 $303.38。守穩 10MA，緩步上升，維持健康的多頭排列。</p>
            <p><strong>NVDA (輝達) +0.48%</strong>：收報 $225.17。股價突破均線阻力後高位窄幅震盪，守穩 $220，蓄勢整理。</p>
            <p><strong>MSFT (微軟) +0.32%</strong>：收報 $494.02。回踩短期均線後企穩反彈，多空在 $495 附近暫時達到平衡。</p>
            <p><strong>AMZN (亞馬遜) -0.80%</strong>：收報 $265.13。貝佐斯售股餘波未平，股價持續走弱探底，考驗 $260 支撐。</p>
            <p><strong>GOOGL (Alphabet) +0.13%</strong>：收報 $343.97。低位窄幅整理，守穩 $340 關卡。</p>
          </div>
        </details>

        <details class="group bg-white dark:bg-zinc-900 p-4 rounded-xl border border-slate-200 dark:border-zinc-800">
          <summary class="font-bold text-slate-800 dark:text-white flex justify-between items-center text-sm sm:text-base">
            <span>8.2 AI 硬體 / 半導體重點股異動分析</span>
          </summary>
          <div class="mt-3 text-sm space-y-3 leading-relaxed text-slate-655 dark:text-zinc-350">
            <p><strong>MRVL (馬威爾) +4.56%</strong>：收報 $226.99。受 AI 光電晶片出貨超預期與光互聯升級利多提振，放量暴漲，突破阻力區間。</p>
            <p><strong>DELL (戴爾) +2.50%</strong>：收報 $496.61。AI 伺服器積壓訂單強勁，股價連日攀升，向 $500 大關邁進。</p>
            <p><strong>AMD (超微) +2.39%</strong>：收報 $494.47。長陽拉升，突破中短期均線，形態走強。</p>
            <p><strong>AVGO (博通) +2.39%</strong>：收報 $426.01。底部分批買盤浮現，大漲收復均線，底部整理完成。</p>
            <p><strong>LITE (Lumentum) -5.60% / COHR (Coherent) -7.99%</strong>：前日暴漲的光模組雙雄遭遇劇烈獲利了結。LITE 下滑至 $880.25，COHR 下跌至 $327.22，主要是「利好兌現」後的正常回調。</p>
            <p><strong>ANET (Arista) -3.27%</strong>：收報 $203.62。創新高後回調，回踩 20MA 平台。</p>
          </div>
        </details>

        <details class="group bg-white dark:bg-zinc-900 p-4 rounded-xl border border-slate-200 dark:border-zinc-800">
          <summary class="font-bold text-slate-800 dark:text-white flex justify-between items-center text-sm sm:text-base">
            <span>8.3 軟體 / SaaS / AI 應用重點股異動分析</span>
          </summary>
          <div class="mt-3 text-sm space-y-3 leading-relaxed text-slate-655 dark:text-zinc-350">
            <p><strong>ADBE (Adobe) +4.53%</strong>：收報 $270.47。利率走低提振軟體估值，買盤大舉湧入超跌的 AI 創意設計龍頭，收復多條均線。</p>
            <p><strong>CRM (Salesforce) +3.27%</strong>：收報 $199.64。大漲收復失地，帶動整個雲端 SaaS 軟體反攻。</p>
            <p><strong>NOW (ServiceNow) +1.72%</strong>：收報 $127.09。形態健康，長陽反包前日跌幅。</p>
            <p><strong>ORCL (甲骨文) -3.69%</strong>：收報 $147.62。新高後遭遇獲利回吐，回踩均線平台。</p>
          </div>
        </details>

        <details class="group bg-white dark:bg-zinc-900 p-4 rounded-xl border border-slate-200 dark:border-zinc-800">
          <summary class="font-bold text-slate-800 dark:text-white flex justify-between items-center text-sm sm:text-base">
            <span>8.4 AI 電力 / 資料中心 / 能源基礎設施重點股分析</span>
          </summary>
          <div class="mt-3 text-sm space-y-3 leading-relaxed text-slate-655 dark:text-zinc-350">
            <p><strong>OKLO (奧克洛) +3.10%</strong>：收報 $46.55。小型核能概念股隨板塊企穩反彈，維持在短期均線之上。</p>
            <p><strong>GEV (GE Vernova) +1.74%</strong>：收報 $1,058.04。電網重電需求極為火熱，股價再度拉升創歷史新高。</p>
            <p><strong>VRT (Vertiv) +1.15%</strong>：收報 $291.68。液冷散熱龍頭買氣不減，股價再創歷史收盤新高。</p>
            <p><strong>ETN (伊頓) -1.40% / CEG (星座能源) -0.09%</strong>：ETN高位獲利回吐回調；CEG在均線附近橫盤整理。</p>
          </div>
        </details>

        <details class="group bg-white dark:bg-zinc-900 p-4 rounded-xl border border-slate-200 dark:border-zinc-800">
          <summary class="font-bold text-slate-800 dark:text-white flex justify-between items-center text-sm sm:text-base">
            <span>8.5 其他顯著大漲/大跌的股票與異動原因</span>
          </summary>
          <div class="mt-3 text-sm space-y-3 leading-relaxed text-slate-655 dark:text-zinc-350">
            <p><strong>CSCO (思科) -8.40%</strong>：思科第四財季業績勉強符合預期，但給予的第一財季指引中值顯得保守，管理層表示非 AI 企業網通產品庫存去化速度慢於預期，引發股價在週四交易日暴跌 8.40%。</p>
          </div>
        </details>
      </div>
    </section>

    <!-- 9. 財報解讀日曆 -->
    <section id="sec-9" class="scroll-mt-6 font-sans">
      <h2 class="text-xl font-bold mb-4 flex items-center gap-2 border-b border-slate-100 dark:border-zinc-850 pb-2">
        <span class="text-brand-500">9.</span> 財報解讀日曆
      </h2>
      <div class="space-y-6">
        <div>
          <h3 class="text-lg font-semibold mb-3">9.1 當日已公佈財報的重點公司解讀</h3>
          <div class="space-y-4">
            <div class="p-5 rounded-xl bg-white dark:bg-zinc-900 border border-slate-200 dark:border-zinc-800/80 shadow-sm">
              <h4 class="font-bold text-slate-900 dark:text-white flex justify-between items-center mb-2">
                <span>Cisco (CSCO) - 傳統網通庫存去化緩慢，指引保守</span>
                <span class="text-rose-500 font-bold">暴跌 8.40% (收盤報 $47.38)</span>
              </h4>
              <p class="text-sm text-slate-655 dark:text-zinc-350 leading-relaxed mb-3">
                思科（CSCO）公佈的季度營收為 135.4 億美元，略低於預估，每股收益 $0.85 持平。然而，管理層對下一季度的營收展望範圍中值定在 131 億美元，顯著低於分析師普遍預期的 137.5 億美元。管理層指出，雖然 800G 交換機在 AI 數據中心的採購有所增加，但佔比仍低，且傳統企業客戶採購網通設備意願受利率環境壓制，導致庫存清理進度落後。
              </p>
              <div class="p-3 bg-slate-50 dark:bg-zinc-800 text-slate-500 dark:text-zinc-400 text-xs font-semibold rounded-lg font-sans">
                💡 核心解讀：思科的大跌暴露了傳統網通設備板塊的估值痛點。在沒有強烈 AI 算力高成長引擎支撐的情況下，傳統網通極易受宏觀 IT 支出收縮的衝擊，這也促使資金大舉離開思科，轉移向具備 AI 確定性訂單的光模組及以太交換網板塊。
              </div>
            </div>
          </div>
        </div>

        <div>
          <h3 class="text-lg font-semibold mb-3">未來重要財報預告</h3>
          <div class="overflow-x-auto border border-slate-200 dark:border-zinc-800 rounded-xl mt-4">
            <table class="min-w-full text-left text-sm text-slate-655 dark:text-zinc-300">
              <thead class="text-xs uppercase bg-slate-150 dark:bg-zinc-800 text-slate-700 dark:text-zinc-200">
                <tr>
                  <th class="p-3">發佈日期</th>
                  <th class="p-3">Company (代號)</th>
                  <th class="p-3">預期 EPS</th>
                  <th class="p-3">預期營收</th>
                  <th class="p-3">市場關注焦點</th>
                </tr>
              </thead>
              <tbody class="divide-y divide-slate-200 dark:divide-zinc-800 font-mono text-xs">
                <tr>
                  <td class="p-3 font-sans">08-14 盤前</td>
                  <td class="p-3 font-semibold font-sans">Deere & Co. (DE)</td>
                  <td class="p-3">$5.75</td>
                  <td class="p-3">$10.82B</td>
                  <td class="p-3 font-sans">重型農業與工業機具訂單指引，作為實體經濟和製造業週期的重要風向標。</td>
                </tr>
                <tr>
                  <td class="p-3 font-sans">08-20 盤後</td>
                  <td class="p-3 font-semibold font-sans">Snowflake (SNOW)</td>
                  <td class="p-3">$0.16</td>
                  <td class="p-3">$850M</td>
                  <td class="p-3 font-sans">新任 CEO 上台後首個完整季度財報，觀察其 AI 數據庫產品（Cortex）商業化進展。</td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </section>

    <!-- 10. 機構觀點與資金流 -->
    <section id="sec-10" class="scroll-mt-6 font-sans">
      <h2 class="text-xl font-bold mb-4 flex items-center gap-2 border-b border-slate-100 dark:border-zinc-850 pb-2">
        <span class="text-brand-500">10.</span> 機構觀點與資金流
      </h2>
      <div class="p-5 rounded-xl bg-white dark:bg-zinc-900 border border-slate-200 dark:border-zinc-800/80 shadow-sm leading-relaxed text-sm text-slate-655 dark:text-zinc-300 space-y-4">
        <p>
          <strong>高盛：軟體SaaS板塊正迎來強烈「估值回補」行情：</strong>高盛策略師在最新報告中指出，利率下行正使 SaaS 軟體與雲端估值重獲溢價。經過上半年的超跌，軟體股的擁擠度與估值水位均處於歷史低點。一旦 PPI 等宏觀通膨指標落地，機構必然會將部分資金從高位擁擠的半導體硬體端調倉至估值低廉且能見度高的軟體龍頭（ADBE、CRM），這是一次健康的資產再分配。
        </p>
        <p>
          <strong>資金流向 (ETF Flow)</strong>：今日軟體 SaaS（IGV）與地產（XLRE）獲得強勁的機構淨流入，而光模組與網通（CSCO、LITE）則錄得顯著的資金淨流出。大宗商品 ETF（GLD）在高位回吐下錄得溫和流出。
        </p>
      </div>
    </section>

    <!-- 11. 板塊輪動判斷 -->
    <section id="sec-11" class="scroll-mt-6 font-sans">
      <h2 class="text-xl font-bold mb-4 flex items-center gap-2 border-b border-slate-100 dark:border-zinc-850 pb-2">
        <span class="text-brand-500">11.</span> 板塊輪動判斷
      </h2>
      <div class="p-5 rounded-xl bg-white dark:bg-zinc-900 border border-slate-200 dark:border-zinc-800/80 shadow-sm leading-relaxed text-sm text-slate-655 dark:text-zinc-300">
        <p class="mb-3">
          今日市場板塊輪動呈現強烈的<strong>「資金從高位硬體向低位軟體及利率敏感地產輪動」</strong>：
        </p>
        <ul class="list-disc pl-5 space-y-2">
          <li><strong>軟體端多頭絕地反撲</strong>：高息壓力緩解後，估值受壓抑最嚴重的軟體板塊迎來全面補漲。資金大舉流入 Adobe、CRM、SaaS 股。</li>
          <li><strong>光通訊與網通主動回調</strong>：思科財報利空加速了網通設備板塊的短線修正，前日暴漲的光模組（LITE、COHR）進入健康的良性回踩，並非行情結束。</li>
          <li><strong>結論</strong>：多頭藉由利多數據擴展了市場寬度，小盤股與軟體股開始跟上大盤節奏，反映出大盤處於健康的良性上升趨勢中。</li>
        </ul>
      </div>
    </section>

    <!-- 12. 重點關注股觀察 -->
    <section id="sec-12" class="scroll-mt-6 font-sans">
      <h2 class="text-xl font-bold mb-4 flex items-center gap-2 border-b border-slate-100 dark:border-zinc-850 pb-2">
        <span class="text-brand-500">12.</span> 重點關注股觀察
      </h2>
      
      <div class="mb-4 flex flex-col sm:flex-row gap-2 no-print">
        <input type="text" id="watchSearch" placeholder="搜尋個股代碼或關鍵字..." class="px-4 py-2 text-sm rounded-lg border border-slate-300 dark:border-zinc-800 bg-white dark:bg-zinc-900 focus:outline-none focus:ring-2 focus:ring-sky-500 w-full sm:w-72">
      </div>

      <div class="p-5 rounded-xl bg-white dark:bg-zinc-900 border border-slate-200 dark:border-zinc-800/80 shadow-sm overflow-x-auto">
        <table class="w-full text-left text-sm text-slate-655 dark:text-zinc-300" id="watchTable" data-sort-dir="none">
          <thead class="text-xs uppercase bg-slate-150 dark:bg-zinc-800 text-slate-700 dark:text-zinc-200">
            <tr>
              <th class="p-3 sortable" onclick="sortTable('watchTable', 0)">代碼</th>
              <th class="p-3 sortable" onclick="sortTable('watchTable', 1, true)">當日價格</th>
              <th class="p-3 sortable" onclick="sortTable('watchTable', 2, true)">漲跌幅</th>
              <th class="p-3">技術趨勢</th>
              <th class="p-3">關鍵支撐/壓力</th>
              <th class="p-3">交易決策判定</th>
            </tr>
          </thead>
          <tbody class="divide-y divide-slate-200 dark:divide-zinc-800">
{watch_rows}          </tbody>
        </table>
      </div>
    </section>

    <!-- 13. 明日交易計畫 -->
    <section id="sec-13" class="scroll-mt-6 font-sans">
      <h2 class="text-xl font-bold mb-4 flex items-center gap-2 border-b border-slate-100 dark:border-zinc-850 pb-2">
        <span class="text-brand-500">13.</span> 明日交易計畫 / 觀察清單
      </h2>
      <div class="grid grid-cols-1 md:grid-cols-3 gap-6 text-sm">
        <div class="p-5 rounded-xl bg-white dark:bg-zinc-900 border border-slate-200 dark:border-zinc-800/80 shadow-sm space-y-2">
          <h4 class="font-bold text-slate-800 dark:text-white">13.1 宏觀觀察點</h4>
          <ul class="list-decimal pl-5 space-y-1.5 text-slate-600 dark:text-zinc-400 text-xs font-sans">
            <li><strong>週五零售銷售數據</strong>：即將公佈的 7 月零售銷售報告，將是衡量美國消費者支出與軟著陸的重要訊號。</li>
            <li><strong>美債收益率 4.60% 關口</strong>：10年期殖利率已降至 4.64%，若能進一步下穿 4.60% 平台，將會引導 SaaS 與成長股持續逼空。</li>
            <li><strong>美元指數</strong>：觀察美元在 99.95 水平的支撐力度。</li>
          </ul>
        </div>
        
        <div class="p-5 rounded-xl bg-white dark:bg-zinc-900 border border-slate-200 dark:border-zinc-800/80 shadow-sm space-y-2">
          <h4 class="font-bold text-slate-800 dark:text-white">13.2 大盤指數觀察</h4>
          <ul class="list-decimal pl-5 space-y-1.5 text-slate-600 dark:text-zinc-400 text-xs font-sans">
            <li><strong>SPY (標普500)</strong>：再創歷史收盤新高，若站穩 777 點，上行目標鎖定 790 點。</li>
            <li><strong>QQQ (納指100)</strong>：已穩穩突破 50MA，觀察週五能否確認這一右側突破信號，開啟新上攻浪。</li>
            <li><strong>IWM (羅素2000)</strong>：守在 300 點之上，具備降息定價下的補漲機會。</li>
          </ul>
        </div>
        
        <div class="p-5 rounded-xl bg-white dark:bg-zinc-900 border border-slate-200 dark:border-zinc-800/80 shadow-sm space-y-2">
          <h4 class="font-bold text-slate-800 dark:text-white">13.3 個股與板塊聚焦</h4>
          <ul class="list-decimal pl-5 space-y-1.5 text-slate-600 dark:text-zinc-400 text-xs font-sans">
            <li><strong>Adobe (ADBE) / Salesforce (CRM)</strong>：超跌後底部長陽突破，可在拉回短期均線時主動分批建立右側倉位。</li>
            <li><strong>Lumentum (LITE) / Coherent (COHR)</strong>：高位回撤提供良好的低吸機會，關注 LITE 在 $860-$870 支撐。</li>
            <li><strong>Cisco (CSCO)</strong>：財報大跌破位，短期面臨庫存去化壓力，暫時不宜進場抄底。</li>
          </ul>
        </div>
      </div>
    </section>

    <!-- 14. 風險提示 -->
    <section id="sec-14" class="scroll-mt-6 font-sans">
      <h2 class="text-xl font-bold mb-4 flex items-center gap-2 border-b border-slate-100 dark:border-zinc-850 pb-2">
        <span class="text-brand-500">14.</span> 風險提示
      </h2>
      <div class="p-5 rounded-xl bg-white dark:bg-zinc-900 border border-slate-200 dark:border-zinc-800/80 shadow-sm overflow-x-auto">
        <table class="w-full text-left text-sm text-slate-655 dark:text-zinc-300">
          <thead class="text-xs uppercase bg-slate-150 dark:bg-zinc-800 text-slate-700 dark:text-zinc-200">
            <tr>
              <th class="p-3">風險項目</th>
              <th class="p-3 text-center">風險等級</th>
              <th class="p-3">具體解讀與應對策略</th>
            </tr>
          </thead>
          <tbody class="divide-y divide-slate-200 dark:divide-zinc-800 font-sans text-xs sm:text-sm">
            <tr>
              <td class="p-3 font-semibold">傳統企業 IT 開支疲弱風險</td>
              <td class="p-3 text-center"><span class="px-2.5 py-0.5 rounded-full text-xs font-semibold bg-orange-100 dark:bg-orange-950/40 text-orange-700 dark:text-orange-300">中高</span></td>
              <td class="p-3 text-slate-500 dark:text-zinc-400">思科的大跌警告我們，除了 AI 算力基建之外的傳統硬體和網絡設備需求依然疲軟。操作上應避開非 AI 屬性的傳統硬體股。</td>
            </tr>
            <tr>
              <td class="p-3 font-semibold">高位光網絡獲利盤踩踏</td>
              <td class="p-3 text-center"><span class="px-2.5 py-0.5 rounded-full text-xs font-semibold bg-yellow-100 dark:bg-yellow-950/40 text-yellow-700 dark:text-yellow-300">中</span></td>
              <td class="p-3 text-slate-500 dark:text-zinc-400">LITE、COHR 融資盤比例較高，短線暴漲後的獲利了結可能在 1-2 個交易日內引發寬幅波動。低吸不宜過急。</td>
            </tr>
            <tr>
              <td class="p-3 font-semibold">零售銷售數據若大幅低於預期</td>
              <td class="p-3 text-center"><span class="px-2.5 py-0.5 rounded-full text-xs font-semibold bg-yellow-100 dark:bg-yellow-950/40 text-yellow-700 dark:text-yellow-300">中</span></td>
              <td class="p-3 text-slate-500 dark:text-zinc-400">若週五公佈的消費數據意外走弱，市場可能會重新燃起對「經濟衰退」的擔憂，引發獲利盤拋售。建議控制整體倉位，避免滿倉。</td>
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
      <div class="p-5 rounded-xl bg-slate-900 text-white shadow-md space-y-4 text-sm sm:text-base leading-relaxed">
        <p>
          <strong>今日市場結論：</strong>
          今日美股成功向市場展現了「健康的板塊輪動與指數新高」。在批發通膨 PPI 續呈溫和的助推下，利率下行定價引爆了超跌的軟體 SaaS 板塊（ADBE、CRM）的強力估值修復。儘管思科財報利空導致傳統網通與高位光模組板塊（LITE、COHR、ANET）短線獲利回吐，但這部分資金並未離開科技主線，而是完成了板塊間的健康輪換。標普 500 再創收盤歷史新高，均線支持紮實，多頭趨勢良好。
        </p>
        <p>
          <strong>當前市場階段：</strong>
          <span class="text-emerald-400 font-bold">批發通膨降溫 / 超跌SaaS板塊估值強勢回補 / 高位光網絡板塊健康回踩整理</span>
        </p>
        <p>
          <strong>我的操作傾向：</strong>
          「分批建倉超跌 SaaS 軟體龍頭，逢低承接回踩均線的光通訊配套龍頭，避開傳統企業硬體股」。建議分批加倉底部走強的 Adobe（ADBE）、Salesforce（CRM），同時耐心等待光通訊龍頭 Lumentum（LITE）回踩 20MA（約 $870 附近）再行介入，對思科（CSCO）等傳統網通股保持觀望。
        </p>
        <div class="p-3.5 bg-zinc-800 text-slate-300 rounded-lg text-xs">
          <strong>💡 明日最值得關注的 5 個信號：</strong>
          <ul class="list-decimal pl-5 mt-2 space-y-1">
            <li>週五將發布的美國 7 月零售銷售數據，觀察消費力是否健康。</li>
            <li>Adobe（ADBE）大漲後是否能站穩在 $268 美元平台之上。</li>
            <li>10年期美債殖利率是否會進一步下探至 4.60% 平台。</li>
            <li>Lumentum（LITE）在 $870 支撐處是否會出現止跌買盤。</li>
            <li>思科（CSCO）暴跌後，機構是否會在 $46-$47 區域低吸建倉。</li>
          </ul>
        </div>
      </div>
    </section>

    <!-- Footer -->
    <footer class="mt-16 pt-8 border-t border-slate-200 dark:border-zinc-800 text-xs text-slate-500 dark:text-zinc-500 text-center space-y-1">
      <p>美股收盤日報 • 2026-08-13 版面模板 • 實際美股數據發布版 2026-08-13</p>
      <p>資料來源：CNBC, Reuters, Bloomberg, Yahoo Finance, CME FedWatch • 僅供投資研究復盤，不構成任何投資建議</p>
    </footer>

  </main>
</div>

<script>
  // Theme Toggle
  const themeToggleBtn = document.getElementById('theme-toggle');
  
  themeToggleBtn.addEventListener('click', () => {{
    const isDark = document.documentElement.classList.toggle('dark');
    localStorage.theme = isDark ? 'dark' : 'light';
    
    // Re-init mermaid with new theme if loaded
    if (window.__mermaid) {{
      document.querySelectorAll('.mermaid[data-processed]').forEach(el => {{
        el.removeAttribute('data-processed');
        el.innerHTML = el.dataset.src || el.textContent;
      }});
      window.__mermaid.initialize({{ startOnLoad: false, theme: isDark ? 'dark' : 'default', securityLevel: 'loose' }});
      window.__mermaid.run();
    }}
  }});

  // Overview Chart (Chart.js)
  const ctx = document.getElementById('overviewChart').getContext('2d');
  new Chart(ctx, {{
    type: 'bar',
    data: {{
      labels: ['標普500 (SPY)', '納斯達克 (QQQ)', '道瓊工業 (DIA)', '羅素2000 (IWM)', '費半半導體 (SOXX)', '科技軟體 (IGV)', '能源板塊 (XLE)'],
      datasets: [{{
        label: '當日漲跌幅 (%)',
        data: [{spy_pct:.2f}, {qqq_pct:.2f}, {dia_pct:.2f}, {iwm_pct:.2f}, {soxx_pct:.2f}, {igv_pct:.2f}, {xle_pct:.2f}],
        backgroundColor: [
          {f"'{spy_pct_color}'"}, {f"'{qqq_pct_color}'"}, {f"'{dia_pct_color}'"}, {f"'{iwm_pct_color}'"}, {f"'{soxx_pct_color}'"}, {f"'{igv_pct_color}'"}, {f"'{xle_pct_color}'"}
        ],
        borderRadius: 8,
        borderWidth: 1
      }}]
    }},
    options: {{
      responsive: true,
      maintainAspectRatio: false,
      plugins: {{
        legend: {{ display: false }}
      }},
      scales: {{
        y: {{
          ticks: {{ callback: value => value + '%' }}
        }}
      }}
    }}
  }});

  // Search/Filter for Sector Table
  document.getElementById('sectorSearch').addEventListener('input', function(e) {{
    const q = e.target.value.toLowerCase();
    const rows = document.querySelectorAll('#sectorTable tbody tr');
    rows.forEach(row => {{
      const text = row.textContent.toLowerCase();
      row.style.display = text.includes(q) ? '' : 'none';
    }});
  }});

  // Search/Filter for Watch Table
  document.getElementById('watchSearch').addEventListener('input', function(e) {{
    const q = e.target.value.toLowerCase();
    const rows = document.querySelectorAll('#watchTable tbody tr');
    rows.forEach(row => {{
      const text = row.textContent.toLowerCase();
      row.style.display = text.includes(q) ? '' : 'none';
    }});
  }});

  // Simple Vanilla JS Table Sorting
  function sortTable(tableId, colIndex, isNumeric = false) {{
    const table = document.getElementById(tableId);
    const tbody = table.querySelector('tbody');
    const rows = Array.from(tbody.querySelectorAll('tr'));
    const currentDir = table.getAttribute('data-sort-dir') === 'asc' ? 'desc' : 'asc';
    table.setAttribute('data-sort-dir', currentDir);
    
    rows.sort((a, b) => {{
      let cellA = a.cells[colIndex].textContent.trim();
      let cellB = b.cells[colIndex].textContent.trim();
      
      if (isNumeric) {{
        cellA = parseFloat(cellA.replace(/[^\d\.\\-]/g, '')) || 0;
        cellB = parseFloat(cellB.replace(/[^\d\.\\-]/g, '')) || 0;
        return currentDir === 'asc' ? cellA - cellB : cellB - cellA;
      }}
      
      return currentDir === 'asc' 
        ? cellA.localeCompare(cellB, 'zh-TW') 
        : cellB.localeCompare(cellA, 'zh-TW');
    }});
    
    tbody.innerHTML = '';
    rows.forEach(r => tbody.appendChild(r));
  }}

  // Sticky TOC scroll-spy
  const tocLinks = document.querySelectorAll('.toc a');
  const sections = [...tocLinks].map(a => document.querySelector(a.getAttribute('href'))).filter(Boolean);
  if (sections.length) {{
    const onScroll = () => {{
      const y = window.scrollY + 120;
      let active = sections[0];
      for (const s of sections) {{
        if (s.offsetTop <= y) {{
          active = s;
        }}
      }}
      tocLinks.forEach(a => a.classList.toggle('active', a.getAttribute('href') === '#' + active.id));
    }};
    window.addEventListener('scroll', onScroll, {{ passive: true }});
    onScroll();
  }}
</script>

</body>
</html>
"""

# Write HTML file
output_path = "/Users/wisdom/html-report-skill/reports/2026-08-13-us-stock-closing-daily-report.html"
with open(output_path, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"Generated report HTML at {output_path}")

# Run publish.py
publish_script = "/Users/wisdom/html-report-skill/.antigravitycli/skills/html-report/scripts/publish.py"
title = "美股收盤日報｜2026-08-13"
description = "週四（2026年8月13日），美股PPI數據超預期溫和，支持降息預期，標普500上漲0.65%再創歷史新高，軟體SaaS板塊大反攻，Adobe大漲4.53%，但光通訊面臨回調，Cisco財報後大跌。"

cmd = [
    "python3",
    publish_script,
    output_path,
    title,
    description,
    "--no-push"
]

print(f"Running publish script: {' '.join(cmd)}")
res = subprocess.run(cmd, capture_output=True, text=True)
print("Publish STDOUT:", res.stdout)
print("Publish STDERR:", res.stderr)
sys.exit(res.returncode)
