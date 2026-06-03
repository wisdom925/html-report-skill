import os
import json

html_content = """<!doctype html>
<html lang="zh-TW" class="scroll-smooth">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <title>美股收盤日報｜2026-06-02</title>
  <meta name="description" content="2026年6月2日美股收盤日報：三大指數齊創盤中與收盤歷史新高！Marvell (MRVL) 狂飆 32.52% 與 HPE 暴漲 25.26% 領軍 AI 算力半導體，費半 (SOX) 暴漲 5.19%。Alphabet (GOOGL) 因宣布 800 億美元股權融資計劃大跌 4.06%。美國 4 月 JOLTs 職位空缺達 760 萬遠超預期，刺激美債利率大幅震盪，市場呈現極限分化的多頭輪動結構。">
  <meta property="og:title" content="美股收盤日報｜2026-06-02">
  <meta property="og:description" content="AI 算力與伺服器雙引擎爆發，費半狂飆 5.19%！谷歌融資 800 億跌 4%，JOLTs 職位空缺驚人超預期，大盤續創歷史新高。">
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

  <!-- KaTeX for Formulas -->
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
    details > summary { cursor: pointer; user-select: none; }
    details > summary::marker { content: "▸ "; }
    details[open] > summary::marker { content: "▾ "; }

    .toc a { display: block; padding: .25rem 0; opacity: .6; transition: opacity .15s, color .15s; }
    .toc a:hover, .toc a.active { opacity: 1; color: #0284c7; }
    .toc a.active { font-weight: 600; border-left: 2px solid #0284c7; padding-left: 0.5rem; margin-left: -0.5rem; }

    /* Tab styles using radio buttons & CSS siblings */
    .tabs { display: flex; flex-wrap: wrap; }
    .tabs > input[type="radio"] { display: none; }
    .tabs > label {
      cursor: pointer; padding: .5rem 1.25rem;
      border-bottom: 2px solid transparent;
      font-size: .9rem; font-weight: 500;
      color: #6b7280; transition: color .15s, border-color .15s;
    }
    .tabs > label:hover { color: #111; }
    .dark .tabs > label:hover { color: #f4f4f5; }
    .tabs > input:checked + label { border-color: #0284c7; color: #0284c7; font-weight: 600; }
    .tabs > .tab-panel { display: none; width: 100%; padding-top: 1rem; }
    .tabs > input:nth-of-type(1):checked ~ .tab-panel:nth-of-type(1),
    .tabs > input:nth-of-type(2):checked ~ .tab-panel:nth-of-type(2),
    .tabs > input:nth-of-type(3):checked ~ .tab-panel:nth-of-type(3),
    .tabs > input:nth-of-type(4):checked ~ .tab-panel:nth-of-type(4) { display: block; }

    /* Premium styled elements */
    .stat-card {
      background: linear-gradient(135deg, rgba(2,132,199,0.06) 0%, rgba(59,130,246,0.03) 100%);
      border: 1px solid rgba(2,132,199,0.15);
      border-radius: 1rem;
      padding: 1.5rem;
      transition: transform .2s, box-shadow .2s;
    }
    .stat-card:hover { transform: translateY(-2px); box-shadow: 0 8px 24px rgba(2,132,199,0.08); }

    .tag-strong { background-color: rgba(34, 197, 94, 0.15); color: #22c55e; border: 1px solid rgba(34, 197, 94, 0.25); }
    .tag-neutral { background-color: rgba(107, 114, 128, 0.15); color: #9ca3af; border: 1px solid rgba(107, 114, 128, 0.25); }
    .tag-warning { background-color: rgba(234, 179, 8, 0.15); color: #eab308; border: 1px solid rgba(234, 179, 8, 0.25); }
    .tag-danger { background-color: rgba(239, 68, 68, 0.15); color: #ef4444; border: 1px solid rgba(239, 68, 68, 0.25); }

    .grad-text {
      background: linear-gradient(135deg, #0284c7, #3b82f6, #6366f1);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      background-clip: text;
    }

    .chart-wrap { position: relative; height: 350px; }
  </style>
</head>

<body class="bg-white dark:bg-zinc-950 text-zinc-900 dark:text-zinc-100 font-sans antialiased">

<!-- Floating controls -->
<div class="fixed top-4 right-4 z-50 flex gap-2 no-print">
  <button id="theme-toggle" class="px-3 py-1.5 rounded-md border border-zinc-300 dark:border-zinc-700 bg-white/80 dark:bg-zinc-900/80 backdrop-blur text-sm hover:bg-zinc-100 dark:hover:bg-zinc-800 transition-colors">
    ☼ / ☾
  </button>
  <button onclick="window.print()" class="px-3 py-1.5 rounded-md border border-zinc-300 dark:border-zinc-700 bg-white/80 dark:bg-zinc-900/80 backdrop-blur text-sm hover:bg-zinc-100 dark:hover:bg-zinc-800 transition-colors">
    列印
  </button>
</div>

<div class="max-w-7xl mx-auto px-6 py-12 lg:grid lg:grid-cols-[240px_minmax(0,1fr)] lg:gap-12">

  <!-- Sticky TOC -->
  <nav class="toc lg:sticky lg:top-12 self-start text-sm mb-8 lg:mb-0 no-print border-r border-zinc-200 dark:border-zinc-800 pr-6">
    <div class="font-bold mb-4 text-zinc-400 dark:text-zinc-500 uppercase tracking-wider text-xs">報告目錄</div>
    <a href="#summary">0. 今日一句話總結</a>
    <a href="#indices">1. 大盤表現總覽</a>
    <a href="#timeline">2. 盤中走勢復盤</a>
    <a href="#macro">3. 宏觀環境分析</a>
    <a href="#sectors">4. S&P 500 板塊表現</a>
    <a href="#themes">5. 主題與風格表現</a>
    <a href="#breadth">6. 市場寬度與參與度</a>
    <a href="#technical">7. 技術面分析</a>
    <a href="#stocks">8. 重點個股新聞與異動</a>
    <a href="#earnings">9. 財報日曆與解讀</a>
    <a href="#institutional">10. 機構觀點與資金流</a>
    <a href="#rotation">11. 板塊輪動判斷</a>
    <a href="#watch-list">12. 重點關注股觀察</a>
    <a href="#plans">13. 明日交易計畫</a>
    <a href="#risks">14. 風險提示矩陣</a>
    <a href="#conclusion">15. 最終結論</a>
  </nav>

  <!-- Main Content -->
  <main class="min-w-0">

    <!-- Header -->
    <header class="mb-12 border-b border-zinc-200 dark:border-zinc-800 pb-8">
      <div class="flex items-center gap-3 mb-3">
        <span class="px-2.5 py-0.5 rounded text-xs font-semibold bg-brand-50 text-brand-600 dark:bg-brand-500/10 dark:text-brand-500 border border-brand-100 dark:border-brand-500/20">美股收盤日報</span>
        <span class="text-sm text-zinc-500"><time datetime="2026-06-02">2026-06-02 (星期二)</time></span>
      </div>
      <h1 class="text-4xl font-extrabold tracking-tight mb-4 grad-text">美股收盤日報｜2026-06-02</h1>
      <p class="text-xl text-zinc-600 dark:text-zinc-400">三大指數齊刷歷史收盤新高！Marvell (MRVL) 因輝達 CEO 黃仁勳點名肯定 AI 基建實力大漲 32.52%，Hewlett Packard Enterprise (HPE) 財報與展望爆表激增 25.26% 領跑算力，帶動費半狂飆 5.19%。Alphabet (GOOGL) 宣佈 800 億美元融資與稀釋股價重跌 4.06% 壓制納指。美國 4 月 JOLTs 職缺錄得 760 萬超預期，刺激美債利率日內巨幅波動，資金展現高位抱團與板塊極限分化結構。</p>
    </header>

    <!-- 0. 今日一句話總結 -->
    <section id="summary" class="mb-12 scroll-mt-6">
      <h2 class="text-2xl font-bold mb-4 flex items-center gap-2 border-b border-zinc-100 dark:border-zinc-800 pb-2">
        <span class="text-brand-500">0.</span> 今日一句話總結
      </h2>
      <div class="p-6 rounded-xl bg-zinc-50 dark:bg-zinc-900 border border-zinc-100 dark:border-zinc-800 space-y-4">
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
          <div class="space-y-2">
            <p class="text-sm font-semibold text-zinc-400">市場狀態判定</p>
            <p class="text-lg font-bold text-emerald-500 flex items-center gap-1">
              指數強勢創高、板塊極限分化；AI 算力基建受硬體與伺服器雙引擎引爆，但谷歌稀釋利空及利率波動使軟體與個別巨頭回吐。
            </p>
          </div>
          <div class="space-y-2">
            <p class="text-sm font-semibold text-zinc-400">核心驅動因素</p>
            <p class="text-sm text-zinc-600 dark:text-zinc-300">
              今日美股多頭主線在「AI 算力基建」中再次大放異彩，Marvell 獲輝達 CEO 認可暴漲 32.52%，HPE 財報大超預期暴拉 25.26%，引領半導體及費半 (SOX) 狂飆 5.19% 創下歷史最佳單日表現之一。然而，Alphabet (GOOGL) 宣佈 $800 億美元股權籌資（Berkshire 直接認購 $100 億）因稀釋預期大跌 4.06%，極大壓制了納指與通訊服務板塊。此外，4 月 JOLTs 職缺超預期升至 760 萬（預期 686 萬）引發對聯準會下半年的加息/鷹派顧慮，美債收益率與美元盤中暴跳，最終 10 年期美債利率收報 4.45% 震盪整理，WTI 原油受地緣停火預期落空上漲 1.46% 至 $93.76。
            </p>
          </div>
        </div>
        <hr class="border-zinc-200 dark:border-zinc-800">
        <ul class="list-disc pl-5 space-y-2 text-zinc-600 dark:text-zinc-300">
          <li><strong>大盤趨勢：</strong>三大指數均創歷史收盤新高。標普 500 指數微漲 0.13% 收報 7,609.78 點；道瓊斯工業指數受 HPE 與傳統電網/工業股提振上漲 0.45% 報 51,307.79 點；納斯達克綜合指數微漲 0.03% 報 27,093.90 點。小盤股 (Russell 2000) 補漲跑贏大盤，大漲 0.90%。</li>
          <li><strong>資金態度：</strong>資金強烈擁抱有實質業績（HPE）及高確定性地位（Marvell、博通）的 AI 硬體鏈，同時加倉工業、電網電能與地緣政治溢價的石油板塊。高估值的 SaaS 軟體與個別受到稀釋衝擊的科技巨頭出現失血回調。</li>
          <li><strong>市場寬度：</strong>市場寬度明顯改善，中小盤股 Russell 2000 開始補漲。NYSE 與 Nasdaq 交易所的上漲家數均多於下跌家數，但大盤指數受谷歌重跌拖累表現溫和，呈現「內部熱滾滾，指數小碎步」特徵。</li>
        </ul>
      </div>
    </section>

    <!-- 1. 大盤表現總覽 -->
    <section id="indices" class="mb-12 scroll-mt-6">
      <h2 class="text-2xl font-bold mb-4 flex items-center gap-2 border-b border-zinc-100 dark:border-zinc-800 pb-2">
        <span class="text-brand-500">1.</span> 大盤表現總覽
      </h2>
      <div class="grid grid-cols-1 lg:grid-cols-3 gap-6 mb-6">
        <div class="lg:col-span-2 overflow-x-auto border border-zinc-200 dark:border-zinc-800 rounded-xl">
          <table class="min-w-full divide-y divide-zinc-200 dark:divide-zinc-800 text-sm">
            <thead class="bg-zinc-50 dark:bg-zinc-900">
              <tr>
                <th class="px-4 py-3 text-left font-semibold text-zinc-600 dark:text-zinc-400">指數名稱</th>
                <th class="px-4 py-3 text-right font-semibold text-zinc-600 dark:text-zinc-400">收盤點位</th>
                <th class="px-4 py-3 text-right font-semibold text-zinc-600 dark:text-zinc-400">漲跌幅</th>
                <th class="px-4 py-3 text-right font-semibold text-zinc-600 dark:text-zinc-400">當日高低點</th>
                <th class="px-4 py-3 text-left font-semibold text-zinc-600 dark:text-zinc-400">技術狀態</th>
              </tr>
            </thead>
            <tbody class="divide-y divide-zinc-200 dark:divide-zinc-800 font-mono text-zinc-700 dark:text-zinc-300">
              <tr>
                <td class="px-4 py-3 font-semibold font-sans text-zinc-900 dark:text-zinc-100">Dow Jones</td>
                <td class="px-4 py-3 text-right">51,307.79</td>
                <td class="px-4 py-3 text-right text-emerald-500 font-semibold">+0.45%</td>
                <td class="px-4 py-3 text-right">50,840.98 - 51,356.91</td>
                <td class="px-4 py-3 text-left font-sans text-xs">歷史收盤新高！重回 51,000 大關上方，受傳統及工業板塊支撐。</td>
              </tr>
              <tr>
                <td class="px-4 py-3 font-semibold font-sans text-zinc-900 dark:text-zinc-100">S&P 500</td>
                <td class="px-4 py-3 text-right">7,609.78</td>
                <td class="px-4 py-3 text-right text-emerald-500 font-semibold">+0.13%</td>
                <td class="px-4 py-3 text-right">7,582.99 - 7,620.90</td>
                <td class="px-4 py-3 text-left font-sans text-xs text-emerald-500">歷史收盤新高！站在所有主要均線之上，多頭結構維持完美。</td>
              </tr>
              <tr>
                <td class="px-4 py-3 font-semibold font-sans text-zinc-900 dark:text-zinc-100">Nasdaq Composite</td>
                <td class="px-4 py-3 text-right">27,093.90</td>
                <td class="px-4 py-3 text-right text-emerald-500 font-semibold">+0.03%</td>
                <td class="px-4 py-3 text-right">26,932.90 - 27,171.24</td>
                <td class="px-4 py-3 text-left font-sans text-xs text-emerald-500">歷史收盤新高！受谷歌重跌壓制，盤中創下歷史新高 27,171。</td>
              </tr>
              <tr>
                <td class="px-4 py-3 font-semibold font-sans text-zinc-900 dark:text-zinc-100">Nasdaq 100 / QQQ</td>
                <td class="px-4 py-3 text-right">30,660.60</td>
                <td class="px-4 py-3 text-right text-emerald-500 font-semibold">+0.48%</td>
                <td class="px-4 py-3 text-right">30,318.50 - 30,710.25</td>
                <td class="px-4 py-3 text-left font-sans text-xs text-emerald-500">歷史收盤新高！半導體晶片大漲帶動，走勢略優於綜合指數。</td>
              </tr>
              <tr>
                <td class="px-4 py-3 font-semibold font-sans text-zinc-900 dark:text-zinc-100">Russell 2000 / IWM</td>
                <td class="px-4 py-3 text-right">2,931.96</td>
                <td class="px-4 py-3 text-right text-emerald-500 font-semibold">+0.90%</td>
                <td class="px-4 py-3 text-right">2,900.70 - 2,934.95</td>
                <td class="px-4 py-3 text-left font-sans text-xs text-emerald-500">強勢跑贏！市場風險偏好上升，中小盤股迎來爆發補漲。</td>
              </tr>
              <tr>
                <td class="px-4 py-3 font-semibold font-sans text-zinc-900 dark:text-zinc-100">SOX 半導體指數</td>
                <td class="px-4 py-3 text-right">13,638.28</td>
                <td class="px-4 py-3 text-right text-emerald-500 font-semibold">+5.19%</td>
                <td class="px-4 py-3 text-right">13,202.18 - 13,733.72</td>
                <td class="px-4 py-3 text-left font-sans text-xs text-emerald-500">狂飆創歷史收盤新高！Marvell 及博通引領，暴漲長陽確立極強動能。</td>
              </tr>
              <tr>
                <td class="px-4 py-3 font-semibold font-sans text-zinc-900 dark:text-zinc-100">VIX 恐慌指數</td>
                <td class="px-4 py-3 text-right">16.15</td>
                <td class="px-4 py-3 text-right text-emerald-500 font-semibold">+1.00%</td>
                <td class="px-4 py-3 text-right">16.10 - 16.28</td>
                <td class="px-4 py-3 text-left font-sans text-xs">低位微升，仍受制於 17 關口，市場定價部分 JOLTs 與地緣風險。</td>
              </tr>
            </tbody>
          </table>
        </div>
        <div class="stat-card flex flex-col justify-between">
          <div>
            <h4 class="font-bold text-zinc-800 dark:text-zinc-200">當日指數回報動態對比</h4>
            <p class="text-xs text-zinc-400 mt-1">反映各主要指數的單日相對強弱程度，半導體指數與羅素2000小盤股明顯跑贏。</p>
          </div>
          <div class="chart-wrap mt-4">
            <canvas id="returnsChart"></canvas>
          </div>
        </div>
      </div>
    </section>

    <!-- 2. 盤中走勢復盤 -->
    <section id="timeline" class="mb-12 scroll-mt-6">
      <h2 class="text-2xl font-bold mb-6 flex items-center gap-2 border-b border-zinc-100 dark:border-zinc-800 pb-2">
        <span class="text-brand-500">2.</span> 盤中走勢復盤
      </h2>

      <div class="mb-8 p-4 bg-zinc-50 dark:bg-zinc-900 rounded-xl border border-zinc-100 dark:border-zinc-800">
        <p class="text-sm text-zinc-500 mb-4 font-bold text-center">資金情緒與市場事件流向圖：</p>
        <div class="mermaid text-center" id="rotation-flow">
          graph LR
            JOLTs[JOLTs 職缺達 760 萬] -->|遠超預期 686 萬| Yields[美債 10Y 利率盤中大跳]
            NvidiaHuang[黃仁勳 Computex 演說點名] -->|激勵 ASIC 算力大增| MRVL[Marvell 狂噴 32.52%]
            HPE_Earnings[HPE Q2 財報大幅超預期] -->|訂單與指引超常發揮| HPE[HPE 暴漲 25.26%]
            GoogleRaise[谷歌宣布 $800 億股權融資] -->|市場擔憂股本稀釋| GOOGL[Alphabet 重挫 4.06%]
            Yields & GOOGL -->|指數壓制但資金抱團晶片| Markets[標普/納指/道指齊收盤創高]
        </div>
      </div>

      <div class="relative border-l border-zinc-200 dark:border-zinc-800 ml-4 space-y-6">
        <div class="relative pl-6">
          <div class="absolute -left-1.5 top-1.5 w-3 h-3 rounded-full bg-brand-500"></div>
          <time class="text-xs text-zinc-400 font-mono">10:00 AM</time>
          <h4 class="font-bold text-zinc-900 dark:text-zinc-100">4 月 JOLTs 數據爆表，美債利率劇震</h4>
          <p class="text-sm text-zinc-600 dark:text-zinc-400 mt-1">
            美國勞工統計局公佈 4 月 JOLTs 職位空缺數急增至 760.0 萬（預期 686.0 萬），創下近兩年最大單月增幅。就業市場極度強勁引發市場對聯準會 6 月維持利率不變及年內推遲降息的擔憂，10年期美債利率盤中直逼 4.52%，美股盤初遭遇部分債券利率攀升帶來的估值拋售潮。
          </p>
        </div>
        <div class="relative pl-6">
          <div class="absolute -left-1.5 top-1.5 w-3 h-3 rounded-full bg-brand-500"></div>
          <time class="text-xs text-zinc-400 font-mono">11:30 AM</time>
          <h4 class="font-bold text-zinc-900 dark:text-zinc-100">Alphabet 爆股權籌資利空，巨頭板塊承壓</h4>
          <p class="text-sm text-zinc-600 dark:text-zinc-400 mt-1">
            Alphabet 宣佈 $800 億美元的龐大股權融資計劃，包含向波克夏私募配售 $100 億及未來 ATM 發行。儘管目的是投資 AI 基礎設施，但市場對其背離回購策略、實施龐大稀釋股本的行動作出負面反應，谷歌股價大挫逾 4%，拖累微軟、特斯拉等巨頭盤中一度回軟。
          </p>
        </div>
        <div class="relative pl-6">
          <div class="absolute -left-1.5 top-1.5 w-3 h-3 rounded-full bg-brand-500"></div>
          <time class="text-xs text-zinc-400 font-mono">02:00 PM</time>
          <h4 class="font-bold text-zinc-900 dark:text-zinc-100">HPE 與 Marvell 掀起算力巨浪，費半強勢狂飆</h4>
          <p class="text-sm text-zinc-600 dark:text-zinc-400 mt-1">
            午盤後，資金以極端熱情瘋狂抱團半導體硬體板塊。HPE 因為 AI 訂單積壓大減、營收猛增 40% 爆漲 25.26%，Marvell 更在黃仁勳台北 Computex 年會發言中獲讚其光通訊與 AI ASIC 互聯實力狂飆 32.52%，博通、AMD 也集體被資金強力掃貨，費城半導體指數大漲 5.19%，抵消谷歌下跌壓力。
          </p>
        </div>
        <div class="relative pl-6">
          <div class="absolute -left-1.5 top-1.5 w-3 h-3 rounded-full bg-brand-500"></div>
          <time class="text-xs text-zinc-400 font-mono">04:00 PM</time>
          <h4 class="font-bold text-zinc-900 dark:text-zinc-100">尾盤多頭部隊完成包抄，三大指數同步創高收盤</h4>
          <p class="text-sm text-zinc-600 dark:text-zinc-400 mt-1">
            尾盤十年期美債利率從日內高點回落至 4.45%，舒緩了高利率帶來的緊張情緒。中小盤 Russell 2000 出現明顯的補漲大漲 0.90%，科技巨頭微軟與蘋果亦走高護航。三大指數尾盤悉數拉升，標普 500、道瓊斯與納斯達克在最後十分鐘再度創下收盤歷史最高點。
          </p>
        </div>
      </div>
    </section>

    <!-- 3. 宏觀環境 -->
    <section id="macro" class="mb-12 scroll-mt-6">
      <h2 class="text-2xl font-bold mb-4 flex items-center gap-2 border-b border-zinc-100 dark:border-zinc-800 pb-2">
        <span class="text-brand-500">3.</span> 宏觀環境分析
      </h2>

      <div class="tabs">
        <input type="radio" name="macro-tabs" id="tab-yields" checked>
        <label for="tab-yields">3.1 美債收益率</label>

        <input type="radio" name="macro-tabs" id="tab-fed">
        <label for="tab-fed">3.2 Fed 降息預期</label>

        <input type="radio" name="macro-tabs" id="tab-commodities">
        <label for="tab-commodities">3.3 大宗商品與外匯</label>

        <input type="radio" name="macro-tabs" id="tab-data">
        <label for="tab-data">3.4 重要經濟數據</label>

        <!-- Panel 1: Yields -->
        <div class="tab-panel">
          <div class="p-4 bg-zinc-50 dark:bg-zinc-900 border border-zinc-200 dark:border-zinc-800 rounded-xl space-y-3">
            <h4 class="font-bold text-zinc-800 dark:text-zinc-200">國債收益率日變化：</h4>
            <div class="grid grid-cols-3 gap-4 text-center">
              <div class="p-3 bg-white dark:bg-zinc-800 rounded-lg border border-zinc-100 dark:border-zinc-700">
                <span class="text-xs text-zinc-400">2年期美債收益率</span>
                <p class="text-lg font-bold font-mono mt-1">4.055%</p>
                <span class="text-xs text-emerald-500">-2.5 Bps</span>
              </div>
              <div class="p-3 bg-white dark:bg-zinc-800 rounded-lg border border-zinc-100 dark:border-zinc-700">
                <span class="text-xs text-zinc-400">10年期美債收益率</span>
                <p class="text-lg font-bold font-mono mt-1">4.450%</p>
                <span class="text-xs text-emerald-500">-2.5 Bps</span>
              </div>
              <div class="p-3 bg-white dark:bg-zinc-800 rounded-lg border border-zinc-100 dark:border-zinc-700">
                <span class="text-xs text-zinc-400">30年期美債收益率</span>
                <p class="text-lg font-bold font-mono mt-1">4.600%</p>
                <span class="text-xs text-emerald-500">-1.8 Bps</span>
              </div>
            </div>
            <p class="text-xs text-zinc-500 leading-relaxed pt-2 border-t border-zinc-200 dark:border-zinc-850">
              <strong>收益率曲線解讀：</strong>儘管 JOLTs 職缺創高引發盤中收益率拉升（10Y 一度觸及 4.52%），但尾盤避險資金購入長端國債，使收益率同步回踩前一交易日收盤位置。2Y-10Y 曲線倒掛維持在 -40Bps 左右，顯示市場在就業韌性下定價了長期的偏緊融資環境，但並未引發系統性通膨崩潰。
            </p>
          </div>
        </div>

        <!-- Panel 2: Fed -->
        <div class="tab-panel">
          <div class="p-4 bg-zinc-50 dark:bg-zinc-900 border border-zinc-200 dark:border-zinc-800 rounded-xl space-y-3">
            <h4 class="font-bold text-zinc-800 dark:text-zinc-200">CME FedWatch 當前降息預估：</h4>
            <ul class="list-disc pl-5 text-sm space-y-2 text-zinc-600 dark:text-zinc-300">
              <li><strong>6 月 17 日 FOMC 議息預期：</strong>維持現行利率不變（5.25% - 5.50%）的機率高達 **98.2%**，降息 25Bps 的機率僅存 **1.8%**。</li>
              <li><strong>年內降息次數預期：</strong>就業數據超預期迫使降息定價繼續向後推遲。市場主流預期（約 54% 機率）年內僅降息 1 次或不降息，最快在 11 月或 12 月大選後才具備寬鬆條件。</li>
              <li><strong>Fed 官員講話：</strong>數位地區聯儲主席（包括明尼阿波利斯卡什卡里）在 JOLTs 發佈後表示，如果勞動力市場持續緊張且通膨黏性強，年內不排除需要再次加息或拉長利率在高位的停留時長（Higher for longer）。</li>
            </ul>
          </div>
        </div>

        <!-- Panel 3: Commodities -->
        <div class="tab-panel">
          <div class="p-4 bg-zinc-50 dark:bg-zinc-900 border border-zinc-200 dark:border-zinc-800 rounded-xl space-y-3">
            <h4 class="font-bold text-zinc-800 dark:text-zinc-200">大宗商品與加密貨幣收盤行情：</h4>
            <div class="grid grid-cols-2 md:grid-cols-4 gap-4 text-center">
              <div class="p-3 bg-white dark:bg-zinc-800 rounded-lg border border-zinc-100 dark:border-zinc-700">
                <span class="text-xs text-zinc-400">美元指數 (DXY)</span>
                <p class="text-sm font-bold font-mono mt-1">99.12</p>
                <span class="text-xs text-rose-500">+0.06%</span>
              </div>
              <div class="p-3 bg-white dark:bg-zinc-800 rounded-lg border border-zinc-100 dark:border-zinc-700">
                <span class="text-xs text-zinc-400">WTI 原油 (紐約)</span>
                <p class="text-sm font-bold font-mono mt-1">$93.76</p>
                <span class="text-xs text-rose-500">+1.46%</span>
              </div>
              <div class="p-3 bg-white dark:bg-zinc-800 rounded-lg border border-zinc-100 dark:border-zinc-700">
                <span class="text-xs text-zinc-400">黃金現貨 (Gold)</span>
                <p class="text-sm font-bold font-mono mt-1">$4,498.50</p>
                <span class="text-xs text-rose-500">+0.12%</span>
              </div>
              <div class="p-3 bg-white dark:bg-zinc-800 rounded-lg border border-zinc-100 dark:border-zinc-700">
                <span class="text-xs text-zinc-400">比特幣 (BTC)</span>
                <p class="text-sm font-bold font-mono mt-1">$68,950</p>
                <span class="text-xs text-rose-500">-1.36%</span>
              </div>
            </div>
            <p class="text-xs text-zinc-500 leading-relaxed pt-2 border-t border-zinc-200 dark:border-zinc-850">
              <strong>資金流向分析：</strong>美元指數維持在 99 關口上方偏強整理。油價主要受伊朗霍爾木茲海峽地緣衝突降溫談判破裂刺激，WTI 回彈 1.46% 企穩 $93。比特幣與以太坊（Eth 報 $1,955，跌 1.8%）受高息顧慮及 ETF 短期流出打擊呈現 Risk-off 震盪整理。
            </p>
          </div>
        </div>

        <!-- Panel 4: Data -->
        <div class="tab-panel">
          <div class="p-4 bg-zinc-50 dark:bg-zinc-900 border border-zinc-200 dark:border-zinc-800 rounded-xl space-y-3">
            <h4 class="font-bold text-zinc-800 dark:text-zinc-200">今日發佈經濟指標：</h4>
            <div class="overflow-x-auto">
              <table class="min-w-full text-xs divide-y divide-zinc-250 dark:divide-zinc-800">
                <thead>
                  <tr class="text-zinc-500 dark:text-zinc-400 text-left">
                    <th class="py-2">指標名稱</th>
                    <th class="py-2 text-center">公佈時間</th>
                    <th class="py-2 text-right">實際值</th>
                    <th class="py-2 text-right">預期值</th>
                    <th class="py-2 text-right">前值</th>
                    <th class="py-2">市場解讀</th>
                  </tr>
                </thead>
                <tbody class="divide-y divide-zinc-200 dark:divide-zinc-850 text-zinc-700 dark:text-zinc-300">
                  <tr>
                    <td class="py-2.5 font-semibold">4月 JOLTs 職位空缺 (萬人)</td>
                    <td class="py-2.5 text-center">10:00 AM</td>
                    <td class="py-2.5 text-right font-mono font-bold text-rose-500">760.0</td>
                    <td class="py-2.5 text-right font-mono">686.0</td>
                    <td class="py-2.5 text-right font-mono">726.0 (修正)</td>
                    <td class="py-2.5">大幅偏強。勞工需求意外反彈，失業率與職缺比拉大，支持聯準會延後降息。</td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- 4. 板塊表現 -->
    <section id="sectors" class="mb-12 scroll-mt-6">
      <div class="flex flex-col md:flex-row md:items-center justify-between gap-4 mb-4 border-b border-zinc-100 dark:border-zinc-800 pb-2">
        <h2 class="text-2xl font-bold flex items-center gap-2">
          <span class="text-brand-500">4.</span> S&P 500 板塊表現
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
              <th onclick="sortSectors(3)" class="cursor-pointer hover:bg-zinc-100 dark:hover:bg-zinc-800 px-4 py-3 text-right font-semibold text-zinc-600 dark:text-zinc-400">當日漲跌幅 ▲▼</th>
              <th onclick="sortSectors(4)" class="cursor-pointer hover:bg-zinc-100 dark:hover:bg-zinc-800 px-4 py-3 text-right font-semibold text-zinc-600 dark:text-zinc-400">近5日 ▲▼</th>
              <th onclick="sortSectors(5)" class="cursor-pointer hover:bg-zinc-100 dark:hover:bg-zinc-800 px-4 py-3 text-right font-semibold text-zinc-600 dark:text-zinc-400">近1月 ▲▼</th>
              <th class="px-4 py-3 text-left font-semibold text-zinc-600 dark:text-zinc-400">主要驅動</th>
            </tr>
          </thead>
          <tbody class="divide-y divide-zinc-200 dark:divide-zinc-800">
            <tr>
              <td class="px-4 py-3 font-medium">1</td>
              <td class="px-4 py-3 font-medium">能源 (Energy)</td>
              <td class="px-4 py-3 font-mono">XLE</td>
              <td class="px-4 py-3 text-right font-mono text-emerald-500 font-semibold" data-val="1.15">+1.15%</td>
              <td class="px-4 py-3 text-right font-mono" data-val="4.25">+4.25%</td>
              <td class="px-4 py-3 text-right font-mono" data-val="-0.95">-0.95%</td>
              <td class="px-4 py-3 text-xs">伊朗局勢中談判破裂令 WTI 站穩 $93.76，能源龍頭 ExxonMobil、Chevron 均有買盤湧入。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-medium">2</td>
              <td class="px-4 py-3 font-medium">工業 (Industrials)</td>
              <td class="px-4 py-3 font-mono">XLI</td>
              <td class="px-4 py-3 text-right font-mono text-emerald-500 font-semibold" data-val="0.34">+0.34%</td>
              <td class="px-4 py-3 text-right font-mono" data-val="0.80">+0.80%</td>
              <td class="px-4 py-3 text-right font-mono" data-val="2.10">+2.10%</td>
              <td class="px-4 py-3 text-xs">強勁的就業與實體需求利好傳統基建，Eaton 電網與變壓器板塊受惠於電網改造需求狂拉。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-medium">3</td>
              <td class="px-4 py-3 font-medium">公用事業 (Utilities)</td>
              <td class="px-4 py-3 font-mono">XLU</td>
              <td class="px-4 py-3 text-right font-mono text-emerald-500 font-semibold" data-val="0.16">+0.16%</td>
              <td class="px-4 py-3 text-right font-mono" data-val="0.94">+0.94%</td>
              <td class="px-4 py-3 text-right font-mono" data-val="-1.40">-1.40%</td>
              <td class="px-4 py-3 text-xs">美債十年期收益率尾盤自高位回踩，AI 資料中心用電需求依舊為長期多頭提供基本盤。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-medium">4</td>
              <td class="px-4 py-3 font-medium">原材料 (Materials)</td>
              <td class="px-4 py-3 font-mono">XLB</td>
              <td class="px-4 py-3 text-right font-mono text-emerald-500 font-semibold" data-val="0.07">+0.07%</td>
              <td class="px-4 py-3 text-right font-mono" data-val="0.37">+0.37%</td>
              <td class="px-4 py-3 text-right font-mono" data-val="-1.13">-1.13%</td>
              <td class="px-4 py-3 text-xs">黃金現貨維持在 $4,500 高位震盪，金屬與礦業公司平穩洗籌。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-medium">5</td>
              <td class="px-4 py-3 font-mono">金融 (Financials)</td>
              <td class="px-4 py-3 font-mono">XLF</td>
              <td class="px-4 py-3 text-right font-mono text-emerald-500 font-semibold" data-val="0.06">+0.06%</td>
              <td class="px-4 py-3 text-right font-mono" data-val="0.16">+0.16%</td>
              <td class="px-4 py-3 text-right font-mono" data-val="0.86">+0.86%</td>
              <td class="px-4 py-3 text-xs">職缺超預期有利銀行高淨利差利好，但波克夏加碼谷歌並未大量流向銀行板塊。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-medium">6</td>
              <td class="px-4 py-3 font-medium">房地產 (Real Estate)</td>
              <td class="px-4 py-3 font-mono">XLRE</td>
              <td class="px-4 py-3 text-right font-mono text-rose-500 font-semibold" data-val="-0.05">-0.05%</td>
              <td class="px-4 py-3 text-right font-mono" data-val="-0.85">-0.85%</td>
              <td class="px-4 py-3 text-right font-mono" data-val="-2.30">-2.30%</td>
              <td class="px-4 py-3 text-xs">迎來多檔權重股的除權息日 (Ex-Dividend)，高融資利率繼續壓抑估值，微幅回檔。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-medium">7</td>
              <td class="px-4 py-3 font-medium">資訊科技 (Information Technology)</td>
              <td class="px-4 py-3 font-mono">XLK</td>
              <td class="px-4 py-3 text-right font-mono text-rose-500 font-semibold" data-val="-0.13">-0.13%</td>
              <td class="px-4 py-3 text-right font-mono" data-val="0.67">+0.67%</td>
              <td class="px-4 py-3 text-right font-mono" data-val="18.37">+18.37%</td>
              <td class="px-4 py-3 text-xs">費半狂飆但 SaaS 軟體與部分非晶片科技股回調（如 Salesforce 等），使板塊呈現分化微跌。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-medium">8</td>
              <td class="px-4 py-3 font-medium">醫療保健 (Health Care)</td>
              <td class="px-4 py-3 font-mono">XLV</td>
              <td class="px-4 py-3 text-right font-mono text-rose-500 font-semibold" data-val="-0.26">-0.26%</td>
              <td class="px-4 py-3 text-right font-mono" data-val="0.91">+0.91%</td>
              <td class="px-4 py-3 text-right font-mono" data-val="1.91">+1.91%</td>
              <td class="px-4 py-3 text-xs">防守型醫藥板塊在多頭風險偏好回暖、中小盤吸金的情況下，面臨小幅套現流出。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-medium">9</td>
              <td class="px-4 py-3 font-medium">日常消費品 (Consumer Staples)</td>
              <td class="px-4 py-3 font-mono">XLP</td>
              <td class="px-4 py-3 text-right font-mono text-rose-500 font-semibold" data-val="-0.38">-0.38%</td>
              <td class="px-4 py-3 text-right font-mono" data-val="-0.18">-0.18%</td>
              <td class="px-4 py-3 text-right font-mono" data-val="1.12">+1.12%</td>
              <td class="px-4 py-3 text-xs">市場對年內降息次數降溫，重債的大型消費日用品巨頭面臨防禦撤資。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-medium">10</td>
              <td class="px-4 py-3 font-medium">非日常消費品 (Consumer Discretionary)</td>
              <td class="px-4 py-3 font-mono">XLY</td>
              <td class="px-4 py-3 text-right font-mono text-rose-500 font-semibold" data-val="-0.50">-0.50%</td>
              <td class="px-4 py-3 text-right font-mono" data-val="-1.73">-1.73%</td>
              <td class="px-4 py-3 text-right font-mono" data-val="3.04">+3.04%</td>
              <td class="px-4 py-3 text-xs">特斯拉 (TSLA) 因需求憂慮小幅回檔，加上消費性零售股走勢偏軟拖累。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-medium">11</td>
              <td class="px-4 py-3 font-medium">通訊服務 (Communication Services)</td>
              <td class="px-4 py-3 font-mono">XLC</td>
              <td class="px-4 py-3 text-right font-mono text-rose-500 font-semibold" data-val="-0.67">-0.67%</td>
              <td class="px-4 py-3 text-right font-mono" data-val="-0.25">-0.25%</td>
              <td class="px-4 py-3 text-right font-mono" data-val="14.43">+14.43%</td>
              <td class="px-4 py-3 text-xs">受 Alphabet (GOOGL -4.06%) 宣佈 $800 億股權私募與公開融資计划拖累。</td>
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
      <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
        <div class="p-5 rounded-xl border border-zinc-200 dark:border-zinc-800 bg-white dark:bg-zinc-900">
          <span class="text-xs font-semibold text-zinc-400">最強風格</span>
          <h3 class="text-lg font-bold text-emerald-500 mt-1">AI 互聯與伺服器 (ASIC)</h3>
          <p class="text-sm text-zinc-500 mt-2 leading-relaxed">
            Nvidia CEO 年會背書令光晶片與 ASIC 連接巨頭 Marvell (MRVL) 狂飆 32.52%，搭配 HPE (+25.26%) 與博通 (+6.46%) 的極限買盤，將 AI 硬體賽道熱度推向沸點，SMH/SOXX 創最大單日漲幅。
          </p>
        </div>
        <div class="p-5 rounded-xl border border-zinc-200 dark:border-zinc-800 bg-white dark:bg-zinc-900">
          <span class="text-xs font-semibold text-zinc-400">最弱風格</span>
          <h3 class="text-lg font-bold text-rose-500 mt-1">SaaS 軟體應用與高值成長</h3>
          <p class="text-sm text-zinc-500 mt-2 leading-relaxed">
            ServiceNow (NOW) 因籌碼高位獲利了結大挫 7.17%，雪花 (SNOW) 因 Summit 26 後新產品缺乏即刻利潤催化重跌 8.00%，高估值軟體 SaaS 面臨利率波動之下的流動性撤換。
          </p>
        </div>
        <div class="p-5 rounded-xl border border-zinc-200 dark:border-zinc-800 bg-white dark:bg-zinc-900">
          <span class="text-xs font-semibold text-zinc-400">輪動特徵</span>
          <h3 class="text-lg font-bold text-amber-500 mt-1">小盤補漲與 AI 基建重構</h3>
          <p class="text-sm text-zinc-500 mt-2 leading-relaxed">
            Russell 2000 小盤股 (+0.90%) 與等權標普 (RSP +0.42%) 出現罕見的同步補漲，資金在巨頭被谷歌股權融資拖累時，分流至傳統電網變壓器 (ETN) 與電力基建。
          </p>
        </div>
      </div>
    </section>

    <!-- 6. 市場寬度與參與度 -->
    <section id="breadth" class="mb-12 scroll-mt-6">
      <h2 class="text-2xl font-bold mb-4 flex items-center gap-2 border-b border-zinc-100 dark:border-zinc-800 pb-2">
        <span class="text-brand-500">6.</span> 市場寬度與參與度
      </h2>
      <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
        <div class="p-5 rounded-xl bg-zinc-50 dark:bg-zinc-900 border border-zinc-100 dark:border-zinc-800">
          <h4 class="font-bold text-zinc-800 dark:text-zinc-200">6.1 均線參與度</h4>
          <p class="text-sm text-zinc-600 dark:text-zinc-400 mt-2 leading-relaxed">
            S&P 500 高於 50MA 比例為 <strong>64.8%</strong> (前值 60.2%)；Nasdaq 100 比例為 <strong>59.5%</strong> (前值 56.4%)。這表明大盤在指數創歷史新高的過程中，底層個股的均線健康度有所修復，並非僅靠單一龍頭護盤。
          </p>
        </div>
        <div class="p-5 rounded-xl bg-zinc-50 dark:bg-zinc-900 border border-zinc-100 dark:border-zinc-800">
          <h4 class="font-bold text-zinc-800 dark:text-zinc-200">6.2 漲跌家數與新高</h4>
          <p class="text-sm text-zinc-600 dark:text-zinc-400 mt-2 leading-relaxed">
            <strong>NYSE 交易所：</strong>上漲 1,624 家，下跌 1,182 家。新高 102 家，新低 18 家。<br>
            <strong>Nasdaq 交易所：</strong>上漲 2,154 家，下跌 1,890 家。新高 134 家，新低 45 家。<br>
            上漲比率擴大至 58% 左右，寬度逐步從前期極端抱團改善。
          </p>
        </div>
        <div class="p-5 rounded-xl bg-zinc-50 dark:bg-zinc-900 border border-zinc-100 dark:border-zinc-800">
          <h4 class="font-bold text-zinc-800 dark:text-zinc-200">6.3 內部指標與量能</h4>
          <p class="text-sm text-zinc-600 dark:text-zinc-400 mt-2 leading-relaxed">
            <strong>Put/Call 比例：</strong>0.71 (前值 0.76)，顯示市場高位投機性看漲情緒有所升溫。量能較昨日放大 12%，主要受 Marvell 及 HPE 的天量爆發換手推動，反映機構高位調倉。
          </p>
        </div>
      </div>
    </section>

    <!-- 7. 技術面分析 -->
    <section id="technical" class="mb-12 scroll-mt-6">
      <h2 class="text-2xl font-bold mb-4 flex items-center gap-2 border-b border-zinc-100 dark:border-zinc-800 pb-2">
        <span class="text-brand-500">7.</span> 技術面分析
      </h2>
      <div class="overflow-x-auto border border-zinc-200 dark:border-zinc-800 rounded-xl">
        <table class="min-w-full divide-y divide-zinc-200 dark:divide-zinc-800 text-sm">
          <thead class="bg-zinc-50 dark:bg-zinc-900">
            <tr>
              <th class="px-4 py-3 text-left font-semibold text-zinc-600 dark:text-zinc-400">ETF代號</th>
              <th class="px-4 py-3 text-right font-semibold text-zinc-600 dark:text-zinc-400">最新收盤</th>
              <th class="px-4 py-3 text-right font-semibold text-zinc-600 dark:text-zinc-400">20 MA</th>
              <th class="px-4 py-3 text-right font-semibold text-zinc-600 dark:text-zinc-400">50 MA</th>
              <th class="px-4 py-3 text-right font-semibold text-zinc-600 dark:text-zinc-400">200 MA</th>
              <th class="px-4 py-3 text-center font-semibold text-zinc-600 dark:text-zinc-400">RSI (14)</th>
              <th class="px-4 py-3 text-left font-semibold text-zinc-600 dark:text-zinc-400">關鍵支撐 / 壓力</th>
              <th class="px-4 py-3 text-left font-semibold text-zinc-600 dark:text-zinc-400">短線趨勢判定</th>
            </tr>
          </thead>
          <tbody class="divide-y divide-zinc-200 dark:divide-zinc-800 font-mono text-zinc-700 dark:text-zinc-300">
            <tr>
              <td class="px-4 py-3 font-semibold font-sans text-zinc-900 dark:text-zinc-100">SPY (S&P 500)</td>
              <td class="px-4 py-3 text-right">$760.98</td>
              <td class="px-4 py-3 text-right">$744.50</td>
              <td class="px-4 py-3 text-right">$729.80</td>
              <td class="px-4 py-3 text-right">$683.50</td>
              <td class="px-4 py-3 text-center">68.9</td>
              <td class="px-4 py-3 font-sans text-xs text-left">$750 / $765</td>
              <td class="px-4 py-3 font-sans text-xs text-emerald-500 font-semibold text-left">多頭強勢突破，逼近超買區</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold font-sans text-zinc-900 dark:text-zinc-100">QQQ (Nasdaq 100)</td>
              <td class="px-4 py-3 text-right">$746.18</td>
              <td class="px-4 py-3 text-right">$735.00</td>
              <td class="px-4 py-3 text-right">$721.50</td>
              <td class="px-4 py-3 text-right">$679.00</td>
              <td class="px-4 py-3 text-center">68.5</td>
              <td class="px-4 py-3 font-sans text-xs text-left">$738 / $750</td>
              <td class="px-4 py-3 font-sans text-xs text-emerald-500 font-semibold text-left">歷史收盤新高，高位均線托底</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold font-sans text-zinc-900 dark:text-zinc-100">IWM (Russell 2000)</td>
              <td class="px-4 py-3 text-right">$293.20</td>
              <td class="px-4 py-3 text-right">$288.00</td>
              <td class="px-4 py-3 text-right">$285.50</td>
              <td class="px-4 py-3 text-right">$272.00</td>
              <td class="px-4 py-3 text-center">54.2</td>
              <td class="px-4 py-3 font-sans text-xs text-left">$288 / $295</td>
              <td class="px-4 py-3 font-sans text-xs text-emerald-500 font-semibold text-left">突破短期平台，展開補漲攻勢</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold font-sans text-zinc-900 dark:text-zinc-100">SMH (Semiconductors)</td>
              <td class="px-4 py-3 text-right">$298.50</td>
              <td class="px-4 py-3 text-right">$272.50</td>
              <td class="px-4 py-3 text-right">$255.00</td>
              <td class="px-4 py-3 text-right">$217.50</td>
              <td class="px-4 py-3 text-center">74.2</td>
              <td class="px-4 py-3 font-sans text-xs text-left">$285 / $305</td>
              <td class="px-4 py-3 font-sans text-xs text-rose-500 font-semibold text-left">嚴重超買！爆量破位，需警戒乖離率過大</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold font-sans text-zinc-900 dark:text-zinc-100">IGV (Software)</td>
              <td class="px-4 py-3 text-right">$86.50</td>
              <td class="px-4 py-3 text-right">$91.20</td>
              <td class="px-4 py-3 text-right">$92.50</td>
              <td class="px-4 py-3 text-right">$90.10</td>
              <td class="px-4 py-3 text-center">39.5</td>
              <td class="px-4 py-3 font-sans text-xs text-left">$85 / $91</td>
              <td class="px-4 py-3 font-sans text-xs text-rose-500 font-semibold text-left">技術破位，均線向下，短期下尋底支撐</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold font-sans text-zinc-900 dark:text-zinc-100">XLK (Technology)</td>
              <td class="px-4 py-3 text-right">$195.51</td>
              <td class="px-4 py-3 text-right">$192.80</td>
              <td class="px-4 py-3 text-right">$188.60</td>
              <td class="px-4 py-3 text-right">$175.40</td>
              <td class="px-4 py-3 text-center">59.8</td>
              <td class="px-4 py-3 font-sans text-xs text-left">$192 / $200</td>
              <td class="px-4 py-3 font-sans text-xs text-zinc-500 font-semibold text-left">高位強震，晶片與軟體拉鋸洗籌</td>
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

      <!-- 8.1 巨頭 -->
      <details class="mb-4 p-4 rounded-xl border border-zinc-200 dark:border-zinc-800 bg-zinc-50/50 dark:bg-zinc-900/50">
        <summary class="font-bold text-zinc-800 dark:text-zinc-200 text-base">8.1 大型科技七巨頭動態</summary>
        <div class="mt-4 space-y-3 text-sm text-zinc-600 dark:text-zinc-400">
          <p><strong>GOOGL (Alphabet) -4.06% ($361.10)：</strong>正式宣佈 $800 億美元的龐大股權籌資擴張 AI 計算。其中包括波克夏·哈薩威私募直接認購 $100 億、公開發行 $300 億及未來 ATM 增發 $400 億。此舉徹底打破其多年來大規模買回股票的資本返還常規，市場引發稀釋權益憂慮及 AI 基建高成本焦慮，引導股價大跌。</p>
          <p><strong>NVDA (Nvidia) +0.65% ($225.81)：</strong>台北 Computex 續發酵，Jensen Huang 重點介紹其新互聯與網絡架構，並親自點名肯定 Marvell 助推 AI 網路，刺激自身股價穩步攀高，持穩在 $225 歷史新高附近。</p>
          <p><strong>AAPL (Apple) +1.61% ($315.22)：</strong>WWDC 2026 前夕，大摩與美銀等報告預期蘋果將把全新本地隱私 AI 模型整合至 iOS 20，並與 OpenAI 的下一代協議有突破性發展，股價放量大漲創下收盤新高。</p>
          <p><strong>MSFT (Microsoft) +0.50% ($441.29)：</strong>宣佈全面整合 Copilot 進入商用 Windows 終端，並表示 AI PC 在企業端預售翻倍，股價穩步走強。</p>
          <p><strong>META (Meta Platforms) +1.08% ($597.63)：</strong>回踩 50 日均線後吸引逢低買盤，機構上調廣告定價預期，股價收復大部分昨日跌幅。</p>
          <p><strong>TSLA (Tesla) -0.53% ($423.74)：</strong>因歐盟可能提高對中國產電動車關稅的預期，以及被馬斯克高額薪資案再次干擾，股價小幅回撤震盪。</p>
        </div>
      </details>

      <!-- 8.2 半導體 -->
      <details class="mb-4 p-4 rounded-xl border border-zinc-200 dark:border-zinc-800 bg-zinc-50/50 dark:bg-zinc-900/50">
        <summary class="font-bold text-zinc-800 dark:text-zinc-200 text-base">8.2 AI 硬體 / 半導體重點股異動分析</summary>
        <div class="mt-4 space-y-3 text-sm text-zinc-600 dark:text-zinc-400">
          <p><strong>MRVL (Marvell Technology) +32.52% ($290.79)：</strong>今日最強明星股。黃仁勳在演說中極力肯定其在超大規模 AI cluster 光模組 (Optical DSP) 與客製化晶片 (ASIC) 技術地位，並宣稱其是「下一波千億至兆元級基建的幕後英雄」。隨即爆發歷史性天量上漲，一口氣突破所有阻力平台。</p>
          <p><strong>HPE (Hewlett Packard Enterprise) +25.26% ($58.94)：</strong>盤前公佈 Q2 財報大幅擊敗市場預期（營收 $107 億年增 40%，EPS 暴漲 108% 達 $0.79）。AI 伺服器與 Networking 業務增長狂野，管理層指引顯著樂觀。Citigroup 盤中隨即將其目標價從 $39 狂調至 $70。</p>
          <p><strong>AVGO (Broadcom) +6.46% ($481.57)：</strong>作為 ASIC 與網絡晶片二把手，受 Marvell 上漲的外溢效應及台北 Computex 期間與谷歌新一代 TPU 連接架構合作傳言刺激，股價放量大漲突破歷史天花板。</p>
          <p><strong>AMD (Advanced Micro Devices) +4.17% ($509.64)：</strong>蘇姿丰在台北 Computex 展示 Ryzen AI 300 晶片對微軟 Copilot+ 的原生支持。股價在昨日利空消化後出現大幅補漲修復。</p>
        </div>
      </details>

      <!-- 8.3 軟體 -->
      <details class="mb-4 p-4 rounded-xl border border-zinc-200 dark:border-zinc-800 bg-zinc-50/50 dark:bg-zinc-900/50">
        <summary class="font-bold text-zinc-800 dark:text-zinc-200 text-base">8.3 軟體 / SaaS / AI 應用重點股異動分析</summary>
        <div class="mt-4 space-y-3 text-sm text-zinc-600 dark:text-zinc-400">
          <p><strong>NOW (ServiceNow) -7.17% ($831.01)：</strong>在無特大負面消息下大跌，機構報告指出 SaaS 訂閱由於大客戶預算被 AI 算力（買晶片/建機房）擠壓，面臨潛在的年報增長下修，高位引發劇烈套現。</p>
          <p><strong>SNOW (Snowflake) -8.00% ($179.77)：</strong>今日正逢 Snowflake Summit 2026 行會，雖然推出了針對多雲混合的「Snowflake CoCo」跨平台智能管家，但市場普遍質疑其對本季度的營收轉化速度過慢，股價破位下跌 8%。</p>
          <p><strong>CRM (Salesforce) -14.63% ($198.15)：</strong>受 SaaS 行業整體景氣收緊焦慮拖累，股價大幅殺跌跌破 $200 關鍵整數位，短期趨勢轉弱。</p>
        </div>
      </details>

      <!-- 8.4 AI 電力 -->
      <details class="mb-4 p-4 rounded-xl border border-zinc-200 dark:border-zinc-850 bg-zinc-50/50 dark:bg-zinc-900/50">
        <summary class="font-bold text-zinc-800 dark:text-zinc-200 text-base">8.4 AI 電力 / 資料中心 / 能源基礎設施重點股分析</summary>
        <div class="mt-4 space-y-3 text-sm text-zinc-600 dark:text-zinc-400">
          <p><strong>VST (Vistra Corp) +14.22% ($157.85)：</strong>電價與電網重構需求大熱，作為獨立核電與天然氣電力供給巨頭，再度獲得華爾街戰略基金大筆追捧，股價爆量拉升。</p>
          <p><strong>CEG (Constellation Energy) -8.72% ($266.62)：</strong>在高位遭遇近期少見的深度獲利回吐，主要因為部分投機資金向小盤股 Russell 2000 分流，且其估值被部分分析師點名過高。</p>
          <p><strong>ETN (Eaton Corporation) +9.21% ($417.62)：</strong>AI 變壓器與電網設備的訂單積壓時間（Backlog）已經排至 2028 年，業績確定性極高，股價強大長陽，確立新上升浪。</p>
        </div>
      </details>
    </section>

    <!-- 9. 財報日曆與財報解讀 -->
    <section id="earnings" class="mb-12 scroll-mt-6">
      <h2 class="text-2xl font-bold mb-4 flex items-center gap-2 border-b border-zinc-100 dark:border-zinc-800 pb-2">
        <span class="text-brand-500">9.</span> 財報日曆與財報解讀
      </h2>
      <div class="p-6 rounded-xl border border-zinc-200 dark:border-zinc-800 space-y-4 bg-zinc-50/30 dark:bg-zinc-900/30">
        <h3 class="text-lg font-bold text-zinc-950 dark:text-zinc-50">9.1 已公佈財報解讀</h3>
        <div class="border-l-4 border-emerald-500 pl-4 space-y-2">
          <p class="font-bold text-zinc-900 dark:text-zinc-100">Hewlett Packard Enterprise (HPE.US)</p>
          <ul class="list-disc pl-5 text-sm text-zinc-600 dark:text-zinc-400 space-y-1">
            <li><strong>Q2 業績：</strong>營收 $107 億美元（年增 40%），大幅擊敗分析師預期的 $98.5 億美元；非 GAAP EPS 報 $0.79（年增 108%），大幅超出指導區間上限 $0.55。</li>
            <li><strong>業務細節：</strong>AI 與 Cloud 業務錄得 $77 億，暴增 22.9%。高性能 AI 伺服器因算力芯片到貨加快，積壓訂單大幅向營收轉化，整體毛利率優於預期。</li>
            <li><strong>展望指引：</strong>大幅上調 2026 全年非 GAAP EPS 目標至 $2.60–$2.75。股價日內暴漲 25.26% 報 $58.94。</li>
          </ul>
        </div>
        <hr class="border-zinc-200 dark:border-zinc-800">
        <h3 class="text-lg font-bold text-zinc-950 dark:text-zinc-50">9.2 接下來 1-3 日重要財報日曆</h3>
        <div class="overflow-x-auto">
          <table class="min-w-full text-xs divide-y divide-zinc-200 dark:divide-zinc-800">
            <thead class="text-zinc-500 dark:text-zinc-400 text-left">
              <tr>
                <th class="py-2">公佈時間</th>
                <th class="py-2">公司名稱 (代碼)</th>
                <th class="py-2 text-right">預期 EPS</th>
                <th class="py-2 text-right">預期營收</th>
                <th class="py-2">市場關注點</th>
              </tr>
            </thead>
            <tbody class="divide-y divide-zinc-250 dark:divide-zinc-850 text-zinc-700 dark:text-zinc-300">
              <tr>
                <td class="py-2">06-03 盤後</td>
                <td class="py-2 font-semibold">CrowdStrike (CRWD)</td>
                <td class="py-2 text-right font-mono">$1.04</td>
                <td class="py-2 text-right font-mono">$986M</td>
                <td class="py-2">網路安全 Agentic AI 是否拉動大客戶客單價，觀察是否能提振低迷的 SaaS 板塊。</td>
              </tr>
              <tr>
                <td class="py-2">06-04 盤後</td>
                <td class="py-2 font-semibold">Lululemon (LULU)</td>
                <td class="py-2 text-right font-mono">$2.40</td>
                <td class="py-2 text-right font-mono">$2.20B</td>
                <td class="py-2">北美中產階級消費疲軟情況是否持續，以及中國市場增長是否見頂。</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </section>

    <!-- 10. 機構觀點與資金流 -->
    <section id="institutional" class="mb-12 scroll-mt-6">
      <h2 class="text-2xl font-bold mb-4 flex items-center gap-2 border-b border-zinc-100 dark:border-zinc-800 pb-2">
        <span class="text-brand-500">10.</span> 機構觀點與資金流
      </h2>
      <div class="space-y-4 text-sm text-zinc-600 dark:text-zinc-400 leading-relaxed">
        <p><strong>波克夏認購谷歌 100 億股權：</strong>巴菲特旗下 Berkshire Hathaway 宣佈私募買入 Alphabet $100 億 Class A 及 Class C Common Stock，巴菲特聲稱「谷歌在搜尋的壟斷力是極佳的護城河，且 AI 將進一步強化其優勢，私募對價極具吸引力」。此舉在谷歌大跌中為其提供了強力的底部估值支撐。</p>
        <p><strong>花旗對 HPE 的評級上調：</strong>花旗分析師指出，HPE 的業績大超預期，不僅僅是芯片到貨加快，更反映了企業對私有雲 AI 伺服器的爆發性需求。隨即將 HPE 評級調至「買入」，目標價直接拉高至 $70，領跑華爾街目標調升。</p>
        <p><strong>期權大宗異動：</strong>期權市場上，Marvell (MRVL) 日內看漲期權（Call）成交量激增 450%，主要集中在 6月20日到期的 $310 及 $330 檔口，顯示短線投機資金正在進行極端看漲博弈。</p>
      </div>
    </section>

    <!-- 11. 板塊輪動判斷 -->
    <section id="rotation" class="mb-12 scroll-mt-6">
      <h2 class="text-2xl font-bold mb-4 flex items-center gap-2 border-b border-zinc-100 dark:border-zinc-800 pb-2">
        <span class="text-brand-500">11.</span> 板塊輪動判斷
      </h2>
      <p class="text-sm text-zinc-600 dark:text-zinc-300 leading-relaxed">
        <strong>資金的「高位抱團與多點開花」：</strong>當前的板塊輪動從「極端科技抱團」開始向「工業、電網電力、小盤股」演變。谷歌融資利空和 SaaS 軟體大跌，並沒有導致大盤出現破位性恐慌。相反，資金迅速轉投受黃仁勳肯定、有業績支撐的 **AI 光晶片與伺服器硬體**，同時向**公用電網 (ETN/VST)** 及**對沖通膨的石油板塊 (XLE)** 流動。
        <br><br>
        羅素 2000 的大漲也說明市場底層的「多頭廣度」正在加寬，這是一個典型且健康的**大牛市中期輪動特徵**。只要半導體硬件龙头（NVDA、AVGO、MRVL）及電網電力（VST、ETN）不倒，指數高位震盪上行的基本牛市格局將非常牢固。
      </p>
    </section>

    <!-- 12. 重點關注股觀察 -->
    <section id="watch-list" class="mb-12 scroll-mt-6">
      <h2 class="text-2xl font-bold mb-4 flex items-center gap-2 border-b border-zinc-100 dark:border-zinc-800 pb-2">
        <span class="text-brand-500">12.</span> 我的重點關注股觀察
      </h2>
      <div class="overflow-x-auto border border-zinc-200 dark:border-zinc-800 rounded-xl">
        <table class="min-w-full divide-y divide-zinc-200 dark:divide-zinc-800 text-sm">
          <thead class="bg-zinc-50 dark:bg-zinc-900">
            <tr>
              <th class="px-4 py-3 text-left font-semibold text-zinc-600 dark:text-zinc-400">代號</th>
              <th class="px-4 py-3 text-left font-semibold text-zinc-600 dark:text-zinc-400">當日收盤 / 漲跌</th>
              <th class="px-4 py-3 text-left font-semibold text-zinc-600 dark:text-zinc-400">決策判定</th>
              <th class="px-4 py-3 text-left font-semibold text-zinc-600 dark:text-zinc-400">技術位置與操作傾向</th>
            </tr>
          </thead>
          <tbody class="divide-y divide-zinc-200 dark:divide-zinc-800 text-zinc-700 dark:text-zinc-300">
            <tr>
              <td class="px-4 py-3 font-semibold text-zinc-900 dark:text-zinc-100">NVDA</td>
              <td class="px-4 py-3 font-mono text-emerald-500 font-semibold">$225.81 (+0.65%)</td>
              <td class="px-4 py-3"><span class="px-2 py-0.5 rounded text-xs tag-strong">繼續強勢</span></td>
              <td class="px-4 py-3 text-xs">Computex 大會熱度持續，股價維持在歷史最高水平整理，短期多頭結構堅不可摧。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold text-zinc-900 dark:text-zinc-100">AMD</td>
              <td class="px-4 py-3 font-mono text-emerald-500 font-semibold">$509.64 (+4.17%)</td>
              <td class="px-4 py-3"><span class="px-2 py-0.5 rounded text-xs tag-strong">繼續強勢</span></td>
              <td class="px-4 py-3 text-xs">發布 Ryzen AI 300 處理器，Computex 展現 AI PC 野心，股價大漲重回 20 日均線。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold text-zinc-900 dark:text-zinc-100">AVGO</td>
              <td class="px-4 py-3 font-mono text-emerald-500 font-semibold">$481.57 (+6.46%)</td>
              <td class="px-4 py-3"><span class="px-2 py-0.5 rounded text-xs tag-strong">繼續強勢</span></td>
              <td class="px-4 py-3 text-xs">爆量大陽線突破歷史新高，ASIC 互聯晶片王者與 MRVL 產生強烈共振。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold text-zinc-900 dark:text-zinc-100">MRVL</td>
              <td class="px-4 py-3 font-mono text-emerald-500 font-semibold">$290.79 (+40.31%)</td>
              <td class="px-4 py-3"><span class="px-2 py-0.5 rounded text-xs tag-warning">短線過熱</span></td>
              <td class="px-4 py-3 text-xs">狂飆 32.52% (自前值 $207 計算為 +40.3%)，Jensen 點名引發天量暴漲，偏離均線過遠，切勿追高。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold text-zinc-900 dark:text-zinc-100">GOOGL</td>
              <td class="px-4 py-3 font-mono text-rose-500 font-semibold">$361.10 (-4.06%)</td>
              <td class="px-4 py-3"><span class="px-2 py-0.5 rounded text-xs tag-warning">回踩支撐</span></td>
              <td class="px-4 py-3 text-xs">宣佈 $800 億融資回踩 20 日均線。波克夏認購 $100 億提供底部安全邊際，關注 $350 支撐。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold text-zinc-900 dark:text-zinc-100">MSFT</td>
              <td class="px-4 py-3 font-mono text-emerald-500 font-semibold">$441.29 (+0.50%)</td>
              <td class="px-4 py-3"><span class="px-2 py-0.5 rounded text-xs tag-strong">繼續強勢</span></td>
              <td class="px-4 py-3 text-xs">高位強震穩健，企業端 Copilot 整合進度順暢，仍是長線資金避風港。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold text-zinc-900 dark:text-zinc-100">META</td>
              <td class="px-4 py-3 font-mono text-emerald-500 font-semibold">$597.63 (+0.91%)</td>
              <td class="px-4 py-3"><span class="px-2 py-0.5 rounded text-xs tag-strong">繼續強勢</span></td>
              <td class="px-4 py-3 text-xs">在 50 日均線止跌回彈，中期上升通道結構依然完整，繼續持股。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold text-zinc-900 dark:text-zinc-100">AMZN</td>
              <td class="px-4 py-3 font-mono text-emerald-500 font-semibold">$259.89 (+0.69%)</td>
              <td class="px-4 py-3"><span class="px-2 py-0.5 rounded text-xs tag-neutral">高位震盪</span></td>
              <td class="px-4 py-3 text-xs">股價在高位區間小幅橫盤整理，AWS 機房電網建設推進，形態偏多。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold text-zinc-900 dark:text-zinc-100">ORCL</td>
              <td class="px-4 py-3 font-mono text-emerald-500 font-semibold">$243.05 (+19.29%)</td>
              <td class="px-4 py-3"><span class="px-2 py-0.5 rounded text-xs tag-warning">短線過熱</span></td>
              <td class="px-4 py-3 text-xs">受 AI 伺服器狂潮外溢刺激放量暴漲 19.29%，挑戰前高，可部分獲利了結。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold text-zinc-900 dark:text-zinc-100">CRM</td>
              <td class="px-4 py-3 font-mono text-rose-500 font-semibold">$198.15 (-14.63%)</td>
              <td class="px-4 py-3"><span class="px-2 py-0.5 rounded text-xs tag-danger">破位風險</span></td>
              <td class="px-4 py-3 text-xs">跌破 $200 關鍵支撐並跌破 200 日線，SaaS 行業寒冬引發撤資，短期暫避。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold text-zinc-900 dark:text-zinc-100">NOW</td>
              <td class="px-4 py-3 font-mono text-rose-500 font-semibold">$831.01 (-7.17%)</td>
              <td class="px-4 py-3"><span class="px-2 py-0.5 rounded text-xs tag-warning">回踩支撐</span></td>
              <td class="px-4 py-3 text-xs">受 SaaS 整體失血拖累大挫 7.17%，測試 100 日線支撐，觀望防守。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold text-zinc-900 dark:text-zinc-100">SNOW</td>
              <td class="px-4 py-3 font-mono text-rose-500 font-semibold">$179.77 (-8.00%)</td>
              <td class="px-4 py-3"><span class="px-2 py-0.5 rounded text-xs tag-warning">回踩支撐</span></td>
              <td class="px-4 py-3 text-xs">峰會新品未打動短線資金，大跌 8% 回補跳空缺口，靜待機構調倉完成。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold text-zinc-900 dark:text-zinc-100">ADBE</td>
              <td class="px-4 py-3 font-mono text-rose-500 font-semibold">$486.74 (-0.30%)</td>
              <td class="px-4 py-3"><span class="px-2 py-0.5 rounded text-xs tag-neutral">高位震盪</span></td>
              <td class="px-4 py-3 text-xs">隨大流小幅波動整理，下週面臨核心財報大考，暫停新開倉。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold text-zinc-900 dark:text-zinc-100">PLTR</td>
              <td class="px-4 py-3 font-mono text-emerald-500 font-semibold">$152.27 (+1.80%)</td>
              <td class="px-4 py-3"><span class="px-2 py-0.5 rounded text-xs tag-strong">繼續強勢</span></td>
              <td class="px-4 py-3 text-xs">Agentic AI 第一品牌，走勢堅挺，在所有主要均線上方強勢運行，繼續看多。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold text-zinc-900 dark:text-zinc-100">LITE</td>
              <td class="px-4 py-3 font-mono text-rose-500 font-semibold">$68.02 (-0.70%)</td>
              <td class="px-4 py-3"><span class="px-2 py-0.5 rounded text-xs tag-neutral">高位震盪</span></td>
              <td class="px-4 py-3 text-xs">光模組配套跟隨大盤震盪洗籌，波動不大，守穩均線。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold text-zinc-900 dark:text-zinc-100">COHR</td>
              <td class="px-4 py-3 font-mono text-rose-500 font-semibold">$190.56 (-0.80%)</td>
              <td class="px-4 py-3"><span class="px-2 py-0.5 rounded text-xs tag-neutral">高位震盪</span></td>
              <td class="px-4 py-3 text-xs">光通訊主線稍事修整，高位巨量震盪換手，依舊處於牛市通道中。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold text-zinc-900 dark:text-zinc-100">ANET</td>
              <td class="px-4 py-3 font-mono text-emerald-500 font-semibold">$392.67 (+1.10%)</td>
              <td class="px-4 py-3"><span class="px-2 py-0.5 rounded text-xs tag-strong">繼續強勢</span></td>
              <td class="px-4 py-3 text-xs">AI 網路架構與交換機龍頭，股價沿 5 日線碎步大漲創歷史收盤新高。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold text-zinc-900 dark:text-zinc-100">FLNC</td>
              <td class="px-4 py-3 font-mono text-rose-500 font-semibold">$24.11 (-1.60%)</td>
              <td class="px-4 py-3"><span class="px-2 py-0.5 rounded text-xs tag-neutral">需要觀察</span></td>
              <td class="px-4 py-3 text-xs">儲能板塊對高利率敏感，日內大幅下探，目前正尋找底部 50 日均線支持。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold text-zinc-900 dark:text-zinc-100">OKLO</td>
              <td class="px-4 py-3 font-mono text-rose-500 font-semibold">$13.51 (-2.10%)</td>
              <td class="px-4 py-3"><span class="px-2 py-0.5 rounded text-xs tag-neutral">需要觀察</span></td>
              <td class="px-4 py-3 text-xs">小盤核能投機盤回撤，Russell 2000 走強並未帶動投機妖股，回歸冷靜。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold text-zinc-900 dark:text-zinc-100">VST</td>
              <td class="px-4 py-3 font-mono text-emerald-500 font-semibold">$157.85 (+14.22%)</td>
              <td class="px-4 py-3"><span class="px-2 py-0.5 rounded text-xs tag-strong">繼續強勢</span></td>
              <td class="px-4 py-3 text-xs">受電價調漲與資料中心用電爆量刺激爆量大漲，上升空間再次打開。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold text-zinc-900 dark:text-zinc-100">CEG</td>
              <td class="px-4 py-3 font-mono text-rose-500 font-semibold">$266.62 (-8.72%)</td>
              <td class="px-4 py-3"><span class="px-2 py-0.5 rounded text-xs tag-neutral">高位震盪</span></td>
              <td class="px-4 py-3 text-xs">經歷高位劇烈獲利了結回跌 8.72%，防守買盤在 20 日線卡位，中線無礙。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold text-zinc-900 dark:text-zinc-100">ETN</td>
              <td class="px-4 py-3 font-mono text-emerald-500 font-semibold">$417.62 (+9.21%)</td>
              <td class="px-4 py-3"><span class="px-2 py-0.5 rounded text-xs tag-strong">繼續強勢</span></td>
              <td class="px-4 py-3 text-xs">電網變壓器需求暴增，股價長陽飆升，開啟全新主升浪，堅定持股。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold text-zinc-900 dark:text-zinc-100">VRT</td>
              <td class="px-4 py-3 font-mono text-emerald-500 font-semibold">$118.50 (+5.33%)</td>
              <td class="px-4 py-3"><span class="px-2 py-0.5 rounded text-xs tag-strong">繼續強勢</span></td>
              <td class="px-4 py-3 text-xs">液冷散熱景氣火熱，沿 10 日均線碎步上攻刷新收盤新高。</td>
            </tr>
          </tbody>
        </table>
      </div>
    </section>

    <!-- 13. 明日交易計畫 -->
    <section id="plans" class="mb-12 scroll-mt-6">
      <h2 class="text-2xl font-bold mb-4 flex items-center gap-2 border-b border-zinc-100 dark:border-zinc-800 pb-2">
        <span class="text-brand-500">13.</span> 明日交易計畫 / 觀察清單
      </h2>
      <div class="space-y-4 text-sm text-zinc-600 dark:text-zinc-400">
        <p><strong>13.1 宏觀觀察：</strong>明日將公佈 ADP 就業人數（小非農）及美國 5 月 ISM 非製造業 PMI。在 JOLTs 職缺超預期引發利率日內劇震後，小非農數據若再度爆表，將推升 10年期美債利率再度挑戰 4.55% 警戒位。需要密切防範高利率引發的成長股日內回調風險。</p>
        <p><strong>13.2 大盤觀察：</strong>標普 5500 及納指強震走高。短期 QQQ 支撐在 $738，壓力在 $750。若 QQQ 跌破 $738 則可能轉為高位寬幅震盪。同時觀察羅素 2000 (IWM) 今日大漲 0.9% 後是否具備突破短期箱體上軌 (2,950 點) 的補漲動能。</p>
        <p><strong>13.3 板塊個股觀察：</strong>
          <ul class="list-decimal pl-5 space-y-1">
            <li><strong>CRWD (CrowdStrike)：</strong>明日盤後發佈財報。作為安全 SaaS 巨頭，其財報將是判定整個低迷軟體板塊是「繼續沉淪」還是「迎來超跌報復反彈」的風向標。</li>
            <li><strong>MRVL (Marvell)：</strong>今日暴增 32.52%，短線高度超買。明天預期將有獲利了結回吐，關注缺口上方支撐，不宜追高。</li>
            <li><strong>HPE (Hewlett Packard Enterprise)：</strong>財報大捷確立算力高增長，關注跳空缺口支撐，若出現回踩 20 日線，可分批佈局。</li>
          </ul>
        </p>
      </div>
    </section>

    <!-- 14. 風險提示 -->
    <section id="risks" class="mb-12 scroll-mt-6">
      <h2 class="text-2xl font-bold mb-4 flex items-center gap-2 border-b border-zinc-100 dark:border-zinc-800 pb-2">
        <span class="text-brand-500">14.</span> 風險提示矩陣
      </h2>
      <div class="overflow-x-auto border border-zinc-200 dark:border-zinc-800 rounded-xl">
        <table class="min-w-full divide-y divide-zinc-200 dark:divide-zinc-800 text-sm">
          <thead class="bg-zinc-50 dark:bg-zinc-900">
            <tr>
              <th class="px-4 py-3 text-left font-semibold text-zinc-600 dark:text-zinc-400">風險維度</th>
              <th class="px-4 py-3 text-center font-semibold text-zinc-600 dark:text-zinc-400">風險評級</th>
              <th class="px-4 py-3 text-left font-semibold text-zinc-600 dark:text-zinc-400">具體解讀</th>
            </tr>
          </thead>
          <tbody class="divide-y divide-zinc-200 dark:divide-zinc-800 text-zinc-700 dark:text-zinc-300">
            <tr>
              <td class="px-4 py-3 font-semibold text-zinc-900 dark:text-zinc-100">宏觀利率風險</td>
              <td class="px-4 py-3 text-center"><span class="px-2 py-0.5 rounded text-xs tag-warning">中高風險</span></td>
              <td class="px-4 py-3 text-xs">JOLTs 超預期說明就業市場非常強勁。若本週五非農再度爆表，美債 10 年期收益率將可能迅速突破 4.55% 壓力位，對高融資高估值的軟體與中小盤構成二次殺估值。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold text-zinc-900 dark:text-zinc-100">AI 擁擠度風險</td>
              <td class="px-4 py-3 text-center"><span class="px-2 py-0.5 rounded text-xs tag-warning">中高風險</span></td>
              <td class="px-4 py-3 text-xs">Marvell 日內飆漲 32% 及費半大漲 5%，半導體板塊 RSI 紛紛衝至 70-75 嚴重超買邊界，短線炒作熱度過熱，切忌高位追加大筆倉位，謹防盤中劇烈洗盤。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold text-zinc-900 dark:text-zinc-100">地緣政治風險</td>
              <td class="px-4 py-3 text-center"><span class="px-2 py-0.5 rounded text-xs tag-warning">中等風險</span></td>
              <td class="px-4 py-3 text-xs">美伊外交談判再度陷入僵局，霍爾木茲海峽航道威脅未能解除，原油 WTI 站穩 $93.76。若局部地緣衝突激化，油價突破 $96 將重燃大宗商品通膨威脅。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold text-zinc-900 dark:text-zinc-100">SaaS 業績衰退</td>
              <td class="px-4 py-3 text-center"><span class="px-2 py-0.5 rounded text-xs tag-strong">高風險</span></td>
              <td class="px-4 py-3 text-xs">SaaS 大龍頭 Salesforce 及 ServiceNow 近期大跌顯示，企業 AI 轉型初期正嚴重擠壓傳統 SaaS 預算，板塊技術破位明顯，在利潤轉化未被證實前不宜盲目左側抄底。</td>
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
      <div class="p-6 rounded-xl bg-brand-50/10 dark:bg-brand-500/5 border border-brand-100 dark:border-brand-500/20 space-y-4">
        <p class="text-sm text-zinc-600 dark:text-zinc-300 leading-relaxed">
          <strong>市場主線評估：</strong>今日美股在就業爆表與巨頭利差（谷歌稀釋）的雙重壓制下，憑藉 Marvell 互聯大潮與 HPE 驚艷財報完成了對「AI 算力基建」的二次大爆發，帶動指數完美收創收盤新高。這顯示資金抱團 AI 強力基建意志極高，市場健康度在中小盤 Russell 2000 的補漲下反而有所加寬。
        </p>
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4 text-sm">
          <div class="space-y-2">
            <span class="text-xs font-semibold text-zinc-400">當前市場階段</span>
            <p class="text-base font-bold text-brand-600 dark:text-brand-500">強趨勢上漲 / 板塊極限分化</p>
          </div>
          <div class="space-y-2">
            <span class="text-xs font-semibold text-zinc-400">操作傾向 (中性)</span>
            <p class="text-base font-bold text-zinc-800 dark:text-zinc-200">持股核心 AI 硬體，防禦配置能源/電網設備，防範超買晶片股短線波動與 SaaS 軟體破位風險。</p>
          </div>
        </div>
        <div class="p-4 bg-zinc-50 dark:bg-zinc-900 rounded-lg border border-zinc-100 dark:border-zinc-800">
          <span class="text-xs font-semibold text-zinc-400 block mb-2">最值得關注的 5 個訊號</span>
          <ul class="list-decimal pl-5 text-xs text-zinc-650 dark:text-zinc-350 space-y-1">
            <li><strong>ADP 就業人數與非農：</strong>本週最核心的宏觀變量，直接定價 10 年期美債利率。</li>
            <li><strong>10年期美債利率：</strong>觀察是否會放量突防 4.52% 的日內高位阻力。</li>
            <li><strong>CRWD (CrowdStrike) 財報：</strong>判定安全與 SaaS 軟體是否有超跌反彈契機。</li>
            <li><strong>Marvell (MRVL) 是否高位回踩：</strong>今日大漲後是否能平穩洗籌並維持在缺口上方。</li>
            <li><strong>羅素 2000 (IWM)：</strong>觀察小盤股大漲後是否具有可持續性的補漲效應。</li>
          </ul>
        </div>
      </div>
    </section>

  </main>
</div>

<script>
  // Theme Toggle Logic
  const toggleBtn = document.getElementById('theme-toggle');
  toggleBtn.addEventListener('click', () => {
    const isDark = document.documentElement.classList.toggle('dark');
    localStorage.theme = isDark ? 'dark' : 'light';
    
    // Update Mermaid if loaded
    if (window.__mermaid) {
      window.__mermaid.initialize({ startOnLoad: false, theme: isDark ? 'dark' : 'default' });
      // Re-render mermaid diagrams if needed
    }
    
    // Update Chart.js Grid Colors
    if (window.returnsChartInstance) {
      const gridColor = isDark ? 'rgba(255,255,255,0.08)' : 'rgba(0,0,0,0.05)';
      const tickColor = isDark ? '#a1a1aa' : '#71717a';
      const legendColor = isDark ? '#f4f4f5' : '#18181b';
      
      window.returnsChartInstance.options.scales.x.grid.color = gridColor;
      window.returnsChartInstance.options.scales.x.ticks.color = tickColor;
      window.returnsChartInstance.options.scales.y.grid.color = gridColor;
      window.returnsChartInstance.options.scales.y.ticks.color = tickColor;
      window.returnsChartInstance.options.plugins.legend.labels.color = legendColor;
      window.returnsChartInstance.update();
    }
  });

  // TOC Active State on Scroll
  const sections = document.querySelectorAll('main section');
  const links = document.querySelectorAll('.toc a');
  
  if (sections.length && links.length) {
    const onScroll = () => {
      let scrollPos = window.scrollY + 100;
      let activeIdx = 0;
      
      sections.forEach((sec, idx) => {
        const top = sec.offsetTop;
        const height = sec.offsetHeight;
        if (scrollPos >= top && scrollPos < top + height) {
          activeIdx = idx;
        }
      });
      
      // Fallback for bottom of page
      if ((window.innerHeight + window.scrollY) >= document.body.offsetHeight - 50) {
        activeIdx = sections.length - 1;
      }

      links.forEach((link, idx) => {
        if (idx === activeIdx) {
          link.classList.add('active');
        } else {
          link.classList.remove('active');
        }
      });
    };
    window.addEventListener('scroll', onScroll, { passive: true });
    onScroll();
  }

  // Chart.js: Rendering Returns Comparison Chart
  const ctx = document.getElementById('returnsChart').getContext('2d');
  const isDark = document.documentElement.classList.contains('dark');
  window.returnsChartInstance = new Chart(ctx, {
    type: 'bar',
    data: {
      labels: ['道瓊工業', '標普 500', '納指綜合', '納指 100', '羅素 2000', 'SOX 半導體', 'VIX 恐慌'],
      datasets: [{
        label: '當日漲跌幅 (%)',
        data: [0.45, 0.13, 0.03, 0.48, 0.90, 5.19, 1.00],
        backgroundColor: function(context) {
          const val = context.dataset.data[context.dataIndex];
          return val >= 0 ? 'rgba(2, 132, 199, 0.15)' : 'rgba(239, 68, 68, 0.15)';
        },
        borderColor: function(context) {
          const val = context.dataset.data[context.dataIndex];
          return val >= 0 ? '#0284c7' : '#ef4444';
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
          grid: { color: isDark ? 'rgba(255,255,255,0.08)' : 'rgba(0,0,0,0.05)' },
          ticks: { color: isDark ? '#a1a1aa' : '#71717a', font: { family: 'mono' } }
        },
        y: {
          grid: { color: isDark ? 'rgba(255,255,255,0.08)' : 'rgba(0,0,0,0.05)' },
          ticks: { color: isDark ? '#a1a1aa' : '#71717a', font: { weight: 'bold' } }
        }
      },
      plugins: {
        legend: {
          labels: { color: isDark ? '#f4f4f5' : '#18181b', font: { weight: 'bold' } }
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

  // Vanilla JS Search for Sectors Table
  document.getElementById('sectorSearch').addEventListener('input', function(e) {
    const q = e.target.value.toLowerCase();
    const rows = document.querySelectorAll('#sectorsTable tbody tr');
    rows.forEach(r => {
      const text = r.textContent.toLowerCase();
      r.style.display = text.includes(q) ? '' : 'none';
    });
  });

  // Vanilla JS Sorter for Sectors Table
  let currentSortCol = -1;
  let currentSortAsc = true;
  window.sortSectors = function(colIdx) {
    const table = document.getElementById('sectorsTable');
    const tbody = table.querySelector('tbody');
    const rows = Array.from(tbody.querySelectorAll('tr'));

    if (currentSortCol === colIdx) {
      currentSortAsc = !currentSortAsc;
    } else {
      currentSortCol = colIdx;
      currentSortAsc = true;
    }

    rows.sort((a, b) => {
      let aVal = a.cells[colIdx].innerText;
      let bVal = b.cells[colIdx].innerText;

      // Extract raw data-val attributes for numerical sorting if present
      const aData = a.cells[colIdx].getAttribute('data-val');
      const bData = b.cells[colIdx].getAttribute('data-val');

      if (aData !== null && bData !== null) {
        return currentSortAsc ? parseFloat(aData) - parseFloat(bData) : parseFloat(bData) - parseFloat(aData);
      }

      // Check if sorting by integer rank
      if (colIdx === 0) {
        return currentSortAsc ? parseInt(aVal) - parseInt(bVal) : parseInt(bVal) - parseInt(aVal);
      }

      // Default string compare
      return currentSortAsc ? aVal.localeCompare(bVal) : bVal.localeCompare(aVal);
    });

    // Re-append sorted rows
    tbody.innerHTML = '';
    rows.forEach(r => tbody.appendChild(r));
  }
</script>

</body>
</html>
"""

