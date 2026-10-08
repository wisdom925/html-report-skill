import json, re, subprocess, sys

R = "/Users/wisdom/html-report-skill/"
D = "2026-10-07"
q = json.load(open(R + f"scratch/quotes_{D}.json"))
t = json.load(open(R + f"scratch/tech_{D}.json"))
old = open(R + "reports/2026-10-06-us-stock-closing-daily-report.html", encoding="utf-8").read()

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
TITLE = f"美股收盤日報｜{D}"
DESC = ("週三（2026年10月7日）美股自高位小幅回檔：標普500 -0.22%報7,801.77點、納指 -0.22%報27,538.69點、道瓊 -0.66%（-341點）報51,179.87點；"
        "FOMC 9月會議紀要偏鷹促使10年期殖利率盤中衝至5.36%後收在5.28%，美元走強（UUP +0.48%）；"
        "美光（MU +4.06%）與Vistra（VST +3.88%）逆勢大漲，小型股續弱（羅素2000 -1.31%），僅醫療保健板塊收紅（XLV +1.03%）。")

head = old[: old.index("<!-- Header Block -->")]
head = re.sub(r"<title>.*?</title>", f"<title>{TITLE}｜標普高位回踩、Fed紀要偏鷹壓制、美光逆勢大漲、電力股分化 ({D})</title>", head, flags=re.S)
head = re.sub(r'<meta name="description" content=".*?">', f'<meta name="description" content="{DESC}">', head, flags=re.S)
head = re.sub(r'<meta property="og:title" content=".*?">', f'<meta property="og:title" content="{TITLE}">', head)
head = re.sub(r'<meta property="og:description" content=".*?">', '<meta property="og:description" content="標普高位回踩，Fed會議紀要偏鷹，美光與Vistra逆勢走強，小型股疲弱，僅醫療保健收紅。">', head)
head = head.replace("2026-10-06", D)

header = f'''<!-- Header Block -->
    <header class="border-b border-slate-200 dark:border-zinc-800 pb-6">
      <div class="flex flex-wrap items-center justify-between gap-3 mb-2">
        <span class="inline-flex items-center gap-1.5 px-3 py-1 rounded-full text-xs font-semibold bg-amber-100 text-amber-800 dark:bg-amber-950 dark:text-amber-300">
          <span class="w-2 h-2 rounded-full bg-amber-500 animate-pulse"></span> 指數高位回踩・Fed紀要偏鷹・美光逆勢大漲・電力股分化
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
        <p>{S}【大盤走勢】</strong> 美股週三自前日歷史收盤高位溫和回踩。標普500 <strong>{PC("^GSPC")}</strong> 收 <strong>{PX("^GSPC")}</strong>，納斯達克綜合指數 <strong>{PC("^IXIC")}</strong> 收 <strong>{PX("^IXIC")}</strong>，道瓊工業指數 <strong>{PC("^DJI")}</strong> 下跌 {abs(q['^DJI']['change']):.2f} 點收 <strong>{PX("^DJI")}</strong>；費城半導體指數 <strong>{PC("^SOX")}</strong> 收 {PX("^SOX")}；羅素2000小型股持續疲弱，重挫 <strong>{PC("^RUT")}</strong> 收 {PX("^RUT")}。</p>
        <p>{S}【驅動因素】</strong> 下午2:00公布的 FOMC 9月會議紀要偏向鷹派，顯示多數官員認為通膨依然頑固，年內仍有再次升息的必要性；10年期美債殖利率盤中一度衝高至5.36%的多年高點，隨後略有收窄收在 {PX("^TNX")}%（+1bp）。MBA 房貸申請量因利率上揚續降4.2%，美元指數強勢反彈（UUP {PC("UUP")}），共同壓制了市場估值擴張。</p>
        <p>{S}【資金偏好】</strong> Risk-Off 偏向防禦避險：VIX 盤中最高觸及 16.01，收盤回穩至 {PX("^VIX")}（{PC("^VIX")}）；黃金現貨期貨大幅回吐 {PC("GC=F")}（收 ${PX("GC=F",1)}/oz）；WTI 原油回跌 {PC("CL=F")}（收 ${PX("CL=F")}）；加密貨幣全線承壓，比特幣 {PC("BTC-USD")}（收 ${PX("BTC-USD",0)}），以太幣 {PC("ETH-USD")}。</p>
        <p>{S}【市場寬度】</strong> 寬度顯著惡化：S&P 500 11大板塊中僅醫療保健（XLV {PC("XLV")}）逆勢上漲，其餘10大板塊全數收黑；工業（XLI {PC("XLI")}）、原物料（XLB {PC("XLB")}）及房地產（XLRE {PC("XLRE")}）領跌；小型股（IWM {PC("IWM")}）連續大幅跑輸標普，近1個月落後幅度擴大（IWM {q["IWM"]["1m"]:+.2f}% vs SPY {q["SPY"]["1m"]:+.2f}%）。</p>
        <p>{S}【核心主線】</strong> AI 主線出現結構性分化：美光科技（MU {PC("MU")}）在HBM晶片與存儲景氣爆發下逆勢飆漲創波段新高；獨立電力發电商 Vistra（VST {PC("VST")}）與 NRG（{PC("NRG")}）延續強勢，但昨日暴漲的 Constellation Energy（CEG {PC("CEG")}）及電力設備股（ETN {PC("ETN")}、GEV {PC("GEV")}、PWR {PC("PWR")}）遭遇獲利了結賣壓；盤後 Applied Digital（APLD）首季營收年增322%大幅超預期引發盤後大漲。</p>
        <div class="mt-4 p-4 rounded-xl bg-amber-50 dark:bg-zinc-800/60 border border-amber-200 dark:border-amber-900/40 text-amber-900 dark:text-amber-200 font-medium">
          💡 <strong>今日市場狀態判斷：</strong>「指數高位回踩，Fed鷹派紀要推升殖利率與美元，防禦股與個別強勢晶片（MU）抗跌；但市場寬度顯著惡化、小型股疲弱，短線防禦情緒升溫。」
        </div>
      </div>
    </section>
'''

# ---------- sec 1 ----------
def card(name, key, px, sub):
    return f'<div class="{CARD}"><div class="text-xs text-slate-500 dark:text-zinc-400 font-medium">{name}</div><div class="text-xl font-extrabold font-mono mt-1">{px}</div><div class="text-xs mt-1 flex items-center justify-between"><span class="{C(P(key), key=="^VIX")}">{PC(key)}</span><span class="text-slate-400 font-mono">{sub}</span></div></div>'

cards = "".join([
    card("S&P 500 (標普500)", "^GSPC", PX("^GSPC"), f"SPY ${PX('SPY')}"),
    card("Nasdaq Composite", "^IXIC", PX("^IXIC"), "高位微幅整固"),
    card("Dow Jones (道瓊)", "^DJI", PX("^DJI"), f"{q['^DJI']['change']:+.2f} 點"),
    card("Nasdaq 100", "^NDX", PX("^NDX"), f"QQQ ${PX('QQQ')}"),
    card("Russell 2000", "^RUT", PX("^RUT"), f"IWM ${PX('IWM')}"),
    card("SOX (費城半導體)", "^SOX", PX("^SOX"), f"SMH ${PX('SMH')}"),
    card("Software (IGV)", "IGV", PX("IGV"), "軟體高位回吐"),
    card("VIX", "^VIX", PX("^VIX"), "盤中一度觸及16.01"),
])

