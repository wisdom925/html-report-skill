import os
import subprocess
import sys

html_content = """<!doctype html>
<html lang="zh-TW" class="scroll-smooth">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <title>美股收盤日報｜AI資本支出疑慮引爆科技股大拋售，雙雄財報後特斯拉暴跌14.5%，標普創月內最大單日跌幅！</title>
  <meta name="description" content="2026年7月23日美股收盤日報：Alphabet與特斯拉業績引發AI資本支出回報率質疑，特斯拉崩跌14.5%，谷歌大跌7.13%，拖累科技板塊大幅下挫。中東局勢再起推升油價突破100美元，10年期美債收益率飆升至4.71%的2026年新高。三大指數重挫，標普跌1.21%，納指重挫2.15%，VIX恐慌指數飆升13.7%至18.92。洛克希德馬丁（+10.54%）與RTX（+7.5%）逆市上揚護盤。">
  <meta property="og:title" content="美股收盤日報｜2026-07-23">
  <meta property="og:description" content="AI資本支出擔憂疊加債息及原油雙升，大盤重挫，特斯拉大跌14.5%，防禦及國防板塊逆市護盤。">
  <meta property="og:type" content="article">

  <!-- Tailwind CSS & Dark Mode -->
  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config = {
      darkMode: 'class',
      theme: {
        extend: {
          colors: {
            brand: {
              50: '#f0f9ff',
              100: '#e0f2fe',
              550: '#0284c7',
              600: '#0369a1',
              700: '#075985',
            }
          },
          fontFamily: {
            sans: ['Inter', 'Outfit', 'system-ui', 'sans-serif']
          }
        }
      }
    };
    if (localStorage.theme === 'dark' || (!('theme' in localStorage) && matchMedia('(prefers-color-scheme: dark)').matches)) {
      document.documentElement.classList.add('dark');
    }
  </script>

  <!-- Highlight.js for Code Syntax -->
  <link id="hljs-theme" rel="stylesheet" href="https://cdn.jsdelivr.net/gh/highlightjs/cdn-release@11/build/styles/github-dark.min.css">
  <script src="https://cdn.jsdelivr.net/gh/highlightjs/cdn-release@11/build/highlight.min.js"></script>

  <!-- Chart.js -->
  <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>

  <!-- Mermaid.js for Diagrams -->
  <script type="module">
    import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs';
    const isDark = document.documentElement.classList.contains('dark');
    mermaid.initialize({ startOnLoad: true, theme: isDark ? 'dark' : 'default', securityLevel: 'loose' });
    window.__mermaid = mermaid;
  </script>

  <!-- KaTeX for Equations -->
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.10/dist/katex.min.css">
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.10/dist/katex.min.js"></script>
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.10/dist/contrib/auto-render.min.js"
    onload='renderMathInElement(document.body, { delimiters: [
      {left:"$$",right:"$$",display:true},
      {left:"$",right:"$",display:false},
      {left:"\\\\(",right:"\\\\)",display:false},
      {left:"\\\\[",right:"\\\\]",display:true}
    ]})'></script>

  <style>
    @media (prefers-reduced-motion: reduce) { * { animation: none !important; transition: none !important; } }
    @media print {
      .no-print { display: none !important; }
      body { color: #000; background: #fff; }
      a { color: inherit; text-decoration: underline; }
      details { display: block; } details > summary { display: none; }
    }
    pre code.hljs { border-radius: .5rem; padding: 1rem; font-size: .85rem; }
    details > summary { cursor: pointer; user-select: none; }
    details > summary::marker { content: "▸ "; }
    details[open] > summary::marker { content: "▾ "; }
    .toc a { display: block; padding: .25rem 0; opacity: .6; transition: opacity .15s; border-left: 2px solid transparent; padding-left: 0.75rem; }
    .toc a:hover, .toc a.active { opacity: 1; }
    .toc a.active { font-weight: 600; border-color: #0284c7; color: #0284c7; }
    .copy-btn { position: absolute; top: .5rem; right: .5rem; }
    pre.has-copy { position: relative; }

    /* Tab pattern: pure CSS, no JS */
    .tabs > input[type="radio"] { display: none; }
    .tabs > label { cursor: pointer; padding: .5rem 1rem; border-bottom: 2px solid transparent; font-weight: 500; color: #71717a; transition: all 0.2s; }
    .tabs > input:checked + label { border-color: #0284c7; color: #0284c7; font-weight: 600; }
    .tabs > .tab-panel { display: none; padding-top: 1rem; }
    .tabs > input:nth-of-type(1):checked ~ .tab-panel:nth-of-type(1),
    .tabs > input:nth-of-type(2):checked ~ .tab-panel:nth-of-type(2),
    .tabs > input:nth-of-type(3):checked ~ .tab-panel:nth-of-type(3),
    .tabs > input:nth-of-type(4):checked ~ .tab-panel:nth-of-type(4) { display: block; }
    
    .dark .toc a.active { border-color: #38bdf8; color: #38bdf8; }
    .dark .tabs > input:checked + label { border-color: #38bdf8; color: #38bdf8; }
  </style>
</head>

<body class="bg-slate-50 dark:bg-zinc-950 text-zinc-900 dark:text-zinc-100 font-sans antialiased">

<!-- Floating controls -->
<div class="fixed top-4 right-4 z-50 flex gap-2 no-print">
  <button id="theme-toggle" class="px-3 py-1.5 rounded-lg border border-zinc-200 dark:border-zinc-800 bg-white/80 dark:bg-zinc-900/80 backdrop-blur text-sm hover:bg-zinc-100 dark:hover:bg-zinc-800 font-medium shadow-sm transition-colors">
    ☼ / ☾
  </button>
  <button onclick="window.print()" class="px-3 py-1.5 rounded-lg border border-zinc-200 dark:border-zinc-800 bg-white/80 dark:bg-zinc-900/80 backdrop-blur text-sm hover:bg-zinc-100 dark:hover:bg-zinc-800 font-medium shadow-sm transition-colors">
    Print
  </button>
</div>

<div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12 lg:grid lg:grid-cols-[220px_minmax(0,1fr)] lg:gap-12">

  <!-- Sticky TOC -->
  <nav class="toc lg:sticky lg:top-12 self-start text-sm mb-8 lg:mb-0 no-print space-y-1 bg-white dark:bg-zinc-900 p-4 rounded-xl border border-zinc-200 dark:border-zinc-800 shadow-sm">
    <div class="font-bold mb-3 text-zinc-400 dark:text-zinc-500 uppercase tracking-wider text-xs">報告目錄</div>
    <a href="#summary" class="active">0. 今日一句話總結</a>
    <a href="#market-overview">1. 大盤表現總覽</a>
    <a href="#timeline">2. 盤中走勢復盤</a>
    <a href="#macro">3. 宏觀環境 (Tabs)</a>
    <a href="#sectors">4. 板塊表現 (Table)</a>
    <a href="#themes">5. 主題與風格表現</a>
    <a href="#breadth">6. 市場寬度與參與度</a>
    <a href="#technical">7. 技術面分析</a>
    <a href="#stocks">8. 重點個股異動 (Details)</a>
    <a href="#earnings">9. 財報日曆與解讀</a>
    <a href="#institution">10. 機構觀點與資金流</a>
    <a href="#rotation">11. 板塊輪動判斷</a>
    <a href="#watchlist">12. 重點關注股觀察</a>
    <a href="#trading-plan">13. 明日交易計畫</a>
    <a href="#risks">14. 風險提示</a>
    <a href="#conclusion">15. 最終結論</a>
  </nav>

  <main class="min-w-0 bg-white dark:bg-zinc-900 p-6 sm:p-8 rounded-2xl border border-zinc-200 dark:border-zinc-800 shadow-sm">

    <!-- Header -->
    <header class="mb-12 border-b border-zinc-100 dark:border-zinc-800 pb-8">
      <div class="flex items-center gap-2 mb-3">
        <span class="px-2.5 py-1 text-xs font-semibold rounded-full bg-rose-50 text-rose-650 dark:bg-rose-950/50 dark:text-rose-450">AI支出疑慮 & 債息油價雙飆</span>
        <span class="text-sm text-zinc-400">•</span>
        <time class="text-sm font-semibold text-zinc-500 dark:text-zinc-400">2026-07-23</time>
      </div>
      <h1 class="text-3xl sm:text-4xl font-extrabold tracking-tight mb-4 bg-gradient-to-r from-zinc-900 to-zinc-700 dark:from-zinc-100 dark:to-zinc-400 bg-clip-text text-transparent">
        美股收盤日報｜AI資本支出疑慮引爆科技股大拋售，雙雄財報後特斯拉暴跌14.5%，標普創月內最大單日跌幅！
      </h1>
      <p class="text-lg text-zinc-500 dark:text-zinc-400 leading-relaxed">
        週四（2026年7月23日），美股遭遇一個月來最慘烈單日拋售，三大指數全線重挫。Alphabet與特斯拉公佈的Q2財報引發市場對AI龐大資本支出回報率（ROI）的集體焦慮。特斯拉因利潤率嚴重承壓崩跌14.52%，Alphabet跌7.13%，拖累科技與晶片板塊大幅下挫。同時，中東局勢再起推升布蘭特原油重返100美元之上，加上10年期美債收益率飆升至4.71%的2026年新高，通膨隱憂與高利率壓力令風險資產全面失血。標普500指數跌1.21%，納指重挫2.15%，VIX恐慌指數飆升13.70%至18.92。防禦性板塊及公佈超預期業績的國防巨頭洛克希德馬丁（+10.54%）與RTX（+7.5%）逆市大漲護盤。
      </p>
    </header>

    <!-- 0. 今日一句話總結 -->
    <section id="summary" class="mb-12 scroll-mt-6">
      <h2 class="text-2xl font-bold mb-4 flex items-center gap-2 border-b border-zinc-100 dark:border-zinc-800 pb-2">
        <span class="text-brand-500">0.</span> 今日一句話總結
      </h2>
      <div class="bg-zinc-50/50 dark:bg-zinc-900/50 p-6 rounded-2xl border border-zinc-200/60 dark:border-zinc-800/60 leading-relaxed text-zinc-700 dark:text-zinc-300">
        <ul class="list-disc pl-5 space-y-3">
          <li><strong>大盤狀態：</strong>美股多頭大舉潰退，三大指數開低走低，終結先前短暫反彈。標普500指數重挫1.21%失守7,450點並跌破關鍵20日均線，納指暴跌2.15%，創近一個月來最大單日跌幅。</li>
          <li><strong>驅動因素：</strong>特斯拉與谷歌兩大權重股業績爆冷，市場對龐大AI資本支出的回報速度產生強烈質疑；另外，中東紅海衝突加劇導致油價重返100美元上方，且10年期美債收益率飆升至4.71%高點，宏觀與微觀利空共振引發恐慌。</li>
          <li><strong>資金流向：</strong>高貝塔成長板塊（科技、半導體算力、可選消費）資金大幅流出，去槓桿壓力顯著。避險資金流向能源股、防禦性醫藥股以及公佈極佳業績且調升指引的國防巨頭（LMT、RTX），令工業板塊逆市走高。</li>
          <li><strong>市場寬度：</strong>市場參與度顯著惡化，上漲與下跌家數比例接近1:3，高於短期均線的個股比例迅速回落，反映市場整體賺錢效應受到大市值科技股崩跌的劇烈衝擊。</li>
          <li><strong>一句話判斷：</strong><span class="text-rose-500 font-semibold dark:text-rose-400">AI投資利潤質疑重創科技估值，債息油價雙升加劇宏觀通膨隱憂，資金全面撤向防禦防衛與大宗商品。</span></li>
        </ul>
      </div>
    </section>

    <!-- 1. 大盤表現總覽 -->
    <section id="market-overview" class="mb-12 scroll-mt-6">
      <h2 class="text-2xl font-bold mb-4 flex items-center gap-2 border-b border-zinc-100 dark:border-zinc-800 pb-2">
        <span class="text-brand-500">1.</span> 大盤表現總覽
      </h2>
      
      <div class="overflow-x-auto border border-zinc-200 dark:border-zinc-800 rounded-xl mb-6">
        <table class="min-w-full divide-y divide-zinc-200 dark:divide-zinc-850 text-sm">
          <thead class="bg-zinc-50 dark:bg-zinc-900">
            <tr class="text-zinc-550 dark:text-zinc-400 text-left">
              <th class="px-4 py-3 font-semibold">指數/ETF 名稱</th>
              <th class="px-4 py-3 text-right font-semibold">當前收盤點位</th>
              <th class="px-4 py-3 text-right font-semibold">單日漲跌幅</th>
              <th class="px-4 py-3 text-right font-semibold">單日漲跌點數/價格</th>
              <th class="px-4 py-3 text-right font-semibold">技術與走勢狀態</th>
            </tr>
          </thead>
          <tbody class="divide-y divide-zinc-200 dark:divide-zinc-850 font-mono text-zinc-700 dark:text-zinc-300">
            <tr>
              <td class="px-4 py-3 font-semibold font-sans text-zinc-900 dark:text-zinc-100">Dow Jones (道瓊)</td>
              <td class="px-4 py-3 text-right">51,711.65</td>
              <td class="px-4 py-3 text-right text-rose-500 font-semibold">-0.97%</td>
              <td class="px-4 py-3 text-right text-rose-500 font-semibold">-506.93</td>
              <td class="px-4 py-3 font-sans text-xs text-rose-500 font-semibold">跌破均線。受科技股拖累低開，雖然LMT（+10.54%）與RTX（+7.5%）暴漲支撐工業權重，但仍跌破10日均線，跌幅限制在1%以內。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold font-sans text-zinc-900 dark:text-zinc-100">S&P 500 (標普 500)</td>
              <td class="px-4 py-3 text-right">7,408.30</td>
              <td class="px-4 py-3 text-right text-rose-500 font-semibold">-1.21%</td>
              <td class="px-4 py-3 text-right text-rose-500 font-semibold">-90.66</td>
              <td class="px-4 py-3 font-sans text-xs text-rose-500 font-semibold">多頭受挫。失守7,450點及20日均線（7485點），短期趨勢走弱，面臨回測50日均線（約7,321點）的支撐壓力。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold font-sans text-zinc-900 dark:text-zinc-100">Nasdaq Composite (納斯達克)</td>
              <td class="px-4 py-3 text-right">25,137.69</td>
              <td class="px-4 py-3 text-right text-rose-500 font-semibold">-2.15%</td>
              <td class="px-4 py-3 text-right text-rose-500 font-semibold">-553.21</td>
              <td class="px-4 py-3 font-sans text-xs text-rose-500 font-semibold">強烈去槓桿。Alphabet大跌7%與特斯拉暴跌14.5%引發科技板塊巨震，指數跌穿50日均線，短期技術形態嚴重受損。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold font-sans text-zinc-900 dark:text-zinc-100">QQQ (納指 100 ETF)</td>
              <td class="px-4 py-3 text-right">691.96</td>
              <td class="px-4 py-3 text-right text-rose-500 font-semibold">-1.90%</td>
              <td class="px-4 py-3 text-right text-rose-500 font-semibold">-13.39</td>
              <td class="px-4 py-3 font-sans text-xs text-rose-500 font-semibold">重回整理。跌穿短期均線平台，直接跌破700美元心理大關，RSI指標跌至41，進入短期偏空震盪區。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold font-sans text-zinc-900 dark:text-zinc-100">Russell 2000 (羅素 2000 ETF / IWM)</td>
              <td class="px-4 py-3 text-right">293.48</td>
              <td class="px-4 py-3 text-right text-rose-500 font-semibold">-0.54%</td>
              <td class="px-4 py-3 text-right text-rose-500 font-semibold">-1.60</td>
              <td class="px-4 py-3 font-sans text-xs text-rose-500 font-semibold">相對堅韌。受10年期債息創高壓制，但小盤股並未遭遇恐慌踩踏，依然守穩在20日均線之上。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold font-sans text-zinc-900 dark:text-zinc-100">SOXX (費半半導體 ETF)</td>
              <td class="px-4 py-3 text-right">546.01</td>
              <td class="px-4 py-3 text-right text-rose-500 font-semibold">-1.71%</td>
              <td class="px-4 py-3 text-right text-rose-500 font-semibold">-9.48</td>
              <td class="px-4 py-3 font-sans text-xs text-rose-500 font-semibold">大舉回吐。費城半導體指數（SOX）收跌0.54%至12,343.84點，晶片股遭遇利多兌現拋售，測試50日均線支撐。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold font-sans text-zinc-900 dark:text-zinc-100">VIX 波動率指數 (反向對比)</td>
              <td class="px-4 py-3 text-right">18.92</td>
              <td class="px-4 py-3 text-right text-emerald-500 font-semibold">+13.70%</td>
              <td class="px-4 py-3 text-right text-emerald-500 font-semibold">+2.28</td>
              <td class="px-4 py-3 font-sans text-xs text-emerald-500 font-semibold">恐慌飆升。市場避險情緒大幅升溫，VIX創下一個月來收盤新高，顯示多空分歧與短期對沖需求急升。</td>
            </tr>
          </tbody>
        </table>
      </div>

      <div class="h-80 w-full mb-6">
        <canvas id="returnsChart"></canvas>
      </div>
    </section>

    <!-- 2. 盤中走勢復盤 -->
    <section id="timeline" class="mb-12 scroll-mt-6">
      <h2 class="text-2xl font-bold mb-4 flex items-center gap-2 border-b border-zinc-100 dark:border-zinc-800 pb-2">
        <span class="text-brand-500">2.</span> 當日走勢復盤 (2026-07-23)
      </h2>
      
      <div class="mb-6">
        <div class="mermaid py-4 bg-zinc-50 dark:bg-zinc-950/40 rounded-xl border border-zinc-200 dark:border-zinc-800 flex justify-center">
          timeline
            title 2026-07-23 AI資本支出隱憂與油價飆升衝擊時間線
            盤前交易 : 科技雙雄財報引發避險情绪。Alphabet與特斯拉季報後股價大幅低開。LMT與RTX公佈強勁財報，股價大漲。
            開盤階段 (09:30 - 11:30) : 三大指數低開，納指在特斯拉和谷歌拖累下迅速下探。防禦性工業股、國防板塊逆市上揚。
            盤中走勢 (11:30 - 14:00) : 地緣政治局勢緊張。布蘭特原油狂飆突破100美元。10年期美債收益率升至4.71%的高點，科技股估值進一步承壓。
            尾盤階段 (14:00 - 16:00) : 避險資金加速撤離高估值科技板塊。三大指數跌幅擴大，標普500失守7,450點。VIX恐慌指數飆升。
            盤後市場 : 部分半導體及軟體股在盤後維持震盪整理。市場等待次日的重要通膨數據。
        </div>
      </div>

      <div class="bg-zinc-50/50 dark:bg-zinc-900/50 p-6 rounded-2xl border border-zinc-200/60 dark:border-zinc-800/60 text-sm leading-relaxed text-zinc-700 dark:text-zinc-300">
        <p class="mb-3"><strong>盤面主線解讀：</strong></p>
        <p>週四美股呈現顯著的「科技避險、實體護盤」行情。特斯拉與谷歌兩大科技巨頭週三盤後公佈財報，引爆了整個AI硬體與軟體板塊的去槓桿踩踏。特斯拉因銷量利潤被壓縮且AI資本開支龐大，導致利潤率顯著下降，開盤即遭機構清倉式拋售；Alphabet雖然整體表現不俗，但同樣因為調高AI投資CapEx指引而遭到股價打壓。盤中，地緣政治的突然惡化（中東對紅海油輪的襲擊）導致原油突破100美元關關，進一步推升了市場對通膨重重及聯準會延後降息的憂慮，10年期債息升破4.7%創出年度新高，壓垮了科技股的最後防線。所幸，防禦性板塊（醫藥、公用）和國防板塊表現極佳，才使得道瓊與標普的跌幅在尾盤並未演變成系統性崩潰。</p>
      </div>
    </section>

    <!-- 3. 宏觀環境 -->
    <section id="macro" class="mb-12 scroll-mt-6">
      <h2 class="text-2xl font-bold mb-4 flex items-center gap-2 border-b border-zinc-100 dark:border-zinc-800 pb-2">
        <span class="text-brand-500">3.</span> 宏觀環境 (Tabs)
      </h2>
      
      <div class="tabs flex flex-wrap border-b border-zinc-200 dark:border-zinc-850">
        <input type="radio" id="tab-yield" name="macro-tabs" checked>
        <label for="tab-yield">3.1 美債收益率</label>
        
        <input type="radio" id="tab-fed" name="macro-tabs">
        <label for="tab-fed">3.2 Fed 降息預期</label>
        
        <input type="radio" id="tab-fx" name="macro-tabs">
        <label for="tab-fx">3.3 商品與加密貨幣</label>
        
        <input type="radio" id="tab-data" name="macro-tabs">
        <label for="tab-data">3.4 當日重要數據解讀</label>

        <!-- Tab Panel 1 -->
        <div class="tab-panel w-full text-sm leading-relaxed text-zinc-650 dark:text-zinc-350">
          <div class="bg-zinc-50 dark:bg-zinc-900/40 p-5 rounded-xl border border-zinc-200 dark:border-zinc-800">
            <h4 class="font-bold text-zinc-800 dark:text-zinc-200 mb-2">通膨預期抬頭，美債收益率創2026年新高</h4>
            <p class="mb-2">受油價飆升及地緣局勢引發的通膨預期回升影響，美國債市遭遇拋售，收益率大幅上行：</p>
            <ul class="list-disc pl-5 space-y-2">
              <li><strong>2年期美債收益率：</strong>報 <span class="font-semibold text-rose-500">4.95%</span>，逼近5.0%警戒線。</li>
              <li><strong>10年期美債收益率：</strong>大漲至 <span class="font-semibold text-rose-500">4.71%</span>，創下2026年以來的最高水平。</li>
            </ul>
            <p class="mt-2"><strong>市場含義：</strong>10年期美債收益率是全球風險資產的「定價之錨」。債息飆升令高估值的科技成長股首當其衝。在市場對科技巨頭AI龐大支出的回報周期（ROI）產生懷疑時，折現率的上升無疑加劇了資金向防禦性與實體低估值板塊撤退的步伐。</p>
          </div>
        </div>

        <!-- Tab Panel 2 -->
        <div class="tab-panel w-full text-sm leading-relaxed text-zinc-650 dark:text-zinc-350">
          <div class="bg-zinc-50 dark:bg-zinc-900/40 p-5 rounded-xl border border-zinc-200 dark:border-zinc-800">
            <h4 class="font-bold text-zinc-800 dark:text-zinc-200 mb-2">9月降息機率有所鬆動，但防禦性降息基調仍在</h4>
            <p class="mb-2">聯準會7月份決議前夕，油價與通膨預期的意外升溫令短期降息機率出現小幅波動：</p>
            <ul class="list-disc pl-5 space-y-2">
              <li><strong>7月FOMC利率決議：</strong>維持基準利率不變的機率升至 <strong>98.0%</strong>，基本無懸念。</li>
              <li><strong>9月降息預期：</strong>降息25個基點的概率回落至 <strong>68.0%</strong>（先前為76%），反映出大宗商品走高令美聯儲立場再度面臨考驗。</li>
            </ul>
            <p class="mt-2"><strong>解讀：</strong>市場對於聯準會能否在下半年順暢開啟防禦性降息週期的信心有所減弱。油價破100美元是最大宏觀變數，若油價維持高位，則聯準會在9月或11月啟動降息的路徑可能會受到阻礙，這是科技板塊面臨的又一重打擊。</p>
          </div>
        </div>

        <!-- Tab Panel 3 -->
        <div class="tab-panel w-full text-sm leading-relaxed text-zinc-650 dark:text-zinc-350">
          <div class="bg-zinc-50 dark:bg-zinc-900/40 p-5 rounded-xl border border-zinc-200 dark:border-zinc-800">
            <h4 class="font-bold text-zinc-800 dark:text-zinc-200 mb-2">原油重返100美元關口，避險美元走強，比特幣承壓</h4>
            <ul class="list-disc pl-5 space-y-2">
              <li><strong>美元指數 (DXY)：</strong>反彈至 <strong>101.48</strong>，避險情緒和債息走高雙重支撐美元。</li>
              <li><strong>原油 (Brent)：</strong>暴漲逾4%收在 <strong>$100.20/桶</strong>，兩個月來首次破百。中東緊張局勢升級，紅海油輪遭遇導彈襲擊引發供應中斷擔憂。</li>
              <li><strong>黃金現貨：</strong>微幅整理，收報 <strong>$4,118/盎司</strong>。避險買盤抵消了強美元和高利率帶來的壓制。</li>
              <li><strong>比特幣 (BTC)：</strong>下跌至 <strong>$65,120</strong>，跟隨美股科技股等高風險資產出現流出。</li>
            </ul>
          </div>
        </div>

        <!-- Tab Panel 4 -->
        <div class="tab-panel w-full text-sm leading-relaxed text-zinc-650 dark:text-zinc-350">
          <div class="bg-zinc-50 dark:bg-zinc-900/40 p-5 rounded-xl border border-zinc-200 dark:border-zinc-800">
            <h4 class="font-bold text-zinc-800 dark:text-zinc-200 mb-2">初請失業金人數符合預期，市場完全聚焦微觀財報與油價</h4>
            <p class="mb-2">今日公佈的宏觀數據符合預期，但未對市場產生主要推動力：</p>
            <ul class="list-disc pl-5 space-y-2">
              <li><strong>美國上週初請失業金人數：</strong>實際值 <strong>21.8萬人</strong>，預期 21.9萬人，前值 21.7萬人。</li>
            </ul>
            <p class="mt-2"><strong>數據解讀：</strong>就業數據表明美國勞動力市場依然極具彈性，支持了經濟「軟著陸」的底色。然而，這也意味著聯準會並無迫切的「大幅放水降息」需求。在就業穩定但油價通膨隱憂上升的背景下，市場進一步調整降息預期。</p>
          </div>
        </div>
      </div>
    </section>

    <!-- 4. 板塊表現 -->
    <section id="sectors" class="mb-12 scroll-mt-6">
      <h2 class="text-2xl font-bold mb-4 flex items-center gap-2 border-b border-zinc-100 dark:border-zinc-800 pb-2">
        <span class="text-brand-500">4.</span> 板塊表現 (Table)
      </h2>
      
      <div class="mb-4 flex flex-col sm:flex-row gap-2 no-print">
        <input type="text" id="sectorSearch" onkeyup="filterSectors()" placeholder="搜尋板塊名稱或代碼..." class="px-4 py-2 text-sm rounded-lg border border-zinc-200 dark:border-zinc-800 bg-white dark:bg-zinc-950 focus:outline-none focus:ring-2 focus:ring-brand-550 w-full sm:w-72">
      </div>

      <div class="overflow-x-auto border border-zinc-200 dark:border-zinc-800 rounded-xl mb-3">
        <table id="sectorTable" class="min-w-full divide-y divide-zinc-200 dark:divide-zinc-850 text-sm">
          <thead class="bg-zinc-50 dark:bg-zinc-900 cursor-pointer">
            <tr class="text-zinc-550 dark:text-zinc-400 text-left select-none">
              <th onclick="sortSectors(0)" class="px-4 py-3 font-semibold hover:bg-zinc-100 dark:hover:bg-zinc-850">排名</th>
              <th onclick="sortSectors(1)" class="px-4 py-3 font-semibold hover:bg-zinc-100 dark:hover:bg-zinc-850">標普11大板塊</th>
              <th onclick="sortSectors(2)" class="px-4 py-3 font-semibold hover:bg-zinc-100 dark:hover:bg-zinc-850">代表 ETF</th>
              <th onclick="sortSectors(3)" class="px-4 py-3 text-right font-semibold hover:bg-zinc-100 dark:hover:bg-zinc-850">當日漲跌</th>
              <th onclick="sortSectors(4)" class="px-4 py-3 text-right font-semibold hover:bg-zinc-100 dark:hover:bg-zinc-850">跑贏/跑輸標普</th>
              <th class="px-4 py-3 font-semibold">當日驅動核心原因</th>
            </tr>
          </thead>
          <tbody class="divide-y divide-zinc-200 dark:divide-zinc-850 font-mono text-zinc-700 dark:text-zinc-300">
            <tr class="hover:bg-zinc-50/50 dark:hover:bg-zinc-900/30">
              <td>1</td>
              <td class="font-sans font-medium text-zinc-900 dark:text-zinc-100">Energy (能源)</td>
              <td>XLE</td>
              <td class="text-right text-emerald-500 font-semibold" data-val="0.80">+0.80%</td>
              <td class="text-right text-emerald-500" data-val="2.01">+2.01%</td>
              <td class="font-sans text-xs">中東衝突推動布蘭特原油突破100美元大關，刺激大宗商品與油氣股逆市走高。</td>
            </tr>
            <tr class="hover:bg-zinc-50/50 dark:hover:bg-zinc-900/30">
              <td>2</td>
              <td class="font-sans font-medium text-zinc-900 dark:text-zinc-100">Industrials (工業)</td>
              <td>XLI</td>
              <td class="text-right text-emerald-500 font-semibold" data-val="0.65">+0.65%</td>
              <td class="text-right text-emerald-500" data-val="1.86">+1.86%</td>
              <td class="font-sans text-xs">Lockheed Martin（+10.5%）與RTX（+7.5%）爆表財報大漲，強力提振工業與國防軍工板塊。</td>
            </tr>
            <tr class="hover:bg-zinc-50/50 dark:hover:bg-zinc-900/30">
              <td>3</td>
              <td class="font-sans font-medium text-zinc-900 dark:text-zinc-100">Healthcare (醫療保健)</td>
              <td>XLV</td>
              <td class="text-right text-emerald-500 font-semibold" data-val="0.35">+0.35%</td>
              <td class="text-right text-emerald-500" data-val="1.56">+1.56%</td>
              <td class="font-sans text-xs">避險情緒高企，防禦性製藥板塊吸引機構避險資金流入抱團。</td>
            </tr>
            <tr class="hover:bg-zinc-50/50 dark:hover:bg-zinc-900/30">
              <td>4</td>
              <td class="font-sans font-medium text-zinc-900 dark:text-zinc-100">Utilities (公用事業)</td>
              <td>XLU</td>
              <td class="text-right text-emerald-500 font-semibold" data-val="0.20">+0.20%</td>
              <td class="text-right text-emerald-500" data-val="1.41">+1.41%</td>
              <td class="font-sans text-xs">避險抱團資金流入，雖然債息飆升形成壓力，但板塊仍以平盤微升收盤。</td>
            </tr>
            <tr class="hover:bg-zinc-50/50 dark:hover:bg-zinc-900/30">
              <td>5</td>
              <td class="font-sans font-medium text-zinc-900 dark:text-zinc-100">Consumer Staples (必需消費)</td>
              <td>XLP</td>
              <td class="text-right text-rose-500 font-semibold" data-val="-0.20">-0.20%</td>
              <td class="text-right text-emerald-500" data-val="1.01">+1.01%</td>
              <td class="font-sans text-xs">消費必需品展現相對抗跌性，跑贏大盤指數。</td>
            </tr>
            <tr class="hover:bg-zinc-50/50 dark:hover:bg-zinc-900/30">
              <td>6</td>
              <td class="font-sans font-medium text-zinc-900 dark:text-zinc-100">Financials (金融)</td>
              <td>XLF</td>
              <td class="text-right text-rose-500 font-semibold" data-val="-0.40">-0.40%</td>
              <td class="text-right text-emerald-500" data-val="0.81">+0.81%</td>
              <td class="font-sans text-xs">債息飆升雖然利好利差，但大盤拋售導致銀行股跟隨大盤小幅下滑。</td>
            </tr>
            <tr class="hover:bg-zinc-50/50 dark:hover:bg-zinc-900/30">
              <td>7</td>
              <td class="font-sans font-medium text-zinc-950 dark:text-zinc-100">Materials (材料)</td>
              <td>XLB</td>
              <td class="text-right text-rose-500 font-semibold" data-val="-0.50">-0.50%</td>
              <td class="text-right text-emerald-500" data-val="0.71">+0.71%</td>
              <td class="font-sans text-xs">工業材料股跟隨大盤小幅調整，表現基本與小盤股持平。</td>
            </tr>
            <tr class="hover:bg-zinc-50/50 dark:hover:bg-zinc-900/30">
              <td>8</td>
              <td class="font-sans font-medium text-zinc-900 dark:text-zinc-100">Real Estate (房地產)</td>
              <td>XLRE</td>
              <td class="text-right text-rose-500 font-semibold" data-val="-0.60">-0.60%</td>
              <td class="text-right text-emerald-500" data-val="0.61">+0.61%</td>
              <td class="font-sans text-xs">10年期國債收益率飆至4.71%高位，對高債務與敏感的房地產板塊形成估值壓制。</td>
            </tr>
            <tr class="hover:bg-zinc-50/50 dark:hover:bg-zinc-900/30">
              <td>9</td>
              <td class="font-sans font-medium text-zinc-900 dark:text-zinc-100">Information Technology (資訊科技)</td>
              <td>XLK</td>
              <td class="text-right text-rose-500 font-semibold" data-val="-1.90">-1.90%</td>
              <td class="text-right text-rose-500" data-val="-0.69">-0.69%</td>
              <td class="font-sans text-xs">微軟、輝達及半導體設備商遭遇去槓桿資金撤離，軟體板塊亦出現回調。</td>
            </tr>
            <tr class="hover:bg-zinc-50/50 dark:hover:bg-zinc-900/30">
              <td>10</td>
              <td class="font-sans font-medium text-zinc-900 dark:text-zinc-100">Consumer Discretionary (可選消費)</td>
              <td>XLY</td>
              <td class="text-right text-rose-500 font-semibold" data-val="-3.50">-3.50%</td>
              <td class="text-right text-rose-500" data-val="-2.29">-2.29%</td>
              <td class="font-sans text-xs">特斯拉業績大爆冷重挫14.5%，加上亞馬遜跌2.3%，拖累板塊跑輸大盤。</td>
            </tr>
            <tr class="hover:bg-zinc-50/50 dark:hover:bg-zinc-900/30">
              <td>11</td>
              <td class="font-sans font-medium text-zinc-900 dark:text-zinc-100">Communication Services (通訊服務)</td>
              <td>XLC</td>
              <td class="text-right text-rose-500 font-semibold" data-val="-5.20">-5.20%</td>
              <td class="text-right text-rose-500" data-val="-3.99">-3.99%</td>
              <td class="font-sans text-xs">Alphabet財報後資本支出受質疑股價重挫7.13%，拖累Meta（-3.75%）及整個通訊板塊全線暴跌。</td>
            </tr>
          </tbody>
        </table>
      </div>
      <p class="text-xs text-zinc-400 dark:text-zinc-500">* 點選標題欄位可對板塊排名、漲跌幅或價格進行動態排序。</p>
    </section>

    <!-- 5. 主題與風格表現 -->
    <section id="themes" class="mb-12 scroll-mt-6">
      <h2 class="text-2xl font-bold mb-4 flex items-center gap-2 border-b border-zinc-100 dark:border-zinc-800 pb-2">
        <span class="text-brand-500">5.</span> 主題與風格表現
      </h2>
      <div class="bg-zinc-50/50 dark:bg-zinc-900/50 p-6 rounded-2xl border border-zinc-200/60 dark:border-zinc-800/60 text-sm leading-relaxed text-zinc-700 dark:text-zinc-300">
        <p class="mb-3">
          今日市場風格呈現極端的<strong>「AI支出質疑打壓科技與晶片、地緣局勢刺激原油大漲、國防爆喜板塊逆市吸金」</strong>特徵：
        </p>
        <ul class="list-disc pl-5 space-y-2">
          <li><strong>晶片與硬體板塊 (SOXX/SMH)：</strong>半導體晶片股面臨獲利回吐及去槓桿壓力，雖然輝達（NVDA -1.65%）跌幅受限於200美元整數關卡，但超微（AMD -2.3%）與博通（AVGO -1.57%）仍收低，費半整體收跌0.54%表現偏弱。</li>
          <li><strong>軟體板塊 (IGV)：</strong>收跌2.08%，微軟（-2.24%）、ServiceNow（-3.5%）、Adobe（-2.84%）等權重軟體股均顯著回撤，表明資金對整個AI應用端轉化進度及研發開支擴大持謹慎態度。</li>
          <li><strong>小盤股 (IWM) vs 大盤股：</strong>小盤股今日跌幅僅為0.54%，相較於標普（-1.21%）和納指（-2.15%）展現了極佳的抗跌性。市場正將資金從高估值巨頭向傳統與防禦類資產進行轉移。</li>
          <li><strong>國防與電力基建：</strong>受LMT與RTX強大業績刺激，加上中東局勢惡化，國防軍工股大爆發。此外，資料中心液冷龍頭維諦技術（VRT +3.22%）與核能股Oklo（+4.76%）展現出極強的抗跌與反彈特徵。</li>
        </ul>
      </div>
    </section>

    <!-- 6. 市場寬度與參與度 -->
    <section id="breadth" class="mb-12 scroll-mt-6">
      <h2 class="text-2xl font-bold mb-4 flex items-center gap-2 border-b border-zinc-100 dark:border-zinc-800 pb-2">
        <span class="text-brand-500">6.</span> 市場寬度與參與度
      </h2>
      
      <div class="grid grid-cols-1 md:grid-cols-3 gap-6 text-sm">
        <div class="bg-zinc-50 dark:bg-zinc-900/40 p-5 rounded-xl border border-zinc-200 dark:border-zinc-800">
          <h4 class="font-bold text-zinc-800 dark:text-zinc-200 mb-3 flex items-center gap-1.5">
            <span class="w-2 h-2 rounded-full bg-brand-550"></span> 均線參與度
          </h4>
          <ul class="space-y-2">
            <li class="flex justify-between"><span>標普500高於50MA比例：</span><span class="font-semibold text-rose-500">58.0%</span></li>
            <li class="flex justify-between"><span>納指100高於50MA比例：</span><span class="font-semibold text-rose-500">46.0%</span></li>
            <li class="flex justify-between"><span>標普500高於200MA比例：</span><span class="font-semibold">66.5%</span></li>
          </ul>
          <p class="text-xs text-zinc-400 mt-3">納指100高於50MA比例跌破50%的分水嶺，顯示中期上行軌跡的個股正在萎縮，市場由極少數權重股勉強支撐的結構風險再度回升。</p>
        </div>

        <div class="bg-zinc-50 dark:bg-zinc-900/40 p-5 rounded-xl border border-zinc-200 dark:border-zinc-800">
          <h4 class="font-bold text-zinc-800 dark:text-zinc-200 mb-3 flex items-center gap-1.5">
            <span class="w-2 h-2 rounded-full bg-brand-550"></span> 漲跌家數與新高新低
          </h4>
          <ul class="space-y-2">
            <li class="flex justify-between"><span>NYSE 漲/跌家數：</span><span>710 / 2,340</span></li>
            <li class="flex justify-between"><span>Nasdaq 漲/跌家數：</span><span>1,250 / 3,120</span></li>
            <li class="flex justify-between"><span>NYSE 新高/新低：</span><span>12 / 45</span></li>
            <li class="flex justify-between"><span>Nasdaq 新高/新低：</span><span>25 / 95</span></li>
          </ul>
          <p class="text-xs text-zinc-400 mt-3">兩市下跌家數呈壓倒性優勢，漲跌比接近1:3，新高與新低家數差值顯著惡化，顯示空頭主導了今日的交易情緒。</p>
        </div>

        <div class="bg-zinc-50 dark:bg-zinc-900/40 p-5 rounded-xl border border-zinc-200 dark:border-zinc-800">
          <h4 class="font-bold text-zinc-800 dark:text-zinc-200 mb-3 flex items-center gap-1.5">
            <span class="w-2 h-2 rounded-full bg-brand-550"></span> 內部指標觀察
          </h4>
          <ul class="space-y-2">
            <li class="flex justify-between"><span>McClellan Oscillator：</span><span class="font-semibold text-rose-500">-35</span></li>
            <li class="flex justify-between"><span>Put/Call Ratio：</span><span class="font-semibold">0.88</span></li>
            <li class="flex justify-between"><span>VIX 期限結構：</span><span class="font-semibold">近月合約急升，呈平坦化</span></li>
          </ul>
          <p class="text-xs text-zinc-400 mt-3">麥克連指標降至-35，顯示短線下行動能正在擴大；Put/Call比率升至0.88，反映期權市場對於保護性對沖的需求明顯增強。</p>
        </div>
      </div>
    </section>

    <!-- 7. 技術面分析 -->
    <section id="technical" class="mb-12 scroll-mt-6">
      <h2 class="text-2xl font-bold mb-4 flex items-center gap-2 border-b border-zinc-100 dark:border-zinc-800 pb-2">
        <span class="text-brand-500">7.</span> 技術面分析
      </h2>
      
      <div class="overflow-x-auto border border-zinc-200 dark:border-zinc-800 rounded-xl mb-3">
        <table class="min-w-full divide-y divide-zinc-200 dark:divide-zinc-850 text-sm">
          <thead class="bg-zinc-50 dark:bg-zinc-900 font-semibold text-zinc-550 dark:text-zinc-400 text-left">
            <tr>
              <th class="px-4 py-3">ETF 代號</th>
              <th class="px-4 py-3 text-right">收盤價格</th>
              <th class="px-4 py-3 text-right">20日均線</th>
              <th class="px-4 py-3 text-right">50日均線</th>
              <th class="px-4 py-3 text-right">RSI (14)</th>
              <th class="px-4 py-3 text-right">MACD 狀態</th>
              <th class="px-4 py-3 text-right">關鍵支撐 / 壓力</th>
            </tr>
          </thead>
          <tbody class="divide-y divide-zinc-200 dark:divide-zinc-850 font-mono text-zinc-700 dark:text-zinc-300">
            <tr>
              <td class="px-4 py-3 font-bold font-sans text-zinc-900 dark:text-zinc-100">SPY (標普 500 ETF)</td>
              <td class="px-4 py-3 text-right">738.18</td>
              <td class="px-4 py-3 text-right">745.50</td>
              <td class="px-4 py-3 text-right">732.10</td>
              <td class="px-4 py-3 text-right">46</td>
              <td class="px-4 py-3 text-right text-rose-500">綠柱萎縮/死叉邊緣</td>
              <td class="px-4 py-3 text-right">730.00 / 748.00</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-bold font-sans text-zinc-900 dark:text-zinc-100">QQQ (納斯達克 100 ETF)</td>
              <td class="px-4 py-3 text-right">691.96</td>
              <td class="px-4 py-3 text-right">704.10</td>
              <td class="px-4 py-3 text-right">688.50</td>
              <td class="px-4 py-3 text-right">41</td>
              <td class="px-4 py-3 text-right text-rose-500">死叉確認下行</td>
              <td class="px-4 py-3 text-right">685.00 / 705.00</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-bold font-sans text-zinc-900 dark:text-zinc-100">IWM (羅素 2000 ETF)</td>
              <td class="px-4 py-3 text-right">293.48</td>
              <td class="px-4 py-3 text-right">292.10</td>
              <td class="px-4 py-3 text-right">285.40</td>
              <td class="px-4 py-3 text-right">52</td>
              <td class="px-4 py-3 text-right text-emerald-500">金叉開口收窄</td>
              <td class="px-4 py-3 text-right">290.00 / 300.00</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-bold font-sans text-zinc-900 dark:text-zinc-100">SMH (半導體 ETF)</td>
              <td class="px-4 py-3 text-right">584.28</td>
              <td class="px-4 py-3 text-right">598.50</td>
              <td class="px-4 py-3 text-right">578.10</td>
              <td class="px-4 py-3 text-right">43</td>
              <td class="px-4 py-3 text-right text-rose-500">柱體向下擴大</td>
              <td class="px-4 py-3 text-right">575.00 / 605.00</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-bold font-sans text-zinc-900 dark:text-zinc-100">IGV (科技軟體 ETF)</td>
              <td class="px-4 py-3 text-right">87.17</td>
              <td class="px-4 py-3 text-right">89.20</td>
              <td class="px-4 py-3 text-right">86.50</td>
              <td class="px-4 py-3 text-right">45</td>
              <td class="px-4 py-3 text-right text-rose-500">綠柱萎縮</td>
              <td class="px-4 py-3 text-right">85.50 / 90.00</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-bold font-sans text-zinc-900 dark:text-zinc-100">XLK (科技板塊 ETF)</td>
              <td class="px-4 py-3 text-right">175.71</td>
              <td class="px-4 py-3 text-right">179.80</td>
              <td class="px-4 py-3 text-right">173.20</td>
              <td class="px-4 py-3 text-right">42</td>
              <td class="px-4 py-3 text-right text-rose-500">死叉下行</td>
              <td class="px-4 py-3 text-right">172.00 / 181.00</td>
            </tr>
          </tbody>
        </table>
      </div>
      <p class="text-xs text-zinc-400 dark:text-zinc-500 leading-relaxed">
        <strong>技術評語：</strong>大盤與多數高彈性成長板塊ETF（SPY、QQQ、SMH、XLK）均跌破了原先上行的20日均線，目前正處於測試50日均線（中期強弱分水嶺）的關鍵時刻。RSI指標回落至41-46之間，未進入超賣區，顯示短期修正仍有進一步調整空間。小盤股（IWM）則在20日均線上方維持防禦整理，是目前日線圖上最強勢的ETF結構。
      </p>
    </section>

    <!-- 8. 重點個股新聞與異動 -->
    <section id="stocks" class="mb-12 scroll-mt-6">
      <h2 class="text-2xl font-bold mb-4 flex items-center gap-2 border-b border-zinc-100 dark:border-zinc-800 pb-2">
        <span class="text-brand-500">8.</span> 重點個股新聞與異動 (Details)
      </h2>
      
      <div class="space-y-4">
        <details class="group bg-zinc-50 dark:bg-zinc-950/20 p-4 rounded-xl border border-zinc-200 dark:border-zinc-800">
          <summary class="font-bold text-zinc-800 dark:text-zinc-200 flex justify-between items-center">
            8.1 大型科技七巨頭 (Magnificent 7)
          </summary>
          <div class="mt-3 text-sm space-y-3 leading-relaxed text-zinc-650 dark:text-zinc-350">
            <p><strong>TSLA (特斯拉) -14.52%：</strong>第二季度財報多項利潤率指標不及預期，因降價促銷、人工智慧及機器人項目資本支出暴增導致淨利大跌，EPS大幅 beat 預期落空，股價跳水創2026年最大單日跌幅，直接打擊了科技股的估值底氣。</p>
            <p><strong>GOOGL (Alphabet) -6.45%：</strong>營收營利雖超市場預期，但投資者對其在AI硬體與伺服器投資指引調升（指引上調至195億-205億美元）及短期利潤轉化率產生質疑，股價開低走低大跌，反映出市場對「AI投入重回紅海」的強烈擔憂。</p>
            <p><strong>MSFT (微軟) -2.24%：</strong>微軟作為AI最大的投入者之一，股價受到大盤科技股去估值拋售波及，收盤跌破均線平台，市場屏息等待其7月29日的財報結果。</p>
            <p><strong>AAPL (蘋果) -1.36%：</strong>展現了極佳的避險錨作用，跌幅低於其他科技巨頭，維持在321.46美元心理關口之上。</p>
            <p><strong>META (Meta Platforms) -3.75%：</strong>收報$603.64，高位窄幅平台被跌破，同樣被AI高開支利空所波及。</p>
            <p><strong>NVDA (輝達) -1.65%：</strong>輝達在200美元整數心理關卡展開多空大搏殺。雖然算力去風險明顯，但在大盤巨震背景下表現相對堅挺，收報$200.04。</p>
          </div>
        </details>

        <details class="group bg-zinc-50 dark:bg-zinc-950/20 p-4 rounded-xl border border-zinc-200 dark:border-zinc-800">
          <summary class="font-bold text-zinc-800 dark:text-zinc-200 flex justify-between items-center">
            8.2 AI 硬體 / 半導體重點股異動分析
          </summary>
          <div class="mt-3 text-sm space-y-3 leading-relaxed text-zinc-650 dark:text-zinc-350">
            <p><strong>AMD (超微) -2.30%：</strong>收報$539.69。在前日Advancing AI 2026大會宣布與微軟和Anthropic的重磅合作後，股價出現利多兌現的正常技術回調，繼續在540美元附近震盪。</p>
            <p><strong>AVGO (博通) -1.57%：</strong>收報$393.68。失守400美元整數關口，但整體下行速度受限，成交量未見恐慌放大。</p>
            <p><strong>MRVL (美滿電子) -0.79%：</strong>表現極其堅韌，微幅收跌至$209.32，技術面上守穩200日均線上方，底部多頭護盤跡象明顯。</p>
            <p><strong>ASML / TSM (阿斯麥/台積電)：</strong>台積電ADR跌幅逾1.8%，阿斯麥跌逾2.1%，半導體巨頭跟隨費半指數修正，反映大資金在下週科技決議前進行戰術性防守建倉調整。</p>
          </div>
        </details>

        <details class="group bg-zinc-50 dark:bg-zinc-950/20 p-4 rounded-xl border border-zinc-200 dark:border-zinc-800">
          <summary class="font-bold text-zinc-800 dark:text-zinc-200 flex justify-between items-center">
            8.3 軟體 / SaaS / AI 應用重點股異動分析
          </summary>
          <div class="mt-3 text-sm space-y-3 leading-relaxed text-zinc-650 dark:text-zinc-350">
            <p><strong>CRM (Salesforce) -3.70%：</strong>收報$156.93。再次跌破主要短期均線，股價自底部修復的走勢遭遇挫折，面臨重新築底的壓力。</p>
            <p><strong>NOW (ServiceNow) -3.50%：</strong>回調至$766.98。作為高增長軟體龍頭，跟隨IGV進行估值釋放，市場等待即將公佈的季報指引以驗證AI工具的盈利能力。</p>
            <p><strong>SNOW (Snowflake) -1.00%：</strong>雪花收跌至$265.13，展現了一定的底部抗跌性，量能極度萎縮，處於箱體底部盤整中。</p>
            <p><strong>ADBE (Adobe) -2.84%：</strong>回落至$533.70，前期突破箱體上軌後回踩支撐，需觀察能否在530美元支撐上方企穩。</p>
          </div>
        </details>

        <details class="group bg-zinc-50 dark:bg-zinc-950/20 p-4 rounded-xl border border-zinc-200 dark:border-zinc-800">
          <summary class="font-bold text-zinc-800 dark:text-zinc-200 flex justify-between items-center">
            8.4 AI 電力 / 資料中心 / 能源基礎設施重點股分析
          </summary>
          <div class="mt-3 text-sm space-y-3 leading-relaxed text-zinc-650 dark:text-zinc-350">
            <p><strong>VRT (維諦技術) +3.22%：</strong>放量大漲收在$310.50。作為全球資料中心液冷及溫控龍頭，受到大資金對AI實體基建需求的強大支撐，逆市暴漲創近期高點，展現強大板塊彈性。</p>
            <p><strong>OKLO (Oklo Inc.) +4.76%：</strong>收在$45.36。受益於政策面對核電與小堆（SMR）開發的支持，作為算力電力的投機題材，股價吸引了充沛的動能追捧。</p>
            <p><strong>CEG / VST (Constellation / Vistra) +0.05% / +0.87%：</strong>雙雙收綠。在科技大盤全線失血的狀況下，核電及獨立發電商巨頭依然牢牢守在多頭通道中，凸顯出電力才是AI最終物理瓶頸的長線邏輯。</p>
          </div>
        </details>
      </div>
    </section>

    <!-- 9. 財報日曆與財報解讀 -->
    <section id="earnings" class="mb-12 scroll-mt-6">
      <h2 class="text-2xl font-bold mb-4 flex items-center gap-2 border-b border-zinc-100 dark:border-zinc-800 pb-2">
        <span class="text-brand-500">9.</span> 財報日曆與財報解讀
      </h2>
      
      <div class="mb-6">
        <h3 class="text-lg font-semibold mb-3">9.1 昨夜已公佈財報的重點公司解讀</h3>
        <div class="space-y-4">
          <div class="bg-zinc-50 dark:bg-zinc-950/20 p-5 rounded-xl border border-zinc-200 dark:border-zinc-800">
            <h4 class="font-bold text-zinc-900 dark:text-zinc-100 mb-2 flex justify-between">
              <span>TSLA (特斯拉) - Q2 業績爆冷</span>
              <span class="text-rose-500">-14.52% (收盤)</span>
            </h4>
            <p class="text-sm leading-relaxed mb-2 text-zinc-650 dark:text-zinc-350">
              營收 282.4億美元（YoY +26%），高於預期的245億美元；但 non-GAAP EPS 僅為 <strong>$0.33</strong>，遠低於分析師預期的 $0.53。營業利潤同比崩跌 57% 至約4億美元，毛利率下滑至 14.6%，主要因促銷降價、重組費用以及在AI項目和自動駕駛（FSD）基礎設施上的龐大資本開支。
            </p>
            <p class="text-xs text-zinc-550"><strong>核心解讀：</strong>市場對於特斯拉「降價求量卻犧牲利潤」的商業模式感到失望，且大量投入的AI和機器人開支並未能及時轉化為利潤，股價短線面臨估值重塑。</p>
          </div>

          <div class="bg-zinc-50 dark:bg-zinc-950/20 p-5 rounded-xl border border-zinc-200 dark:border-zinc-800">
            <h4 class="font-bold text-zinc-900 dark:text-zinc-100 mb-2 flex justify-between">
              <span>GOOGL (Alphabet) - Q2 利潤與營收超預期</span>
              <span class="text-rose-500">-6.45% (收盤)</span>
            </h4>
            <p class="text-sm leading-relaxed mb-2 text-zinc-650 dark:text-zinc-350">
              營收 1,198億美元（YoY +24%），勝預期的1,185億美元；EPS 達 <strong>$9.11</strong>，勝預期的$8.85。雲業務營收增長強勁。然而，公司將全年資本支出（CapEx）指引區間調高至 <strong>1,950億 - 2,050億美元</strong>（先前為1,800億-1,900億），引發市場對AI高昂基建開支短期難以獲得回報的疑慮。
            </p>
            <p class="text-xs text-zinc-555"><strong>核心解讀：</strong>「營收雖好但開支嚇人」。在大盤估值本已緊繃的背景下，大幅超支的AI投入被市場解讀為短期利潤率的阻礙，引發資金獲利回吐。</p>
          </div>

          <div class="bg-zinc-50 dark:bg-zinc-950/20 p-5 rounded-xl border border-zinc-200 dark:border-zinc-800">
            <h4 class="font-bold text-zinc-900 dark:text-zinc-100 mb-2 flex justify-between">
              <span>LMT & RTX (洛克希德馬丁與雷神) - 軍工強勁beat</span>
              <span class="text-emerald-500">LMT +10.54% / RTX +7.50%</span>
            </h4>
            <p class="text-sm leading-relaxed mb-2 text-zinc-650 dark:text-zinc-350">
              LMT第二季度營收達201億美元，同比增長11%；EPS達 <strong>$7.94</strong>，大幅超出預期，積壓訂單創下2,300億美元的歷史新高。RTX營收247億美元，同比增長16%；調整後EPS達 <strong>$1.89</strong>，強勁超預期。兩家國防巨頭雙雙大幅調升了2026全年的營收和自由現金流指引。
            </p>
            <p class="text-xs text-zinc-555"><strong>核心解讀：</strong>全球地緣政治局勢動盪推升了防務需求，兩大軍工巨頭憑藉爆表業績與創紀錄訂單積壓，成為當日避險資金的最優選擇，強勢帶動大工業板塊逆市上揚。</p>
          </div>
        </div>
      </div>

      <div>
        <h3 class="text-lg font-semibold mb-3">9.2 接下來 1-3 個交易日的重要財報日曆</h3>
        <div class="overflow-x-auto border border-zinc-200 dark:border-zinc-800 rounded-xl">
          <table class="min-w-full divide-y divide-zinc-200 dark:divide-zinc-850 text-sm">
            <thead class="bg-zinc-50 dark:bg-zinc-900 font-semibold text-zinc-550 dark:text-zinc-400 text-left">
              <tr>
                <th class="px-4 py-3">交易日期</th>
                <th class="px-4 py-3">公司代號</th>
                <th class="px-4 py-3">中文名稱</th>
                <th class="px-4 py-3">發佈時段</th>
                <th class="px-4 py-3">市場關注焦點</th>
              </tr>
            </thead>
            <tbody class="divide-y divide-zinc-200 dark:divide-zinc-850 text-zinc-700 dark:text-zinc-300">
              <tr>
                <td class="px-4 py-3 font-mono">2026-07-29</td>
                <td class="px-4 py-3 font-bold font-mono">MSFT</td>
                <td class="px-4 py-3">微軟</td>
                <td class="px-4 py-3 text-amber-500">盤後發佈</td>
                <td class="px-4 py-3 text-xs">Azure雲端業務增速是否因AI產能瓶頸而放緩；AI資本支出的回報周期與對利潤率的擠壓。</td>
              </tr>
              <tr>
                <td class="px-4 py-3 font-mono">2026-07-30</td>
                <td class="px-4 py-3 font-bold font-mono">AMD</td>
                <td class="px-4 py-3">超微半導體</td>
                <td class="px-4 py-3 text-amber-550">盤後發佈</td>
                <td class="px-4 py-3 text-xs">MI300/MI400系列晶片出貨指引；與微軟及Meta等AI算力大單的實質營收貢獻。</td>
              </tr>
              <tr>
                <td class="px-4 py-3 font-mono">2026-07-31</td>
                <td class="px-4 py-3 font-bold font-mono">META</td>
                <td class="px-4 py-3">Meta Platforms</td>
                <td class="px-4 py-3 text-amber-550">盤後發佈</td>
                <td class="px-4 py-3 text-xs">AI廣告算法帶來的實際變現增長；Llama 3商業化進展以及元宇宙與AI高昂支出的平衡。</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </section>

    <!-- 10. 機構觀點與資金流 -->
    <section id="institution" class="mb-12 scroll-mt-6">
      <h2 class="text-2xl font-bold mb-4 flex items-center gap-2 border-b border-zinc-100 dark:border-zinc-800 pb-2">
        <span class="text-brand-500">10.</span> 機構觀點與資金流
      </h2>
      <div class="grid grid-cols-1 md:grid-cols-2 gap-6 text-sm leading-relaxed text-zinc-700 dark:text-zinc-300">
        <div class="bg-zinc-50 dark:bg-zinc-900/40 p-5 rounded-xl border border-zinc-200 dark:border-zinc-800">
          <h4 class="font-bold text-zinc-800 dark:text-zinc-200 mb-2">高盛與摩根士丹利：AI估值容錯率正在急劇降低</h4>
          <p class="mb-2"><strong>高盛（Goldman Sachs）</strong>在最新市場評述中指出，過去一年科技巨頭的估值大幅上調是建立在「AI將迅速提升企業盈利」的預期之上。然而，Alphabet和特斯拉的財報表明，AI目前的投入（CapEx）依然是吞噬利潤的無底洞，而實質變現（ROI）的窗口期正在被拉長。未來一到兩季，財報稍有瑕疵的科技股將面臨估值重塑，資金將加速流向實體經濟和傳統週期股。</p>
          <p><strong>摩根士丹利（Morgan Stanley）</strong>則強調，10年期美債收益率重回4.7%上方意味著折現率高企，這將對科技巨頭形成「估值與利息雙重擠壓」，建議投資者短期將配置轉向更具確定性的防禦性資產（大工業、醫藥及大宗商品）。</p>
        </div>

        <div class="bg-zinc-50 dark:bg-zinc-900/40 p-5 rounded-xl border border-zinc-200 dark:border-zinc-800">
          <h4 class="font-bold text-zinc-800 dark:text-zinc-200 mb-2">ETF資金流向與期權市場異動</h4>
          <p class="mb-2"><strong>ETF 資金觀測：</strong>今日科技板塊ETF（XLK、QQQ）出現顯著的淨流出，為近一個月來首見。相反，防禦性板塊（XLI 工業、XLE 能源）迎來防守型資金的淨流入。特別是國防和原油主題ETF，資金追捧熱度明顯上升。</p>
          <p><strong>期權市場異動：</strong>特斯拉與谷歌在公佈財報後，期權成交量創下歷史天量。特斯拉的看跌期權（Put）交易量占比急升至58%，大量看漲期權（Call）多頭止損出局。此外，微軟與Meta在下週季報前夕，保護性期權成交量亦出現異動，顯示機構正大舉買入看跌期權對沖科技股進一步崩塌的風險。</p>
        </div>
      </div>
    </section>

    <!-- 11. 板塊輪動判斷 -->
    <section id="rotation" class="mb-12 scroll-mt-6">
      <h2 class="text-2xl font-bold mb-4 flex items-center gap-2 border-b border-zinc-100 dark:border-zinc-800 pb-2">
        <span class="text-brand-500">11.</span> 板塊輪動判斷
      </h2>
      <div class="bg-zinc-50/50 dark:bg-zinc-900/50 p-6 rounded-2xl border border-zinc-200/60 dark:border-zinc-800/60 text-sm leading-relaxed text-zinc-700 dark:text-zinc-300">
        <p class="mb-3">
          <strong>資金從「AI科技算力」流向「防務、實體大工業與大宗商品」：</strong>
        </p>
        <p class="mb-3">
          今日市場見證了清晰的板塊輪動軌跡。前段時間高高在上的AI晶片、科技巨頭以及應用端軟體板塊在特斯拉與谷歌的業績打擊下，集體遭遇了估值和倉位的雙重去槓桿拋售。這部分撤出的熱錢並未選擇離場觀望，而是大舉回流實體與防禦板塊。
        </p>
        <p>
          <strong>中長線研判：</strong>AI的主線並未宣告破產，但已經從「純概念估值擴張」過渡到「實質盈利與ROI變現檢驗」的嚴酷右側階段。在下週微軟、AMD及Meta的業績塵埃落定之前，資金依然會維持防守姿態，電力、核能（OKLO、VST）等物理算力瓶頸，以及國防、能源大宗（XLE）將是資金的臨時避風港。
        </p>
      </div>
    </section>

    <!-- 12. 我的重點關注股觀察 -->
    <section id="watchlist" class="mb-12 scroll-mt-6">
      <h2 class="text-2xl font-bold mb-4 flex items-center gap-2 border-b border-zinc-100 dark:border-zinc-800 pb-2">
        <span class="text-brand-500">12.</span> 我的重點關注股觀察
      </h2>
      
      <div class="overflow-x-auto border border-zinc-200 dark:border-zinc-800 rounded-xl">
        <table class="min-w-full divide-y divide-zinc-200 dark:divide-zinc-850 text-sm">
          <thead class="bg-zinc-50 dark:bg-zinc-900">
            <tr class="text-zinc-550 dark:text-zinc-400 text-left">
              <th class="px-4 py-3 font-semibold">代號</th>
              <th class="px-4 py-3 font-semibold text-right">最新收盤價</th>
              <th class="px-4 py-3 font-semibold text-right">單日漲跌</th>
              <th class="px-4 py-3 font-semibold text-center">決策判定標籤</th>
              <th class="px-4 py-3 font-semibold">觀察與交易心法</th>
            </tr>
          </thead>
          <tbody class="divide-y divide-zinc-200 dark:divide-zinc-850 font-mono text-zinc-700 dark:text-zinc-300">
            <tr class="hover:bg-zinc-50/50 dark:hover:bg-zinc-900/30">
              <td class="font-bold">NVDA</td>
              <td class="text-right">200.04</td>
              <td class="text-right text-rose-500">-1.65%</td>
              <td class="text-center font-semibold text-amber-500 font-sans"><span class="px-2 py-0.5 rounded bg-amber-50 dark:bg-amber-950/40">等財報催化</span></td>
              <td class="font-sans text-xs">200美元大關面臨激烈爭奪。大盤科技去槓桿波及股價，短線需保持克制，靜待業績出爐。</td>
            </tr>
            <tr class="hover:bg-zinc-50/50 dark:hover:bg-zinc-900/30">
              <td class="font-bold">AMD</td>
              <td class="text-right">539.69</td>
              <td class="text-right text-rose-500">-2.30%</td>
              <td class="text-center font-semibold text-zinc-500 font-sans"><span class="px-2 py-0.5 rounded bg-zinc-100 dark:bg-zinc-800/40">高位震盪</span></td>
              <td class="font-sans text-xs">AI大會釋放利好後遭遇利多兌現。股價短期處於高位偏弱震盪，等待下週季報指引。</td>
            </tr>
            <tr class="hover:bg-zinc-50/50 dark:hover:bg-zinc-900/30">
              <td class="font-bold">AVGO</td>
              <td class="text-right">393.68</td>
              <td class="text-right text-rose-500">-1.57%</td>
              <td class="text-center font-semibold text-zinc-500 font-sans"><span class="px-2 py-0.5 rounded bg-zinc-100 dark:bg-zinc-800/40">需要觀察</span></td>
              <td class="font-sans text-xs">失守400美元平台，晶片股去槓桿賣壓未竭，需等待半導體板塊探底企穩。</td>
            </tr>
            <tr class="hover:bg-zinc-50/50 dark:hover:bg-zinc-900/30">
              <td class="font-bold">MRVL</td>
              <td class="text-right">209.32</td>
              <td class="text-right text-rose-500">-0.79%</td>
              <td class="text-center font-semibold text-emerald-500 font-sans"><span class="px-2 py-0.5 rounded bg-emerald-50 dark:bg-emerald-950/40">低位修復</span></td>
              <td class="font-sans text-xs">展現極強抗跌性，守在短期及中期均線之上，反映資金對其算力轉化率的初步認可。</td>
            </tr>
            <tr class="hover:bg-zinc-50/50 dark:hover:bg-zinc-900/30">
              <td class="font-bold">GOOGL</td>
              <td class="text-right">320.02</td>
              <td class="text-right text-rose-500">-6.45%</td>
              <td class="text-center font-semibold text-amber-500 font-sans"><span class="px-2 py-0.5 rounded bg-amber-50 dark:bg-amber-950/40">利好兌現</span></td>
              <td class="font-sans text-xs">財報數據雖佳，但AI資本支出指引大增引發估值打壓，股價大幅殺跌，短線需防守。</td>
            </tr>
            <tr class="hover:bg-zinc-50/50 dark:hover:bg-zinc-900/30">
              <td class="font-bold">MSFT</td>
              <td class="text-right">381.58</td>
              <td class="text-right text-rose-500">-2.24%</td>
              <td class="text-center font-semibold text-zinc-500 font-sans"><span class="px-2 py-0.5 rounded bg-zinc-100 dark:bg-zinc-800/40">需要觀察</span></td>
              <td class="font-sans text-xs">受行業支出擔憂影響走弱，暫時跑輸大盤，關注7/29財報釋放的Azure實際利潤空間。</td>
            </tr>
            <tr class="hover:bg-zinc-50/50 dark:hover:bg-zinc-900/30">
              <td class="font-bold">META</td>
              <td class="text-right">603.64</td>
              <td class="text-right text-rose-500">-3.75%</td>
              <td class="text-center font-semibold text-zinc-500 font-sans"><span class="px-2 py-0.5 rounded bg-zinc-100 dark:bg-zinc-800/40">需要觀察</span></td>
              <td class="font-sans text-xs">跌破610美元支撐，高位震盪平台失守，等待7/31財報給予廣告與AI支出的新指引。</td>
            </tr>
            <tr class="hover:bg-zinc-50/50 dark:hover:bg-zinc-900/30">
              <td class="font-bold">AMZN</td>
              <td class="text-right">205.27</td>
              <td class="text-right text-rose-500">-2.30%</td>
              <td class="text-center font-semibold text-zinc-500 font-sans"><span class="px-2 py-0.5 rounded bg-zinc-100 dark:bg-zinc-800/40">需要觀察</span></td>
              <td class="font-sans text-xs">隨科技板塊同步回檔，失守210美元整數支撐，短期技術面承壓。</td>
            </tr>
            <tr class="hover:bg-zinc-50/50 dark:hover:bg-zinc-900/30">
              <td class="font-bold">ORCL</td>
              <td class="text-right">136.20</td>
              <td class="text-right text-rose-500">-2.11%</td>
              <td class="text-center font-semibold text-emerald-500 font-sans"><span class="px-2 py-0.5 rounded bg-emerald-50 dark:bg-emerald-950/40">繼續強勢</span></td>
              <td class="font-sans text-xs">穩步調整，雲基礎設施需求與未完成訂單亮眼，回調幅度小於其他軟體龍頭。</td>
            </tr>
            <tr class="hover:bg-zinc-50/50 dark:hover:bg-zinc-900/30">
              <td class="font-bold">CRM</td>
              <td class="text-right">156.93</td>
              <td class="text-right text-rose-500">-3.70%</td>
              <td class="text-center font-semibold text-zinc-500 font-sans"><span class="px-2 py-0.5 rounded bg-zinc-100 dark:bg-zinc-800/40">需要觀察</span></td>
              <td class="font-sans text-xs">股價再次重挫跌破均線，多頭動能回吐，重回底部箱體震盪。</td>
            </tr>
            <tr class="hover:bg-zinc-50/50 dark:hover:bg-zinc-900/30">
              <td class="font-bold">NOW</td>
              <td class="text-right">766.98</td>
              <td class="text-right text-rose-500">-3.50%</td>
              <td class="text-center font-semibold text-zinc-500 font-sans"><span class="px-2 py-0.5 rounded bg-zinc-100 dark:bg-zinc-800/40">需要觀察</span></td>
              <td class="font-sans text-xs">跟隨軟體板塊大幅修正，技術形態走弱，靜待季報以期扭轉跌勢。</td>
            </tr>
            <tr class="hover:bg-zinc-50/50 dark:hover:bg-zinc-900/30">
              <td class="font-bold">SNOW</td>
              <td class="text-right">265.13</td>
              <td class="text-right text-rose-500">-1.00%</td>
              <td class="text-center font-semibold text-zinc-500 font-sans"><span class="px-2 py-0.5 rounded bg-zinc-100 dark:bg-zinc-800/40">需要觀察</span></td>
              <td class="font-sans text-xs">底部盤整，量能進一步萎縮，等待催化劑引導方向選擇。</td>
            </tr>
            <tr class="hover:bg-zinc-50/50 dark:hover:bg-zinc-900/30">
              <td class="font-bold">ADBE</td>
              <td class="text-right">533.70</td>
              <td class="text-right text-rose-500">-2.84%</td>
              <td class="text-center font-semibold text-zinc-500 font-sans"><span class="px-2 py-0.5 rounded bg-zinc-100 dark:bg-zinc-800/40">需要觀察</span></td>
              <td class="font-sans text-xs">前期大突破後回踩下軌支撐。需守住前低，多頭格局面臨考驗。</td>
            </tr>
            <tr class="hover:bg-zinc-50/50 dark:hover:bg-zinc-900/30">
              <td class="font-bold">PLTR</td>
              <td class="text-right">28.68</td>
              <td class="text-right text-rose-500">-1.95%</td>
              <td class="text-center font-semibold text-emerald-500 font-sans"><span class="px-2 py-0.5 rounded bg-emerald-50 dark:bg-emerald-950/40">低位修復</span></td>
              <td class="font-sans text-xs">回踩短期均線，跌幅相對大盤溫和，AI應用端溢價仍受部分買盤支撐。</td>
            </tr>
            <tr class="hover:bg-zinc-50/50 dark:hover:bg-zinc-900/30">
              <td class="font-bold">LITE</td>
              <td class="text-right">49.85</td>
              <td class="text-right text-emerald-500">+0.11%</td>
              <td class="text-center font-semibold text-zinc-500 font-sans"><span class="px-2 py-0.5 rounded bg-zinc-100 dark:bg-zinc-800/40">需要觀察</span></td>
              <td class="font-sans text-xs">光通訊板塊隨算力巨震而維持窄幅波動，等待大板塊止跌企穩。</td>
            </tr>
            <tr class="hover:bg-zinc-50/50 dark:hover:bg-zinc-900/30">
              <td class="font-bold">COHR</td>
              <td class="text-right">64.35</td>
              <td class="text-right text-rose-500">-0.24%</td>
              <td class="text-center font-semibold text-zinc-500 font-sans"><span class="px-2 py-0.5 rounded bg-zinc-100 dark:bg-zinc-800/40">需要觀察</span></td>
              <td class="font-sans text-xs">窄幅回調，多空在此位置基本均衡，等待進一步算力指引。</td>
            </tr>
            <tr class="hover:bg-zinc-50/50 dark:hover:bg-zinc-900/30">
              <td class="font-bold">ANET</td>
              <td class="text-right">174.47</td>
              <td class="text-right text-rose-500">-0.23%</td>
              <td class="text-center font-semibold text-emerald-500 font-sans"><span class="px-2 py-0.5 rounded bg-emerald-50 dark:bg-emerald-950/40">繼續強勢</span></td>
              <td class="font-sans text-xs">極為抗跌，高位窄幅動盪收紅邊緣，多頭趨勢結構及歷史高點仍完好。</td>
            </tr>
            <tr class="hover:bg-zinc-50/50 dark:hover:bg-zinc-900/30">
              <td class="font-bold">FLNC</td>
              <td class="text-right">14.66</td>
              <td class="text-right text-rose-500">-0.95%</td>
              <td class="text-center font-semibold text-zinc-500 font-sans"><span class="px-2 py-0.5 rounded bg-zinc-100 dark:bg-zinc-800/40">需要觀察</span></td>
              <td class="font-sans text-xs">超跌後底部縮量震盪，尚未看見大資金抄底信號，需耐心觀察。</td>
            </tr>
            <tr class="hover:bg-zinc-50/50 dark:hover:bg-zinc-900/30">
              <td class="font-bold">OKLO</td>
              <td class="text-right">45.36</td>
              <td class="text-right text-emerald-500">+4.76%</td>
              <td class="text-center font-semibold text-emerald-500 font-sans"><span class="px-2 py-0.5 rounded bg-emerald-50 dark:bg-emerald-950/40">繼續強勢</span></td>
              <td class="font-sans text-xs">核能題材股大漲，吸引投機熱錢逆市上漲，持倉需防範高位劇烈波動。</td>
            </tr>
            <tr class="hover:bg-zinc-50/50 dark:hover:bg-zinc-900/30">
              <td class="font-bold">VST</td>
              <td class="text-right">163.63</td>
              <td class="text-right text-emerald-500">+0.87%</td>
              <td class="text-center font-semibold text-emerald-500 font-sans"><span class="px-2 py-0.5 rounded bg-emerald-50 dark:bg-emerald-950/40">繼續強勢</span></td>
              <td class="font-sans text-xs">長線算力電力短缺邏輯未變，資金持續流入做防守性配置。</td>
            </tr>
            <tr class="hover:bg-zinc-50/50 dark:hover:bg-zinc-900/30">
              <td class="font-bold">CEG</td>
              <td class="text-right">275.05</td>
              <td class="text-right text-emerald-500">+0.05%</td>
              <td class="text-center font-semibold text-emerald-500 font-sans"><span class="px-2 py-0.5 rounded bg-emerald-50 dark:bg-emerald-950/40">繼續強勢</span></td>
              <td class="font-sans text-xs">核電龍頭高位強勢震盪，避險資金鎖定度極佳，多頭通道完好。</td>
            </tr>
            <tr class="hover:bg-zinc-50/50 dark:hover:bg-zinc-900/30">
              <td class="font-bold">ETN</td>
              <td class="text-right">406.91</td>
              <td class="text-right text-rose-500">-1.75%</td>
              <td class="text-center font-semibold text-zinc-500 font-sans"><span class="px-2 py-0.5 rounded bg-zinc-100 dark:bg-zinc-800/40">需要觀察</span></td>
              <td class="font-sans text-xs">隨大盤出現戰術性獲利盤回流，回踩短期均線平台，尋求支撐。</td>
            </tr>
            <tr class="hover:bg-zinc-50/50 dark:hover:bg-zinc-900/30">
              <td class="font-bold">VRT</td>
              <td class="text-right">310.50</td>
              <td class="text-right text-emerald-500">+3.22%</td>
              <td class="text-center font-semibold text-emerald-500 font-sans"><span class="px-2 py-0.5 rounded bg-emerald-50 dark:bg-emerald-950/40">繼續強勢</span></td>
              <td class="font-sans text-xs">液冷基建放量逆市暴漲！展現強大板塊彈性與資金認可度，創歷史新高。</td>
            </tr>
          </tbody>
        </table>
      </div>
    </section>

    <!-- 13. 明日交易計畫 -->
    <section id="trading-plan" class="mb-12 scroll-mt-6">
      <h2 class="text-2xl font-bold mb-4 flex items-center gap-2 border-b border-zinc-100 dark:border-zinc-800 pb-2">
        <span class="text-brand-500">13.</span> 明日交易計畫 / 觀察清單
      </h2>
      <div class="space-y-4 text-sm leading-relaxed text-zinc-700 dark:text-zinc-300">
        <div>
          <h3 class="font-semibold text-zinc-900 dark:text-zinc-100 mb-1">13.1 宏觀與指數觀察：</h3>
          <p>密切跟隨10年期美債收益率是否會進一步升穿4.75%警戒線，以及布蘭特原油能否守穩在100美元之上。若債息與油價繼續走高，則大盤成長股仍有去估值風險。技術面上，標普需在明日確認50日均線支撐的有效性，若再度破位跌向7,300點，需大幅降低倉位上限。</p>
        </div>
        <div>
          <h3 class="font-semibold text-zinc-900 dark:text-zinc-100 mb-1">13.2 交易傾向（中性表述）：</h3>
          <p>秉持防守優先、切忌盲目接飛刀的策略。對高溢價半導體（NVDA、AMD、AVGO）轉向觀望，等待大盤情緒平穩及右側止跌信號；可將部分防禦性倉位鎖定在表現強悍的AI電力基建龍頭（VRT、CEG、VST）及高景氣度國防股上。若微軟財報爆雷，則需警惕第二波去槓桿衝擊。</p>
        </div>
      </div>
    </section>

    <!-- 14. 風險提示 -->
    <section id="risks" class="mb-12 scroll-mt-6">
      <h2 class="text-2xl font-bold mb-4 flex items-center gap-2 border-b border-zinc-100 dark:border-zinc-800 pb-2">
        <span class="text-brand-500">14.</span> 風險提示 (Risk Matrix)
      </h2>
      
      <div class="overflow-x-auto border border-zinc-200 dark:border-zinc-800 rounded-xl">
        <table class="min-w-full divide-y divide-zinc-200 dark:divide-zinc-850 text-sm">
          <thead class="bg-zinc-50 dark:bg-zinc-900 font-semibold text-zinc-550 dark:text-zinc-400 text-left">
            <tr>
              <th class="px-4 py-3">風險維度</th>
              <th class="px-4 py-3 text-center">評級</th>
              <th class="px-4 py-3">具體解讀與應對策略</th>
            </tr>
          </thead>
          <tbody class="divide-y divide-zinc-200 dark:divide-zinc-850 text-zinc-700 dark:text-zinc-300">
            <tr>
              <td class="px-4 py-3 font-semibold">宏觀利率風險</td>
              <td class="px-4 py-3 text-center"><span class="px-2 py-0.5 text-xs font-semibold rounded bg-amber-50 text-amber-600 dark:bg-amber-950/40">中高風險</span></td>
              <td class="px-4 py-3 text-xs leading-relaxed">10Y國債收益率飆至4.71%壓制折現率，若油價持續推升通膨，降息可能延遲，科技股估值將繼續承壓。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold">市場寬度與參與度</td>
              <td class="px-4 py-3 text-center"><span class="px-2 py-0.5 text-xs font-semibold rounded bg-amber-50 text-amber-600 dark:bg-amber-950/40">中等風險</span></td>
              <td class="px-4 py-3 text-xs leading-relaxed">上漲家數與短期均線參與比例大幅下降，大資金避險撤離，短期賺錢效應迅速惡化。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold">AI板塊擁擠度</td>
              <td class="px-4 py-3 text-center"><span class="px-2 py-0.5 text-xs font-semibold rounded bg-rose-50 text-rose-600 dark:bg-rose-950/40">高風險</span></td>
              <td class="px-4 py-3 text-xs leading-relaxed">大資金對AI巨額CapEx的ROI質疑正處於情緒爆發期，晶片及硬體板塊面臨系統性獲利盤和對沖拋壓。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold">財報爆冷風險</td>
              <td class="px-4 py-3 text-center"><span class="px-2 py-0.5 text-xs font-semibold rounded bg-rose-50 text-rose-600 dark:bg-rose-950/40">高風險</span></td>
              <td class="px-4 py-3 text-xs leading-relaxed">下週微軟、AMD及Meta季報即將來臨，高估值背景下容錯率極低。若指引不及預期，恐引發二度踩踏。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold">地緣政治風險</td>
              <td class="px-4 py-3 text-center"><span class="px-2 py-0.5 text-xs font-semibold rounded bg-rose-50 text-rose-600 dark:bg-rose-950/40">高風險</span></td>
              <td class="px-4 py-3 text-xs leading-relaxed">中東局勢驟然緊張，紅海衝突推升布油破100美元，大宗商品上漲可能破壞通膨冷卻路徑。</td>
            </tr>
          </tbody>
        </table>
      </div>
    </section>

    <!-- 15. 最終結論 -->
    <section id="conclusion" class="mb-12 scroll-mt-6">
      <h2 class="text-2xl font-bold mb-4 flex items-center gap-2 border-b border-zinc-100 dark:border-zinc-800 pb-2">
        <span class="text-brand-500">15.</span> 最終結論
      </h2>
      <div class="bg-zinc-50/50 dark:bg-zinc-900/50 p-6 rounded-2xl border border-zinc-200/60 dark:border-zinc-800/60 text-sm leading-relaxed text-zinc-700 dark:text-zinc-300">
        <p class="mb-3">
          <strong>今日市場結論：</strong>
          昨夜美股在宏觀（美債收益率與原油雙雙大漲）與微觀（特斯拉、谷歌財報引發AI資本支出焦慮）利空共振下遭遇重挫。大盤避險情緒顯著升溫，大市值科技股及半導體晶片股面臨龐大賣壓，標普跌破20日均線，納指重挫逾2%跌破50日均線，市場短期進入健康修正與避險倉位重組狀態。
        </p>
        <p class="mb-3">
          <strong>當前市場階段：</strong><span class="font-semibold text-rose-500">健康回撤 / 資金防禦性轉移 / 財報避險</span>。
        </p>
        <p class="mb-3">
          <strong>我的操作傾向：</strong>
          短線應當採取克制姿態，降低整體倉位暴露，對高貝塔的半導體科技板塊停止左側接刀，耐心等待下週超級財報週明朗化。中長線可維持對電力（VRT、CEG、VST）及業績爆表的實體防衛板塊（LMT、RTX）的低吸配置。
        </p>
        <p>
          <strong>明日最值得關注的5個訊號：</strong>
          1. 10年期美債收益率是否會繼續向上突破4.75%阻力；2. 布蘭特原油能否守在100美元上方；3. 標普500指數能否在50日均線（7,321點）獲得有效支撐；4. 輝達能否站穩200美元心理關口；5. 保護性看跌期權（Put）的成交量是否持續攀升。
        </p>
      </div>
    </section>

    <footer class="mt-16 pt-8 border-t border-zinc-200 dark:border-zinc-800 text-sm text-zinc-500">
      Generated by the <a href="https://github.com" class="underline hover:text-zinc-900 dark:hover:text-zinc-100"><code>html-report</code></a> Antigravity CLI skill.
    </footer>

  </main>
</div>

<script>
  // Theme toggle
  document.getElementById('theme-toggle').addEventListener('click', () => {
    const dark = document.documentElement.classList.toggle('dark');
    localStorage.theme = dark ? 'dark' : 'light';
    
    // Update chart grid & text colors
    if (window.returnsChartInstance) {
      const isDark = dark;
      window.returnsChartInstance.options.scales.x.grid.color = isDark ? 'rgba(255,255,255,0.08)' : 'rgba(0,0,0,0.05)';
      window.returnsChartInstance.options.scales.x.ticks.color = isDark ? '#a1a1aa' : '#71717a';
      window.returnsChartInstance.options.scales.y.grid.color = isDark ? 'rgba(255,255,255,0.08)' : 'rgba(0,0,0,0.05)';
      window.returnsChartInstance.options.scales.y.ticks.color = isDark ? '#a1a1aa' : '#71717a';
      window.returnsChartInstance.options.plugins.legend.labels.color = isDark ? '#f4f4f5' : '#18181b';
      window.returnsChartInstance.update();
    }

    // Re-init mermaid with new theme if loaded
    if (window.__mermaid) {
      document.querySelectorAll('.mermaid[data-processed]').forEach(el => { 
        el.removeAttribute('data-processed'); 
        el.innerHTML = el.dataset.src || el.textContent; 
      });
      window.__mermaid.initialize({ startOnLoad: false, theme: dark ? 'dark' : 'default', securityLevel: 'loose' });
      window.__mermaid.run();
    }
  });

  // Chart.js: Rendering Returns Comparison Chart
  const ctx = document.getElementById('returnsChart').getContext('2d');
  const isDarkInitial = document.documentElement.classList.contains('dark');
  window.returnsChartInstance = new Chart(ctx, {
    type: 'bar',
    data: {
      labels: ['道瓊工業指數', '標普 500 指數', '納指綜合指數', '納指 100 (QQQ)', '羅素 2000 指數', '費半半導體 (SOXX)', 'VIX 波動率指數'],
      datasets: [{
        label: '單日漲跌幅 (%)',
        data: [-0.97, -1.21, -2.15, -1.90, -0.54, -1.71, 13.70],
        backgroundColor: function(context) {
          const val = context.dataset.data[context.dataIndex];
          return val >= 0 ? 'rgba(16, 185, 129, 0.2)' : 'rgba(239, 68, 68, 0.2)';
        },
        borderColor: function(context) {
          const val = context.dataset.data[context.dataIndex];
          return val >= 0 ? '#10b981' : '#ef4444';
        },
        borderWidth: 1.5,
        borderRadius: 6
      }]
    },
    options: {
      indexAxis: 'y',
      responsive: true,
      maintainAspectRatio: false,
      scales: {
        x: {
          grid: { color: isDarkInitial ? 'rgba(255,255,255,0.08)' : 'rgba(0,0,0,0.05)' },
          ticks: { color: isDarkInitial ? '#a1a1aa' : '#71717a', font: { family: 'mono' } }
        },
        y: {
          grid: { color: isDarkInitial ? 'rgba(255,255,255,0.08)' : 'rgba(0,0,0,0.05)' },
          ticks: { color: isDarkInitial ? '#a1a1aa' : '#71717a', font: { weight: 'bold' } }
        }
      },
      plugins: {
        legend: {
          labels: { color: isDarkInitial ? '#f4f4f5' : '#18181b', font: { weight: 'bold' } }
        },
        tooltip: {
          callbacks: {
            label: function(context) {
              return ' ' + context.dataset.label + ': ' + (context.raw >= 0 ? '+' : '') + context.raw + '%';
            }
          }
        }
      }
    }
  });

  // Table sorting logic
  let currentSortCol = -1;
  let currentSortAsc = true;

  function sortSectors(colIndex) {
    const table = document.getElementById('sectorTable');
    const tbody = table.querySelector('tbody');
    const rows = Array.from(tbody.querySelectorAll('tr'));

    if (currentSortCol === colIndex) {
      currentSortAsc = !currentSortAsc;
    } else {
      currentSortCol = colIndex;
      currentSortAsc = true;
    }

    rows.sort((a, b) => {
      let aVal = a.cells[colIndex].textContent.trim();
      let bVal = b.cells[colIndex].textContent.trim();

      // Handle numeric sort for ranking
      if (colIndex === 0) {
        return currentSortAsc ? parseInt(aVal) - parseInt(bVal) : parseInt(bVal) - parseInt(aVal);
      }
      
      // Handle numeric percentages
      const aValAttr = a.cells[colIndex].getAttribute('data-val');
      const bValAttr = b.cells[colIndex].getAttribute('data-val');
      if (aValAttr !== null && bValAttr !== null) {
        const aNum = parseFloat(aValAttr);
        const bNum = parseFloat(bValAttr);
        return currentSortAsc ? aNum - bNum : bNum - aNum;
      }

      // Default string compare
      return currentSortAsc ? aVal.localeCompare(bVal) : bVal.localeCompare(aVal);
    });

    tbody.innerHTML = '';
    rows.forEach(r => tbody.appendChild(r));
  }

  // Table filtering logic
  function filterSectors() {
    const input = document.getElementById('sectorSearch');
    const filter = input.value.toUpperCase();
    const table = document.getElementById('sectorTable');
    const tbody = table.querySelector('tbody');
    const rows = tbody.getElementsByTagName('tr');

    for (let i = 0; i < rows.length; i++) {
      const cells = rows[i].getElementsByTagName('td');
      let found = false;
      // Search S&P 11 sectors (index 1) and Representative ETF (index 2)
      if (cells[1] || cells[2]) {
        const text1 = cells[1].textContent || cells[1].innerText;
        const text2 = cells[2].textContent || cells[2].innerText;
        if (text1.toUpperCase().indexOf(filter) > -1 || text2.toUpperCase().indexOf(filter) > -1) {
          found = true;
        }
      }
      rows[i].style.display = found ? "" : "none";
    }
  }

  // Sticky TOC scroll-spy
  const tocLinks = document.querySelectorAll('.toc a');
  const sections = [...tocLinks].map(a => document.querySelector(a.getAttribute('href'))).filter(Boolean);
  if (sections.length) {
    const onScroll = () => {
      const y = window.scrollY + 100;
      let active = sections[0];
      for (const s of sections) {
        if (s.offsetTop <= y) active = s;
      }
      tocLinks.forEach(a => a.classList.toggle('active', a.getAttribute('href') === '#' + active.id));
    };
    window.addEventListener('scroll', onScroll, { passive: true });
    onScroll();
  }
</script>

</body>
</html>
"""

