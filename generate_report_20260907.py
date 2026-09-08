import os
import subprocess
import sys
import json

# Load quotes
quotes_file = "/Users/wisdom/html-report-skill/scratch/quotes_2026-09-07.json"
with open(quotes_file, "r", encoding="utf-8") as f:
    quotes = json.load(f)

def get_val(ticker, key):
    if ticker in quotes and key in quotes[ticker]:
        val = quotes[ticker][key]
        if key == "pct":
            return f"{val:+.2f}%" if val >= 0 else f"{val:.2f}%"
        elif key == "change":
            return f"{val:+.2f}" if val >= 0 else f"{val:.2f}"
        elif key == "price":
            if val > 10000:
                return f"{val:,.2f}"
            return f"{val:.2f}"
    return "N/A"

def get_raw_val(ticker, key):
    if ticker in quotes and key in quotes[ticker]:
        return quotes[ticker][key]
    return 0.0

# 11 S&P 500 Sectors data (Friday close baseline for holiday review)
sectors = [
    {"name": "科技板塊", "etf": "XLK", "pct": 0.70, "5d": "+0.95%", "1m": "-0.10%", "driver": "半導體狂潮與AI硬體爆發完全抵消微軟蘋果回吐，輝達（+0.84%）、AMD（+4.69%）、美光（+6.10%）領銜，XLK逆勢收漲+0.70%榮登第一。"},
    {"name": "工業板塊", "etf": "XLI", "pct": 0.41, "5d": "-2.69%", "1m": "-4.69%", "driver": "電網現代化與重電設備伊頓（ETN +3.46%）與電力基建Quanta（PWR +1.35%）延續強勢，XLI穩步收漲+0.41%。"},
    {"name": "公用事業", "etf": "XLU", "pct": 0.12, "5d": "-1.08%", "1m": "-0.78%", "driver": "核電直供電力龍頭CEG（+4.88%）與發電巨頭Vistra（VST +3.52%）暴力拉升，AI電力需求推動XLU收漲+0.12%。"},
    {"name": "原物料板塊", "etf": "XLB", "pct": -0.34, "5d": "+0.76%", "1m": "-1.09%", "driver": "美元指數走強至99.20疊加黃金自歷史天價小幅休整，特種金屬與化工小幅回吐，XLB微跌-0.34%。"},
    {"name": "房地產", "etf": "XLRE", "pct": -0.72, "5d": "-2.82%", "1m": "-2.62%", "driver": "8月非農就業超預期刺激10年期美債利率跳升至4.78%，商業地產與高息REITs再度承壓，XLRE收跌-0.72%。"},
    {"name": "金融板塊", "etf": "XLF", "pct": -0.79, "5d": "+1.06%", "1m": "+2.31%", "driver": "前日大漲後高位整理，大行投行諮詢業務基本面紮實，降息預期延後利好淨息差維持，XLF微跌-0.79%。"},
    {"name": "必需消費", "etf": "XLP", "pct": -0.80, "5d": "-0.95%", "1m": "-0.35%", "driver": "市場資金偏好集中在硬體半導體主線，防禦性超市與日用品縮量整理，XLP收跌-0.80%。"},
    {"name": "能源板塊", "etf": "XLE", "pct": -0.87, "5d": "+2.93%", "1m": "+5.33%", "driver": "WTI原油在$91.35/桶高位整固，資金流向科技晶片主線，油氣龍頭窄幅回調，XLE收跌-0.87%。"},
    {"name": "醫療保健", "etf": "XLV", "pct": -1.04, "5d": "-1.24%", "1m": "-0.69%", "driver": "防禦板塊普遍承壓，大藥企與醫療器械缺乏短線催化劑，XLV收跌-1.04%。"},
    {"name": "通訊服務", "etf": "XLC", "pct": -1.19, "5d": "+1.21%", "1m": "+2.91%", "driver": "儘管Meta（+1.00%）再破$616歷史天價，但谷歌（-1.17%）與傳統電信股回跌拖累，XLC收跌-1.19%。"},
    {"name": "非必需消費", "etf": "XLY", "pct": -1.33, "5d": "-0.93%", "1m": "-2.48%", "driver": "特斯拉（TSLA -5.92%）在前日暴漲後遭遇沉重獲利了結與期權結算賣壓，拖累XLY大跌-1.33%全場墊底。"}
]

sectors_sorted = sorted(sectors, key=lambda x: x["pct"], reverse=True)