idx_rows = []
def irow(name, etf, key, state):
    idx_rows.append([f'<span class="font-semibold font-sans">{name}</span>', etf, f'<b>{PX(key)}</b>', f'<span class="{C(P(key), key=="^VIX")}">{PC(key)}</span>', RNG(key), f'<span class="font-sans">{state}</span>'])
irow("S&P 500", "SPY", "^GSPC", "自昨日歷史新高小幅回踩(-0.22%)，守穩20/50日均線之上，尾盤自日低7,763點反彈約38點，RSI 65")
irow("Nasdaq Composite", "—", "^IXIC", "收27,538.69點，盤中回踩27,341點後收復大部分跌幅，大型科技股相對抗跌")
irow("Nasdaq 100", "QQQ", "^NDX", "QQQ 收757.73(-0.25%)，高位整固；RSI 自83降至78，估值超買微幅修復")
irow("Dow Jones", "DIA", "^DJI", "下跌341.41點(-0.66%)，受工業(CAT/HON)、金融與原物料拖累明顯；近1月-3.15%")
irow("Russell 2000", "IWM", "^RUT", "重挫-1.31%，大幅跑輸標普；IWM跌破20/50日均線，RSI跌至35逼近超賣，中小盤承壓極重")
irow("SOX 半導體", "SOXX / SMH", "^SOX", "收13,066.15(-1.15%)，SMH(-1.18%)；MU大漲(+4.06%)對沖了TSM/ARM/ASML回調")
irow("CBOE VIX", "^VIX", "^VIX", "收15.08(+0.47%)，盤中避險一度拉升至16.01，尾盤回落，整體仍處良性波動區間")
s1 = sec(1, "大盤表現總覽", f'''
      <div class="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-4 gap-4 mb-6">{cards}</div>
      <div class="{BOX}">
        <h3 class="text-sm font-semibold text-slate-700 dark:text-zinc-300 mb-3 flex items-center justify-between"><span>主要指數與核心資產當日漲跌幅對比 (Chart.js)</span><span class="text-xs font-normal text-slate-500">{D} 基準</span></h3>
        <div class="relative h-64 sm:h-72 w-full"><canvas id="overviewChart"></canvas></div>
      </div>
      <div class="mt-6">{table(["指數名稱", "代表ETF", "收盤點位", "當日漲跌幅", "日內高/低", "技術狀態"], idx_rows, mono=True)}</div>
      <p class="mt-3 text-sm text-slate-600 dark:text-zinc-400">補充：標普500與納指自歷史高位溫和回踩未破關鍵均線；小盤股（羅素2000 -1.31%）顯著跑輸大盤；VIX 盤中跳升至 16.01 後收斂至 15.08。</p>
''')

# ---------- sec 2 ----------
mer = f'''graph LR
  subgraph PreMarket["盤前"]
    A["MBA房貸申請降4.2%<br/>長端殖利率居高不下<br/>市場靜待FOMC會議紀要"]
  end
  subgraph Open["開盤"]
    B["標普低開 7,792.98<br/>道瓊低開重挫<br/>醫療保健板塊避險買盤進駐"]
  end
  subgraph MidDay["午盤 14:00"]
    C["FOMC 9月紀要公布偏鷹<br/>暗示年內可能再升息一次<br/>10年期殖利率觸及5.36%高位<br/>標普下探日低 {q['^GSPC']['low']:,.2f}"]
  end
  subgraph Close["尾盤與盤後"]
    D["逢低抄底資金進駐收窄跌幅<br/>標普收 {PX('^GSPC')} (-0.22%)<br/>盤後: APLD 營收爆增322%暴漲<br/>LEVI 獲利超預期"]
  end
  PreMarket --> Open --> MidDay --> Close'''