target_dir = "/Users/wisdom/html-report-skill/reports"
os.makedirs(target_dir, exist_ok=True)
target_path = os.path.join(target_dir, "2026-07-23-us-stock-closing-daily-report.html")

with open(target_path, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"Report HTML file generated successfully at: {target_path}")

# Run publish.py
publish_script = "/Users/wisdom/html-report-skill/.antigravitycli/skills/html-report/scripts/publish.py"
cmd = [
    "python3",
    publish_script,
    target_path,
    "美股收盤日報｜AI資本支出疑慮引爆科技股大拋售，雙雄財報後特斯拉暴跌14.5%，標普創月內最大單日跌幅！",
    "週四（2026年7月23日），美股遭遇一個月來最慘烈單日拋售，三大指數全線重挫。Alphabet與特斯拉公佈的Q2財報引發市場對AI龐大資本支出回報率（ROI）的集體焦慮。特斯拉因利潤率嚴重承壓崩跌14.52%，Alphabet跌7.13%，拖累科技與晶片板塊大幅下挫。同時，中東局勢再起推升布蘭特原油重返100美元之上，加上10年期美債收益率飆升至4.71%的2026年新高，通隱憂與高利率壓力令風險資產全面失血。標普500指數跌1.21%，納指重挫2.15%，VIX恐慌指數飆升13.70%至18.92。防禦性板塊及公佈超預期業績的國防巨頭洛克希德馬丁（+10.54%）與RTX（+7.5%）逆市大漲護盤。"
]

print(f"Running command: {' '.join(cmd)}")
res = subprocess.run(cmd, capture_output=True, text=True)
print("STDOUT:", res.stdout)
print("STDERR:", res.stderr)
sys.exit(res.returncode)
