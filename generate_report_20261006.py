import json, re, subprocess, sys

R = "/Users/wisdom/html-report-skill/"
D = "2026-10-06"
q = json.load(open(R + "scratch/quotes_2026-10-06.json"))
t = json.load(open(R + "scratch/tech_2026-10-06.json"))
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
TITLE = "美股收盤日報｜2026-10-06"
DESC = ("週二（2026年10月6日）美股收高：標普500 +0.58%報7,818.93點、納指 +0.45%報27,599.89點，兩者創歷史收盤新高、道瓊 +0.49%報51,521.28點；"
        "10年期殖利率回落至5.27%，電力股爆發（CEG +12.3%、VST +10.8%）、Marvell 投資人日帶動AI客製晶片股（MRVL +5.8%、AVGO +3.7%）；小型股逆勢走弱（羅素2000 -0.59%）。")

head = old[: old.index("<!-- Header Block -->")]
head = re.sub(r"<title>.*?</title>", f"<title>{TITLE}｜標普納指雙創收盤新高、殖利率回落、電力股爆發 ({D})</title>", head, flags=re.S)
head = re.sub(r'<meta name="description" content=".*?">', f'<meta name="description" content="{DESC}">', head, flags=re.S)
head = re.sub(r'<meta property="og:title" content=".*?">', f'<meta property="og:title" content="{TITLE}">', head)
head = re.sub(r'<meta property="og:description" content=".*?">', '<meta property="og:description" content="標普、納指創收盤新高，殖利率回落至5.27%，電力股與AI客製晶片股領漲，小型股走弱。">', head)
head = head.replace("2026-10-02", D)
head = head.replace("9. 財報解讀 (TSLA等)", "9. 財報與公司事件").replace("13. 下週交易計畫", "13. 明日交易計畫")