sector_rows = ""
for rank, sec in enumerate(sectors_sorted, 1):
    pct_val = sec["pct"]
    pct_color = "text-emerald-600 font-bold" if pct_val >= 0 else "text-rose-500 font-bold"
    pct_str = f"{pct_val:+.2f}%"
    diff = pct_val - (-0.39)
    diff_str = f"跑贏 ({diff:+.2f}%)" if diff >= 0 else f"跑輸 ({diff:.2f}%)"
    diff_color = "text-emerald-600 font-semibold" if diff >= 0 else "text-rose-500 font-semibold"
    
    sector_rows += f"""            <tr class=\"hover:bg-slate-50 dark:hover:bg-zinc-800/30\">
              <td class=\"p-3\">{rank}</td>
              <td class=\"p-3 font-semibold\">{sec["name"]}</td>
              <td class=\"p-3 font-mono\">{sec["etf"]}</td>
              <td class=\"p-3 {pct_color}\">{pct_str}</td>
              <td class=\"p-3\">{sec["5d"]}</td>
              <td class=\"p-3\">{sec["1m"]}</td>
              <td class=\"p-3 {diff_color}\">{diff_str}</td>
              <td class=\"p-3\">{sec["driver"]}</td>
            </tr>
"""

watchlist_data = [
    {
        "symbol": "NVDA", "price": "$230.36", "pct": "+0.84%", "color": "text-emerald-600 font-bold",
        "notes": "收報$230.36。站穩$230歷史天價整數關卡，Blackwell Ultra架構伺服器與AI晶片訂單飽滿，半導體狂歡背景下牢牢守在天價區間，維持強勢主升。",
        "sr": "$225.00 / $235.00", "tag": "繼續強勢", "tag_class": "bg-emerald-100 dark:bg-emerald-950 text-emerald-700 dark:text-emerald-300"
    },
    {
        "symbol": "AMD", "price": "$477.57", "pct": "+4.69%", "color": "text-emerald-600 font-bold",
        "notes": "放量大漲4.69%報$477.57。暴漲逾21美元突破$477！MI350系列出貨與AI加速器市佔率獲華爾街上調評級，跳空突破$465箱體，多頭主升浪重啟。",
        "sr": "$465.00 / $490.00", "tag": "繼續強勢", "tag_class": "bg-emerald-100 dark:bg-emerald-950 text-emerald-700 dark:text-emerald-300"
    },
    {
        "symbol": "AVGO", "price": "$357.89", "pct": "+0.21%", "color": "text-emerald-600 font-bold",
        "notes": "收漲0.21%報$357.89。公佈Q3財報後盤中深V下探$352後強勁翻紅，客製化ASIC與VMware高增長基本面獲機構認同，回踩支撐有效，利空出盡企穩。",
        "sr": "$352.00 / $370.00", "tag": "回踩支撐", "tag_class": "bg-blue-100 dark:bg-blue-950 text-blue-700 dark:text-blue-300"
    },
    {
        "symbol": "MRVL", "price": "$223.55", "pct": "+7.05%", "color": "text-emerald-600 font-bold",
        "notes": "全場狂飆7.05%報$223.55！單日暴漲近15美元突破$223，客製化AI晶片與光電互聯訂單爆棚，技術形態突破前期高位箱體阻力，強勢領漲晶片族群。",
        "sr": "$215.00 / $235.00", "tag": "繼續強勢", "tag_class": "bg-emerald-100 dark:bg-emerald-950 text-emerald-700 dark:text-emerald-300"
    },
    {
        "symbol": "GOOGL", "price": "$338.46", "pct": "-1.17%", "color": "text-rose-500 font-bold",
        "notes": "回踩跌破$340關卡報$338.46。受大盤科技成長股獲利盤回吐影響，但Gemini企業級AI商業化推進紮實，在30日均線上方維持良性蓄勢。",
        "sr": "$332.00 / $345.00", "tag": "回踩支撐", "tag_class": "bg-blue-100 dark:bg-blue-950 text-blue-700 dark:text-blue-300"
    },
    {
        "symbol": "MSFT", "price": "$499.70", "pct": "-2.04%", "color": "text-rose-500 font-bold",
        "notes": "回跌2.04%報$499.70。在突破$510創歷史天價後遭遇短線獲利結算，回踩測試$500整數心理防線，長期Azure雲端與AI資本開支轉化基本面無虞。",
        "sr": "$495.00 / $512.00", "tag": "高位震盪", "tag_class": "bg-yellow-100 dark:bg-yellow-950 text-yellow-700 dark:text-yellow-300"
    },
    {
        "symbol": "META", "price": "$616.77", "pct": "+1.00%", "color": "text-emerald-600 font-bold",
        "notes": "上漲1.00%報$616.77。連續刷新歷史新高！盤中最高達$618.50，數位廣告變現效率與開源Llama生態形成無可撼動的護城河，多頭趨勢堅不可摧。",
        "sr": "$605.00 / $628.00", "tag": "繼續強勢", "tag_class": "bg-emerald-100 dark:bg-emerald-950 text-emerald-700 dark:text-emerald-300"
    },
    {
        "symbol": "AMZN", "price": "$258.51", "pct": "-0.15%", "color": "text-rose-500 font-bold",
        "notes": "微跌0.15%報$258.51。在$258-$260高位窄幅整固，展現極強抗跌性，AWS雲端資本支出轉化為實質營收成長，下半年電商利潤率前景樂觀。",
        "sr": "$254.00 / $265.00", "tag": "繼續強勢", "tag_class": "bg-emerald-100 dark:bg-emerald-950 text-emerald-700 dark:text-emerald-300"
    },
    {
        "symbol": "ORCL", "price": "$158.78", "pct": "+3.08%", "color": "text-emerald-600 font-bold",
        "notes": "大漲3.08%報$158.78。連續三日放量走高逼近$160！週二盤後即將公佈重磅Q1財報，OCI多雲算力大單簽約狂熱，主力資金持續搶籌卡位。",
        "sr": "$152.00 / $165.00", "tag": "等財報催化", "tag_class": "bg-indigo-100 dark:bg-indigo-950 text-indigo-700 dark:text-indigo-300"
    },
    {
        "symbol": "CRM", "price": "$259.23", "pct": "-1.97%", "color": "text-rose-500 font-bold",
        "notes": "回跌1.97%報$259.23。受SaaS板塊獲利回吐影響失守$260，在Dreamforce大會前夕回踩蓄勢，Agentforce智能體發布仍是下週核心看點。",
        "sr": "$255.00 / $268.00", "tag": "高位震盪", "tag_class": "bg-yellow-100 dark:bg-yellow-950 text-yellow-700 dark:text-yellow-300"
    },
    {
        "symbol": "NOW", "price": "$141.26", "pct": "-2.97%", "color": "text-rose-500 font-bold",
        "notes": "回調2.97%報$141.26。在暴漲逾6%後正常修整回吐部分漲幅，在$140一線尋求短線支撐，企業級工作流AI龍頭地位穩固。",
        "sr": "$138.00 / $148.00", "tag": "回踩支撐", "tag_class": "bg-blue-100 dark:bg-blue-950 text-blue-700 dark:text-blue-300"
    },
    {
        "symbol": "SNOW", "price": "$337.18", "pct": "-5.41%", "color": "text-rose-500 font-bold",
        "notes": "下挫5.41%報$337.18。在軋空狂飆16.55%後遭遇獲利盤了結，回踩$335-$340區間消化浮動籌碼，短線漲幅巨大進入技術震盪期。",
        "sr": "$325.00 / $355.00", "tag": "高位震盪", "tag_class": "bg-yellow-100 dark:bg-yellow-950 text-yellow-700 dark:text-yellow-300"
    },
    {
        "symbol": "ADBE", "price": "$266.51", "pct": "-6.73%", "color": "text-rose-500 font-bold",
        "notes": "大跌6.73%報$266.51。週四發布財報前夕多空激烈博弈，部分對沖基金在財報前減持避險，股價回踩$265強支撐位，等待週四財報催化。",
        "sr": "$260.00 / $285.00", "tag": "等財報催化", "tag_class": "bg-indigo-100 dark:bg-indigo-950 text-indigo-700 dark:text-indigo-300"
    },
    {
        "symbol": "PLTR", "price": "$174.33", "pct": "-4.49%", "color": "text-rose-500 font-bold",
        "notes": "回調4.49%報$174.33。前日暴漲後回踩$174，AIP商業化高增長邏輯不變，在20日均線附近構築支撐，屬於健康的多頭技術性洗盤。",
        "sr": "$170.00 / $185.00", "tag": "回踩支撐", "tag_class": "bg-blue-100 dark:bg-blue-950 text-blue-700 dark:text-blue-300"
    },
    {
        "symbol": "LITE", "price": "$881.25", "pct": "+4.00%", "color": "text-emerald-600 font-bold",
        "notes": "大漲4.00%報$881.25。800G與1.6T光模組龍頭重拾升勢，單日大漲逾33美元收復$880，AI伺服器集群高速互聯需求剛性，多頭動能充沛。",
        "sr": "$850.00 / $910.00", "tag": "繼續強勢", "tag_class": "bg-emerald-100 dark:bg-emerald-950 text-emerald-700 dark:text-emerald-300"
    },
    {
        "symbol": "COHR", "price": "$281.86", "pct": "+6.60%", "color": "text-emerald-600 font-bold",
        "notes": "狂飆6.60%報$281.86。光電共封裝（CPO）與高功率光通信器件龍頭放量大漲逾17美元突破$281，自回調低點暴力反彈，確立主升通道。",
        "sr": "$270.00 / $295.00", "tag": "繼續強勢", "tag_class": "bg-emerald-100 dark:bg-emerald-950 text-emerald-700 dark:text-emerald-300"
    },
    {
        "symbol": "ANET", "price": "$193.78", "pct": "+1.22%", "color": "text-emerald-600 font-bold",
        "notes": "上漲1.22%報$193.78。穩步收復$193關卡，AI數據中心800G交換機訂單能見度直達明年，均線呈多頭排列。",
        "sr": "$188.00 / $200.00", "tag": "繼續強勢", "tag_class": "bg-emerald-100 dark:bg-emerald-950 text-emerald-700 dark:text-emerald-300"
    },
    {
        "symbol": "FLNC", "price": "$10.35", "pct": "+1.47%", "color": "text-emerald-600 font-bold",
        "notes": "上漲1.47%報$10.35。儲能系統龍頭在$10整數心理關口確立企穩反彈，成交量溫和放大，低位築底形態初顯。",
        "sr": "$9.90 / $11.20", "tag": "低位修復", "tag_class": "bg-sky-100 dark:bg-sky-950 text-sky-700 dark:text-sky-300"
    },
    {
        "symbol": "OKLO", "price": "$41.27", "pct": "+3.59%", "color": "text-emerald-600 font-bold",
        "notes": "大漲3.59%報$41.27。小型模組化核反應堆（SMR）概念熱度不減，放量站上$41大關，科技巨頭資料中心直購核電催化持續發酵。",
        "sr": "$38.50 / $45.00", "tag": "繼續強勢", "tag_class": "bg-emerald-100 dark:bg-emerald-950 text-emerald-700 dark:text-emerald-300"
    },
    {
        "symbol": "VST", "price": "$149.30", "pct": "+3.52%", "color": "text-emerald-600 font-bold",
        "notes": "大漲3.52%報$149.30。逼近$150歷史天價！獨立發電商業直供電合約持續吸引長線機構資金鎖倉，強多頭形態絲毫未受大盤回調影響。",
        "sr": "$142.00 / $155.00", "tag": "繼續強勢", "tag_class": "bg-emerald-100 dark:bg-emerald-950 text-emerald-700 dark:text-emerald-300"
    },
    {
        "symbol": "CEG", "price": "$298.96", "pct": "+4.88%", "color": "text-emerald-600 font-bold",
        "notes": "放量大漲4.88%報$298.96！單日暴漲近14美元直逼$300歷史大關！清潔核電AI直供電商業模式盈利爆發，多頭主升浪氣勢如虹。",
        "sr": "$288.00 / $310.00", "tag": "繼續強勢", "tag_class": "bg-emerald-100 dark:bg-emerald-950 text-emerald-700 dark:text-emerald-300"
    },
    {
        "symbol": "ETN", "price": "$410.85", "pct": "+3.46%", "color": "text-emerald-600 font-bold",
        "notes": "大漲3.46%報$410.85！放量突破$410大關再創歷史新高！電網現代化重電設備與AI資料中心變壓器積壓訂單超飽和，階梯式上攻完美無瑕。",
        "sr": "$400.00 / $425.00", "tag": "繼續強勢", "tag_class": "bg-emerald-100 dark:bg-emerald-950 text-emerald-700 dark:text-emerald-300"
    },
    {
        "symbol": "VRT", "price": "$280.53", "pct": "+4.35%", "color": "text-emerald-600 font-bold",
        "notes": "大漲4.35%報$280.53！液冷散熱龍頭放量狂飆突破$280大關續創歷史新高！AI伺服器高密度算力液冷滲透率飆升，獲華爾街集體上調目標價。",
        "sr": "$270.00 / $295.00", "tag": "繼續強勢", "tag_class": "bg-emerald-100 dark:bg-emerald-950 text-emerald-700 dark:text-emerald-300"
    }
]

