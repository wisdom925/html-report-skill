import json, re, subprocess, sys

R = "/Users/wisdom/html-report-skill/"
D = "2026-10-05"
q = json.load(open(R + "scratch/quotes_2026-10-05.json"))
t = json.load(open(R + "scratch/tech_2026-10-05.json"))
old = open(R + "reports/2026-10-02-us-stock-closing-daily-report.html", encoding="utf-8").read()

GREEN = "text-emerald-600 dark:text-emerald-400"
RED = "text-rose-500"


def P(k): return q[k]["pct"]
def PX(k, d=2): return f"{q[k]['price']:,.{d}f}"
def PC(k): return f"{P(k):+.2f}%"
def C(v, inv=False):
    up = v >= 0
    if inv: up = not up
    return (GREEN if up else RED) + " font-bold"
def CT(k, inv=False): return f'<span class="{C(P(k), inv)}">{PC(k)}</span>'
def RNG(k, d=2): return f"{q[k]['high']:,.{d}f} / {q[k]['low']:,.{d}f}"

CARD = "p-4 rounded-xl bg-white dark:bg-zinc-900 border border-slate-200 dark:border-zinc-850 shadow-sm"
BOX = "p-5 rounded-2xl bg-white dark:bg-zinc-900 border border-slate-200 dark:border-zinc-850 shadow-sm"
H2 = "text-xl font-bold mb-4 flex items-center gap-2 border-b border-slate-100 dark:border-zinc-800 pb-2"
THEAD = "bg-slate-50 dark:bg-zinc-800/60 border-b border-slate-200 dark:border-zinc-700 text-slate-500 dark:text-zinc-400"
TBODY = "divide-y divide-slate-100 dark:divide-zinc-800"
S = '<strong class="text-slate-900 dark:text-white font-semibold">'


def sec(n, title, body, extra=""):
    return f'''
    <section id="sec-{n}" class="scroll-mt-6 font-sans {extra}">
      <h2 class="{H2}"><span class="text-brand-500">{n}.</span> {title}</h2>
      {body}
    </section>
'''


def paras(items):
    return '<div class="space-y-3 text-sm leading-relaxed text-slate-700 dark:text-zinc-300">' + "".join(
        f"<p>{S}【{h}】</strong> {b}</p>" for h, b in items) + "</div>"


def table(headers, rows, tid=None, sortable=False, mono=False):
    th = ""
    for i, h in enumerate(headers):
        if sortable:
            num = "true" if i in sortable else "false"
            th += f'<th class="p-3 sortable" onclick="sortTable(\'{tid}\',{i},{num})">{h} ⇅</th>'
        else:
            th += f'<th class="p-3">{h}</th>'
    idattr = f' id="{tid}"' if tid else ""
    body = "".join("<tr class=\"hover:bg-slate-50 dark:hover:bg-zinc-800/30\">" + "".join(f'<td class="p-3">{c}</td>' for c in r) + "</tr>" for r in rows)
    return f'<div class="{BOX} overflow-x-auto"><table{idattr} class="w-full text-xs sm:text-sm text-left border-collapse"><thead class="{THEAD}"><tr>{th}</tr></thead><tbody class="{TBODY}{" font-mono" if mono else ""}">{body}</tbody></table></div>'


def stat(label, val, sub=""):
    return f'<div class="p-3 rounded-lg bg-slate-50 dark:bg-zinc-800/50 border border-slate-200 dark:border-zinc-700"><div class="text-xs text-slate-500">{label}</div><div class="text-lg font-bold">{val}</div><div class="text-xs">{sub}</div></div>'


def details(title, inner, op=False):
    return f'<details class="group p-4 rounded-xl bg-white dark:bg-zinc-900 border border-slate-200 dark:border-zinc-850 shadow-sm"{" open" if op else ""}><summary class="cursor-pointer font-bold text-slate-900 dark:text-white">{title}</summary><div class="mt-3 text-sm leading-relaxed text-slate-700 dark:text-zinc-300 space-y-2">{inner}</div></details>'


NA = '<span class="text-slate-400">未取得可查證數據</span>'

# ---------- header / head ----------
TITLE = "美股收盤日報｜2026-10-05"
DESC = ("週一（2026年10月5日）美股收高：標普500 +0.66%報7,773.95點、納指 +1.05%報27,477.31點創歷史收盤新高、道瓊 +0.18%報51,267.90點；"
        "輝達創收盤新高(+2.12%)、微軟 +1.48%領軍AI；施耐德以226億美元收購PTC、嘉里羅賓遜收購RXO；10年期殖利率升至5.31%、WTI 下跌2.1%至$89.18，ISM服務業PMI 54.9。")

head = old[: old.index("<!-- Header Block -->")]
head = re.sub(r"<title>.*?</title>", f"<title>{TITLE}｜納指創收盤新高、AI領漲、殖利率逼近5.3% ({D})</title>", head, flags=re.S)
head = re.sub(r'<meta name="description" content=".*?">', f'<meta name="description" content="{DESC}">', head, flags=re.S)
head = re.sub(r'<meta property="og:title" content=".*?">', f'<meta property="og:title" content="{TITLE}">', head)
head = re.sub(r'<meta property="og:description" content=".*?">', '<meta property="og:description" content="納指創收盤新高，輝達、微軟領漲，10年期殖利率升至5.31%，油價回落。">', head)
head = head.replace("2026-10-02", D)
head = head.replace("9. 財報解讀 (TSLA等)", "9. 財報與公司事件").replace("13. 下週交易計畫", "13. 明日交易計畫")

header = f'''<!-- Header Block -->
    <header class="border-b border-slate-200 dark:border-zinc-800 pb-6">
      <div class="flex flex-wrap items-center justify-between gap-3 mb-2">
        <span class="inline-flex items-center gap-1.5 px-3 py-1 rounded-full text-xs font-semibold bg-emerald-100 text-emerald-800 dark:bg-emerald-950 dark:text-emerald-300">
          <span class="w-2 h-2 rounded-full bg-emerald-500 animate-pulse"></span> 納指創收盤新高・AI主導・殖利率高位
        </span>
        <span class="text-xs text-slate-500 dark:text-zinc-500 font-mono">美東時間 {D} 16:00 收盤</span>
      </div>
      <h1 class="text-2xl sm:text-3xl lg:text-4xl font-extrabold tracking-tight text-slate-900 dark:text-white">{TITLE}</h1>
      <p class="mt-2 text-sm sm:text-base text-slate-600 dark:text-zinc-400">{DESC}</p>
    </header>
'''

