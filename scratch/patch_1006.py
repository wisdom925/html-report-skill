L = open("generate_report_20261005.py", encoding="utf-8").read().split("\n")
P = {}
def rep(a, b, text): P[(a, b)] = text.strip("\n")

rep(69, 71, r"""TITLE = "美股收盤日報｜2026-10-06"
DESC = ("週二（2026年10月6日）美股收高：標普500 +0.58%報7,818.93點、納指 +0.45%報27,599.89點，兩者創歷史收盤新高、道瓊 +0.49%報51,521.28點；"
        "10年期殖利率回落至5.27%，電力股爆發（CEG +12.3%、VST +10.8%）、Marvell 投資人日帶動AI客製晶片股（MRVL +5.8%、AVGO +3.7%）；小型股逆勢走弱（羅素2000 -0.59%）。")""")
rep(74, 74, r"""head = re.sub(r"<title>.*?</title>", f"<title>{TITLE}｜標普納指雙創收盤新高、殖利率回落、電力股爆發 ({D})</title>", head, flags=re.S)""")
rep(77, 77, r"""head = re.sub(r'<meta property="og:description" content=".*?">', '<meta property="og:description" content="標普、納指創收盤新高，殖利率回落至5.27%，電力股與AI客製晶片股領漲，小型股走弱。">', head)""")
rep(85, 85, r"""          <span class="w-2 h-2 rounded-full bg-emerald-500 animate-pulse"></span> 標普納指雙創收盤新高・殖利率回落・電力股爆發""")
rep(99, 105, r"""        <p>{S}【大盤走勢】</strong> 美股週二續創新高。標普500 <strong>{PC("^GSPC")}</strong> 收 <strong>{PX("^GSPC")}</strong>，納斯達克綜合指數 <strong>{PC("^IXIC")}</strong> 收 <strong>{PX("^IXIC")}</strong>（兩者創歷史收盤新高），道瓊 <strong>{PC("^DJI")}</strong> 收 <strong>{PX("^DJI")}</strong>；但羅素2000 {PC("^RUT")}，費半 {PC("^SOX")} 收 {PX("^SOX")}。</p>
        <p>{S}【驅動因素】</strong> 美債殖利率自多年高位回落（10年期 {PX("^TNX")}%，較前日下降約4bp）、Q3財報季前盈利預期樂觀，以及AI主線擴散。個股面：Constellation 與Google簽20年購電協議（CEG {PC("CEG")}）、DOE 向 Vistra 提供最高42億美元有條件貸款承諾（VST {PC("VST")}）引爆電力股；Marvell 投資人日將FY2028營收目標上調至200億美元（MRVL {PC("MRVL")}），帶動 AVGO {PC("AVGO")}、ANET {PC("ANET")}。宏觀面，8月貿易逆差擴大至1,056億美元（高於預期約1,020億）。</p>
        <p>{S}【資金偏好】</strong> Risk-On：VIX 收 {PX("^VIX")}（{PC("^VIX")}），日內區間 {q["^VIX"]["low"]:.2f}–{q["^VIX"]["high"]:.2f}，低波動；WTI 原油 {PC("CL=F")}（收 ${PX("CL=F")}）、黃金期貨 {PC("GC=F")}；美元（UUP）{PC("UUP")}。</p>
        <p>{S}【市場寬度】</strong> 大型股強、小型股弱：11個板塊中10個收高（僅醫療保健 XLV {PC("XLV")} 下跌），公用事業 XLU {PC("XLU")} 領漲，等權 RSP {PC("RSP")} 與 SPY（{PC("SPY")}）同步；但羅素2000 {PC("^RUT")}、IWO {PC("IWO")}，近一個月小型股仍落後（IWM {q["IWM"]["1m"]:+.2f}% vs SPY {q["SPY"]["1m"]:+.2f}%）。</p>
        <p>{S}【核心主線】</strong> AI 基礎設施「電力＋客製晶片＋網通」擴散：CEG、VST、NRG {PC("NRG")}、PWR {PC("PWR")}、GEV {PC("GEV")}、ETN {PC("ETN")} 全線走強。今日盤後 Constellation Brands 公布財報；10月7日（週三）FOMC會議紀要為下一個催化。</p>
        <div class="mt-4 p-4 rounded-xl bg-brand-50 dark:bg-zinc-800/60 border border-brand-100 dark:border-brand-900/40 text-brand-900 dark:text-brand-200 font-medium">
          💡 <strong>今日市場狀態判斷：</strong>「指數創高、AI電力與客製晶片領漲、殖利率回落提供支撐；但小型股走弱、寬度分歧，短線擁擠度仍高。」
        </div>""")