header = f'''<!-- Header Block -->
    <header class="border-b border-slate-200 dark:border-zinc-800 pb-6">
      <div class="flex flex-wrap items-center justify-between gap-3 mb-2">
        <span class="inline-flex items-center gap-1.5 px-3 py-1 rounded-full text-xs font-semibold bg-emerald-100 text-emerald-800 dark:bg-emerald-950 dark:text-emerald-300">
          <span class="w-2 h-2 rounded-full bg-emerald-500 animate-pulse"></span> 標普納指雙創收盤新高・殖利率回落・電力股爆發
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
        <p>{S}【大盤走勢】</strong> 美股週二續創新高。標普500 <strong>{PC("^GSPC")}</strong> 收 <strong>{PX("^GSPC")}</strong>，納斯達克綜合指數 <strong>{PC("^IXIC")}</strong> 收 <strong>{PX("^IXIC")}</strong>（兩者創歷史收盤新高），道瓊 <strong>{PC("^DJI")}</strong> 收 <strong>{PX("^DJI")}</strong>；但羅素2000 {PC("^RUT")}，費半 {PC("^SOX")} 收 {PX("^SOX")}。</p>
        <p>{S}【驅動因素】</strong> 美債殖利率自多年高位回落（10年期 {PX("^TNX")}%，較前日下降約4bp）、Q3財報季前盈利預期樂觀，以及AI主線擴散。個股面：Constellation 與Google簽20年購電協議（CEG {PC("CEG")}）、DOE 向 Vistra 提供最高42億美元有條件貸款承諾（VST {PC("VST")}）引爆電力股；Marvell 投資人日將FY2028營收目標上調至200億美元（MRVL {PC("MRVL")}），帶動 AVGO {PC("AVGO")}、ANET {PC("ANET")}。宏觀面，8月貿易逆差擴大至1,056億美元（高於預期約1,020億）。</p>
        <p>{S}【資金偏好】</strong> Risk-On：VIX 收 {PX("^VIX")}（{PC("^VIX")}），日內區間 {q["^VIX"]["low"]:.2f}–{q["^VIX"]["high"]:.2f}，低波動；WTI 原油 {PC("CL=F")}（收 ${PX("CL=F")}）、黃金期貨 {PC("GC=F")}；美元（UUP）{PC("UUP")}。</p>
        <p>{S}【市場寬度】</strong> 大型股強、小型股弱：11個板塊中10個收高（僅醫療保健 XLV {PC("XLV")} 下跌），公用事業 XLU {PC("XLU")} 領漲，等權 RSP {PC("RSP")} 與 SPY（{PC("SPY")}）同步；但羅素2000 {PC("^RUT")}、IWO {PC("IWO")}，近一個月小型股仍落後（IWM {q["IWM"]["1m"]:+.2f}% vs SPY {q["SPY"]["1m"]:+.2f}%）。</p>
        <p>{S}【核心主線】</strong> AI 基礎設施「電力＋客製晶片＋網通」擴散：CEG、VST、NRG {PC("NRG")}、PWR {PC("PWR")}、GEV {PC("GEV")}、ETN {PC("ETN")} 全線走強。今日盤後 Constellation Brands 公布財報；10月7日（週三）FOMC會議紀要為下一個催化。</p>
        <div class="mt-4 p-4 rounded-xl bg-brand-50 dark:bg-zinc-800/60 border border-brand-100 dark:border-brand-900/40 text-brand-900 dark:text-brand-200 font-medium">
          💡 <strong>今日市場狀態判斷：</strong>「指數創高、AI電力與客製晶片領漲、殖利率回落提供支撐；但小型股走弱、寬度分歧，短線擁擠度仍高。」
        </div>
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
    card("Software (IGV)", "IGV", PX("IGV"), "軟體續彈"),
    card("VIX", "^VIX", PX("^VIX"), "前收 15.52"),
])

idx_rows = []
def irow(name, etf, key, state):
    idx_rows.append([f'<span class="font-semibold font-sans">{name}</span>', etf, f'<b>{PX(key)}</b>', f'<span class="{C(P(key), key=="^VIX")}">{PC(key)}</span>', RNG(key), f'<span class="font-sans">{state}</span>'])
irow("S&P 500", "SPY", "^GSPC", "創歷史收盤新高（據報導），收盤 7,818.93 距日高(7,844.52)約25點；SPY 在20/50/100/200日均線之上，RSI 72")
irow("Nasdaq Composite", "—", "^IXIC", "創歷史收盤新高，開盤後窄幅整理")
irow("Nasdaq 100", "QQQ", "^NDX", "QQQ 收759.66，創20日新高區；RSI 83 偏超買")
irow("Dow Jones", "DIA", "^DJI", "收51,521.28，跟隨大盤；近一個月仍偏弱 (-3.54%)")
irow("Russell 2000", "IWM", "^RUT", f"小盤逆勢下跌(-0.59%)，明顯跑輸標普(+0.58%)；IWM 仍低於20/50日均線")
irow("SOX 半導體", "SOXX / SMH", "^SOX", "近5日 +4.66%、近1月 +12.63%；今日 +0.34%，SMH/SOXX 小幅下跌，高位整固")
irow("CBOE VIX", "^VIX", "^VIX", "收15.01，日內自15.54回落，仍處低波動區")
s1 = sec(1, "大盤表現總覽", f'''
      <div class="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-4 gap-4 mb-6">{cards}</div>
      <div class="{BOX}">
        <h3 class="text-sm font-semibold text-slate-700 dark:text-zinc-300 mb-3 flex items-center justify-between"><span>主要指數與核心資產當日漲跌幅對比 (Chart.js)</span><span class="text-xs font-normal text-slate-500">{D} 基準</span></h3>
        <div class="relative h-64 sm:h-72 w-full"><canvas id="overviewChart"></canvas></div>
      </div>
      <div class="mt-6">{table(["指數名稱", "代表ETF", "收盤點位", "當日漲跌幅", "日內高/低", "技術狀態"], idx_rows, mono=True)}</div>
      <p class="mt-3 text-sm text-slate-600 dark:text-zinc-400">補充：標普500 與納指均創歷史收盤新高；小盤股（羅素2000 -0.59%）明顯跑輸標普500（+0.58%）；VIX 收15.01，較前收下降 0.51。</p>
