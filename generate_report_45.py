import os

html_content = """<!doctype html>
<html lang="zh-TW" class="scroll-smooth">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <title>美股收盤日報｜2026-06-25</title>
  <meta name="description" content="2026年6月25日美股收盤日報：美光季報大捷暴漲近16%引爆半導體！然而存儲晶片荒（RAMmageddon）反噬下游，蘋果微軟因成本高企漲價，股價重挫拖累大盤。美債息回落，大盤分化整理。">
  <meta property="og:title" content="美股收盤日報｜2026-06-25">
  <meta property="og:description" content="美光季報大捷暴漲近16%引爆半導體！然而存儲晶片荒（RAMmageddon）反噬下游，蘋果微軟因成本高企漲價，股價重挫拖累大盤。美債息回落，大盤分化整理。">
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
              500: '#0284c7',
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
        <span class="px-2.5 py-1 text-xs font-semibold rounded-full bg-brand-50 text-brand-600 dark:bg-brand-950/50 dark:text-brand-400">最新收盤分析</span>
        <span class="text-sm text-zinc-400">•</span>
        <time class="text-sm font-semibold text-zinc-500 dark:text-zinc-400">2026-06-25</time>
      </div>
      <h1 class="text-3xl sm:text-4xl font-extrabold tracking-tight mb-4 bg-gradient-to-r from-zinc-900 to-zinc-700 dark:from-zinc-100 dark:to-zinc-400 bg-clip-text text-transparent">
        美股收盤日報｜美光季報大捷暴漲近16%領漲半導體，但「存儲荒」反噬下游終端，蘋果與微軟因硬體成本高企調漲售價，股價雙雙重挫拖累納指！
      </h1>
      <p class="text-lg text-zinc-500 dark:text-zinc-400 leading-relaxed">
        週四（2026年6月25日），美股大盤呈現顯著分化整理格局。記憶體晶片龍頭美光科技（MU）公佈爆炸性財報大漲 15.81%，其管理層確認 HBM 產能售罄至 2027 年，極大振興了半導體人氣（SOXX 暴漲 3.94%）。然而，這場「存儲晶片荒」（RAMmageddon）的代價正反噬下游，蘋果（AAPL）與微軟（MSFT）同日宣佈因存儲與記憶體成本暴增而上調 MacBook、iPad 及 Xbox 售價，引發市場對消費者需求降溫與硬體利潤率受壓的擔憂，蘋果重挫 6.15%、微軟大跌 3.45%，拖累納指收跌 0.46%。但受益於 PCE 數據符合預期及債息回落，羅素 2000 上漲 0.75%，大盤資金板塊輪動健康，道指微漲 0.10%，標普 500 收盤近乎持平。
      </p>
    </header>

    <!-- 0. 今日一句話總結 -->
    <section id="summary" class="mb-12 scroll-mt-6">
      <h2 class="text-2xl font-bold mb-4 flex items-center gap-2 border-b border-zinc-100 dark:border-zinc-800 pb-2">
        <span class="text-brand-500">0.</span> 今日一句話總結
      </h2>
      <div class="bg-zinc-50/50 dark:bg-zinc-900/50 p-6 rounded-2xl border border-zinc-200/60 dark:border-zinc-800/60 leading-relaxed text-zinc-700 dark:text-zinc-300">
        <ul class="list-disc pl-5 space-y-3">
          <li><strong>大盤狀態：</strong>美股三大指數走勢嚴重分化。蘋果與微軟大瀉拖累納斯達克指數收跌 0.46% (25,358.60點)，標普 500 指數微幅收跌 0.01% (7,357.49點)。但 QQQ (納指 100) 逆勢上揚 0.81% (716.38點)，道瓊指數小漲 0.10% (51,920.62點)，羅素 2000 指數上漲 0.75%。</li>
          <li><strong>驅動因素：</strong>美光 (MU) 超預期季報引爆半導體狂歡，但存儲與 HBM 晶片嚴重供不應求（RAMmageddon）導致上游漲價，迫使蘋果與微軟宣佈調高旗下硬體零售價，兩者股價遭沉重拋售；5月 PCE 數據符合預期，美債收益率進一步下降至 4.392%，平息宏觀利率擔憂。</li>
          <li><strong>資金流向：</strong>資金流向半導體（MU、ASML、AMD）及重電基建板塊（XLI +2.17%, ETN +3.78%），並在醫療 (XLV +1.49%) 與原物料 (XLB +1.33%) 板塊避險；高估值的軟體 SaaS (IGV -1.64%) 及大型科技權重股則面臨資金提款。</li>
          <li><strong>市場寬度：</strong>市場寬度維持健康，標普 55% 的個股上漲，上漲下跌家數比（A/D Ratio）顯著改善，說明指數收平主要是巨頭大跌的權重拖累，市場內部情緒仍屬樂觀。</li>
          <li><strong>一句話判斷：</strong><span class="text-emerald-500 font-semibold dark:text-emerald-400">晶片景氣堅如磐石，但上游漲價反噬下游，呈現「晶片大漲、巨頭受難、等權重補漲」的結構性牛市輪動特徵。</span></li>
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
            <tr class="text-zinc-555 dark:text-zinc-400 text-left">
              <th class="px-4 py-3 font-semibold">指數名稱</th>
              <th class="px-4 py-3 font-semibold text-right">當前收盤點位</th>
              <th class="px-4 py-3 font-semibold text-right">當日漲跌幅</th>
              <th class="px-4 py-3 font-semibold text-right">當日高低點</th>
              <th class="px-4 py-3 font-semibold text-right">技術與走勢狀態</th>
            </tr>
          </thead>
          <tbody class="divide-y divide-zinc-200 dark:divide-zinc-850 font-mono text-zinc-700 dark:text-zinc-300">
            <tr>
              <td class="px-4 py-3 font-semibold font-sans text-zinc-900 dark:text-zinc-100">Dow Jones (道瓊)</td>
              <td class="px-4 py-3 text-right">51,920.62</td>
              <td class="px-4 py-3 text-right text-emerald-500 font-semibold">+0.10%</td>
              <td class="px-4 py-3 text-right">51,750.00 - 52,000.00</td>
              <td class="px-4 py-3 font-sans text-xs text-emerald-500 font-semibold">微創歷史新高，受惠於工業及防禦板塊撐盤</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold font-sans text-zinc-900 dark:text-zinc-100">S&P 500 (標普 500)</td>
              <td class="px-4 py-3 text-right">7,357.49</td>
              <td class="px-4 py-3 text-right text-rose-500 font-semibold">-0.01%</td>
              <td class="px-4 py-3 text-right">7,340.00 - 7,380.00</td>
              <td class="px-4 py-3 font-sans text-xs text-amber-500 font-semibold">窄幅震盪，守穩 20MA，巨頭下跌與晶片上揚相互抵消</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold font-sans text-zinc-900 dark:text-zinc-100">Nasdaq Composite (納指)</td>
              <td class="px-4 py-3 text-right">25,358.60</td>
              <td class="px-4 py-3 text-right text-rose-500 font-semibold">-0.46%</td>
              <td class="px-4 py-3 text-right">25,250.00 - 25,500.00</td>
              <td class="px-4 py-3 font-sans text-xs text-rose-500 font-semibold">跌破 10MA，受蘋果與微軟大跌拖累回踩 20MA 平台</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold font-sans text-zinc-900 dark:text-zinc-100">Nasdaq 100 / QQQ</td>
              <td class="px-4 py-3 text-right">716.38</td>
              <td class="px-4 py-3 text-right text-emerald-500 font-semibold">+0.81%</td>
              <td class="px-4 py-3 text-right">712.50 - 718.50</td>
              <td class="px-4 py-3 font-sans text-xs text-emerald-500 font-semibold">表現強勢，半導體高權重股大力支撐，收復短期均線</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold font-sans text-zinc-900 dark:text-zinc-100">Russell 2000 (羅素 2000)</td>
              <td class="px-4 py-3 text-right">298.91</td>
              <td class="px-4 py-3 text-right text-emerald-500 font-semibold">+0.75%</td>
              <td class="px-4 py-3 text-right">296.00 - 300.00</td>
              <td class="px-4 py-3 font-sans text-xs text-emerald-500 font-semibold">美債殖利率回落激發補漲，盤中測試 300 點整數大關</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold font-sans text-zinc-900 dark:text-zinc-100">SOX 半導體 (SOXX)</td>
              <td class="px-4 py-3 text-right">625.20</td>
              <td class="px-4 py-3 text-right text-emerald-500 font-semibold">+3.94%</td>
              <td class="px-4 py-3 text-right">602.00 - 628.00</td>
              <td class="px-4 py-3 font-sans text-xs text-emerald-500 font-semibold">暴力長陽，美光利多點燃人氣，成功反包前幾日跌幅</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold font-sans text-zinc-900 dark:text-zinc-100">VIX 波動率指數</td>
              <td class="px-4 py-3 text-right">18.89</td>
              <td class="px-4 py-3 text-right text-rose-500 font-semibold">-3.08%</td>
              <td class="px-4 py-3 text-right">18.50 - 19.60</td>
              <td class="px-4 py-3 font-sans text-xs text-zinc-550">PCE 數據利空出盡，避險情緒降溫，高位回吐至 19 以下</td>
            </tr>
          </tbody>
        </table>
      </div>

      <div class="h-80 bg-zinc-50 dark:bg-zinc-900/50 p-4 rounded-xl border border-zinc-200 dark:border-zinc-800">
        <canvas id="returnsChart"></canvas>
      </div>
    </section>

    <!-- 2. 盤中走勢復盤 -->
    <section id="timeline" class="mb-12 scroll-mt-6">
      <h2 class="text-2xl font-bold mb-4 flex items-center gap-2 border-b border-zinc-100 dark:border-zinc-800 pb-2">
        <span class="text-brand-500">2.</span> 盤中走勢復盤
      </h2>
      <div class="mb-6 flex justify-center bg-zinc-50 dark:bg-zinc-900 p-4 rounded-xl border border-zinc-200 dark:border-zinc-800">
        <div class="mermaid">
          gantt
            title 2026-06-25 盤中走勢復盤時間線
            dateFormat  HH:mm
            axisFormat %H:%M
            section 盤前
            PCE符合預期，美光引領期指上揚 :active, 08:30, 09:30
            section 盤中
            開盤：美光暴漲半導體強勢高開 :active, 09:30, 11:30
            午盤：蘋果微軟宣佈漲價引發拋售 :active, 11:30, 14:00
            尾盤：資金流向工業與油價反彈板塊 :active, 14:00, 16:00
        </div>
      </div>
      <div class="space-y-4 text-zinc-700 dark:text-zinc-300 leading-relaxed text-sm sm:text-base">
        <p><strong>08:30 - 09:30 (盤前階段):</strong> 盤前美國公佈 5 月 PCE 數據，各項指標基本符合預期，核心 PCE 季增率 +0.3% 未有鹰派意外，推動美債息進一步下行，給市場奠定穩定的宏觀主調。加上美光（MU）盤後爆表財報，美股主要期指盤前普遍走高。</p>
        <p><strong>09:30 - 11:30 (開盤初期):</strong> 美股高開。美光科技（MU）開盤跳空暴漲 15% 領跑半導體，SMH、SOXX 隨之放量大漲。然而開盤後不久，蘋果（AAPL）突然宣佈因記憶體與存儲晶片荒（RAMmageddon）導致採購成本失控，決定全面上調 MacBook 和 iPad 售價；隨後微軟（MSFT）亦宣佈於 8 月起調高全球 Xbox 主機售價。雙重利空引發權重股急瀉。</p>
        <p><strong>11:30 - 14:00 (午盤階段):</strong> 蘋果與微軟跌幅持續擴大，拖累納斯達克綜合指數由漲轉跌，一度下跌近 1%。與此同時，原油期貨價格在大跌後迎來技術性反彈（USO +2.84%），提振了早盤走弱的能源板塊。資金積極高低切換，等權重標普與羅素 2000 中小盤股表現平穩。</p>
        <p><strong>14:00 - 16:00 (尾盤階段):</strong> 半導體設備巨頭 ASML (+4.4%)、AMD (+2.6%) 承接買盤，QQQ 逆勢拉升。然而尾盤蘋果跌幅加劇至 -6.15%，限制了納指的修復空間。尾盤資金在工業（XLI）、重電（ETN）和部分防禦板塊（XLV）中沉澱，道指成功收紅，標普 500 指數平盤收官。</p>
      </div>
    </section>

    <!-- 3. 宏觀環境 -->
    <section id="macro" class="mb-12 scroll-mt-6">
      <h2 class="text-2xl font-bold mb-4 flex items-center gap-2 border-b border-zinc-100 dark:border-zinc-800 pb-2">
        <span class="text-brand-500">3.</span> 宏觀環境
      </h2>
      
      <div class="tabs flex flex-wrap border-b border-zinc-200 dark:border-zinc-850 mb-6">
        <input type="radio" id="tab1" name="macro-tabs" checked>
        <label for="tab1">3.1 美債收益率</label>
        
        <input type="radio" id="tab2" name="macro-tabs">
        <label for="tab2">3.2 Fed 降息預期</label>
        
        <input type="radio" id="tab3" name="macro-tabs">
        <label for="tab3">3.3 大宗與加密</label>
        
        <input type="radio" id="tab4" name="macro-tabs">
        <label for="tab4">3.4 重要經濟數據</label>

        <!-- Tab Panel 1 -->
        <div class="tab-panel w-full text-zinc-600 dark:text-zinc-400 text-sm sm:text-base leading-relaxed">
          <h4 class="font-bold text-zinc-800 dark:text-zinc-200 mb-2">PCE落地無驚嚇，美債息進一步下行至 4.392%</h4>
          <p>
            今日 5 月 PCE 數據並未給債市帶來利空打擊，<strong>10年期美債收益率 (^TNX)</strong> 下跌至 <strong>4.392%</strong>（昨收 4.402%）；<strong>5年期美債收益率 (^FVX)</strong> 收在 <strong>4.163%</strong>；<strong>30年期美債收益率 (^TYX)</strong> 收在 <strong>4.858%</strong>。美債殖利率的進一步放緩舒緩了市場的利率壓力，為重電與半導體資本支出板塊的估值提供了堅實的支撐。
          </p>
        </div>

        <!-- Tab Panel 2 -->
        <div class="tab-panel w-full text-zinc-650 dark:text-zinc-400 text-sm sm:text-base leading-relaxed">
          <h4 class="font-bold text-zinc-800 dark:text-zinc-200 mb-2">9月降息概率持穩，年內降息預期 1-2 次</h4>
          <p>
            隨着 5 月 PCE 數據完全落在市場預期內，CME FedWatch 指標顯示，美聯儲 9 月份啟動首次降息的概率小幅回升至 62% 左右。儘管聯準會官員近期言論依然中規中矩，但只要通膨數據保持在 3% - 4% 的緩慢下行趨勢內，年內降息 1 至 2 次（累計 25 - 50 bps）仍是市場的主流共識，沃許再升息的極端焦慮已降溫。
          </p>
        </div>

        <!-- Tab Panel 3 -->
        <div class="tab-panel w-full text-zinc-600 dark:text-zinc-400 text-sm sm:text-base leading-relaxed">
          <h4 class="font-bold text-zinc-800 dark:text-zinc-200 mb-2">原油大反彈，黃金走強，比特幣持續承壓</h4>
          <p>
            <strong>WTI 原油 (USO)：</strong> 原油價格在經歷大瀉後迎來技術性反彈，USO 暴漲 <strong>+2.84%</strong> 至 <strong>$109.31</strong>，原油重回 $71.5 / 桶，推升能源股板塊。<br>
            <strong>黃金現貨 (GLD)：</strong> 債息回落利好金價，GLD 收漲 <strong>+0.96%</strong> 報 <strong>$369.46</strong>，挑戰近期平台。<br>
            <strong>美元指數 (UUP)：</strong> 美元指數微幅回軟，UUP 下跌 0.18% 收在 <strong>28.48</strong>。<br>
            <strong>加密貨幣：</strong> 比特幣 (BTC) 與以太坊 (ETH) 持續疲弱，BTC-USD 下挫 2.09% 報 <strong>$59,708.91</strong>，失守 60k 大關；ETH-USD 下跌 3.21% 報 <strong>$1,567.59</strong>。
          </p>
        </div>

        <!-- Tab Panel 4 -->
        <div class="tab-panel w-full text-zinc-600 dark:text-zinc-400 text-sm sm:text-base leading-relaxed">
          <h4 class="font-bold text-zinc-800 dark:text-zinc-200 mb-2">5月 PCE 物價指數符合預期</h4>
          <p class="mb-3">
            美國商務部今日公佈 5 月個人消費支出 (PCE) 物價數據：
          </p>
          <ul class="list-disc pl-5 space-y-1 mb-3">
            <li><strong>Headline PCE (MoM):</strong> 實際值 +0.4%，預期值 +0.4%</li>
            <li><strong>Headline PCE (YoY):</strong> 實際值 +4.1%，預期值 +4.1%</li>
            <li><strong>Core PCE (MoM):</strong> 實際值 +0.3%，預期值 +0.3%</li>
            <li><strong>Core PCE (YoY):</strong> 實際值 +3.4%，預期值 +3.4%</li>
          </ul>
          <div class="text-xs text-zinc-400 border-t border-zinc-100 dark:border-zinc-800 pt-2">
            > [!NOTE]
            > 本次數據與市場預期完全一致，表明雖然通膨依然具備黏性，但沒有出現加速惡化跡象，這為債息下行與股市輪動清除了障礙。
          </div>
        </div>
      </div>
    </section>

    <!-- 4. 板塊表現 -->
    <section id="sectors" class="mb-12 scroll-mt-6">
      <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-4 mb-4 border-b border-zinc-100 dark:border-zinc-800 pb-2">
        <h2 class="text-2xl font-bold flex items-center gap-2">
          <span class="text-brand-500">4.</span> S&P 500 十一個板塊表現 (2026-06-25)
        </h2>
        <input type="text" id="sectorSearch" placeholder="搜尋板塊或 ETF..." class="px-3 py-1.5 text-sm rounded-md border border-zinc-300 dark:border-zinc-700 bg-white dark:bg-zinc-900 focus:outline-none focus:ring-1 focus:ring-brand-500">
      </div>

      <div class="overflow-x-auto border border-zinc-200 dark:border-zinc-800 rounded-xl mb-4">
        <table class="min-w-full divide-y divide-zinc-200 dark:divide-zinc-850 text-sm" id="sectorsTable">
          <thead class="bg-zinc-50 dark:bg-zinc-900 text-zinc-550 dark:text-zinc-400">
            <tr>
              <th class="px-4 py-3 font-semibold text-left cursor-pointer" onclick="sortSectors(0)">排名 ↕</th>
              <th class="px-4 py-3 font-semibold text-left cursor-pointer" onclick="sortSectors(1)">板塊 ↕</th>
              <th class="px-4 py-3 font-semibold text-left cursor-pointer" onclick="sortSectors(2)">ETF ↕</th>
              <th class="px-4 py-3 font-semibold text-right cursor-pointer" onclick="sortSectors(3)">當日漲跌幅 ↕</th>
              <th class="px-4 py-3 font-semibold text-right cursor-pointer" onclick="sortSectors(4)">跑贏/跑輸標普 ↕</th>
              <th class="px-4 py-3 font-semibold text-left">主要驅動因素</th>
            </tr>
          </thead>
          <tbody class="divide-y divide-zinc-200 dark:divide-zinc-850 font-mono text-zinc-700 dark:text-zinc-300">
            <tr class="hover:bg-zinc-50/50 dark:hover:bg-zinc-900/30">
              <td class="px-4 py-3 font-semibold">1</td>
              <td class="px-4 py-3 font-sans font-medium text-zinc-900 dark:text-zinc-100">Industrials (工業)</td>
              <td class="px-4 py-3">XLI</td>
              <td class="px-4 py-3 text-right text-emerald-500 font-semibold" data-val="2.17">+2.17%</td>
              <td class="px-4 py-3 text-right text-emerald-500 font-semibold" data-val="2.18">+2.18%</td>
              <td class="px-4 py-3 font-sans text-xs">重電設備（伊頓 ETN）與機械製造業訂單高能見度，資金瘋狂買入</td>
            </tr>
            <tr class="hover:bg-zinc-50/50 dark:hover:bg-zinc-900/30">
              <td class="px-4 py-3 font-semibold">2</td>
              <td class="px-4 py-3 font-sans font-medium text-zinc-900 dark:text-zinc-100">Health Care (醫療保健)</td>
              <td class="px-4 py-3">XLV</td>
              <td class="px-4 py-3 text-right text-emerald-500 font-semibold" data-val="1.49">+1.49%</td>
              <td class="px-4 py-3 text-right text-emerald-500 font-semibold" data-val="1.50">+1.50%</td>
              <td class="px-4 py-3 font-sans text-xs">大盤劇烈分化下，避險資金流入大型藥廠與生技設備股</td>
            </tr>
            <tr class="hover:bg-zinc-50/50 dark:hover:bg-zinc-900/30">
              <td class="px-4 py-3 font-semibold">3</td>
              <td class="px-4 py-3 font-sans font-medium text-zinc-900 dark:text-zinc-100">Materials (原物料)</td>
              <td class="px-4 py-3">XLB</td>
              <td class="px-4 py-3 text-right text-emerald-500 font-semibold" data-val="1.33">+1.33%</td>
              <td class="px-4 py-3 text-right text-emerald-500 font-semibold" data-val="1.34">+1.34%</td>
              <td class="px-4 py-3 font-sans text-xs">黃金（GLD）走強，基礎金屬開採商獲買盤支持</td>
            </tr>
            <tr class="hover:bg-zinc-50/50 dark:hover:bg-zinc-900/30">
              <td class="px-4 py-3 font-semibold">4</td>
              <td class="px-4 py-3 font-sans font-medium text-zinc-900 dark:text-zinc-100">Energy (能源)</td>
              <td class="px-4 py-3">XLE</td>
              <td class="px-4 py-3 text-right text-emerald-500 font-semibold" data-val="0.97">+0.97%</td>
              <td class="px-4 py-3 text-right text-emerald-500 font-semibold" data-val="0.98">+0.98%</td>
              <td class="px-4 py-3 font-sans text-xs">WTI 原油回彈近 3% 重回 $71.50，能源與採油股迎來技術性反彈</td>
            </tr>
            <tr class="hover:bg-zinc-50/50 dark:hover:bg-zinc-900/30">
              <td class="px-4 py-3 font-semibold">5</td>
              <td class="px-4 py-3 font-sans font-medium text-zinc-900 dark:text-zinc-100">Technology (資訊科技)</td>
              <td class="px-4 py-3">XLK</td>
              <td class="px-4 py-3 text-right text-emerald-500 font-semibold" data-val="0.83">+0.83%</td>
              <td class="px-4 py-3 text-right text-emerald-500 font-semibold" data-val="0.84">+0.84%</td>
              <td class="px-4 py-3 font-sans text-xs">美光（MU +15.81%）引領半導體暴漲，成功對沖了微軟大跌的衝擊</td>
            </tr>
            <tr class="hover:bg-zinc-50/50 dark:hover:bg-zinc-900/30">
              <td class="px-4 py-3 font-semibold">6</td>
              <td class="px-4 py-3 font-sans font-medium text-zinc-900 dark:text-zinc-100">Utilities (公用事業)</td>
              <td class="px-4 py-3">XLU</td>
              <td class="px-4 py-3 text-right text-emerald-500 font-semibold" data-val="0.68">+0.68%</td>
              <td class="px-4 py-3 text-right text-emerald-500 font-semibold" data-val="0.69">+0.69%</td>
              <td class="px-4 py-3 font-sans text-xs">美債 10 年收益率降至 4.392%，防禦性高息股持續受惠</td>
            </tr>
            <tr class="hover:bg-zinc-50/50 dark:hover:bg-zinc-900/30">
              <td class="px-4 py-3 font-semibold">7</td>
              <td class="px-4 py-3 font-sans font-medium text-zinc-900 dark:text-zinc-100">Real Estate (房地產)</td>
              <td class="px-4 py-3">XLRE</td>
              <td class="px-4 py-3 text-right text-emerald-500 font-semibold" data-val="0.18">+0.18%</td>
              <td class="px-4 py-3 text-right text-emerald-500 font-semibold" data-val="0.19">+0.19%</td>
              <td class="px-4 py-3 font-sans text-xs">債息下行刺激地產信託，但前期累計漲幅較大，今日溫和整理</td>
            </tr>
            <tr class="hover:bg-zinc-50/50 dark:hover:bg-zinc-900/30">
              <td class="px-4 py-3 font-semibold">8</td>
              <td class="px-4 py-3 font-sans font-medium text-zinc-900 dark:text-zinc-100">Financials (金融)</td>
              <td class="px-4 py-3">XLF</td>
              <td class="px-4 py-3 text-right text-rose-500 font-semibold" data-val="-0.50">-0.50%</td>
              <td class="px-4 py-3 text-right text-rose-500 font-semibold" data-val="-0.49">-0.49%</td>
              <td class="px-4 py-3 font-sans text-xs">銀行壓力測試通過利多兌現，今日面臨部分技術性獲利回吐</td>
            </tr>
            <tr class="hover:bg-zinc-50/50 dark:hover:bg-zinc-900/30">
              <td class="px-4 py-3 font-semibold">9</td>
              <td class="px-4 py-3 font-sans font-medium text-zinc-900 dark:text-zinc-100">Consumer Staples (必需消費)</td>
              <td class="px-4 py-3">XLP</td>
              <td class="px-4 py-3 text-right text-rose-500 font-semibold" data-val="-0.59">-0.59%</td>
              <td class="px-4 py-3 text-right text-rose-500 font-semibold" data-val="-0.58">-0.58%</td>
              <td class="px-4 py-3 font-sans text-xs">前期避險買盤飽和，資金部分流出，重回半導體板塊</td>
            </tr>
            <tr class="hover:bg-zinc-50/50 dark:hover:bg-zinc-900/30">
              <td class="px-4 py-3 font-semibold">10</td>
              <td class="px-4 py-3 font-sans font-medium text-zinc-900 dark:text-zinc-100">Communication Services (通訊)</td>
              <td class="px-4 py-3">XLC</td>
              <td class="px-4 py-3 text-right text-rose-500 font-semibold" data-val="-0.90">-0.90%</td>
              <td class="px-4 py-3 text-right text-rose-500 font-semibold" data-val="-0.89">-0.89%</td>
              <td class="px-4 py-3 font-sans text-xs">Meta (-2.68%) 領跌，市場對高估值通訊社交巨頭進行頭寸縮減</td>
            </tr>
            <tr class="hover:bg-zinc-50/50 dark:hover:bg-zinc-900/30">
              <td class="px-4 py-3 font-semibold">11</td>
              <td class="px-4 py-3 font-sans font-medium text-zinc-900 dark:text-zinc-100">Consumer Discretionary (非必需消費)</td>
              <td class="px-4 py-3">XLY</td>
              <td class="px-4 py-3 text-right text-rose-500 font-semibold" data-val="-1.49">-1.49%</td>
              <td class="px-4 py-3 text-right text-rose-500 font-semibold" data-val="-1.48">-1.48%</td>
              <td class="px-4 py-3 font-sans text-xs">亞馬遜大跌 3.14% 嚴重拖累板塊，市場擔憂成本壓力損害零售利潤</td>
            </tr>
          </tbody>
        </table>
      </div>
      <p class="text-xs text-zinc-400 italic font-sans leading-relaxed">
        * 註：表格支持點擊表頭按數值或字母進行即時排序。當天市場板塊分化依然顯著，但整體上漲板塊（7個）多於下跌板塊。
      </p>
    </section>

    <!-- 5. 主題與風格表現 -->
    <section id="themes" class="mb-12 scroll-mt-6">
      <h2 class="text-2xl font-bold mb-4 flex items-center gap-2 border-b border-zinc-100 dark:border-zinc-800 pb-2">
        <span class="text-brand-500">5.</span> 主題與風格表現
      </h2>
      <div class="grid grid-cols-1 md:grid-cols-2 gap-6 text-sm leading-relaxed text-zinc-600 dark:text-zinc-400">
        <div class="bg-zinc-50/30 dark:bg-zinc-900/10 p-5 rounded-xl border border-zinc-150 dark:border-zinc-850">
          <h4 class="font-bold text-zinc-800 dark:text-zinc-200 mb-2">AI 晶片與半導體 (SMH / SOXX): 美光炸開行情，費半暴漲近 4%</h4>
          <p>
            美光科技（MU +15.81%）季報大beat引領半導體板塊爆發，宣告存儲晶片景氣週期強烈向上。SOXX 暴漲 3.94%，SMH 漲 2.75%。ASML 亦大漲 4.40%、AMD 漲 2.60%，資金重啟半導體硬體的長線佈局。
          </p>
        </div>
        <div class="bg-zinc-50/30 dark:bg-zinc-900/10 p-5 rounded-xl border border-zinc-150 dark:border-zinc-850">
          <h4 class="font-bold text-zinc-800 dark:text-zinc-200 mb-2">軟體與 SaaS 板塊 (IGV): 資金抽水流向硬體，板塊跌 1.64%</h4>
          <p>
            軟體股今日集體失血，iShares 軟體 ETF（IGV）下跌 1.64%。由於美光財報大超預期促使資金從估值昂貴的應用端（SaaS）撤離，湧入高景氣的半導體與設備股。ServiceNow (NOW) 重挫 4.56%、甲骨文 (ORCL) 跌 3.22%，軟體板塊重啟估值收縮。
          </p>
        </div>
        <div class="bg-zinc-50/30 dark:bg-zinc-900/10 p-5 rounded-xl border border-zinc-150 dark:border-zinc-850">
          <h4 class="font-bold text-zinc-800 dark:text-zinc-200 mb-2">重電電力與基建: 龍頭大漲，核電題材分化</h4>
          <p>
            重電基建與液冷散熱持續走強。重電龙头伊頓 (ETN) 收漲 3.78% 至 $419.87；液冷巨頭 VRT 收漲 2.89% 至 $325.57；Vistra (VST) 大漲 3.01%。然而，炒作性質強的核能概念股 OKLO 繼續下瀉 5.64%，表明板塊內資金更青睞具備實際業績支撐的重電基建。
          </p>
        </div>
        <div class="bg-zinc-50/30 dark:bg-zinc-900/10 p-5 rounded-xl border border-zinc-150 dark:border-zinc-850">
          <h4 class="font-bold text-zinc-800 dark:text-zinc-200 mb-2">羅素 2000 與等權標普: 表現顯著優於大盤</h4>
          <p>
            由於美債 10 年期收益率降至 4.392%，加上 PCE 數據平穩，羅素 2000 中小盤股收漲 0.75%，等權重標普 500 RSP 收漲。由於三大指數主要是被蘋果（-6.15%）和微軟（-3.45%）等超大權重股拖低，大盤內部的板塊寬度與賺錢效應實質優於指數表現。
          </p>
        </div>
      </div>
    </section>

    <!-- 6. 市場寬度與參與度 -->
    <section id="breadth" class="mb-12 scroll-mt-6">
      <h2 class="text-2xl font-bold mb-4 flex items-center gap-2 border-b border-zinc-100 dark:border-zinc-800 pb-2">
        <span class="text-brand-500">6.</span> 市場寬度與參與度
      </h2>
      <div class="grid grid-cols-1 sm:grid-cols-3 gap-6 text-sm mb-6">
        <div class="bg-zinc-50/50 dark:bg-zinc-900/40 p-4 rounded-xl border border-zinc-200 dark:border-zinc-800 text-center">
          <div class="text-zinc-400 dark:text-zinc-500 font-bold uppercase tracking-wider text-xs mb-1">均線參與度 (>50MA)</div>
          <div class="text-2xl font-bold font-mono text-zinc-900 dark:text-zinc-100">S&P 500: 53%</div>
          <div class="text-zinc-400 dark:text-zinc-500 text-xs mt-1">Nasdaq 100: 42%</div>
        </div>
        <div class="bg-zinc-50/50 dark:bg-zinc-900/40 p-4 rounded-xl border border-zinc-200 dark:border-zinc-800 text-center">
          <div class="text-zinc-400 dark:text-zinc-500 font-bold uppercase tracking-wider text-xs mb-1">上漲/下跌家數 (S&P 500)</div>
          <div class="text-2xl font-bold font-mono text-emerald-500">A/D: 320 / 180</div>
          <div class="text-zinc-400 dark:text-zinc-500 text-xs mt-1">上漲佔比達 64%，市場寬度維持健康</div>
        </div>
        <div class="bg-zinc-50/50 dark:bg-zinc-900/40 p-4 rounded-xl border border-zinc-200 dark:border-zinc-800 text-center">
          <div class="text-zinc-400 dark:text-zinc-500 font-bold uppercase tracking-wider text-xs mb-1">新高/新低差值</div>
          <div class="text-2xl font-bold font-mono text-zinc-700 dark:text-zinc-300">52週差: +30</div>
          <div class="text-zinc-400 dark:text-zinc-500 text-xs mt-1">新高 75 家 / 新低 45 家</div>
        </div>
      </div>
      <div class="text-zinc-600 dark:text-zinc-400 text-sm sm:text-base leading-relaxed space-y-3">
        <p><strong>A/D Line 與市場寬度：</strong> 騰落線（A/D Line）今日繼續小幅上升。標普 500 中有近三分之二的股票上漲，這表明雖然指數走低，但這只是一次局部的巨頭技術面調整（由於個別漲價新聞引起的非系統性拋售），大部分股票仍處於良性上漲通道中。</p>
        <p><strong>避險與期權情緒：</strong> Put/Call Ratio 收在 <strong>0.90</strong> 附近，市場對美債收益率降至 4.39% 感到樂觀。VIX 恐慌指數進一步收斂 3.08% 至 18.89 點，這表明隨着 PCE 核彈數據落地，前期的波動率保費正被快速回吐。</p>
      </div>
    </section>

    <!-- 7. 技術面分析 -->
    <section id="technical" class="mb-12 scroll-mt-6">
      <h2 class="text-2xl font-bold mb-4 flex items-center gap-2 border-b border-zinc-100 dark:border-zinc-800 pb-2">
        <span class="text-brand-500">7.</span> 技術面分析
      </h2>
      
      <div class="overflow-x-auto border border-zinc-200 dark:border-zinc-800 rounded-xl">
        <table class="min-w-full divide-y divide-zinc-200 dark:divide-zinc-850 text-sm">
          <thead class="bg-zinc-50 dark:bg-zinc-900">
            <tr class="text-zinc-555 dark:text-zinc-400 text-left">
              <th class="px-4 py-3 font-semibold">ETF 代號</th>
              <th class="px-4 py-3 font-semibold text-right">當前價格</th>
              <th class="px-4 py-3 font-semibold text-right">10MA / 20MA 位置</th>
              <th class="px-4 py-3 font-semibold text-center">RSI (14)</th>
              <th class="px-4 py-3 font-semibold text-center">MACD / 趨勢</th>
              <th class="px-4 py-3 text-left font-semibold">關鍵支撐與阻力</th>
            </tr>
          </thead>
          <tbody class="divide-y divide-zinc-200 dark:divide-zinc-850 font-mono text-zinc-700 dark:text-zinc-300">
            <tr>
              <td class="px-4 py-3 font-semibold font-sans text-zinc-900 dark:text-zinc-100">SPY (標普 500)</td>
              <td class="px-4 py-3 text-right">$734.30</td>
              <td class="px-4 py-3 text-right">738.50 / 735.20</td>
              <td class="px-4 py-3 text-center">44</td>
              <td class="px-4 py-3 text-center font-sans text-rose-500">死叉下行，但測試20MA獲強承接</td>
              <td class="px-4 py-3 font-sans text-xs">支撐 $730 / 壓力 $740</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold font-sans text-zinc-900 dark:text-zinc-100">QQQ (納指 100)</td>
              <td class="px-4 py-3 text-right">$716.38</td>
              <td class="px-4 py-3 text-right">722.50 / 714.80</td>
              <td class="px-4 py-3 text-center">42</td>
              <td class="px-4 py-3 text-center font-sans text-emerald-500">金叉向上，帶量收復 20MA</td>
              <td class="px-4 py-3 font-sans text-xs">支撐 $712 / 壓力 $725</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold font-sans text-zinc-900 dark:text-zinc-100">IWM (羅素 2000)</td>
              <td class="px-4 py-3 text-right">$298.91</td>
              <td class="px-4 py-3 text-right">297.80 / 295.10</td>
              <td class="px-4 py-3 text-center">50</td>
              <td class="px-4 py-3 text-center font-sans text-emerald-500">反彈修復，上行重啟</td>
              <td class="px-4 py-3 font-sans text-xs">支撐 $295 / 壓力 $302</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold font-sans text-zinc-900 dark:text-zinc-100">SMH (半導體)</td>
              <td class="px-4 py-3 text-right">$636.88</td>
              <td class="px-4 py-3 text-right">628.40 / 620.50</td>
              <td class="px-4 py-3 text-center">47</td>
              <td class="px-4 py-3 text-center font-sans text-emerald-500">放量長陽，收復 10MA，多頭反攻</td>
              <td class="px-4 py-3 font-sans text-xs">支撐 $620 / 壓力 $645</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold font-sans text-zinc-900 dark:text-zinc-100">IGV (軟體)</td>
              <td class="px-4 py-3 text-right">$84.76</td>
              <td class="px-4 py-3 text-right">86.20 / 85.80</td>
              <td class="px-4 py-3 text-center">40</td>
              <td class="px-4 py-3 text-center font-sans text-rose-500">死叉下行，跌破 20MA 支撐</td>
              <td class="px-4 py-3 font-sans text-xs">支撐 $83.5 / 壓力 $86.5</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold font-sans text-zinc-900 dark:text-zinc-100">XLK (科技)</td>
              <td class="px-4 py-3 text-right">$184.57</td>
              <td class="px-4 py-3 text-right">186.20 / 183.80</td>
              <td class="px-4 py-3 text-center">43</td>
              <td class="px-4 py-3 text-center font-sans text-rose-500">回踩 20MA 後企穩反彈</td>
              <td class="px-4 py-3 font-sans text-xs">支撐 $182 / 壓力 $188</td>
            </tr>
          </tbody>
        </table>
      </div>
    </section>

    <!-- 8. 重點個股新聞與異動 -->
    <section id="stocks" class="mb-12 scroll-mt-6">
      <h2 class="text-2xl font-bold mb-4 flex items-center gap-2 border-b border-zinc-100 dark:border-zinc-800 pb-2">
        <span class="text-brand-500">8.</span> 重點個股新聞與異動
      </h2>

      <div class="space-y-4 no-print">
        
        <details class="bg-zinc-50/50 dark:bg-zinc-900/30 border border-zinc-200 dark:border-zinc-800 rounded-xl p-4" open>
          <summary class="font-bold text-zinc-800 dark:text-zinc-200 text-sm sm:text-base">8.1 大型科技七巨頭 (AAPL, MSFT, AMZN, META, GOOGL, NVDA, TSLA) 異動與新聞</summary>
          <div class="mt-4 space-y-3 text-sm text-zinc-650 dark:text-zinc-400 leading-relaxed border-t border-zinc-100 dark:border-zinc-800 pt-3">
            <p><strong>AAPL (蘋果):</strong> 暴跌 <strong>-6.14%</strong> 收報 <strong>$275.15</strong>。公司宣佈由於 AI 伺服器瘋搶產能導致存儲及記憶體晶片成本大幅上調，將 MacBook Air (512GB) 售價提高至 $1,299 (漲 $200)，iPad Pro 256GB 提高至 $1,199 (漲 $200)。市場憂慮調價將衝擊下半年消費電子需求，引發劇烈拋售。</p>
            <p><strong>MSFT (微軟):</strong> 重挫 <strong>-3.45%</strong> 收報 <strong>$352.83</strong>。微軟跟進宣布，因存儲成本上升，自 8 月 1 日起將全球 Xbox 主機售價分別上調 $100 (512GB) 至 $150 (1TB)，並將停產 2TB 遊戲主機。硬體業務利潤率受壓和高額 AI 資本支出隱憂共同施壓股價。</p>
            <p><strong>AMZN (亞馬遜):</strong> 下跌 <strong>-3.14%</strong> 收報 <strong>$227.01</strong>。受蘋果及微軟引發的消費電子硬件需求擔憂波及，電商及零售巨頭遭主力資金部分提款。</p>
            <p><strong>META (Meta Platforms):</strong> 下跌 <strong>-2.68%</strong> 收報 <strong>$542.87</strong>。無明顯利空，主要受權重科技股板塊整體頭寸削減波及，回踩前波支撐平台。</p>
            <p><strong>NVDA (輝達):</strong> 下跌 <strong>-1.59%</strong> 收報 <strong>$195.74</strong>。常規交易時間高開後遭到一部分科技巨頭避險資金流出的砸盤，收盤微跌，但其在中高階算力硬體的核心地位依然不可動搖。</p>
            <p><strong>GOOGL (Alphabet) / TSLA (特斯拉):</strong> Alphabet 微跌 <strong>-0.45%</strong> 收報 <strong>$343.71</strong>；特斯拉幾乎收平，微跌 <strong>-0.09%</strong> 報 <strong>$375.12</strong>，空頭回補暫時守穩。</p>
          </div>
        </details>

        <details class="bg-zinc-50/50 dark:bg-zinc-900/30 border border-zinc-200 dark:border-zinc-800 rounded-xl p-4">
          <summary class="font-bold text-zinc-800 dark:text-zinc-200 text-sm sm:text-base">8.2 AI 硬體 / 半導體重點股異動分析</summary>
          <div class="mt-4 space-y-3 text-sm text-zinc-650 dark:text-zinc-400 leading-relaxed border-t border-zinc-100 dark:border-zinc-800 pt-3">
            <p><strong>MU (美光科技):</strong> 暴漲 <strong>+15.81%</strong> 收報 <strong>$1,213.56</strong>。季報與指引大超預期，特別是 HBM 產能直至 2027 年已被客戶全部訂滿，且與雲端巨頭簽署了長期合約以保證高定價，確認了存儲業「RAMmageddon」的超級景氣週期。</p>
            <p><strong>ASML (艾司摩爾 ADR):</strong> 大漲 <strong>+4.40%</strong> 收報 <strong>$1,841.18</strong>。美光財報大增表明晶片廠商擴產及更新先進光刻機的需求依然狂熱，光刻機龍頭大受資金追捧。</p>
            <p><strong>AMD (超微半導體):</strong> 上漲 <strong>+2.60%</strong> 收報 <strong>$532.57</strong>。受半導體人氣大回暖刺激，股價重回 $530 上方，收復多條短期均線。</p>
            <p><strong>MRVL (馬威爾):</strong> 上漲 <strong>+1.65%</strong> 收報 <strong>$281.26</strong>。受惠於先進封裝及光互連晶片需求隨美光業績得到印證，股價大漲後持續向上築底。</p>
          </div>
        </details>

        <details class="bg-zinc-50/50 dark:bg-zinc-900/30 border border-zinc-200 dark:border-zinc-800 rounded-xl p-4">
          <summary class="font-bold text-zinc-800 dark:text-zinc-200 text-sm sm:text-base">8.3 軟體 / SaaS / AI 應用重點股異動分析</summary>
          <div class="mt-4 space-y-3 text-sm text-zinc-650 dark:text-zinc-400 leading-relaxed border-t border-zinc-100 dark:border-zinc-800 pt-3">
            <p><strong>NOW (ServiceNow):</strong> 重挫 <strong>-4.56%</strong> 收報 <strong>$89.52</strong>。軟體應用端資金大舉流出以支援高貝塔的半導體硬件股，股價放量跌破短期平台。</p>
            <p><strong>ORCL (甲骨文):</strong> 大跌 <strong>-3.22%</strong> 收報 <strong>$152.46</strong>。估值溢價繼續遭到修正，資金高低切換，短期尋求 50MA 平台支撐。</p>
            <p><strong>PLTR (Palantir):</strong> 下跌 <strong>-5.49%</strong> 收報 <strong>$107.27</strong>。作為高估值 AI 應用股代表，股價連遭殺跌，回踩前波重要支撐位。</p>
            <p><strong>CRM (Salesforce) / ADBE (奧多比):</strong> Salesforce 下跌 <strong>-1.68%</strong> 報 <strong>$150.19</strong>；Adobe 下跌 <strong>-1.60%</strong> 報 <strong>$193.41</strong>，軟體板塊防禦盤暫時退潮。</p>
          </div>
        </details>

        <details class="bg-zinc-50/50 dark:bg-zinc-900/30 border border-zinc-200 dark:border-zinc-800 rounded-xl p-4">
          <summary class="font-bold text-zinc-800 dark:text-zinc-200 text-sm sm:text-base">8.4 AI 電力 / 資料中心 / 能源基礎設施重點股分析</summary>
          <div class="mt-4 space-y-3 text-sm text-zinc-650 dark:text-zinc-400 leading-relaxed border-t border-zinc-100 dark:border-zinc-800 pt-3">
            <p><strong>ETN (伊頓):</strong> 大漲 <strong>+3.78%</strong> 收報 <strong>$419.87</strong>。受美光 HBM 擴產與大型 AI 數據中心重電改造預期的雙重加持，股價延續強勢上行趨勢。</p>
            <p><strong>NRG Energy / VST (Vistra):</strong> NRG Energy 大漲 <strong>+3.44%</strong> 收報 <strong>$147.11</strong>；Vistra 收漲 <strong>+3.01%</strong> 報 <strong>$167.77</strong>。AI 電力與算力擴張引發的長期電能赤字，繼續吸引防守及成長型配置基金建倉。</p>
            <p><strong>OKLO:</strong> 持續下跌 <strong>-5.64%</strong> 收報 <strong>$51.01</strong>。核電熱度短期降溫，散戶多頭資金退潮，股價向 $50 支撐靠攏。</p>
          </div>
        </details>
      </div>
    </section>

    <!-- 9. 財報日曆與財報解讀 -->
    <section id="earnings" class="mb-12 scroll-mt-6">
      <h2 class="text-2xl font-bold mb-4 flex items-center gap-2 border-b border-zinc-100 dark:border-zinc-800 pb-2">
        <span class="text-brand-500">9.</span> 財報日曆與財報解讀
      </h2>
      <div class="space-y-4 text-sm sm:text-base leading-relaxed text-zinc-700 dark:text-zinc-300">
        <div class="bg-zinc-50/50 dark:bg-zinc-900/40 p-5 rounded-xl border border-zinc-200 dark:border-zinc-800">
          <h4 class="font-bold text-zinc-800 dark:text-zinc-200 mb-2">9.1 昨夜公佈財報重點公司：美光科技 (MU) 業績強烈爆發</h4>
          <p class="mb-3">美光科技 (MU) 於盤前暴漲近 16%，兌現了其優秀的 Q3 財報數據：</p>
          <ul class="list-disc pl-5 space-y-2 mb-3">
            <li><strong>營業收入：</strong> $41.46 billion，遠超市場預期的 $39.5B。</li>
            <li><strong>Non-GAAP EPS：</strong> 錄得 $25.11，大超華爾街預期的 $22.50。</li>
            <li><strong>客戶簽約：</strong> 已與數家超大型雲端巨頭簽署了變革性的長期戰略定價協議，這實質上把未來幾年記憶體價格鎖定在極高水平，確保了極其豐厚和穩定的毛利率。</li>
            <li><strong>市場影響：</strong> 本次財報徹底平息了此前大摩等機構宣揚的「HBM 產能過剩論」，引爆了半導體設備、先進封裝及光互連板塊的集體報復性反彈。</li>
          </ul>
        </div>
        <div class="bg-zinc-50/50 dark:bg-zinc-900/40 p-5 rounded-xl border border-zinc-200 dark:border-zinc-800">
          <h4 class="font-bold text-zinc-800 dark:text-zinc-200 mb-2">9.2 未來 1-3 個交易日重要財報</h4>
          <p>緊接著耐吉 (NKE) 等重要零售龍頭將公佈業績，這將為投資者評估蘋果調價後消費者是否有能力繼續為高昂硬件買單提供關鍵的底層微觀參考指標。</p>
        </div>
      </div>
    </section>

    <!-- 10. 機構觀點與資金流 -->
    <section id="institution" class="mb-12 scroll-mt-6">
      <h2 class="text-2xl font-bold mb-4 flex items-center gap-2 border-b border-zinc-100 dark:border-zinc-800 pb-2">
        <span class="text-brand-500">10.</span> 機構觀點與資金流
      </h2>
      <div class="space-y-4 text-zinc-650 dark:text-zinc-400 leading-relaxed text-sm sm:text-base">
        <p><strong>華爾街日報與瑞銀 (UBS):</strong> 針對「RAMmageddon」危機發表研究報告。瑞銀指出，AI 晶片的無限制需求大幅排擠了常規存儲與記憶體產能。晶片製造商（三星、美光、SK海力士）在 HBM 利潤率高達 60% 以上的情況下，已停止擴建普通 PC/主機儲存條生產線。這導致下游消費電子巨頭不得不承受兩倍以上的採購成本，蘋果微軟調高售價是不得不採取的防禦毛利手段，但這無疑會對 Q3 的消費電子出貨量造成潛在負面衝擊。</p>
        <p><strong>美銀證券 (BofA Securities):</strong> 維持對半導體板塊（SOXX）的「增持」評級，但將軟體及雲端應用板塊評級下調至中性。美銀指出，當前 AI 週期的繁榮主要集中在「物理基礎設施層（ASIC、記憶體、電力供應、液冷）」，應用端（SaaS）的變現速度慢於高企的基礎設施支出，短期內資金正加速進行板塊內部的結構性換倉。</p>
      </div>
    </section>

    <!-- 11. 板塊輪動判斷 -->
    <section id="rotation" class="mb-12 scroll-mt-6">
      <h2 class="text-2xl font-bold mb-4 flex items-center gap-2 border-b border-zinc-100 dark:border-zinc-800 pb-2">
        <span class="text-brand-500">11.</span> 板塊輪動判斷
      </h2>
      <p class="text-zinc-650 dark:text-zinc-400 leading-relaxed text-sm sm:text-base">
        今日市場資金呈現高度的<strong>「硬體狂歡、軟體退避、下游承壓」</strong>格局。美光暴漲將資金強行吸回半導體（費半 +3.94%），但晶片價格暴漲引發了蘋果、微軟的成本反噬，使資金大量出逃此類超大市值終端公司。板塊輪動從「常規巨頭護盤」轉移到「上游原料與硬體基建強勢補漲」。重電（ETN, VRT）與能源（XLE）亦吸引了部分避險多頭。只要 PCE 通膨不反彈，這種結構性良性輪動將繼續維持牛市底色，避免了大盤出現系統性崩盤。
      </p>
    </section>

    <!-- 12. 重點關注股觀察 -->
    <section id="watchlist" class="mb-12 scroll-mt-6">
      <h2 class="text-2xl font-bold mb-4 flex items-center gap-2 border-b border-zinc-100 dark:border-zinc-800 pb-2">
        <span class="text-brand-500">12.</span> 重點關注股觀察
      </h2>
      
      <div class="overflow-x-auto border border-zinc-200 dark:border-zinc-800 rounded-xl">
        <table class="min-w-full divide-y divide-zinc-200 dark:divide-zinc-850 text-sm">
          <thead class="bg-zinc-50 dark:bg-zinc-900 text-zinc-550 dark:text-zinc-400">
            <tr class="text-left">
              <th class="px-4 py-3">個股代號</th>
              <th class="px-4 py-3 text-right">收盤價格 (當日變動)</th>
              <th class="px-4 py-3">技術與趨勢特徵</th>
              <th class="px-4 py-3 text-center">交易判定</th>
              <th class="px-4 py-3 text-left">關鍵位置與操作說明</th>
            </tr>
          </thead>
          <tbody class="divide-y divide-zinc-200 dark:divide-zinc-850 font-mono text-zinc-700 dark:text-zinc-300">
            <tr>
              <td class="px-4 py-3 font-semibold font-sans text-zinc-900 dark:text-zinc-100">NVDA</td>
              <td class="px-4 py-3 text-right text-rose-500 font-semibold">$195.74 (-1.59%)</td>
              <td class="px-4 py-3 font-sans">高開後震盪，回調測試 $195 支撐位</td>
              <td class="px-4 py-3 text-center font-sans"><span class="px-2 py-0.5 rounded bg-amber-100 dark:bg-amber-950 text-amber-800 dark:text-amber-350 text-xs font-semibold">回踩支撐</span></td>
              <td class="px-4 py-3 font-sans text-xs">常規時間受大盤拋壓拖累，但在 $195 有強支撐，中線地位並未動搖。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold font-sans text-zinc-900 dark:text-zinc-100">AMD</td>
              <td class="px-4 py-3 text-right text-emerald-500 font-semibold">$532.57 (+2.60%)</td>
              <td class="px-4 py-3 font-sans">放量反彈，站穩 10MA 上方</td>
              <td class="px-4 py-3 text-center font-sans"><span class="px-2 py-0.5 rounded bg-blue-100 dark:bg-blue-950 text-blue-800 dark:text-blue-350 text-xs font-semibold">低位修復</span></td>
              <td class="px-4 py-3 font-sans text-xs">跟隨半導體人氣反彈，重返 $530 上方，中期調整警報解除。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold font-sans text-zinc-900 dark:text-zinc-100">AVGO</td>
              <td class="px-4 py-3 text-right text-rose-500 font-semibold">$378.91 (-0.83%)</td>
              <td class="px-4 py-3 font-sans">窄幅震盪，守在 20MA 附近</td>
              <td class="px-4 py-3 text-center font-sans"><span class="px-2 py-0.5 rounded bg-zinc-100 dark:bg-zinc-800 text-zinc-800 dark:text-zinc-300 text-xs font-semibold">高位震盪</span></td>
              <td class="px-4 py-3 font-sans text-xs">小幅收跌但仍守穩 20MA ($375)。AI ASIC 長線需求依然剛性。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold font-sans text-zinc-900 dark:text-zinc-100">MRVL</td>
              <td class="px-4 py-3 text-right text-emerald-500 font-semibold">$281.26 (+1.65%)</td>
              <td class="px-4 py-3 font-sans">大漲後小幅放量，站上 20MA</td>
              <td class="px-4 py-3 text-center font-sans"><span class="px-2 py-0.5 rounded bg-blue-100 dark:bg-blue-950 text-blue-800 dark:text-blue-350 text-xs font-semibold">低位修復</span></td>
              <td class="px-4 py-3 font-sans text-xs">承接昨日大漲勢頭，資金持續流入先進封裝設備，支撐位 $275。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold font-sans text-zinc-900 dark:text-zinc-100">GOOGL</td>
              <td class="px-4 py-3 text-right text-rose-500 font-semibold">$343.71 (-0.45%)</td>
              <td class="px-4 py-3 font-sans">小幅收跌，回踩 50MA 阻力位</td>
              <td class="px-4 py-3 text-center font-sans"><span class="px-2 py-0.5 rounded bg-zinc-100 dark:bg-zinc-800 text-zinc-800 dark:text-zinc-300 text-xs font-semibold">高位震盪</span></td>
              <td class="px-4 py-3 font-sans text-xs">在 $340-$345 箱體整理，等待大盤情緒穩定。支撐 $340。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold font-sans text-zinc-900 dark:text-zinc-100">MSFT</td>
              <td class="px-4 py-3 text-right text-rose-500 font-semibold">$352.83 (-3.45%)</td>
              <td class="px-4 py-3 font-sans">放量重挫，摜破多條均線，MACD死叉擴大</td>
              <td class="px-4 py-3 text-center font-sans"><span class="px-2 py-0.5 rounded bg-rose-100 dark:bg-rose-950 text-rose-800 dark:text-rose-350 text-xs font-semibold">破位風險</span></td>
              <td class="px-4 py-3 font-sans text-xs">Xbox主機價格調漲折射出硬體成本壓力，股價失守 50MA 平台，尋求 100MA 支撐。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold font-sans text-zinc-900 dark:text-zinc-100">META</td>
              <td class="px-4 py-3 text-right text-rose-500 font-semibold">$542.87 (-2.68%)</td>
              <td class="px-4 py-3 font-sans">跟隨巨頭板塊下挫，測試短期支撐</td>
              <td class="px-4 py-3 text-center font-sans"><span class="px-2 py-0.5 rounded bg-amber-100 dark:bg-amber-950 text-amber-800 dark:text-amber-350 text-xs font-semibold">回踩支撐</span></td>
              <td class="px-4 py-3 font-sans text-xs">大盤獲利回吐，股價面臨短期回踩壓力，守穩 $540 為宜。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold font-sans text-zinc-900 dark:text-zinc-100">AMZN</td>
              <td class="px-4 py-3 text-right text-rose-500 font-semibold">$227.01 (-3.14%)</td>
              <td class="px-4 py-3 font-sans">消費硬體擔憂施壓，股價失守 10MA</td>
              <td class="px-4 py-3 text-center font-sans"><span class="px-2 py-0.5 rounded bg-amber-100 dark:bg-amber-950 text-amber-800 dark:text-amber-350 text-xs font-semibold">回踩支撐</span></td>
              <td class="px-4 py-3 font-sans text-xs">大漲後高位獲利回吐，回調踩向 $225 水平。支撐 $225，阻力 $235。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold font-sans text-zinc-900 dark:text-zinc-100">ORCL</td>
              <td class="px-4 py-3 text-right text-rose-500 font-semibold">$152.46 (-3.22%)</td>
              <td class="px-4 py-3 font-sans">跌勢擴大，進一步跌向 50MA 平台</td>
              <td class="px-4 py-3 text-center font-sans"><span class="px-2 py-0.5 rounded bg-rose-100 dark:bg-rose-950 text-rose-800 dark:text-rose-350 text-xs font-semibold">破位風險</span></td>
              <td class="px-4 py-3 font-sans text-xs">軟體估值泡沫修正，MACD 死叉繼續向下，目前建議觀望至 50MA 支撐。支撐 $150。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold font-sans text-zinc-900 dark:text-zinc-100">CRM</td>
              <td class="px-4 py-3 text-right text-rose-500 font-semibold">$150.19 (-1.68%)</td>
              <td class="px-4 py-3 font-sans">低位窄幅震盪，失守 10MA</td>
              <td class="px-4 py-3 text-center font-sans"><span class="px-2 py-0.5 rounded bg-zinc-100 dark:bg-zinc-800 text-zinc-800 dark:text-zinc-300 text-xs font-semibold">需要觀察</span></td>
              <td class="px-4 py-3 font-sans text-xs">在 $150 整數防禦線邊緣徘徊。觀察能否守住該平台。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold font-sans text-zinc-900 dark:text-zinc-100">NOW</td>
              <td class="px-4 py-3 text-right text-rose-500 font-semibold">$89.52 (-4.56%)</td>
              <td class="px-4 py-3 font-sans">破位下挫，放量砸破 20MA 平台</td>
              <td class="px-4 py-3 text-center font-sans"><span class="px-2 py-0.5 rounded bg-rose-100 dark:bg-rose-950 text-rose-800 dark:text-rose-350 text-xs font-semibold">破位風險</span></td>
              <td class="px-4 py-3 font-sans text-xs">軟體股大提款，股價大幅破位下行，短線防守位置降至 $87.50。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold font-sans text-zinc-900 dark:text-zinc-100">SNOW</td>
              <td class="px-4 py-3 text-right text-emerald-500 font-semibold">$227.06 (+0.49%)</td>
              <td class="px-4 py-3 font-sans">溫和收漲，表現強於其餘軟體股</td>
              <td class="px-4 py-3 text-center font-sans"><span class="px-2 py-0.5 rounded bg-blue-100 dark:bg-blue-950 text-blue-800 dark:text-blue-350 text-xs font-semibold">低位修復</span></td>
              <td class="px-4 py-3 font-sans text-xs">展現一定的抗跌性，守住 $225 箱體。中線低位修復未變。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold font-sans text-zinc-900 dark:text-zinc-100">ADBE</td>
              <td class="px-4 py-3 text-right text-rose-500 font-semibold">$193.41 (-1.60%)</td>
              <td class="px-4 py-3 font-sans">帶量收跌，回踩短期均線</td>
              <td class="px-4 py-3 text-center font-sans"><span class="px-2 py-0.5 rounded bg-zinc-100 dark:bg-zinc-800 text-zinc-800 dark:text-zinc-300 text-xs font-semibold">需要觀察</span></td>
              <td class="px-4 py-3 font-sans text-xs">軟體板塊退潮，股價回踩 $190。若失守此處短期結構將轉弱。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold font-sans text-zinc-900 dark:text-zinc-100">PLTR</td>
              <td class="px-4 py-3 text-right text-rose-500 font-semibold">$107.27 (-5.49%)</td>
              <td class="px-4 py-3 font-sans">重挫下行，砸穿 50MA 重要均線</td>
              <td class="px-4 py-3 text-center font-sans"><span class="px-2 py-0.5 rounded bg-rose-100 dark:bg-rose-950 text-rose-800 dark:text-rose-350 text-xs font-semibold">破位風險</span></td>
              <td class="px-4 py-3 font-sans text-xs">高估值應用溢價加速擠泡沫，跌破 $110 支撐，下方防線降至 $102。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold font-sans text-zinc-900 dark:text-zinc-100">LITE</td>
              <td class="px-4 py-3 text-right text-emerald-500 font-semibold">$861.97 (+2.26%)</td>
              <td class="px-4 py-3 font-sans">光通信熱度加持，延續多頭攻勢</td>
              <td class="px-4 py-3 text-center font-sans"><span class="px-2 py-0.5 rounded bg-emerald-100 dark:bg-emerald-950 text-emerald-800 dark:text-emerald-350 text-xs font-semibold">繼續強勢</span></td>
              <td class="px-4 py-3 font-sans text-xs">在 $850 平台獲得強力承接，光通信硬體端訂單能見度佳。支撐 $845。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold font-sans text-zinc-900 dark:text-zinc-100">COHR</td>
              <td class="px-4 py-3 text-right text-emerald-500 font-semibold">$407.25 (+3.76%)</td>
              <td class="px-4 py-3 font-sans">長陽爆發，收復 10MA 指標</td>
              <td class="px-4 py-3 text-center font-sans"><span class="px-2 py-0.5 rounded bg-emerald-100 dark:bg-emerald-950 text-emerald-800 dark:text-emerald-350 text-xs font-semibold">繼續強勢</span></td>
              <td class="px-4 py-3 font-sans text-xs">美光業績間接證實了高頻光模組模塊的持續爆發力，股價重回 $400。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold font-sans text-zinc-900 dark:text-zinc-100">ANET</td>
              <td class="px-4 py-3 text-right text-emerald-500 font-semibold">$165.45 (+2.29%)</td>
              <td class="px-4 py-3 font-sans">守穩短期均線，帶量收漲</td>
              <td class="px-4 py-3 text-center font-sans"><span class="px-2 py-0.5 rounded bg-emerald-100 dark:bg-emerald-950 text-emerald-800 dark:text-emerald-350 text-xs font-semibold">繼續強勢</span></td>
              <td class="px-4 py-3 font-sans text-xs">以太網交換機龍頭獲買盤青睞，股價突破箱體，關鍵支撐 $162。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold font-sans text-zinc-900 dark:text-zinc-100">FLNC</td>
              <td class="px-4 py-3 text-right text-rose-500 font-semibold">$19.38 (-1.87%)</td>
              <td class="px-4 py-3 font-sans">縮量回調，跌穿 20MA 位置</td>
              <td class="px-4 py-3 text-center font-sans"><span class="px-2 py-0.5 rounded bg-zinc-100 dark:bg-zinc-800 text-zinc-800 dark:text-zinc-300 text-xs font-semibold">需要觀察</span></td>
              <td class="px-4 py-3 font-sans text-xs">儲能概念股熱度回吐，防守支撐降至 $19.00 位置。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold font-sans text-zinc-900 dark:text-zinc-100">OKLO</td>
              <td class="px-4 py-3 text-right text-rose-500 font-semibold">$51.01 (-5.64%)</td>
              <td class="px-4 py-3 font-sans">破位下瀉，賣壓沉重</td>
              <td class="px-4 py-3 text-center font-sans"><span class="px-2 py-0.5 rounded bg-rose-100 dark:bg-rose-950 text-rose-800 dark:text-rose-350 text-xs font-semibold">破位風險</span></td>
              <td class="px-4 py-3 font-sans text-xs">高波動核電概念繼續吐泡沫，跌向 $50 整數防線。謹慎抄底。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold font-sans text-zinc-900 dark:text-zinc-100">VST</td>
              <td class="px-4 py-3 text-right text-emerald-500 font-semibold">$167.77 (+3.01%)</td>
              <td class="px-4 py-3 font-sans">帶量上漲，維持在歷史高點附近</td>
              <td class="px-4 py-3 text-center font-sans"><span class="px-2 py-0.5 rounded bg-emerald-100 dark:bg-emerald-950 text-emerald-800 dark:text-emerald-350 text-xs font-semibold">繼續強勢</span></td>
              <td class="px-4 py-3 font-sans text-xs">電能供需缺口長線利多，股價沿 10MA 穩步上行，支撐 $162。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold font-sans text-zinc-900 dark:text-zinc-100">CEG</td>
              <td class="px-4 py-3 text-right text-emerald-500 font-semibold">$268.69 (+0.27%)</td>
              <td class="px-4 py-3 font-sans">窄幅震盪，守在突破平台上</td>
              <td class="px-4 py-3 text-center font-sans"><span class="px-2 py-0.5 rounded bg-zinc-100 dark:bg-zinc-800 text-zinc-800 dark:text-zinc-300 text-xs font-semibold">高位震盪</span></td>
              <td class="px-4 py-3 font-sans text-xs">守穩 $265 平台。中線電力基建多頭趨勢不變。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold font-sans text-zinc-900 dark:text-zinc-100">ETN</td>
              <td class="px-4 py-3 text-right text-emerald-500 font-semibold">$419.87 (+3.78%)</td>
              <td class="px-4 py-3 font-sans">再度收漲，創收盤新高</td>
              <td class="px-4 py-3 text-center font-sans"><span class="px-2 py-0.5 rounded bg-emerald-100 dark:bg-emerald-950 text-emerald-800 dark:text-emerald-350 text-xs font-semibold">繼續強勢</span></td>
              <td class="px-4 py-3 font-sans text-xs">電網基建需求無比強悍，長陽突破後繼續展現龍頭風範，壓力看 $430。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold font-sans text-zinc-900 dark:text-zinc-100">VRT</td>
              <td class="px-4 py-3 text-right text-emerald-500 font-semibold">$325.57 (+2.89%)</td>
              <td class="px-4 py-3 font-sans">帶量反彈，站穩 20MA</td>
              <td class="px-4 py-3 text-center font-sans"><span class="px-2 py-0.5 rounded bg-emerald-100 dark:bg-emerald-950 text-emerald-800 dark:text-emerald-350 text-xs font-semibold">繼續強勢</span></td>
              <td class="px-4 py-3 font-sans text-xs">液冷散熱隨半導體大行情起飛，成功在 $320 止跌回升，壓力看 $335。</td>
            </tr>
          </tbody>
        </table>
      </div>
    </section>

    <!-- 13. 明日交易計畫 / 觀察清單 -->
    <section id="trading-plan" class="mb-12 scroll-mt-6">
      <h2 class="text-2xl font-bold mb-4 flex items-center gap-2 border-b border-zinc-100 dark:border-zinc-800 pb-2">
        <span class="text-brand-500">13.</span> 明日交易計畫
      </h2>
      <div class="space-y-4 text-sm sm:text-base leading-relaxed text-zinc-650 dark:text-zinc-400">
        <p><strong>13.1 宏觀觀察：</strong>繼續關注美債10Y殖利率能否在 4.40% 以下站穩。通膨數據落地後，下週焦點將轉向各大行在壓力測試合格後所宣布的派息增幅與股票回購計劃細節。</p>
        <p><strong>13.2 大盤觀察：</strong>標普 500 指數在 7,350 點附近有強烈承接，QQQ 收復 20MA 是多頭短線企穩的積極訊號。然而，需要警惕蘋果與微軟股價下行壓力是否會進一步外溢，並壓制納指反彈空間。</p>
        <p><strong>13.3 個股觀察：</strong>重點關注半導體龍頭<strong>美光 (MU)</strong> 暴漲後次日的持續買盤力度，切忌追高，可等待回踩短期均線後分批低吸；注意重電與電網基建龍頭（ETN, VRT, VST）是否有高位滯漲信號。適度減倉高估值且跌破均線的軟體應用股（PLTR, NOW），並把倉位轉移至半導體先進封裝及光模組題材股。</p>
      </div>
    </section>

    <!-- 14. 風險提示 -->
    <section id="risks" class="mb-12 scroll-mt-6">
      <h2 class="text-2xl font-bold mb-4 flex items-center gap-2 border-b border-zinc-100 dark:border-zinc-800 pb-2">
        <span class="text-brand-500">14.</span> 風險提示
      </h2>
      
      <div class="overflow-x-auto border border-zinc-200 dark:border-zinc-800 rounded-xl">
        <table class="min-w-full divide-y divide-zinc-200 dark:divide-zinc-850 text-sm">
          <thead class="bg-zinc-50 dark:bg-zinc-900 text-zinc-550 dark:text-zinc-400 text-left">
            <tr>
              <th class="px-4 py-3 font-semibold">風險維度</th>
              <th class="px-4 py-3 font-semibold text-center">風險等級</th>
              <th class="px-4 py-3 font-semibold">具體解讀</th>
              <th class="px-4 py-3 font-semibold">避險建議</th>
            </tr>
          </thead>
          <tbody class="divide-y divide-zinc-200 dark:divide-zinc-850 font-mono text-zinc-700 dark:text-zinc-300">
            <tr>
              <td class="px-4 py-3 font-semibold font-sans">終端硬件成本壓力擴散</td>
              <td class="px-4 py-3 text-center"><span class="px-2 py-0.5 rounded bg-rose-100 dark:bg-rose-950 text-rose-800 dark:text-rose-350 text-xs font-semibold">高</span></td>
              <td class="px-4 py-3 font-sans text-xs">「存儲荒」導致上游晶片商賺取暴利，但迫使下游品牌漲價，可能衝擊下半年消費出貨量與毛利率</td>
              <td class="px-4 py-3 font-sans text-xs">減少對蘋果及微軟等重度依賴消費電子硬體利潤的持倉，聚焦利潤率有保障的上游廠商</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold font-sans">高估值軟體股去泡沫</td>
              <td class="px-4 py-3 text-center"><span class="px-2 py-0.5 rounded bg-amber-100 dark:bg-amber-950 text-amber-800 dark:text-amber-350 text-xs font-semibold">中</span></td>
              <td class="px-4 py-3 font-sans text-xs">SaaS/應用端營收增長慢於資本開支，資金換倉至硬件，導致軟體股連番破位下瀉</td>
              <td class="px-4 py-3 font-sans text-xs">規避跌破 50MA 且估值過高的 AI 應用股，等待估值出清</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold font-sans">加密貨幣清算外溢風險</td>
              <td class="px-4 py-3 text-center"><span class="px-2 py-0.5 rounded bg-yellow-100 dark:bg-yellow-950 text-yellow-800 dark:text-yellow-350 text-xs font-semibold">中低</span></td>
              <td class="px-4 py-3 font-sans text-xs">比特幣跌穿 60k 可能引發部分槓桿投機資金爆倉，連帶影響股市散戶情绪</td>
              <td class="px-4 py-3 font-sans text-xs">保持充足現金水平（約 3 成），以防流動性突發性緊縮</td>
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
      <div class="bg-zinc-50 dark:bg-zinc-900 p-6 rounded-2xl border border-zinc-200 dark:border-zinc-800 space-y-4 leading-relaxed text-sm sm:text-base">
        <p><strong>今日市場結論：</strong> 今日大盤在晶片股暴漲與下游巨頭重挫的雙重拉扯下呈分化整理。美光爆款財報大漲 15.81%，SOXX 暴漲 3.94% 宣告半導體調整告一段落；然而「晶片荒」上調售價亦重創蘋果微軟。PCE 數據平穩及債息下行，讓中小盤股與等權標普表現良好，市場並非系統性崩盤。</p>
        <p><strong>當前市場階段：</strong> <span class="text-emerald-500 font-semibold">結構性調整分化 / 半導體與硬體基建重啟牛市</span></p>
        <p><strong>操作傾向：</strong> 偏多。大盤在 20MA 有效築底。配置上應「擁抱晶片設備與電力硬件，規避估值虛高軟體與下游利潤受壓巨頭」。適度逢低布局 NVDA, ASML 與 ETN。</p>
        <p><strong>最值得觀測的 5 個訊號：</strong>
          <br>1. <strong>美光科技（MU）的承接力度：</strong> 暴漲後能否維持在 $1,200 上方縮量整固。
          <br>2. <strong>蘋果（AAPL）與微軟（MSFT）是否止跌：</strong> 若巨頭持續下挫，將持續拖累納指反彈。
          <br>3. <strong>10年期美債收益率 (^TNX)：</strong> 能否進一步朝 4.30% 下滑。
          <br>4. <strong>比特幣（BTC）能否奪回 60k：</strong> 關係到投機盤資金情緒。
          <br>5. <strong>大行下週的股息與回購聲明：</strong> 將是金融板塊能否重新走強的關鍵。
        </p>
      </div>
    </section>

    <!-- Footer -->
    <footer class="mt-16 pt-8 border-t border-zinc-200 dark:border-zinc-800 text-sm text-zinc-500 text-center">
      由 <a href="https://github.com/wisdom925/html-report-skill" class="underline hover:text-zinc-900 dark:hover:text-zinc-100"><code>html-report</code></a> 技能發布。
    </footer>

  </main>
</div>

<script>
  // Theme toggle
  document.getElementById('theme-toggle').addEventListener('click', () => {
    const dark = document.documentElement.classList.toggle('dark');
    localStorage.theme = dark ? 'dark' : 'light';
    // Re-init mermaid with new theme if loaded
    if (window.__mermaid) {
      document.querySelectorAll('.mermaid[data-processed]').forEach(el => { 
        el.removeAttribute('data-processed'); 
        el.innerHTML = el.dataset.src || el.textContent; 
      });
      window.__mermaid.initialize({ startOnLoad: false, theme: dark ? 'dark' : 'default', securityLevel: 'loose' });
      window.__mermaid.run();
    }
    // Update Chart.js colors if instance exists
    if (window.returnsChartInstance) {
      const isDark = document.documentElement.classList.contains('dark');
      const gridColor = isDark ? 'rgba(255,255,255,0.08)' : 'rgba(0,0,0,0.05)';
      const labelColor = isDark ? '#a1a1aa' : '#71717a';
      const legendColor = isDark ? '#f4f4f5' : '#18181b';
      
      window.returnsChartInstance.options.scales.x.grid.color = gridColor;
      window.returnsChartInstance.options.scales.x.ticks.color = labelColor;
      window.returnsChartInstance.options.scales.y.grid.color = gridColor;
      window.returnsChartInstance.options.scales.y.ticks.color = labelColor;
      window.returnsChartInstance.options.plugins.legend.labels.color = legendColor;
      window.returnsChartInstance.update();
    }
  });

  // Code highlight + copy buttons
  hljs.highlightAll();
  document.querySelectorAll('pre > code').forEach(code => {
    const pre = code.parentElement;
    pre.classList.add('has-copy');
    const btn = document.createElement('button');
    btn.textContent = 'copy';
    btn.className = 'copy-btn no-print text-xs px-2 py-1 rounded bg-zinc-700 text-zinc-100 hover:bg-zinc-600 opacity-0 group-hover:opacity-100 transition-opacity';
    btn.style.opacity = '0.5';
    btn.addEventListener('mouseenter', () => btn.style.opacity = '1');
    btn.addEventListener('mouseleave', () => btn.style.opacity = '0.5');
    btn.addEventListener('click', async () => {
      await navigator.clipboard.writeText(code.innerText);
      const old = btn.textContent;
      btn.textContent = 'copied';
      setTimeout(() => btn.textContent = old, 1200);
    });
    pre.appendChild(btn);
  });

  // Sticky TOC scroll-spy
  const tocLinks = document.querySelectorAll('.toc a');
  const sections = [...tocLinks].map(a => document.querySelector(a.getAttribute('href'))).filter(Boolean);
  if (sections.length) {
    const onScroll = () => {
      const y = window.scrollY + 100;
      let active = sections[0];
      for (const s of sections) {
        if (s.offsetTop <= y) {
          active = s;
        }
      }
      tocLinks.forEach(a => a.classList.toggle('active', a.getAttribute('href') === '#' + active.id));
    };
    window.addEventListener('scroll', onScroll, { passive: true });
    onScroll();
  }

  // Filter Sectors Table
  const sectorSearch = document.getElementById('sectorSearch');
  if (sectorSearch) {
    sectorSearch.addEventListener('input', function(e) {
      const query = e.target.value.toLowerCase().trim();
      const rows = document.querySelectorAll('#sectorsTable tbody tr');
      rows.forEach(row => {
        const text = row.innerText.toLowerCase();
        if (text.includes(query)) {
          row.style.display = '';
        } else {
          row.style.display = 'none';
        }
      });
    });
  }

  // Sort Table Columns
  let currentSortCol = -1;
  let currentSortAsc = true;
  window.sortSectors = function(colIndex) {
    const table = document.getElementById('sectorsTable');
    const tbody = table.querySelector('tbody');
    const rows = Array.from(tbody.querySelectorAll('tr'));
    
    if (currentSortCol === colIndex) {
      currentSortAsc = !currentSortAsc;
    } else {
      currentSortCol = colIndex;
      currentSortAsc = true;
    }

    rows.sort((a, b) => {
      let aVal = a.cells[colIndex].innerText.trim();
      let bVal = b.cells[colIndex].innerText.trim();
      
      // Handle rank (number)
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

    // Re-append sorted rows
    tbody.innerHTML = '';
    rows.forEach(r => tbody.appendChild(r));
  }

  // Chart.js: Rendering Returns Comparison Chart
  const ctx = document.getElementById('returnsChart').getContext('2d');
  const isDarkInitial = document.documentElement.classList.contains('dark');
  window.returnsChartInstance = new Chart(ctx, {
    type: 'bar',
    data: {
      labels: ['道瓊工業', '標普 500', '納指綜合', '納指 100 (QQQ)', '羅素 2000', 'SOX 半導體', 'VIX 波動率'],
      datasets: [{
        label: '當日變動 (%)',
        data: [0.10, -0.01, -0.46, 0.81, 0.75, 3.94, -3.08],
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
</script>

</body>
</html>
"""

# Save this HTML to reports/2026-06-25-us-stock-closing-daily-report.html inside /Users/wisdom/html-report-skill
target_dir = "/Users/wisdom/html-report-skill/reports"
os.makedirs(target_dir, exist_ok=True)
target_path = os.path.join(target_dir, "2026-06-25-us-stock-closing-daily-report.html")

with open(target_path, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"Report HTML file generated successfully at: {target_path}")