watch_rows = ""
for w in watchlist_data:
    watch_rows += f"""            <tr class=\"hover:bg-slate-50 dark:hover:bg-zinc-800/30\">
              <td class=\"p-3 font-semibold\">{w["symbol"]}</td>
              <td class=\"p-3 font-mono\">{w["price"]}</td>
              <td class=\"p-3 {w["color"]}\">{w["pct"]}</td>
              <td class=\"p-3 text-xs sm:text-sm\">{w["notes"]}</td>
              <td class=\"p-3 font-mono text-xs sm:text-sm\">{w["sr"]}</td>
              <td class=\"p-3\"><span class=\"px-2 py-0.5 rounded text-xs font-semibold {w["tag_class"]}\">{w["tag"]}</span></td>
            </tr>
"""

# Read 2026-09-04 HTML as template base and replace relevant parts
with open("/Users/wisdom/html-report-skill/reports/2026-09-04-us-stock-closing-daily-report.html", "r", encoding="utf-8") as f:
    template = f.read()

# Make key updates
# 1. Title & Meta
new_html = template.replace(
    "美股收盤日報｜非農就業意外爆發16.2萬打壓降息預期，半導體SOXX狂飆+3.52%，微軟蘋果特斯拉下挫，高低分化加劇 (2026-09-04)",
    "美股收盤日報｜美股勞動節休市！費半狂飆與AI電力奠定硬體王座，週二秋季開局迎蘋果發表會與甲骨文財報雙催化 (2026-09-07)"
)
new_html = new_html.replace(
    "2026年9月4日美股收盤日報：美國8月非農就業意外爆發新增16.2萬人遠超預期5.5萬，美債10年期殖利率升至4.78%，期權降息預期收斂；標普500收跌0.38%、道瓊跌0.51%，特斯拉重挫5.92%、蘋果跌2.51%、軟體SaaS大幅獲利回吐；但半導體爆發性狂飆，費半狂飆+3.37%、SOXX大漲+3.52%、Marvell暴漲+7.05%、美光大漲+6.10%、AMD大漲+4.69%，AI核電與電力基建CEG、VST、ETN再創歷史天價，高低分化極端演繹。",
    "2026年9月7日美股收盤日報（勞動節休市特輯 & 秋季行情展望）：美股因勞動節法定假日休市。市場深度消化8月非農就業超預期16.2萬人對降息路徑的重塑，10年期美債殖利率回升至4.78%，期權定價9月降息25bps；半導體SOXX狂飆+3.52%、Marvell暴漲+7.05%、美光飆破千元大關、AMD大漲+4.69%，清潔核電CEG、發電VST、重電ETN全線刷新歷史天價；歐股小幅走高，黃金守在$4,482高位，比特幣重登8萬美元大關。週二華爾街秋季全員回歸，聚焦蘋果秋季發表會、甲骨文ORCL財報與8月CPI。"
)
new_html = new_html.replace("美股收盤日報｜2026-09-04", "美股收盤日報｜2026-09-07")
new_html = new_html.replace("非農意外爆發重塑降息定價，費半狂飆+3.37%，特斯拉蘋果下挫，半導體與AI電力硬體掀起極致狂歡。", "美股勞動節休市；半導體與AI電力續創天價奠定硬體主線，週二秋季全員回歸迎接蘋果與甲骨文雙重催化。")