''')

# ---------- sec 2 ----------
mer = f'''graph LR
  subgraph PreMarket["盤前"]
    A["8月貿易逆差擴至1,056億美元<br/>殖利率自高位回落<br/>CEG-Google購電協議、VST獲DOE貸款承諾"]
  end
  subgraph Open["開盤"]
    B["標普開 {q['^GSPC']['open']:,.2f}（小幅高開）<br/>納指開 {q['^IXIC']['open']:,.2f}<br/>VIX 開 {q['^VIX']['open']:.2f}"]
  end
  subgraph Day["日內"]
    C["標普自開盤價(日低 {q['^GSPC']['low']:,.2f})<br/>逐步走高至日高 {q['^GSPC']['high']:,.2f}<br/>Marvell投資人日帶動AI客製晶片股"]
  end
  subgraph Close["收盤與盤後"]
    D["標普 +0.58% / 納指 +0.45% 創收盤新高<br/>10年期殖利率 5.27%<br/>盤後: STZ 財報；下一關注: 週三FOMC會議紀要"]
  end
  PreMarket --> Open --> Day --> Close'''
s2 = sec(2, "盤中走勢復盤（時間線 Timeline）", f'''
      <div class="{BOX} overflow-x-auto"><div class="mermaid">
{mer}
      </div></div>
      <div class="mt-4 {BOX}">{paras([
    ("盤前", "美國8月貿易逆差擴大至1,056億美元（預期約1,020億，7月修正值928億），進口創歷史新高（半導體、資本財、原油）。Constellation 宣布與Google 20年購電協議（投資逾43億美元提升11座核反應爐出力），DOE 確認對 Vistra 最高42億美元有條件貸款承諾。"),
    ("開盤後", f"標普500 開 {q['^GSPC']['open']:,.2f}（前收 {q['^GSPC']['prev']:,.2f}），開盤價即為日內低點，顯示賣壓有限；納指開 {q['^IXIC']['open']:,.2f}、日低 {q['^IXIC']['low']:,.2f}。電力股開盤即跳空走高。"),
    ("午盤", "（日內分時資料以高低點推斷）指數自低位墊高；Marvell 投資人日公布FY2028營收目標200億美元、FY2031目標700–900億美元，MRVL 日內區間 267.26–301.27，自低位大幅拉升，AVGO、ANET 同步走強；SOX 日內區間 13,196.50–13,349.96。"),
    ("尾盤", f"標普500 收 {PX('^GSPC')}，距日高 {q['^GSPC']['high']-q['^GSPC']['price']:.2f} 點；納指收 {PX('^IXIC')} 創收盤新高，VIX 收 {PX('^VIX')}。"),
    ("盤後與核心原因", "漲跌核心：殖利率回落（10年期 5.27%）＋AI基礎設施題材（電力、客製晶片、網通）。盤後 Constellation Brands(STZ) 公布FQ2：EPS $3.74（預期$3.61）、營收$26.3億（預期$25.4億），但維持全年EPS指引$11.20–11.90（中值低於共識$11.72），股價盤後約跌2.7%。半導體ETF（SMH/SOXX）微跌屬高位整理，未見明顯 sell-the-news。"),
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
tab_y = f'''<div id="panel-yields" class="tab-panel space-y-4"><h4 class="font-bold text-slate-900 dark:text-white text-base">長天期殖利率自高位回落，10年期降至5.27%</h4>
  <div class="grid grid-cols-2 sm:grid-cols-4 gap-3 font-mono">{yield_cards}</div>
  <p>10年期收 {PX("^TNX")}%（前收5.31%，日內區間 5.26–5.30%），較前日下降約4bp，近一個月上升約 {q["^TNX"]["1m"]:.1f}%（相對變動）；30年期 {PX("^TYX")}%（-2bp）、5年期 {PX("^FVX")}%（-4bp）。30年減5年利差由約59bp擴至約61bp，曲線略微陡峭化（2年期殖利率本次未取得）。市場含義：中長端殖利率自多年高位回落，緩解成長股估值壓力，但仍處高位。</p></div>'''
tab_f = '''<div id="panel-fed" class="tab-panel space-y-4"><h4 class="font-bold text-slate-900 dark:text-white text-base">Fed 10月會議：市場傾向按兵不動，12月升息仍有定價</h4>
  <div class="grid grid-cols-2 sm:grid-cols-3 gap-3 font-mono">''' + stat("10/27–28 維持利率", "多數定價", "據報導，上週就業數據弱於預期後升息機率降溫") + stat("12月升息", "仍有定價", "據報導大致已定價（二手來源）") + stat("下一個催化", "10/7 週三", "FOMC會議紀要與Fed官員講話") + '''</div>
  <p>FedWatch 具體機率本次未取得可查證的官方即時數據（前一份報告引述的約82%維持／18%升息為二手來源，未更新），請以 CME 官網為準；年內預期次數未取得可查證數據。市場關注會議紀要對利率路徑與縮表的措辭。</p></div>'''
tab_c = f'''<div id="panel-commodities" class="tab-panel space-y-4"><h4 class="font-bold text-slate-900 dark:text-white text-base">美元走弱、黃金反彈、油價小幅上揚</h4>
  <div class="grid grid-cols-2 sm:grid-cols-3 gap-3 font-mono">
  {stat("美元（UUP代理）", "$"+PX("UUP"), CT("UUP"))}{stat("黃金期貨", "$"+PX("GC=F",1)+"/oz", CT("GC=F"))}{stat("WTI 原油", "$"+PX("CL=F"), CT("CL=F", True))}
  {stat("Brent 原油", "$"+PX("BZ=F"), CT("BZ=F", True))}{stat("比特幣", "$"+PX("BTC-USD",0), CT("BTC-USD"))}{stat("以太幣", "$"+PX("ETH-USD",0), CT("ETH-USD"))}</div>
  <p>DXY 指數本次未取得，使用美元ETF UUP（{PC("UUP")}）作為代理，顯示美元小幅走弱；WTI 期貨 ${PX("CL=F")}（{PC("CL=F")}），Brent ${PX("BZ=F")}（{PC("BZ=F")}），Yahoo 期貨報價為收盤後時點，與盤中走勢可能有差；黃金期貨 {PC("GC=F")}，但近1個月仍 {q["GC=F"]["1m"]:+.1f}%，在實質利率高位下承壓。加密資產小幅回落（加密貨幣為全天候交易，數字為該日收盤）。</p></div>'''
tab_d = '''<div id="panel-data" class="tab-panel space-y-4"><h4 class="font-bold text-slate-900 dark:text-white text-base">8月貿易逆差擴大至1,056億美元，高於預期</h4>
  <div class="overflow-x-auto"><table class="w-full text-sm text-left"><thead class="bg-slate-50 dark:bg-zinc-800/60"><tr><th class="p-3">數據</th><th class="p-3">實際</th><th class="p-3">預期</th><th class="p-3">前值</th><th class="p-3">市場解讀</th></tr></thead><tbody class="divide-y divide-slate-100 dark:divide-zinc-800">
  <tr><td class="p-3 font-semibold">貿易收支（8月）</td><td class="p-3 font-mono">-$105.6B</td><td class="p-3 font-mono">約 -$102.0B</td><td class="p-3 font-mono">-$92.8B（修正）</td><td class="p-3">進口創歷史新高$420.8B（+4.3%，原油、半導體、資本財），出口$315.2B（+1.4%）；反映內需強勁與AI設備進口，對股市影響偏中性。</td></tr></tbody></table></div>
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
    ("原物料", "XLB", "溫和收高，近1月仍偏弱 (-5.2%)"),
    ("通訊服務", "XLC", "近乎持平，META -0.41% 拖累"),
    ("能源", "XLE", "油價小幅上揚，近5日 +3.6%"),
    ("金融", "XLF", "小幅收高，近1月仍落後 (-7.0%)"),
    ("醫療保健", "XLV", "唯一下跌板塊，近5日 -2.1%"),
    ("必需消費", "XLP", "防禦資金回流"),
    ("科技", "XLK", "AVGO +3.67%、MSFT +0.78%、NVDA +0.14%"),
    ("非必需消費", "XLY", "AMZN +1.95%、TSLA +0.51% 支撐"),
    ("公用事業", "XLU", "CEG +12.25%、VST +10.77%、NRG +7.02% 領漲"),
    ("工業", "XLI", "PWR +5.29%、GEV +3.96%、ETN +2.89% 電力基建帶動"),
    ("房地產", "XLRE", "殖利率回落帶動反彈"),
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
      <p class="mt-3 text-sm text-slate-600 dark:text-zinc-400">最強：公用事業 XLU（{PC("XLU")}）、工業 XLI（{PC("XLI")}）、非必需消費 XLY（{PC("XLY")}）；最弱：醫療保健 XLV（{PC("XLV")}）。成長 vs 價值：IWO {PC("IWO")} 與 IWN {PC("IWN")} 均下跌，小盤成長更弱；大型成長（QQQ {PC("QQQ")}）勝過小盤。AI→傳統電力/能源輪動：電力股（CEG、VST、NRG）與電力設備（PWR、GEV、ETN）同日大漲，XLU 與 XLI 領漲而 XLK 僅 {PC("XLK")}，屬「AI主線向電力基礎設施擴散」的明確跡象，但 XLK 近5日仍 {q["XLK"]["5d"]:+.2f}%，並非替代而是擴散。</p>''')

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
note = {"SMH": "高位整理，近5日 +4.22%", "SOXX": "平盤附近，漲多整理", "IGV": "軟體續彈，近5日 +5.65%", "CRWD": "近1月 +30.9% 領漲", "PANW": "近1月 +26.0%，今日大漲",
        "NOW": "軟體龍頭續彈", "PLTR": "溫和上漲", "LITE": "近5日 +16.4%，短線擁擠", "COHR": "近5日 +15.8%",
        "VRT": "近1月 -9.8% 仍在修復", "GEV": "近5日 +6.9%，電力設備領漲", "FLNC": "近1月 -22.4% 偏弱，今日反彈", "IWO": "小盤成長走弱", "IWN": "小盤價值走弱",
        "RSP": "與SPY同步，大型股寬度尚可", "QQQ": "大型成長領漲"}
trows = [[n, f"<b>{e}</b>", f'<span class="{C(P(k))}">{PC(k)}</span>', f'{q[k]["5d"]:+.2f}%', f'{q[k]["1m"]:+.2f}%', note.get(e, "")] for n, e, k in themes]
s5 = sec(5, "主題與風格表現", table(["主題", "代表", "當日", "近5日", "近1月", "特徵"], trows, tid="themeTable", sortable={2, 3, 4}) + '<p class="mt-3 text-sm text-slate-600 dark:text-zinc-400">註：個別主題無單一ETF者使用代表個股作為代理，不等同主題指數。</p>')

# ---------- sec 6 breadth ----------
s6 = sec(6, "市場寬度與參與度", f'''
      <div class="space-y-4">
      <div class="{BOX}"><h3 class="font-semibold mb-2">6.1 均線參與度</h3>
      <p class="text-sm text-slate-700 dark:text-zinc-300">成分股站上20/50/100/200日均線的比例（如 S5TW/S5FI）{NA}；以下為代表ETF相對均線位置（均線、RSI 以至10-06收盤的Yahoo日線計算）：</p>
      {table(["ETF", "SPY", "QQQ", "IWM"], [["20日均線", f'{t["SPY"]["sma20"]:.2f}', f'{t["QQQ"]["sma20"]:.2f}', f'{t["IWM"]["sma20"]:.2f}'], ["50日均線", f'{t["SPY"]["sma50"]:.2f}', f'{t["QQQ"]["sma50"]:.2f}', f'{t["IWM"]["sma50"]:.2f}'], ["200日均線", f'{t["SPY"]["sma200"]:.2f}', f'{t["QQQ"]["sma200"]:.2f}', f'{t["IWM"]["sma200"]:.2f}'], ["10-06收盤", PX("SPY"), PX("QQQ"), PX("IWM")]])}
      <p class="mt-2 text-sm text-slate-600 dark:text-zinc-400">SPY、QQQ 在所有主要均線之上，趨勢健康；IWM 低於20/50日均線，小型股中期趨勢偏弱。</p></div>
      <div class="{BOX}"><h3 class="font-semibold mb-2">6.2 漲跌家數、新高新低</h3><p class="text-sm">NYSE/Nasdaq 上漲/下跌家數、52週新高/新低 {NA}。代理：11個板塊中10個收高；SPY {PC("SPY")} vs RSP {PC("RSP")} 接近，但羅素2000 {PC("^RUT")} 下跌，說明上漲面集中於大型股。</p></div>
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
      <p class="mt-3 text-sm text-slate-600 dark:text-zinc-400">註：均線/RSI/MACD 以Yahoo日線至10-06收盤計算。判讀：SMH（RSI 87）與 XLK（RSI 87）處於極度超買，QQQ（83）偏超買，SPY（72）略超買，追高風險上升；IWM RSI 44 偏中性偏弱。明日多頭確認：SPY 收盤站穩日高 781.6 之上、QQQ 站穩 762.9。風險位：SPY 失守 778.0（日低）、QQQ 失守 759.1（日低），更深支撐為20日均線區。</p>''')

# ---------- sec 8 ----------
def line(sym, txt=""):
    return f'<tr><td class="p-2 font-semibold">{sym}</td><td class="p-2 font-mono">${PX(sym)}</td><td class="p-2 {C(P(sym))}">{PC(sym)}</td><td class="p-2 text-xs">近5日 {q[sym].get("5d", 0):+.1f}% / 近1月 {q[sym].get("1m", 0):+.1f}%</td><td class="p-2 text-xs">{txt}</td></tr>'
def tbl(rows):
    return f'<div class="overflow-x-auto"><table class="w-full text-sm text-left"><tbody class="divide-y divide-slate-100 dark:divide-zinc-800">{"".join(rows)}</tbody></table></div>'
m7 = tbl([line("NVDA", "平盤附近整理，近5日 +5.3%"), line("MSFT", "收$529.3，AI軟體買盤延續"), line("AAPL", "小幅上漲"), line("GOOGL", "與Constellation簽20年購電協議（電力供應AI資料中心）"), line("AMZN", "+1.95%，七巨頭中領漲"), line("META", "小幅回落，近1月 +19.8% 後整理"), line("TSLA", "收$380.68，近5日 +7.9%")])
m8 = tbl([line("AVGO", "受Marvell投資人日帶動，客製晶片題材"), line("TSM", "小幅回落"), line("AMD", "+2.8%，近1月 +36.0%"), line("MRVL", "投資人日：FY2028營收目標上調至$200億（原$180億，共識$182億）；FY2031目標$700–900億、EPS目標$30以上"), line("MU", "-1.73%，高位回吐"), line("ASML", "-1.39%"), line("ARM", "小幅回落"), line("DELL", "+3.93%"), line("VRT", "小幅回落"), line("ANET", "+4.09%，網通題材隨MRVL走強")])
m9 = tbl([line("CRM", "軟體中最弱，近1月 -13.2%"), line("NOW", "軟體龍頭續彈"), line("SNOW", "-0.9%"), line("ORCL", "+1.61%"), line("ADBE", "小幅回落"), line("PANW", "+3.23%，近1月 +26.0%"), line("CRWD", "+2.27%，近1月 +30.9%"), line("PLTR", "+1.41%")])
m10 = tbl([line("CEG", "與Google簽20年購電協議（投資逾$43億提升11座核反應爐、新增890MW）及15年2,700MW供應協議，創單日大漲"), line("VST", "DOE 有條件貸款承諾最高$42億，支持Perry、Davis-Besse、Beaver Valley核電擴建"), line("NRG", "獨立電力商同步走高"), line("ETN", "+2.89%"), line("PWR", "+5.29%，電力基建"), line("GEV", "+3.96%"), line("OKLO", "+7.17%，核能題材跟漲")])
m11 = '''<ul class="list-disc pl-5 space-y-1"><li><b>Constellation Brands（STZ，盤後約-2.7%）</b>：FQ2 EPS $3.74（預期$3.61）、營收$26.3億（預期$25.4億），啤酒銷售+5%，但維持全年EPS指引$11.20–11.90，中值低於共識$11.72。</li>
<li><b>Marvell（+5.81%）</b>：投資人日上調長期營收目標，帶動 AVGO、ANET 及 Astera Labs、Credo 等同業走強。</li>
<li><b>Dell（+3.93%）、PANW（+3.23%）</b>：資料中心與資安股同步走強，未找到單一可查證催化。</li></ul>'''
s8 = sec(8, "重點個股新聞與異動", '<div class="space-y-3">' + details("8.1 大型科技七巨頭", m7, True) + details("8.2 AI 硬體 / 半導體", m8) + details("8.3 軟體 / SaaS / AI 應用", m9) + details("8.4 AI 電力 / 資料中心 / 能源基礎設施", m10) + details("8.5 其他顯著異動（併購與評級）", m11) + '<p class="text-xs text-slate-500">註：未列出個別新聞者，表示未找到可查證的單一催化，漲跌依價格資料呈現。</p></div>')

# ---------- sec 9 ----------
s9 = sec(9, "財報日曆與公司事件", f'''<div class="space-y-4">
  <div class="{BOX}"><h3 class="font-semibold mb-2">9.1 昨夜（10/6）財報與公司事件</h3><p class="text-sm">Marvell 投資人日（盤中）上調長期目標；盤後 Constellation Brands(STZ) 財報：EPS $3.74 對預期 $3.61、營收 $26.3 億對預期 $25.4 億，啤酒部門銷量+5.5%、葡萄酒與烈酒銷售+17%，但維持FY27 EPS指引 $11.20–11.90（共識 $11.72），盤後約-2.7%。Q3財報季將自10月中旬由銀行股拉開序幕。</p></div>
  {table(["日期", "公司", "關注點"], [["10/7 週三", "Levi Strauss (LEVI)、Applied Digital (APLD)", "APLD 為AI資料中心題材股；同日FOMC會議紀要"], ["10/8 週四", "PepsiCo (PEP)、Progressive (PGR)", "消費者價格彈性、保險定價"], ["10/9 週五", "（以公司IR確認為準）", "本日未取得可查證的重要財報"]])}
  <p class="text-xs text-slate-500">日曆來源：Investing.com 財報日曆（沿用前一交易日整理）；EPS/營收預期除STZ外未取得，請於公司IR確認。</p></div>''')

# ---------- sec 10 ----------
s10 = sec(10, "機構觀點與資金流", f'''{paras([
    ("評級／目標價", "本日未取得可查證的大型券商評級或目標價調整（前一日：摩根士丹利維持輝達 Overweight、目標價$300，未更新）。"),
    ("ETF 資金流", f"ETF 資金流量數據 {NA}；價格面：SMH 近5日 +4.22%、SOXX +3.88%，IGV +5.65%，XLU 單日 {PC('XLU')}，顯示軟體、半導體與電力近期受資金追捧。"),
    ("大宗/內部人/期權", f"本日大宗交易、內部人交易與異常期權活動 {NA}。"),
])}''')

# ---------- sec 11 ----------
s11 = sec(11, "板塊輪動判斷", paras([
    ("資金流入", f"公用事業（XLU {PC('XLU')}）、工業（XLI {PC('XLI')}）、非必需消費（XLY {PC('XLY')}）領漲；近5日科技（XLK {q['XLK']['5d']:+.2f}%）、軟體（IGV {q['IGV']['5d']:+.2f}%）、半導體（SMH {q['SMH']['5d']:+.2f}%）與能源（XLE {q['XLE']['5d']:+.2f}%）領先。"),
    ("資金流出／落後", f"醫療保健（XLV 近5日 {q['XLV']['5d']:+.2f}%）、小型股（IWM 近1月 {q['IWM']['1m']:+.2f}%）、金融（XLF 近1月 {q['XLF']['1m']:+.2f}%）。"),
    ("AI 主線健康度與階段", "AI 主線由晶片擴散至電力、客製晶片與網通，健康度良好，但SMH/XLK RSI 87、光通訊個股5日漲約16%，擁擠度偏高，且小型股走弱使寬度分歧。研判為『強趨勢上漲中的高位整理與輪動』，延續概率高於頂部，但追高性價比下降。"),
]))

# ---------- sec 12 watchlist ----------
W = [
    ("NVDA", "高位震盪", "平盤附近整理；近5日+5.3%"), ("AMD", "繼續強勢", "+2.8%，近1月+36.0%"), ("AVGO", "繼續強勢", "+3.67%，MRVL投資人日帶動"),
    ("MRVL", "繼續強勢", "+5.81%，上調長期目標"), ("GOOGL", "繼續強勢", "與CEG簽購電協議"), ("MSFT", "繼續強勢", "+0.78% 收$529"),
    ("META", "高位震盪", "近1月+19.8%，今日小跌"), ("AMZN", "繼續強勢", "+1.95%"), ("ORCL", "低位修復", "近1月-8.8%，近5日反彈5.1%"),
    ("CRM", "破位風險", "近1月-13.2%，今日-2.1%最弱"), ("NOW", "低位修復", "+1.39% 軟體續彈"), ("SNOW", "高位震盪", "-0.9%"),
    ("ADBE", "低位修復", "近1月-10.7%，小幅回落"), ("PLTR", "高位震盪", "近1月+10.2%"), ("LITE", "短線過熱", "近5日+16.4%，今日+3.8%"),
    ("COHR", "短線過熱", "近5日+15.8%，今日+1.4%"), ("ANET", "繼續強勢", "+4.09%"), ("FLNC", "破位風險", "近1月-22.4%，今日反彈"),
    ("OKLO", "高位震盪", "+7.17%，近1月-6.6%"), ("VST", "短線過熱", "+10.77%，近5日+14.0%"), ("CEG", "短線過熱", "+12.25%，近5日+13.5%"),
    ("ETN", "繼續強勢", "+2.89%，近1月+8.3%"), ("VRT", "高位震盪", "-0.19%，近1月-9.8%"),
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
  <div class="{BOX}"><h3 class="font-semibold mb-2">13.1 宏觀觀察</h3><ul class="list-disc pl-5 text-sm space-y-1"><li>10年期殖利率能否守在5.30%下方（今日高5.30%、收5.27%）；30年期5.64%。</li><li>WTI ${PX("CL=F")} / Brent ${PX("BZ=F")} 走勢。</li><li>10/7（週三）FOMC會議紀要與Fed官員講話；美元（UUP）{PC("UUP")}。</li><li>VIX 能否維持15附近。</li></ul></div>
  <div class="{BOX}"><h3 class="font-semibold mb-2">13.2 大盤觀察</h3><p class="text-sm">SPY：壓力 781.6（今日高）、支撐 778.0（今日低）。QQQ：壓力 762.9、支撐 759.1。IGV（{PX("IGV")}，近5日 +5.7%）與 IWM（{PX("IWM")}，今日 {PC("IWM")}）是否改善是寬度確認指標。</p></div>
  <div class="{BOX}"><h3 class="font-semibold mb-2">13.3 板塊與個股觀察</h3><p class="text-sm">CEG、VST、NRG（電力股大漲後是否續強或獲利回吐）；PWR、GEV、ETN（電力基建）；MRVL、AVGO、ANET（客製晶片/網通）；NVDA、MU（高位整理）；LITE、COHR（光通訊擁擠）；CRM（軟體最弱）；STZ（盤後財報反應）；APLD（10/7財報）；LEVI、PEP、PGR（財報）；IWM（小型股走弱）；FLNC、OKLO（弱勢是否止穩）。</p></div></div>''')

# ---------- sec 14 risk ----------
RC = {"高": "bg-rose-100 text-rose-700", "中高": "bg-orange-100 text-orange-700", "中": "bg-yellow-100 text-yellow-700", "低": "bg-emerald-100 text-emerald-700"}
risks = [("宏觀利率", "中高", "10年期5.27%、30年期5.64%雖自高位回落，仍處多年高位；12月升息據報導仍有定價"),
         ("市場寬度", "中高", "近1月RSP -3.1%、IWM -5.0%落後SPY +1.2%，今日羅素2000 -0.59%，指數創高依賴大型股"),
         ("AI 擁擠度", "中高", "SMH RSI 87、LITE/COHR 5日漲約16%，電力股單日大漲10%以上，高位波動放大"),
         ("財報風險", "中", "Q3財報季尚未全面展開；STZ 盤後財報反應偏弱，本週以消費財報為主"),
         ("地緣／油價", "中", "Brent 約$101，油價維持高位"),
         ("技術面", "中高", "多項大型ETF超買，若殖利率續升易回檔"),
         ("流動性／債務", "中", "長端殖利率上行反映債務與期限溢價擔憂")]
s14 = sec(14, "風險提示（風險矩陣）", table(["風險維度", "評級", "解讀"], [[f"<b>{a}</b>", f'<span class="px-2 py-0.5 rounded font-semibold {RC[b]}">{b}</span>', c] for a, b, c in risks]))

# ---------- sec 15 ----------
s15 = f'''
    <section id="sec-15" class="scroll-mt-6 p-6 rounded-2xl bg-gradient-to-br from-white to-slate-50 dark:from-zinc-900 dark:to-zinc-950 border border-slate-200 dark:border-zinc-800 shadow-sm">
      <h2 class="{H2}"><span class="text-brand-500">15.</span> 最終結論</h2>
      <div class="space-y-3 text-sm sm:text-base leading-relaxed text-slate-700 dark:text-zinc-300">
        <p><strong>今日市場結論：</strong>標普500收 {PX("^GSPC")}（{PC("^GSPC")}）、納指收 {PX("^IXIC")}（{PC("^IXIC")}）雙創收盤新高，殖利率回落（10年期5.27%）與AI基礎設施題材（電力、客製晶片、網通）支撐；小型股走弱與超買擁擠是主要制約。</p>
        <p><strong>當前市場階段：</strong>強趨勢上漲中的高位震盪（板塊輪動並行）。</p>
        <p><strong>我的操作傾向（中性表述）：</strong>趨勢仍偏多，但超買（SMH、XLK）與殖利率風險使追高性價比下降；偏向等待回踩或殖利率回落確認，AI電力、客製晶片與網通值得關注（但單日大漲後波動放大），小型股與醫療保健需謹慎。</p>
        <div><strong>最值得關注的 5 個訊號：</strong>
          <ol class="list-decimal pl-6 mt-2 space-y-1">
            <li>10年期殖利率能否守住5.30%下方。</li>
            <li>10/7 FOMC會議紀要對升息/按兵不動的措辭。</li>
            <li>電力股（CEG、VST）大漲後是否續強或回吐；費半在超買下能否守住。</li>
            <li>IWM 能否止跌，改善寬度。</li>
            <li>STZ 盤後反應與 MRVL/AVGO 客製晶片題材延續性。</li>
          </ol></div>
        <p class="text-xs text-slate-500">資料與限制：價格取自 Yahoo Finance，新聞與經濟數據取自公開報導（Benzinga、Investing.com、Morningstar、Census/BEA、公司新聞稿）；寬度、ETF資金流、DXY、2年期殖利率等未取得項目已標示。非投資建議。</p>
      </div>
    </section>
'''

# ---------- tail ----------
tail = old[old.index("<!-- Footer -->"):]
tail = re.sub(r"<div>美股收盤日報｜資料來源：.*?</div>", "<div>美股收盤日報｜資料來源：Yahoo Finance、公開新聞報導（Morningstar、Benzinga、Investing.com 等）、美國普查局/BEA、公司新聞稿</div>", tail)
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
out = R + "reports/2026-10-06-us-stock-closing-daily-report.html"
open(out, "w", encoding="utf-8").write(html)
print("written", out, len(html))
if "--no-publish" in sys.argv:
    sys.exit(0)
pub = R + ".antigravitycli/skills/html-report/scripts/publish.py"
res = subprocess.run(["python3", pub, out, TITLE, DESC], capture_output=True, text=True)
print(res.stdout, res.stderr)
sys.exit(res.returncode)
