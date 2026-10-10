import json, re, subprocess, sys

R = "/Users/wisdom/html-report-skill/"
D = "2026-10-09"
q = json.load(open(R + f"scratch/quotes_{D}.json"))
t = json.load(open(R + f"scratch/tech_{D}.json"))
old = open(R + "reports/2026-10-08-us-stock-closing-daily-report.html", encoding="utf-8").read()

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
DESC = ("週五（2026年10月9日）美股全面反攻收高：標普500 +0.54%報7,807.12點（盤中7,844.52刷52週新高）、納指 +0.57%報27,349.51點、道瓊大漲 +0.70%（+359點）報51,590.64點、費半企穩 +0.67%；"
        "川普承諾期中選舉前不对伊朗動手帶動油價降溫（WTI回落至$90.97、Brent跌至$103.50），地緣通膨威脅短期緩解；"
        "大科技強勁回歸（AMZN +3.03%、MSFT +2.25%、TSLA +2.05%），軟體主線勢不可擋，Palantir狂飆 +5.17%衝破$200關卡收$209.05創歷史新天價！Snowflake飆漲 +7.42%、甲骨文反彈 +4.33%；"
        "密西根消費者信心降至46.3創5個月低，長端殖利率守在5.24%平穩，市場寬度大舉修復（標普9大板塊收紅），全週強勢收漲迎接Q3財報季。")

head = old[: old.index("<!-- Header Block -->")]
head = re.sub(r"<title>.*?</title>", f"<title>{TITLE}｜標普刷52週新高、地緣油價降溫、大科技反攻、Palantir破天價 ({D})</title>", head, flags=re.S)
head = re.sub(r'<meta name="description" content=".*?">', f'<meta name="description" content="{DESC}">', head, flags=re.S)
head = re.sub(r'<meta property="og:title" content=".*?">', f'<meta property="og:title" content="{TITLE}">', head)
head = re.sub(r'<meta property="og:description" content=".*?">', '<meta property="og:description" content="美股全面反攻，標普刷52週新高，地緣油價回落，大科技與軟體共振走強，Palantir突破200美元創歷史天價。">', head)
head = head.replace("2026-10-08", D)

header = f'''<!-- Header Block -->
    <header class="border-b border-slate-200 dark:border-zinc-800 pb-6">
      <div class="flex flex-wrap items-center justify-between gap-3 mb-2">
        <span class="inline-flex items-center gap-1.5 px-3 py-1 rounded-full text-xs font-semibold bg-emerald-100 text-emerald-800 dark:bg-emerald-950 dark:text-emerald-300">
          <span class="w-2 h-2 rounded-full bg-emerald-500 animate-pulse"></span> 標普創52週新高・地緣油價降溫・大科技反撲・Palantir破歷史天價
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
        <p>{S}【大盤走勢】</strong> 週五美股迎來強勁的多頭修復，三大指數全線收高並為本週畫上強勢句點。標普500指數上漲 <strong>{PC("^GSPC")}</strong>（+{q['^GSPC']['change']:.2f}點）收 <strong>{PX("^GSPC")}</strong>，盤中最高衝至 <strong>7,844.52點刷新52週新高</strong>，全週累計上揚 +1.09%；道瓊工業指數在金融與大型價值龍頭助推下大漲 <strong>{PC("^DJI")}</strong>（+{q['^DJI']['change']:.2f}點）收 <strong>{PX("^DJI")}</strong>；納斯達克綜合指數上揚 <strong>{PC("^IXIC")}</strong>（+{q['^IXIC']['change']:.2f}點）收 <strong>{PX("^IXIC")}</strong>；費城半導體指數止跌反彈 <strong>{PC("^SOX")}</strong> 收 {PX("^SOX")}；羅素2000小型股上漲 <strong>{PC("^RUT")}</strong> 收 {PX("^RUT")}，穩守200日均線之上。</p>
        <p>{S}【驅動因素】</strong> 昨夜三大核心驅動共振推動多頭：第一是地緣政治緊張顯著舒緩，美國總統川普表態在11月期中選舉前不會對伊朗發動軍事打擊，波斯灣斷供恐慌減退，國際油價快速回吐戰爭溢價（WTI收降至${PX("CL=F")}、Brent降至${PX("BZ=F")}），化解了市場對二次能源通膨的短期擔憂；第二是大型科技巨頭強勁反攻，亞馬遜（AMZN {PC("AMZN")}）、微軟（MSFT {PC("MSFT")}）、特斯拉（TSLA {PC("TSLA")}）領銜爆發，市場對 OpenAI 營收增速的短線疑慮迅速消化，資金重新聚焦科技巨頭在 Q3 財報季的強勁獲利基本面；第三是宏觀數據提供估值緩衝，密西根大學 10 月消費者信心初值跌至 46.3（創5個月新低），反映物價偏高抑制作耐久財消費意願，壓制了美債殖利率進一步飆升空間，10年期美債殖利率收在 {PX("^TNX")}% 持穩，為風險資產創造良好修復環境。</p>
        <p>{S}【資金偏好】</strong> 市場風險偏好（Risk-On）顯著回升：CBOE 恐慌指數 VIX 回落 <strong>{PC("^VIX")}</strong> 收在 <strong>{PX("^VIX")}</strong>（全週下跌 0.68 點），避險情緒大幅緩解；現貨黃金在美元微幅走弱（UUP {PC("UUP")}）與中長期儲備需求支撐下反彈 <strong>{PC("GC=F")}</strong>（收 ${PX("GC=F",1)}/oz）；加密貨幣流動性充沛，比特幣反彈 <strong>{PC("BTC-USD")}</strong> 收 ${PX("BTC-USD",0)}，以太幣上漲 <strong>{PC("ETH-USD")}</strong> 收 ${PX("ETH-USD",0)}。</p>
        <p>{S}【市場寬度】</strong> 寬度大幅改善，個股普漲特徵明顯：標普 500 十一個板塊中高達 <strong>9 個板塊收紅</strong>；非必需消費（XLY {PC("XLY")}）與金融（XLF {PC("XLF")}）雙雙大漲逾 1% 領跑全場；等權重標普 <strong>RSP 上漲 {PC("RSP")}</strong>，顯示市場並非僅靠單一股票拉抬，而是呈現加權指數與個股共振上行的良性格局。</p>
        <p>{S}【核心主線】</strong> 軟體與 AI 應用持續主導全場，晶片硬體與光通訊核能企穩反彈：最耀眼焦點為 <strong>Palantir（PLTR 狂飆 {PC("PLTR")} 突破 $200 歷史大關，收在 ${PX("PLTR")} 刷歷史新天價！進入全面價格發現階段）</strong>；Snowflake（SNOW 暴漲 <strong>{PC("SNOW")}</strong> 收 ${PX("SNOW")}）；甲骨文（ORCL 強彈 <strong>{PC("ORCL")}</strong> 逢低買盤積極進場）；光模組與電力設備全面回暖（LITE {PC("LITE")}、COHR {PC("COHR")}、CEG {PC("CEG")}）；晶片巨頭輝達（NVDA $229.74）與美光（MU $1,024.06）守穩日低與千元關鍵支撐。</p>
        <div class="mt-4 p-4 rounded-xl bg-emerald-50 dark:bg-zinc-800/60 border border-emerald-200 dark:border-emerald-900/40 text-emerald-900 dark:text-emerald-200 font-medium">
          💡 <strong>今日市場狀態判斷：</strong>「指數全面反撲、標普刷52週新高，地緣油價降溫釋放估值壓力；大科技重聚動能，軟體與核電再度爆發，市場健康迎接下週Q3財報季。」
        </div>
      </div>
    </section>
'''