s2 = sec(2, "盤中走勢復盤（時間線 Timeline）", f'''
      <div class="{BOX} overflow-x-auto"><div class="mermaid">
{mer}
      </div></div>
      <div class="mt-4 {BOX}">{paras([
    ("盤前", "市場在標普納指連續創歷史新高後情緒謹慎。MBA公布房貸申請指數再降4.2%，反映長端房貸利率高企對地產鏈的冷卻效應；原油小幅震盪，美元走強，投資人普遍等待下午公布的 FOMC 9月會議紀要。"),
    ("開盤後", f"三大指數低開，標普500 開在 {q['^GSPC']['open']:,.2f}，道瓊開盤即承壓下跌逾200點。前日大漲的電力基建設備股（GEV、ETN、PWR）與半導體權值股（TSM、ASML）遭遇獲利回吐，而資金迅速湧入醫療保健（XLV）與大型防禦現金流巨頭（AMZN、AAPL）。"),
    ("午盤方向選擇", f"美東時間 14:00，聯準會發布 9 月 FOMC 會議紀要。紀要明確顯示，決策官員雖然全票通過9月升息25基點，但『大多數與會者』認為通膨回落至目標的進展緩慢，年內可能仍需再度調升政策利率。長端美債殖利率聞訊急拉，10年期盤中觸及5.36%的高點，各大指數刷新日內低點（標普探底 {q['^GSPC']['low']:,.2f}，納指下探 {q['^IXIC']['low']:,.2f}）。"),
    ("尾盤拉升", f"臨近尾盤，高殖利率未引發恐慌性拋售，逢低買盤於標普 7,760 點附近強力承接，帶動大盤震盪拉升收復逾半失地；標普收在 {PX('^GSPC')}，距日內高點僅6點；納指收 {PX('^IXIC')}，展現極強的下檔支撐韌性。"),
    ("盤後與核心驅動", "盤後 Applied Digital（APLD）公布 FQ1 財報，營收高達 $3.419 億美元（年增 322%），大幅擊敗市場預期的 $1.25–1.35 億，經調整 EPS -$0.01（優於預期 -$0.30），盤後股價飆升，重新點燃 AI 資料中心算力與基建需求熱度；Levi Strauss（LEVI）Q3 EPS $0.48 超預期。核心驅動：鷹派會議紀要引發的利率預期重定價造成估值回踩，但基本面與AI算力需求仍提供堅實支撐。"),
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
tab_y = f'''<div id="panel-yields" class="tab-panel space-y-4"><h4 class="font-bold text-slate-900 dark:text-white text-base">Fed鷹派紀要推升公債殖利率，10年期收在5.28%（盤中觸及5.36%）</h4>
  <div class="grid grid-cols-2 sm:grid-cols-4 gap-3 font-mono">{yield_cards}</div>
  <p>10年期基準殖利率收在 {PX("^TNX")}%（較前日 +1bp，日內區間 5.26–5.36%），盤中一度創下 2002 年以來的波段新高；30年期收 {PX("^TYX")}%（+2bp）；5年期收 {PX("^FVX")}%（-1bp）。30年與5年利差擴大至 64bp，長端曲線呈現微幅陡峭化特徵。含義解讀：長天期殖利率居高不下持續反映市場對聯準會更長時間維持高利率（Higher for Longer）甚至年內再升息一次的定價，成為當前壓制權益資產估值擴張的核心宏觀變量。</p></div>'''

tab_f = '''<div id="panel-fed" class="tab-panel space-y-4"><h4 class="font-bold text-slate-900 dark:text-white text-base">FOMC 9月會議紀要：大部分官員支持年內仍有再升息空間</h4>
  <div class="grid grid-cols-2 sm:grid-cols-3 gap-3 font-mono">''' + stat("9月升息決定", "全票通過 (12-0)", "將聯邦基金利率目標區間上調至 3.75%–4.00%") + stat("後續利率路徑", "偏向緊縮", "紀要指出「大多數與會官員」認為年內再升息一次可能是合適的") + stat("政策基調", "數據依賴", "重申通膨仍具黏性，必須看到就業與物價進一步降溫") + '''</div>
  <p>根據10月7日下午公布的9月15-16日FOMC會議紀要，聯準會決策成員在升息決議上展現高度團結，並對核心通膨的韌性表達持續擔憂。儘管部分官員提及需要平衡過度緊縮的風險，但主流觀點仍傾向『抗通膨任務尚未完成』。CME FedWatch 即時機率官方數據本次未取得可查證即時流，但受紀要偏鷹影響，市場對10月維持利率的預期維持謹慎，並提升了12月升息的定價溢價。</p></div>'''

tab_c = f'''<div id="panel-commodities" class="tab-panel space-y-4"><h4 class="font-bold text-slate-900 dark:text-white text-base">美元指數反彈、黃金大跌、原油回吐、加密資產下挫</h4>
  <div class="grid grid-cols-2 sm:grid-cols-3 gap-3 font-mono">
  {stat("美元（UUP代理）", "$"+PX("UUP"), CT("UUP"))}{stat("黃金期貨", "$"+PX("GC=F",1)+"/oz", CT("GC=F"))}{stat("WTI 原油", "$"+PX("CL=F"), CT("CL=F", True))}
  {stat("Brent 原油", "$"+PX("BZ=F"), CT("BZ=F", True))}{stat("比特幣", "$"+PX("BTC-USD",0), CT("BTC-USD"))}{stat("以太幣", "$"+PX("ETH-USD",0), CT("ETH-USD"))}</div>
  <p>美元 ETF UUP 上漲 {PC("UUP")}（收 ${PX("UUP")}），反映鷹派紀要後美歐利差擴大提振美元買盤；黃金現貨期貨受強勢美元與高實質利率重擊，重挫 {PC("GC=F")} 收在 ${PX("GC=F",1)}；WTI 原油下跌 {PC("CL=F")} 至 ${PX("CL=F")}/桶，Brent 原油小漲 {PC("BZ=F")} 至 ${PX("BZ=F")}/桶；加密貨幣市場流動性收緊，比特幣下跌 {PC("BTC-USD")}，以太幣大跌 {PC("ETH-USD")}。</p></div>'''

tab_d = '''<div id="panel-data" class="tab-panel space-y-4"><h4 class="font-bold text-slate-900 dark:text-white text-base">MBA 房貸申請續降 4.2%，反映房貸利率重回高位</h4>
  <div class="overflow-x-auto"><table class="w-full text-sm text-left"><thead class="bg-slate-50 dark:bg-zinc-800/60"><tr><th class="p-3">數據名稱</th><th class="p-3">實際值</th><th class="p-3">預期值</th><th class="p-3">前值</th><th class="p-3">市場解讀</th></tr></thead><tbody class="divide-y divide-slate-100 dark:divide-zinc-800">
  <tr><td class="p-3 font-semibold">MBA 房貸申請總指數（至10/2）</td><td class="p-3 font-mono">-4.2%</td><td class="p-3 font-mono">未公布</td><td class="p-3 font-mono">+1.2%（前週）</td><td class="p-3">隨著30年期固定房貸利率緊隨美債殖利率回升，購房與轉貸申請量雙雙下滑，房地產市場承壓。</td></tr>
  <tr><td class="p-3 font-semibold">FOMC 9月會議紀要</td><td class="p-3 font-mono">偏鷹派</td><td class="p-3 font-mono">中性</td><td class="p-3 font-mono">升息25bp</td><td class="p-3">多數官員傾向年內再升息一次，打壓市場寬鬆預期。</td></tr>
  <tr><td class="p-3 font-semibold">8月消費者信貸（美東15:00）</td><td class="p-3 font-mono">增長放緩</td><td class="p-3 font-mono">中性</td><td class="p-3 font-mono">前值放緩</td><td class="p-3">高利率環境下信用卡循環信用與非循環信貸擴張受限。</td></tr>
  </tbody></table></div>
  <p class="text-xs text-slate-500">明日預告：10/8（週四）將公布每週初請失業金人數（Initial Jobless Claims）與8月批發庫存（Wholesale Inventories）。</p></div>'''

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
    ("醫療保健", "XLV", "防禦資金湧入避險，全市場唯一定格上漲板塊 (+1.03%)"),
    ("公用事業", "XLU", "電力商持續走強對沖公用事業回吐，幾乎持平 (-0.02%)"),
    ("必需消費", "XLP", "防禦性相對抗跌，近5日 +1.36% (-0.12%)"),
    ("科技", "XLK", "AAPL/MSFT抗跌對沖硬體回調，近1月仍領漲 +7.20% (-0.30%)"),
    ("非必需消費", "XLY", "AMZN大漲+1.42%支撐，但TSLA微跌 (-0.32%)"),
    ("通訊服務", "XLC", "GOOGL走強(+0.81%)但META獲利了結(-2.38%) (-0.35%)"),
    ("金融", "XLF", "長端利率居高不下，銀行股財報季前謹慎 (-0.48%)"),
    ("能源", "XLE", "油價回吐，近5日仍累積上漲 +3.02% (-0.61%)"),
    ("房地產", "XLRE", "受10年期殖利率衝高重創，近1月 -7.59% (-1.29%)"),
    ("原物料", "XLB", "美元強勁反彈壓制大宗商品價格 (-1.51%)"),
    ("工業", "XLI", "GEV、ETN等電力基建設備股大漲後遭遇獲利回吐領跌 (-2.18%)"),
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
      <p class="mt-3 text-sm text-slate-600 dark:text-zinc-400">最強板塊：醫療保健 XLV（{PC("XLV")}）、公用事業 XLU（{PC("XLU")}）、必需消費 XLP（{PC("XLP")}）；最弱板塊：工業 XLI（{PC("XLI")}）、原物料 XLB（{PC("XLB")}）、房地產 XLRE（{PC("XLRE")}）。風格特徵：典型防禦型板塊（醫療、公用、必需）顯著跑贏週期與重資本（工業、原物料、房地產）；成長 vs 價值方面，小盤價值 IWN（{PC("IWN")}）與小盤成長 IWO（{PC("IWO")}）雙雙重挫，大盤成長 QQQ（{PC("QQQ")}）憑藉充沛現金流相對抗跌。AI電力設備與基建股出現短線漲多獲利回吐，但獨立發電商（VST、NRG）依然強勢。</p>''')