# ---------- sec 0 ----------
s0 = f'''
    <section id="sec-0" class="scroll-mt-6 p-6 rounded-2xl bg-gradient-to-br from-white to-slate-50 dark:from-zinc-900 dark:to-zinc-950 border border-slate-200 dark:border-zinc-800 shadow-sm">
      <h2 class="{H2}"><span class="text-brand-500">0.</span> 今日一句話總結</h2>
      <div class="space-y-3 text-sm sm:text-base leading-relaxed text-slate-700 dark:text-zinc-300">
        <p>{S}【大盤走勢】</strong> 美股週一溫和收高。標普500 <strong>{PC("^GSPC")}</strong> 收 <strong>{PX("^GSPC")}</strong>，納斯達克綜合指數 <strong>{PC("^IXIC")}</strong> 收 <strong>{PX("^IXIC")}</strong>（創歷史收盤新高），道瓊 <strong>{PC("^DJI")}</strong> 收 <strong>{PX("^DJI")}</strong>；羅素2000 {PC("^RUT")}，費半 {PC("^SOX")} 收 {PX("^SOX")}。</p>
        <p>{S}【驅動因素】</strong> 以AI主線與個股為主：輝達創收盤新高（{PC("NVDA")}）、微軟 {PC("MSFT")}；併購消息（施耐德電機擬以約226億美元收購PTC，PTC 大漲約33%；C.H. Robinson 擬以58億美元收購RXO）提供題材。宏觀面，9月ISM服務業PMI 54.9（預期55.0、前值55.4）略低於預期但仍在擴張區，10年期殖利率升至 {PX("^TNX")}%，為本輪高位，限制了指數漲幅。</p>
        <p>{S}【資金偏好】</strong> 偏 Risk-On 但不極端：VIX 日內自 {q["^VIX"]["high"]:.2f} 回落、收 {PX("^VIX")}（{PC("^VIX")}，較前收微升）；WTI 原油 {PC("CL=F")}、Brent {PC("BZ=F")}，通膨壓力略緩；黃金持平。</p>
        <p>{S}【市場寬度】</strong> 代理指標顯示參與度尚可：等權標普 RSP {PC("RSP")} 與SPY（{PC("SPY")}）同步，11個板塊中10個收高（僅房地產 XLRE {PC("XLRE")} 下跌），但近一個月小型股仍落後（IWM {q["IWM"]["1m"]:+.2f}% vs SPY {q["SPY"]["1m"]:+.2f}%）。</p>
        <p>{S}【核心主線】</strong> AI 龍頭（NVDA、MSFT、TSM {PC("TSM")}、AVGO {PC("AVGO")}）延續強勢；電力股 CEG {PC("CEG")}、VST {PC("VST")} 跳升。需關注10月7日（週三）FOMC會議紀要與高位殖利率。</p>
        <div class="mt-4 p-4 rounded-xl bg-brand-50 dark:bg-zinc-800/60 border border-brand-100 dark:border-brand-900/40 text-brand-900 dark:text-brand-200 font-medium">
          💡 <strong>今日市場狀態判斷：</strong>「指數穩步創高、AI大型股主導；殖利率5.3%上方形成壓力，市場強而不躁。」
        </div>
      </div>
    </section>
'''

# ---------- sec 1 ----------
def card(name, key, px, sub):
    return f'<div class="{CARD}"><div class="text-xs text-slate-500 dark:text-zinc-400 font-medium">{name}</div><div class="text-xl font-extrabold font-mono mt-1">{px}</div><div class="text-xs mt-1 flex items-center justify-between"><span class="{C(P(key), key=="^VIX")}">{PC(key)}</span><span class="text-slate-400 font-mono">{sub}</span></div></div>'

cards = "".join([
    card("S&P 500 (標普500)", "^GSPC", PX("^GSPC"), f"SPY ${PX('SPY')}"),
    card("Nasdaq Composite", "^IXIC", PX("^IXIC"), "創收盤新高"),
    card("Dow Jones (道瓊)", "^DJI", PX("^DJI"), f"{q['^DJI']['change']:+.2f} 點"),
    card("Nasdaq 100", "^NDX", PX("^NDX"), f"QQQ ${PX('QQQ')}"),
    card("Russell 2000", "^RUT", PX("^RUT"), f"IWM ${PX('IWM')}"),
    card("SOX (費城半導體)", "^SOX", PX("^SOX"), f"SMH ${PX('SMH')}"),
    card("Software (IGV)", "IGV", PX("IGV"), "軟體反彈"),
    card("VIX", "^VIX", PX("^VIX"), "前收 15.31"),
])

idx_rows = []
def irow(name, etf, key, state):
    idx_rows.append([f'<span class="font-semibold font-sans">{name}</span>', etf, f'<b>{PX(key)}</b>', f'<span class="{C(P(key), key=="^VIX")}">{PC(key)}</span>', RNG(key), f'<span class="font-sans">{state}</span>'])