# ---------- sec 1 ----------
def card(name, key, px, sub):
    return f'<div class="{CARD}"><div class="text-xs text-slate-500 dark:text-zinc-400 font-medium">{name}</div><div class="text-xl font-extrabold font-mono mt-1">{px}</div><div class="text-xs mt-1 flex items-center justify-between"><span class="{C(P(key), key=="^VIX")}">{PC(key)}</span><span class="text-slate-400 font-mono">{sub}</span></div></div>'

cards = "".join([
    card("S&P 500 (標普500)", "^GSPC", PX("^GSPC"), f"SPY ${PX('SPY')}"),
    card("Nasdaq Composite", "^IXIC", PX("^IXIC"), "科技大股引領反彈"),
    card("Dow Jones (道瓊)", "^DJI", PX("^DJI"), f"{q['^DJI']['change']:+.2f} 點"),
    card("Nasdaq 100", "^NDX", PX("^NDX"), f"QQQ ${PX('QQQ')}"),
    card("Russell 2000", "^RUT", PX("^RUT"), f"IWM ${PX('IWM')}"),
    card("SOX (費城半導體)", "^SOX", PX("^SOX"), f"SMH ${PX('SMH')}"),
    card("Software (IGV)", "IGV", PX("IGV"), "軟體板塊強勁延續"),
    card("VIX", "^VIX", PX("^VIX"), "波動率顯著回落"),
])

idx_rows = []
def irow(name, etf, key, state):
    idx_rows.append([f'<span class="font-semibold font-sans">{name}</span>', etf, f'<b>{PX(key)}</b>', f'<span class="{C(P(key), key=="^VIX")}">{PC(key)}</span>', RNG(key), f'<span class="font-sans">{state}</span>'])
irow("S&P 500", "SPY", "^GSPC", "收漲+0.54%報7,807.12，盤中7,844.52刷52週新高，守穩20日線，週漲+1.09%")
irow("Nasdaq Composite", "—", "^IXIC", "收27,349.51點(+0.57%)，大科技AMZN與MSFT領軍，全週累漲+0.58%")
irow("Nasdaq 100", "QQQ", "^NDX", "QQQ 收751.27(+0.49%)，重回750關卡上方，RSI回升至76.8維持強勢多頭")
irow("Dow Jones", "DIA", "^DJI", "大漲359.00點(+0.70%)收51,590.64，金融與非必需消費雙輪驅動，週漲+0.81%")
irow("Russell 2000", "IWM", "^RUT", "上揚+0.37%收2,804.46點，連續兩日企穩於200日均線(2,788)上方")
irow("SOX 半導體", "SOXX / SMH", "^SOX", "企穩回升+0.67%收12,708.20，SMH(+0.67%)，晶片硬體暫止跌勢")
irow("CBOE VIX", "^VIX", "^VIX", "降至14.84(-3.70%)，全週跌0.68點，避險溢價大幅消除，市場情緒重返偏多")
s1 = sec(1, "大盤表現總覽", f'''
      <div class="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-4 gap-4 mb-6">{cards}</div>
      <div class="{BOX}">
        <h3 class="text-sm font-semibold text-slate-700 dark:text-zinc-300 mb-3 flex items-center justify-between"><span>主要指數與核心資產當日漲跌幅對比 (Chart.js)</span><span class="text-xs font-normal text-slate-500">{D} 基準</span></h3>
        <div class="relative h-64 sm:h-72 w-full"><canvas id="overviewChart"></canvas></div>
      </div>
      <div class="mt-6">{table(["指數名稱", "代表ETF", "收盤點位", "當日漲跌幅", "日內高/低", "技術狀態"], idx_rows, mono=True)}</div>
      <p class="mt-3 text-sm text-slate-600 dark:text-zinc-400">大盤動態：標普500指數盤中刷新52週新高（7,844.52點），全週上漲 +1.09%；道瓊工業指數連兩日收紅（週漲+0.81%）；小盤股（羅素2000）在200日線成功築底企穩；恐慌指數VIX跌破15點關卡至14.84，全市場流動性環境顯著轉向積極。</p>
''')

# ---------- sec 2 ----------
mer = f'''graph LR
  subgraph PreMarket["盤前"]
    A["密西根消費者信心降至46.3<br/>川普承諾期中前不对伊朗動手<br/>原油回跌通膨憂慮消退<br/>達美航空DAL財報因航油承壓"]
  end
  subgraph Open["開盤"]
    B["三大指數全面高開<br/>大科技AMZN/MSFT/TSLA領漲<br/>PLTR迅速衝上$200整數關卡<br/>軟體股延續火爆行情"]
  end
  subgraph MidDay["午盤 13:00-14:00"]
    C["10年期美債殖利率持平5.24%<br/>金融板塊(XLF)在財報前獲買盤加碼<br/>標普攻破7,840點刷52週新高<br/>晶片股低接資金進場"]
  end
  subgraph Close["尾盤與盤後"]
    D["多頭守穩漲幅高位結算<br/>標普收 {PX('^GSPC')} (+0.54%)<br/>道瓊大漲 +359 點<br/>PLTR收$209.05創歷史天價<br/>全週完美收官迎財報季"]
  end
  PreMarket --> Open --> MidDay --> Close'''