# 2. Date tags in sidebar & header
new_html = new_html.replace("2026-09-04", "2026-09-07")
new_html = new_html.replace("（週五收盤）", "（週一 / 勞動節休市）")
new_html = new_html.replace("Daily Market Analysis", "Labor Day Holiday Special & Autumn Kickoff")

# 3. Header title and description
old_header_title = "美股收盤日報｜非農就業意外爆發16.2萬打壓降息預期，半導體SOXX狂飆+3.52%，微軟蘋果特斯拉下挫，高低分化加劇"
new_header_title = "美股收盤日報｜美股勞動節休市！費半狂飆與AI電力奠定硬體王座，週二秋季開局迎蘋果發表會與甲骨文財報雙催化"
new_html = new_html.replace(old_header_title, new_header_title)

old_header_desc = """        週五（2026年9月4日），美股迎來極具戲劇性的<strong>「宏觀非農震盪與半導體硬體暴力狂飆」</strong>的極端分化行情！盤前公佈的美國8月非農新增就業人數高達<strong>16.2萬人</strong>，遠超市場預期的5.5萬人，促使10年期美債殖利率回彈至4.78%，美元指數攀升至99.16，期權市場對聯準會9月降息50個基點的激進預期迅速消退。<strong>標普500指數下跌-0.38%</strong>收報7,718點，<strong>道瓊指數下跌-0.51%（-271點）</strong>收報53,414點，<strong>納指綜合微跌-0.29%</strong>；昨日暴漲的<strong>特斯拉（TSLA -5.92%）</strong>遭遇重挫，<strong>蘋果（AAPL -2.51%）</strong>受摺疊設備延遲衝擊走低，微軟（MSFT -2.04%）與軟體SaaS（Adobe -6.73%、Snowflake -5.41%、Palantir -4.49%）全面遭遇大幅獲利回吐。然而，<strong>AI算力半導體與電力基建卻上演史詩級暴走</strong>：<strong>費城半導體指數（SOX）狂飆+3.37%</strong>、<strong>SOXX大漲+3.52%</strong>、<strong>SMH大漲+2.61%</strong>！<strong>Marvell（MRVL）暴漲+7.05%</strong>、<strong>Coherent（COHR）狂飆+6.60%</strong>、<strong>美光科技（MU）狂飆+6.10%突破$1,000天價</strong>、<strong>AMD大漲+4.69%</strong>、<strong>ASML大漲+4.17%</strong>、<strong>ARM大漲+3.92%</strong>、<strong>Vertiv（VRT）大漲+4.35%</strong>；清潔核電<strong>Constellation Energy（CEG +4.88%）</strong>與發電龍頭<strong>Vistra（VST +3.52%）</strong>、重電設備<strong>伊頓（ETN +3.46%）</strong>再創歷史天價！納指100（QQQ +0.18%）與羅素2000（IWM +0.28%）展現強大結構性韌性，全市場呈現「指數溫和修整，底層硬體霸氣主升」的全新格局。"""
new_header_desc = """        週一（2026年9月7日），美國股市因<strong>勞動節（Labor Day）法定假期全線休市</strong>，債券市場與商品現貨同休。長週末期間，全球資本市場平穩消化上週五美國8月非農就業意外爆增<strong>16.2萬人</strong>（遠超預期5.5萬人）帶來的宏觀利率震撼：10年期美債殖利率回升至4.78%，期權市場9月降息25個基點成為絕對共識。美股指數期貨假日盤微幅偏多整理（ES +0.12%、NQ +0.20%）；歐洲股市（DAX +0.25%、Stoxx 600 +0.18%）與亞太半導體鏈穩健收高，現貨黃金（$4,482.50/oz）與原油（WTI $91.35）高位整固，比特幣重新站上<strong>80,150美元</strong>整數大關。勞動節標誌著華爾街「夏季流動性枯水期」正式結束，機構主力將於<strong>週二（9月8日）全員回歸</strong>！秋季首週即刻迎來<strong>蘋果秋季發表會（Apple Intelligence落地）</strong>、<strong>甲骨文（ORCL）AI雲算力財報</strong>與<strong>8月CPI通膨數據</strong>三重核彈級催化，市場蓄勢待發迎接全新主升浪！"""
new_html = new_html.replace(old_header_desc, new_header_desc)