irow("S&P 500", "SPY", "^GSPC", "收7,773.95，距歷史高點約0.3%（來源報導），收盤接近日高(7,794.35)，SPY 在20/50/100/200日均線之上")
irow("Nasdaq Composite", "—", "^IXIC", "創歷史收盤新高，收盤貼近日高")
irow("Nasdaq 100", "QQQ", "^NDX", "QQQ 收756.20，貼近20日高點(756.91)；RSI 偏高(10-02: 75.8)")
irow("Dow Jones", "DIA", "^DJI", "落後大盤，近一個月仍偏弱 (-2.88%)")
irow("Russell 2000", "IWM", "^RUT", f"小盤落後標普(+0.50% vs +0.66%)；IWM 仍低於20/50/100日均線（10-02基準）")
irow("SOX 半導體", "SOXX / SMH", "^SOX", "近5日 +5.68%、近1月 +10.81%，今日僅 +0.27% 高位整固")
irow("CBOE VIX", "^VIX", "^VIX", "日內自16.38回落至15.52，仍處低波動區")
s1 = sec(1, "大盤表現總覽", f'''
      <div class="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-4 gap-4 mb-6">{cards}</div>
      <div class="{BOX}">
        <h3 class="text-sm font-semibold text-slate-700 dark:text-zinc-300 mb-3 flex items-center justify-between"><span>主要指數與核心資產當日漲跌幅對比 (Chart.js)</span><span class="text-xs font-normal text-slate-500">{D} 基準</span></h3>
        <div class="relative h-64 sm:h-72 w-full"><canvas id="overviewChart"></canvas></div>
      </div>
      <div class="mt-6">{table(["指數名稱", "代表ETF", "收盤點位", "當日漲跌幅", "日內高/低", "技術狀態"], idx_rows, mono=True)}</div>
      <p class="mt-3 text-sm text-slate-600 dark:text-zinc-400">補充：納指創歷史收盤新高；標普500 距歷史高點約0.3%，尚未確認創收盤新高；小盤股（羅素2000 +0.50%）跑輸標普500（+0.66%）；VIX 收15.52，較前收微升但日內明顯回落。</p>
''')

# ---------- sec 2 ----------
mer = f'''graph LR
  subgraph PreMarket["盤前"]
    A["ISM服務業PMI 54.9 略低於預期55.0<br/>施耐德宣布226億美元收購PTC<br/>C.H. Robinson 宣布收購RXO"]
  end
  subgraph Open["開盤"]
    B["標普開 {q['^GSPC']['open']:,.2f}（小幅高開）<br/>納指開 {q['^IXIC']['open']:,.2f}<br/>VIX 開 {q['^VIX']['open']:.2f}"]
  end
  subgraph Day["日內"]
    C["標普自開盤附近低點 {q['^GSPC']['low']:,.2f}<br/>逐步走高至日高 {q['^GSPC']['high']:,.2f}<br/>VIX 自 {q['^VIX']['high']:.2f} 回落"]
  end
  subgraph Close["收盤與盤後"]
    D["標普 +0.66% / 納指 +1.05% 創收盤新高<br/>10年期殖利率 5.31%<br/>下一關注: 週三FOMC會議紀要"]
  end
  PreMarket --> Open --> Day --> Close'''
s2 = sec(2, "盤中走勢復盤（時間線 Timeline）", f'''
      <div class="{BOX} overflow-x-auto"><div class="mermaid">
{mer}
      </div></div>
      <div class="mt-4 {BOX}">{paras([
    ("盤前", "ISM服務業PMI 9月 54.9（預期55.0、前值55.4），略低於預期但維持擴張；上週弱於預期的就業數據使市場對Fed升息的定價降溫。同日施耐德電機宣布以每股205美元（約226億美元）現金收購PTC，C.H. Robinson 宣布收購RXO。"),
    ("開盤後", f"標普500 開 {q['^GSPC']['open']:,.2f}（前收 {q['^GSPC']['prev']:,.2f}），日內低點 {q['^GSPC']['low']:,.2f} 與開盤相近，顯示開盤後賣壓有限；納指開 {q['^IXIC']['open']:,.2f}、低點 {q['^IXIC']['low']:,.2f} 亦貼近開盤價。"),
    ("午盤", "（日內分時資料以高低點推斷）指數自低位逐步墊高，費半日內區間 13,004.67–13,179.71，晶片股高位消化；10年期殖利率日內高點 5.35%，對成長股估值形成壓力但未破壞趨勢。"),
    ("尾盤", f"標普500 收 {PX('^GSPC')}，距日高 {q['^GSPC']['high']-q['^GSPC']['price']:.2f} 點；納指收 {PX('^IXIC')} 創收盤新高，VIX 自日高16.38回落至15.52。"),
    ("盤後與核心原因", "漲跌核心：AI龍頭（輝達創收盤新高、微軟 +1.48%）帶動，加上併購題材；利率（10年期5.31%）是主要制約。原油下跌約2%（中東原油出口增加、G7承諾增加供給）緩解通膨擔憂。未見明顯 sell-the-news，費半漲幅收斂屬高位整理。"),
])}</div>
''')

# ---------- sec 3 tabs ----------
def ybp(k):
    return f"{q[k]['change']*100:+.0f}bp"
yield_cards = "".join([
    stat("13週 (^IRX)", f"{PX('^IRX')}%", ybp("^IRX")),
    stat("5年 (^FVX)", f"{PX('^FVX')}%", ybp("^FVX")),
    stat("10年 (^TNX)", f"{PX('^TNX')}%", ybp("^TNX")),
    stat("30年 (^TYX)", f"{PX('^TYX')}%", ybp("^TYX")),
])
tab_y = f'''<div id="panel-yields" class="tab-panel space-y-4"><h4 class="font-bold text-slate-900 dark:text-white text-base">長天期殖利率續升，10年期站上5.3%</h4>
  <div class="grid grid-cols-2 sm:grid-cols-4 gap-3 font-mono">{yield_cards}</div>
  <p>10年期收 {PX("^TNX")}%（前收5.28%，日內區間 5.26–5.35%），近5日 +7bp 左右、近一個月上升約 {q["^TNX"]["1m"]:.1f}%（相對變動）；30年期 {PX("^TYX")}%。30年減5年利差由約58bp擴至約59bp，曲線略微陡峭化（2年期殖利率本次未取得）。市場含義：長端利率處於多年高位，反映政府債務與通膨擔憂，成長股估值對利率敏感。</p></div>'''
tab_f = '''<div id="panel-fed" class="tab-panel space-y-4"><h4 class="font-bold text-slate-900 dark:text-white text-base">Fed 10月會議：市場定價以按兵不動為主</h4>
  <div class="grid grid-cols-2 sm:grid-cols-3 gap-3 font-mono">''' + stat("10/27–28 維持利率", "約82%", "據市場定價報導（二手來源）") + stat("升息25bp", "約18%", "上週就業數據偏弱後明顯降溫") + stat("下一個催化", "10/7 週三", "FOMC會議紀要與Fed官員講話") + '''</div>
  <p>FedWatch 機率來自二手報導，非官方即時截圖，請以 CME 官網為準；年內預期次數未取得可查證數據。在10年期殖利率高於5.3%的背景下，市場關注會議紀要對縮表與利率路徑的措辭。</p></div>'''
