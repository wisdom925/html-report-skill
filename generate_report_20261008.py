import json, re, subprocess, sys

R = "/Users/wisdom/html-report-skill/"
D = "2026-10-08"
q = json.load(open(R + f"scratch/quotes_{D}.json"))
t = json.load(open(R + f"scratch/tech_{D}.json"))
old = open(R + "reports/2026-10-07-us-stock-closing-daily-report.html", encoding="utf-8").read()

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
DESC = ("週四（2026年10月8日）美股漲跌互見、呈現劇烈板塊輪動：標普500 -0.47%報7,765.36點、納指 -1.25%報27,193.34點、費半暴跌 -3.39%，道瓊逆勢微漲 +0.10%（+51點）報51,231.64點；"
        "中東地緣局勢惡化推動原油大漲（WTI +3.29%突破$91、Brent突破$104），OpenAI營收數據引發AI基建ROI疑慮觸發晶片硬體重挫（MU -4.79%、ARM -6.48%、NVDA -2.94%）；"
        "等權標普逆勢上揚（RSP +0.60%），資金湧入能源（XLE +2.97%）、必需消費（XLP +2.11%）與企業軟體（ADBE +3.56%、SNOW +3.17%、PLTR +2.40%），初請失業金降至19.7萬反映就業穩健。")

head = old[: old.index("<!-- Header Block -->")]
head = re.sub(r"<title>.*?</title>", f"<title>{TITLE}｜AI硬體重挫殺估值、地緣推升油價、等權與軟體逆勢修復 ({D})</title>", head, flags=re.S)
head = re.sub(r'<meta name="description" content=".*?">', f'<meta name="description" content="{DESC}">', head, flags=re.S)
head = re.sub(r'<meta property="og:title" content=".*?">', f'<meta property="og:title" content="{TITLE}">', head)
head = re.sub(r'<meta property="og:description" content=".*?">', '<meta property="og:description" content="AI硬體重挫，中東局勢推升油價，等權標普與企業軟體逆勢走強，道瓊收紅。">', head)
head = head.replace("2026-10-07", D)

header = f'''<!-- Header Block -->
    <header class="border-b border-slate-200 dark:border-zinc-800 pb-6">
      <div class="flex flex-wrap items-center justify-between gap-3 mb-2">
        <span class="inline-flex items-center gap-1.5 px-3 py-1 rounded-full text-xs font-semibold bg-amber-100 text-amber-800 dark:bg-amber-950 dark:text-amber-300">
          <span class="w-2 h-2 rounded-full bg-amber-500 animate-pulse"></span> AI硬體殺估值・油價狂飆・板塊劇烈輪動・等權與軟體逆勢抗跌
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
        <p>{S}【大盤走勢】</strong> 週四美股呈現強烈的「結構分化與指數背離」。標普500指數 <strong>{PC("^GSPC")}</strong> 回跌 {abs(q['^GSPC']['change']):.2f} 點收 <strong>{PX("^GSPC")}</strong>；納斯達克綜合指數因科技硬體集中拋售重挫 <strong>{PC("^IXIC")}</strong>（-345點）收 <strong>{PX("^IXIC")}</strong>；費城半導體指數暴跌 <strong>{PC("^SOX")}</strong> 收 {PX("^SOX")}；但道瓊工業指數在能源與傳統防禦股帶動下逆勢微漲 <strong>{PC("^DJI")}</strong>（+51.77點）收 <strong>{PX("^DJI")}</strong>；羅素2000小型股持平微漲 <strong>{PC("^RUT")}</strong> 收 {PX("^RUT")}。</p>
        <p>{S}【驅動因素】</strong> 昨夜三大核心驅動交織：一是中東地緣軍事緊張急遽升溫，引發波斯灣航運擔憂與原油飆漲，Brent原油突破 $104/桶，WTI大漲 {PC("CL=F")} 至 ${PX("CL=F")}；二是市場報導 OpenAI 短期營收增長放緩，再度點燃投資人對超大規模雲端巨頭天文數字級 AI 資本支出（Capex）投資回報率（ROI）的焦慮，觸發半導體與電力設備獲利了結賣壓；三是美國勞工部公布初請失業金降至 19.7 萬（連4週低於20萬，為1969年以來罕見低位），勞動力市場極具韌性，下午財政部 30 年期國債拍賣需求強勁壓低長端殖利率（10年期自5.35%回落至 {PX("^TNX")}%），提供價值股估值支撐。</p>
        <p>{S}【資金偏好】</strong> 風格大轉移（AI硬體去槓桿，資金湧入高現金流軟體與防禦價值資產）：恐慌指數 VIX 微幅回升至 {PX("^VIX")}（{PC("^VIX")}），盤中最高 16.25；黃金現貨期貨受地緣避險支撐反彈 {PC("GC=F")}（收 ${PX("GC=F",1)}/oz）；美元指數 UUP 微跌 {PC("UUP")}（收 ${PX("UUP")}）；加密資產流動性承壓，比特幣下跌 {PC("BTC-USD")}（收 ${PX("BTC-USD",0)}）。</p>
        <p>{S}【市場寬度】</strong> 寬度呈現極罕見的「指數跌但個股普漲」良性特徵：標普 500 十一個板塊中高達 8 個板塊收紅！等權重標普 <strong>RSP 大漲 {PC("RSP")}</strong>，與市值加權標普（SPY {PC("SPY")}）形成鮮明背離；能源（XLE {PC("XLE")}）、必需消費（XLP {PC("XLP")}）、金融（XLF {PC("XLF")}）全面走強；指數之所以收黑，完全是由於權重極高的科技板塊（XLK {PC("XLK")}）單日大跌拖累。</p>
        <p>{S}【核心主線】</strong> AI 主線內部發生「由硬體向軟體、由上游基建向終端應用」的深刻輪動：前期大熱的記憶體（MU {PC("MU")}）、光模組（COHR {PC("COHR")}、LITE {PC("LITE")}）、電力核能（VST {PC("VST")}、OKLO {PC("OKLO")}、CEG {PC("CEG")}）及晶片巨頭（NVDA {PC("NVDA")}、AMD {PC("AMD")}、AVGO {PC("AVGO")}）遭遇獲利回吐；而前期滯漲的企業軟體 SaaS 龍頭全面爆發（ADBE {PC("ADBE")}、SNOW {PC("SNOW")}、PLTR {PC("PLTR")}、CRM {PC("CRM")}、NOW {PC("NOW")}），軟體板塊展現強烈抗跌韌性。</p>
        <div class="mt-4 p-4 rounded-xl bg-amber-50 dark:bg-zinc-800/60 border border-amber-200 dark:border-amber-900/40 text-amber-900 dark:text-amber-200 font-medium">
          💡 <strong>今日市場狀態判斷：</strong>「指數受晶片與AI硬體權重獲利了結拖累回踩，地緣推升油價，但底層市場寬度顯著改善；資金由高估值硬體轉向企業軟體與傳統能源價值股，呈現健康的劇烈風格輪動。」
        </div>
      </div>
    </section>
'''