rep(117, 117, r"""    card("Nasdaq Composite", "^IXIC", PX("^IXIC"), "創收盤新高"),""")
rep(122, 123, r"""    card("Software (IGV)", "IGV", PX("IGV"), "軟體續彈"),
    card("VIX", "^VIX", PX("^VIX"), "前收 15.52"),""")
rep(129, 135, r"""irow("S&P 500", "SPY", "^GSPC", "創歷史收盤新高（據報導），收盤 7,818.93 距日高(7,844.52)約25點；SPY 在20/50/100/200日均線之上，RSI 72")
irow("Nasdaq Composite", "—", "^IXIC", "創歷史收盤新高，開盤後窄幅整理")
irow("Nasdaq 100", "QQQ", "^NDX", "QQQ 收759.66，創20日新高區；RSI 83 偏超買")
irow("Dow Jones", "DIA", "^DJI", "收51,521.28，跟隨大盤；近一個月仍偏弱 (-3.54%)")
irow("Russell 2000", "IWM", "^RUT", f"小盤逆勢下跌(-0.59%)，明顯跑輸標普(+0.58%)；IWM 仍低於20/50日均線")
irow("SOX 半導體", "SOXX / SMH", "^SOX", "近5日 +4.66%、近1月 +12.63%；今日 +0.34%，SMH/SOXX 小幅下跌，高位整固")
irow("CBOE VIX", "^VIX", "^VIX", "收15.01，日內自15.54回落，仍處低波動區")""")
rep(143, 143, r"""      <p class="mt-3 text-sm text-slate-600 dark:text-zinc-400">補充：標普500 與納指均創歷史收盤新高；小盤股（羅素2000 -0.59%）明顯跑輸標普500（+0.58%）；VIX 收15.01，較前收下降 0.51。</p>""")
rep(147, 160, r"""mer = f'''graph LR
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
  PreMarket --> Open --> Day --> Close'''""")
rep(166, 170, r"""    ("盤前", "美國8月貿易逆差擴大至1,056億美元（預期約1,020億，7月修正值928億），進口創歷史新高（半導體、資本財、原油）。Constellation 宣布與Google 20年購電協議（投資逾43億美元提升11座核反應爐出力），DOE 確認對 Vistra 最高42億美元有條件貸款承諾。"),
    ("開盤後", f"標普500 開 {q['^GSPC']['open']:,.2f}（前收 {q['^GSPC']['prev']:,.2f}），開盤價即為日內低點，顯示賣壓有限；納指開 {q['^IXIC']['open']:,.2f}、日低 {q['^IXIC']['low']:,.2f}。電力股開盤即跳空走高。"),
    ("午盤", "（日內分時資料以高低點推斷）指數自低位墊高；Marvell 投資人日公布FY2028營收目標200億美元、FY2031目標700–900億美元，MRVL 日內區間 267.26–301.27，自低位大幅拉升，AVGO、ANET 同步走強；SOX 日內區間 13,196.50–13,349.96。"),
    ("尾盤", f"標普500 收 {PX('^GSPC')}，距日高 {q['^GSPC']['high']-q['^GSPC']['price']:.2f} 點；納指收 {PX('^IXIC')} 創收盤新高，VIX 收 {PX('^VIX')}。"),
    ("盤後與核心原因", "漲跌核心：殖利率回落（10年期 5.27%）＋AI基礎設施題材（電力、客製晶片、網通）。盤後 Constellation Brands(STZ) 公布FQ2：EPS $3.74（預期$3.61）、營收$26.3億（預期$25.4億），但維持全年EPS指引$11.20–11.90（中值低於共識$11.72），股價盤後約跌2.7%。半導體ETF（SMH/SOXX）微跌屬高位整理，未見明顯 sell-the-news。"),""")