tab_c = f'''<div id="panel-commodities" class="tab-panel space-y-4"><h4 class="font-bold text-slate-900 dark:text-white text-base">油價回落，美元偏強，黃金持平</h4>
  <div class="grid grid-cols-2 sm:grid-cols-3 gap-3 font-mono">
  {stat("美元（UUP代理）", "$"+PX("UUP"), CT("UUP"))}{stat("黃金期貨", "$"+PX("GC=F",1)+"/oz", CT("GC=F"))}{stat("WTI 原油", "$"+PX("CL=F"), CT("CL=F", True))}
  {stat("Brent 原油", "$"+PX("BZ=F"), CT("BZ=F", True))}{stat("比特幣", "$"+PX("BTC-USD",0), CT("BTC-USD"))}{stat("以太幣", "$"+PX("ETH-USD",0), CT("ETH-USD"))}</div>
  <p>DXY 指數本次未取得，使用美元ETF UUP（{PC("UUP")}）作為代理，顯示美元走強；WTI 日內收 ${PX("CL=F")}（{PC("CL=F")}），Brent 收 ${PX("BZ=F")}（{PC("BZ=F")}），原因包含中東原油出口增加與G7提升供給的表態；金價近1個月 {q["GC=F"]["1m"]:+.1f}%，在實質利率高位下承壓。加密資產小幅回落（加密貨幣為全天候交易，數字為該日收盤）。</p></div>'''
tab_d = '''<div id="panel-data" class="tab-panel space-y-4"><h4 class="font-bold text-slate-900 dark:text-white text-base">9月ISM服務業PMI 54.9，略低於預期</h4>
  <div class="overflow-x-auto"><table class="w-full text-sm text-left"><thead class="bg-slate-50 dark:bg-zinc-800/60"><tr><th class="p-3">數據</th><th class="p-3">實際</th><th class="p-3">預期</th><th class="p-3">前值</th><th class="p-3">市場解讀</th></tr></thead><tbody class="divide-y divide-slate-100 dark:divide-zinc-800">
  <tr><td class="p-3 font-semibold">ISM 服務業 PMI（9月）</td><td class="p-3 font-mono">54.9</td><td class="p-3 font-mono">55.0</td><td class="p-3 font-mono">55.4</td><td class="p-3">連續第27個月擴張，成長略降溫；對股市影響偏中性。</td></tr></tbody></table></div>
  <p>本日無其他主要經濟數據（CPI/PPI/非農等）公布。</p></div>'''
s3 = sec(3, "宏觀環境（利率、Fed、大宗商品與經濟數據）", f'''
      <div class="tabs {BOX}">
        <div class="flex flex-wrap items-center gap-2 border-b border-slate-200 dark:border-zinc-800 pb-3 mb-4">
          <input type="radio" id="tab-yields" name="macro-tabs" checked><label for="tab-yields">3.1 美債收益率</label>
          <input type="radio" id="tab-fed" name="macro-tabs"><label for="tab-fed">3.2 Fed 預期</label>
          <input type="radio" id="tab-commodities" name="macro-tabs"><label for="tab-commodities">3.3 美元・黃金・原油・加密</label>
          <input type="radio" id="tab-data" name="macro-tabs"><label for="tab-data">3.4 當日數據</label>
        </div>
        <div class="tab-content text-sm leading-relaxed text-slate-700 dark:text-zinc-300">{tab_y}{tab_f}{tab_c}{tab_d}</div>
      </div>''')

# ---------- sec 4 sectors ----------
sectors = [
    ("原物料", "XLB", "單日大漲，近1月仍偏弱 (-4.7%)，屬超跌反彈"),
    ("通訊服務", "XLC", "GOOGL +0.86%、META +1.90% 帶動"),
    ("能源", "XLE", "油價下跌但能源股逆勢上漲，近5日強"),
    ("金融", "XLF", "跟隨大盤；近1月仍落後 (-5.97%)"),
    ("醫療保健", "XLV", "防禦板塊收漲，但近5日 -2.27%；MRK 約 -3%"),
    ("必需消費", "XLP", "防禦資金溫和回流"),
    ("科技", "XLK", "NVDA +2.12%、MSFT +1.48%、AVGO +2.08%"),
    ("非必需消費", "XLY", "TSLA +2.2% 支撐，AMZN/AAPL 持平略跌"),
    ("公用事業", "XLU", "CEG +3.93%、VST +3.48% 與電力需求題材"),
    ("工業", "XLI", "近乎持平，ETN -0.80%"),
    ("房地產", "XLRE", "唯一下跌板塊，10年期殖利率上行壓力"),
]
sectors = sorted(sectors, key=lambda s: P(s[1]), reverse=True)
srows = []
for i, (n, e, drv) in enumerate(sectors, 1):
    d = P(e) - P("SPY")
    srows.append([str(i), f'<b>{n}</b>', e, f'<span class="{C(P(e))}">{PC(e)}</span>', f'{q[e]["5d"]:+.2f}%', f'{q[e]["1m"]:+.2f}%',
                  f'<span class="{C(d)}">{"跑贏" if d >= 0 else "跑輸"} ({d:+.2f}%)</span>', drv])
s4 = sec(4, "板塊表現（可排序／搜尋表格）", f'''
      <input id="sectorSearch" type="text" placeholder="搜尋板塊 / ETF…" class="mb-3 w-full sm:w-72 px-3 py-2 text-sm rounded-lg border border-slate-200 dark:border-zinc-700 bg-white dark:bg-zinc-900">
      {table(["排名", "板塊", "ETF", "當日", "近5日", "近1月", "相對SPY", "主要驅動"], srows, tid="sectorTable", sortable={0, 3, 4, 5})}
      <p class="mt-3 text-sm text-slate-600 dark:text-zinc-400">最強：原物料 XLB（{PC("XLB")}）、通訊服務 XLC（{PC("XLC")}）；最弱：房地產 XLRE（{PC("XLRE")}）。成長 vs 價值：IWO {PC("IWO")} 與 IWN {PC("IWN")} 均收高，成長略強；週期（XLB、XLE）與防禦（XLP、XLV）同步收高，輪動方向不明顯。AI→傳統電力/能源輪動：CEG、VST 與 XLE 同日走強，但 XLK 近5日仍領先 (+3.29%)，目前屬並行而非替代。</p>''')