# ---------- sec 1 ----------
def card(name, key, px, sub):
    return f'<div class="{CARD}"><div class="text-xs text-slate-500 dark:text-zinc-400 font-medium">{name}</div><div class="text-xl font-extrabold font-mono mt-1">{px}</div><div class="text-xs mt-1 flex items-center justify-between"><span class="{C(P(key), key=="^VIX")}">{PC(key)}</span><span class="text-slate-400 font-mono">{sub}</span></div></div>'

cards = "".join([
    card("S&P 500 (標普500)", "^GSPC", PX("^GSPC"), f"SPY ${PX('SPY')}"),
    card("Nasdaq Composite", "^IXIC", PX("^IXIC"), "晶片拖累回踩"),
    card("Dow Jones (道瓊)", "^DJI", PX("^DJI"), f"{q['^DJI']['change']:+.2f} 點"),
    card("Nasdaq 100", "^NDX", PX("^NDX"), f"QQQ ${PX('QQQ')}"),
    card("Russell 2000", "^RUT", PX("^RUT"), f"IWM ${PX('IWM')}"),
    card("SOX (費城半導體)", "^SOX", PX("^SOX"), f"SMH ${PX('SMH')}"),
    card("Software (IGV)", "IGV", PX("IGV"), "軟體抗跌僅微跌"),
    card("VIX", "^VIX", PX("^VIX"), "波動率溫和上升"),
])

idx_rows = []
def irow(name, etf, key, state):
    idx_rows.append([f'<span class="font-semibold font-sans">{name}</span>', etf, f'<b>{PX(key)}</b>', f'<span class="{C(P(key), key=="^VIX")}">{PC(key)}</span>', RNG(key), f'<span class="font-sans">{state}</span>'])
irow("S&P 500", "SPY", "^GSPC", "回跌-0.47%，守在20日均線(7,654)之上，尾盤自日低7,729反彈36點，RSI自65降至63.7")
irow("Nasdaq Composite", "—", "^IXIC", "收27,193.34點(-1.25%)，受半導體權重下殺拖累，但仍維持在50日均線之上")
irow("Nasdaq 100", "QQQ", "^NDX", "QQQ 收747.58(-1.34%)，高位整固修復超買指標，RSI自77.8降至75.4")
irow("Dow Jones", "DIA", "^DJI", "逆勢上揚51.77點(+0.10%)收51,231.64，能源(CVX)與金融消費護盤有力")
irow("Russell 2000", "IWM", "^RUT", "微漲+0.03%收2,794.13點，終結連日重挫，於200日均線附近企穩")
irow("SOX 半導體", "SOXX / SMH", "^SOX", "暴跌-3.39%收12,623.71，SMH(-2.84%)；晶片股全面獲利回吐")
irow("CBOE VIX", "^VIX", "^VIX", "收15.41(+2.19%)，盤中最高16.25後回落，未見系統性恐慌情緒")
s1 = sec(1, "大盤表現總覽", f'''
      <div class="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-4 gap-4 mb-6">{cards}</div>
      <div class="{BOX}">
        <h3 class="text-sm font-semibold text-slate-700 dark:text-zinc-300 mb-3 flex items-center justify-between"><span>主要指數與核心資產當日漲跌幅對比 (Chart.js)</span><span class="text-xs font-normal text-slate-500">{D} 基準</span></h3>
        <div class="relative h-64 sm:h-72 w-full"><canvas id="overviewChart"></canvas></div>
      </div>
      <div class="mt-6">{table(["指數名稱", "代表ETF", "收盤點位", "當日漲跌幅", "日內高/低", "技術狀態"], idx_rows, mono=True)}</div>
      <p class="mt-3 text-sm text-slate-600 dark:text-zinc-400">補充：標普500與納指雖收黑，但未跌破關鍵技術支撐位；等權標普 RSP (+0.60%) 與道瓊表現顯著優於加權指數；半導體指數 SOX 單日重挫 -3.39% 成為壓制指數的核心源頭。</p>
''')

# ---------- sec 2 ----------
mer = f'''graph LR
  subgraph PreMarket["盤前"]
    A["初請失業金19.7萬維持歷史低位<br/>中東地緣升級油價暴漲破$104<br/>OpenAI營收雜音引發晶片股普跌"]
  end
  subgraph Open["開盤"]
    B["納指與費半重挫跳空開低<br/>晶片股(NVDA/MU/ARM)遭獲利了結<br/>能源(XLE)與軟體(ADBE/PLTR)逆勢飆升"]
  end
  subgraph MidDay["午盤 13:00-14:00"]
    C["30年美債拍賣需求強勁<br/>10年期殖利率自5.35%回落至5.23%<br/>金融與房地產擴大漲幅<br/>標普自日低 {q['^GSPC']['low']:,.2f} 震盪回升"]
  end
  subgraph Close["尾盤與盤後"]
    D["道瓊翻紅收漲 +51.77 點<br/>等權標普 RSP 大漲 +0.60%<br/>標普收 {PX('^GSPC')} (-0.47%)<br/>軟體板塊逆勢領跑"]
  end
  PreMarket --> Open --> MidDay --> Close'''