rep(183, 185, r"""tab_y = f'''<div id="panel-yields" class="tab-panel space-y-4"><h4 class="font-bold text-slate-900 dark:text-white text-base">長天期殖利率自高位回落，10年期降至5.27%</h4>
  <div class="grid grid-cols-2 sm:grid-cols-4 gap-3 font-mono">{yield_cards}</div>
  <p>10年期收 {PX("^TNX")}%（前收5.31%，日內區間 5.26–5.30%），較前日下降約4bp，近一個月上升約 {q["^TNX"]["1m"]:.1f}%（相對變動）；30年期 {PX("^TYX")}%（-2bp）、5年期 {PX("^FVX")}%（-4bp）。30年減5年利差由約59bp擴至約61bp，曲線略微陡峭化（2年期殖利率本次未取得）。市場含義：中長端殖利率自多年高位回落，緩解成長股估值壓力，但仍處高位。</p></div>'''""")
rep(186, 188, r"""tab_f = '''<div id="panel-fed" class="tab-panel space-y-4"><h4 class="font-bold text-slate-900 dark:text-white text-base">Fed 10月會議：市場傾向按兵不動，12月升息仍有定價</h4>
  <div class="grid grid-cols-2 sm:grid-cols-3 gap-3 font-mono">''' + stat("10/27–28 維持利率", "多數定價", "據報導，上週就業數據弱於預期後升息機率降溫") + stat("12月升息", "仍有定價", "據報導大致已定價（二手來源）") + stat("下一個催化", "10/7 週三", "FOMC會議紀要與Fed官員講話") + '''</div>
  <p>FedWatch 具體機率本次未取得可查證的官方即時數據（前一份報告引述的約82%維持／18%升息為二手來源，未更新），請以 CME 官網為準；年內預期次數未取得可查證數據。市場關注會議紀要對利率路徑與縮表的措辭。</p></div>'''""")
rep(189, 189, r"""tab_c = f'''<div id="panel-commodities" class="tab-panel space-y-4"><h4 class="font-bold text-slate-900 dark:text-white text-base">美元走弱、黃金反彈、油價小幅上揚</h4>""")
rep(193, 193, r"""  <p>DXY 指數本次未取得，使用美元ETF UUP（{PC("UUP")}）作為代理，顯示美元小幅走弱；WTI 期貨 ${PX("CL=F")}（{PC("CL=F")}），Brent ${PX("BZ=F")}（{PC("BZ=F")}），Yahoo 期貨報價為收盤後時點，與盤中走勢可能有差；黃金期貨 {PC("GC=F")}，但近1個月仍 {q["GC=F"]["1m"]:+.1f}%，在實質利率高位下承壓。加密資產小幅回落（加密貨幣為全天候交易，數字為該日收盤）。</p></div>'''""")
rep(194, 197, r"""tab_d = '''<div id="panel-data" class="tab-panel space-y-4"><h4 class="font-bold text-slate-900 dark:text-white text-base">8月貿易逆差擴大至1,056億美元，高於預期</h4>
  <div class="overflow-x-auto"><table class="w-full text-sm text-left"><thead class="bg-slate-50 dark:bg-zinc-800/60"><tr><th class="p-3">數據</th><th class="p-3">實際</th><th class="p-3">預期</th><th class="p-3">前值</th><th class="p-3">市場解讀</th></tr></thead><tbody class="divide-y divide-slate-100 dark:divide-zinc-800">
  <tr><td class="p-3 font-semibold">貿易收支（8月）</td><td class="p-3 font-mono">-$105.6B</td><td class="p-3 font-mono">約 -$102.0B</td><td class="p-3 font-mono">-$92.8B（修正）</td><td class="p-3">進口創歷史新高$420.8B（+4.3%，原油、半導體、資本財），出口$315.2B（+1.4%）；反映內需強勁與AI設備進口，對股市影響偏中性。</td></tr></tbody></table></div>
  <p>本日無其他主要經濟數據（CPI/PPI/非農等）公布。</p></div>'''""")