# ---------- sec 5 themes ----------
themes = [
    ("半導體", "SMH", "SMH"), ("半導體", "SOXX", "SOXX"), ("軟體", "IGV", "IGV"),
    ("存儲晶片（代理）", "MU", "MU"),
    ("網路安全（代理）", "CRWD", "CRWD"), ("網路安全（代理）", "PANW", "PANW"),
    ("雲端運算（代理）", "NOW", "NOW"), ("AI/自動化（代理）", "PLTR", "PLTR"),
    ("光通訊（代理）", "LITE", "LITE"), ("光通訊（代理）", "COHR", "COHR"),
    ("資料中心/電力（代理）", "VST", "VST"), ("資料中心/電力（代理）", "GEV", "GEV"),
    ("儲能（代理）", "FLNC", "FLNC"),
    ("小盤成長", "IWO", "IWO"), ("小盤價值", "IWN", "IWN"), ("等權標普", "RSP", "RSP"), ("大盤成長（納指100）", "QQQ", "QQQ"),
]
note = {
    "SMH": "高位獲利回吐，近5日 +3.43%",
    "SOXX": "半導體高位整理，費半 -1.15%",
    "IGV": "軟體回調，近5日仍有 +3.16%",
    "MU": "逆勢大漲 +4.06%，HBM與業績帶動",
    "CRWD": "資安龍頭整理 (-1.16%)，近1月 +28.9%",
    "PANW": "微幅回落 (-0.95%)，高位整固",
    "NOW": "軟體權重平盤整理 (-0.07%)",
    "PLTR": "抗跌逆揚 +1.07%，近1月 +14.0%",
    "LITE": "高位急拉後回踩 (-1.97%)，5日仍大漲 +14.4%",
    "COHR": "光通訊回吐 (-1.12%)，5日仍漲 +16.2%",
    "VST": "獨立發電商續飆 +3.88%，5日暴漲 +20.5%",
    "GEV": "電力設備重挫 (-3.12%)，漲多回吐",
    "FLNC": "儲能破位下挫 (-4.48%)，月跌 -30.5%",
    "IWO": "小盤成長領跌 (-1.41%)，風險偏好驟降",
    "IWN": "小盤價值弱勢 (-1.18%)，均線失守",
    "RSP": "等權標普跌 -0.89%，大幅跑輸市值加權SPY",
    "QQQ": "大盤成長僅跌 -0.25%，大科技發揮護盤韌性"
}
trows = [[n, f"<b>{e}</b>", f'<span class="{C(P(k))}">{PC(k)}</span>', f'{q[k]["5d"]:+.2f}%', f'{q[k]["1m"]:+.2f}%', note.get(e, "")] for n, e, k in themes]
s5 = sec(5, "主題與風格表現", table(["主題", "代表", "當日", "近5日", "近1月", "特徵"], trows, tid="themeTable", sortable={2, 3, 4}) + '<p class="mt-3 text-sm text-slate-600 dark:text-zinc-400">主題解讀：存儲晶片（MU）與獨立發電（VST）為盤面雙巨頭亮點；光通訊（LITE、COHR）與電力設備（GEV）在連日暴漲後出現技術性降溫回吐；等權標普 RSP 下跌 0.89% 明顯跑輸 SPY，反映下跌廣度擴散至中等市值股票。</p>')

# ---------- sec 6 breadth ----------
s6 = sec(6, "市場寬度與參與度", f'''
      <div class="space-y-4">
      <div class="{BOX}"><h3 class="font-semibold mb-2">6.1 均線參與度</h3>
      <p class="text-sm text-slate-700 dark:text-zinc-300">成分股站上20/50/100/200日均線的比例（如 S5TW/S5FI）{NA}；代表ETF相對均線位置如下（依至10-07收盤日線計算）：</p>
      {table(["ETF", "SPY", "QQQ", "IWM"], [["20日均線", f'{t["SPY"]["sma20"]:.2f}', f'{t["QQQ"]["sma20"]:.2f}', f'{t["IWM"]["sma20"]:.2f}'], ["50日均線", f'{t["SPY"]["sma50"]:.2f}', f'{t["QQQ"]["sma50"]:.2f}', f'{t["IWM"]["sma50"]:.2f}'], ["200日均線", f'{t["SPY"]["sma200"]:.2f}', f'{t["QQQ"]["sma200"]:.2f}', f'{t["IWM"]["sma200"]:.2f}'], ["10-07收盤", PX("SPY"), PX("QQQ"), PX("IWM")]])}
      <p class="mt-2 text-sm text-slate-600 dark:text-zinc-400">趨勢研判：SPY 與 QQQ 穩居所有主要均線上方，大盤中長期上升趨勢未受損害；但 IWM 跌破20日均線（{t["IWM"]["sma20"]:.2f}）並持續低於50日均線（{t["IWM"]["sma50"]:.2f}），小型股均線系統完全呈現空頭排列，寬度極度脆弱。</p></div>
      <div class="{BOX}"><h3 class="font-semibold mb-2">6.2 漲跌家數、新高新低</h3><p class="text-sm">NYSE 與 Nasdaq 交易所的上漲／下跌家數與52週新高／新低官方明細 {NA}。寬度代理觀察：S&P 500 11大板塊中僅1個收漲（醫療保健 XLV +1.03%），10個板塊收黑；等權重標普（RSP -0.89%）跌幅近乎為市值加權標普（SPY -0.24%）的四倍，羅素2000更暴跌 -1.31%，顯示市場下跌呈現高度普遍性，僅少數權值股掩蓋了廣泛股票的修正。</p></div>
      <div class="{BOX}"><h3 class="font-semibold mb-2">6.3 其他內部指標</h3><p class="text-sm">騰落線（A/D Line）、McClellan Oscillator、Put/Call Ratio、VIX 期限結構 {NA}。VIX 恐慌指數盤中自 14.97 急拉至 16.01，收盤回落至 {PX("^VIX")}（+0.47%），顯示期權避險需求微幅升溫但未引發流動性踩踏；成交流量方面，標普500 成交量約 {q["^GSPC"]["volume"]/1e9:.2f} 十億股，Nasdaq 約 {q["^IXIC"]["volume"]/1e9:.2f} 十億股，整體成交量能溫和，非恐慌性出逃。</p></div>
      </div>''')

# ---------- sec 7 technicals ----------
def trow(sym, supp_res):
    x = t[sym]; p = q[sym]["price"]
    def pos(m): return "上" if p > x[m] else "下"
    macd = "多頭" if x["macd"] > 0 else "空頭"
    ob = "極度超買" if x["rsi"] >= 80 else ("超買" if x["rsi"] >= 70 else ("超賣" if x["rsi"] <= 30 else ("偏弱" if x["rsi"] <= 40 else "中性")))
    return [f"<b>{sym}</b>", f"{p:.2f}", f'<span class="{C(P(sym))}">{PC(sym)}</span>', f'{pos("sma20")}({x["sma20"]:.1f})', f'{pos("sma50")}({x["sma50"]:.1f})', f'{pos("sma200")}({x["sma200"]:.1f})', f'{x["rsi"]:.0f} {ob}', macd, supp_res]