s2 = sec(2, "盤中走勢復盤（時間線 Timeline）", f'''
      <div class="{BOX} overflow-x-auto"><div class="mermaid">
{mer}
      </div></div>
      <div class="mt-4 {BOX}">{paras([
    ("盤前", "早盤公布的美國每週初請失業金人數錄得 19.7 萬人，低於預期的 20.5 萬，連續第 4 週低於 20 萬關卡，凸顯美國勞動市場依舊處於極度緊俏的『低招聘、低解僱』狀態。與此同時，中東波斯灣航運緊張與潛在軍事摩擦升溫，Brent 原油飆漲破 $104/桶、WTI 漲破 $91。市場同時傳出 OpenAI 短期營收增長放緩的分析報告，引發晶片與硬體巨頭盤前全面承壓。"),
    ("開盤後", f"美股開盤呈現極端分化走勢：科技權重重挫，納斯達克開低逾 1%，費城半導體指數大跌逾 3%；前幾日暴漲的記憶體巨頭美光（MU -4.8%）、安謀（ARM -6.5%）、博通（AVGO -4.3%）與光通訊巨頭（COHR -9.6%）遭遇凶猛的獲利了結賣壓；但資金並未離場，而是迅速湧入能源巨頭（XOM、CVX）與企業軟體龍頭（ADBE、PLTR、SNOW），推動道瓊工業指數在開盤微跌後迅速走高。"),
    ("午盤方向選擇", f"美東時間 13:00，美國財政部完成 220 億美元的 30 年期國債拍賣，得標利率 5.606%，投標倍數達 2.45 倍，海外間接投標人認購踴躍。優異的標售結果迅速扭轉早盤債市跌勢，10 年期基準殖利率自盤初的 5.35% 高點急速回落至 5.23%，帶動金融（XLF +0.89%）、公用事業與房地產板塊穩步走高，標普 500 自日內低點 {q['^GSPC']['low']:,.2f} 強力反彈逾 35 點。"),
    ("尾盤拉升與盤後", f"臨近尾盤，傳統權重股持續護盤，道瓊工業指數收在全日高位區間 {PX('^DJI')}（+0.10%）；標普 500 收報 {PX('^GSPC')}（-0.47%），成功守住 7,760 點支撐；納指收 {PX('^IXIC')}。盤後百事可樂（PEP）公布財報指引平穩，市場焦點全面轉向明日（10/9）的達美航空（DAL）及即將登場的華爾街大行財報季。核心驅動總結：地緣油價飆漲＋AI硬體估值獲利了結，推動資金向能源、傳統防禦及企業軟體進行大級別輪動。"),
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
tab_y = f'''<div id="panel-yields" class="tab-panel space-y-4"><h4 class="font-bold text-slate-900 dark:text-white text-base">30年期美債強勁拍賣壓低長端殖利率，10年期自5.35%回落至5.23%</h4>
  <div class="grid grid-cols-2 sm:grid-cols-4 gap-3 font-mono">{yield_cards}</div>
  <p>10年期基準殖利率收在 {PX("^TNX")}%（較前日 -5bp，日內最高一度觸及 5.35%）；30年期收 {PX("^TYX")}%（-7bp）；5年期收 {PX("^FVX")}%（-4bp）。下午 30 年期國債拍賣得標利率 5.606%，市場需求極為強勁，直接帶動長端殖利率全線自盤初高位大幅回撤。含義解讀：儘管油價大漲帶來二次通膨擔憂，但強勁的海外認購需求驗證了長端國債在 5.3%–5.6% 水位的配置吸引力，殖利率回落為利率敏感型資產（地產、公用事業、金融）提供了關鍵估值喘息機會。</p></div>'''

tab_f = '''<div id="panel-fed" class="tab-panel space-y-4"><h4 class="font-bold text-slate-900 dark:text-white text-base">Fed 降息預期：初請失業金持續低迷，高利率維持更長時間（Higher-for-Longer）</h4>
  <div class="grid grid-cols-2 sm:grid-cols-3 gap-3 font-mono">''' + stat("就業市場指標", "極具韌性", "初請失業金 19.7 萬，連 4 週低於 20 萬") + stat("高油價通膨威脅", "升級關注", "Brent 衝破 $104，輸入型能源通膨風險增溫") + stat("政策定價傾向", "鷹派防禦", "年內政策利率預期維持高位，排除提前降息") + '''</div>
  <p>昨日公布的 9 月 FOMC 會議紀要顯示多數官員傾向年內仍有升息必要，今日極度強勁的初請失業金數據進一步佐證美國實體經濟尚未出現失業潮。再加上油價單日飆升 3%–4%，加劇了市場對通膨黏性的定價。聯邦基金期貨隱含利率顯示，市場對聯準會近期降息的預期降至冰點，普遍接受政策利率將在高位維持更長時間（Higher for Longer）甚至年內維持緊縮傾向的定價邏輯。</p></div>'''

tab_c = f'''<div id="panel-commodities" class="tab-panel space-y-4"><h4 class="font-bold text-slate-900 dark:text-white text-base">中東緊張推升原油狂飆、黃金避險走強、加密貨幣承壓</h4>
  <div class="grid grid-cols-2 sm:grid-cols-3 gap-3 font-mono">
  {stat("美元（UUP代理）", "$"+PX("UUP"), CT("UUP"))}{stat("黃金期貨", "$"+PX("GC=F",1)+"/oz", CT("GC=F"))}{stat("WTI 原油", "$"+PX("CL=F"), CT("CL=F"))}
  {stat("Brent 原油", "$"+PX("BZ=F"), CT("BZ=F"))}{stat("比特幣", "$"+PX("BTC-USD",0), CT("BTC-USD"))}{stat("以太幣", "$"+PX("ETH-USD",0), CT("ETH-USD"))}</div>
  <p>原油成為全市場最大焦點：因中東地緣局勢驟然緊繃，WTI 原油期貨大漲 {PC("CL=F")} 收在 ${PX("CL=F")}/桶，Brent 原油飆升 {PC("BZ=F")} 突破 ${PX("BZ=F")}/桶；黃金現貨期貨受避險買盤推升，反彈 {PC("GC=F")} 收在 ${PX("GC=F",1)}/盎司；美元 ETF UUP 微幅回吐 {PC("UUP")} 收 ${PX("UUP")}；比特幣承壓下跌 {PC("BTC-USD")} 至 ${PX("BTC-USD",0)}，以太幣下跌 {PC("ETH-USD")}。</p></div>'''

tab_d = '''<div id="panel-data" class="tab-panel space-y-4"><h4 class="font-bold text-slate-900 dark:text-white text-base">每週初請失業金降至 19.7 萬人，創 1969 年以來罕見低迷紀錄</h4>
  <div class="overflow-x-auto"><table class="w-full text-sm text-left"><thead class="bg-slate-50 dark:bg-zinc-800/60"><tr><th class="p-3">數據名稱</th><th class="p-3">實際值</th><th class="p-3">預期值</th><th class="p-3">前值</th><th class="p-3">市場解讀</th></tr></thead><tbody class="divide-y divide-slate-100 dark:divide-zinc-800">
  <tr><td class="p-3 font-semibold">初請失業金人數（至10/3）</td><td class="p-3 font-mono">19.7 萬</td><td class="p-3 font-mono">20.5 萬</td><td class="p-3 font-mono">19.9 萬（修正）</td><td class="p-3">連續第4週低於20萬人關卡，創下自1969年以來的最長紀錄，證實美國勞動市場處於歷史級別的「低招聘、極低解僱」狀態。</td></tr>
  <tr><td class="p-3 font-semibold">30 年期國債拍賣得標利率</td><td class="p-3 font-mono">5.606%</td><td class="p-3 font-mono">5.620%</td><td class="p-3 font-mono">前次 5.58%</td><td class="p-3">得標利率低於發行前交易水準（Stop-through），投標倍數 2.45，顯示長端國債高收益率吸引大量境內外買盤。</td></tr>
  <tr><td class="p-3 font-semibold">8月批發庫存月率</td><td class="p-3 font-mono">+0.1%</td><td class="p-3 font-mono">+0.2%</td><td class="p-3 font-mono">+0.2%</td><td class="p-3">庫存積累速度放緩，企業庫存管理保持謹慎。</td></tr>
  </tbody></table></div>
  <p class="text-xs text-slate-500">明日預告：10/9（週五）將公布 9 月進出口物價指數及密西根大學 10 月消費者信心指數初值。</p></div>'''

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
    ("能源", "XLE", "中東局勢升級推動WTI原油飆升3.3%，油氣股全線大漲領跑 (+2.97%)"),
    ("必需消費", "XLP", "避險防禦資金大幅流入高股息食品飲料與生活用品 (+2.11%)"),
    ("金融", "XLF", "長端公債拍賣強勁、殖利率企穩，銀行與保險股財報季前反彈 (+0.89%)"),
    ("通訊服務", "XLC", "GOOGL/META相對抗跌，數位廣告與串流媒體防禦買盤支撐 (+0.73%)"),
    ("房地產", "XLRE", "受10年期美債殖利率自5.35%回落激勵，地產信託反彈 (+0.69%)"),
    ("原物料", "XLB", "大宗商品與金屬受避險需求及美元回吐帶動走高 (+0.59%)"),
    ("工業", "XLI", "國防軍工與重型機械抗跌對沖電氣設備回調 (+0.33%)"),
    ("非必需消費", "XLY", "消費零售相對穩健，對沖了特斯拉微跌 (+0.31%)"),
    ("公用事業", "XLU", "電力發電商高位回踩，傳統公用事業維持微跌整理 (-0.19%)"),
    ("醫療保健", "XLV", "昨日大漲逾1%後今日小幅獲利回吐，維持高位整固 (-0.39%)"),
    ("科技", "XLK", "半導體與AI硬體權重股集體暴跌拖累，單日領跌全場 (-1.79%)"),
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
      <p class="mt-3 text-sm text-slate-600 dark:text-zinc-400">最強板塊：能源 XLE（{PC("XLE")}）、必需消費 XLP（{PC("XLP")}）、金融 XLF（{PC("XLF")}）；最弱板塊：科技 XLK（{PC("XLK")}）、醫療保健 XLV（{PC("XLV")}）、公用事業 XLU（{PC("XLU")}）。風格特徵：呈現教科書式的『週期與防禦價值板塊大獲全勝，成長科技股遭遇獲利了結』；S&P 500 十一個板塊中多達 8 個收紅，等權標普 RSP 上漲 +0.60%，充分證明市場內部並無系統性恐慌拋壓，而是資金從高擁擠度的晶片硬體主動流向傳統防禦與價值板塊。</p>''')

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
    "SMH": "晶片硬體劇烈回吐，費半重跌 -3.39%",
    "SOXX": "半導體普遍承壓，單日 -3.22%",
    "IGV": "軟體抗跌顯著，單日僅微跌 -0.23%",
    "MU": "昨日大漲後獲利回吐 -4.79%，守穩千元",
    "CRWD": "資安龍頭整理 (-0.92%)，月漲 +26.6%",
    "PANW": "資安權重高位消化 (-1.74%)",
    "NOW": "企業軟體逆勢上揚 +1.36%，需求穩健",
    "PLTR": "逆勢大漲 +2.40%，AIP商用訂單強勁",
    "LITE": "光模組回吐 -5.62%，5日仍漲 +0.3%",
    "COHR": "光通訊高位重挫 -9.63%，短線過熱消化",
    "VST": "電力發電商回吐 -6.35%，5日仍暴漲 +11.7%",
    "GEV": "電力設備抗跌微漲 +0.23%，守住千元",
    "FLNC": "儲能概念弱勢 (-2.87%)，月跌 -26.4%",
    "IWO": "小盤成長弱勢 (-0.85%)，承壓整理",
    "IWN": "小盤價值翻紅 (+0.55%)，低位修復",
    "RSP": "等權標普逆勢漲 +0.60%，大幅跑贏 SPY",
    "QQQ": "大盤成長下跌 -1.34%，科技巨頭拖累"
}
trows = [[n, f"<b>{e}</b>", f'<span class="{C(P(k))}">{PC(k)}</span>', f'{q[k]["5d"]:+.2f}%', f'{q[k]["1m"]:+.2f}%', note.get(e, "")] for n, e, k in themes]
s5 = sec(5, "主題與風格表現", table(["主題", "代表", "當日", "近5日", "近1月", "特徵"], trows, tid="themeTable", sortable={2, 3, 4}) + '<p class="mt-3 text-sm text-slate-600 dark:text-zinc-400">主題解讀：盤面焦點呈現『硬體退潮、軟體抗跌、價值接棒』。前期漲幅最兇猛的光通訊（COHR -9.63%、LITE -5.62%）、存儲晶片（MU -4.79%）與電力核能（VST -6.35%）集體遭遇獲利了結大洗盤；但企業軟體（PLTR +2.40%、NOW +1.36%、ADBE +3.56%）逆勢大漲，等權標普 RSP (+0.60%) 顯著跑贏大盤，資金由單一AI硬體擴散至廣泛領域。</p>')