s2 = sec(2, "盤中走勢復盤（時間線 Timeline）", f'''
      <div class="{BOX} overflow-x-auto"><div class="mermaid">
{mer}
      </div></div>
      <div class="mt-4 {BOX}">{paras([
    ("盤前", "早盤密西根大學公布 10 月消費者信心初值跌至 46.3（創5個月新低），反映高物價對終端耐用品消費意願的侵蝕；與此同時，地緣政治迎來重大降溫信號，美國總統川普表態在 11 月期中選舉前不會對伊朗發動軍事打擊，原油期貨應聲大跌，WTI 原油回調至 $90.97，Brent 原油回跌至 $103.50，極大地緩解了輸入型二次通膨焦慮。盤前達美航空（DAL）公布 Q3 財報，營收雖創歷史新高但受航油成本暴漲 62% 衝擊導致 EPS 不及預期並下調全年指引，印證了油價波動對企業獲利的直接影響。"),
    ("開盤後", f"美股三大指數跳空開高：受油價回落與財報季預期提振，大科技權重股全面走強，亞馬遜（AMZN +3.03%）、微軟（MSFT +2.25%）與特斯拉（TSLA +2.05%）迅速拉升；企業軟體板塊延續前一日的極強動能，昨日直逼 $200 的 Palantir（PLTR）開盤即放量衝破 $200 歷史大關，觸發強烈空頭回補與追多買盤；前一日因 OpenAI 營收放緩報導而重跌的甲骨文（ORCL +4.33%）與 Snowflake（SNOW +7.42%）湧現報復性大抄底買盤。"),
    ("午盤方向選擇", f"美東時間 13:00，美債殖利率在 5.24% 水平維持狹幅震盪，並未隨指數上漲而攀升，為股票市場提供了優異的估值環境。金融板塊（XLF +1.10%）在下週二即將登場的華爾街大行（JPMorgan、Wells Fargo、Citi）財報季前夕，獲得機構資金的大幅提前配置；大盤買氣全面擴散，標普 500 指數於午盤衝破 7,840 點關卡，觸及 7,844.52 點，創下歷史級別的 52 週新高。"),
    ("尾盤拉升與盤後", f"臨近尾盤，各板塊多頭秩序井然，道瓊工業指數維持高位整固收在全日高檔 {PX('^DJI')}（+0.70%）；標普 500 收報 {PX('^GSPC')}（+0.54%）；納指收 {PX('^IXIC')}（+0.57%）。全週五個交易日標普累計上揚 +1.09%，道瓊週漲 +0.81%。核心驅動總結：川普地緣表態帶動油價降溫＋大科技獲利預期重聚＋軟體主線進入爆發期，推動美股在財報季前夕確立中短期多頭強勢格局。"),
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
tab_y = f'''<div id="panel-yields" class="tab-panel space-y-4"><h4 class="font-bold text-slate-900 dark:text-white text-base">美債殖利率於高位平穩整固，10年期基準殖利率持平收在 5.24%</h4>
  <div class="grid grid-cols-2 sm:grid-cols-4 gap-3 font-mono">{yield_cards}</div>
  <p>美債殖利率收在穩定水平：10年期基準殖利率收在 {PX("^TNX")}%（微變 +1bp，日內波動區間 5.22%–5.26%）；30年期收 {PX("^TYX")}%（+2bp）；5年期收 {PX("^FVX")}%（+1bp）；13週國庫券收 {PX("^IRX")}%（-1bp）。市場含義：儘管密西根通膨預期微升，但川普表態推動油價回跌，以及密西根消費者信心降至五個月低點，有效制約了債市空頭，美債殖利率曲線在 5.24% 附近築起堅固平台，為成長股估值提供了罕見的低波動平穩窗口。</p></div>'''

tab_f = '''<div id="panel-fed" class="tab-panel space-y-4"><h4 class="font-bold text-slate-900 dark:text-white text-base">Fed 政策定價：密西根通膨預期微升，市場全面轉向下週 9 月 CPI 報告</h4>
  <div class="grid grid-cols-2 sm:grid-cols-3 gap-3 font-mono">''' + stat("密西根消費者信心", "46.3（降）", "創 5 個月新低，耐用品購買意願驟降") + stat("1年期通膨預期", "4.7%（微升）", "自前月 4.6% 小幅上修，物價痛感仍在") + stat("5年期通膨預期", "3.5%（微升）", "長期通膨預期黏性支撐央行鷹派定價") + '''</div>
  <p>密西根大學公布的初步數據顯示，短期 1 年通膨預期自 4.6% 微升至 4.7%，5 年長期通膨預期自 3.4% 微升至 3.5%。結合本週強勁的非農與初請失業金（19.7萬）數據，聯邦基金期貨市場依然維持「Higher for Longer」的基本假設，排除年內大幅降息可能性。然而，油價自高位回吐為即將於下週二（10/13）公布的 9 月 CPI 報告提供了一定心理緩衝，市場目前定價央行在 11 月 FOMC 會議上將保持耐心觀望。</p></div>'''

tab_c = f'''<div id="panel-commodities" class="tab-panel space-y-4"><h4 class="font-bold text-slate-900 dark:text-white text-base">川普承諾降溫中東戰爭溢價、原油回跌、黃金走穩、加密資產大漲</h4>
  <div class="grid grid-cols-2 sm:grid-cols-3 gap-3 font-mono">
  {stat("美元（UUP代理）", "$"+PX("UUP"), CT("UUP"))}{stat("黃金期貨", "$"+PX("GC=F",1)+"/oz", CT("GC=F"))}{stat("WTI 原油", "$"+PX("CL=F"), CT("CL=F"))}
  {stat("Brent 原油", "$"+PX("BZ=F"), CT("BZ=F"))}{stat("比特幣", "$"+PX("BTC-USD",0), CT("BTC-USD"))}{stat("以太幣", "$"+PX("ETH-USD",0), CT("ETH-USD"))}</div>
  <p>大宗商品與另類資產動態：中東地緣恐慌降溫，WTI 原油自週四高位回吐 {PC("CL=F")} 收在 ${PX("CL=F")}/桶，Brent 原油回跌 {PC("BZ=F")} 收在 ${PX("BZ=F")}/桶；現貨與期貨黃金受美元走弱與地緣避險底倉需求支撐，反彈 {PC("GC=F")} 收在 ${PX("GC=F",1)}/盎司；美元 ETF UUP 微幅整理 {PC("UUP")} 收 ${PX("UUP")}；加密貨幣市場流動性充沛，比特幣大漲 {PC("BTC-USD")} 重返 ${PX("BTC-USD",0)}，以太幣上揚 {PC("ETH-USD")} 收在 ${PX("ETH-USD",0)}。</p></div>'''

tab_d = '''<div id="panel-data" class="tab-panel space-y-4"><h4 class="font-bold text-slate-900 dark:text-white text-base">密西根大學 10 月消費者信心降至 46.3，台灣 9 月出口連創歷史新高</h4>
  <div class="overflow-x-auto"><table class="w-full text-sm text-left"><thead class="bg-slate-50 dark:bg-zinc-800/60"><tr><th class="p-3">數據名稱</th><th class="p-3">實際值</th><th class="p-3">預期值</th><th class="p-3">前值</th><th class="p-3">市場解讀</th></tr></thead><tbody class="divide-y divide-slate-100 dark:divide-zinc-800">
  <tr><td class="p-3 font-semibold">密西根大學 10 月消費者信心初值</td><td class="p-3 font-mono">46.3</td><td class="p-3 font-mono">47.8</td><td class="p-3 font-mono">48.1</td><td class="p-3">創下 5 個月以來新低，家庭對高物價與借貸成本高度敏感，耐久財購買條件驟降，實體消費動能趨向保守。</td></tr>
  <tr><td class="p-3 font-semibold">密西根大學 1 年期通膨預期</td><td class="p-3 font-mono">4.7%</td><td class="p-3 font-mono">4.6%</td><td class="p-3 font-mono">4.6%</td><td class="p-3">受近期汽油價格波動影響，消費者短期通膨預期微幅攀升。</td></tr>
  <tr><td class="p-3 font-semibold">密西根大學 5 年期通膨預期</td><td class="p-3 font-mono">3.5%</td><td class="p-3 font-mono">3.4%</td><td class="p-3 font-mono">3.4%</td><td class="p-3">長期通膨預期微升，央行降息空間持續受到約束。</td></tr>
  <tr><td class="p-3 font-semibold">台灣 9 月出口統計（對比驗證）</td><td class="p-3 font-mono">創單月歷史新高</td><td class="p-3 font-mono">擴張預期</td><td class="p-3 font-mono">連續創高</td><td class="p-3">連續第 2 個月改寫歷史單月新高紀錄，受全球 AI 伺服器與半導體供應鏈出貨強勁拉動，驗證硬體基本面實質需求旺盛。</td></tr>
  </tbody></table></div>
  <p class="text-xs text-slate-500">下週重要日程：10/13（週二）美國 9 月 CPI 報告、10/14（週三）華爾街大行摩根大通、富國銀行等正式公布 Q3 財報。</p></div>'''

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
    ("非必需消費", "XLY", "TSLA (+2.05%) 與 AMZN (+3.03%) 暴力反彈領跑大盤 (+1.40%)"),
    ("金融", "XLF", "下週大行財報季前夕機構資金積極提前卡位布局 (+1.10%)"),
    ("通訊服務", "XLC", "GOOGL (+0.95%) 走強與數位廣告防禦買盤支持 (+0.69%)"),
    ("工業", "XLI", "重型機械、電氣與航太軍工延續穩健走勢 (+0.62%)"),
    ("房地產", "XLRE", "10年期美債殖利率平穩於 5.24%，REITs 板塊溫和上漲 (+0.56%)"),
    ("科技", "XLK", "微軟大漲 +2.25% 與半導體企穩，對沖了蘋果微幅整理 (+0.54%)"),
    ("公用事業", "XLU", "電力發電商重拾升勢，傳統公用事業收漲 (+0.54%)"),
    ("原物料", "XLB", "黃金反彈與工業金屬持穩支撐化學材料股 (+0.53%)"),
    ("醫療保健", "XLV", "防禦性大型製藥與醫療器材穩步收紅 (+0.49%)"),
    ("能源", "XLE", "中東緊張情緒暫緩油價微跌，但油氣股守在紅盤 (+0.20%)"),
    ("必需消費", "XLP", "昨日避險大漲後今日資金分流至成長股，維持微漲整固 (+0.18%)"),
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
      <p class="mt-3 text-sm text-slate-600 dark:text-zinc-400">最強板塊：非必需消費 XLY（{PC("XLY")}）、金融 XLF（{PC("XLF")}）、通訊服務 XLC（{PC("XLC")}）；最弱板塊：必需消費 XLP（{PC("XLP")}）、能源 XLE（{PC("XLE")}）。風格特徵：呈現教科書式的『成長與金融雙輪驅動、避險資金回流成長股』；S&P 500 十一個板塊中高達 9 個收紅，等權標普 RSP 上揚 +0.43%，驗證了市場經過週四劇烈輪動洗盤後，內部健康度顯著增強，全市場風險偏好再度點燃。</p>''')

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
    "SMH": "晶片硬體企穩反彈 +0.67%，守穩20日均線",
    "SOXX": "半導體普遍止跌，單日 +0.61%",
    "IGV": "軟體延續火爆行情，單日勁揚 +1.70%",
    "MU": "千元整數關卡買盤強勁，守在 $1,024",
    "CRWD": "資安龍頭穩步回升 (+0.95%)，月漲 +25.8%",
    "PANW": "資安龍頭小幅修復 (+0.68%)，高位整固",
    "NOW": "企業工作流軟體持平整固，需求高度確定",
    "PLTR": "狂飆 +5.17% 衝破 $200 創 $209.05 歷史天價！",
    "LITE": "光模組暴力反彈 +5.22%，重回千元上方",
    "COHR": "光通訊龍頭急跌後強彈 +3.40%，重拾升勢",
    "VST": "電力發電商企穩 (+0.46%)，5日仍大賺 +9.5%",
    "GEV": "電力設備再創波段高，攻破千元至 $1,004.73",
    "FLNC": "儲能微幅止跌 (+0.40%)，超跌整理",
    "IWO": "小盤成長反彈 (+0.42%)，築底企穩",
    "IWN": "小盤價值續升 (+0.41%)，低位連續修復",
    "RSP": "等權標普上漲 +0.43%，個股普漲格局健康",
    "QQQ": "大盤成長收漲 +0.49%，大科技重拾升勢"
}
trows = [[n, f"<b>{e}</b>", f'<span class="{C(P(k))}">{PC(k)}</span>', f'{q[k]["5d"]:+.2f}%', f'{q[k]["1m"]:+.2f}%', note.get(e, "")] for n, e, k in themes]
s5 = sec(5, "主題與風格表現", table(["主題", "代表", "當日", "近5日", "近1月", "特徵"], trows, tid="themeTable", sortable={2, 3, 4}) + '<p class="mt-3 text-sm text-slate-600 dark:text-zinc-400">主題解讀：市場焦點呈現『軟體主線瘋狂領跑、硬體超跌強烈回血、光通訊與核能王者歸來』。Palantir（PLTR +5.17%）與 Snowflake（SNOW +7.42%）帶領整個 IGV 軟體板塊暴漲 +1.70%；昨日遭遇深幅回調的光通訊雙雄（LITE +5.22%、COHR +3.40%）與核能發電龍頭（CEG +4.58%）展現了強大的逢低承接買盤；大型成長科技股與等權標普同步收高，多頭結構擴展至多個關鍵子賽道。</p>')