trs = []
for sym in ["SPY", "QQQ", "IWM", "SMH", "IGV", "XLK"]:
    x = t[sym]
    trs.append(trow(sym, f"支撐 {q[sym]['low']:.2f}（日低）/ {x['sma20']:.1f}（20日）；壓力 {max(q[sym]['high'], x['hi20']):.2f}（高點）"))

s7 = sec(7, "技術面分析", table(["ETF", "收盤", "當日", "20日均線", "50日均線", "200日均線", "RSI(14)", "MACD", "支撐／壓力"], trs, mono=True) + f'''
      <p class="mt-3 text-sm text-slate-600 dark:text-zinc-400">技術判讀：SMH（RSI 80）與 XLK（RSI 84）仍處於高度超買區間，追高風險仍大；QQQ（RSI 78）與 SPY（RSI 65）高位整固修復；IWM（RSI 35）瀕臨超賣但處於空頭破位排列。明日多頭確認信號：SPY 能否放量突破日高 779.10 點並重返 780 點上方，QQQ 突破 758.20 點。關鍵風險防守位：SPY 今日低點 773.61 點（失守將下探20日均線 765.6 區間），QQQ 今日低點 751.76 點。</p>''')

# ---------- sec 8 ----------
def line(sym, txt=""):
    return f'<tr><td class="p-2 font-semibold">{sym}</td><td class="p-2 font-mono">${PX(sym)}</td><td class="p-2 {C(P(sym))}">{PC(sym)}</td><td class="p-2 text-xs">近5日 {q[sym].get("5d", 0):+.1f}% / 近1月 {q[sym].get("1m", 0):+.1f}%</td><td class="p-2 text-xs">{txt}</td></tr>'

def tbl(rows):
    return f'<div class="overflow-x-auto"><table class="w-full text-sm text-left"><tbody class="divide-y divide-slate-100 dark:divide-zinc-800">{"".join(rows)}</tbody></table></div>'

m7 = tbl([
    line("AMZN", "大漲 +1.42% 收$259.92，雲端AWS算力利好驅動，七巨頭中表現最強"),
    line("AAPL", "穩步上揚 +0.91% 收$336.67，防禦資金與硬體換機預期支撐"),
    line("GOOGL", "延續強勢 +0.81% 收$350.50，受與CEG核電合作及Gemini AI進展提振"),
    line("MSFT", "微漲 +0.09% 收$529.76，高位強勢震盪守穩5日線"),
    line("NVDA", "回調 -0.74% 收$237.47，盤中低點$236.38獲買盤支撐，SpaceX合作傳聞持續發酵"),
    line("TSLA", "小跌 -0.75% 收$377.81，在日前交付量大漲後進行技術性休整"),
    line("META", "回落 -2.38% 收$721.31，近1月大漲近18%後遭遇獲利了結賣壓")
])

m8 = tbl([
    line("MU", "大暴走 +4.06% 收$1,088.00！盤中最高觸及$1,089.20，HBM記憶體產能爆滿效應持續發酵，半導體最亮眼星"),
    line("AVGO", "微漲 +0.19% 收$376.51，受Marvell客製晶片外溢效應支撐，近5日大漲+7.2%"),
    line("DELL", "小漲 +0.86% 收$578.96，AI伺服器需求持續強勁"),
    line("ANET", "微漲 +0.22% 收$215.83，高階資料中心交換機需求看好"),
    line("AMD", "微跌 -0.55% 收$645.86，在破兆市值平台高位整理"),
    line("MRVL", "微跌 -0.81% 收$284.68，投資人日大漲後小幅消化賣壓，近5日+7.8%"),
    line("ASML", "下跌 -1.59% 收$1,804.96，歐洲半導體板塊同步拖累"),
    line("TSM", "回調 -2.09% 收$472.20，ADR高位整固"),
    line("ARM", "下跌 -2.71% 收$294.37，高估值成長股受殖利率飆升衝擊"),
    line("LITE", "回吐 -1.97% 收$1,111.07，光通訊大漲後遭遇技術回踩，5日仍大賺+14.4%"),
    line("COHR", "回吐 -1.12% 收$334.56，光模組龍頭高位震盪，5日仍漲+16.2%")
])

m9 = tbl([
    line("PLTR", "逆勢走強 +1.07% 收$194.12，AIP商業化推進持續吸引買盤，近1月大漲+14.0%"),
    line("NOW", "持平微跌 -0.07% 收$137.87，企業工作流需求穩健"),
    line("CRM", "微跌 -0.19% 收$224.56，Agentforce發布後低位反覆築底"),
    line("ORCL", "下跌 -0.84% 收$143.56，雲端基建訂單支撐，但高估值承壓"),
    line("SNOW", "回調 -0.92% 收$332.85，數據雲端高位震盪"),
    line("ADBE", "重挫 -2.25% 收$232.77，創意軟體競爭擔憂重燃，近1月跌-9.5%")
])

m10 = tbl([
    line("NRG", "暴漲 +4.84% 收$108.61，獨立電力零售龍頭受AI算力長期購電協議熱度刺激，領漲電力股"),
    line("VST", "大漲 +3.88% 收$166.72！延續獲能源部最高42億美元貸款承諾利多，5日暴漲+20.5%"),
    line("CEG", "微幅消化 -0.27% 收$299.59，守穩昨日與Google簽約暴漲成果，全日維持高位整固"),
    line("PWR", "重挫 -2.57% 收$701.07，電力基建工程股大漲後獲利了結"),
    line("VRT", "下跌 -2.63% 收$246.49，散熱與液冷設備隨重工板塊回調"),
    line("ETN", "下跌 -3.09% 收$431.33，電氣設備權重股高位回吐"),
    line("GEV", "大跌 -3.12% 收$997.09，失守千元大關，電力設備類股整固"),
    line("OKLO", "重挫 -4.49% 收$36.82，小型模組化核反應爐（SMR）概念股高波動劇烈回檔")
])

m11 = '''<ul class="list-disc pl-5 space-y-2">
<li><b>Applied Digital（APLD，盤後飆升）</b>：公布 2027 會計年度第一季財報，營收達 3.419 億美元，較去年同期暴增 322%，碾壓分析師預期的 1.25–1.35 億美元區間；調整後每股虧損僅 $0.01，遠優於預期的每股虧損 $0.30。超大規模資料中心租賃訂單強勁落地，盤後股價飆升逾 10%。</li>
<li><b>Levi Strauss（LEVI，盤後微幅走強）</b>：公布 Q3 財報，營收 16.1 億美元大致符合預期（略低於預期的 16.2 億）；每股盈餘 $0.48，顯著擊敗預期的 $0.36，主要受益於關稅退稅收益與直營業務毛利率擴張。</li>
<li><b>Constellation Brands（STZ）</b>：延續前一日盤後公布平淡財報指引的跌勢，今日正規交易時段承壓。</li>
</ul>'''