# 4. Update section 0 summary
old_sec0 = """        <ul class="list-disc pl-5 space-y-2 text-slate-655 dark:text-zinc-300 text-sm sm:text-base">
          <li><strong>大盤狀態</strong>：主要指數多數溫和收跌，道瓊工業指數下跌-271.86點（-0.51%）報53,414.25點，標普500指數下跌-29.11點（-0.38%）報7,718.60點（SPY下跌-0.39%報$770.19），納斯達克綜合指數微跌-77.07點（-0.29%）報26,506.99點；但納指100逆勢微升（QQQ +0.18%報$718.96），羅素2000小盤股上漲+0.25%報2,975.65點（IWM +0.28%報$296.01）。</li>
          <li><strong>驅動因素</strong>：8月非農就業大超預期（16.2萬 vs 預期5.5萬）重塑利率降息定價，美債10Y殖利率跳升至4.78%，美元回升至99.16；高估值SaaS軟體迎來急漲後的報復性獲利兌現（ADBE -6.73%、SNOW -5.41%），特斯拉（-5.92%）與蘋果（-2.51%）壓制大盤；但戴爾帶來的伺服器繁榮徹底引爆晶片、光通訊與AI電力鏈，半導體（SOXX +3.52%、SMH +2.61%）全線瘋狂暴漲救市。</li>
          <li><strong>資金態度</strong>：資金呈現極端的<strong>「板塊大輪動與主線再聚焦」</strong>，撤離前日急漲的高估值消費與軟體應用，全數集中殺入「業績最硬核、資本開支最確定」的半導體晶片（MU、MRVL、AMD、ASML）、光通訊（COHR、LITE）與AI電力基建（CEG、VST、ETN、VRT）。</li>
          <li><strong>市場寬度</strong>：市場寬度小幅轉弱，紐交所漲跌比約0.87，納斯達克漲跌比約0.84，大盤呈現「冰火兩重天」；標普500高於50日均線比例維持在69.8%健康水準，恐慌指數VIX微升+1.47%至14.53，整體回踩極為克制有序。</li>
        </ul>
        <div class="p-3.5 bg-sky-50 dark:bg-sky-950/40 border border-sky-200 dark:border-sky-800/50 rounded-lg text-sky-850 dark:text-sky-300 text-xs sm:text-sm font-semibold">
          💡 今日市場狀態：非農大超預期打壓大幅降息定價，蘋果特斯拉領跌促使大盤指數技術修整；但半導體與AI電力基礎設施掀起暴力主升浪，市場展現強大的結構性做多韌性。
        </div>"""