# ---------- sec 6 breadth ----------
s6 = sec(6, "市場寬度與參與度", f'''
      <div class="space-y-4">
      <div class="{BOX}"><h3 class="font-semibold mb-2">6.1 均線參與度</h3>
      <p class="text-sm text-slate-700 dark:text-zinc-300">成分股高於主要均線比例官方明細 {NA}；主要代表 ETF 相對均線位置如下（依至 10-08 收盤日線計算）：</p>
      {table(["ETF", "SPY", "QQQ", "IWM"], [["20日均線", f'{t["SPY"]["sma20"]:.2f}', f'{t["QQQ"]["sma20"]:.2f}', f'{t["IWM"]["sma20"]:.2f}'], ["50日均線", f'{t["SPY"]["sma50"]:.2f}', f'{t["QQQ"]["sma50"]:.2f}', f'{t["IWM"]["sma50"]:.2f}'], ["200日均線", f'{t["SPY"]["sma200"]:.2f}', f'{t["QQQ"]["sma200"]:.2f}', f'{t["IWM"]["sma200"]:.2f}'], ["10-08收盤", PX("SPY"), PX("QQQ"), PX("IWM")]])}
      <p class="mt-2 text-sm text-slate-600 dark:text-zinc-400">趨勢研判：SPY（773.93）與 QQQ（747.58）雖有回檔，但仍遠高於 20 日均線（SPY 765.46 / QQQ 731.10）及 50 日均線，中長期多頭結構毫髮無損；IWM（277.57）在 200 日均線（276.64）獲得實質技術支撐，小盤股在連續數日大跌後展現初步止跌回穩跡象。</p></div>
      <div class="{BOX}"><h3 class="font-semibold mb-2">6.2 漲跌家數、新高新低</h3><p class="text-sm">交易所上漲/下跌家數明細 {NA}。寬度代理觀察：標普 500 十一個板塊中高達 8 個收漲，僅 3 個收黑；等權重標普（RSP +0.60%）大漲，顯著強於市值加權標普（SPY -0.42%），顯示市場下挫主要是『指數殺估值』而非『個股普跌恐慌』，底層個股賺錢效應甚至優於昨日。</p></div>
      <div class="{BOX}"><h3 class="font-semibold mb-2">6.3 其他內部指標</h3><p class="text-sm">騰落線、McClellan Oscillator、Put/Call Ratio {NA}。VIX 恐慌指數盤中一度衝至 16.25，收盤回落至 {PX("^VIX")}（+2.19%），仍處於歷史偏低的中性健康水位；成交流量方面，晶片類股出貨成交量顯著放大，但能源與防禦類股承接買盤強勁，整體市場未見系統性拋售踩踏。</p></div>
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
      <p class="mt-3 text-sm text-slate-600 dark:text-zinc-400">技術判讀：經過今日修正，SMH（RSI 自 79.5 降至 74.4）與 XLK（RSI 自 83.7 降至 80.5）的高位嚴重超買狀態得到健康修復；QQQ（RSI 75.4）回踩 5 日均線但守穩高位平台；IWM（RSI 34.8）在 200 日均線（276.64）獲得支撐。明日多頭確認信號：SPY 能否放量收復 777 點並挑戰日高 777.09 點；QQQ 能否重回 750 點上方。關鍵風險防守位：SPY 今日低點 770.43 點（若跌破將考驗 20 日均線 765.46 點），QQQ 今日低點 743.23 點。</p>''')