# ---------- sec 5 themes ----------
themes = [
    ("半導體", "SMH", "SMH"), ("半導體", "SOXX", "SOXX"), ("軟體", "IGV", "IGV"),
    ("網路安全（代理）", "CRWD", "CRWD"), ("網路安全（代理）", "PANW", "PANW"),
    ("雲端運算（代理）", "NOW", "NOW"), ("AI/自動化（代理）", "PLTR", "PLTR"),
    ("光通訊（代理）", "LITE", "LITE"), ("光通訊（代理）", "COHR", "COHR"),
    ("資料中心/電力（代理）", "VRT", "VRT"), ("資料中心/電力（代理）", "GEV", "GEV"),
    ("儲能（代理）", "FLNC", "FLNC"),
    ("小盤成長", "IWO", "IWO"), ("小盤價值", "IWN", "IWN"), ("等權標普", "RSP", "RSP"), ("大盤成長（納指100）", "QQQ", "QQQ"),
]
note = {"SMH": "高位整理，近5日 +5.65%", "SOXX": "平盤附近，漲多整理", "IGV": "軟體反彈，近5日 +4.07%", "CRWD": "近1月 +29.8% 領漲", "PANW": "近1月 +20.7%",
        "NOW": "軟體龍頭反彈", "PLTR": "溫和上漲", "LITE": "近5日 +18.5%，短線擁擠", "COHR": "近5日 +18.1%，今日回吐",
        "VRT": "近1月 -12.8% 仍在修復", "GEV": "近5日 +4.2%", "FLNC": "近1月 -30.7% 偏弱", "IWO": "小盤成長領先小盤價值", "IWN": "小盤價值落後",
        "RSP": "與SPY同步，寬度尚可", "QQQ": "大型成長領漲"}
trows = [[n, f"<b>{e}</b>", f'<span class="{C(P(k))}">{PC(k)}</span>', f'{q[k]["5d"]:+.2f}%', f'{q[k]["1m"]:+.2f}%', note.get(e, "")] for n, e, k in themes]
s5 = sec(5, "主題與風格表現", table(["主題", "代表", "當日", "近5日", "近1月", "特徵"], trows, tid="themeTable", sortable={2, 3, 4}) + '<p class="mt-3 text-sm text-slate-600 dark:text-zinc-400">註：個別主題無單一ETF者使用代表個股作為代理，不等同主題指數。</p>')

# ---------- sec 6 breadth ----------
s6 = sec(6, "市場寬度與參與度", f'''
      <div class="space-y-4">
      <div class="{BOX}"><h3 class="font-semibold mb-2">6.1 均線參與度</h3>
      <p class="text-sm text-slate-700 dark:text-zinc-300">成分股站上20/50/100/200日均線的比例（如 S5TW/S5FI）{NA}；以下為代表ETF相對均線位置（均線、RSI 以10-02收盤計算）：</p>
      {table(["ETF", "SPY", "QQQ", "IWM"], [["20日均線", f'{t["SPY"]["sma20"]:.2f}', f'{t["QQQ"]["sma20"]:.2f}', f'{t["IWM"]["sma20"]:.2f}'], ["50日均線", f'{t["SPY"]["sma50"]:.2f}', f'{t["QQQ"]["sma50"]:.2f}', f'{t["IWM"]["sma50"]:.2f}'], ["200日均線", f'{t["SPY"]["sma200"]:.2f}', f'{t["QQQ"]["sma200"]:.2f}', f'{t["IWM"]["sma200"]:.2f}'], ["10-05收盤", PX("SPY"), PX("QQQ"), PX("IWM")]])}
      <p class="mt-2 text-sm text-slate-600 dark:text-zinc-400">SPY、QQQ 在所有主要均線之上，趨勢健康；IWM 仍低於20/50/100日均線，小型股中期趨勢偏弱。</p></div>
      <div class="{BOX}"><h3 class="font-semibold mb-2">6.2 漲跌家數、新高新低</h3><p class="text-sm">NYSE/Nasdaq 上漲/下跌家數、52週新高/新低 {NA}。代理：11個板塊中10個收高；SPY {PC("SPY")} vs RSP {PC("RSP")} 幾乎相同，說明當日上漲面不窄。</p></div>
      <div class="{BOX}"><h3 class="font-semibold mb-2">6.3 其他內部指標</h3><p class="text-sm">A/D Line、McClellan、Put/Call、VIX期限結構 {NA}。VIX 收 {PX("^VIX")}，近5日 {q["^VIX"]["5d"]:+.2f}%，仍處低波動區；成交量：標普500 成交量約 {q["^GSPC"]["volume"]/1e9:.2f} 十億股，Nasdaq 約 {q["^IXIC"]["volume"]/1e9:.2f} 十億股。</p></div>
      </div>''')

# ---------- sec 7 technicals ----------
def trow(sym, supp_res):
    x = t[sym]; p = q[sym]["price"]
    def pos(m): return "上" if p > x[m] else "下"
    macd = "多頭" if x["macd"] > 0 else "空頭"
    ob = "超買" if x["rsi"] >= 70 else ("超賣" if x["rsi"] <= 30 else "中性")
    return [f"<b>{sym}</b>", f"{p:.2f}", f'<span class="{C(P(sym))}">{PC(sym)}</span>', f'{pos("sma20")}({x["sma20"]:.1f})', f'{pos("sma50")}({x["sma50"]:.1f})', f'{pos("sma200")}({x["sma200"]:.1f})', f'{x["rsi"]:.0f} {ob}', macd, supp_res]
