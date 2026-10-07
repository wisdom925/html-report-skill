import re
s = open("scratch/gen_1006_stage.py", encoding="utf-8").read()
def sub(a, b):
    global s
    assert a in s, a[:50]
    s = s.replace(a, b)
# 13
a = s.index('s13 = sec(13'); b = s.index('# ---------- sec 14 risk')
s = s[:a] + r"""s13 = sec(13, "明日交易計畫 / 觀察清單", f'''<div class="space-y-4">
  <div class="{BOX}"><h3 class="font-semibold mb-2">13.1 宏觀觀察</h3><ul class="list-disc pl-5 text-sm space-y-1"><li>10年期殖利率能否守在5.30%下方（今日高5.30%、收5.27%）；30年期5.64%。</li><li>WTI ${PX("CL=F")} / Brent ${PX("BZ=F")} 走勢。</li><li>10/7（週三）FOMC會議紀要與Fed官員講話；美元（UUP）{PC("UUP")}。</li><li>VIX 能否維持15附近。</li></ul></div>
  <div class="{BOX}"><h3 class="font-semibold mb-2">13.2 大盤觀察</h3><p class="text-sm">SPY：壓力 781.6（今日高）、支撐 778.0（今日低）。QQQ：壓力 762.9、支撐 759.1。IGV（{PX("IGV")}，近5日 +5.7%）與 IWM（{PX("IWM")}，今日 {PC("IWM")}）是否改善是寬度確認指標。</p></div>
  <div class="{BOX}"><h3 class="font-semibold mb-2">13.3 板塊與個股觀察</h3><p class="text-sm">CEG、VST、NRG（電力股大漲後是否續強或獲利回吐）；PWR、GEV、ETN（電力基建）；MRVL、AVGO、ANET（客製晶片/網通）；NVDA、MU（高位整理）；LITE、COHR（光通訊擁擠）；CRM（軟體最弱）；STZ（盤後財報反應）；APLD（10/7財報）；LEVI、PEP、PGR（財報）；IWM（小型股走弱）；FLNC、OKLO（弱勢是否止穩）。</p></div></div>''')

""" + s[b:]
sub('("宏觀利率", "高", "10年期5.31%、30年期5.66%處多年高位；市場仍定價約18%升息機率")', '("宏觀利率", "中高", "10年期5.27%、30年期5.64%雖自高位回落，仍處多年高位；12月升息據報導仍有定價")')
sub('"近1月RSP -2.6%、IWM -3.8%落後SPY +1.2%，指數創高依賴大型股"', '"近1月RSP -3.1%、IWM -5.0%落後SPY +1.2%，今日羅素2000 -0.59%，指數創高依賴大型股"')
sub('"SMH RSI 88、LITE/COHR 5日漲約18%，高位波動放大"', '"SMH RSI 87、LITE/COHR 5日漲約16%，電力股單日大漲10%以上，高位波動放大"')
sub('"Q3財報季尚未全面展開，本週以消費財報為主"', '"Q3財報季尚未全面展開；STZ 盤後財報反應偏弱，本週以消費財報為主"')
sub('"Brent 約$100，油價單日大幅波動"', '"Brent 約$101，油價維持高位"')
sub("標普500收 {PX(\"^GSPC\")}（{PC(\"^GSPC\")}）、納指收 {PX(\"^IXIC\")}（{PC(\"^IXIC\")}）創收盤新高，AI龍頭領漲，併購與原油回落提供支撐；10年期殖利率5.31%與偏高擁擠度是主要制約。",
    "標普500收 {PX(\"^GSPC\")}（{PC(\"^GSPC\")}）、納指收 {PX(\"^IXIC\")}（{PC(\"^IXIC\")}）雙創收盤新高，殖利率回落（10年期5.27%）與AI基礎設施題材（電力、客製晶片、網通）支撐；小型股走弱與超買擁擠是主要制約。")
sub("10年期殖利率是否突破5.35%。", "10年期殖利率能否守住5.30%下方。")
sub("NVDA 與費半能否在超買下守住漲幅。", "電力股（CEG、VST）大漲後是否續強或回吐；費半在超買下能否守住。")
sub("IWM、RSP 是否追上SPY，改善寬度。", "IWM 能否止跌，改善寬度。")
sub("WTI/Brent 油價與美元（UUP）方向。", "STZ 盤後反應與 MRVL/AVGO 客製晶片題材延續性。")
sub("AI龍頭與電力股值得關注，小盤與房地產需謹慎。", "AI電力、客製晶片與網通值得關注（但單日大漲後波動放大），小型股與醫療保健需謹慎。")
sub("Yahoo Finance、Reuters、Bloomberg/BNN、Investing.com、ISM、公司新聞稿", "Yahoo Finance、公開新聞報導（Morningstar、Benzinga、Investing.com 等）、美國普查局/BEA、公司新聞稿")
sub("新聞與經濟數據取自公開報導（Reuters/Bloomberg/BNN、Investing.com、ForexFactory、公司新聞稿）", "新聞與經濟數據取自公開報導（Benzinga、Investing.com、Morningstar、Census/BEA、公司新聞稿）")
sub('"繼續強勢": "bg-emerald-100 text-emerald-700"', '"繼續強勢": "bg-emerald-100 text-emerald-700"')
s = s.replace("10-05", "10-06")
open("generate_report_20261006.py", "w", encoding="utf-8").write(s)