rep(211, 221, r"""    ("原物料", "XLB", "溫和收高，近1月仍偏弱 (-5.2%)"),
    ("通訊服務", "XLC", "近乎持平，META -0.41% 拖累"),
    ("能源", "XLE", "油價小幅上揚，近5日 +3.6%"),
    ("金融", "XLF", "小幅收高，近1月仍落後 (-7.0%)"),
    ("醫療保健", "XLV", "唯一下跌板塊，近5日 -2.1%"),
    ("必需消費", "XLP", "防禦資金回流"),
    ("科技", "XLK", "AVGO +3.67%、MSFT +0.78%、NVDA +0.14%"),
    ("非必需消費", "XLY", "AMZN +1.95%、TSLA +0.51% 支撐"),
    ("公用事業", "XLU", "CEG +12.25%、VST +10.77%、NRG +7.02% 領漲"),
    ("工業", "XLI", "PWR +5.29%、GEV +3.96%、ETN +2.89% 電力基建帶動"),
    ("房地產", "XLRE", "殖利率回落帶動反彈"),""")
rep(232, 232, r"""      <p class="mt-3 text-sm text-slate-600 dark:text-zinc-400">最強：公用事業 XLU（{PC("XLU")}）、工業 XLI（{PC("XLI")}）、非必需消費 XLY（{PC("XLY")}）；最弱：醫療保健 XLV（{PC("XLV")}）。成長 vs 價值：IWO {PC("IWO")} 與 IWN {PC("IWN")} 均下跌，小盤成長更弱；大型成長（QQQ {PC("QQQ")}）勝過小盤。AI→傳統電力/能源輪動：電力股（CEG、VST、NRG）與電力設備（PWR、GEV、ETN）同日大漲，XLU 與 XLI 領漲而 XLK 僅 {PC("XLK")}，屬「AI主線向電力基礎設施擴散」的明確跡象，但 XLK 近5日仍 {q["XLK"]["5d"]:+.2f}%，並非替代而是擴散。</p>''')""")
rep(244, 247, r"""note = {"SMH": "高位整理，近5日 +4.22%", "SOXX": "平盤附近，漲多整理", "IGV": "軟體續彈，近5日 +5.65%", "CRWD": "近1月 +30.9% 領漲", "PANW": "近1月 +26.0%，今日大漲",
        "NOW": "軟體龍頭續彈", "PLTR": "溫和上漲", "LITE": "近5日 +16.4%，短線擁擠", "COHR": "近5日 +15.8%",
        "VRT": "近1月 -9.8% 仍在修復", "GEV": "近5日 +6.9%，電力設備領漲", "FLNC": "近1月 -22.4% 偏弱，今日反彈", "IWO": "小盤成長走弱", "IWN": "小盤價值走弱",
        "RSP": "與SPY同步，大型股寬度尚可", "QQQ": "大型成長領漲"}""")