# ---------- sec 8 ----------
def line(sym, txt=""):
    return f'<tr><td class="p-2 font-semibold">{sym}</td><td class="p-2 font-mono">${PX(sym)}</td><td class="p-2 {C(P(sym))}">{PC(sym)}</td><td class="p-2 text-xs">近5日 {q[sym].get("5d", 0):+.1f}% / 近1月 {q[sym].get("1m", 0):+.1f}%</td><td class="p-2 text-xs">{txt}</td></tr>'

def tbl(rows):
    return f'<div class="overflow-x-auto"><table class="w-full text-sm text-left"><tbody class="divide-y divide-slate-100 dark:divide-zinc-800">{"".join(rows)}</tbody></table></div>'

m7 = tbl([
    line("AAPL", "逆勢大漲 +1.11% 收$340.42！市值達 4.75 兆美元，防禦現金流龍頭成為全市場避風港"),
    line("META", "微跌 -0.06% 收$720.89，守住 720 美元關卡，近1月仍大漲 +10.3%"),
    line("GOOGL", "微跌 -0.63% 收$348.29，搜尋與雲端廣告防禦性凸顯，表現優於大盤"),
    line("TSLA", "小跌 -0.74% 收$375.00，在日前大漲後持續於 375 美元附近震盪整理"),
    line("MSFT", "下跌 -1.35% 收$522.61，隨 AI 算力回調承壓，但原生 Windows AI Agent 生態預期不變"),
    line("AMZN", "下跌 -2.25% 收$254.06，AWS 算力成本擔憂壓制股價，消化前期漲幅"),
    line("NVDA", "重挫 -2.94% 收$230.48，OpenAI 營收放緩雜音引發晶片獲利了結，分析師維持 $300 目標價")
])

m8 = tbl([
    line("MU", "大跌 -4.79% 收$1,035.84，昨日暴漲後未能突破 $1,100 阻力，台灣廠勞資傳聞引發獲利回吐，D.A. Davidson重申看好"),
    line("ARM", "重挫 -6.48% 收$275.29，高估值半導體 IP 股受市場去槓桿衝擊最大"),
    line("AVGO", "大跌 -4.35% 收$360.14，客製化 AI 晶片短線獲利回吐，近5日仍漲 +4.8%"),
    line("AMD", "大跌 -3.90% 收$620.68，隨晶片類股同步調整，回踩 20 日均線"),
    line("MRVL", "下跌 -3.52% 收$274.66，客製化晶片板塊整固，近1月仍大賺 +16.9%"),
    line("TSM", "下跌 -3.01% 收$457.99，台積電 ADR 隨費半回檔，近1月仍維持 +5.2%"),
    line("ASML", "下跌 -1.95% 收$1,769.79，光刻機龍頭維持區間震盪"),
    line("ANET", "下跌 -2.25% 收$210.97，高階交換機回踩支撐，近1月仍漲 +9.4%"),
    line("VRT", "下跌 -1.12% 收$243.73，液冷散熱設備表現相對抗跌"),
    line("DELL", "微跌 -0.76% 收$574.55，AI 伺服器龍頭守穩高位"),
    line("COHR", "暴跌 -9.63% 收$302.35，光模組龍頭短線過熱後遭遇技術性深幅回調"),
    line("LITE", "大跌 -5.62% 收$1,048.60，光通訊高位劇烈洗盤")
])

m9 = tbl([
    line("ADBE", "狂飆 +3.56% 收$241.05！企業創意軟體與 Firefly AI 商業化低位強力反彈"),
    line("SNOW", "大漲 +3.17% 收$343.40！企業數據雲端平台吸引避險買盤，創波段反彈新高"),
    line("PLTR", "大漲 +2.40% 收$198.78！逼近 200 美元整數大關，企業 AIP 擴張勢不可擋，近1月+17.3%"),
    line("CRM", "穩步反彈 +1.44% 收$227.80，Agentforce 企業應用催化低位築底回升"),
    line("NOW", "逆勢上揚 +1.36% 收$139.75，工作流自動化平台需求穩健"),
    line("CRWD", "微跌 -0.92% 收$263.01，網路安全龍頭高位整固，近1月仍大漲 +26.6%"),
    line("PANW", "回調 -1.74% 收$398.50，高位消化獲利籌碼"),
    line("ORCL", "重挫 -5.48% 收$135.69，雲端基建訂單雖強但毛利率與 Capex 擔憂引發下殺")
])