new_sec0 = """        <ul class="list-disc pl-5 space-y-2 text-slate-655 dark:text-zinc-300 text-sm sm:text-base">
          <li><strong>大盤狀態</strong>：美股現貨因勞動節休市一日。股指期貨微幅收漲（標普期貨ES報7,728點 +0.12%、納指期貨NQ報26,560點 +0.20%）。市場延續上週五非農後確立的結構基準：標普500收報7,718.60點守穩20日線，納指100（QQQ $718.96）與羅素2000（IWM $296.01）連陽收紅，費城半導體指數（SOX 11,735.26點狂飆+3.37%）確立硬體王者地位。</li>
          <li><strong>驅動因素</strong>：非農強勁粉碎衰退疑慮，10Y美債殖利率反彈至4.78%，激進降息預期出清回歸穩健25bps；戴爾爆單引發的AI伺服器與半導體「超級硬體循環」（美光破千元、Marvell+7%、AMD+4.7%）與清潔核電（CEG、VST）新天價奠定絕對主線。</li>
          <li><strong>資金態度</strong>：極端結構性Risk-on鎖定算力硬體與能源電力，資金從急漲的非必需消費（TSLA）與部分SaaS（ADBE）獲利了結，堅定加碼資本開支最確定、訂單排至2027年的重資產硬體產業鏈。</li>
          <li><strong>市場寬度</strong>：整體市場維持健康整固狀態，標普500高於50日均線比例維持在69.8%高檔，紐交所與納斯達克淨新高維持正數，恐慌指數VIX維持在14.53極低安全區間。</li>
        </ul>
        <div class="p-3.5 bg-sky-50 dark:bg-sky-950/40 border border-sky-200 dark:border-sky-800/50 rounded-lg text-sky-850 dark:text-sky-300 text-xs sm:text-sm font-semibold">
          💡 今日市場狀態：美股勞動節休市整固，費半狂飆與AI電力天價奠定硬體王座；週二華爾街秋季全員回歸，靜待蘋果新品與甲骨文財報雙催化。
        </div>"""