# ---------- sec 6 breadth ----------
s6 = sec(6, "市場寬度與參與度", f'''
      <div class="space-y-4">
      <div class="{BOX}"><h3 class="font-semibold mb-2">6.1 均線參與度</h3>
      <p class="text-sm text-slate-700 dark:text-zinc-300">成分股高於主要均線比例官方明細 {NA}；主要代表 ETF 相對均線位置如下（依至 10-09 收盤日線計算）：</p>
      {table(["ETF", "SPY", "QQQ", "IWM"], [["20日均線", f'{t["SPY"]["sma20"]:.2f}', f'{t["QQQ"]["sma20"]:.2f}', f'{t["IWM"]["sma20"]:.2f}'], ["50日均線", f'{t["SPY"]["sma50"]:.2f}', f'{t["QQQ"]["sma50"]:.2f}', f'{t["IWM"]["sma50"]:.2f}'], ["200日均線", f'{t["SPY"]["sma200"]:.2f}', f'{t["QQQ"]["sma200"]:.2f}', f'{t["IWM"]["sma200"]:.2f}'], ["10-09收盤", PX("SPY"), PX("QQQ"), PX("IWM")]])}
      <p class="mt-2 text-sm text-slate-600 dark:text-zinc-400">趨勢研判：SPY（778.53）與 QQQ（751.27）強勢站穩於 20 日均線（SPY 766.82 / QQQ 733.25）之上，中長期上升通道完美維持；IWM（278.60）連續兩個交易日穩穩守在 200 日生命線（276.72）上方，小型股的空頭下殺動能已實質耗盡。</p></div>
      <div class="{BOX}"><h3 class="font-semibold mb-2">6.2 漲跌家數、新高新低</h3><p class="text-sm">交易所上漲/下跌家數明細 {NA}。寬度代理觀察：標普 500 十一個板塊中高達 9 個收漲，僅 2 個微幅整理；標普 500 指數盤中觸及 7,844.52 點創下 52 週新高；等權重標普（RSP +0.43%）與市值加權標普（SPY +0.59%）同步上揚，顯示市場普漲參與度極佳，大盤擺脫了先前的結構性背離。</p></div>
      <div class="{BOX}"><h3 class="font-semibold mb-2">6.3 其他內部指標</h3><p class="text-sm">騰落線、McClellan Oscillator、Put/Call Ratio {NA}。VIX 恐慌指數下跌 -3.70% 收在 {PX("^VIX")}，全週自 15.52 下滑至 14.84，完全脫離警戒水位；成交量方面，在週五選擇權到期與週末前夕呈現平穩交投，機構買盤在大盤刷出 52 週新高時並無恐慌出貨跡象。</p></div>
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
    trs.append(trow(sym, f"支撐 {q[sym]['low']:.2f}（日低）/ {x['sma20']:.1f}（20日）；壓力 {max(q[sym]['high'], x['hi52']):.2f}（高點）"))

s7 = sec(7, "技術面分析", table(["ETF", "收盤", "當日", "20日均線", "50日均線", "200日均線", "RSI(14)", "MACD", "支撐／壓力"], trs, mono=True) + f'''
      <p class="mt-3 text-sm text-slate-600 dark:text-zinc-400">技術判讀：SPY 重新站上 778 點，RSI 回升至 67.4，位於健康的多頭運行區間；QQQ（RSI 76.8）收復 750 點心理關卡，MACD 多頭柱狀持續擴張；IWM（RSI 36.5）在 200 日均線（276.72）展現強烈雙底支撐；IGV（RSI 67.8）突破多條短期均線向上發散。下週多頭確認信號：SPY 能否放量突破 782.10 今日高點並挑戰 785 點整數大關；QQQ 能否上攻 755–760 點歷史高位平台。關鍵風險防守位：SPY 774.20（今日低點）與 766.82（20日均線），QQQ 748.10（今日低點）。</p>''')

# ---------- sec 8 ----------
def line(sym, txt=""):
    return f'<tr><td class="p-2 font-semibold">{sym}</td><td class="p-2 font-mono">${PX(sym)}</td><td class="p-2 {C(P(sym))}">{PC(sym)}</td><td class="p-2 text-xs">近5日 {q[sym].get("5d", 0):+.1f}% / 近1月 {q[sym].get("1m", 0):+.1f}%</td><td class="p-2 text-xs">{txt}</td></tr>'

def tbl(rows):
    return f'<div class="overflow-x-auto"><table class="w-full text-sm text-left"><tbody class="divide-y divide-slate-100 dark:divide-zinc-800">{"".join(rows)}</tbody></table></div>'

m7 = tbl([
    line("AMZN", "大漲 +3.03% 收$261.77！AWS 雲端算力需求預期回溫，電商旺季備貨催化，領跑七巨頭"),
    line("MSFT", "強勁大漲 +2.25% 收$534.38，Copilot 企業付費滲透加速，守穩 530 美元關卡"),
    line("TSLA", "勁揚 +2.05% 收$382.70，收復 380 美元大關，Robotaxi 與儲能交付預期持續發酵"),
    line("GOOGL", "穩健上揚 +0.95% 收$351.60，突破 350 美元整數關卡，近1月仍漲 +6.1%"),
    line("NVDA", "微跌 -0.32% 收$229.74，守穩 $228 日低關鍵支撐，盤中最高達 $233.20，消化 OpenAI 雜音"),
    line("META", "微跌 -0.48% 收$717.42，在 720 美元附近高位震盪，近1月仍大賺 +9.5%"),
    line("AAPL", "回調 -1.27% 收$336.11，昨日避險資金回流高貝塔成長股，蘋果小幅獲利了結")
])

m8 = tbl([
    line("LITE", "暴力反彈 +5.22% 收$1,103.36！光模組龍頭急跌後強勁修復，重返千元大關上方"),
    line("COHR", "強彈 +3.40% 收$312.62，光通訊龍頭洗盤結束，逢低買盤積極承接"),
    line("ANET", "大漲 +2.91% 收$217.10，高階 AI 交換機龍頭突破整理平台，近1月大漲 +12.3%"),
    line("ASML", "反彈 +1.79% 收$1,801.51，光刻機巨頭重返 1,800 美元關卡上方"),
    line("VRT", "微漲 +0.59% 收$245.18，液冷散熱設備企穩收紅"),
    line("AVGO", "微漲 +0.41% 收$361.63，客製化 AI 晶片重返升勢，近5日大漲 +5.2%"),
    line("MRVL", "微漲 +0.23% 收$275.28，客製化 ASIC 晶片高位整固，近1月大賺 +17.2%"),
    line("DELL", "持平 0.00% 收$574.55，AI 伺服器龍頭守穩高位區間"),
    line("TSM", "下跌 -1.03% 收$453.27，台積電 ADR 隨台股國慶連假休市微幅整理"),
    line("MU", "下跌 -1.14% 收$1,024.06，守穩 $1,000 整數關卡與日低 $1,018.50 支撐，近1月大賺 +13.5%"),
    line("AMD", "下跌 -2.03% 收$608.10，回踩 600 美元平台支撐，等待財報催化"),
    line("ARM", "下跌 -2.47% 收$268.48，高估值 IP 股在連跌後逼近短期支撐位")
])

m9 = tbl([
    line("SNOW", "暴漲 +7.42% 收$368.89！企業數據雲端平台爆發，大行上調評級，創波段反彈新高"),
    line("PLTR", "狂飆 +5.17% 收$209.05！衝破 $200 歷史整數關卡，創歷史新天價！AIP 進入價格發現主升浪"),
    line("ORCL", "強彈 +4.33% 收$141.56，昨日重挫後逢低大抄底買盤湧入，收復 140 美元關卡"),
    line("CRWD", "上揚 +0.95% 收$265.50，網路安全龍頭續創波段反彈高，近1月大賺 +25.8%"),
    line("PANW", "微漲 +0.68% 收$401.20，突破 400 美元整數大關"),
    line("NOW", "持平 0.00% 收$139.75，工作流自動化平台需求穩健高位整固"),
    line("CRM", "持平 0.00% 收$227.80，Agentforce 應用推動低位築底平台確立"),
    line("ADBE", "持平 0.00% 收$241.05，昨日大漲 3.6% 後高位消化，維持強勢整固")
])

m10 = tbl([
    line("CEG", "暴漲 +4.58% 收$298.12！核電概念股昨日回吐後報復性大反彈，直逼 300 美元大關"),
    line("OKLO", "反彈 +1.53% 收$35.10，小型核反應堆概念股止跌回升"),
    line("NRG", "上揚 +1.11% 收$107.50，獨立電力股恢復上行趨勢"),
    line("ETN", "上漲 +0.87% 收$428.20，電氣設備龍頭在 20 日線上方重聚買盤"),
    line("PWR", "上漲 +0.83% 收$691.00，電網基建龍頭穩步上揚"),
    line("GEV", "上揚 +0.54% 收$1,004.73，電力設備龍頭突破千元整數關卡，分析師上調目標價"),
    line("VST", "微漲 +0.46% 收$156.86，發電商龍頭企穩回升，近5日仍大賺 +9.5%")
])

m11 = '''<ul class="list-disc pl-5 space-y-2">
<li><b>達美航空（DAL，盤前財報）</b>：公布 Q3 財報，GAAP 營收達 202 億美元創同期歷史新高，年增 16%；但受航油支出暴增 62% 至 41 億美元衝擊，調整後每股盈餘 $1.72 低於市場預期（$1.77–$1.92），管理層下調全年度 EPS 指引至 $5.10–$5.60，股價承壓下跌，提醒市場關注能源油價對交通運輸利潤的侵蝕。</li>
<li><b>達美樂披薩（DPZ）</b>：同店銷售成長平穩，外送促銷策略展現韌性，股價高位整固。</li>
<li><b>華爾街大行（JPM、WFC、C）</b>：下週二即將正式公布 Q3 財報，市場預期淨利息收入（NII）與投行承銷業務將顯著改善，推動金融板塊（XLF +1.10%）全線走強。</li>
<li><b>台灣外銷與科技股聯動</b>：台灣公布 9 月出口連創歷史新高，AI 晶片與伺服器外銷訂單強勁，為美股科技硬體提供了強大的基本面底氣。</li>
</ul>'''

s8 = sec(8, "重點個股新聞與異動", '<div class="space-y-3">' + details("8.1 大型科技七巨頭", m7, True) + details("8.2 AI 硬體 / 半導體重點股", m8) + details("8.3 軟體 / SaaS / AI 應用重點股", m9) + details("8.4 AI 電力 / 資料中心 / 能源基礎設施", m10) + details("8.5 其他顯著異動（財報與熱點股）", m11) + '<p class="text-xs text-slate-500">註：漲跌與區間根據 Yahoo Finance 官方報價；新聞與財報資料取自彭博、路透社、公司公告與可查證財經媒體。</p></div>')

# ---------- sec 9 ----------
s9 = sec(9, "財報日曆與財報解讀", f'''<div class="space-y-4">
  <div class="{BOX}"><h3 class="font-semibold mb-2">9.1 今日已公佈重點財報深度解讀</h3>
    <div class="space-y-3 text-sm leading-relaxed">
      <p><b>達美航空 (DAL，盤前)</b>：Q3 GAAP 營收達 202 億美元（調整後 176 億美元，年增 16%，符合市場預期）；調整後 EPS $1.72（市場預期 $1.77–$1.92，顯著低於預期）。核心獲利失色主要由於燃油成本激增 62% 達 41 億美元（預計全年燃料成本增加高達 60 億美元）。管理層將全年度 EPS 指引自原先的 $6.50–$7.50 大幅下調至 $5.10–$5.60；Q4 預期 EPS 為 $1.15–$1.65。市場解讀：商務與國際出行需求依然強勁，但油價暴漲對航空業形成了實質成本痛點，驗證了高油價對非能源實體產業的利潤擠壓風險。</p>
    </div>
  </div>
  {table(["日期", "公司名稱及代號", "重要關注點與市場預期"], [
    ["10/14 下週二 盤前", "JPMorgan Chase (JPM)", "華爾街大行財報季正式開幕！淨利息收入（NII）、投行與資產管理手續費、信貸損失撥備、高利率對借貸需求的影響"],
    ["10/14 下週二 盤前", "Wells Fargo (WFC)", "商業房地產（CRE）壞帳撥備、淨息差展望、資產上限監管進展"],
    ["10/14 下週二 盤前", "Citigroup (C)", "組織重組進度、海外投行業務復甦、資本回報計畫"],
    ["10/15 下週三 盤前", "Bank of America (BAC) / Goldman Sachs (GS)", "固定收益交易業務、全球併購顧問手續費成長率"],
    ["10/15 下週三 盤後", "Taiwan Semiconductor (TSM ADR)", "N2/N3 先進製程產能利用率、CoWoS 先進封裝擴產進度、2027 Capex 指引"]
  ])}
  <p class="text-xs text-slate-500">日曆來源：FactSet / Investing.com 財報日曆；實際公布時間以各公司投資人關係官網（IR）為準。</p></div>''')

# ---------- sec 10 ----------
s10 = sec(10, "機構觀點與資金流", f'''{paras([
    ("華爾街大行策略：標普刷52週新高確認牛市主升段", "高盛首席美股策略師今日發布研報指出，標普 500 指數在 Q3 財報季前夕刷新 52 週新高（7,844.52點），充分證明大盤並未受到地緣衝突與硬體估值波動的實質破壞；週四的晶片回踩屬於典型的牛市健康換手。美銀策略團隊則指出，隨著川普釋出中東不擴大衝突的表態，油價回落將緩解市場對二次通膨的恐慌，資金正從避險資產（必需消費、公用事業）大規模回流高確定性科技成長股與大型金融股。韋德布希分析師 Dan Ives 強調，Palantir 突破 $200 象徵著 AI 企業級軟體商業化全面進入收穫期。"),
    ("ETF 資金流向與板塊輪動特徵", f"ETF 資金流量官方數據 {NA}；從價格行為與成交分佈觀察：資金今日大舉流入非必需消費 ETF（XLY {PC('XLY')}）、金融 ETF（XLF {PC('XLF')}）、科技 ETF（XLK {PC('XLK')}）以及企業軟體 ETF（IGV {PC('IGV')}）；同時自昨日避險湧入的必需消費品板塊適度分流。這表明機構資金在財報季即將開啟之際，堅定選擇了『增配高貝塔成長股與受益高利率的金融龍頭』的進攻型再平衡策略。"),
    ("大宗交易與期權市場異動", f"大宗交易與內部人交易數據 {NA}。期權市場方面，VIX 波動率指數大幅下挫 -3.70% 收在 {PX('^VIX')}，全週自 15.52 回落；週五 SPY 與 QQQ 的價外看漲期權（Call）成交量顯著放大，尤其是 Palantir（PLTR）在突破 $200 後引發了大規模的 Gamma Squeeze，期權做市商被迫在現貨市場買入股票對沖，加速了股價向上拓展空間。"),
])}''')

# ---------- sec 11 ----------
s11 = sec(11, "板塊輪動判斷", paras([
    ("資金流入板塊", f"非必需消費（XLY {PC('XLY')}）、金融（XLF {PC('XLF')}）、通訊服務（XLC {PC('XLC')}）、企業軟體 SaaS（IGV {PC('IGV')}、PLTR、SNOW、ORCL）以及光通訊與核電發電（CEG、LITE、COHR）。此外，大型雲端與電商巨頭亞馬遜（AMZN {PC('AMZN')}）與微軟（MSFT {PC('MSFT')}）重新成為機構重倉回補的核心對象。"),
    ("資金流出板塊", f"昨日避險大漲的必需消費品（XLP {PC('XLP')}）漲幅收窄，資金主動撤出純防禦板塊；高估值半導體 IP 股（ARM）與個別晶片股（AMD）仍在消化前期獲利盤，但拋壓已顯著趨緩。"),
    ("AI 主線健康度與結構演變", "AI 主線格局呈現極度健康的『軟硬雙翼齊飛』：過往市場擔憂『上游硬體估值過高，下游應用無法兌現』，但今日 Palantir 狂飆突破 $200 創歷史天價、Snowflake 大漲 7.4%、甲骨文反彈 4.3%，以無可辯駁的市場表現宣告企業級 AI 應用商業化爆發；與此同時，光通訊（LITE +5.2%、COHR +3.4%）與核能發電（CEG +4.6%、GEV 突破千元）再度大漲，證明硬體基建需求並未衰退。大盤處於牛市主升通道中的健康輪動階段，結構極具韌性。"),
]))

# ---------- sec 12 watchlist ----------
W = [
    ("NVDA", "高位震盪", "微跌-0.32%收$229.74，守住$228低點支撐，消化OpenAI雜音，等待下週TSM財報"),
    ("AMD", "回踩支撐", "下跌-2.03%收$608.10，回踩600美元平台支撐，等待財報催化"),
    ("AVGO", "高位震盪", "微漲+0.41%收$361.63，客製化AI晶片重聚動能，近5日大漲+5.2%"),
    ("MRVL", "高位震盪", "微漲+0.23%收$275.28，客製化ASIC晶片高位整固，近1月大賺+17.2%"),
    ("GOOGL", "繼續強勢", "上揚+0.95%收$351.60，突破350美元整數大關，搜尋與雲端廣告防禦性極強"),
    ("MSFT", "繼續強勢", "大漲+2.25%收$534.38，Copilot商業化落地加速，領跑科技巨頭"),
    ("META", "高位震盪", "微跌-0.48%收$717.42，守在720平台附近，近1月仍大賺+9.5%"),
    ("AMZN", "繼續強勢", "暴漲+3.03%收$261.77，AWS算力支出擔憂消除，電商與雲端雙輪驅動"),
    ("ORCL", "低位修復", "強彈+4.33%收$141.56，昨日重挫後逢低大抄底買盤湧入，收復140元關卡"),
    ("CRM", "低位修復", "持平0.00%收$227.80，Agentforce企業應用低位築底平台確立"),
    ("NOW", "繼續強勢", "持平0.00%收$139.75，工作流軟體龍頭維持高位整固"),
    ("SNOW", "繼續強勢", "暴漲+7.42%收$368.89，企業數據雲端平台大爆發，破位反轉創波段新高"),
    ("ADBE", "高位震盪", "持平0.00%收$241.05，昨日大漲3.6%後高位強勢消化"),
    ("PLTR", "繼續強勢", "狂飆+5.17%收$209.05！衝破$200歷史大關，創歷史新天價！主升浪確立"),
    ("LITE", "繼續強勢", "暴力反彈+5.22%收$1103.36，光模組急跌後強勁修復，重返千元上方"),
    ("COHR", "繼續強勢", "強彈+3.40%收$312.62，光通訊洗盤結束，逢低買盤積極承接"),
    ("ANET", "繼續強勢", "大漲+2.91%收$217.10，高階交換機突破平台，近1月大漲+12.3%"),
    ("FLNC", "需要觀察", "微漲+0.40%收$7.48，超跌低位初步企穩，仍需量能驗證"),
    ("OKLO", "高位震盪", "反彈+1.53%收$35.10，SMR概念股高波動中企穩回升"),
    ("VST", "高位震盪", "企穩+0.46%收$156.86，發電商龍頭消化獲利盤，近5日仍大賺+9.5%"),
    ("CEG", "繼續強勢", "暴漲+4.58%收$298.12！核電概念股重啟升勢，直逼300元大關"),
    ("ETN", "回踩支撐", "上漲+0.87%收$428.20，電氣設備在20日線獲實質買盤承接"),
    ("VRT", "高位震盪", "微漲+0.59%收$245.18，液冷散熱設備企穩收紅")
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
s13 = sec(13, "明日（下週）交易計畫 / 觀察清單", f'''<div class="space-y-4">
  <div class="{BOX}"><h3 class="font-semibold mb-2">13.1 宏觀觀察要點</h3>
    <ul class="list-disc pl-5 text-sm space-y-1">
      <li><b>國際原油價格走勢</b>：WTI 今日回落至 ${PX("CL=F")}、Brent 回跌至 ${PX("BZ=F")}，關注週末中東情勢是否維持克制，油價能否持續運行於 90 美元下方。</li>
      <li><b>下週二（10/13）美國 9 月 CPI 報告</b>：通膨數據為全市場最關鍵核心宏觀指標，觀察核心 CPI 年率能否如期降溫，決定 10 年期美債殖利率（目前 5.24%）的後續方向。</li>
      <li><b>美債殖利率 5.20%–5.25% 平台穩定度</b>：若 CPI 符合預期促使殖利率跌破 5.20%，將全面引爆高估值成長股新一輪估值擴張行情。</li>
      <li><b>VIX 恐慌指數維持低位</b>：今日收 14.84，下週初觀察能否維持在 15.0 榮枯線下方。</li>
    </ul>
  </div>
  <div class="{BOX}"><h3 class="font-semibold mb-2">13.2 大盤與結構關鍵位置</h3>
    <p class="text-sm"><b>SPY</b>：今日收 778.53 點；上方壓力 782.10（今日高點）與 785.00 整數關卡；下方第一防守支撐 774.20（今日低點），次級強生命線為 20 日均線 766.82。<br/>
    <b>QQQ</b>：今日收 751.27 點；上方壓力 755.00 與 762.86（歷史高點）；下方第一防守 748.10（今日低點），次級強支撐 20 日均線 733.25。<br/>
    <b>結構確認信號</b>：關注小型股 IWM（收 ${PX("IWM")}）在 200 日線（276.72）企穩後能否發起補漲，以及等權標普 RSP 能否與大盤同步創高。</p>
  </div>
  <div class="{BOX}"><h3 class="font-semibold mb-2">13.3 核心板塊與重點個股觀察清單</h3>
    <p class="text-sm leading-relaxed">
      <b>最值得關注的個股</b>：<br/>
      1. <b>PLTR</b>：狂飆 +5.17% 衝破 $200 收 $209.05 創歷史天價！下週觀察突破後的持倉保護與價格發現上行空間，切忌盲目追高，留意回踩 $200 整數關卡時的支撐有效性。<br/>
      2. <b>SNOW</b>：大漲 +7.42% 收 $368.89，觀察連續放量突破後的動能延續性，確認是否確立中期反轉主升浪。<br/>
      3. <b>AMZN & MSFT</b>：亞馬遜（+3.03%）與微軟（+2.25%）重聚多頭動能，作為權重核心，觀察能否引領納指 100 衝擊歷史新高。<br/>
      4. <b>JPM & WFC</b>：下週二盤前公布 Q3 財報，作為財報季開路先鋒，其淨利息收入與撥備指引將直接定價全市場金融板塊。<br/>
      5. <b>NVDA</b>：守穩 $228 日低支撐收 $229.74，觀察下週能否放量重返 $235 上方，消化短期籌碼。<br/>
      6. <b>MU</b>：在 $1,000 整數關卡與 $1,018 日低展現強支撐，下週觀察千元底部的買盤厚度。<br/>
      7. <b>CEG & GEV</b>：Constellation Energy（CEG +4.58%）直逼 $300、GE Vernova（GEV）突破千元，核電與電力設備再度成為資金寵兒，觀察高位放量突破信號。<br/>
      8. <b>LITE & COHR</b>：光通訊單日報復性反彈 3%–5%，急跌洗盤結束後觀察波段攻擊動能。<br/>
      9. <b>ORCL</b>：強彈 +4.33% 收復 $140，觀察 140 美元支撐確立情況。<br/>
      10. <b>DAL</b>：財報指引下調後觀察航空股對油價回落的吸收反應。
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
    ("下週二 9 月 CPI 數據波動", "中高", "密西根通膨預期微升，若 9 月 CPI 超預期反彈，將刺激美債殖利率再度上攻 5.30% 以上，對高估值股票形成壓制"),
    ("華爾街大行財報季容錯率", "中高", "下週二 JPM、WFC、Citi 開啟財報季，在高利率與信貸放緩背景下，若業績指引不及預期可能引發金融板塊短期獲利回吐"),
    ("中東地緣政治反覆與油價反撲", "中高", "雖然川普表態期中前不攻擊伊朗，但波斯灣潛在摩擦依然存在，若原油再度飆升破 $95 將重新推升通膨恐慌"),
    ("終端消費動能放緩風險", "中", "密西根消費者信心降至 46.3 創五個月新低，耐用品購買意願驟降，需警惕消費降級對非必需消費品零售業績的滯後衝擊"),
    ("軟體強勢股短線獲利盤兌現", "中", "Palantir 突破 $200 創歷史天價、Snowflake 單日暴漲 7.4%，短線獲利盤豐厚，需警惕下週初可能出現的震盪洗盤"),
    ("半導體硬體供應鏈分化", "中", "費半反彈 +0.67% 雖企穩，但 AMD 與 ARM 依然承壓，市場對下週台積電法說會指引保持高度審慎"),
    ("流動性環境與美元走勢", "低", "恐慌指數 VIX 回落至 14.84，美元指數平穩，短期系統性流動性緊縮風險極低")
]