trs = []
for sym in ["SPY", "QQQ", "IWM", "SMH", "IGV", "XLK"]:
    x = t[sym]
    trs.append(trow(sym, f"支撐 {q[sym]['low']:.2f}（日低）/ {x['sma20']:.1f}（20日）；壓力 {max(q[sym]['high'], x['hi20']):.2f}（20日高）"))
s7 = sec(7, "技術面分析", table(["ETF", "收盤", "當日", "20日均線", "50日均線", "200日均線", "RSI(14)", "MACD", "支撐／壓力"], trs, mono=True) + f'''
      <p class="mt-3 text-sm text-slate-600 dark:text-zinc-400">註：均線/RSI/MACD 以Yahoo日線至10-02收盤計算（RSI 為10-02讀數），收盤價為10-05。判讀：SMH（RSI 88）與 XLK（RSI 83）處於極度超買，QQQ（76）偏超買，追高風險上升；IWM RSI 36 偏弱。明日多頭確認：SPY 收盤站穩日高 776.6 並創新高、QQQ 突破 756.9。風險位：SPY 失守 769.7（前收）、QQQ 失守 749（今日開盤區）。</p>''')

# ---------- sec 8 ----------
def line(sym, txt=""):
    return f'<tr><td class="p-2 font-semibold">{sym}</td><td class="p-2 font-mono">${PX(sym)}</td><td class="p-2 {C(P(sym))}">{PC(sym)}</td><td class="p-2 text-xs">近5日 {q[sym].get("5d", 0):+.1f}% / 近1月 {q[sym].get("1m", 0):+.1f}%</td><td class="p-2 text-xs">{txt}</td></tr>'
def tbl(rows):
    return f'<div class="overflow-x-auto"><table class="w-full text-sm text-left"><tbody class="divide-y divide-slate-100 dark:divide-zinc-800">{"".join(rows)}</tbody></table></div>'
m7 = tbl([line("NVDA", "創收盤新高，市值約5.76兆美元；摩根士丹利維持Overweight、目標價$300"), line("MSFT", "AI相關買盤，收漲1.48%"), line("AAPL", "小幅回落"), line("GOOGL", ""), line("AMZN", "持平"), line("META", "近1月 +20.9%，漲幅大"), line("TSLA", "收$378.73，近5日 +5.95%")])
m8 = tbl([line("AVGO"), line("TSM", "領漲晶片股"), line("AMD", "近1月 +24.9%，今日小回"), line("MRVL"), line("MU", ""), line("ASML"), line("ARM", "今日回吐1.5%，近5日仍+6.9%"), line("DELL", "-1.82%"), line("VRT"), line("ANET")])
m9 = tbl([line("CRM", "軟體中最弱"), line("NOW"), line("SNOW"), line("ORCL", "近5日 +7.5%"), line("ADBE"), line("PANW"), line("CRWD", "近1月 +29.8%"), line("PLTR")])
m10 = tbl([line("CEG", "領漲電力股"), line("VST", "跟漲"), line("NRG"), line("ETN", "-0.80%"), line("PWR"), line("GEV"), line("OKLO", "近1月 -17%")])
m11 = '''<ul class="list-disc pl-5 space-y-1"><li><b>PTC（約+33.5%）</b>：施耐德電機宣布以每股205美元（約226億美元）全現金收購，較前收溢價約42.3%，預計2027年第三季完成。</li>
<li><b>C.H. Robinson（約-10.8%）</b>：宣布以約58億美元現金加股票收購RXO（RXO約+22.5%）；市場擔憂融資、稀釋與整合風險，標普將其展望調為負面。</li>
<li><b>Merck（約-3%）</b>：收$144.30；JPMorgan 將目標價自150上調至165、維持Overweight；市場關注競品疫苗臨床數據（Vaxcyte）。MRK 將於10月29日公布Q3財報。</li></ul>'''
s8 = sec(8, "重點個股新聞與異動", '<div class="space-y-3">' + details("8.1 大型科技七巨頭", m7, True) + details("8.2 AI 硬體 / 半導體", m8) + details("8.3 軟體 / SaaS / AI 應用", m9) + details("8.4 AI 電力 / 資料中心 / 能源基礎設施", m10) + details("8.5 其他顯著異動（併購與評級）", m11) + '<p class="text-xs text-slate-500">註：未列出個別新聞者，表示未找到可查證的單一催化，漲跌依價格資料呈現。</p></div>')

# ---------- sec 9 ----------
s9 = sec(9, "財報日曆與公司事件", f'''<div class="space-y-4">
  <div class="{BOX}"><h3 class="font-semibold mb-2">9.1 昨夜（10/5）財報與公司事件</h3><p class="text-sm">10月5日無已查證的重要大型公司財報。重點為併購：施耐德電機收購PTC（約226億美元）、C.H. Robinson 收購RXO（約58億美元）。Q3財報季將自10月中旬由銀行股拉開序幕。</p></div>
  {table(["日期", "公司", "關注點"], [["10/6 週二", "Constellation Brands (STZ)、RPM、Lamb Weston (LW)、Neogen", "消費與食品通路需求、成本壓力"], ["10/7 週三", "Levi Strauss (LEVI)、Applied Digital (APLD)", "APLD 為AI資料中心題材股；同日FOMC會議紀要"], ["10/8 週四", "PepsiCo (PEP)、Progressive (PGR)", "消費者價格彈性、保險定價"]])}
  <p class="text-xs text-slate-500">日曆來源：Investing.com 財報日曆；EPS/營收預期未取得，請於公司IR確認。</p></div>''')

# ---------- sec 10 ----------
s10 = sec(10, "機構觀點與資金流", f'''{paras([
    ("評級／目標價", "摩根士丹利重申輝達 Overweight、目標價$300；JPMorgan 將默克目標價自$150上調至$165（Overweight）。其他華爾街大型策略師目標調整本日未取得可查證資料。"),
    ("ETF 資金流", f"ETF 資金流量數據 {NA}；價格面：SMH 近5日 +5.65%、SOXX +5.12%，IGV +4.07%，顯示半導體與軟體近期受資金追捧。"),
    ("大宗/內部人/期權", f"本日大宗交易、內部人交易與異常期權活動 {NA}。"),
])}''')

