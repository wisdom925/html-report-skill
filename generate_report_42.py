import os
import json

html_content = """<!doctype html>
<html lang="zh-TW" class="scroll-smooth">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <title>美股收盤日報｜2026-06-22</title>
  <meta name="description" content="2026年6月22日美股收盤日報：科技巨頭高位獲利回吐，SpaceX發債及ESG評級重挫16.4%，但英特爾與台積電合作/訂單利多續漲，費半逆勢收紅創歷史新高！美伊和平協定進展致油價重挫，道指受藍籌防禦股支撐逆勢走高。">
  <meta property="og:title" content="美股收盤日報｜2026-06-22">
  <meta property="og:description" content="科技巨頭高位回吐，SpaceX重挫16.4%，但英特爾與台積電強勢護盤費半逆市創高，美伊地緣緩和致油價大跌。">
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
        <time class="text-sm font-semibold text-zinc-500 dark:text-zinc-400">2026-06-22</time>
      </div>
      <h1 class="text-3xl sm:text-4xl font-extrabold tracking-tight mb-4 bg-gradient-to-r from-zinc-900 to-zinc-700 dark:from-zinc-100 dark:to-zinc-400 bg-clip-text text-transparent">
        美股收盤日報｜科技巨頭高位回吐，SpaceX發債及ESG評級重挫16.4%，但英特爾與台積電合作/訂單利多續漲，費半逆勢收紅創歷史新高！美伊和平協定進展致油價重挫，道指受藍籌防禦股支撐逆勢走高
      </h1>
      <p class="text-lg text-zinc-500 dark:text-zinc-400 leading-relaxed">
        週一（2026年6月22日）美股在結束六月節長週末後，三大指數呈現強烈的分化格局。由於美伊和平談判取得突破性進展，霍爾木茲海峽風險溢價大幅消退，原油價格重挫（WTI 跌穿 $75），這有效降溫了通膨預期，但也引導資金大舉流出估值高企的科技巨頭，轉向更具防禦屬性的醫療、金融與能源板塊，推升道指上揚 148 點。相反，大型科技股（MSFT、AMZN、META 等）面臨獲利回吐，Alphabet (GOOGL) 更是因核心 AI 人才流失擔憂重挫 5.22%。此外，新近上市的太空巨頭 SpaceX (SPCX) 因宣佈發債 200 億美元償還過渡貸款，加之 MSCI 給予其不利的 ESG 評級，股價崩瀉 16.4%。然而，半導體板塊依然展現極強韌性：英特爾 (INTC) 因與蘋果的本土代工進展及 Google 的代工大單預期飆升 5.20%，台積電 (TSM) 受投行調升目標價刺激收高 1.30%，帶動費半指數逆勢收紅 0.70%，創歷史收盤新高。
      </p>
    </header>

    <!-- 0. 今日一句話總結 -->
    <section id="summary" class="mb-12 scroll-mt-6">
      <h2 class="text-2xl font-bold mb-4 flex items-center gap-2 border-b border-zinc-100 dark:border-zinc-800 pb-2">
        <span class="text-brand-500">0.</span> 今日一句話總結
      </h2>
      <div class="bg-zinc-50/50 dark:bg-zinc-900/50 p-6 rounded-2xl border border-zinc-200/60 dark:border-zinc-800/60 leading-relaxed text-zinc-700 dark:text-zinc-300">
        <ul class="list-disc pl-5 space-y-3">
          <li><strong>大盤狀態：</strong>美股大盤走勢極度分化，道指受藍籌防禦板塊護盤小幅收高 0.29%，標普 500 指數微跌 0.37%，納斯達克綜合指數重挫 1.32%，羅素 2000 小盤股強勢上漲 0.83% 重上 3000 關卡。</li>
          <li><strong>驅動因素：</strong>美伊地緣緩和帶動油價暴跌至 $74，打壓通膨預期並激勵消費/羅素小盤；但在高利率長駐共識下，高估值科技巨頭（七巨頭大多下跌）遭遇去溢價調倉，SpaceX 發債與 ESG 報告引爆 16.4% 暴跌亦重創市場人氣。</li>
          <li><strong>資金流向：</strong>資金從高溢價的科技巨頭與應用軟體 (SaaS) 中流出，避險防禦性地湧入醫療、重電能源、以及受惠於油價下跌的羅素 2000；半導體代工核心（INTC、TSM）因實質訂單與國產代工紅利吸引抱團。</li>
          <li><strong>市場寬度：</strong>市場寬度顯著改善，羅素 2000 跑贏標普 500，交易所上漲家數多於下跌家數，顯示並非系統性恐慌，而是結構性的健康防禦性輪動。</li>
          <li><strong>一句話判斷：</strong><span class="text-emerald-500 font-semibold dark:text-emerald-400">大盤指數受巨頭及 SPCX 大跌壓制，但美伊緩和油價落，英特爾及台積電護盤費半創高，資金呈向防禦藍籌與小盤之健康大輪動格局。</span></li>
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
              <td class="px-4 py-3 text-right">51,712.71</td>
              <td class="px-4 py-3 text-right text-emerald-500 font-semibold">+0.29%</td>
              <td class="px-4 py-3 text-right">51,555.19 - 51,780.00</td>
              <td class="px-4 py-3 font-sans text-xs text-emerald-500 font-semibold">站穩短期均線，防禦藍籌護盤維持強勢震盪</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold font-sans text-zinc-900 dark:text-zinc-100">S&P 500 (標普 500)</td>
              <td class="px-4 py-3 text-right">7,472.79</td>
              <td class="px-4 py-3 text-right text-rose-500 font-semibold">-0.37%</td>
              <td class="px-4 py-3 text-right">7,461.04 - 7,530.01</td>
              <td class="px-4 py-3 font-sans text-xs text-amber-500 font-semibold">受阻於 7500 關卡上方，小幅回踩 10MA ($7,450)</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold font-sans text-zinc-900 dark:text-zinc-100">Nasdaq Composite (納指)</td>
              <td class="px-4 py-3 text-right">26,166.60</td>
              <td class="px-4 py-3 text-right text-rose-500 font-semibold">-1.32%</td>
              <td class="px-4 py-3 text-right">26,156.46 - 26,561.12</td>
              <td class="px-4 py-3 font-sans text-xs text-rose-500 font-semibold">長黑 K 棒跌破 5MA ($26,450)，高位獲利了結壓力沉重</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold font-sans text-zinc-900 dark:text-zinc-100">Nasdaq 100 / QQQ</td>
              <td class="px-4 py-3 text-right">730.34</td>
              <td class="px-4 py-3 text-right text-rose-500 font-semibold">-1.32%</td>
              <td class="px-4 py-3 text-right">728.50 - 741.00</td>
              <td class="px-4 py-3 font-sans text-xs text-rose-500 font-semibold">受巨頭集體下殺拖累，跌破前高阻力線，回試 $728 支撐</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold font-sans text-zinc-900 dark:text-zinc-100">Russell 2000 (羅素 2000)</td>
              <td class="px-4 py-3 text-right">3,004.40</td>
              <td class="px-4 py-3 text-right text-emerald-500 font-semibold">+0.83%</td>
              <td class="px-4 py-3 text-right">2,975.00 - 3,012.00</td>
              <td class="px-4 py-3 font-sans text-xs text-emerald-500 font-semibold">強勢突破 3000 點整數大關，直接受惠於油價暴跌物流開支大降</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold font-sans text-zinc-900 dark:text-zinc-100">SOX 半導體指數</td>
              <td class="px-4 py-3 text-right">14,441.54</td>
              <td class="px-4 py-3 text-right text-emerald-500 font-semibold">+0.70%</td>
              <td class="px-4 py-3 text-right">14,290.00 - 14,480.00</td>
              <td class="px-4 py-3 font-sans text-xs text-emerald-500 font-semibold">受 INTC (+5.2%) 及 TSM (+1.3%) 護盤，逆市攀升續創歷史收盤新高</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold font-sans text-zinc-900 dark:text-zinc-100">VIX 波動率指數</td>
              <td class="px-4 py-3 text-right">17.37</td>
              <td class="px-4 py-3 text-right text-emerald-500 font-semibold">+3.52%</td>
              <td class="px-4 py-3 text-right">16.80 - 17.65</td>
              <td class="px-4 py-3 font-sans text-xs text-amber-500 font-semibold">科技巨頭重挫及美伊後續談判推遲預期，帶動避險買盤小幅升溫</td>
            </tr>
          </tbody>
        </table>
      </div>

      <!-- Returns Chart -->
      <div class="p-4 bg-zinc-50 dark:bg-zinc-900 rounded-xl border border-zinc-200 dark:border-zinc-800">
        <h3 class="text-sm font-semibold text-zinc-500 mb-3 text-center uppercase tracking-wider">主要指數當日漲跌幅對比 (%)</h3>
        <div class="h-64 relative">
          <canvas id="returnsChart"></canvas>
        </div>
      </div>
    </section>

    <!-- 2. 盤中走勢復盤 -->
    <section id="timeline" class="mb-12 scroll-mt-6">
      <h2 class="text-2xl font-bold mb-4 flex items-center gap-2 border-b border-zinc-100 dark:border-zinc-800 pb-2">
        <span class="text-brand-500">2.</span> 盤中走勢復盤 (Timeline)
      </h2>

      <div class="relative border-l border-zinc-200 dark:border-zinc-800 ml-4 md:ml-6 space-y-8 mb-8">
        <!-- Event 1 -->
        <div class="relative pl-8 md:pl-10">
          <div class="absolute -left-3 top-1.5 w-6 h-6 rounded-full bg-blue-500 border-4 border-white dark:border-zinc-900 flex items-center justify-center"></div>
          <div class="bg-zinc-50 dark:bg-zinc-900 p-4 rounded-xl border border-zinc-200 dark:border-zinc-800 text-sm grow">
            <span class="text-xs text-zinc-400 font-semibold">盤前 (Pre-market)</span>
            <h4 class="font-bold text-zinc-800 dark:text-zinc-200 mt-1">美伊和平協定進展油價跌破 $75，英特爾合作及代工大單利多刺激走高</h4>
            <p class="text-zinc-555 dark:text-zinc-400 mt-1 leading-relaxed">
              美伊和平談判釋放極佳進展信號，WTI 原油價格直奔 $74 關卡，極大緩解了市場的二次通膨擔憂。與此同時，英特爾 (INTC) 因 Apple 在美本土設計與代工晶片的進展，以及傳聞中 Google DeepMind 最新發佈的代工大單，引導盤前大漲逾 4%。
            </p>
          </div>
        </div>

        <!-- Event 2 -->
        <div class="relative pl-8 md:pl-10">
          <div class="absolute -left-3 top-1.5 w-6 h-6 rounded-full bg-blue-500 border-4 border-white dark:border-zinc-900 flex items-center justify-center"></div>
          <div class="bg-zinc-50 dark:bg-zinc-900 p-4 rounded-xl border border-zinc-200 dark:border-zinc-800 text-sm grow">
            <span class="text-xs text-zinc-400 font-semibold">開盤 (9:30 AM - 11:30 AM)</span>
            <h4 class="font-bold text-zinc-800 dark:text-zinc-200 mt-1">大盤多空對決，科技巨頭高位獲利了結，SpaceX 發債崩瀉拖累納指</h4>
            <p class="text-zinc-555 dark:text-zinc-400 mt-1 leading-relaxed">
              開盤三大指數走勢出現顯著分化。Alphabet (GOOGL) 因核心 AI 人才離職潮憂慮大跌，亞馬遜、微軟等科技巨頭亦高位回吐。新上市的 SpaceX (SPCX) 因宣佈發行 200 億美元 senior notes 償還 bridge loan 以興建 Colossus AI 算力基建，加之 MSCI ESG 的不利評級，開盤後出現資金多頭踩踏大跌，拖累科技與工業板塊走弱，但金融與醫療等防禦板塊強勢護盤。
            </p>
          </div>
        </div>

        <!-- Event 3 -->
        <div class="relative pl-8 md:pl-10">
          <div class="absolute -left-3 top-1.5 w-6 h-6 rounded-full bg-blue-555 border-4 border-white dark:border-zinc-900 flex items-center justify-center"></div>
          <div class="bg-zinc-50 dark:bg-zinc-900 p-4 rounded-xl border border-zinc-200 dark:border-zinc-800 text-sm grow">
            <span class="text-xs text-zinc-400 font-semibold">午盤 (11:30 AM - 2:00 PM)</span>
            <h4 class="font-bold text-zinc-800 dark:text-zinc-200 mt-1">美債息高位彈升至 4.507%，羅素 2000 與防禦藍籌受油氣走跌提振上揚</h4>
            <p class="text-zinc-555 dark:text-zinc-400 mt-1 leading-relaxed">
              CME 利率預期重新計價（九名聯準會官員預計 2026 年會至少升息一次），美債 10 年期殖利率攀升至 4.507%。然而，油價暴跌直接減輕了美國中小型企業的物流成本，羅素 2000 指數順勢突破 3000 點整數大關。防禦性板塊（醫療、公用事業、地產）持續獲得資金青睞。
            </p>
          </div>
        </div>

        <!-- Event 4 -->
        <div class="relative pl-8 md:pl-10">
          <div class="absolute -left-3 top-1.5 w-6 h-6 rounded-full bg-red-500 border-4 border-white dark:border-zinc-900 flex items-center justify-center"></div>
          <div class="bg-zinc-50 dark:bg-zinc-900 p-4 rounded-xl border border-zinc-200 dark:border-zinc-800 text-sm grow">
            <span class="text-xs text-zinc-400 font-semibold">尾盤與收盤 (2:00 PM - 4:00 PM)</span>
            <h4 class="font-bold text-zinc-800 dark:text-zinc-200 mt-1">SpaceX 收於當日低點 (-16.4%)，英特爾及台積電護盤費半收紅</h4>
            <p class="text-zinc-555 dark:text-zinc-400 mt-1 leading-relaxed">
              尾盤時段，SpaceX (SPCX) 出現進一步的融資去槓桿賣壓，最終大跌 16.4% 收於 $154.60，導致工業和大型科技板塊的整體走勢進一步走低。微軟、谷歌、亞馬遜均收於日內低點附近，納指收跌 1.32%。但英特爾 (+5.2%)、台積電 (+1.3%) 和 AMD (+2.65%) 等半導體硬體龍頭頂住壓力，推動費半指數逆勢收紅 0.70%，創歷史收盤新高。
            </p>
          </div>
        </div>
      </div>

      <!-- Timeline visual flow in Mermaid -->
      <div class="p-4 bg-zinc-50 dark:bg-zinc-900 rounded-xl border border-zinc-200 dark:border-zinc-800 text-center">
        <h3 class="text-xs font-semibold text-zinc-500 mb-4 uppercase tracking-wider">今日市場邏輯與資金流向傳導 (Mermaid)</h3>
        <pre class="mermaid bg-transparent">
graph TD
    USIranPeace[美伊和平進展突破] --> OilCrash[WTI 原油重挫跌破 $75]
    OilCrash --> LogisticsBenef[中小型股物流成本大降]
    LogisticsBenef --> RussellSurge[羅素 2000 逆勢突破 3000 點]

    FedHawkish[CME 利率定價偏鷹派] --> YieldSpike[10Y 美債息升至 4.507%]
    YieldSpike --> TechValuation[高估值科技巨頭溢價回吐]
    
    TalentWorry[Google AI人才離職潮] --> GOOGLCrash[Alphabet 大跌 5.22%]
    SPCXDebt[SpaceX發債20B+ESG評級不利] --> SPCXCrash[SpaceX 暴跌 16.4%]
    
    GOOGLCrash & SPCXCrash & TechValuation --> NasdaqPullback[納斯達克指數重挫 1.32%]
    
    IntelAppleUMC[Intel 本土代工/大單預期] & TSMUpgrade[台積電 ADR 投行上調評級] --> Semi抱團[半導體板塊逆勢走強]
    Semi抱團 --> SOXNewHigh[費半指數收紅 0.70% 創歷史新高]
        </pre>
      </div>
    </section>

    <!-- 3. 宏觀環境 -->
    <section id="macro" class="mb-12 scroll-mt-6">
      <h2 class="text-2xl font-bold mb-4 flex items-center gap-2 border-b border-zinc-100 dark:border-zinc-800 pb-2">
        <span class="text-brand-500">3.</span> 宏觀環境
      </h2>

      <!-- Tabs system -->
      <div class="tabs flex flex-wrap border-b border-zinc-200 dark:border-zinc-800">
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
          <h4 class="font-bold text-zinc-800 dark:text-zinc-200 mb-2">美債息高位彈升，10Y 收益率升至 4.507%</h4>
          <p>
            美國國債殖利率今日全面走高。<strong>10年期美債收益率</strong> 攀升 5.6 個基點收於 <strong>4.507%</strong>；<strong>30年期美債收益率</strong> 上漲 4.5 個基點至 <strong>4.945%</strong>。債息走高主要因上週聯準會最新公佈的偏鷹「點陣圖」持續被計價，市場擔心通膨的黏性及新主席偏向強硬的作風，殖利率曲線倒掛程度依然嚴峻。這直接壓抑了無息且高倍數的 SaaS 應用板塊。
          </p>
        </div>

        <!-- Tab Panel 2 -->
        <div class="tab-panel w-full text-zinc-650 dark:text-zinc-400 text-sm sm:text-base leading-relaxed">
          <h4 class="font-bold text-zinc-800 dark:text-zinc-200 mb-2">聯準會加息預期蠢蠢欲動，降息計價基本歸零</h4>
          <p>
            今日 CME FedWatch 利率期貨的定價顯示了市場重大的情緒改變：年內基本不再預期會有多次降息，相反，<strong>升息預期開始被納入考慮</strong>。由於 18 名點陣圖參與者中有 9 名預計 2026 年會至少升息一次，市場目前甚至押注最快在 7 月或 9 月會有將近 50% 的加息概率，以防止二次通膨。新任 Fed 主席 Kevin Warsh 的政策不確定性使得估值敏感型板塊遭遇強烈獲利回吐。
          </p>
        </div>

        <!-- Tab Panel 3 -->
        <div class="tab-panel w-full text-zinc-600 dark:text-zinc-400 text-sm sm:text-base leading-relaxed">
          <h4 class="font-bold text-zinc-800 dark:text-zinc-200 mb-2">美伊緩和致原油重挫至 $74，美元創一年來新高，黃金回穩</h4>
          <p>
            <strong>WTI 原油 &amp; Brent 原油：</strong>美伊和平談判釋放極大誠意，霍爾木茲海峽的油輪航道安全恢復預期令原油地緣溢價被大幅剝離，WTI 原油重挫 4% 以上，跌至 <strong>$74.14 / 桶</strong>，這極大舒緩了製造業和物流業的通膨焦慮。<br>
            <strong>美元指數 DXY：</strong>美債收益率彈升與降息落空帶動美元指數大漲至 <strong>101.02</strong>，寫下近一年來高位。<br>
            <strong>黃金現貨：</strong>現貨黃金價格迎來長線牛市的技術性修正回溫，微升 0.35% 至 <strong>$4,191.00 / 盎司</strong>。<br>
            <strong>加密貨幣：</strong>比特幣 (BTC) 隨著避險資金從風險資產流出而修正，震盪下跌至 <strong>$62,888</strong>。
          </p>
        </div>

        <!-- Tab Panel 4 -->
        <div class="tab-panel w-full text-zinc-600 dark:text-zinc-400 text-sm sm:text-base leading-relaxed">
          <h4 class="font-bold text-zinc-800 dark:text-zinc-200 mb-2">本週重要經濟數據展望</h4>
          <p class="mb-3">
            今日美國宏觀經濟數據日曆較為冷清。全球市場主要消化了歐盟 Consumer Confidence (歐元區消費者信心指數) 閃估值上升 1.3bp 錄得的溫和復甦。本週市場焦點主要指向本週四（6月25日）即將公佈的 <strong>PCE 物價指數</strong>、Q1 GDP 修正值及耐用品訂單，預期這將給出聯準會是否可能考慮「預防性加息」的實質線索。
          </p>
          <div class="text-xs text-zinc-400 border-t border-zinc-100 dark:border-zinc-800 pt-2">
            > [!IMPORTANT]
            > 原油大跌對宏觀通膨是長期利多，但在 Fed 現行「高利率長駐」的鷹派引導下，科技股高估值的折現率壓力依然是壓制指數的核心。
          </div>
        </div>
      </div>
    </section>

    <!-- 4. 板塊表現 -->
    <section id="sectors" class="mb-12 scroll-mt-6">
      <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-4 mb-4 border-b border-zinc-100 dark:border-zinc-800 pb-2">
        <h2 class="text-2xl font-bold flex items-center gap-2">
          <span class="text-brand-500">4.</span> S&P 500 十一個板塊表現 (2026-06-22)
        </h2>
        <input type="text" id="sectorSearch" placeholder="搜尋板塊或 ETF..." class="px-3 py-1.5 text-sm rounded-md border border-zinc-300 dark:border-zinc-700 bg-white dark:bg-zinc-900 focus:outline-none focus:ring-1 focus:ring-brand-500">
      </div>

      <div class="overflow-x-auto border border-zinc-200 dark:border-zinc-800 rounded-xl">
        <table class="min-w-full divide-y divide-zinc-200 dark:divide-zinc-800 text-sm" id="sectorsTable">
          <thead class="bg-zinc-50 dark:bg-zinc-900 select-none">
            <tr>
              <th onclick="sortSectors(0)" class="cursor-pointer hover:bg-zinc-100 dark:hover:bg-zinc-800 px-4 py-3 text-left font-semibold text-zinc-600 dark:text-zinc-400">排名 ▲▼</th>
              <th onclick="sortSectors(1)" class="cursor-pointer hover:bg-zinc-100 dark:hover:bg-zinc-800 px-4 py-3 text-left font-semibold text-zinc-600 dark:text-zinc-400">板塊 ▲▼</th>
              <th onclick="sortSectors(2)" class="cursor-pointer hover:bg-zinc-100 dark:hover:bg-zinc-800 px-4 py-3 text-left font-semibold text-zinc-600 dark:text-zinc-400">ETF ▲▼</th>
              <th onclick="sortSectors(3)" class="cursor-pointer hover:bg-zinc-100 dark:hover:bg-zinc-800 px-4 py-3 text-right font-semibold text-zinc-600 dark:text-zinc-400">當日變動 ▲▼</th>
              <th onclick="sortSectors(4)" class="cursor-pointer hover:bg-zinc-100 dark:hover:bg-zinc-800 px-4 py-3 text-right font-semibold text-zinc-600 dark:text-zinc-400">本月累計 ▲▼</th>
              <th class="px-4 py-3 text-left font-semibold text-zinc-600 dark:text-zinc-400">今日主要驅動因素</th>
            </tr>
          </thead>
          <tbody class="divide-y divide-zinc-200 dark:divide-zinc-800">
            <tr>
              <td class="px-4 py-3 font-medium">1</td>
              <td class="px-4 py-3 font-medium">醫療 (Health Care)</td>
              <td class="px-4 py-3 font-mono">XLV</td>
              <td class="px-4 py-3 text-right font-mono text-emerald-500 font-semibold" data-val="0.95">+0.95%</td>
              <td class="px-4 py-3 text-right font-mono" data-val="3.10">+3.10%</td>
              <td class="px-4 py-3 text-zinc-500 dark:text-zinc-400">資金顯著流入防禦性藍籌股，大型製藥與醫療保險龍頭護盤。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-medium">2</td>
              <td class="px-4 py-3 font-medium">能源 (Energy)</td>
              <td class="px-4 py-3 font-mono">XLE</td>
              <td class="px-4 py-3 text-right font-mono text-emerald-500 font-semibold" data-val="0.85">+0.85%</td>
              <td class="px-4 py-3 text-right font-mono" data-val="1.45">+1.45%</td>
              <td class="px-4 py-3 text-zinc-500 dark:text-zinc-400">雖然油價重挫，但資金看好地緣局勢緩和下的全球供應穩定，低位防禦資金抱團。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-medium">3</td>
              <td class="px-4 py-3 font-medium">房地產 (Real Estate)</td>
              <td class="px-4 py-3 font-mono">XLRE</td>
              <td class="px-4 py-3 text-right font-mono text-emerald-500 font-semibold" data-val="0.65">+0.65%</td>
              <td class="px-4 py-3 text-right font-mono" data-val="-1.20">-1.20%</td>
              <td class="px-4 py-3 text-zinc-500 dark:text-zinc-400">避險買盤帶動，對高油價和地緣焦慮的降溫減輕了營運擔憂。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-medium">4</td>
              <td class="px-4 py-3 font-medium">消費者必需品 (Consumer Staples)</td>
              <td class="px-4 py-3 font-mono">XLP</td>
              <td class="px-4 py-3 text-right font-mono text-emerald-500 font-semibold" data-val="0.50">+0.50%</td>
              <td class="px-4 py-3 text-right font-mono" data-val="2.40">+2.40%</td>
              <td class="px-4 py-3 text-zinc-500 dark:text-zinc-400">典型的 Risk-off 防禦配置，受地緣局勢緩和與高股息配置需求推升。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-medium">5</td>
              <td class="px-4 py-3 font-medium">公用事業 (Utilities)</td>
              <td class="px-4 py-3 font-mono">XLU</td>
              <td class="px-4 py-3 text-right font-mono text-emerald-500 font-semibold" data-val="0.40">+0.40%</td>
              <td class="px-4 py-3 text-right font-mono" data-val="3.75">+3.75%</td>
              <td class="px-4 py-3 text-zinc-500 dark:text-zinc-400">AI 資料中心用電需求剛性預期，配合防禦配置，無視债息飆升走高。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-medium">6</td>
              <td class="px-4 py-3 font-medium">金融 (Financials)</td>
              <td class="px-4 py-3 font-mono">XLF</td>
              <td class="px-4 py-3 text-right font-mono text-emerald-500 font-semibold" data-val="0.30">+0.30%</td>
              <td class="px-4 py-3 text-right font-mono" data-val="2.15">+2.15%</td>
              <td class="px-4 py-3 text-zinc-500 dark:text-zinc-400">美債收益率高位攀升，利多銀行業淨息差利潤，金融股高位持穩。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-medium">7</td>
              <td class="px-4 py-3 font-medium">基礎材料 (Materials)</td>
              <td class="px-4 py-3 font-mono">XLB</td>
              <td class="px-4 py-3 text-right font-mono text-rose-500 font-semibold" data-val="-0.20">-0.20%</td>
              <td class="px-4 py-3 text-right font-mono" data-val="1.10">+1.10%</td>
              <td class="px-4 py-3 text-zinc-500 dark:text-zinc-400">商品市場漲跌互現，化學與包裝材料股微幅走弱。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-medium">8</td>
              <td class="px-4 py-3 font-medium">資訊科技 (Information Technology)</td>
              <td class="px-4 py-3 font-mono">XLK</td>
              <td class="px-4 py-3 text-right font-mono text-rose-500 font-semibold" data-val="-1.25">-1.25%</td>
              <td class="px-4 py-3 text-right font-mono" data-val="3.90">+3.90%</td>
              <td class="px-4 py-3 text-zinc-500 dark:text-zinc-400">微軟、蘋果高位整理，SaaS 板塊跟跌，雖有英特爾大漲但未能扭轉科技頹勢。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-medium">9</td>
              <td class="px-4 py-3 font-medium">非必需消費 (Consumer Discretionary)</td>
              <td class="px-4 py-3 font-mono">XLY</td>
              <td class="px-4 py-3 text-right font-mono text-rose-500 font-semibold" data-val="-1.50">-1.50%</td>
              <td class="px-4 py-3 text-right font-mono" data-val="1.85">+1.85%</td>
              <td class="px-4 py-3 text-zinc-500 dark:text-zinc-400">主要權重股亞馬遜大跌 4.45% 拖累板塊，特斯拉小漲 +1.1% 勉強對沖。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-medium">10</td>
              <td class="px-4 py-3 font-medium">工業 (Industrials)</td>
              <td class="px-4 py-3 font-mono">XLI</td>
              <td class="px-4 py-3 text-right font-mono text-rose-500 font-semibold" data-val="-3.10">-3.10%</td>
              <td class="px-4 py-3 text-right font-mono" data-val="-0.85">-0.85%</td>
              <td class="px-4 py-3 text-zinc-500 dark:text-zinc-400">航運與重裝製造業高位大幅回吐，SpaceX (SPCX) 發債暴跌重創相關板塊人氣。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-medium">11</td>
              <td class="px-4 py-3 font-medium">通訊服務 (Communication Services)</td>
              <td class="px-4 py-3 font-mono">XLC</td>
              <td class="px-4 py-3 text-right font-mono text-rose-500 font-semibold" data-val="-3.20">-3.20%</td>
              <td class="px-4 py-3 text-right font-mono" data-val="1.40">+1.40%</td>
              <td class="px-4 py-3 text-zinc-500 dark:text-zinc-400">權重巨頭 Alphabet 因 AI 人才離職潮大跌 5.22%，Meta 下跌 1.80% 共同拖累。</td>
            </tr>
          </tbody>
        </table>
      </div>
    </section>

    <!-- 5. 主題與風格表現 -->
    <section id="themes" class="mb-12 scroll-mt-6">
      <h2 class="text-2xl font-bold mb-4 flex items-center gap-2 border-b border-zinc-100 dark:border-zinc-800 pb-2">
        <span class="text-brand-500">5.</span> 主題與風格表現
      </h2>
      <div class="grid grid-cols-1 md:grid-cols-3 gap-6 text-sm">
        <div class="p-5 bg-zinc-50 dark:bg-zinc-900 border border-zinc-200 dark:border-zinc-800 rounded-xl">
          <h4 class="font-bold text-zinc-800 dark:text-zinc-200 mb-2">半導體與 AI 硬體抱團依舊</h4>
          <p class="text-zinc-500 dark:text-zinc-400 leading-relaxed">
            半導體 ETF (SMH) 與費半 (SOX) 呈現多頭分化護盤。英特爾 (INTC) 與台積電 (TSM) ADR 表現強勢，這表明市場對於 AI 半導體物理層與國產化代工的邏輯依然極為認可，資金依然在晶片硬體板塊中強力抱團。
          </p>
        </div>
        <div class="p-5 bg-zinc-50 dark:bg-zinc-900 border border-zinc-200 dark:border-zinc-800 rounded-xl">
          <h4 class="font-bold text-zinc-800 dark:text-zinc-200 mb-2">應用軟體 (SaaS) 與大盤科技失血</h4>
          <p class="text-zinc-555 dark:text-zinc-400 leading-relaxed">
            高倍數 SaaS 應用軟體板塊 (IGV) 在高債息與高利率長駐的壓制下，合約增長放緩，資金抽離跡象明顯。大型軟體股與 SaaS 指標（CRM、NOW）在均線下方延續震盪整理。
          </p>
        </div>
        <div class="p-5 bg-zinc-50 dark:bg-zinc-900 border border-zinc-200 dark:border-zinc-800 rounded-xl">
          <h4 class="font-bold text-zinc-800 dark:text-zinc-200 mb-2">太空科技與基建巨震</h4>
          <p class="text-zinc-500 dark:text-zinc-400 leading-relaxed">
            SpaceX (SPCX) 作為新上市的太空與 AI 基建雙核心巨頭，在經歷了上週的飆升後，今日宣佈大規模發債 200 億美元 senior notes 引發大額套現去槓桿賣壓，加之 MSCI 給予的不利評級，單日重挫 16.4%，大幅衝擊了新興成長股的主線氣氛。
          </p>
        </div>
      </div>
    </section>

    <!-- 6. 市場寬度與參與度 -->
    <section id="breadth" class="mb-12 scroll-mt-6">
      <h2 class="text-2xl font-bold mb-4 flex items-center gap-2 border-b border-zinc-100 dark:border-zinc-800 pb-2">
        <span class="text-brand-500">6.</span> 市場寬度與參與度
      </h2>
      <div class="grid grid-cols-1 md:grid-cols-3 gap-6 text-sm">
        <div class="p-5 bg-zinc-50 dark:bg-zinc-900 border border-zinc-200 dark:border-zinc-800 rounded-xl text-center">
          <span class="text-xs text-zinc-400 font-semibold uppercase tracking-wider block mb-1">均線參與度 (高於 50MA 比例)</span>
          <span class="text-3xl font-extrabold text-brand-500 font-mono">68.5%</span>
          <p class="text-zinc-500 dark:text-zinc-400 mt-2 text-xs">S&P 500 成份股守穩 50MA 比例上升，大盤中長期健康度仍屬良好，板塊實現輪動。</p>
        </div>
        <div class="p-5 bg-zinc-50 dark:bg-zinc-900 border border-zinc-200 dark:border-zinc-800 rounded-xl text-center">
          <span class="text-xs text-zinc-400 font-semibold uppercase tracking-wider block mb-1">漲跌家數比 (NYSE / Nasdaq)</span>
          <span class="text-3xl font-extrabold text-emerald-500 font-mono">1.38 : 1</span>
          <p class="text-zinc-500 dark:text-zinc-400 mt-2 text-xs">紐交所與納交所上漲股票總數多於下跌股票，小盤股大面積收紅抵消了大權重科技股下殺。</p>
        </div>
        <div class="p-5 bg-zinc-50 dark:bg-zinc-900 border border-zinc-200 dark:border-zinc-800 rounded-xl text-center">
          <span class="text-xs text-zinc-400 font-semibold uppercase tracking-wider block mb-1">52週新高 - 新低差值</span>
          <span class="text-3xl font-extrabold text-emerald-500 font-mono">+112 家</span>
          <p class="text-zinc-500 dark:text-zinc-400 mt-2 text-xs">新高家數多於新低家數，尤其重電、醫療與金融股集中刷新歷史新高，寬度表現良性。</p>
        </div>
      </div>
    </section>

    <!-- 7. 技術面分析 -->
    <section id="technical" class="mb-12 scroll-mt-6">
      <h2 class="text-2xl font-bold mb-4 flex items-center gap-2 border-b border-zinc-100 dark:border-zinc-800 pb-2">
        <span class="text-brand-500">7.</span> 技術面分析
      </h2>
      <div class="overflow-x-auto border border-zinc-200 dark:border-zinc-800 rounded-xl">
        <table class="min-w-full divide-y divide-zinc-200 dark:divide-zinc-850 text-sm text-left">
          <thead class="bg-zinc-50 dark:bg-zinc-900">
            <tr class="text-zinc-555 dark:text-zinc-400">
              <th class="px-4 py-3 font-semibold">ETF 名稱</th>
              <th class="px-4 py-3 font-semibold text-right">當前價格</th>
              <th class="px-4 py-3 font-semibold">均線位置與技術狀態</th>
              <th class="px-4 py-3 text-center font-semibold">RSI (14)</th>
              <th class="px-4 py-3 font-semibold">趨勢與明日期望</th>
              <th class="px-4 py-3 font-semibold">關鍵支撐 / 阻力</th>
            </tr>
          </thead>
          <tbody class="divide-y divide-zinc-200 dark:divide-zinc-850 font-mono text-zinc-700 dark:text-zinc-300">
            <tr>
              <td class="px-4 py-3 font-semibold font-sans text-zinc-900 dark:text-zinc-100">SPY (S&P 500)</td>
              <td class="px-4 py-3 text-right">$747.28</td>
              <td class="px-4 py-3 font-sans text-xs text-amber-500">受阻於 $750 整數大關，高位窄幅收縮回踩 10MA</td>
              <td class="px-4 py-3 text-center">59</td>
              <td class="px-4 py-3 font-sans text-xs text-emerald-500">中性偏多，回踩 10MA 守穩可重新走強</td>
              <td class="px-4 py-3 font-sans text-xs">$742 / $753</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold font-sans text-zinc-900 dark:text-zinc-100">QQQ (Nasdaq 100)</td>
              <td class="px-4 py-3 text-right">$730.34</td>
              <td class="px-4 py-3 font-sans text-xs text-rose-500">跌破 5MA ($738.5)，回踩 10MA ($729) 尋求支撐</td>
              <td class="px-4 py-3 text-center">54</td>
              <td class="px-4 py-3 font-sans text-xs text-rose-500">短期超買回吐，不急於接刀，等待 10MA 防守確認</td>
              <td class="px-4 py-3 font-sans text-xs">$728 / $741</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold font-sans text-zinc-900 dark:text-zinc-100">IWM (Russell 2000)</td>
              <td class="px-4 py-3 text-right">$300.44</td>
              <td class="px-4 py-3 font-sans text-xs text-emerald-500">強勢帶量向上突破 50MA 及 20MA，站上 3000 大關</td>
              <td class="px-4 py-3 text-center">61</td>
              <td class="px-4 py-3 font-sans text-xs text-emerald-500">底部黃金交叉形態，油價大跌為中小型股續航提供動能</td>
              <td class="px-4 py-3 font-sans text-xs">$296 / $305</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold font-sans text-zinc-900 dark:text-zinc-100">SMH (Semiconductor)</td>
              <td class="px-4 py-3 text-right">$285.50</td>
              <td class="px-4 py-3 font-sans text-xs text-emerald-500">費半逆勢創高，成份股維持 5MA 短期均線支撐之上</td>
              <td class="px-4 py-3 text-center">69</td>
              <td class="px-4 py-3 font-sans text-xs text-amber-500">極度超買但買力強盛，維持高位整固</td>
              <td class="px-4 py-3 font-sans text-xs">$278 / $292</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold font-sans text-zinc-900 dark:text-zinc-100">IGV (Software)</td>
              <td class="px-4 py-3 text-right">$481.50</td>
              <td class="px-4 py-3 font-sans text-xs text-rose-500">延續跌勢破 100MA，測試下軌支撐</td>
              <td class="px-4 py-3 text-center">28</td>
              <td class="px-4 py-3 font-sans text-xs text-rose-500">指標極度超賣，但拋售量能尚未衰竭，觀望為主</td>
              <td class="px-4 py-3 font-sans text-xs">$475 / $495</td>
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

      <div class="space-y-4">
        <!-- 8.1 大型科技七巨頭 -->
        <details class="bg-zinc-50 dark:bg-zinc-900 border border-zinc-200 dark:border-zinc-800 rounded-xl p-4" open>
          <summary class="font-bold text-zinc-800 dark:text-zinc-200 text-sm sm:text-base">8.1 大型科技七巨頭 (NVDA, GOOGL, MSFT, META, AMZN, AAPL, TSLA) 異動與新聞</summary>
          <div class="mt-3 space-y-3 pl-4 text-sm leading-relaxed text-zinc-650 dark:text-zinc-400 border-l-2 border-zinc-200 dark:border-zinc-800">
            <p><strong>GOOGL (Alphabet):</strong> 下跌 <strong>-5.22%</strong> 收報 <strong>$348.67</strong>。市場高度擔憂 DeepMind 多位資深 AI 科學家跳槽至新興大模型初創公司，引發技術領先優勢動搖的預期；此外，$800 億股權增發的資金稀釋效應亦持續壓制估值。</p>
            <p><strong>AMZN (亞馬遜):</strong> 下跌 <strong>-4.45%</strong> 收報 <strong>$233.52</strong>。儘管油價下跌利多物流配送開支，但大盤科技股整體遭遇去槓桿調倉，拖累股價跌破短期均線支撐。</p>
            <p><strong>META (Meta Platforms):</strong> 下跌 <strong>-1.80%</strong> 收報 <strong>$563.85</strong>。隨大市自歷史高位回吐，在 5MA 位置尋求首個支撐防線。</p>
            <p><strong>MSFT (微軟):</strong> 下跌 <strong>-1.64%</strong> 收報 <strong>$372.40</strong>。美債殖利率反彈對其 Azure 雲端業務估值折現率帶來微幅壓制，股價失守 20MA。</p>
            <p><strong>AAPL (蘋果):</strong> 下跌 <strong>-0.95%</strong> 收報 <strong>$293.12</strong>。在高位震盪休整，但本土代工合作預期為其提供了一定的安全墊。</p>
            <p><strong>NVDA (輝達):</strong> 下跌 <strong>-1.10%</strong> 收報 <strong>$208.65</strong>。資金部份移防至估值較低的 INTC 及 TSM，股價於高位守住 10MA 支撐，多頭主線邏輯未受動搖。</p>
            <p><strong>TSLA (特斯拉):</strong> 逆市上漲 <strong>+1.10%</strong> 收報 <strong>$405.05</strong>。原油大跌及地緣局勢緩和引導普通民眾消費預期復甦，激勵股價沿 5MA 小幅走高。</p>
          </div>
        </details>

        <!-- 8.2 AI 硬體 / 半導體重點股 -->
        <details class="bg-zinc-50 dark:bg-zinc-900 border border-zinc-200 dark:border-zinc-800 rounded-xl p-4">
          <summary class="font-bold text-zinc-800 dark:text-zinc-200 text-sm sm:text-base">8.2 AI 硬體 / 半導體重點股 (Intel, TSM, AMD, AVGO, MRVL, ARM, ASML)</summary>
          <div class="mt-3 space-y-3 pl-4 text-sm leading-relaxed text-zinc-650 dark:text-zinc-400 border-l-2 border-zinc-200 dark:border-zinc-800">
            <p><strong>Intel (INTC):</strong> 大漲 <strong>+5.20%</strong> 收 <strong>$140.94</strong>。與 Apple 在美本土設計及代工合作的進展被進一步發酵，且傳聞其 18A-P 工藝順利獲得 Google 雲端晶片代工訂單，刺激代工估值大爆發。</p>
            <p><strong>TSM (台積電ADR):</strong> 上漲 <strong>+1.30%</strong> 收 <strong>$468.08</strong>。投行 Susquehanna 發佈重磅策略報告，大讚其在 2nm 及 CoWoS 封裝的霸主地位不可動搖，並將目標價一口氣上調至 $575.00，激勵股價逆市創歷史新高。</p>
            <p><strong>AMD (超微):</strong> 上漲 <strong>+2.65%</strong> 收報 <strong>$551.67</strong>。部分輝達套現資金流入估值相對較低的超微，帶動股價突破 $550 心理關口。</p>
            <p><strong>ARM (安謀):</strong> 下跌 <strong>-6.00%</strong> 收報 <strong>$413.00</strong>。在高位超買嚴重的背景下遭遇了劇烈的手機與客戶端晶片熱錢套現去槓桿。</p>
            <p><strong>AVGO (博通):</strong> 下跌 <strong>-4.03%</strong> 收報 <strong>$392.13</strong>。主要因大客戶訂單調整傳聞干擾，股價回踩 20MA 支撐位。</p>
          </div>
        </details>

        <!-- 8.3 軟體 / SaaS / AI 應用與新股 -->
        <details class="bg-zinc-50 dark:bg-zinc-900 border border-zinc-200 dark:border-zinc-800 rounded-xl p-4">
          <summary class="font-bold text-zinc-800 dark:text-zinc-200 text-sm sm:text-base">8.3 軟體 / SaaS / AI 應用與新股 (SPCX, PLTR, ORCL, CRM, NOW, SNOW, ADBE)</summary>
          <div class="mt-3 space-y-3 pl-4 text-sm leading-relaxed text-zinc-650 dark:text-zinc-400 border-l-2 border-zinc-200 dark:border-zinc-800">
            <p><strong>SpaceX (SPCX):</strong> 崩瀉 <strong>-16.40%</strong> 收報 <strong>$154.60</strong>。宣佈將啟動發行高達 200 億美元的 senior unsecured notes，以全額償還過渡期貸款並建置 colossus 數據中心。發債帶來的融資壓力及 MSCI 给予的不利 ESG 評級，疊加期權做空工具引入，引發多頭資金大舉踩踏踩退。</p>
            <p><strong>PLTR (Palantir):</strong> 大跌 <strong>-8.14%</strong> 收報 <strong>$120.00</strong>。高息環境重創 AI 應用估值乘數，股價出現放量補跌，測試 50MA 支撐。</p>
            <p><strong>ORCL (甲骨文):</strong> 大跌 <strong>-5.00%</strong> 收報 <strong>$175.07</strong>。受大盤軟體板塊慘遭抽血影響，回吐上週大漲幅度，测试 10MA 支撐。</p>
          </div>
        </details>
      </div>
    </section>

    <!-- 9. 財報日曆與財報解讀 -->
    <section id="earnings" class="mb-12 scroll-mt-6">
      <h2 class="text-2xl font-bold mb-4 flex items-center gap-2 border-b border-zinc-100 dark:border-zinc-800 pb-2">
        <span class="text-brand-500">9.</span> 財報日曆與財報解讀
      </h2>
      <div class="grid grid-cols-1 md:grid-cols-2 gap-6 text-sm">
        <div class="p-5 bg-zinc-50 dark:bg-zinc-900 border border-zinc-200 dark:border-zinc-800 rounded-xl">
          <h4 class="font-bold text-zinc-800 dark:text-zinc-200 mb-2">9.1 今日財報重點解讀</h4>
          <p class="text-zinc-500 dark:text-zinc-400 leading-relaxed mb-3">
            <strong>FDS (FactSet) - 週一盤前公佈：</strong>第一財季營收符合預期，但 EPS 微 beat。由於高息環境下全球中小投行和買方機構縮減終端機軟體開支，其合約訂閱指引僅微增 1.5%，這進一步佐證了企業在 SaaS 應用採購上的防禦保守心態，壓制了整體應用軟體估值。
          </p>
        </div>
        <div class="p-5 bg-zinc-50 dark:bg-zinc-900 border border-zinc-200 dark:border-zinc-800 rounded-xl">
          <h4 class="font-bold text-zinc-800 dark:text-zinc-200 mb-2">9.2 本週接下來 1-3 個交易日財報日曆</h4>
          <p class="text-zinc-500 dark:text-zinc-400 leading-relaxed">
            - <strong>CarMax (KMX) - 週二：</strong>解讀高利率、油價變動對美國普通家庭中古車大宗開支與信用貸款逾期率的實質衝擊。<br>
            - <strong>Accenture (ACN) - 週三：</strong>本季重中之重，將為全球企業 AI 雲端轉型與大模型諮詢外包需求給予最權威的訂單指引。
          </p>
        </div>
      </div>
    </section>

    <!-- 10. 機構觀點與資金流 -->
    <section id="institution" class="mb-12 scroll-mt-6">
      <h2 class="text-2xl font-bold mb-4 flex items-center gap-2 border-b border-zinc-100 dark:border-zinc-800 pb-2">
        <span class="text-brand-500">10.</span> 機構觀點與資金流
      </h2>
      <div class="bg-zinc-50 dark:bg-zinc-900 p-6 rounded-xl border border-zinc-200 dark:border-zinc-800 leading-relaxed text-sm">
        <p class="mb-3">
          <strong>摩根大通策略部 (JPMorgan):</strong> 儘管新主席引導的 Fed「防禦性加息」概率浮現，但美伊達成和平協定將原油壓至 $74 關卡，已實質性地排除了下半年發生大宗商品惡性通膨的風險。高息會壓抑 SaaS 的合約增速，但對於製造業與實體經濟卻是良性軟著陸的基礎。
        </p>
        <p>
          <strong>大宗交易與資金流向：</strong>今日大宗交易顯示，大量的對沖基金資金從 Alphabet、Amazon 中套現，轉而大舉加碼重電設備（ETN、VRT）及德州供電概念（VST），顯示機構在「AI 基礎設施物理層」上的供需能見度遠高於應用軟體層。
        </p>
      </div>
    </section>

    <!-- 11. 板塊輪動判斷 -->
    <section id="rotation" class="mb-12 scroll-mt-6">
      <h2 class="text-2xl font-bold mb-4 flex items-center gap-2 border-b border-zinc-100 dark:border-zinc-800 pb-2">
        <span class="text-brand-500">11.</span> 板塊輪動判斷
      </h2>
      <div class="bg-zinc-50 dark:bg-zinc-900 p-6 rounded-xl border border-zinc-200 dark:border-zinc-800 leading-relaxed text-sm">
        <p>
          今日市場板塊輪動發揮了極佳的「避險安全墊」作用。雖然納指大跌 1.32%，但羅素 2000 與藍籌防禦（XLV、XLP、XLU）全線走強，市場並沒有出現流動性恐慌，反而是高位熱錢移防的良性牛市特徵。AI 主線正進一步收斂至半導體國產製造鏈與重電核能供電基建，防禦型牛市的健康度依然得以維持。
        </p>
      </div>
    </section>

    <!-- 12. 我的重點關注股觀察 -->
    <section id="watchlist" class="mb-12 scroll-mt-6">
      <h2 class="text-2xl font-bold mb-4 flex items-center gap-2 border-b border-zinc-100 dark:border-zinc-800 pb-2">
        <span class="text-brand-500">12.</span> 我的重點關注股觀察
      </h2>
      
      <div class="overflow-x-auto border border-zinc-200 dark:border-zinc-800 rounded-xl">
        <table class="min-w-full divide-y divide-zinc-200 dark:divide-zinc-800 text-sm">
          <thead class="bg-zinc-50 dark:bg-zinc-900">
            <tr class="text-zinc-555 dark:text-zinc-400 text-left">
              <th class="px-4 py-3 font-semibold">代碼</th>
              <th class="px-4 py-3 font-semibold text-right">收盤價格 (當日變動)</th>
              <th class="px-4 py-3">技術與趨勢特徵</th>
              <th class="px-4 py-3 text-center">交易判定</th>
              <th class="px-4 py-3 text-left">關鍵位置與操作說明</th>
            </tr>
          </thead>
          <tbody class="divide-y divide-zinc-200 dark:divide-zinc-850 font-mono text-zinc-700 dark:text-zinc-300">
            <tr>
              <td class="px-4 py-3 font-semibold font-sans text-zinc-900 dark:text-zinc-100">NVDA</td>
              <td class="px-4 py-3 text-right text-rose-500 font-semibold">$208.65 (-1.10%)</td>
              <td class="px-4 py-3 font-sans">高位窄幅收縮，回踩 10MA 支撐</td>
              <td class="px-4 py-3 text-center font-sans"><span class="px-2 py-0.5 rounded bg-amber-100 dark:bg-amber-950 text-amber-800 dark:text-amber-350 text-xs font-semibold">回踩支撐</span></td>
              <td class="px-4 py-3 font-sans text-xs">主線物理層，回調是良性分批配置機會。支撐 $202，壓力 $215。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold font-sans text-zinc-900 dark:text-zinc-100">AMD</td>
              <td class="px-4 py-3 text-right text-emerald-500 font-semibold">$551.67 (+2.65%)</td>
              <td class="px-4 py-3 font-sans">放量逆勢突圍，重回 5MA 均線之上</td>
              <td class="px-4 py-3 text-center font-sans"><span class="px-2 py-0.5 rounded bg-emerald-100 dark:bg-emerald-950 text-emerald-800 dark:text-emerald-350 text-xs font-semibold">繼續強勢</span></td>
              <td class="px-4 py-3 font-sans text-xs">受惠於輝達套現溢出資金。支撐 $535，阻力 $560。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold font-sans text-zinc-900 dark:text-zinc-100">AVGO</td>
              <td class="px-4 py-3 text-right text-rose-500 font-semibold">$392.13 (-4.03%)</td>
              <td class="px-4 py-3 font-sans">放量回調，回踩 20MA 支撐</td>
              <td class="px-4 py-3 text-center font-sans"><span class="px-2 py-0.5 rounded bg-amber-100 dark:bg-amber-950 text-amber-800 dark:text-amber-350 text-xs font-semibold">回踩支撐</span></td>
              <td class="px-4 py-3 font-sans text-xs">大客戶合約訂單微調傳聞利空，等待 20MA 守穩。支撐 $385。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold font-sans text-zinc-900 dark:text-zinc-100">MRVL</td>
              <td class="px-4 py-3 text-right text-rose-500 font-semibold">$308.04 (-5.07%)</td>
              <td class="px-4 py-3 font-sans">跟隨大市調整，回踩突破後的箱體上軌</td>
              <td class="px-4 py-3 text-center font-sans"><span class="px-2 py-0.5 rounded bg-amber-100 dark:bg-amber-950 text-amber-800 dark:text-amber-350 text-xs font-semibold">回踩支撐</span></td>
              <td class="px-4 py-3 font-sans text-xs">良性回調，測試前箱體阻力變支撐（$305）。支撐 $305。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold font-sans text-zinc-900 dark:text-zinc-100">GOOGL</td>
              <td class="px-4 py-3 text-right text-rose-500 font-semibold">$348.67 (-5.22%)</td>
              <td class="px-4 py-3 font-sans">長黑 K 破 20MA，面臨 AI 人才流失利空打壓</td>
              <td class="px-4 py-3 text-center font-sans"><span class="px-2 py-0.5 rounded bg-rose-100 dark:bg-rose-950 text-rose-800 dark:text-rose-350 text-xs font-semibold">破位風險</span></td>
              <td class="px-4 py-3 font-sans text-xs">技術面轉弱，在 $342 尋求 50MA 支撐，暫時觀望。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold font-sans text-zinc-900 dark:text-zinc-100">MSFT</td>
              <td class="px-4 py-3 text-right text-rose-500 font-semibold">$372.40 (-1.64%)</td>
              <td class="px-4 py-3 font-sans">跌破 20MA，受制於長息彈升折現率壓力</td>
              <td class="px-4 py-3 text-center font-sans"><span class="px-2 py-0.5 rounded bg-zinc-100 dark:bg-zinc-800 text-zinc-800 dark:text-zinc-300 text-xs font-semibold">高位震盪</span></td>
              <td class="px-4 py-3 font-sans text-xs">防禦屬性佳但缺乏突破動能。支撐 $368，壓力 $385。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold font-sans text-zinc-900 dark:text-zinc-100">META</td>
              <td class="px-4 py-3 text-right text-rose-500 font-semibold">$563.85 (-1.80%)</td>
              <td class="px-4 py-3 font-sans">高位獲利回吐，守在 10MA 支撐</td>
              <td class="px-4 py-3 text-center font-sans"><span class="px-2 py-0.5 rounded bg-zinc-100 dark:bg-zinc-800 text-zinc-800 dark:text-zinc-300 text-xs font-semibold">高位震盪</span></td>
              <td class="px-4 py-3 font-sans text-xs">防守 10MA ($560) 平台支撐，不宜盲目追高。支撐 $560。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold font-sans text-zinc-900 dark:text-zinc-100">AMZN</td>
              <td class="px-4 py-3 text-right text-rose-500 font-semibold">$233.52 (-4.45%)</td>
              <td class="px-4 py-3 font-sans">大長黑 K 破短期均線，抹去上週大部漲幅</td>
              <td class="px-4 py-3 text-center font-sans"><span class="px-2 py-0.5 rounded bg-amber-100 dark:bg-amber-950 text-amber-800 dark:text-amber-350 text-xs font-semibold">回踩支撐</span></td>
              <td class="px-4 py-3 font-sans text-xs">大跌後測試 20MA ($232)。支撐 $232，阻力 $242。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold font-sans text-zinc-900 dark:text-zinc-100">ORCL</td>
              <td class="px-4 py-3 text-right text-rose-500 font-semibold">$175.07 (-5.00%)</td>
              <td class="px-4 py-3 font-sans">隨軟體板塊流血而大跌，跌破 5MA</td>
              <td class="px-4 py-3 text-center font-sans"><span class="px-2 py-0.5 rounded bg-amber-100 dark:bg-amber-950 text-amber-800 dark:text-amber-350 text-xs font-semibold">回踩支撐</span></td>
              <td class="px-4 py-3 font-sans text-xs">回試上週突破口 $174 支撐，此位置具較強買盤。支撐 $174。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold font-sans text-zinc-900 dark:text-zinc-100">CRM</td>
              <td class="px-4 py-3 text-right text-emerald-500 font-semibold">$151.78 (+0.07%)</td>
              <td class="px-4 py-3 font-sans">超跌後低量窄幅橫盤企穩</td>
              <td class="px-4 py-3 text-center font-sans"><span class="px-2 py-0.5 rounded bg-zinc-100 dark:bg-zinc-800 text-zinc-800 dark:text-zinc-300 text-xs font-semibold">需要觀察</span></td>
              <td class="px-4 py-3 font-sans text-xs">在 $150 關卡嘗試築底。不宜進場，防守 $148。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold font-sans text-zinc-900 dark:text-zinc-100">NOW</td>
              <td class="px-4 py-3 text-right text-rose-500 font-semibold">$94.44 (-1.09%)</td>
              <td class="px-4 py-3 font-sans">超跌後橫盤，缺乏買盤支撐</td>
              <td class="px-4 py-3 text-center font-sans"><span class="px-2 py-0.5 rounded bg-zinc-100 dark:bg-zinc-800 text-zinc-800 dark:text-zinc-300 text-xs font-semibold">需要觀察</span></td>
              <td class="px-4 py-3 font-sans text-xs">技術破位後的震盪修復。支撐 $92，阻力 $98。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold font-sans text-zinc-900 dark:text-zinc-100">SNOW</td>
              <td class="px-4 py-3 text-right text-rose-500 font-semibold">$232.29 (-0.95%)</td>
              <td class="px-4 py-3 font-sans">低位量縮橫盤，維持區間防守</td>
              <td class="px-4 py-3 text-center font-sans"><span class="px-2 py-0.5 rounded bg-zinc-100 dark:bg-zinc-800 text-zinc-800 dark:text-zinc-300 text-xs font-semibold">需要觀察</span></td>
              <td class="px-4 py-3 font-sans text-xs">SaaS 人氣低迷。防守 $230 整數關卡。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold font-sans text-zinc-900 dark:text-zinc-100">ADBE</td>
              <td class="px-4 py-3 text-right text-rose-500 font-semibold">$195.16 (-0.07%)</td>
              <td class="px-4 py-3 font-sans">在 $195 心理關卡拉鋸防守</td>
              <td class="px-4 py-3 text-center font-sans"><span class="px-2 py-0.5 rounded bg-amber-100 dark:bg-amber-950 text-amber-800 dark:text-amber-350 text-xs font-semibold">回踩支撐</span></td>
              <td class="px-4 py-3 font-sans text-xs">大跌超賣後的抵抗。觀望 $190 關鍵防線。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold font-sans text-zinc-900 dark:text-zinc-100">PLTR</td>
              <td class="px-4 py-3 text-right text-rose-500 font-semibold">$120.00 (-8.14%)</td>
              <td class="px-4 py-3 font-sans">放量暴跌，跌破 20MA，測試 50MA</td>
              <td class="px-4 py-3 text-center font-sans"><span class="px-2 py-0.5 rounded bg-rose-100 dark:bg-rose-950 text-rose-800 dark:text-rose-350 text-xs font-semibold">破位風險</span></td>
              <td class="px-4 py-3 font-sans text-xs">AI 應用估值乘數被殺。觀望不抄底，防守支撐 $118。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold font-sans text-zinc-900 dark:text-zinc-100">LITE</td>
              <td class="px-4 py-3 text-right text-rose-500 font-semibold">$836.76 (-4.17%)</td>
              <td class="px-4 py-3 font-sans">隨光模組高位修正，跌破 10MA</td>
              <td class="px-4 py-3 text-center font-sans"><span class="px-2 py-0.5 rounded bg-amber-100 dark:bg-amber-950 text-amber-800 dark:text-amber-350 text-xs font-semibold">回踩支撐</span></td>
              <td class="px-4 py-3 font-sans text-xs">良性修正，觀察 20MA ($825) 的防守力度。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold font-sans text-zinc-900 dark:text-zinc-100">COHR</td>
              <td class="px-4 py-3 text-right text-emerald-500 font-semibold">$401.70 (+5.40%)</td>
              <td class="px-4 py-3 font-sans">逆市拉出大陽 K 棒，站穩所有均線</td>
              <td class="px-4 py-3 text-center font-sans"><span class="px-2 py-0.5 rounded bg-emerald-100 dark:bg-emerald-950 text-emerald-800 dark:text-emerald-350 text-xs font-semibold">繼續強勢</span></td>
              <td class="px-4 py-3 font-sans text-xs">光模組剛性需求大增。支撐 $390，阻力挑戰 $415。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold font-sans text-zinc-900 dark:text-zinc-100">ANET</td>
              <td class="px-4 py-3 text-right text-emerald-500 font-semibold">$174.56 (+2.85%)</td>
              <td class="px-4 py-3 font-sans">帶量逆市衝高，逼近歷史天價</td>
              <td class="px-4 py-3 text-center font-sans"><span class="px-2 py-0.5 rounded bg-emerald-100 dark:bg-emerald-950 text-emerald-800 dark:text-emerald-350 text-xs font-semibold">繼續強勢</span></td>
              <td class="px-4 py-3 font-sans text-xs">資料中心網絡需求強勁。支撐 $168，阻力挑戰 $180。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold font-sans text-zinc-900 dark:text-zinc-100">FLNC</td>
              <td class="px-4 py-3 text-right text-emerald-500 font-semibold">$24.77 (+9.50%)</td>
              <td class="px-4 py-3 font-sans">大漲突破箱體阻力，創三月來最大單日漲幅</td>
              <td class="px-4 py-3 text-center font-sans"><span class="px-2 py-0.5 rounded bg-emerald-100 dark:bg-emerald-950 text-emerald-800 dark:text-emerald-350 text-xs font-semibold">繼續強勢</span></td>
              <td class="px-4 py-3 font-sans text-xs">儲能重電大爆發直接受益者。支撐 $23.5，阻力挑戰 $26.0。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold font-sans text-zinc-900 dark:text-zinc-100">OKLO</td>
              <td class="px-4 py-3 text-right text-rose-500 font-semibold">$60.88 (-0.47%)</td>
              <td class="px-4 py-3 font-sans">高位窄幅整理，維持在 5MA 上方</td>
              <td class="px-4 py-3 text-center font-sans"><span class="px-2 py-0.5 rounded bg-zinc-100 dark:bg-zinc-800 text-zinc-800 dark:text-zinc-300 text-xs font-semibold">高位震盪</span></td>
              <td class="px-4 py-3 font-sans text-xs">受制於發債帶來的市場雜音，高位整理。支撐 $58。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold font-sans text-zinc-900 dark:text-zinc-100">VST</td>
              <td class="px-4 py-3 text-right text-emerald-500 font-semibold">$167.26 (+2.41%)</td>
              <td class="px-4 py-3 font-sans">沿 5MA 繼續走強，續創歷史最高收盤價</td>
              <td class="px-4 py-3 text-center font-sans"><span class="px-2 py-0.5 rounded bg-emerald-100 dark:bg-emerald-950 text-emerald-800 dark:text-emerald-350 text-xs font-semibold">繼續強勢</span></td>
              <td class="px-4 py-3 font-sans text-xs">資料中心供電題材剛性吸金。支撐 $160，阻力挑戰 $175。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold font-sans text-zinc-900 dark:text-zinc-100">CEG</td>
              <td class="px-4 py-3 text-right text-emerald-500 font-semibold">$276.07 (+0.73%)</td>
              <td class="px-4 py-3 font-sans">突破高位箱體後橫盤，創歷史收盤最高價</td>
              <td class="px-4 py-3 text-center font-sans"><span class="px-2 py-0.5 rounded bg-emerald-100 dark:bg-emerald-950 text-emerald-800 dark:text-emerald-350 text-xs font-semibold">繼續強勢</span></td>
              <td class="px-4 py-3 font-sans text-xs">微軟核電採購長期題材。支撐 $268，阻力挑戰 $285。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold font-sans text-zinc-900 dark:text-zinc-100">ETN</td>
              <td class="px-4 py-3 text-right text-zinc-500 font-semibold">$421.77 (0.00%)</td>
              <td class="px-4 py-3 font-sans">高位平盤十字星，沿 5MA 保持完美上行通道</td>
              <td class="px-4 py-3 text-center font-sans"><span class="px-2 py-0.5 rounded bg-zinc-100 dark:bg-zinc-800 text-zinc-800 dark:text-zinc-300 text-xs font-semibold">高位震盪</span></td>
              <td class="px-4 py-3 font-sans text-xs">重電基建出貨旺季。支撐 $412，壓力阻力看 $435。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold font-sans text-zinc-900 dark:text-zinc-100">VRT</td>
              <td class="px-4 py-3 text-right text-emerald-500 font-semibold">$344.23 (+4.21%)</td>
              <td class="px-4 py-3 font-sans">逆市爆出長紅 K 棒再創歷史新高，液冷需求火熱</td>
              <td class="px-4 py-3 text-center font-sans"><span class="px-2 py-0.5 rounded bg-emerald-100 dark:bg-emerald-950 text-emerald-800 dark:text-emerald-350 text-xs font-semibold">繼續強勢</span></td>
              <td class="px-4 py-3 font-sans text-xs">散熱龍頭，大行上調目標至 $380。支撐 $332，壓力 $360。</td>
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
        <p><strong>13.1 宏觀觀察：</strong>緊密監測 10 年期美債殖利率在 4.50% 的防守情況。關注美伊後續談判的最新進展，研判原油價格 (WTI) 能否在 $74 附近維持，這對大眾消費股（TSLA、AMZN）的物流回扣將是關鍵指引。</p>
        <p><strong>13.2 大盤觀察：</strong>觀察 S&P 500 指數在 7,450 點附近的 10MA 支撐力度。納斯達克指數在大型科技股高位獲利了結下，面臨回調壓力，觀察 26,000 點整數大關。羅素 2000 與費半指數強勢，關注能否延續跑贏大盤的態勢。</p>
        <p><strong>13.3 板塊與個股觀察：</strong>
          <ul class="list-disc pl-5 space-y-2 mt-2">
            <li><strong>半導體物理層 (INTC &amp; TSM):</strong> 英特爾因 18A-P 工藝大單與本土代工利多走高，台積電 ADR 亦創歷史新高，回踩 5MA 仍是良性配置點。</li>
            <li><strong>AI 基建 (VRT, VST, CEG):</strong> 散熱與電力供電作為本輪牛市中剛性需求極高的雙核心，在創高後宜逢回踩 10MA 進行分批布局，切忌高位盲目追高。</li>
            <li><strong>SpaceX (SPCX):</strong> 首日暴漲後大跌，200 億美元發債在短期帶來融資壓力，若回踩 $145 支撐可做左側小額試倉。</li>
            <li><strong>SaaS 應用 (PLTR, CRM):</strong> Palantir 放量跌 8% 顯示估值被利率壓制嚴重，避開左側接刀，等待 Accenture (ACN) 週三財報指引。</li>
          </ul>
        </p>
      </div>
    </section>

    <!-- 14. 風險提示 -->
    <section id="risks" class="mb-12 scroll-mt-6">
      <h2 class="text-2xl font-bold mb-4 flex items-center gap-2 border-b border-zinc-100 dark:border-zinc-800 pb-2">
        <span class="text-brand-500">14.</span> 風險提示
      </h2>
      
      <div class="overflow-x-auto border border-zinc-200 dark:border-zinc-800 rounded-xl">
        <table class="min-w-full divide-y divide-zinc-200 dark:divide-zinc-800 text-sm text-left">
          <thead class="bg-zinc-50 dark:bg-zinc-900">
            <tr>
              <th class="px-4 py-3 font-semibold text-zinc-600 dark:text-zinc-400 w-1/4">風險維度</th>
              <th class="px-4 py-3 font-semibold text-zinc-600 dark:text-zinc-400 w-1/4 text-center">風險評級</th>
              <th class="px-4 py-3 font-semibold text-zinc-600 dark:text-zinc-400">具體解讀</th>
            </tr>
          </thead>
          <tbody class="divide-y divide-zinc-200 dark:divide-zinc-850 font-sans text-zinc-700 dark:text-zinc-300">
            <tr>
              <td class="px-4 py-3 font-semibold">宏觀利率與政策風險</td>
              <td class="px-4 py-3 text-center"><span class="px-2 py-0.5 rounded bg-rose-100 dark:bg-rose-950 text-rose-800 dark:text-rose-350 text-xs font-semibold">高</span></td>
              <td class="px-4 py-3 text-zinc-500 dark:text-zinc-400 text-xs sm:text-sm leading-relaxed">CME 降息預期降溫，升息風險隱現。10Y 債息拉升至 4.507%，高倍數的 SaaS 軟體與 AI 應用（PLTR）融資成本壓力大，估值乘數被持續壓縮。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold">新股去槓桿風險</td>
              <td class="px-4 py-3 text-center"><span class="px-2 py-0.5 rounded bg-rose-100 dark:bg-rose-950 text-rose-800 dark:text-rose-350 text-xs font-semibold">中高</span></td>
              <td class="px-4 py-3 text-zinc-500 dark:text-zinc-400 text-xs sm:text-sm leading-relaxed">SpaceX (SPCX) 發債 200 億美元引發大規模做空與槓桿套現，加上 MSCI 評級不利。如果融資壓力擴散，將影響科技與太空新興板塊的流動性。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold">科技巨頭估值回吐</td>
              <td class="px-4 py-3 text-center"><span class="px-2 py-0.5 rounded bg-amber-100 dark:bg-amber-950 text-amber-800 dark:text-amber-350 text-xs font-semibold">中</span></td>
              <td class="px-4 py-3 text-zinc-500 dark:text-zinc-400 text-xs sm:text-sm leading-relaxed">Alphabet (GOOGL) 爆出 AI 人才流失利空，引發大廠核心技術流失的擔憂，科技巨頭自歷史高點進行均線修正，大盤指數承壓。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold">地緣談判波動風險</td>
              <td class="px-4 py-3 text-center"><span class="px-2 py-0.5 rounded bg-amber-100 dark:bg-amber-950 text-amber-800 dark:text-amber-350 text-xs font-semibold">中</span></td>
              <td class="px-4 py-3 text-zinc-500 dark:text-zinc-400 text-xs sm:text-sm leading-relaxed">美伊和平協定目前雖順利但未來細節談判依然有延遲風險，如果原油從 $74 急劇反彈，將重新引爆市場對輸入性通膨的焦慮。</td>
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
      <div class="space-y-4 text-sm sm:text-base leading-relaxed text-zinc-650 dark:text-zinc-400">
        <p><strong>今日市場結論：</strong>美股今日大盤走勢呈現強烈分化，主要因美伊局勢緩和帶動油價暴跌至 $74，在排除了商品通膨的同時，促使熱錢從高估值科技巨頭中移防，轉向防禦型藍籌。英特爾及台積電憑藉實質代工合作逆市走高，帶動費半指數創歷史新高。雖然 SpaceX 發債崩瀉壓制大盤，但寬度表現良好，屬於良性的防禦性大輪動。</p>
        <p><strong>當前市場階段：</strong><span class="text-emerald-500 font-semibold">大盤高位震盪 / 科技股高位整理 / 資金向醫療與小盤股防禦輪動。</span></p>
        <p><strong>操作傾向（中性表述）：</strong>避免盲目在左側抄底破位嚴重的 SaaS 板塊。多頭持倉可逐步轉移至有剛性用電需求的電力（VST、CEG）與散熱（VRT）等硬體基建，以及英特爾與台積電等有明確晶片代工紅利的龍頭，逢回踩 10MA 分批配置。</p>
        
        <div class="mt-4 p-4 rounded-xl border border-zinc-200 dark:border-zinc-800 bg-zinc-50/50 dark:bg-zinc-900/50">
          <h4 class="font-bold text-zinc-800 dark:text-zinc-200 mb-2">明日最值得關注的 5 個核心信號</h4>
          <ol class="list-decimal pl-5 space-y-2 text-xs sm:text-sm font-mono text-zinc-600 dark:text-zinc-400">
            <li><strong>10年期美債收益率：</strong>能否在 4.50% 的關口企穩或回落。</li>
            <li><strong>WTI 原油價格：</strong>原油大跌至 $74 後，能否止跌橫盤，地緣消息是否繼續釋放正面談判。</li>
            <li><strong>SpaceX (SPCX) 的企穩點：</strong>在暴跌 16% 後，是否能在 $150 整數關口獲得支撐。</li>
            <li><strong>Alphabet (GOOGL) 技術修復：</strong>黑 K 破位後，在 50MA ($342) 附近是否有買盤護盤。</li>
            <li><strong>埃森哲 (ACN) 週三財報預期計價：</strong>觀察週二諮詢版塊是否提前反應 AI 合約採購信心。</li>
          </ol>
        </div>
      </div>
    </section>

  </main>
</div>

<!-- Theme toggle & print script -->
<script>
  const toggleBtn = document.getElementById('theme-toggle');
  toggleBtn.addEventListener('click', () => {
    if (document.documentElement.classList.contains('dark')) {
      document.documentElement.classList.remove('dark');
      localStorage.theme = 'light';
    } else {
      document.documentElement.classList.add('dark');
      localStorage.theme = 'dark';
    }
    if (window.__mermaid) {
      window.location.reload();
    }
  });

  // Table Search and Filter Logic
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
  function sortSectors(colIndex) {
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
      labels: ['道瓊工業', '標普 500', '納指綜合', '納指 100', '羅素 2000', 'SOX 半導體', 'VIX 波動率'],
      datasets: [{
        label: '當日變動 (%)',
        data: [0.29, -0.37, -1.32, -1.32, 0.83, 0.70, 3.52],
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

# Save this HTML to reports/2026-06-22-us-stock-closing-daily-report.html inside /Users/wisdom/html-report-skill
target_dir = "/Users/wisdom/html-report-skill/reports"
os.makedirs(target_dir, exist_ok=True)
target_path = os.path.join(target_dir, "2026-06-22-us-stock-closing-daily-report.html")

with open(target_path, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"Report HTML file generated successfully at: {target_path}")