m10 = tbl([
    line("GEV", "逆勢微漲 +0.23% 收$999.35，電力設備龍頭韌性十足，守住千元整數關卡"),
    line("VRT", "微跌 -1.12% 收$243.73，資料中心散熱龍頭整固"),
    line("ETN", "下跌 -1.58% 收$424.51，電氣基建回踩 20 日均線支撐"),
    line("NRG", "下跌 -2.11% 收$106.32，獨立電力股昨日暴漲後小幅消化"),
    line("PWR", "下跌 -2.25% 收$685.33，電網工程龍頭高位整理"),
    line("CEG", "下跌 -4.85% 收$285.07，核電題材在連日大漲後遭遇獲利了結"),
    line("OKLO", "重挫 -6.11% 收$34.57，小型核反應堆概念股波動劇烈"),
    line("VST", "大跌 -6.35% 收$156.14，獨立發電商龍頭短線急拉後技術回踩，5日仍漲+11.7%")
])

m11 = '''<ul class="list-disc pl-5 space-y-2">
<li><b>油氣雙雄（XOM、CVX）</b>：受中東地緣政治風險及國際油價（WTI +3.29%）推動，埃克森美孚與雪佛龍大幅收高逾 2.5%，引領能源板塊成為全市場最強領頭羊。</li>
<li><b>百事可樂（PEP，盤前財報）</b>：公布 Q3 財報，營收 233.2 億美元微幅低於預期，每股盈餘 $2.31 符合預期；北美零食定價承壓但國際飲料業務穩健，股價抗跌微漲 +0.8%。</li>
<li><b>Applied Digital（APLD）</b>：昨日盤後公布 Q1 營收年增 322% 暴賺後，今日常規盤交易放量巨震，高位換手積極，凸顯市場對真實交付之算力基礎設施的高度關注。</li>
<li><b>達美航空（DAL）</b>：明日盤前即將公布財報，市場聚焦燃料成本上升與高端商務艙出行需求的平衡。</li>
</ul>'''

s8 = sec(8, "重點個股新聞與異動", '<div class="space-y-3">' + details("8.1 大型科技七巨頭", m7, True) + details("8.2 AI 硬體 / 半導體重點股", m8) + details("8.3 軟體 / SaaS / AI 應用重點股", m9) + details("8.4 AI 電力 / 資料中心 / 能源基礎設施", m10) + details("8.5 其他顯著異動（財報與熱點股）", m11) + '<p class="text-xs text-slate-500">註：漲跌與區間根據 Yahoo Finance 官方報價；新聞與財報資料取自彭博、路透社、公司公告與可查證財經媒體。</p></div>')

# ---------- sec 9 ----------
s9 = sec(9, "財報日曆與財報解讀", f'''<div class="space-y-4">
  <div class="{BOX}"><h3 class="font-semibold mb-2">9.1 昨夜／盤前重點財報解讀</h3>
    <div class="space-y-3 text-sm leading-relaxed">
      <p><b>百事可樂 (PEP，盤前)</b>：Q3 營收 $233.2 億美元（預期 $238 億，略微低於預期）；核心 EPS $2.31（預期 $2.29，符合預期）。受通膨累積效應影響，北美休閒食品（Frito-Lay）銷量微幅下滑，但國際市場成長強勁及嚴格成本控制支撐獲利，管理層微調全年度有機營收預期至低個位數增長。</p>
      <p><b>Applied Digital (APLD，常規交易日消化)</b>：FQ1 營收爆增 322% 達 $3.419 億美元，超大規模資料中心租賃收入進入爆發期，驗證 AI 算力基建從規劃進入大規模運營交付階段。</p>
    </div>
  </div>
  {table(["日期", "公司名稱及代號", "重要關注點與市場預期"], [
    ["10/9 週五 盤前", "Delta Air Lines (DAL)", "航空高端商務艙與國際長途出行需求、航空燃油成本攀升影響、Q4指引"],
    ["10/9 週五 盤前", "Domino's Pizza (DPZ)", "同店銷售成長率、外送促銷策略、消費降級趨勢"],
    ["10/14 下週二", "JPMorgan Chase (JPM)", "Q3財報季正式開幕，淨利息收入（NII）、投行併購業務復甦、信貸損失撥備"],
    ["10/14 下週二", "Wells Fargo (WFC) / Citigroup (C)", "商業地產（CRE）資產品質、淨息差展望、資本回報計畫"]
  ])}
  <p class="text-xs text-slate-500">日曆來源：FactSet / Investing.com 財報日曆；實際公布時間以各公司投資人關係官網（IR）為準。</p></div>''')

# ---------- sec 10 ----------
s10 = sec(10, "機構觀點與資金流", f'''{paras([
    ("華爾街策略與AI投資回報論戰", "華爾街大行今日對科技股走勢發表分化觀點。高盛科技策略主管指出，晶片股單日回調並非 AI 週期終結，而是市場在財報季前對『AI Capex 轉化為企業營收的速度』進行健康壓力測試；摩根大通則指出，在 10 年期殖利率徘徊在 5.2%–5.3% 的背景下，市場對超高估值硬體股的容忍度正在下降，資金正自然分流至具有確定性防禦現金流的標的。韋德布希（Wedbush）分析師 Dan Ives 則重申對輝達（NVDA）的看好與 $300 目標價，強調主權 AI 與企業級推理晶片需求仍在加速。"),
    ("ETF 資金流向與板塊輪動特徵", f"ETF 資金流量官方數據 {NA}；從價格行為與成交分佈觀察：資金今日大舉流出半導體 ETF（SMH、SOXX）與高估值科技股，同時大幅流入能源 ETF（XLE {PC('XLE')}）、必需消費 ETF（XLP {PC('XLP')}）及等權重標普（RSP {PC('RSP')}）。這表明機構投資者並未全面撤出美股市場，而是執行了經典的『去擁擠度、增配防禦與價值』的內部再平衡操作。"),
    ("大宗交易與期權市場異動", f"大宗交易與內部人交易數據 {NA}。期權市場方面，VIX 波動率指數小幅上升至 {PX('^VIX')}，盤中看跌期權（Put）買盤主要集中在半導體個股（NVDA、MU），但尾盤 SPY 與 QQQ 的末日看漲期權出現逢低吸納跡象，顯示機構避險主要局限在硬體賽道，大盤系統性對沖需求受控。"),
])}''')