rep(255, 255, r"""      <p class="text-sm text-slate-700 dark:text-zinc-300">成分股站上20/50/100/200日均線的比例（如 S5TW/S5FI）{NA}；以下為代表ETF相對均線位置（均線、RSI 以至10-06收盤的Yahoo日線計算）：</p>""")
rep(257, 257, r"""      <p class="mt-2 text-sm text-slate-600 dark:text-zinc-400">SPY、QQQ 在所有主要均線之上，趨勢健康；IWM 低於20/50日均線，小型股中期趨勢偏弱。</p></div>""")
rep(258, 258, r"""      <div class="{BOX}"><h3 class="font-semibold mb-2">6.2 漲跌家數、新高新低</h3><p class="text-sm">NYSE/Nasdaq 上漲/下跌家數、52週新高/新低 {NA}。代理：11個板塊中10個收高；SPY {PC("SPY")} vs RSP {PC("RSP")} 接近，但羅素2000 {PC("^RUT")} 下跌，說明上漲面集中於大型股。</p></div>""")
rep(274, 274, r"""      <p class="mt-3 text-sm text-slate-600 dark:text-zinc-400">註：均線/RSI/MACD 以Yahoo日線至10-06收盤計算。判讀：SMH（RSI 87）與 XLK（RSI 87）處於極度超買，QQQ（83）偏超買，SPY（72）略超買，追高風險上升；IWM RSI 44 偏中性偏弱。明日多頭確認：SPY 收盤站穩日高 781.6 之上、QQQ 站穩 762.9。風險位：SPY 失守 778.0（日低）、QQQ 失守 759.1（日低），更深支撐為20日均線區。</p>''')""")
rep(281, 287, r"""m7 = tbl([line("NVDA", "平盤附近整理，近5日 +5.3%"), line("MSFT", "收$529.3，AI軟體買盤延續"), line("AAPL", "小幅上漲"), line("GOOGL", "與Constellation簽20年購電協議（電力供應AI資料中心）"), line("AMZN", "+1.95%，七巨頭中領漲"), line("META", "小幅回落，近1月 +19.8% 後整理"), line("TSLA", "收$380.68，近5日 +7.9%")])
m8 = tbl([line("AVGO", "受Marvell投資人日帶動，客製晶片題材"), line("TSM", "小幅回落"), line("AMD", "+2.8%，近1月 +36.0%"), line("MRVL", "投資人日：FY2028營收目標上調至$200億（原$180億，共識$182億）；FY2031目標$700–900億、EPS目標$30以上"), line("MU", "-1.73%，高位回吐"), line("ASML", "-1.39%"), line("ARM", "小幅回落"), line("DELL", "+3.93%"), line("VRT", "小幅回落"), line("ANET", "+4.09%，網通題材隨MRVL走強")])
m9 = tbl([line("CRM", "軟體中最弱，近1月 -13.2%"), line("NOW", "軟體龍頭續彈"), line("SNOW", "-0.9%"), line("ORCL", "+1.61%"), line("ADBE", "小幅回落"), line("PANW", "+3.23%，近1月 +26.0%"), line("CRWD", "+2.27%，近1月 +30.9%"), line("PLTR", "+1.41%")])
m10 = tbl([line("CEG", "與Google簽20年購電協議（投資逾$43億提升11座核反應爐、新增890MW）及15年2,700MW供應協議，創單日大漲"), line("VST", "DOE 有條件貸款承諾最高$42億，支持Perry、Davis-Besse、Beaver Valley核電擴建"), line("NRG", "獨立電力商同步走高"), line("ETN", "+2.89%"), line("PWR", "+5.29%，電力基建"), line("GEV", "+3.96%"), line("OKLO", "+7.17%，核能題材跟漲")])
m11 = '''<ul class="list-disc pl-5 space-y-1"><li><b>Constellation Brands（STZ，盤後約-2.7%）</b>：FQ2 EPS $3.74（預期$3.61）、營收$26.3億（預期$25.4億），啤酒銷售+5%，但維持全年EPS指引$11.20–11.90，中值低於共識$11.72。</li>
<li><b>Marvell（+5.81%）</b>：投資人日上調長期營收目標，帶動 AVGO、ANET 及 Astera Labs、Credo 等同業走強。</li>
<li><b>Dell（+3.93%）、PANW（+3.23%）</b>：資料中心與資安股同步走強，未找到單一可查證催化。</li></ul>'''""")
rep(292, 294, r"""  <div class="{BOX}"><h3 class="font-semibold mb-2">9.1 昨夜（10/6）財報與公司事件</h3><p class="text-sm">Marvell 投資人日（盤中）上調長期目標；盤後 Constellation Brands(STZ) 財報：EPS $3.74 對預期 $3.61、營收 $26.3 億對預期 $25.4 億，啤酒部門銷量+5.5%、葡萄酒與烈酒銷售+17%，但維持FY27 EPS指引 $11.20–11.90（共識 $11.72），盤後約-2.7%。Q3財報季將自10月中旬由銀行股拉開序幕。</p></div>
  {table(["日期", "公司", "關注點"], [["10/7 週三", "Levi Strauss (LEVI)、Applied Digital (APLD)", "APLD 為AI資料中心題材股；同日FOMC會議紀要"], ["10/8 週四", "PepsiCo (PEP)、Progressive (PGR)", "消費者價格彈性、保險定價"], ["10/9 週五", "（以公司IR確認為準）", "本日未取得可查證的重要財報"]])}
  <p class="text-xs text-slate-500">日曆來源：Investing.com 財報日曆（沿用前一交易日整理）；EPS/營收預期除STZ外未取得，請於公司IR確認。</p></div>''')""")