# ---------- sec 11 ----------
s11 = sec(11, "板塊輪動判斷", paras([
    ("資金流入", f"科技（XLK 近5日 {q['XLK']['5d']:+.2f}%）、半導體（SMH {q['SMH']['5d']:+.2f}%）、軟體（IGV {q['IGV']['5d']:+.2f}%）與能源（XLE {q['XLE']['5d']:+.2f}%）近5日領先；今日原物料、通訊、能源居前。"),
    ("資金流出／落後", f"醫療保健近5日 {q['XLV']['5d']:+.2f}%、必需消費 {q['XLP']['5d']:+.2f}%、房地產 {q['XLRE']['5d']:+.2f}%；小盤股近1月仍落後。"),
    ("AI 主線健康度與階段", "AI 龍頭（NVDA 創收盤新高）仍健康，但費半/半導體 RSI 極度超買、光通訊個股5日大漲近20%，擁擠度偏高；10年期殖利率5.3%以上是核心制約。研判為『強趨勢上漲中的高位整理』，延續概率高於頂部，但追高性價比下降。"),
]))

# ---------- sec 12 watchlist ----------
W = [
    ("NVDA", "繼續強勢", "創收盤新高；MS 目標$300"), ("AMD", "高位震盪", "近1月+24.9%，今日回吐"), ("AVGO", "繼續強勢", "+2.08% 領漲晶片"),
    ("MRVL", "高位震盪", "近5日+7.7%後整理"), ("GOOGL", "繼續強勢", "通訊板塊領漲之一"), ("MSFT", "繼續強勢", "+1.48% 收$525"),
    ("META", "短線過熱", "近1月+20.9%"), ("AMZN", "需要觀察", "窄幅，無明確方向"), ("ORCL", "低位修復", "近1月-12.3%，近5日反彈7.5%"),
    ("CRM", "破位風險", "近1月-7.8%，今日-2.1%最弱"), ("NOW", "低位修復", "+1.27% 軟體反彈"), ("SNOW", "高位震盪", "小跌-0.6%"),
    ("ADBE", "低位修復", "近1月-7.2%，小幅反彈"), ("PLTR", "高位震盪", "近1月+11.2%"), ("LITE", "短線過熱", "近5日+18.5%"),
    ("COHR", "短線過熱", "近5日+18.1%，今日回吐-1.0%"), ("ANET", "高位震盪", "-0.22%"), ("FLNC", "破位風險", "近1月-30.7%"),
    ("OKLO", "破位風險", "近1月-17.0%，近5日-3.1%"), ("VST", "低位修復", "+3.48%，近1月仍-4.5%"), ("CEG", "低位修復", "+3.93%，近1月-10.5%"),
    ("ETN", "高位震盪", "-0.80%"), ("VRT", "低位修復", "近1月-12.8%，近5日+3.9%"),
]
TAGC = {"繼續強勢": "bg-emerald-100 text-emerald-700", "高位震盪": "bg-yellow-100 text-yellow-700", "短線過熱": "bg-orange-100 text-orange-700", "需要觀察": "bg-zinc-100 text-zinc-700", "低位修復": "bg-sky-100 text-sky-700", "破位風險": "bg-rose-100 text-rose-700"}
wrows = []
for s, tag, nt in W:
    wrows.append([f"<b>{s}</b>", f"${PX(s)}", f'<span class="{C(P(s))}">{PC(s)}</span>', f'{q[s].get("5d", 0):+.1f}% / {q[s].get("1m", 0):+.1f}%', f'<span class="font-mono text-xs">日低 {q[s]["low"]:,.2f} / 日高 {q[s]["high"]:,.2f}</span>', nt, f'<span class="px-2 py-0.5 rounded text-xs font-semibold {TAGC[tag]}">{tag}</span>'])
s12 = sec(12, "我的重點關注股觀察", f'''<input id="watchSearch" type="text" placeholder="搜尋股票…" class="mb-3 w-full sm:w-72 px-3 py-2 text-sm rounded-lg border border-slate-200 dark:border-zinc-700 bg-white dark:bg-zinc-900">
  {table(["代號", "收盤", "當日", "近5日／近1月", "短線關鍵位（日內）", "關鍵訊息", "判定"], wrows, tid="watchTable", sortable={2})}
  <p class="mt-2 text-xs text-slate-500">標籤為依價格趨勢的機械式判定，非投資建議。</p>''')

# ---------- sec 13 ----------
s13 = sec(13, "明日交易計畫 / 觀察清單", f'''<div class="space-y-4">
  <div class="{BOX}"><h3 class="font-semibold mb-2">13.1 宏觀觀察</h3><ul class="list-disc pl-5 text-sm space-y-1"><li>10年期殖利率能否守在5.35%（日高）下方；30年期5.66%。</li><li>WTI $89 / Brent $100 的走勢與G7供給表態。</li><li>10/7（週三）FOMC會議紀要與Fed官員講話；美元（UUP）續強與否。</li><li>VIX 能否維持15–16。</li></ul></div>
  <div class="{BOX}"><h3 class="font-semibold mb-2">13.2 大盤觀察</h3><p class="text-sm">SPY：壓力 776.6（今日高）、支撐 769.7（前收）/769.69（今日低）。QQQ：壓力 756.9、支撐 749。IGV（{PX("IGV")}，近5日 +4.1%）與 IWM（{PX("IWM")}，仍低於主要均線）是否續跑贏是寬度確認指標。</p></div>
  <div class="{BOX}"><h3 class="font-semibold mb-2">13.3 板塊與個股觀察</h3><p class="text-sm">NVDA、MSFT、AVGO、TSM（AI龍頭是否續創高）；META（近1月+20.9%過熱）；CEG、VST（電力股續強）；LITE、COHR（光通訊擁擠）；CRM（軟體最弱）；PTC、RXO、CHRW（併購後走勢）；MRK（醫療弱勢）；APLD（10/7財報）；STZ/PEP（消費財報）；ORCL、ADBE（低位修復）；FLNC、OKLO（弱勢是否止穩）。</p></div></div>''')

