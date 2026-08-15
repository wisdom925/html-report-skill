import os
import subprocess
import sys
import json

# Load quotes
with open("/Users/wisdom/html-report-skill/scratch/quotes_2026-08-14.json", "r", encoding="utf-8") as f:
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

# Sectors data for 2026-08-14
sectors = [
    {"name": "能源板塊", "etf": "XLE", "pct": get_raw_val("XLE", "pct"), "5d": "+6.50%", "1m": "+8.50%", "driver": "WTI原油價格反彈收漲1.26%，受中東地緣政治局勢緊張及需求回補支撐，能源股逆勢上揚1.39%領跑大盤。"},
    {"name": "公用事業", "etf": "XLU", "pct": get_raw_val("XLU", "pct"), "5d": "+1.20%", "1m": "-0.80%", "driver": "AI資料中心對電力的長期需求持續發酵，電網股如NRG Energy（+5.42%）與星座能源（+1.39%）表現強勁，提振板塊收漲0.61%。"},
    {"name": "原物料板塊", "etf": "XLB", "pct": get_raw_val("XLB", "pct"), "5d": "+0.60%", "1m": "+0.90%", "driver": "金價反彈上漲0.63%提振黃金與材料股，XLB收漲0.44%。"},
    {"name": "工業板塊", "etf": "XLI", "pct": get_raw_val("XLI", "pct"), "5d": "+0.50%", "1m": "+1.20%", "driver": "重電設備伊頓（ETN -0.40%）高位整理，但GE Vernova（+1.32%）再創新高，帶動工業板塊收漲0.39%。"},
    {"name": "通訊服務", "etf": "XLC", "pct": get_raw_val("XLC", "pct"), "5d": "+1.10%", "1m": "-0.20%", "driver": "Reddit（RDDT）因即將納入標普500指數暴漲13.80%，抵消了Meta（-0.86%）的小幅回調，XLC收漲0.36%。"},
    {"name": "房地產板塊", "etf": "XLRE", "pct": get_raw_val("XLRE", "pct"), "5d": "+0.20%", "1m": "+2.10%", "driver": "零售數據疲軟加強了聯準會降息預期，利率敏感的房地產板塊表現穩健，收漲0.33%。"},
    {"name": "必需消費", "etf": "XLP", "pct": get_raw_val("XLP", "pct"), "5d": "+0.40%", "1m": "+0.00%", "driver": "防禦性買氣回暖，必需消費品在市場回調中發揮避險作用，小幅收漲0.10%。"},
    {"name": "金融板塊", "etf": "XLF", "pct": get_raw_val("XLF", "pct"), "5d": "+0.30%", "1m": "+1.10%", "driver": "美債收益率小幅反彈但仍處於相對低點，銀行股窄幅整理，金融板塊收跌0.17%。"},
    {"name": "非必需消費", "etf": "XLY", "pct": get_raw_val("XLY", "pct"), "5d": "+0.50%", "1m": "+0.80%", "driver": "零售銷售月率降溫拖累消費者信心，亞馬遜（-0.94%）回落，非必需消費板塊收跌0.21%。"},
    {"name": "科技板塊", "etf": "XLK", "pct": get_raw_val("XLK", "pct"), "5d": "+4.50%", "1m": "+1.00%", "driver": "博通（AVGO -5.94%）因融資擔憂重挫，應用材料（AMAT -4.50%）財報後利多出盡，雖超微（AMD +6.50%）暴漲，板塊仍收跌0.40%。"},
    {"name": "醫療保健", "etf": "XLV", "pct": get_raw_val("XLV", "pct"), "5d": "+2.50%", "1m": "+3.20%", "driver": "部分防禦性資金撤出，醫藥巨頭普遍回調，醫療保健板塊收跌0.60%表現最弱。"},
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

# Watch List data for 2026-08-14
watch_list = [
    {"symbol": "NVDA", "trend": "微跌0.06%報$225.16，高位橫盤整理，多空在$225附近僵持，守穩均線", "levels": "$218.00 / $232.00", "tag": "高位震盪"},
    {"symbol": "AMD", "trend": "大漲6.50%報$514.39，放量突破短期均線並創收盤高點，型態極強", "levels": "$495.00 / $530.00", "tag": "繼續強勢"},
    {"symbol": "AVGO", "trend": "重挫5.94%報$392.99，受BofA融資質疑拖累，跌破短期均線回踩支撐", "levels": "$385.00 / $415.00", "tag": "回踩支撐"},
    {"symbol": "MRVL", "trend": "微跌0.07%報$222.02，昨日大漲後窄幅整理，多頭格局未變", "levels": "$215.00 / $232.00", "tag": "高位震盪"},
    {"symbol": "GOOGL", "trend": "微跌0.13%報$345.90，低位震盪築底，在$340上方企穩", "levels": "$340.00 / $355.00", "tag": "等財報催化"},
    {"symbol": "MSFT", "trend": "收跌0.30%報$495.40，隨科技板塊震盪回調，高位窄幅盤整", "levels": "$488.00 / $505.00", "tag": "高位震盪"},
    {"symbol": "META", "trend": "下跌0.86%報$589.85，創新高後小幅獲利回吐，維持在上升通道", "levels": "$578.00 / $600.00", "tag": "高位震盪"},
    {"symbol": "AMZN", "trend": "下跌0.94%報$262.65，受疲軟零售數據壓抑，持續考驗下軌平台", "levels": "$258.00 / $270.00", "tag": "需要觀察"},
    {"symbol": "ORCL", "trend": "下跌3.65%報$150.52，連日回調，回踩下方短期均線支撐", "levels": "$146.00 / $156.00", "tag": "回踩支撐"},
    {"symbol": "CRM", "trend": "下跌2.56%報$196.21，昨日大漲後技術性回踩，量能溫和", "levels": "$190.00 / $204.00", "tag": "需要觀察"},
    {"symbol": "NOW", "trend": "下跌2.55%報$124.00，隨SaaS板塊回調，守在關鍵支撐位之上", "levels": "$120.00 / $128.00", "tag": "需要觀察"},
    {"symbol": "SNOW", "trend": "下跌2.51%報$328.92，低位盤整整理，靜待財報催化", "levels": "$322.00 / $340.00", "tag": "低位修復"},
    {"symbol": "ADBE", "trend": "下跌2.39%報$264.02，昨日長陽突破後獲利回吐，回試突破口支撐", "levels": "$258.00 / $272.00", "tag": "需要觀察"},
    {"symbol": "PLTR", "trend": "下跌2.78%報$174.04，高位窄幅震盪，在$170上方強勢整固", "levels": "$168.00 / $180.00", "tag": "高位震盪"},
    {"symbol": "LITE", "trend": "大漲5.19%報$926.14，回踩後多頭強力拉升，再創波段新高，動能充沛", "levels": "$890.00 / $950.00", "tag": "繼續強勢"},
    {"symbol": "COHR", "trend": "微跌0.43%報$325.83，高位回踩後逐步企穩，量能縮減", "levels": "$318.00 / $345.00", "tag": "高位震盪"},
    {"symbol": "ANET", "trend": "下跌2.36%報$198.82，破位回踩20日均線，尋求平台支撐", "levels": "$195.00 / $208.00", "tag": "回踩支撐"},
    {"symbol": "FLNC", "trend": "微跌0.61%報$13.14，儲能板塊低位弱勢盤整", "levels": "$12.50 / $13.80", "tag": "需要觀察"},
    {"symbol": "OKLO", "trend": "下跌4.46%報$44.38，震盪回調，考驗下方中期均線支撐", "levels": "$42.00 / $47.50", "tag": "需要觀察"},
    {"symbol": "VST", "trend": "上漲1.18%報$148.13，多頭延續，沿5日均線穩健攀升", "levels": "$144.00 / $152.00", "tag": "繼續強勢"},
    {"symbol": "CEG", "trend": "上漲1.39%報$282.50，放量突破盤整區間，重拾多頭攻勢", "levels": "$275.00 / $290.00", "tag": "繼續強勢"},
    {"symbol": "ETN", "trend": "下跌0.40%報$451.51，重電龍頭高位回吐，守在重要均線上方", "levels": "$445.00 / $462.00", "tag": "回踩支撐"},
    {"symbol": "VRT", "trend": "上漲2.36%報$293.84，液冷龍頭放量拉升，再創收盤歷史新高", "levels": "$285.00 / $305.00", "tag": "繼續強勢"},
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
  <title>美股收盤日報｜零售數據爆冷引發衰退憂慮，三大指數自高點回吐！小盤股羅素2000逆勢創高，博通大跌6%拖累晶片股，Reddit因納入標普飆漲14%</title>
  <meta name="description" content="2026年8月14日美股收盤日報：美股零售數據爆冷大跌0.6%引發衰退憂慮，三大指數自高點回調，但小盤股羅素2000逆勢創歷史新高，博通大跌近6%拖累半導體，Reddit因加入標普500飆升14%。">
  <meta property="og:title" content="美股收盤日報｜2026-08-14">
  <meta property="og:description" content="零售銷售下降0.6%引燃衰退憂慮，三大指數自歷史高點回落，小盤股逆勢破頂，博通重挫，Reddit暴漲。">
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
        <span>美股交易日：<strong>2026-08-14</strong></span>
      </div>
      <h1 class="text-3xl font-extrabold tracking-tight text-slate-900 dark:text-white sm:text-4xl mb-4 font-sans font-bold">
        美股收盤日報｜零售數據爆冷引發衰退憂慮，三大指數自高點回吐！小盤股羅素2000逆勢創高，博通大跌6%拖累晶片股，Reddit因納入標普飆漲14%
      </h1>
      <p class="text-base text-slate-500 dark:text-zinc-400 leading-relaxed max-w-4xl font-sans">
        週五（2026年8月14日），美股大盤在美國7月零售銷售數據意外下滑0.6%後震盪走弱，市場擔憂消費支出放緩及高利率對實體經濟的壓抑，三大指數均自前一日創下的歷史高點回調。標普500指數微跌0.17%（報7,785.76點），納斯達克綜合指數下跌0.28%（報26,729.16點），道瓊工業指數下跌0.20%。然而，小盤股指數羅素2000（IWM）逆勢收漲0.52%，續創歷史收盤新高，顯示降息預期下中小企業融資壓力改善的邏輯依然強烈。個股方面，博通（AVGO）因分析師對複雜債務融資工具的擔憂重挫5.94%，拖累半導體板塊；應用材料（AMAT）雖財報優於預期，但利多出盡及估值過高壓抑股價下跌4.50%；Reddit（RDDT）則受惠於下週二即將納入標普500指數的消息暴漲13.80%。
      </p>
    </header>

    <!-- 0. 今日一句話總結 -->
    <section id="sec-0" class="scroll-mt-6 font-sans">
      <h2 class="text-xl font-bold mb-4 flex items-center gap-2 border-b border-slate-100 dark:border-zinc-850 pb-2">
        <span class="text-brand-500">0.</span> 今日一句話總結
      </h2>
      <div class="p-5 rounded-xl bg-white dark:bg-zinc-900 border border-slate-200 dark:border-zinc-800/80 shadow-sm leading-relaxed space-y-3">
        <ul class="list-disc pl-5 space-y-2 text-slate-600 dark:text-zinc-300 text-sm sm:text-base">
          <li><strong>大盤狀態</strong>：零售數據大幅走弱引燃衰退憂慮，三大指數自高點獲利回吐，但小盤股逆勢破頂，市場寬度仍具支撐。</li>
          <li><strong>驅動因素</strong>：7月零售銷售大跌0.6%遠遜於預期，觸發消費疲軟擔憂；但數據走弱也更加固化了9月聯準會降息的底牌。</li>
          <li><strong>資金態度</strong>：資金從高估值的AI硬體與軟體端流出，避險至重電發電（NRG +5.42%、CEG +1.39%）與能源板塊，大盤呈現防禦分化。</li>
        </ul>
        <div class="p-3.5 bg-yellow-50 dark:bg-yellow-950/40 border border-yellow-250 dark:border-yellow-805/50 rounded-lg text-yellow-850 dark:text-yellow-300 text-xs sm:text-sm font-semibold">
          ⚠️ 今日市場狀態：指數高位盤整，小盤股與能源強，軟體SaaS與AI硬體龍頭博通領跌，板塊輪動下多頭趨勢仍良好。
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
          <div class="text-xs font-semibold mt-1 {iwm_color}">{get_val("IWM", "pct")} (VIX: {get_val("^VIX", "price")})</div>
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
            title 2026-08-14 盤中走勢大事記
            盤前階段 : 盤前 8:30 公布美國 7 月零售銷售，環比暴跌 0.6% 遠低於市場預期的 +0.1%，創下近期最大跌幅。期指直線跳水，國債殖利率維持低位波動。
            開盤走勢 : 三大指數低開。博通（AVGO）因分析師質疑其潛在的 3700 億美元融資工具暴跌 5% 領跌晶片股，Reddit（RDDT）則受納入標普500消息提振暴漲 10%。
            早盤交易 : 盤初恐慌情緒緩解，市場開始預期疲軟數據將逼迫聯準會更大膽降息。小盤股（IWM）逆勢拉升，電力與發電（NRG +5%、CEG +1.3%）吸引避險資金。
            午盤波動 : 大盤探底回升，標普 500 指數與納指跌幅顯著收窄，羅素 2000（IWM）大漲突破 300 點整數關卡，續寫歷史新高。
            尾盤收盤 : 尾盤因週末效應買氣不足，指數小幅走軟。標普收跌 0.17%，博通大跌 5.94% 拖累科技股，Reddit 最終飆升 13.80% 報 $180.11。
        </div>
        <p class="text-sm text-slate-500 dark:text-zinc-400 leading-relaxed">
          <strong>復盤解析：</strong>週五的市場主線是「零售數據疲軟與科技股獲利回吐」。美國 7 月零售銷售大跌 0.6%，證實了高利率對消費者意願的壓抑，激發了短期的衰退擔憂，三大指數因而低開高走後再度震盪。然而，市場內部寬度依然強韌，羅素 2000 指數（IWM）在降息預期再度強化的支撐下逆勢創下歷史新高。資金表現出明顯的防禦性防守，科技軟體端（IGV）和博通（AVGO）大跌拖累大盤，但能源（XLE）及重電（NRG）獲得防禦性買盤的持續加倉。整體而言，這是一次健康的獲利了結與高位整固。
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
          <h4 class="font-bold text-slate-800 dark:text-white mb-2">零售數據爆冷後收益率低位反彈，曲線維持陡峭化趨勢</h4>
          <p class="mb-3">
            儘管零售數據疲軟，美債收益率在連日走跌後出現技術性小幅反彈：
          </p>
          <ul class="list-disc pl-5 space-y-1 font-mono text-xs sm:text-sm">
            <li><strong>5年期國債收益率 (FVX)</strong>：收報 <strong>{get_raw_val("^FVX", "price")}%</strong>，日升 +1.14%（昨日收 4.31%）。</li>
            <li><strong>10年期國債收益率 (TNX)</strong>：收報 <strong>{get_raw_val("^TNX", "price")}%</strong>，日升 +1.19%（昨日收 4.64%）。</li>
            <li><strong>30年期國債收益率 (TYX)</strong>：收報 <strong>{get_raw_val("^TYX", "price")}%</strong>，日升 +1.00%（昨日收 5.22%）。</li>
          </ul>
          <p class="mt-3 text-slate-500 text-xs font-sans">
            收益率的微幅反彈反映了國債多頭在 Jackson Hole 央行年會前的獲利回吐，但長端債息下行通道依然完整，利好中小企業融資及小盤股（IWM）。
          </p>
        </div>
        
        <!-- Tab panel 2 -->
        <div class="tab-panel text-sm text-slate-655 dark:text-zinc-300 leading-relaxed bg-white dark:bg-zinc-900 p-5 rounded-xl border border-slate-200 dark:border-zinc-800/80 mt-2">
          <h4 class="font-bold text-slate-800 dark:text-white mb-2">零售爆冷強化9月降息確定性</h4>
          <p class="mb-3">
            零售銷售月率意外大跌0.6%，為聯準會開啟降息提供了最直接的理由：
          </p>
          <ul class="list-disc pl-5 space-y-1">
            <li><strong>利率目標區間機率 (CME FedWatch)</strong>：9月降息 25 個基點的機率依然高達 <strong>70.0%</strong>，同時市場對降息 50 個基點（以防經濟失速）的投機性預期也有所抬頭。</li>
            <li><strong>背景解析</strong>：疲軟數據打破了「通膨頑固」的最後防線。市場預計，下半年聯準會將有 2-3 次降息以支持經濟，這使得小盤股與高負債的發電重電企業估值重獲支持。</li>
          </ul>
        </div>
        
        <!-- Tab panel 3 -->
        <div class="tab-panel text-sm text-slate-655 dark:text-zinc-350 leading-relaxed bg-white dark:bg-zinc-900 p-5 rounded-xl border border-slate-200 dark:border-zinc-800/80 mt-2">
          <h4 class="font-bold text-slate-800 dark:text-white mb-2">黃金避險拉升，原油隨能源反彈，比特幣震盪</h4>
          <p class="mb-3">
            在衰退憂慮下，大宗商品及加密貨幣表現分化：
          </p>
          <ul class="list-disc pl-5 space-y-2">
            <li><strong>黃金現貨 (GLD)</strong>：<strong>上漲 +0.63%</strong> 報 401.48 美元，避險資金在零售數據走弱後湧入黃金。</li>
            <li><strong>原油 (USO)</strong>：<strong>上漲 +1.26%</strong> 報 126.60 美元，WTI原油重返 $82.50/桶，受地緣局勢緊張支持。</li>
            <li><strong>美元指數 (DXY)</strong>：UUP 收於 28.11，<strong>下跌 -0.25%</strong>，反映出降息預期升溫壓制美元。</li>
            <li><strong>比特幣 (BTC-USD)</strong>：下跌 -0.67% 報 62,975.19 美元；以太坊 (ETH-USD) 微跌 -0.19% 報 1,880.46 美元。</li>
          </ul>
        </div>
        
        <!-- Tab panel 4 -->
        <div class="tab-panel text-sm text-slate-655 dark:text-zinc-300 leading-relaxed bg-white dark:bg-zinc-900 p-5 rounded-xl border border-slate-200 dark:border-zinc-800/80 mt-2">
          <h4 class="font-bold text-slate-800 dark:text-white mb-2">美國 7 月零售銷售經濟數據發布詳情</h4>
          <div class="overflow-x-auto my-3">
            <table class="min-w-full text-xs font-mono text-left">
              <thead>
                <tr class="bg-slate-100 dark:bg-zinc-800 text-slate-700 dark:text-zinc-300">
                  <th class="p-2 border-b">數據項目</th>
                  <th class="p-2 border-b">實際值 (2026-08-14)</th>
                  <th class="p-2 border-b">市場預期值</th>
                  <th class="p-2 border-b">前值 (6月)</th>
                  <th class="p-2 border-b">市場解讀</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td class="p-2 border-b font-sans font-semibold">7月 零售銷售月率 (MoM)</td>
                  <td class="p-2 border-b font-bold text-rose-500">-0.6%</td>
                  <td class="p-2 border-b">+0.1%</td>
                  <td class="p-2 border-b">+0.4%</td>
                  <td class="p-2 border-b font-sans text-rose-500">數據爆冷，遠遜於市場預期。證實了高負債利率對居民開支的壓制。</td>
                </tr>
                <tr>
                  <td class="p-2 border-b font-sans font-semibold">7月 核心零售銷售月率 (MoM)</td>
                  <td class="p-2 border-b font-bold text-rose-500">-0.3%</td>
                  <td class="p-2 border-b">+0.2%</td>
                  <td class="p-2 border-b">+0.3%</td>
                  <td class="p-2 border-b font-sans text-rose-500">低於預期。剔除汽車與汽油後，顯示基礎消費動能減弱，引發衰退擔憂。</td>
                </tr>
              </tbody>
            </table>
          </div>
          <p class="text-xs text-slate-500 mt-2 font-sans">
            <strong>宏觀解讀：</strong>零售數據爆冷是一柄「雙面刃」。短期它激發了消費失速的衰退恐慌，拖累大盤回落；但長期它保證了通膨將被擊敗，並確保聯準會將於 9 月正式降息。
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
        <table class="w-full text-left text-sm text-slate-655 dark:text-zinc-300" id="sectorTable" data-sort-dir="none">
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
          今日市場風格呈現<strong>「防禦板塊與小盤股創高、軟體SaaS全線回調、晶片半導體劇烈分化」</strong>的特徵：
        </p>
        <ul class="list-disc pl-5 space-y-2">
          <li><strong>小盤成長與價值 (IWM)</strong>：逆勢攀升 <strong>+0.52%</strong>，收盤續創歷史新高，市場寬度支持穩健。</li>
          <li><strong>重電、電力與發電 (NRG/CEG/VST/GEV)</strong>：避險資金大舉配置，NRG 暴漲 <strong>+5.42%</strong>，星座能源（CEG）上揚 <strong>+1.39%</strong>，GE Vernova（GEV）上漲 <strong>+1.32%</strong> 再度創高。</li>
          <li><strong>晶片與半導體 (SOXX/SMH)</strong>：強烈分化。博通（AVGO）大跌 <strong>-5.94%</strong> 拖累板塊，但超微（AMD）暴漲 <strong>+6.50%</strong> 護盤，Lumentum（LITE）亦反彈 <strong>+5.19%</strong>，使 SOXX 整體僅微跌 <strong>-0.06%</strong>。</li>
          <li><strong>軟體與 SaaS (IGV)</strong>：前日大反彈後遭遇獲利回吐，IGV 大跌 <strong>-2.07%</strong>，SaaS 龍頭 Salesforce（CRM）下跌 <strong>-2.56%</strong>，Adobe（ADBE）收跌 <strong>-2.39%</strong>。</li>
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
            <li class="flex justify-between"><span>標普500高於50MA比例：</span><span class="font-semibold text-emerald-600">61.2%</span></li>
            <li class="flex justify-between"><span>納指100高於50MA比例：</span><span class="font-semibold text-emerald-600">55.2%</span></li>
            <li class="flex justify-between"><span>標普500高於200MA比例：</span><span class="font-semibold text-emerald-600">68.1%</span></li>
          </ul>
          <p class="text-slate-400 text-xs font-sans">在大盤回調中，位於中短期均線之上的股票比例略微下滑，但整體多頭架構依然牢固。</p>
        </div>

        <div class="p-5 rounded-xl bg-white dark:bg-zinc-900 border border-slate-200 dark:border-zinc-800/80 shadow-sm space-y-3">
          <h4 class="font-bold text-slate-800 dark:text-white flex items-center gap-1.5">
            <span class="w-2.5 h-2.5 rounded-full bg-yellow-500"></span> 漲跌家數與新高/新低
          </h4>
          <ul class="space-y-2 font-mono">
            <li class="flex justify-between"><span>NYSE 漲/跌家數：</span><span>1,450 / 1,580</span></li>
            <li class="flex justify-between"><span>Nasdaq 漲/跌家數：</span><span>1,980 / 2,240</span></li>
            <li class="flex justify-between"><span>NYSE 52周新高/新低：</span><span>71 / 12</span></li>
            <li class="flex justify-between"><span>Nasdaq 52周新高/新低：</span><span>48 / 22</span></li>
          </ul>
          <p class="text-slate-400 text-xs font-sans">交易所內上漲家數略低於下跌家數，但52週新高數量依然大幅跑贏新低，顯示結構分化。</p>
        </div>

        <div class="p-5 rounded-xl bg-white dark:bg-zinc-900 border border-slate-200 dark:border-zinc-800/80 shadow-sm space-y-3">
          <h4 class="font-bold text-slate-800 dark:text-white flex items-center gap-1.5">
            <span class="w-2.5 h-2.5 rounded-full bg-yellow-500"></span> 內部指標觀察
          </h4>
          <ul class="space-y-2 font-mono">
            <li class="flex justify-between"><span>McClellan Oscillator：</span><span class="font-semibold text-rose-500">-2</span></li>
            <li class="flex justify-between"><span>Put/Call Ratio：</span><span class="font-semibold text-emerald-600">0.65</span></li>
            <li class="flex justify-between"><span>VIX 期限結構：</span><span class="font-semibold text-emerald-600">平穩，VIX回落至 14.25</span></li>
          </ul>
          <p class="text-slate-400 text-xs font-sans">麥克連指標微幅轉負，期權PCR維持中性，VIX的持續下滑顯示大盤並無系統性恐慌情緒。</p>
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
              <td class="p-3 font-bold text-rose-500">{get_val("SPY", "price")}</td>
              <td class="p-3">764.10</td>
              <td class="p-3">754.20</td>
              <td class="p-3">60</td>
              <td class="p-3 text-emerald-600 font-sans">歷史高點小幅回踩，上升趨勢完好</td>
              <td class="p-3">770.00 / 782.00</td>
            </tr>
            <tr class="hover:bg-slate-50 dark:hover:bg-zinc-800/30">
              <td class="p-3 font-semibold font-sans">QQQ (納指100 ETF)</td>
              <td class="p-3 font-bold text-rose-500">{get_val("QQQ", "price")}</td>
              <td class="p-3">716.40</td>
              <td class="p-3">715.20</td>
              <td class="p-3">57</td>
              <td class="p-3 text-emerald-600 font-sans">守在50日均線之上盤整，短期趨勢偏多</td>
              <td class="p-3">724.00 / 738.00</td>
            </tr>
            <tr class="hover:bg-slate-50 dark:hover:bg-zinc-800/30">
              <td class="p-3 font-semibold font-sans">IWM (羅素2000 ETF)</td>
              <td class="p-3 font-bold text-emerald-600">{get_val("IWM", "price")}</td>
              <td class="p-3">298.50</td>
              <td class="p-3">291.10</td>
              <td class="p-3">61</td>
              <td class="p-3 font-sans text-emerald-600">放量收漲並創收盤歷史新高，表現強勢</td>
              <td class="p-3">300.00 / 312.00</td>
            </tr>
            <tr class="hover:bg-slate-50 dark:hover:bg-zinc-800/30">
              <td class="p-3 font-semibold font-sans">SMH (費半半導體 ETF)</td>
              <td class="p-3 text-rose-500 font-bold">{get_val("SMH", "price")}</td>
              <td class="p-3">565.10</td>
              <td class="p-3">549.30</td>
              <td class="p-3">56</td>
              <td class="p-3 font-sans text-emerald-600">高位窄幅震盪，博通大跌但超微暴漲護盤</td>
              <td class="p-3">580.00 / 600.00</td>
            </tr>
            <tr class="hover:bg-slate-50 dark:hover:bg-zinc-800/30">
              <td class="p-3 font-semibold font-sans">IGV (科技軟體 ETF)</td>
              <td class="p-3 font-bold text-rose-500">{get_val("IGV", "price")}</td>
              <td class="p-3">101.90</td>
              <td class="p-3">97.80</td>
              <td class="p-3">54</td>
              <td class="p-3 text-rose-500 font-sans">長陽後陰線回踩突破平台，尋求均線支撐</td>
              <td class="p-3">102.50 / 106.50</td>
            </tr>
            <tr class="hover:bg-slate-50 dark:hover:bg-zinc-800/30">
              <td class="p-3 font-semibold font-sans">XLK (科技 ETF)</td>
              <td class="p-3 text-rose-500 font-bold">{get_val("XLK", "price")}</td>
              <td class="p-3">186.20</td>
              <td class="p-3">181.00</td>
              <td class="p-3">58</td>
              <td class="p-3 font-sans text-emerald-600">微幅回撤，各短期均線維持金叉排列</td>
              <td class="p-3">188.00 / 194.00</td>
            </tr>
          </tbody>
        </table>
      </div>
      <p class="text-xs text-slate-500 dark:text-zinc-400 mt-3 leading-relaxed">
        <strong>技術評語：</strong>標普指數（SPY -0.20%）與納指（QQQ -0.14%）在創高後良性回撤。IWM 大漲並創出歷史收盤新高，說明市場寬度依然維持在牛市良性狀態。軟體板塊（IGV -2.07%）昨日大漲後回踩平台支撐。總體大盤上升趨勢沒有受到實質損害，回調依然是右側逢低建倉的主基調。
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
            <p><strong>MSFT (微軟) -0.30%</strong>：收報 $495.40。隨軟體板塊回調，在 $495 阻力關口高位窄幅整理。</p>
            <p><strong>AAPL (蘋果) +0.22%</strong>：收報 $305.93。維持穩步推升走勢，技術多頭形態健康。</p>
            <p><strong>NVDA (輝達) -0.06%</strong>：收報 $225.16。平盤震盪，在 $225 平台附近高位橫盤整固。</p>
            <p><strong>META (Meta) -0.86%</strong>：收報 $589.85。大漲後小幅獲利回吐，退守 $590 平台。</p>
            <p><strong>GOOGL (Alphabet) -0.13%</strong>：收報 $345.90。在 $345 上方小幅盤整築底。</p>
            <p><strong>AMZN (亞馬遜) -0.94%</strong>：收報 $262.65。零售數據爆冷壓制消費股信心，亞馬遜再度承壓回落，測試 $260 支撐。</p>
            <p><strong>TSLA (特斯拉) +0.68%</strong>：收報 $342.27。逆勢上揚，站穩多條短期均線，形態在七巨頭中相對偏強。</p>
          </div>
        </details>

        <details class="group bg-white dark:bg-zinc-900 p-4 rounded-xl border border-slate-200 dark:border-zinc-800">
          <summary class="font-bold text-slate-800 dark:text-white flex justify-between items-center text-sm sm:text-base">
            <span>8.2 AI 硬體 / 半導體重點股異動分析</span>
          </summary>
          <div class="mt-3 text-sm space-y-3 leading-relaxed text-slate-655 dark:text-zinc-350">
            <p><strong>AVGO (博通) -5.94%</strong>：收報 $392.99。受美銀分析師質疑其潛在的 3700 億美元高額債務融資工具影響，機構拋售導致股價大跌近 6%，跌破短線均線。</p>
            <p><strong>AMD (超微) +6.50%</strong>：收報 $514.39。多頭強勢爆發，突破前高與短期均線阻力，放量大漲 6.50%，主要得益於博通資金流出的溢出效應及機構低吸算力備選股。</p>
            <p><strong>AMAT (應用材料) -4.50%</strong>：收報 $505.62。公佈的第三財季財報雖在營收與EPS上雙雙beat，但因對非AI成熟節點設備增長指引不溫不火，且前期漲幅巨大，股價「利多出盡」重挫 4.50%。</p>
            <p><strong>LITE (Lumentum) +5.19%</strong>：收報 $926.14。回踩均線後多頭快速收復失地，展現出極強的買盤承接能力，光模組高速互聯邏輯依然是核心主線。</p>
            <p><strong>VRT (Vertiv) +2.36%</strong>：收報 $293.84。液冷配套基建需求火爆，放量上漲 2.36%，創歷史收盤新高。</p>
          </div>
        </details>

        <details class="group bg-white dark:bg-zinc-900 p-4 rounded-xl border border-slate-200 dark:border-zinc-800">
          <summary class="font-bold text-slate-800 dark:text-white flex justify-between items-center text-sm sm:text-base">
            <span>8.3 軟體 / SaaS / AI 應用重點股異動分析</span>
          </summary>
          <div class="mt-3 text-sm space-y-3 leading-relaxed text-slate-655 dark:text-zinc-350">
            <p><strong>CRM (Salesforce) -2.56%</strong>：收報 $196.21。昨日大漲後技術性回調，量能收縮，在 $195 平台尋求支撐。</p>
            <p><strong>ADBE (Adobe) -2.39%</strong>：收報 $264.02。技術性獲利回吐，回踩均線平台，短線反彈格局未破。</p>
            <p><strong>NOW (ServiceNow) -2.55%</strong>：收報 $124.00。隨軟體板塊全線回調，重新考驗 $122 支撐。</p>
            <p><strong>PLTR (Palantir) -2.78%</strong>：收報 $174.04。高位窄幅整理，在 $170 上方維持良性蓄勢。</p>
          </div>
        </details>

        <details class="group bg-white dark:bg-zinc-900 p-4 rounded-xl border border-slate-200 dark:border-zinc-800">
          <summary class="font-bold text-slate-800 dark:text-white flex justify-between items-center text-sm sm:text-base">
            <span>8.4 AI 電力 / 資料中心 / 能源基礎設施重點股分析</span>
          </summary>
          <div class="mt-3 text-sm space-y-3 leading-relaxed text-slate-655 dark:text-zinc-350">
            <p><strong>NRG (NRG Energy) +5.42%</strong>：收報 $126.24。發電量與電力價格預期走強，避險資金大舉買入，股價暴漲 5.42%。</p>
            <p><strong>CEG (星座能源) +1.39%</strong>：收報 $282.50。AI 核電合約利多持續發酵，突破前期高位平台。</p>
            <p><strong>GEV (GE Vernova) +1.32%</strong>：收報 $1,063.25。重電設備龍頭持續創下歷史新高，多頭趨勢不減。</p>
            <p><strong>OKLO (奧克洛) -4.46%</strong>：收報 $44.38。高波動性小型核電股今日面臨獲利盤拋售回調。</p>
          </div>
        </details>

        <details class="group bg-white dark:bg-zinc-900 p-4 rounded-xl border border-slate-200 dark:border-zinc-800">
          <summary class="font-bold text-slate-800 dark:text-white flex justify-between items-center text-sm sm:text-base">
            <span>8.5 其他顯著大漲/大跌的股票與異動原因</span>
          </summary>
          <div class="mt-3 text-sm space-y-3 leading-relaxed text-slate-655 dark:text-zinc-350">
            <p><strong>RDDT (Reddit) +13.80%</strong>：收報 $180.11。標普道瓊指數公司宣佈，Reddit 將於下週二（8月18日）開盤前納入 S&P 500 指數，取代即將被收購的退市公司。消息引發指數基金被動配置買盤，股價暴漲近 14%。</p>
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
                <span>Applied Materials (AMAT) - 財報超預期，但高預期與成熟節點增長保守引發獲利回吐</span>
                <span class="text-rose-500 font-bold">下跌 4.50% (收盤報 $505.62)</span>
              </h4>
              <p class="text-sm text-slate-655 dark:text-zinc-350 leading-relaxed mb-3">
                半導體設備龍頭應用材料（AMAT）公佈其第三財季營收達到 91.2 億美元，高於市場預期的 89.6 億美元；調整後每股收益為 $3.50，高於預估的 $3.32。然而，管理層對下一財季的營收中值預測為 93 億美元，雖然略高於預期，但並未給予市場「驚喜」。同時，管理層提到成熟節點（如非 AI 工業和成熟晶片）設備開支的增長仍然偏向保守，引發股價在大漲後利多出盡回調。
              </p>
              <div class="p-3 bg-slate-50 dark:bg-zinc-800 text-slate-500 dark:text-zinc-400 text-xs font-semibold rounded-lg font-sans">
                💡 核心解讀：AMAT 的走勢是典型半導體高估值下的「Sell the News」。儘管 AI 先進製程與 HBM 包裝需求依舊極為火熱，但成熟產能需求復甦的保守性使得追高資金決定短線撤出，轉而流向同樣回調但處於低位或有被動資金加倉的其他個股（如 Reddit 或 AMD）。
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
                  <td class="p-3 font-sans">08-20 盤後</td>
                  <td class="p-3 font-semibold font-sans">Snowflake (SNOW)</td>
                  <td class="p-3">$0.16</td>
                  <td class="p-3">$850M</td>
                  <td class="p-3 font-sans">觀察其 AI 資料庫產品（Cortex）商業化進展及新 CEO 對全年指引的調整。</td>
                </tr>
                <tr>
                  <td class="p-3 font-sans">08-27 盤後</td>
                  <td class="p-3 font-semibold font-sans">NVIDIA (NVDA)</td>
                  <td class="p-3">$0.64</td>
                  <td class="p-3">$28.5B</td>
                  <td class="p-3 font-sans">AI 晶片霸主的歷史性財報，Blackwell 架構出貨時程與產能瓶頸是全市場的核心焦點。</td>
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
          <strong>摩根大通：零售銷售爆冷證實高利率壓制，但軟著陸趨勢未改：</strong>摩根大通宏觀策略師表示，7月零售銷售大跌0.6%是 cumulative 高利率開支抑制的表現，但消費者財務狀況並未系統性崩潰。這為聯準會 9 月開啟降息週期提供了無可爭辯的依據。數據爆冷排除了年內維持高利率的鷹派選項，長期對小盤股與發電等高槓桿實體企業反而是好消息。
        </p>
        <p>
          <strong>資金流向 (ETF Flow)</strong>：今日能源（XLE）與小盤股（IWM）錄得顯著機構淨流入；受 Reddit 加入標普影響，S&P 500 被動指數基金出現尾盤大額配置。與此同時，科技軟體（IGV）和半導體大型個股博通（AVGO）錄得機構流出。
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
          今日市場板塊輪動呈現<strong>「高位科技向小盤股、能源與公用發電防禦板塊分流」</strong>：
        </p>
        <ul class="list-disc pl-5 space-y-2">
          <li><strong>小盤股逆勢破頂</strong>：利率走低預期加強，高融資成本的中小企業股價持續補漲，羅素 2000（IWM）跑贏三大指數再創歷史新高。</li>
          <li><strong>AI硬體出現高度分化</strong>：博通（AVGO -5.94%）和應材（AMAT -4.50%）因個股與估值利空重挫，但資金並未完全撤出晶片主線，反而大舉湧入超微（AMD +6.50%）和 LITE（+5.19%）護盤。</li>
          <li><strong>電力與發電股獲資金避險</strong>：NRG Energy 大漲 5.42%，GE Vernova 續創歷史新高，電力是 AI 物理限制中最具確定性的防守反擊板塊。</li>
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
            <li><strong>Jackson Hole 央行年會</strong>：關注各央行官員發言對 9 月降息幅度的暗示。</li>
            <li><strong>十年期美債收益率 4.70% 水平</strong>：若能跌回 4.60% 平台，將進一步開啟中小型企業融資空間。</li>
            <li><strong>美元指數</strong>：觀察美元在 28.11 附近的支撐，弱勢美元將助推黃金與非美貨幣。</li>
          </ul>
        </div>
        
        <div class="p-5 rounded-xl bg-white dark:bg-zinc-900 border border-slate-200 dark:border-zinc-800/80 shadow-sm space-y-2">
          <h4 class="font-bold text-slate-800 dark:text-white">13.2 大盤指數觀察</h4>
          <ul class="list-decimal pl-5 space-y-1.5 text-slate-600 dark:text-zinc-400 text-xs font-sans">
            <li><strong>SPY (標普500)</strong>：小幅回踩 776，若能在 770 點平台築底，多頭突破勢頭依舊，下週有望再度衝刺 785 點。</li>
            <li><strong>QQQ (納指100)</strong>：守在 731 點，關鍵支撐看 724 點，50日均線（715點）是中期牛熊分界線。</li>
            <li><strong>IWM (羅素2000)</strong>：收於 305 點歷史高位，降息邏輯下小盤股有望繼續逼空。</li>
          </ul>
        </div>
        
        <div class="p-5 rounded-xl bg-white dark:bg-zinc-900 border border-slate-200 dark:border-zinc-800/80 shadow-sm space-y-2">
          <h4 class="font-bold text-slate-800 dark:text-white">13.3 個股與板塊聚焦</h4>
          <ul class="list-decimal pl-5 space-y-1.5 text-slate-600 dark:text-zinc-400 text-xs font-sans">
            <li><strong>Reddit (RDDT)</strong>：下週二納入 S&P 500 指數，預期週一仍有被動指數資金搶跑，高位波動加劇，不宜追高。</li>
            <li><strong>超微 (AMD)</strong>：放量大漲 6.50% 突破，均線走強，短線可在回調時大膽低吸。</li>
            <li><strong>博通 (AVGO)</strong>：大跌回踩 $390 平台，若能在美銀債務事件澄清後止跌，將是良好的中長線佈局點。</li>
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
              <td class="p-3 font-semibold">消費者支出衰退風險</td>
              <td class="p-3 text-center"><span class="px-2.5 py-0.5 rounded-full text-xs font-semibold bg-orange-100 dark:bg-orange-950/40 text-orange-700 dark:text-orange-300">中高</span></td>
              <td class="p-3 text-slate-500 dark:text-zinc-400">零售月率大跌0.6%顯示美國經濟的消費支柱正在軟化，可能在未來引發非AI類零售及大宗消費股股價下修。操作上建議避開傳統零售與非必需消費。</td>
            </tr>
            <tr>
              <td class="p-3 font-semibold">半導體高槓桿融資質疑</td>
              <td class="p-3 text-center"><span class="px-2.5 py-0.5 rounded-full text-xs font-semibold bg-yellow-100 dark:bg-yellow-950/40 text-yellow-700 dark:text-yellow-300">中</span></td>
              <td class="p-3 text-slate-500 dark:text-zinc-400">博通的債務融資質疑表明，高利率環境下大型併購與資本擴張的債務壓力正受到華爾街的放大檢視。短期應避開負債率偏高的晶片與科技股。</td>
            </tr>
            <tr>
              <td class="p-3 font-semibold">指數高位獲利回吐</td>
              <td class="p-3 text-center"><span class="px-2.5 py-0.5 rounded-full text-xs font-semibold bg-yellow-100 dark:bg-yellow-950/40 text-yellow-700 dark:text-yellow-300">中</span></td>
              <td class="p-3 text-slate-500 dark:text-zinc-400">大盤創高後累積了豐厚的獲利籌碼，在Jackson Hole央行年會前有避險離場要求。控制倉位，回調時分批低吸，避免盲目追高。</td>
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
          今日美股成功消化了爆冷的美國零售銷售數據利空。雖然數據走軟引燃了短期內消費者衰退的憂慮，拖累標普500指數和納斯達克指數自歷史高位回吐，但降息預期的鐵板釘釘也激勵資金流入小盤股（IWM），推升羅素 2000 指數再創歷史新高。雖然博通因融資事件重挫，但算力晶片股超微（AMD）和光互聯龍頭（LITE）大漲吸金，表明 AI 主線資金並未流失，大盤寬度依然健康。
        </p>
        <p>
          <strong>當前市場階段：</strong>
          <span class="text-emerald-400 font-bold">消費數據爆冷引發衰退擔憂 / 高位科技股與博通獲利回吐 / 降息預期深化助推小盤股創歷史新高</span>
        </p>
        <p>
          <strong>我的操作傾向：</strong>
          「分批建倉放量突破的算力巨頭 AMD，逢低佈局高位回調完成的博通 AVGO，同時避免追高即將納入標普的 Reddit」。電力基建龍頭 GEV 與 VRT 可繼續作為中線防禦配置持有。
        </p>
        <div class="p-3.5 bg-zinc-800 text-slate-300 rounded-lg text-xs">
          <strong>💡 下週最值得關注的 5 個信號：</strong>
          <ul class="list-decimal pl-5 mt-2 space-y-1">
            <li>下週二（8月18日）Reddit 納入 S&P 500 指數後的股價承接力。</li>
            <li>Jackson Hole 央行年會上聯準會主席鮑威爾對 9 月降息幅度的政策定調。</li>
            <li>超微（AMD）能否突破並站穩在 $515 平台之上。</li>
            <li>博通（AVGO）在 $390 關鍵支撐線的止跌信號。</li>
            <li>10年期美債收益率能否再次向 4.60% 進一步下行探底。</li>
          </ul>
        </div>
      </div>
    </section>

    <!-- Footer -->
    <footer class="mt-16 pt-8 border-t border-slate-200 dark:border-zinc-800 text-xs text-slate-500 dark:text-zinc-500 text-center space-y-1">
      <p>美股收盤日報 • 2026-08-14 版面模板 • 實際美股數據發布版 2026-08-14</p>
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
output_path = "/Users/wisdom/html-report-skill/reports/2026-08-14-us-stock-closing-daily-report.html"
with open(output_path, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"Generated report HTML at {output_path}")

# Run publish.py
publish_script = "/Users/wisdom/html-report-skill/.antigravitycli/skills/html-report/scripts/publish.py"
title = "美股收盤日報｜2026-08-14"
description = "週五（2026年8月14日），美股零售數據爆冷大跌0.6%引發衰退憂慮，三大指數自高點回調，但小盤股羅素2000逆勢創歷史新高，博通大跌近6%拖累半導體，Reddit因加入S&P 500飆升14%。"

cmd = [
    "python3",
    publish_script,
    output_path,
    title,
    description
]

print(f"Running publish script: {' '.join(cmd)}")
res = subprocess.run(cmd, capture_output=True, text=True)
print("Publish STDOUT:", res.stdout)
print("Publish STDERR:", res.stderr)
sys.exit(res.returncode)