rep(298, 300, r"""    ("評級／目標價", "本日未取得可查證的大型券商評級或目標價調整（前一日：摩根士丹利維持輝達 Overweight、目標價$300，未更新）。"),
    ("ETF 資金流", f"ETF 資金流量數據 {NA}；價格面：SMH 近5日 +4.22%、SOXX +3.88%，IGV +5.65%，XLU 單日 {PC('XLU')}，顯示軟體、半導體與電力近期受資金追捧。"),
    ("大宗/內部人/期權", f"本日大宗交易、內部人交易與異常期權活動 {NA}。"),""")
rep(305, 307, r"""    ("資金流入", f"公用事業（XLU {PC('XLU')}）、工業（XLI {PC('XLI')}）、非必需消費（XLY {PC('XLY')}）領漲；近5日科技（XLK {q['XLK']['5d']:+.2f}%）、軟體（IGV {q['IGV']['5d']:+.2f}%）、半導體（SMH {q['SMH']['5d']:+.2f}%）與能源（XLE {q['XLE']['5d']:+.2f}%）領先。"),
    ("資金流出／落後", f"醫療保健（XLV 近5日 {q['XLV']['5d']:+.2f}%）、小型股（IWM 近1月 {q['IWM']['1m']:+.2f}%）、金融（XLF 近1月 {q['XLF']['1m']:+.2f}%）。"),
    ("AI 主線健康度與階段", "AI 主線由晶片擴散至電力、客製晶片與網通，健康度良好，但SMH/XLK RSI 87、光通訊個股5日漲約16%，擁擠度偏高，且小型股走弱使寬度分歧。研判為『強趨勢上漲中的高位整理與輪動』，延續概率高於頂部，但追高性價比下降。"),""")
rep(312, 319, r"""    ("NVDA", "高位震盪", "平盤附近整理；近5日+5.3%"), ("AMD", "繼續強勢", "+2.8%，近1月+36.0%"), ("AVGO", "繼續強勢", "+3.67%，MRVL投資人日帶動"),
    ("MRVL", "繼續強勢", "+5.81%，上調長期目標"), ("GOOGL", "繼續強勢", "與CEG簽購電協議"), ("MSFT", "繼續強勢", "+0.78% 收$529"),
    ("META", "高位震盪", "近1月+19.8%，今日小跌"), ("AMZN", "繼續強勢", "+1.95%"), ("ORCL", "低位修復", "近1月-8.8%，近5日反彈5.1%"),
    ("CRM", "破位風險", "近1月-13.2%，今日-2.1%最弱"), ("NOW", "低位修復", "+1.39% 軟體續彈"), ("SNOW", "高位震盪", "-0.9%"),
    ("ADBE", "低位修復", "近1月-10.7%，小幅回落"), ("PLTR", "高位震盪", "近1月+10.2%"), ("LITE", "短線過熱", "近5日+16.4%，今日+3.8%"),
    ("COHR", "短線過熱", "近5日+15.8%，今日+1.4%"), ("ANET", "繼續強勢", "+4.09%"), ("FLNC", "破位風險", "近1月-22.4%，今日反彈"),
    ("OKLO", "高位震盪", "+7.17%，近1月-6.6%"), ("VST", "短線過熱", "+10.77%，近5日+14.0%"), ("CEG", "短線過熱", "+12.25%，近5日+13.5%"),
    ("ETN", "繼續強勢", "+2.89%，近1月+8.3%"), ("VRT", "高位震盪", "-0.19%，近1月-9.8%"),""")
open("scratch/_blocks_ok", "w").write("ok")
out = []
i = 1
starts = {a: (b, t) for (a, b), t in P.items()}
while i <= len(L):
    if i in starts:
        b, t = starts[i]
        out.append(t)
        i = b + 1
    else:
        out.append(L[i - 1]); i += 1
s = "\n".join(out)
open("scratch/gen_1006_stage.py", "w", encoding="utf-8").write(s)