s8 = sec(8, "重點個股新聞與異動", '<div class="space-y-3">' + details("8.1 大型科技七巨頭", m7, True) + details("8.2 AI 硬體 / 半導體重點股", m8) + details("8.3 軟體 / SaaS / AI 應用重點股", m9) + details("8.4 AI 電力 / 資料中心 / 能源基礎設施", m10) + details("8.5 其他顯著異動（財報與熱點股）", m11) + '<p class="text-xs text-slate-500">註：漲跌與區間根據 Yahoo Finance 官方報價；新聞與財報資料取自彭博、路透社、公司公告與可查證財經媒體。</p></div>')

# ---------- sec 9 ----------
s9 = sec(9, "財報日曆與財報解讀", f'''<div class="space-y-4">
  <div class="{BOX}"><h3 class="font-semibold mb-2">9.1 昨夜／盤後（10/7）重點財報解讀</h3>
    <div class="space-y-3 text-sm leading-relaxed">
      <p><b>Applied Digital (APLD，盤後大漲)</b>：FQ1 營收 $3.419 億美元（預期 ~$1.3 億，Beat >150%）；調整後 EPS -$0.01（預期 -$0.30，大幅收窄）。AI HPC 資料中心基礎設施加速交付，雲端算力客戶預付款及承諾租約暴增，驗證市場對資料中心算力基建的高景氣預期。</p>
      <p><b>Levi Strauss (LEVI，盤後微揚)</b>：Q3 營收 $16.1 億美元（預期 $16.2 億，年持平）；經調整 EPS $0.48（預期 $0.36，大幅超越）。直接面對消費者（DTC）業務維持雙位數增長，供應鏈優化提振利潤率。</p>
      <p><b>Constellation Brands (STZ)</b>：消化 Q2 業績，啤酒銷量增長但維持全年度偏謹慎指引，股價持續整固。</p>
    </div>
  </div>
  {table(["日期", "公司名稱及代號", "重要關注點與市場預期"], [
    ["10/8 週四 盤前", "PepsiCo (PEP)", "消費降級與定價能力、北美休閒零食與飲料銷量"],
    ["10/8 週四 盤前", "Progressive (PGR)", "車險承保利潤率、巨災損失與保費定價"],
    ["10/9 週五 盤前", "Delta Air Lines (DAL) / Domino's (DPZ)", "航空高端商務艙出行需求、燃料成本上升衝擊、外送消費趨勢"],
    ["10/14 下週三", "JPMorgan (JPM)、Wells Fargo (WFC)", "Q3財報季正式揭幕，淨利息收入（NII）與信貸撥備展望"]
  ])}
  <p class="text-xs text-slate-500">日曆來源：FactSet / Investing.com 財報日曆；實際公布時間以各公司投資人關係官網（IR）為準。</p></div>''')

# ---------- sec 10 ----------
s10 = sec(10, "機構觀點與資金流", f'''{paras([
    ("華爾街策略與FOMC紀要解讀", "華爾街大行多數認為，9月會議紀要確認了聯準會的鷹派防禦傾向。高盛策略團隊指出，雖然大盤估值在高利率環境下擴張受限，但標普500權重股具備極高的自由現金流收益率，能夠在『高殖利率＋溫和增長』的宏觀情境中提供抗跌緩衝；摩根大通則警告，若10年期殖利率持續突破5.35%並向5.50%推進，小型股與高負債工業股將面臨更大的去槓桿估值殺傷。"),
    ("ETF 資金流向與板塊輪動", f"ETF 資金流量官方數據 {NA}；但從價格走勢可清晰觀察：資金由週期工業（XLI -2.18%）、原物料（XLB -1.51%）與小型股（IWM -1.29%）大舉撤出，轉而流入防禦性醫療保健（XLV {PC('XLV')}）與公用事業（XLU {PC('XLU')}），顯示機構資金在財報季前夕進行去風險（De-risking）防禦配置。"),
    ("大宗交易與期權市場異動", f"大宗交易與內部人交易數據 {NA}。期權市場方面，VIX 看漲期權買盤在早盤殖利率衝高時段顯著升溫，推升 VIX 盤中最高衝至 16.01，但在尾盤大盤企穩後快速回吐，顯示機構主要進行日內防守性對沖而非恐慌性去庫存。"),
])}''')

# ---------- sec 11 ----------
s11 = sec(11, "板塊輪動判斷", paras([
    ("資金流入板塊", f"醫療保健（XLV {PC('XLV')}）成為全市場唯一顯著收紅的板塊，反映在利率攀升與紀要偏鷹背景下，具備非週期性獲利能力的防禦資產最受青睞；大型雲端軟硬體巨頭（AMZN {PC('AMZN')}、AAPL {PC('AAPL')}、GOOGL {PC('GOOGL')}）因資產負債表堅固而獲得避險資金駐留。"),
    ("資金流出板塊", f"工業設備（XLI {PC('XLI')}）、原物料（XLB {PC('XLB')}）、房地產（XLRE {PC('XLRE')}）及小型股（IWM {PC('IWM')}）領跌。此外，近期漲幅巨大的AI電力設備（GEV -3.12%、ETN -3.09%）與光通訊（LITE -1.97%）出現正常的獲利了結回調。"),
    ("AI 主線健康度與結構演變", "AI 主線依然健康，但內部輪動特徵極為劇烈：前期領跑的光通訊與電力設備短期進入估值消化期；而受供需基本面極度緊繃驅動的存儲晶片（MU +4.06%）、受政策與長期協議催化的獨立發電商（VST +3.88%、NRG +4.84%），以及盤後獲利暴增的資料中心算力基建（APLD）重新接棒領漲。市場處於『強趨勢創高後的健康高位洗盤』階段，尚未形成系統性頂部。"),
]))