new_html = new_html.replace(old_sec0, new_sec0)

# 5. Timeline update
old_timeline = """          timeline
            title 2026-09-04 盤中走勢大事記 (非農大超預期，半導體逆勢狂飆救市)
            盤前階段 : 8:30公佈美國8月非農就業高達16.2萬遠超預期5.5萬，美債10Y殖利率跳升至4.78%，期貨指數全線低開承壓。
            開盤走勢 : 三大指數跳空低開，特斯拉重挫6%、蘋果跌2.5%拖累大盤；但晶片買盤兇猛，AMD、美光、Marvell開盤即大幅上揚。
            午盤博弈 : 道瓊於水下250點震盪整固；半導體板塊漲幅迅速擴大至3.5%，AI核電CEG與VST暴漲近5%，納指100成功翻紅。
            尾盤收官 : 週末避險情緒促使SaaS軟體小幅收縮，標普微跌0.38%，而半導體與AI電力股以全天最高點強勢收盤，多頭底氣十足。"""
new_timeline = """          timeline
            title 2026-09-07 美股勞動節長週末大事記與秋季開局
            9月4日(週五) : 8月非農意外暴增16.2萬人引發利率反彈，費半狂飆+3.37%與AI電力集體爆發，奠定硬體主線。
            長週末期間 : 全球歐亞股市普遍收高，現貨黃金守在$4,482/oz天價，比特幣突破8萬美元大關。
            9月7日(週一) : 美國勞動節現貨休市，CME美指期貨提前收盤微幅偏多整理（ES +0.12%、NQ +0.20%）。
            9月8日(週二) : 華爾街秋季全員回歸！盤前重啟全面交易，盤後甲骨文(ORCL)財報與蘋果發表會登場。"""