# Save this HTML to reports/2026-06-02-us-stock-closing-daily-report.html inside /Users/wisdom/html-report-skill
target_dir = "/Users/wisdom/html-report-skill/reports"
os.makedirs(target_dir, exist_ok=True)
target_path = os.path.join(target_dir, "2026-06-02-us-stock-closing-daily-report.html")

with open(target_path, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"Report HTML file generated successfully at: {target_path}")

# Now let's update manifest.json
manifest_path = os.path.join(target_dir, "manifest.json")
try:
    with open(manifest_path, "r", encoding="utf-8") as f:
        manifest = json.load(f)
except Exception:
    manifest = []

# Check if already exists to avoid duplicate
exists = any(item.get("file") == "2026-06-02-us-stock-closing-daily-report.html" for item in manifest)
if not exists:
    new_entry = {
      "file": "2026-06-02-us-stock-closing-daily-report.html",
      "title": "美股收盤日報｜2026-06-02",
      "date": "2026-06-02",
      "description": "美股大盤續創歷史新高！Marvell (MRVL) 與 HPE 財報驚艷引領 AI 算力半導體狂飆，SOX 指數暴漲 5.19%；Alphabet (GOOGL) 籌資 800 億美元回調 4.06%，JOLTs 職位空缺 760 萬超預期令利率短線波動。"
    }
    manifest.insert(0, new_entry)
    with open(manifest_path, "w", encoding="utf-8") as f:
        json.dump(manifest, f, ensure_ascii=False, indent=2)
    print(f"Updated manifest.json successfully at: {manifest_path}")
else:
    print("manifest.json already contains the entry for 2026-06-02.")