# ---------- sec 12 watchlist ----------
W = [
    ("NVDA", "高位震盪", "回落-0.74%守穩$237，SpaceX合作傳聞持續發酵，支撐位$235"),
    ("AMD", "高位震盪", "微跌-0.55%收$645.86，在破兆市值平台良性整理"),
    ("AVGO", "繼續強勢", "逆勢抗跌+0.19%收$376.51，客製晶片外溢效應持續，5日+7.2%"),
    ("MRVL", "高位震盪", "微跌-0.81%收$284.68，投資人日大幅調高長期目標後高位消化"),
    ("GOOGL", "繼續強勢", "逆勢上揚+0.81%收$350.50，與CEG核電合作及Gemini生態加持"),
    ("MSFT", "高位震盪", "微漲+0.09%收$529.76，守穩歷史高位支撐區間"),
    ("META", "高位震盪", "回落-2.38%收$721.31，近1月大漲近18%後健康技術回踩"),
    ("AMZN", "繼續強勢", "大漲+1.42%收$259.92，雲端AWS獲利預期樂觀，七巨頭中最強"),
    ("ORCL", "低位修復", "回調-0.84%收$143.56，近5日反彈+4.6%，築底修復中"),
    ("CRM", "需要觀察", "微跌-0.19%收$224.56，Agentforce發布後低位反覆震盪"),
    ("NOW", "高位震盪", "持平微跌-0.07%收$137.87，軟體龍頭抗跌韌性極強"),
    ("SNOW", "高位震盪", "微跌-0.92%收$332.85，數據雲端高位整固"),
    ("ADBE", "破位風險", "大跌-2.25%收$232.77，失守短期均線，近1月重挫-9.5%"),
    ("PLTR", "繼續強勢", "逆勢走強+1.07%收$194.12，AIP商業化推進持續受買盤追捧"),
    ("LITE", "短線過熱", "高位回吐-1.97%收$1111.07，近5日仍暴漲+14.4%，技術指標超買"),
    ("COHR", "短線過熱", "回調-1.12%收$334.56，光通訊5日仍漲+16.2%，高位震盪加劇"),
    ("ANET", "繼續強勢", "逆勢小漲+0.22%收$215.83，高階資料中心交換機需求看好"),
    ("FLNC", "破位風險", "大跌-4.48%收$7.67，破底走弱，近1月崩跌-30.5%"),
    ("OKLO", "高位震盪", "重挫-4.49%收$36.82，SMR核能題材高波動劇烈回踩"),
    ("VST", "繼續強勢", "大漲+3.88%收$166.72！獲DOE 42億貸款利多續發酵，5日暴漲+20.5%"),
    ("CEG", "高位震盪", "微跌-0.27%收$299.59，守穩昨日Google協議爆發成果，5日累積+17.9%"),
    ("ETN", "回踩支撐", "下跌-3.09%收$431.33，電氣設備權重股高位回踩20日線"),
    ("VRT", "需要觀察", "回調-2.63%收$246.49，散熱設備隨基建板塊整理，月跌-15.3%"),
]

TAGC = {
    "繼續強勢": "bg-emerald-100 text-emerald-700 dark:bg-emerald-950 dark:text-emerald-300",
    "高位震盪": "bg-yellow-100 text-yellow-700 dark:bg-yellow-950 dark:text-yellow-300",
    "短線過熱": "bg-orange-100 text-orange-700 dark:bg-orange-950 dark:text-orange-300",
    "需要觀察": "bg-zinc-100 text-zinc-700 dark:bg-zinc-800 dark:text-zinc-300",
    "低位修復": "bg-sky-100 text-sky-700 dark:bg-sky-950 dark:text-sky-300",
    "回踩支撐": "bg-blue-100 text-blue-700 dark:bg-blue-950 dark:text-blue-300",
    "破位風險": "bg-rose-100 text-rose-700 dark:bg-rose-950 dark:text-rose-300"
}

wrows = []
for s, tag, nt in W:
    wrows.append([f"<b>{s}</b>", f"${PX(s)}", f'<span class="{C(P(s))}">{PC(s)}</span>', f'{q[s].get("5d", 0):+.1f}% / {q[s].get("1m", 0):+.1f}%', f'<span class="font-mono text-xs">日低 {q[s]["low"]:,.2f} / 日高 {q[s]["high"]:,.2f}</span>', nt, f'<span class="px-2 py-0.5 rounded text-xs font-semibold {TAGC[tag]}">{tag}</span>'])

s12 = sec(12, "我的重點關注股觀察", f'''<input id="watchSearch" type="text" placeholder="搜尋股票代號…" class="mb-3 w-full sm:w-72 px-3 py-2 text-sm rounded-lg border border-slate-200 dark:border-zinc-700 bg-white dark:bg-zinc-900">
  {table(["代號", "收盤", "當日", "近5日／近1月", "日內高低點", "核心動態與技術位", "判定標籤"], wrows, tid="watchTable", sortable={2})}
  <p class="mt-2 text-xs text-slate-500">註：追蹤涵蓋 NVDA、AMD、AVGO、MRVL、GOOGL、MSFT、META、AMZN、ORCL、CRM、NOW、SNOW、ADBE、PLTR、LITE、COHR、ANET、FLNC、OKLO、VST、CEG、ETN、VRT 等 23 檔核心標的。判定標籤為客觀技術與動能評級，非投資建議。</p>''')

# ---------- sec 13 ----------
s13 = sec(13, "明日交易計畫 / 觀察清單", f'''<div class="space-y-4">
  <div class="{BOX}"><h3 class="font-semibold mb-2">13.1 宏觀觀察要點</h3>
    <ul class="list-disc pl-5 text-sm space-y-1">
      <li><b>美債10年期殖利率</b>：觀察能否在 5.30%–5.35% 阻力區受阻回落；若持續升破 5.36% 將加大高估值科技股回調壓力。</li>
      <li><b>美元指數與匯率</b>：UUP 今日收 ${PX("UUP")}（+0.48%），觀察美元反彈是否持續壓抑黃金（現收 ${PX("GC=F",1)}）與大宗原油。</li>
      <li><b>經濟數據與官員發言</b>：明日重點聚焦初請失業金人數與批發庫存，評估就業市場降溫速度。</li>
      <li><b>VIX 波動率水位</b>：今日收 15.08，觀察能否持續守在 16.0 警戒線下方。</li>
    </ul>
  </div>
  <div class="{BOX}"><h3 class="font-semibold mb-2">13.2 大盤與結構關鍵位置</h3>
    <p class="text-sm"><b>SPY</b>：上方壓力 779.10（今日高點）與 781.62（歷史新高）；下方關鍵防守 773.61（今日低點），次級支撐為20日均線 765.62。<br/>
    <b>QQQ</b>：上方壓力 758.20，下方關鍵防守 751.76，次級支撐 731.61。<br/>
    <b>結構改善信號</b>：關注小型股 IWM（收 ${PX("IWM")}）在 RSI 逼近 35 時能否出現止跌反彈；若 IWM 繼續下挫，市場寬度將進一步承壓。</p>
  </div>
  <div class="{BOX}"><h3 class="font-semibold mb-2">13.3 核心板塊與重點個股觀察清單</h3>
    <p class="text-sm leading-relaxed">
      <b>最值得關注的個股</b>：<br/>
      1. <b>MU</b>：大漲+4.06%突破千元大關，觀察能否在千元上方形成強勢中繼。<br/>
      2. <b>APLD</b>：盤後公布爆表財報（營收暴增322%），明日開盤將成為 AI 資料中心算力風向標。<br/>
      3. <b>VST & NRG</b>：電力股龍頭續強，觀察獨立發電商的動能延續性與成交量。<br/>
      4. <b>CEG</b>：昨日暴漲12%後今日僅微跌0.27%，關注300美元整數關卡整固後的突破機會。<br/>
      5. <b>AMZN & AAPL</b>：七巨頭中防禦現金流代表，抗跌領跑的大盤定海神針。<br/>
      6. <b>NVDA & AMD</b>：高位震盪，觀察20日均線支撐力道與SpaceX等合作傳聞進展。<br/>
      7. <b>LITE & COHR</b>：光通訊雙雄5日飆升逾15%後回調，觀察急跌時的逢低承接力道。<br/>
      8. <b>ETN & GEV</b>：電力設備股今日回吐逾3%，觀察是否回踩20日均線獲支撐。<br/>
      9. <b>PEP & PGR</b>：明日盤前公布財報，觀察消費與金融保險定價權。<br/>
      10. <b>ADBE & FLNC</b>：走勢疲弱，需嚴格防範破位下殺風險。
    </p>
  </div>
</div>''')