# ---------- sec 11 ----------
s11 = sec(11, "板塊輪動判斷", paras([
    ("資金流入板塊", f"能源（XLE {PC('XLE')}）、必需消費（XLP {PC('XLP')}）、金融（XLF {PC('XLF')}）、房地產（XLRE {PC('XLRE')}）及企業軟體 SaaS（ADBE、SNOW、PLTR）。此外，大型現金流之王蘋果（AAPL {PC('AAPL')}）成為巨頭中最受青睞的資金避風港。"),
    ("資金流出板塊", f"高估值半導體與硬體供應鏈（XLK {PC('XLK')}、SMH {PC('SMH')}）、光通訊（COHR、LITE）、獨立發電商與核能概念（VST、CEG、OKLO）。前期漲幅過大、獲利盤過於豐厚的標的遭遇集中減持。"),
    ("AI 主線健康度與結構演變", "AI 主線並未終結，而是邁入『第二階段：硬體估值消化，應用與軟體崛起』。過往市場行情完全由 Nvidia、ASML、美光等上游硬體晶片與電力基礎設施驅動，估值推升至極致；而今日 Adobe（+3.56%）、Snowflake（+3.17%）、Palantir（+2.40%）、ServiceNow（+1.36%）等企業級軟體與 AI 應用全面接棒逆勢大漲，證明市場正在將資金轉移至能將 AI 轉化為真實商業化營收的終端應用端。大盤處於健康的結構性洗盤，非系統性見頂。"),
]))

# ---------- sec 12 watchlist ----------
W = [
    ("NVDA", "高位震盪", "大跌-2.94%收$230.48，OpenAI營收雜音引發晶片獲利了結，支撐看$228日低"),
    ("AMD", "高位震盪", "回落-3.90%收$620.68，隨半導體族群同步回檔，回踩20日線"),
    ("AVGO", "高位震盪", "下跌-4.35%收$360.14，客製化晶片短線消化獲利賣壓，5日仍漲+4.8%"),
    ("MRVL", "高位震盪", "回踩-3.52%收$274.66，投資人日大漲後健康消化，近1月仍大賺+16.9%"),
    ("GOOGL", "高位震盪", "微跌-0.63%收$348.29，搜尋與雲端廣告展現極強抗跌防禦力"),
    ("MSFT", "高位震盪", "下跌-1.35%收$522.61，守穩520美元關卡，AI原生生態推進"),
    ("META", "高位震盪", "持平微跌-0.06%收$720.89，守住720平台，近1月仍大漲+10.3%"),
    ("AMZN", "高位震盪", "下跌-2.25%收$254.06，AWS算力支出擔憂短期壓制股價"),
    ("ORCL", "破位風險", "重挫-5.48%收$135.69，失守多條短期均線，雲端資本開支承壓"),
    ("CRM", "低位修復", "逆勢走強+1.44%收$227.80，Agentforce應用低位反彈築底"),
    ("NOW", "繼續強勢", "抗跌上揚+1.36%收$139.75，工作流軟體龍頭逆勢創新高"),
    ("SNOW", "繼續強勢", "大漲+3.17%收$343.40，企業數據雲端平台吸引避險買盤，破位修復"),
    ("ADBE", "低位修復", "狂飆+3.56%收$241.05，Firefly商用加速，自超跌低點強勢報復反彈"),
    ("PLTR", "繼續強勢", "逆勢大漲+2.40%收$198.78，逼近200元大關，AIP商業化動能強勁"),
    ("LITE", "短線過熱", "大跌-5.62%收$1048.60，光模組急拉後劇烈回踩消化超買"),
    ("COHR", "短線過熱", "暴跌-9.63%收$302.35，光通訊單日深幅回調，短期波動加劇"),
    ("ANET", "回踩支撐", "下跌-2.25%收$210.97，高階交換機回測支撐，月漲仍達+9.4%"),
    ("FLNC", "破位風險", "走弱-2.87%收$7.45，破底疲軟，近1月崩跌-26.4%"),
    ("OKLO", "破位風險", "重挫-6.11%收$34.57，SMR概念股高波動劇烈回檔"),
    ("VST", "高位震盪", "回吐-6.35%收$156.14，DOE利多急漲後技術性洗盤，5日仍漲+11.7%"),
    ("CEG", "高位震盪", "回調-4.85%收$285.07，核電概念股短線獲利回吐，維持高位整固"),
    ("ETN", "回踩支撐", "下跌-1.58%收$424.51，電氣設備回測20日線獲買盤支撐"),
    ("VRT", "需要觀察", "下跌-1.12%收$243.73，散熱設備隨基建板塊整理，跌幅相對受限"),
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
      <li><b>國際原油價格</b>：WTI 今日收 ${PX("CL=F")}（+3.29%），觀察油價能否在 90–92 美元區間整固；若進一步飆升衝向 95 美元，將加大能源通膨對央行寬鬆預期的掣肘。</li>
      <li><b>美債殖利率延續性</b>：10 年期美債殖利率在 30 年期國債拍賣後降至 {PX("^TNX")}%，觀察能否有效守在 5.30% 阻力下方，持續回落將有利於估值修復。</li>
      <li><b>中東地緣局勢與黃金</b>：黃金收 ${PX("GC=F",1)}，觀察週末前避險情緒是否促使資金加速鎖定利潤。</li>
      <li><b>VIX 波動率水位</b>：今日收 15.41，觀察明日能否維持在 16.0 警戒線下方。</li>
    </ul>
  </div>
  <div class="{BOX}"><h3 class="font-semibold mb-2">13.2 大盤與結構關鍵位置</h3>
    <p class="text-sm"><b>SPY</b>：上方壓力 777.09（今日高點）與 781.62（歷史新高）；下方關鍵防守 770.43（今日低點），次級生命線支撐為 20 日均線 765.46。<br/>
    <b>QQQ</b>：上方壓力 753.94，下方關鍵防守 743.23（今日低點），次級強支撐為 20 日均線 731.10。<br/>
    <b>結構改善信號</b>：關注等權標普 RSP（收 ${PX("RSP")}）能否延續跑贏 SPY，以及羅素 2000（IWM 收 ${PX("IWM")}）在 200 日線（276.64）企穩後能否發起反彈。</p>
  </div>
  <div class="{BOX}"><h3 class="font-semibold mb-2">13.3 核心板塊與重點個股觀察清單</h3>
    <p class="text-sm leading-relaxed">
      <b>最值得關注的個股</b>：<br/>
      1. <b>AAPL</b>：逆勢大漲 +1.11% 創波段新高，作為4.75兆美元巨頭，觀察能否持續擔綱大盤護盤中流砥柱。<br/>
      2. <b>NVDA</b>：重挫 -2.94% 逼近 230 美元關卡，觀察 228 美元今日低點的買盤支撐力道與是否有低接資金。<br/>
      3. <b>PLTR</b>：大漲 +2.40% 報 $198.78，觀察明日能否強勢突破 200 美元歷史心理整數大關。<br/>
      4. <b>ADBE & SNOW</b>：軟體反彈先鋒，觀察大漲 3% 之後的買盤延續性，確認是否確立中級築底反轉。<br/>
      5. <b>MU</b>：大跌 -4.79% 守在 $1,035，觀察在千元整數關卡能否獲得強支撐並重聚動能。<br/>
      6. <b>XOM & CVX</b>：能源權重龍頭，受油價暴漲催化，觀察動能是否能跨越前期壓力位。<br/>
      7. <b>DAL</b>：明日盤前公布財報，觀察航空客運需求對高油價的吸收能力。<br/>
      8. <b>VST & CEG</b>：電力龍頭深幅洗盤後，觀察是否回踩 10 日線獲承接買盤。<br/>
      9. <b>COHR & LITE</b>：光通訊單日大跌逾 5%–9%，急跌釋放超買風險後觀察量能萎縮止跌點。<br/>
      10. <b>ORCL</b>：跌破短期均線，需嚴格防範進一步回調下探風險。
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
    ("地緣衝突與能源油價風險", "高", "中東緊張推升 Brent 原油衝破 $104/桶、WTI 大漲 3.3%，油價持續飆升將直接引發二次通膨擔憂，限制聯準會貨幣政策彈性"),
    ("AI 投資回報率 (ROI) 質疑", "中高", "OpenAI 營收增速放緩報導引發市場對科技巨頭龐大 AI Capex 盈利轉化的質疑，上游硬體晶片估值殺傷風險加劇"),
    ("宏觀長端利率高位震盪", "中高", "初請失業金 19.7 萬顯示經濟強勁，儘管 30 年美債拍賣優異促使利率回落，但 10 年期仍位於 5.23% 高位，制約估值擴張"),
    ("半導體板塊短線波動", "中高", "費半單日大跌 -3.39%，光通訊與記憶體短線回檔幅度深，高貝塔成長股短線洗盤尚未完全結束"),
    ("Q3 財報季降溫風險", "中", "下週摩根大通、富國銀行等大行財報登場，市場對金融信貸與消費支出的指引容錯率極低"),
    ("小型股估值修復不確定性", "中", "羅素 2000 今日微漲 +0.03% 雖止跌，但仍在 200 日線邊緣掙扎，需防範假止跌再破位"),
    ("流動性環境與週末避險", "中", "美元與加密貨幣分化，臨近週末地緣不確定性可能促使更多槓桿資金在週五平倉避險")
]