# ---------- sec 14 risk ----------
RC = {"高": "bg-rose-100 text-rose-700", "中高": "bg-orange-100 text-orange-700", "中": "bg-yellow-100 text-yellow-700", "低": "bg-emerald-100 text-emerald-700"}
risks = [("宏觀利率", "高", "10年期5.31%、30年期5.66%處多年高位；市場仍定價約18%升息機率"),
         ("市場寬度", "中高", "近1月RSP -2.6%、IWM -3.8%落後SPY +1.2%，指數創高依賴大型股"),
         ("AI 擁擠度", "中高", "SMH RSI 88、LITE/COHR 5日漲約18%，高位波動放大"),
         ("財報風險", "中", "Q3財報季尚未全面展開，本週以消費財報為主"),
         ("地緣／油價", "中", "Brent 約$100，油價單日大幅波動"),
         ("技術面", "中高", "多項大型ETF超買，若殖利率續升易回檔"),
         ("流動性／債務", "中", "長端殖利率上行反映債務與期限溢價擔憂")]
s14 = sec(14, "風險提示（風險矩陣）", table(["風險維度", "評級", "解讀"], [[f"<b>{a}</b>", f'<span class="px-2 py-0.5 rounded font-semibold {RC[b]}">{b}</span>', c] for a, b, c in risks]))

# ---------- sec 15 ----------
s15 = f'''
    <section id="sec-15" class="scroll-mt-6 p-6 rounded-2xl bg-gradient-to-br from-white to-slate-50 dark:from-zinc-900 dark:to-zinc-950 border border-slate-200 dark:border-zinc-800 shadow-sm">
      <h2 class="{H2}"><span class="text-brand-500">15.</span> 最終結論</h2>
      <div class="space-y-3 text-sm sm:text-base leading-relaxed text-slate-700 dark:text-zinc-300">
        <p><strong>今日市場結論：</strong>標普500收 {PX("^GSPC")}（{PC("^GSPC")}）、納指收 {PX("^IXIC")}（{PC("^IXIC")}）創收盤新高，AI龍頭領漲，併購與原油回落提供支撐；10年期殖利率5.31%與偏高擁擠度是主要制約。</p>
        <p><strong>當前市場階段：</strong>強趨勢上漲中的高位震盪（板塊輪動並行）。</p>
        <p><strong>我的操作傾向（中性表述）：</strong>趨勢仍偏多，但超買（SMH、XLK）與殖利率風險使追高性價比下降；偏向等待回踩或殖利率回落確認，AI龍頭與電力股值得關注，小盤與房地產需謹慎。</p>
        <div><strong>最值得關注的 5 個訊號：</strong>
          <ol class="list-decimal pl-6 mt-2 space-y-1">
            <li>10年期殖利率是否突破5.35%。</li>
            <li>10/7 FOMC會議紀要對升息/按兵不動的措辭。</li>
            <li>NVDA 與費半能否在超買下守住漲幅。</li>
            <li>IWM、RSP 是否追上SPY，改善寬度。</li>
            <li>WTI/Brent 油價與美元（UUP）方向。</li>
          </ol></div>
        <p class="text-xs text-slate-500">資料與限制：價格取自 Yahoo Finance，新聞與經濟數據取自公開報導（Reuters/Bloomberg/BNN、Investing.com、ForexFactory、公司新聞稿）；寬度、ETF資金流、DXY、2年期殖利率等未取得項目已標示。非投資建議。</p>
      </div>
    </section>
'''

# ---------- tail ----------
tail = old[old.index("<!-- Footer -->"):]
tail = re.sub(r"<div>美股收盤日報｜資料來源：.*?</div>", "<div>美股收盤日報｜資料來源：Yahoo Finance、Reuters、Bloomberg/BNN、Investing.com、ISM、公司新聞稿</div>", tail)
labels = ['標普500 (SPY)', '納斯達克 (QQQ)', '道瓊 (DIA)', '羅素2000 (IWM)', '半導體 (SMH)', '費半 (SOXX)', '軟體 (IGV)', '科技 (XLK)']
keys = ["SPY", "QQQ", "DIA", "IWM", "SMH", "SOXX", "IGV", "XLK"]
chart_js = f"""// Overview Chart (Chart.js)
  const ctx = document.getElementById('overviewChart').getContext('2d');
  new Chart(ctx, {{
    type: 'bar',
    data: {{ labels: {json.dumps(labels, ensure_ascii=False)},
      datasets: [{{ label: '當日漲跌幅 (%)', data: {json.dumps([P(k) for k in keys])},
        backgroundColor: {json.dumps(['#10b981' if P(k) >= 0 else '#f43f5e' for k in keys])}, borderRadius: 6 }}] }},
    options: {{ responsive: true, maintainAspectRatio: false, plugins: {{ legend: {{ display: false }},
      tooltip: {{ callbacks: {{ label: function(c) {{ return ' 漲跌幅: ' + (c.raw >= 0 ? '+' : '') + c.raw + '%'; }} }} }} }},
      scales: {{ y: {{ grid: {{ color: 'rgba(148,163,184,0.15)' }}, ticks: {{ callback: function(v) {{ return v + '%'; }} }} }}, x: {{ grid: {{ display: false }} }} }} }}
  }});

  """
a = tail.index("// Overview Chart (Chart.js)")
b = tail.index("// Vanilla JS Search / Filter for Sectors")
tail = tail[:a] + chart_js + tail[b:]

main_open = '''<div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8 flex gap-8">'''
html = head + header + s0 + s1 + s2 + s3 + s4 + s5 + s6 + s7 + s8 + s9 + s10 + s11 + s12 + s13 + s14 + s15 + "\n  </main>\n</div>\n\n" + tail
out = R + "reports/2026-10-05-us-stock-closing-daily-report.html"
open(out, "w", encoding="utf-8").write(html)
print("written", out, len(html))
if "--no-publish" in sys.argv:
    sys.exit(0)
pub = R + ".antigravitycli/skills/html-report/scripts/publish.py"
res = subprocess.run(["python3", pub, out, TITLE, DESC], capture_output=True, text=True)
print(res.stdout, res.stderr)
sys.exit(res.returncode)