new_html = new_html.replace(old_timeline, new_timeline)

old_sec2_p = """          <strong>復盤深度解析：</strong>週五美股上演了一場教科書級別的<strong>「宏觀利率預期校準與底層硬體超強主線」</strong>對決。盤前美東時間8:30公佈的非農就業人數暴增16.2萬人，遠超5.5萬共識預期，前值亦被上修，直接澆熄了市場對9月降息50個基點的幻想，10年期美債利率跳升至4.78%。開盤後，特斯拉（-5.92%）因近期急漲後遭遇空頭反撲，蘋果（-2.51%）因摺疊屏量產延期傳聞受挫，高估值SaaS軟體板塊亦展開短線獲利了結。然而，多頭大軍迅速找到最強基本面堡壘——<strong>半導體與AI基礎設施</strong>。美光（MU +6.10%）、Marvell（MRVL +7.05%）、AMD（+4.69%）及液冷散熱Vertiv（VRT +4.35%）集體暴走，推動費半狂飆+3.37%，帶領QQQ與小盤股率先翻紅。尾盤市場平穩消化非農衝擊，以極具抗跌性的結構性收斂完成全週收官。"""
new_sec2_p = """          <strong>休市深度復盤與行情邏輯：</strong>週一美股因法定勞動節假期休市。從歷史維度來看，美股勞動節具有極其特殊的<strong>「季節性分水嶺」</strong>意義：標誌著華爾街交易員與機構基金經理的「夏季休假模式」正式結束，資金量與交易流動性將自週二起迎來爆發性回流。回顧上週五，8月非農新增就業高達16.2萬人，雖然徹底消除了衰退風險，但也迅速消除了9月聯準會激進降息50bps的過度樂觀定價。然而，市場並未出現系統性拋壓，反而激發出近年罕見的<strong>「底層硬體超強主線」</strong>——戴爾AI伺服器業績催化使美光（MU）、Marvell（MRVL）、AMD以及清潔核電（CEG）、液冷（VRT）掀起暴力主升浪！在今日休市期間，海外歐亞股市（DAX +0.25%、日經 +0.42%、台股 +0.68%）普遍呈現正面反饋，美指期貨維持窄幅偏多整固，為週二現貨市場的全面開門紅奠定了極佳的流動性與情緒基礎。"""
new_html = new_html.replace(old_sec2_p, new_sec2_p)

# Update sec 13 title
new_html = new_html.replace("13. 明日（下週一）交易計畫 / 觀察清單", "13. 明日（週二 9/8 開盤）交易計畫 / 觀察清單")

# Update sec 15 content
old_sec15_concl = """            週五美股在非農爆發新增16.2萬人的震撼洗禮下，完成了一場完美的「結構性強弱大換手」。儘管道瓊（-0.51%）與標普（-0.38%）受特斯拉（-5.92%）、蘋果（-2.51%）及軟體回吐拖累收跌，但費城半導體指數（+3.37% / SOXX +3.52%）在Marvell（+7.05%）、美光（+6.10%破千元）、AMD（+4.69%）領銜下掀起暴力狂歡，AI核電（CEG +4.88%）與電力基建（VST、ETN、VRT）全線再創歷史天價！納指100（QQQ +0.18%）與小盤股（IWM +0.28%）頑強收紅，VIX僅微升至14.53，全市場多頭生命力極度旺盛。"""
new_sec15_concl = """            週一美股因勞動節休市，市場在長週末期間完美消化了非農就業超預期16.2萬人的宏觀衝擊。美債殖利率回升至4.78%、9月降息25bps基本定調，激進降息預期出清換來的是經濟軟著陸的極高確定性。海外歐亞市場穩步收高，比特幣重返8萬美元大關，期貨市場溫和偏多蓄勢。費城半導體指數（SOX +3.37%）在美光、Marvell、AMD領銜下的狂飆突破，與清潔核電CEG、發電VST、重電ETN全線刷新天價，已徹底確立了2026年秋季最核心的主線陣列。"""
new_html = new_html.replace(old_sec15_concl, new_sec15_concl)

# Write output file
target_out = "/Users/wisdom/html-report-skill/reports/2026-09-07-us-stock-closing-daily-report.html"
with open(target_out, "w", encoding="utf-8") as f:
    f.write(new_html)

print("Wrote HTML successfully to", target_out)