# ---------- sec 14 risk ----------
RC = {
    "高": "bg-rose-100 text-rose-700 dark:bg-rose-950 dark:text-rose-300",
    "中高": "bg-orange-100 text-orange-700 dark:bg-orange-950 dark:text-orange-300",
    "中": "bg-yellow-100 text-yellow-700 dark:bg-yellow-950 dark:text-yellow-300",
    "低": "bg-emerald-100 text-emerald-700 dark:bg-emerald-950 dark:text-emerald-300"
}

risks = [
    ("宏觀利率風險", "高", "FOMC 紀要偏鷹促使10年期殖利率盤中飆至5.36%，長端殖利率若持續位於高位將嚴重壓制權益資產估值擴張空間"),
    ("市場寬度惡化", "高", "11大板塊中僅1個收紅，等權RSP跌幅近4倍於SPY，羅素2000連日破位暴跌，大盤漲勢過度依賴少數巨頭"),
    ("AI 賽道擁擠度", "中高", "半導體 SMH（RSI 80）與科技 XLK（RSI 84）仍處嚴重超買區，光通訊與電力設備板塊短線獲利回吐波動加劇"),
    ("財報季不確定性", "中", "下週銀行股財報即將登場，消費與傳統週期類股（如STZ）面臨指引下修考驗，盤面容錯率降低"),
    ("地緣與大宗商品", "中", "Brent 原油重返 $100 上方，高能源價格使通膨預期黏性上升，壓縮聯準會後續政策寬鬆空間"),
    ("技術面回踩風險", "中高", "三大指數在創下歷史新高後呈現假突破或高位背離風險，SPY 若失守 773 點將向下尋求20日均線支撐"),
    ("金融流動性環境", "中", "美元指數 UUP 強勢反彈，加密資產大跌，全球流動性微幅收斂，高槓桿中小盤股資金抽離明顯")
]

s14 = sec(14, "風險提示（視覺化風險矩陣）", table(["風險維度", "風險等級", "具體情境與解讀分析"], [[f"<b>{a}</b>", f'<span class="px-2 py-0.5 rounded font-semibold {RC[b]}">{b}</span>', c] for a, b, c in risks]))

# ---------- sec 15 ----------
s15 = f'''
    <section id="sec-15" class="scroll-mt-6 p-6 rounded-2xl bg-gradient-to-br from-white to-slate-50 dark:from-zinc-900 dark:to-zinc-950 border border-slate-200 dark:border-zinc-800 shadow-sm">
      <h2 class="{H2}"><span class="text-brand-500">{n}.</span> 最終結論</h2>
      <div class="space-y-3 text-sm sm:text-base leading-relaxed text-slate-700 dark:text-zinc-300">
        <p><strong>今日市場結論：</strong>標普500收 {PX("^GSPC")}（{PC("^GSPC")}）、納斯達克收 {PX("^IXIC")}（{PC("^IXIC")}），自歷史高位溫和回踩；道瓊下跌341點（{PC("^DJI")}），費半回吐 {PC("^SOX")}，羅素2000重挫 {PC("^RUT")}。FOMC 鷹派紀要引發10年期殖利率一度狂飆至5.36%，迫使市場進行防禦性調倉。盤面出現顯著分化：防禦型醫療保健（XLV +1.03%）、儲存晶片龍頭（MU +4.06%）、獨立電力商（VST +3.88%）與現金流大巨頭（AMZN、AAPL）抗跌領漲，而工業設備、房地產與中小盤股遭遇廣泛賣壓。</p>
        <p><strong>當前市場階段：</strong>強趨勢上漲後的「高位震盪回踩與劇烈板塊輪動」（大盤技術型態完好，但內部寬度惡化）。</p>
        <p><strong>操作傾向（中性表述）：</strong>目前指數並未出現趨勢性破位，但高估值成長股與多項ETF技術指標（SMH、XLK）嚴重超買，追高性價比顯著下降。建議耐心等待指數回踩關鍵支撐位（SPY 773點 / QQQ 751點）或殖利率回落企穩信號；關注焦點維持在業績高確定性的AI算力核心硬體（MU、APLD）、具有長期購電協議防護的電力龍頭（VST、CEG），以及防禦配置優勢的大型巨頭（AMZN、AAPL），並嚴格規避空頭破位的小型股與高負債弱勢板塊。</p>
        <div><strong>最值得關注的 5 個核心訊號：</strong>
          <ol class="list-decimal pl-6 mt-2 space-y-1">
            <li><b>10年期美債殖利率</b>：明日能否受阻於 5.30%–5.35% 阻力區，不再刷新高點。</li>
            <li><b>APLD 盤後暴漲之延續性</b>：觀察明日正規交易時段能否引領 AI 資料中心與算力基建板塊全面反彈。</li>
            <li><b>美光科技（MU）與存儲晶片</b>：在突破千元大關後能否守穩並帶動費半止跌。</li>
            <li><b>SPY 773.61 與 QQQ 751.76 日低防守</b>：尾盤抄底買盤能否延續，防範跌向20日均線。</li>
            <li><b>羅素2000（IWM）止跌信號</b>：小型股何時終結單邊下殺，市場寬度是否停止惡化。</li>
          </ol>
        </div>
        <p class="text-xs text-slate-500 mt-3">資料來源與聲明：價格與技術數據取自 Yahoo Finance 官方報價（至2026-10-07收盤），宏觀經濟與公司動態整合彭博、路透社、FactSet、美聯儲官方紀要與企業公告；未取得完整公開流之項目已於內文中清晰標註。本文僅供投資復盤與策略研究，不構成任何個人投資建議。</p>
      </div>
    </section>
'''.replace("{n}", "15")

# ---------- tail ----------
tail = old[old.index("<!-- Footer -->"):]
tail = re.sub(r"<div>美股收盤日報｜資料來源：.*?</div>", "<div>美股收盤日報｜資料來源：Yahoo Finance、FOMC官方會議紀要、彭博、路透社、FactSet、BEA、公司新聞稿與SEC申報檔案</div>", tail)

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

html = head + header + s0 + s1 + s2 + s3 + s4 + s5 + s6 + s7 + s8 + s9 + s10 + s11 + s12 + s13 + s14 + s15 + "\n  </main>\n</div>\n\n" + tail
out = R + f"reports/{D}-us-stock-closing-daily-report.html"
open(out, "w", encoding="utf-8").write(html)
print(f"Report written successfully to {out} (size: {len(html)} bytes)")

if "--no-publish" in sys.argv:
    sys.exit(0)

pub = R + ".antigravitycli/skills/html-report/scripts/publish.py"
res = subprocess.run(["python3", pub, out, TITLE, DESC], capture_output=True, text=True)
print("Publish STDOUT:\n", res.stdout)
if res.stderr:
    print("Publish STDERR:\n", res.stderr)
sys.exit(res.returncode)