s14 = sec(14, "風險提示（視覺化風險矩陣）", table(["風險維度", "風險等級", "具體情境與解讀分析"], [[f"<b>{a}</b>", f'<span class="px-2 py-0.5 rounded font-semibold {RC[b]}">{b}</span>', c] for a, b, c in risks]))

# ---------- sec 15 ----------
s15 = f'''
    <section id="sec-15" class="scroll-mt-6 p-6 rounded-2xl bg-gradient-to-br from-white to-slate-50 dark:from-zinc-900 dark:to-zinc-950 border border-slate-200 dark:border-zinc-800 shadow-sm">
      <h2 class="{H2}"><span class="text-brand-500">15.</span> 最終結論</h2>
      <div class="space-y-3 text-sm sm:text-base leading-relaxed text-slate-700 dark:text-zinc-300">
        <p><strong>今日市場結論：</strong>標普 500 指數收漲 <strong>{PC("^GSPC")}</strong> 報 <strong>{PX("^GSPC")}</strong>（盤中 7,844.52 點刷 52 週新高）、道瓊工業指數大漲 359 點（{PC("^DJI")}）、納斯達克上揚 {PC("^IXIC")}、費半企穩回升 {PC("^SOX")}。川普表態期中選舉前不对伊朗動手帶動油價降溫（WTI 回跌至 $90.97），大幅消解了地緣二次通膨擔憂；大科技權重股（AMZN +3.03%、MSFT +2.25%、TSLA +2.05%）強勢回歸，軟體與 AI 應用持續爆發（Palantir 狂飆 +5.17% 突破 $200 大關創 $209.05 歷史天價！Snowflake 大漲 7.4%）。全市場 11 大板塊高達 9 個收紅，等權標普 RSP 上漲 +0.43%，大盤呈現健康且強勁的普漲格局。</p>
        <p><strong>當前市場階段：</strong>強趨勢上漲 / 高位整固後強勢突破（標普刷新 52 週新高，VIX 回落至 14.84，技術與基本面共振走強）。</p>
        <p><strong>我的操作傾向（中性表述）：</strong>大盤上升通道結構健康完整，切忌盲目看空做空。策略上建議：第一，對已進入歷史新高價格發現的龍頭（如 PLTR）適度上移保護停利位，讓利潤充分奔跑但不盲目追高；第二，對基本面具備高壁壘但在本週遭遇非理性殺估值的晶片硬體（如 NVDA、MU）與光通訊/核能龍頭，可在整數關卡支撐位耐心尋求低吸機會；第三，關注即將到來的 Q3 財報季，保持科技成長與大型金融的均衡配置，靜待下週 CPI 報告落地。</p>
        <div><strong>最值得關注的 5 個核心訊號：</strong>
          <ol class="list-decimal pl-6 mt-2 space-y-1">
            <li><b>下週二（10/13）美國 9 月 CPI 報告</b>：通膨數據能否如期降溫，將直接決定 10 年期美債殖利率是否具備向下突破 5.20% 的動能。</li>
            <li><b>下週二摩根大通（JPM）等華爾街大行財報</b>：銀行業淨利息收入與信貸品質展望，將為整個 Q3 財報季奠定基調。</li>
            <li><b>WTI 原油能否守在 $90–$91 下方</b>：觀察中東地緣政治緩和的延續性，油價回落是維持美股估值擴張的關鍵底層支撐。</li>
            <li><b>Palantir（PLTR $209.05）歷史突破後的高度與承接</b>：觀察 $200 整數關卡是否轉化為強大支撐位，引領整個 SaaS 板塊估值重估。</li>
            <li><b>標普 500 挑戰 7,850 點整數大關</b>：守穩 7,770 點今日低點之上，確認本次 52 週新高突破為真實有效的牛市主升段。</li>
          </ol>
        </div>
        <p class="text-xs text-slate-500 mt-3">資料來源與聲明：價格與技術數據取自 Yahoo Finance 官方報價（至 2026-10-09 收盤），宏觀經濟與公司動態整合彭博、路透社、FactSet、美國密西根大學、勞工部DOL、財政部官方公告與企業新聞稿；未取得完整公開流之項目已於內文中清晰標註。本文僅供投資復盤與策略研究，不構成任何個人投資建議。</p>
      </div>
    </section>
'''

# ---------- tail ----------
tail = old[old.index("<!-- Footer -->"):]
tail = re.sub(r"<div>美股收盤日報｜資料來源：.*?</div>", "<div>美股收盤日報｜資料來源：Yahoo Finance、美國密西根大學、勞工部DOL、財政部、彭博、路透社、FactSet、公司新聞稿與SEC申報檔案</div>", tail)

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