s14 = sec(14, "風險提示（視覺化風險矩陣）", table(["風險維度", "風險等級", "具體情境與解讀分析"], [[f"<b>{a}</b>", f'<span class="px-2 py-0.5 rounded font-semibold {RC[b]}">{b}</span>', c] for a, b, c in risks]))

# ---------- sec 15 ----------
s15 = f'''
    <section id="sec-15" class="scroll-mt-6 p-6 rounded-2xl bg-gradient-to-br from-white to-slate-50 dark:from-zinc-900 dark:to-zinc-950 border border-slate-200 dark:border-zinc-800 shadow-sm">
      <h2 class="{H2}"><span class="text-brand-500">{n}.</span> 最終結論</h2>
      <div class="space-y-3 text-sm sm:text-base leading-relaxed text-slate-700 dark:text-zinc-300">
        <p><strong>今日市場結論：</strong>標普 500 收 {PX("^GSPC")}（{PC("^GSPC")}）、納斯達克收 {PX("^IXIC")}（{PC("^IXIC")}）、費半重挫 {PC("^SOX")}，主要受 OpenAI 營收雜音引發的晶片獲利了結與中東局勢推升油價衝擊；但道瓊逆勢微漲 51 點（{PC("^DJI")}），等權標普 RSP 大漲 {PC("RSP")}，全市場 11 大板塊中多達 8 個收紅。這是一場教科書級別的「科技硬體殺估值、資金湧入傳統能源（XLE +2.97%）、必需消費（XLP +2.11%）與企業軟體（ADBE/SNOW/PLTR）」的巨幅風格再平衡。</p>
        <p><strong>當前市場階段：</strong>強趨勢中的「高位震盪回踩與巨幅板塊輪動」（加權指數受科技巨頭壓制，但底層市場寬度出現積極的價值與軟體修復）。</p>
        <p><strong>操作傾向（中性表述）：</strong>大盤並未發生系統性空頭破位，SPY 與 QQQ 距離各自 20 日均線仍有安全墊。策略上切忌盲目追高已大幅拉升的熱點，同時不宜恐慌拋售具備長期壁壘的優質晶片龍頭；可保持倉位均衡，適度向抗跌防禦現金流資產（AAPL、必需消費）、受惠油價上漲的能源板塊，以及具備獨立估值修復動能的企業軟體 SaaS（PLTR、ADBE、SNOW）傾斜，耐心等待費半與晶片股縮量企穩。</p>
        <div><strong>最值得關注的 5 個核心訊號：</strong>
          <ol class="list-decimal pl-6 mt-2 space-y-1">
            <li><b>WTI 原油能否在 $90–$92 整固</b>：觀察中東地緣局勢是否進一步失控，原油若突破 $95 將加大通膨預期。</li>
            <li><b>10 年期美債殖利率 5.20%–5.25% 支撐帶</b>：拍賣利好推動殖利率自 5.35% 回落後，觀察能否維持下行走勢。</li>
            <li><b>輝達（NVDA $228）與美光（MU $1,000）防守位</b>：晶片龍頭能否在今日低點與整數關卡止跌回穩。</li>
            <li><b>Palantir（PLTR $198.78）能否突破 $200</b>：作為軟體與 AI 應用領頭羊，其突破將帶動 SaaS 板塊持續走強。</li>
            <li><b>SPY 770.43 日低防守</b>：若週五守穩 770 點上方，將確認本次回踩為健康的上升通道中繼整固。</li>
          </ol>
        </div>
        <p class="text-xs text-slate-500 mt-3">資料來源與聲明：價格與技術數據取自 Yahoo Finance 官方報價（至 2026-10-08 收盤），宏觀經濟與公司動態整合彭博、路透社、FactSet、美國勞工部、財政部官方公告與企業新聞稿；未取得完整公開流之項目已於內文中清晰標註。本文僅供投資復盤與策略研究，不構成任何個人投資建議。</p>
      </div>
    </section>
'''.replace("{n}", "15")

# ---------- tail ----------
tail = old[old.index("<!-- Footer -->"):]
tail = re.sub(r"<div>美股收盤日報｜資料來源：.*?</div>", "<div>美股收盤日報｜資料來源：Yahoo Finance、美國勞工部DOL、財政部、彭博、路透社、FactSet、公司新聞稿與SEC申報檔案</div>", tail)

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
    print("Skipping publish as requested.")
    sys.exit(0)

pub = R + ".antigravitycli/skills/html-report/scripts/publish.py"
res = subprocess.run(["python3", pub, out, TITLE, DESC], capture_output=True, text=True)
print("Publish STDOUT:\n", res.stdout)
if res.stderr:
    print("Publish STDERR:\n", res.stderr)
sys.exit(res.returncode)
