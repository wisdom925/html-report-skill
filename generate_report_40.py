import os
import json

html_content = """<!doctype html>
<html lang="zh-TW" class="scroll-smooth">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <title>美股收盤日報｜2026-06-18</title>
  <meta name="description" content="2026年6月18日美股收盤日報：美伊敲定臨時和平協議引油價大瀉，特朗普宣佈Apple與Intel晶片合作引爆晶片製造狂潮，費半暴漲6.42%，標普收復7500，三大指數高歌反彈，電力基建及冷卻散熱巨頭續創歷史新高。">
  <meta property="og:title" content="美股收盤日報｜2026-06-18">
  <meta property="og:description" content="美伊和平協議油價跌，Intel攜手Apple晶片自主狂潮，費半大漲6.42%創高，電力散熱巨頭飆升。">
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
        <span class="px-2.5 py-1 text-xs font-semibold rounded-full bg-brand-50 text-brand-600 dark:bg-brand-950/50 dark:text-brand-400">美股收盤日報</span>
        <span class="text-sm text-zinc-400">•</span>
        <time class="text-sm font-semibold text-zinc-500 dark:text-zinc-400">2026-06-18</time>
      </div>
      <h1 class="text-3xl sm:text-4xl font-extrabold tracking-tight mb-4 bg-gradient-to-r from-zinc-900 to-zinc-700 dark:from-zinc-100 dark:to-zinc-400 bg-clip-text text-transparent">
        美股收盤日報｜美伊敲定和平協議引油價大瀉，Intel攜手Apple晶片合作引爆晶片製造狂潮！費半暴漲6.42%，標普收復7500，三大指數高歌反彈，電力基建及液冷散熱持續大爆發
      </h1>
      <p class="text-lg text-zinc-500 dark:text-zinc-400 leading-relaxed">
        週四美股三大指數呈現報復性大反彈。盤前公佈的美國初請失業金人數符合勞動市場溫和降溫趨勢，費城聯邦儲備銀行製造業指數大幅反彈至 10.3 顯示基本面仍具強勁韌性。隨後，特朗普於 Truth Social 發帖透露 Apple 已與 Intel 達成在美設計及生產晶片的歷史性協議，引發 Intel 暴漲 9.38% 並刺激半導體板塊井噴，費城半導體指數大漲 6.42% 創下歷史收盤新高。同時，美伊正式敲定臨時和平框架協議，重新開放霍爾木茲海峽，刺激 WTI 原油價格大跌至 $74 關口附近，顯著舒緩市場對滯脹及通膨的焦慮。在晶片股與油價大跌的雙重催化下，標普 500 指數上漲 1.08% 收復 7,500 點大關，納指暴漲 1.91%，羅素 2000 亦大漲 2.12% 站上 50MA。資金亦持續湧入受用電剛性需求推動的 AI 電力公共事業（VST、CEG）及散熱設備（VRT），帶動板塊續創歷史新高。然而板塊分化依然嚴重的特徵是高估值的 SaaS 應用軟體板塊在利率高企壓制下遭遇大幅拋售，Salesforce（CRM）暴跌 7.80%。
      </p>
    </header>

    <!-- 0. 今日一句話總結 -->
    <section id="summary" class="mb-12 scroll-mt-6">
      <h2 class="text-2xl font-bold mb-4 flex items-center gap-2 border-b border-zinc-100 dark:border-zinc-800 pb-2">
        <span class="text-brand-500">0.</span> 今日一句話總結
      </h2>
      <div class="bg-zinc-50/50 dark:bg-zinc-900/50 p-6 rounded-2xl border border-zinc-200/60 dark:border-zinc-800/60 leading-relaxed text-zinc-700 dark:text-zinc-300">
        <ul class="list-disc pl-5 space-y-3">
          <li><strong>大盤狀態：</strong>美股指數全線反彈，標普 500 指數重回 7500 關卡之上，費城半導體指數受 Apple-Intel 消息刺激暴拉 6.42% 續創歷史新高。</li>
          <li><strong>驅動因素：</strong>核心利多為特朗普透露 Apple 與 Intel 達成晶片生產合作，引爆晶片國產化熱潮；以及美伊敲定臨時和平協定令原油地緣溢價被大幅剝離，油價重挫舒緩通膨壓力。</li>
          <li><strong>資金流向：</strong>資金重回半導體板塊（SMH）與中小型股票（IWM），同時對 AI 電力（CEG、VST）與液冷散熱（VRT）的剛性配置需求不減；但資金繼續從對利率敏感、缺乏短期業績催化的應用軟體 SaaS 板塊大舉移出。</li>
          <li><strong>市場寬度：</strong>市場寬度相較昨日顯著改善，交易所上漲個股數量是下跌數量的 3 倍以上，中小型股大舉復甦。</li>
          <li><strong>一句話判斷：</strong><span class="text-emerald-500 font-semibold dark:text-emerald-400">油價暴瀉舒緩通膨，晶片電力雙引擎噴發，SaaS板塊破位大跌，大盤呈報復性反彈與強烈結構性大輪動。</span></li>
        </ul>
      </div>
    </section>

    <!-- 1. 大盤表現總覽 -->
    <section id="market-overview" class="mb-12 scroll-mt-6">
      <h2 class="text-2xl font-bold mb-4 flex items-center gap-2 border-b border-zinc-100 dark:border-zinc-800 pb-2">
        <span class="text-brand-500">1.</span> 大盤表現總覽
      </h2>
      
      <div class="overflow-x-auto border border-zinc-200 dark:border-zinc-800 rounded-xl mb-6">
        <table class="min-w-full divide-y divide-zinc-200 dark:divide-zinc-800 text-sm">
          <thead class="bg-zinc-50 dark:bg-zinc-900">
            <tr class="text-zinc-555 dark:text-zinc-400 text-left">
              <th class="px-4 py-3 font-semibold">指數名稱</th>
              <th class="px-4 py-3 font-semibold text-right">收盤點位</th>
              <th class="px-4 py-3 font-semibold text-right">漲跌點</th>
              <th class="px-4 py-3 font-semibold text-right">漲跌幅</th>
              <th class="px-4 py-3 font-semibold text-right">技術狀態</th>
            </tr>
          </thead>
          <tbody class="divide-y divide-zinc-200 dark:divide-zinc-850 font-mono text-zinc-700 dark:text-zinc-300">
            <tr>
              <td class="px-4 py-3 font-semibold font-sans text-zinc-900 dark:text-zinc-100">Dow Jones (道瓊)</td>
              <td class="px-4 py-3 text-right">51,564.70</td>
              <td class="px-4 py-3 text-right text-emerald-500 font-semibold">+72.15</td>
              <td class="px-4 py-3 text-right text-emerald-500 font-semibold">+0.14%</td>
              <td class="px-4 py-3 font-sans text-xs text-emerald-500 font-semibold">突破並收復 10MA ($51,520)，高位震盪回穩</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold font-sans text-zinc-900 dark:text-zinc-100">S&P 500 (標普 500)</td>
              <td class="px-4 py-3 text-right">7,500.58</td>
              <td class="px-4 py-3 text-right text-emerald-500 font-semibold">+80.48</td>
              <td class="px-4 py-3 text-right text-emerald-500 font-semibold">+1.08%</td>
              <td class="px-4 py-3 font-sans text-xs text-emerald-500 font-semibold">強勢突破並收復 10MA，重返 7500 整數關口之上</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold font-sans text-zinc-900 dark:text-zinc-100">Nasdaq Composite (納指)</td>
              <td class="px-4 py-3 text-right">26,517.93</td>
              <td class="px-4 py-3 text-right text-emerald-500 font-semibold">+496.28</td>
              <td class="px-4 py-3 text-right text-emerald-500 font-semibold">+1.91%</td>
              <td class="px-4 py-3 font-sans text-xs text-emerald-500 font-semibold">帶量大陽線收復 10MA，短線多頭動能回升</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold font-sans text-zinc-900 dark:text-zinc-100">Nasdaq 100 / QQQ</td>
              <td class="px-4 py-3 text-right">740.11</td>
              <td class="px-4 py-3 text-right text-emerald-500 font-semibold">+7.91</td>
              <td class="px-4 py-3 text-right text-emerald-500 font-semibold">+1.08%</td>
              <td class="px-4 py-3 font-sans text-xs text-emerald-500 font-semibold">強勢突破 $732 平台，再創收盤歷史新高</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold font-sans text-zinc-900 dark:text-zinc-100">Russell 2000 (羅素 2000)</td>
              <td class="px-4 py-3 text-right">2,979.77</td>
              <td class="px-4 py-3 text-right text-emerald-500 font-semibold">+61.79</td>
              <td class="px-4 py-3 text-right text-emerald-500 font-semibold">+2.12%</td>
              <td class="px-4 py-3 font-sans text-xs text-emerald-500 font-semibold">突破 50MA ($291.2) 和 20MA ($294.5)，短期底部構築</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold font-sans text-zinc-900 dark:text-zinc-100">SOX 半導體指數</td>
              <td class="px-4 py-3 text-right">14,341.78</td>
              <td class="px-4 py-3 text-right text-emerald-500 font-semibold">+864.68</td>
              <td class="px-4 py-3 text-right text-emerald-500 font-semibold">+6.42%</td>
              <td class="px-4 py-3 font-sans text-xs text-emerald-500 font-semibold">跳空長陽線向上突破，創歷史收盤新高，多頭排列</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold font-sans text-zinc-900 dark:text-zinc-100">VIX 波動率指數</td>
              <td class="px-4 py-3 text-right">16.94</td>
              <td class="px-4 py-3 text-right text-emerald-500 font-semibold">+0.74</td>
              <td class="px-4 py-3 text-right text-emerald-500 font-semibold">+4.57%</td>
              <td class="px-4 py-3 font-sans text-xs text-amber-500 font-semibold">長週末前避險買盤活躍，VIX 逆大盤小幅攀升</td>
            </tr>
          </tbody>
        </table>
      </div>

      <!-- Returns Chart -->
      <div class="p-4 bg-zinc-50 dark:bg-zinc-900 rounded-xl border border-zinc-200 dark:border-zinc-800">
        <h3 class="text-sm font-semibold text-zinc-500 mb-3 text-center uppercase tracking-wider">指數收盤漲跌幅對比</h3>
        <div class="h-64 relative">
          <canvas id="returnsChart"></canvas>
        </div>
      </div>
    </section>

    <!-- 2. 盤中走勢復盤 -->
    <section id="timeline" class="mb-12 scroll-mt-6">
      <h2 class="text-2xl font-bold mb-4 flex items-center gap-2 border-b border-zinc-100 dark:border-zinc-800 pb-2">
        <span class="text-brand-500">2.</span> 盤中走勢復盤
      </h2>

      <div class="relative border-l border-zinc-200 dark:border-zinc-800 ml-4 md:ml-6 space-y-8 mb-8">
        <!-- Event 1 -->
        <div class="relative pl-8 md:pl-10">
          <div class="absolute -left-3 top-1.5 w-6 h-6 rounded-full bg-blue-500 border-4 border-white dark:border-zinc-900 flex items-center justify-center"></div>
          <div class="bg-zinc-50 dark:bg-zinc-900 p-4 rounded-xl border border-zinc-200 dark:border-zinc-800 text-sm grow">
            <span class="text-xs text-zinc-400 font-semibold">盤前 08:30 AM</span>
            <h4 class="font-bold text-zinc-800 dark:text-zinc-200 mt-1">製造業數據重回擴張，初請失業金溫和</h4>
            <p class="text-zinc-555 dark:text-zinc-400 mt-1 leading-relaxed">
              美國勞工部公佈初請失業金人數為 22.6 萬，符合市場預期；同時，6月費城聯邦儲備銀行製造業指數大幅反彈至 10.3（遠超前值的 -0.4 及預期的 9.8），表明製造業擴張提速。數據令大盤盤前小幅高開。
            </p>
          </div>
        </div>

        <!-- Event 2 -->
        <div class="relative pl-8 md:pl-10">
          <div class="absolute -left-3 top-1.5 w-6 h-6 rounded-full bg-blue-500 border-4 border-white dark:border-zinc-900 flex items-center justify-center"></div>
          <div class="bg-zinc-50 dark:bg-zinc-900 p-4 rounded-xl border border-zinc-200 dark:border-zinc-800 text-sm grow">
            <span class="text-xs text-zinc-400 font-semibold">開盤 09:30 AM</span>
            <h4 class="font-bold text-zinc-800 dark:text-zinc-200 mt-1">特朗普宣佈 Apple 與 Intel 晶片合作，半導體板塊跳空井噴</h4>
            <p class="text-zinc-555 dark:text-zinc-400 mt-1 leading-relaxed">
              特朗普在 Truth Social 透露 Apple 與 Intel 已達成在美國本土設計及代工晶片的重大戰略協議，Intel Premarket 瞬間狂飆，帶領整個費半板塊跳空高開。ASML、台積電 ADR (TSM)、Micron 及 Broadcom 均帶量大幅衝高。
            </p>
          </div>
        </div>

        <!-- Event 3 -->
        <div class="relative pl-8 md:pl-10">
          <div class="absolute -left-3 top-1.5 w-6 h-6 rounded-full bg-blue-500 border-4 border-white dark:border-zinc-900 flex items-center justify-center"></div>
          <div class="bg-zinc-50 dark:bg-zinc-900 p-4 rounded-xl border border-zinc-200 dark:border-zinc-800 text-sm grow">
            <span class="text-xs text-zinc-400 font-semibold">午盤 01:00 PM</span>
            <h4 class="font-bold text-zinc-800 dark:text-zinc-200 mt-1">美伊和平協議敲定，油價崩跌解除通膨焦慮</h4>
            <p class="text-zinc-555 dark:text-zinc-400 mt-1 leading-relaxed">
              美伊敲定臨時和平框架協議，霍爾木茲海峽重新安全開放。WTI 原油重挫 1.45% 跌破 $75，通膨憂慮大幅緩解，降息重估情緒好轉。資金瘋狂湧入先前受高息壓制的中小型股（Russell 2000），推動小盤股暴力反彈，XLI 工業與 XLY 非必需消費亦強勢拉升。
            </p>
          </div>
        </div>

        <!-- Event 4 -->
        <div class="relative pl-8 md:pl-10">
          <div class="absolute -left-3 top-1.5 w-6 h-6 rounded-full bg-blue-500 border-4 border-white dark:border-zinc-900 flex items-center justify-center"></div>
          <div class="bg-zinc-50 dark:bg-zinc-900 p-4 rounded-xl border border-zinc-200 dark:border-zinc-800 text-sm grow">
            <span class="text-xs text-zinc-400 font-semibold">收盤 04:00 PM</span>
            <h4 class="font-bold text-zinc-800 dark:text-zinc-200 mt-1">標普重上 7,500，半導體電力基建狂飆，SaaS 板塊血流成河</h4>
            <p class="text-zinc-555 dark:text-zinc-400 mt-1 leading-relaxed">
              大盤尾盤加速上揚，標普 500 指數收於 7,500.58 點。AI 電力巨頭 Vistra (VST +6.42%) 及散熱龍頭 Vertiv (VRT +6.72%) 續創歷史新高。但無息的 SaaS 軟體遭資金無情拋售，CRM 下挫 7.80%，引致板塊走向極端結構性輪動。由於週五為 Juneteenth 假期，市場交易在長週末前收盤。
            </p>
          </div>
        </div>
      </div>

      <!-- Timeline visual flow in Mermaid -->
      <div class="p-4 bg-zinc-50 dark:bg-zinc-900 rounded-xl border border-zinc-200 dark:border-zinc-800 text-center">
        <h3 class="text-xs font-semibold text-zinc-500 mb-4 uppercase tracking-wider">今日市場運行邏輯 (Mermaid)</h3>
        <pre class="mermaid bg-transparent">
graph TD
    TrumpPost[特朗普透露 Apple-Intel 晶片代工協議] --> IntelSurge[Intel暴漲9% 費半SOX大噴發6.42%]
    USIranDeal[美伊敲定臨時和平框架協議] --> CrudeDrop[WTI原油跌破$75 舒緩通膨預期]
    CrudeDrop --> IWMRebound[中小企業融資舒緩 羅素2000暴漲2.12%]
    
    PhillyFed[費城聯邦製造業指數10.3超預期] --> BroadMarketRebound[標普500上漲1.08% 收復7500點]
    
    AIPowerDemand[AI資料中心電力與液冷散熱剛性需求] --> PowerSurge[VST暴漲6.4% VRT飆漲6.7%創高]
    SaaSRotation[高估值SaaS無息避險能力差] --> SaaSPlunge[CRM暴跌7.8% 軟體板塊重挫2.85%]
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
        <label for="tab4">3.4 當日經濟數據</label>

        <!-- Tab Panel 1 -->
        <div class="tab-panel w-full text-zinc-600 dark:text-zinc-400 text-sm sm:text-base leading-relaxed">
          <h4 class="font-bold text-zinc-800 dark:text-zinc-200 mb-2">地緣局勢緩和舒緩美息，收益率曲線小幅平坦化</h4>
          <p>
            在美伊達成和平協定、原油價格回落後，美債收益率從昨日的高位小幅回落。政策敏感的 <strong>2年期美債收益率</strong> 下滑 4 個基點至 <strong>4.84%</strong>（昨日 4.88%）；<strong>10年期美債收益率</strong> 亦跌 2 個基點收於 <strong>4.46%</strong>（昨日 4.48%）；<strong>30年期美債收益率</strong> 則收於 <strong>4.91%</strong>。收益率曲線依然呈現倒掛狀態，雖然通膨焦慮有所降低，但聯準會點陣圖顯露的鷹派預期限制了美息的下行空間，高融資利率繼續對軟體板塊構成重創。
          </p>
        </div>

        <!-- Tab Panel 2 -->
        <div class="tab-panel w-full text-zinc-600 dark:text-zinc-400 text-sm sm:text-base leading-relaxed">
          <h4 class="font-bold text-zinc-800 dark:text-zinc-200 mb-2">降息預期維持低位整理，市場聚焦下半年通膨走勢</h4>
          <p>
            根據 CME FedWatch 指標，市場對聯準會年底前「按兵不動」或「降息一次」的機率仍然佔據主導（合計機率約為 82%）。新任聯準會主席凱文·沃許（Kevin Warsh）的鷹派首秀確立了聯準會「數據依賴」而非「前瞻引導」的立場。由於今日零售與失業金數據保持平穩，市場對 9 月降息的期待已大幅下挫至 25% 左右，將核心目光轉向即將公佈的 6 月通膨報告。
          </p>
        </div>

        <!-- Tab Panel 3 -->
        <div class="tab-panel w-full text-zinc-600 dark:text-zinc-400 text-sm sm:text-base leading-relaxed">
          <h4 class="font-bold text-zinc-800 dark:text-zinc-200 mb-2">霍爾木茲開通原油急瀉，美元大幅走高，黃金加密回穩</h4>
          <p>
            <strong>WTI 原油 &amp; Brent 原油：</strong>中東危機解除，原油供應中斷疑慮消除。WTI 原油下跌 1.45% 報 <strong>$74.58 / 桶</strong>；Brent 原油下跌 1.25% 至 <strong>$78.22 / 桶</strong>。<br>
            <strong>美元指數 DXY：</strong>美債息居高不下吸引跨國套利資金，DXY 升至 <strong>100.65</strong> (+1.11%)。<br>
            <strong>黃金現貨：</strong>黃金期貨發揮避險配置價值，今日反彈 2.08% 收於 <strong>$4,325.00 / 盎司</strong>。<br>
            <strong>加密貨幣：</strong>市場風險偏好回暖推動加密貨幣反彈。比特幣 (BTC) 上漲 1.97% 報 <strong>$66,120</strong>，以太坊 (ETH) 上漲 2.49% 報 <strong>$1,812</strong>。
          </p>
        </div>

        <!-- Tab Panel 4 -->
        <div class="tab-panel w-full text-zinc-600 dark:text-zinc-400 text-sm sm:text-base leading-relaxed">
          <h4 class="font-bold text-zinc-800 dark:text-zinc-200 mb-2">製造業重回擴張區間，勞動市場溫和降溫</h4>
          <div class="overflow-x-auto my-3">
            <table class="min-w-full divide-y divide-zinc-200 dark:divide-zinc-800 text-xs sm:text-sm text-left">
              <thead class="bg-zinc-50 dark:bg-zinc-900 text-zinc-400">
                <tr>
                  <th class="px-3 py-2 font-semibold">經濟指標</th>
                  <th class="px-3 py-2 font-semibold">公佈時間</th>
                  <th class="px-3 py-2 text-center font-semibold">實際值</th>
                  <th class="px-3 py-2 text-center font-semibold">預期值</th>
                  <th class="px-3 py-2 text-center font-semibold">前值</th>
                  <th class="px-3 py-2">市場解讀</th>
                </tr>
              </thead>
              <tbody class="divide-y divide-zinc-200 dark:divide-zinc-850 font-mono text-zinc-700 dark:text-zinc-300">
                <tr>
                  <td class="px-3 py-2 font-sans font-semibold">6月費城聯邦儲備銀行製造業指數</td>
                  <td class="px-3 py-2 font-sans">08:30 AM</td>
                  <td class="px-3 py-2 text-center text-emerald-500 font-bold">10.3</td>
                  <td class="px-3 py-2 text-center">9.8</td>
                  <td class="px-3 py-2 text-center">-0.4</td>
                  <td class="px-3 py-2 font-sans text-xs">大超預期的 10.3，顯示美國區域性製造業重新回歸擴張，新訂單和出貨均強勁。</td>
                </tr>
                <tr>
                  <td class="px-3 py-2 font-sans font-semibold">美國上週初請失業金人數 (Initial Claims)</td>
                  <td class="px-3 py-2 font-sans">08:30 AM</td>
                  <td class="px-3 py-2 text-center text-emerald-500 font-bold">22.6萬</td>
                  <td class="px-3 py-2 text-center">22.5萬</td>
                  <td class="px-3 py-2 text-center">23.0萬</td>
                  <td class="px-3 py-2 font-sans text-xs">溫和降溫但依然健康，表明就業市場雖有放緩跡象但並未出現大規模裁員。</td>
                </tr>
              </tbody>
            </table>
          </div>
          <div class="text-xs text-zinc-400 border-t border-zinc-100 dark:border-zinc-800 pt-2">
            > [!NOTE]
            > 製造業反彈與勞動力市場的健康狀態，支持了聯準會的偏鷹觀點，市場仍以「更高更長」利率常態進行計價。
          </div>
        </div>
      </div>
    </section>

    <!-- 4. 板塊表現 -->
    <section id="sectors" class="mb-12 scroll-mt-6">
      <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-4 mb-4 border-b border-zinc-100 dark:border-zinc-800 pb-2">
        <h2 class="text-2xl font-bold flex items-center gap-2">
          <span class="text-brand-500">4.</span> S&P 500 十一個板塊表現
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
              <td class="px-4 py-3 font-medium">資訊科技 (Information Technology)</td>
              <td class="px-4 py-3 font-mono">XLK</td>
              <td class="px-4 py-3 text-right font-mono text-emerald-500 font-semibold" data-val="2.18">+2.18%</td>
              <td class="px-4 py-3 text-right font-mono" data-val="1.55">+1.55%</td>
              <td class="px-4 py-3 text-right font-mono" data-val="5.80">+5.80%</td>
              <td class="px-4 py-3 text-zinc-500 dark:text-zinc-400">半導體板塊狂熱，Apple與Intel合作引發晶片股爆買，彌補了軟體板塊跌勢。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-medium">2</td>
              <td class="px-4 py-3 font-medium">基礎材料 (Materials)</td>
              <td class="px-4 py-3 font-mono">XLB</td>
              <td class="px-4 py-3 text-right font-mono text-emerald-500 font-semibold" data-val="1.52">+1.52%</td>
              <td class="px-4 py-3 text-right font-mono" data-val="1.85">+1.85%</td>
              <td class="px-4 py-3 text-right font-mono" data-val="2.10">+2.10%</td>
              <td class="px-4 py-3 text-zinc-500 dark:text-zinc-400">製造業指數反彈與原物料需求預期回升，對金屬與礦業公司構成推動。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-medium">3</td>
              <td class="px-4 py-3 font-medium">非必需消費 (Consumer Discretionary)</td>
              <td class="px-4 py-3 font-mono">XLY</td>
              <td class="px-4 py-3 text-right font-mono text-emerald-500 font-semibold" data-val="1.48">+1.48%</td>
              <td class="px-4 py-3 text-right font-mono" data-val="1.15">+1.15%</td>
              <td class="px-4 py-3 text-right font-mono" data-val="3.10">+3.10%</td>
              <td class="px-4 py-3 text-zinc-500 dark:text-zinc-400">油價大跌直接減少消費者生活成本，加之零售額維持健康，亞馬遜大反彈。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-medium">4</td>
              <td class="px-4 py-3 font-medium">工業 (Industrials)</td>
              <td class="px-4 py-3 font-mono">XLI</td>
              <td class="px-4 py-3 text-right font-mono text-emerald-500 font-semibold" data-val="1.28">+1.28%</td>
              <td class="px-4 py-3 text-right font-mono" data-val="2.10">+2.10%</td>
              <td class="px-4 py-3 text-right font-mono" data-val="3.25">+3.25%</td>
              <td class="px-4 py-3 text-zinc-500 dark:text-zinc-400">費城製造業PMI大反彈和运输物流成本因原油暴瀉而降低。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-medium">5</td>
              <td class="px-4 py-3 font-medium">金融 (Financials)</td>
              <td class="px-4 py-3 font-mono">XLF</td>
              <td class="px-4 py-3 text-right font-mono text-emerald-500 font-semibold" data-val="1.02">+1.02%</td>
              <td class="px-4 py-3 text-right font-mono" data-val="2.80">+2.80%</td>
              <td class="px-4 py-3 text-right font-mono" data-val="3.85">+3.85%</td>
              <td class="px-4 py-3 text-zinc-500 dark:text-zinc-400">美國債息居高不下保障銀行息差利潤，金融大行吸引避險性配置。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-medium">6</td>
              <td class="px-4 py-3 font-medium">通訊服務 (Communication Services)</td>
              <td class="px-4 py-3 font-mono">XLC</td>
              <td class="px-4 py-3 text-right font-mono text-emerald-500 font-semibold" data-val="0.95">+0.95%</td>
              <td class="px-4 py-3 text-right font-mono" data-val="0.80">+0.80%</td>
              <td class="px-4 py-3 text-right font-mono" data-val="4.15">+4.15%</td>
              <td class="px-4 py-3 text-zinc-500 dark:text-zinc-400">Google 與 Meta 擺脫利率陰霾強勁上攻反彈，抵消部分媒體龍頭拖累。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-medium">7</td>
              <td class="px-4 py-3 font-medium">公用事業 (Utilities)</td>
              <td class="px-4 py-3 font-mono">XLU</td>
              <td class="px-4 py-3 text-right font-mono text-emerald-500 font-semibold" data-val="0.82">+0.82%</td>
              <td class="px-4 py-3 text-right font-mono" data-val="2.15">+2.15%</td>
              <td class="px-4 py-3 text-right font-mono" data-val="3.30">+3.30%</td>
              <td class="px-4 py-3 text-zinc-500 dark:text-zinc-400">AI資料中心電力需求推升電網基建及核電板塊，板塊無視債息走高而強推。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-medium">8</td>
              <td class="px-4 py-3 font-medium">日常消費 (Consumer Staples)</td>
              <td class="px-4 py-3 font-mono">XLP</td>
              <td class="px-4 py-3 text-right font-mono text-emerald-500 font-semibold" data-val="0.42">+0.42%</td>
              <td class="px-4 py-3 text-right font-mono" data-val="0.50">+0.50%</td>
              <td class="px-4 py-3 text-right font-mono" data-val="0.95">+0.95%</td>
              <td class="px-4 py-3 text-zinc-500 dark:text-zinc-400">隨着大盤強勁風險偏好回暖，防禦性資金移防，表現跑輸大盤。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-medium">9</td>
              <td class="px-4 py-3 font-medium">醫療保健 (Health Care)</td>
              <td class="px-4 py-3 font-mono">XLV</td>
              <td class="px-4 py-3 text-right font-mono text-emerald-500 font-semibold" data-val="0.31">+0.31%</td>
              <td class="px-4 py-3 text-right font-mono" data-val="0.10">+0.10%</td>
              <td class="px-4 py-3 text-right font-mono" data-val="0.65">+0.65%</td>
              <td class="px-4 py-3 text-zinc-500 dark:text-zinc-400">非核心大盤防禦類股，買盤冷清，資金流向科技及小盤板塊。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-medium">10</td>
              <td class="px-4 py-3 font-medium">房地產 (Real Estate)</td>
              <td class="px-4 py-3 font-mono">XLRE</td>
              <td class="px-4 py-3 text-right font-mono text-rose-500 font-semibold" data-val="-0.15">-0.15%</td>
              <td class="px-4 py-3 text-right font-mono" data-val="-0.80">-0.80%</td>
              <td class="px-4 py-3 text-right font-mono" data-val="-0.55">-0.55%</td>
              <td class="px-4 py-3 text-zinc-500 dark:text-zinc-400">房地產板塊仍然受 4.8% 以上的 2年期融資利率重壓。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-medium">11</td>
              <td class="px-4 py-3 font-medium">能源 (Energy)</td>
              <td class="px-4 py-3 font-mono">XLE</td>
              <td class="px-4 py-3 text-right font-mono text-rose-500 font-semibold" data-val="-1.78">-1.78%</td>
              <td class="px-4 py-3 text-right font-mono" data-val="-8.95">-8.95%</td>
              <td class="px-4 py-3 text-right font-mono" data-val="-6.50">-6.50%</td>
              <td class="px-4 py-3 text-zinc-500 dark:text-zinc-400">中東和平談判順利導致油價急跌，重創石油探勘與煉油類股股價。</td>
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
      <div class="grid grid-cols-1 md:grid-cols-2 gap-6 text-sm sm:text-base leading-relaxed text-zinc-650 dark:text-zinc-400">
        <div class="p-5 rounded-xl bg-sky-50/20 dark:bg-sky-950/10 border border-sky-100 dark:border-sky-900/30">
          <h4 class="font-bold text-zinc-800 dark:text-zinc-200 mb-2">半導體與 AI 算力硬件 (SMH/SOXX)</h4>
          <p>
            費城半導體指數（SOX）暴漲 <strong>+6.42%</strong>。Intel 與 Apple 的合作傳聞引爆晶片國產化與代工狂潮。Intel 暴漲 9.38%，台積電 ADR (TSM) 大漲 3.49% 創歷史新高，半導體板塊（SMH）跳空強勢突破前期歷史高點。
          </p>
        </div>
        <div class="p-5 rounded-xl bg-amber-50/20 dark:bg-amber-955/10 border border-amber-100 dark:border-amber-900/30">
          <h4 class="font-bold text-zinc-800 dark:text-zinc-200 mb-2">應用軟體與 SaaS (IGV)</h4>
          <p>
            軟體板塊在飆升的無風險利率壓制下重創，IGV 大跌 <strong>-2.85%</strong>。板塊遭到無情拋售，估值乘數重塑。Salesforce (CRM) 下跌 7.80% 收於 $151.67，Adobe (ADBE) 下挫 4.81% 報 $195.29。
          </p>
        </div>
        <div class="p-5 rounded-xl bg-emerald-50/20 dark:bg-emerald-950/10 border border-emerald-100 dark:border-emerald-900/30">
          <h4 class="font-bold text-zinc-800 dark:text-zinc-200 mb-2">中小型股與等權標普 (IWM/RSP)</h4>
          <p>
            羅素 2000 指數暴漲 <strong>+2.12%</strong> 報 2,979.77，成功收復 50MA 關鍵均線。油價大瀉直接舒緩了中小企業的通膨成本，風險偏好回暖刺激小盤股報復性補漲。等權標普（RSP）今日大漲 1.25%，表現好於加權標普 500。
          </p>
        </div>
        <div class="p-5 rounded-xl bg-purple-50/20 dark:bg-purple-955/10 border border-purple-100 dark:border-purple-900/30">
          <h4 class="font-bold text-zinc-800 dark:text-zinc-200 mb-2">AI 資料中心電力與散熱 (XLU/VST)</h4>
          <p>
            電力與液冷散熱持續井噴。Vistra (VST) 大漲 <strong>+6.42%</strong> 收報 $163.33 創高，核電巨擘 Constellation (CEG) 狂漲 <strong>+7.97%</strong> 收報 $274.08，散熱大廠 Vertiv (VRT) 暴漲 <strong>+6.72%</strong> 至 $330.32 創歷史新高。
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
        <div class="p-5 bg-zinc-50 dark:bg-zinc-900 border border-zinc-200 dark:border-zinc-800 rounded-xl">
          <h4 class="font-bold text-zinc-800 dark:text-zinc-200 text-sm mb-2">均線參與度</h4>
          <p class="text-xs text-zinc-500 mb-3">成分股高於各主要均線比例</p>
          <div class="space-y-2 text-sm font-mono">
            <div class="flex justify-between">
              <span class="text-zinc-400">S&P 500 > 50MA:</span>
              <strong class="text-emerald-500">64% (比昨日顯著回暖)</strong>
            </div>
            <div class="flex justify-between">
              <span class="text-zinc-400">Nasdaq 100 > 50MA:</span>
              <strong class="text-emerald-500">58% (多頭防線修復)</strong>
            </div>
            <div class="flex justify-between">
              <span class="text-zinc-400">S&P 500 > 200MA:</span>
              <strong class="text-emerald-500">66% (中期牛市趨勢健康)</strong>
            </div>
          </div>
          <p class="text-xs text-zinc-400 mt-2">大盤大反彈帶動多數破位個股反彈回均線上方，市場健康度重回良性狀態。</p>
        </div>
        <div class="p-5 bg-zinc-50 dark:bg-zinc-900 border border-zinc-200 dark:border-zinc-800 rounded-xl">
          <h4 class="font-bold text-zinc-800 dark:text-zinc-200 text-sm mb-2">漲跌家數與新高新低</h4>
          <p class="text-xs text-zinc-500 mb-3">NYSE &amp; Nasdaq 交易所數據</p>
          <div class="space-y-2 text-sm font-mono">
            <div class="flex justify-between">
              <span class="text-zinc-400">NYSE 上漲/下跌:</span>
              <strong class="text-emerald-500">2,350 / 680</strong>
            </div>
            <div class="flex justify-between">
              <span class="text-zinc-400">Nasdaq 上漲/下跌:</span>
              <strong class="text-emerald-500">3,100 / 920</strong>
            </div>
            <div class="flex justify-between">
              <span class="text-zinc-400">52週新高/新低差值:</span>
              <strong class="text-emerald-500">NYSE (+88), Nasdaq (+120)</strong>
            </div>
          </div>
          <p class="text-xs text-zinc-400 mt-2">交易所上漲股與下跌股為 3:1 以上，新高數量飆升，顯示多頭具備高度主導權。</p>
        </div>
        <div class="p-5 bg-zinc-50 dark:bg-zinc-900 border border-zinc-200 dark:border-zinc-800 rounded-xl">
          <h4 class="font-bold text-zinc-800 dark:text-zinc-200 text-sm mb-2">其他內部指標</h4>
          <p class="text-xs text-zinc-500 mb-3">市場情緒與資金動態指標</p>
          <div class="space-y-2 text-sm font-mono">
            <div class="flex justify-between">
              <span class="text-zinc-400">Put/Call Ratio:</span>
              <strong class="text-emerald-500">0.72 (避險意願降溫)</strong>
            </div>
            <div class="flex justify-between">
              <span class="text-zinc-400">McClellan Oscillator:</span>
              <strong class="text-emerald-500">+15 (重回正值區間)</strong>
            </div>
            <div class="flex justify-between">
              <span class="text-zinc-400">VIX Term Structure:</span>
              <strong class="text-emerald-500">陡峭化 (短線恐慌釋放)</strong>
            </div>
          </div>
          <p class="text-xs text-zinc-400 mt-2">Put/Call 比率回落至常態區間，麥氏指標低位大彈，反映市場短線拋售動能完全枯竭。</p>
        </div>
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
              <th class="px-4 py-3 font-semibold">ETF 名稱</th>
              <th class="px-4 py-3 font-semibold text-right">收盤價格</th>
              <th class="px-4 py-3 font-semibold">各均線位置</th>
              <th class="px-4 py-3 text-center font-semibold">RSI (14)</th>
              <th class="px-4 py-3 font-semibold">MACD / 趨勢狀態</th>
              <th class="px-4 py-3 font-semibold">關鍵支撐 / 壓力</th>
            </tr>
          </thead>
          <tbody class="divide-y divide-zinc-200 dark:divide-zinc-850 font-mono text-zinc-700 dark:text-zinc-300">
            <tr>
              <td class="px-4 py-3 font-semibold font-sans text-zinc-900 dark:text-zinc-100">SPY (S&P 500)</td>
              <td class="px-4 py-3 text-right">$750.06</td>
              <td class="px-4 py-3 font-sans text-xs text-emerald-500">收復 10MA ($748.2)，站穩上升趨勢軌道之上</td>
              <td class="px-4 py-3 text-center">56</td>
              <td class="px-4 py-3 font-sans text-xs text-emerald-500">多頭動能回升，死叉警報暫時解除</td>
              <td class="px-4 py-3 font-sans text-xs">$742 / $755</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold font-sans text-zinc-900 dark:text-zinc-100">QQQ (Nasdaq 100)</td>
              <td class="px-4 py-3 text-right">$740.11</td>
              <td class="px-4 py-3 font-sans text-xs text-emerald-500">強勢拉升創歷史新高，遠高於 5MA ($732.2)</td>
              <td class="px-4 py-3 text-center">66</td>
              <td class="px-4 py-3 font-sans text-xs text-emerald-500">強勢多頭，均線呈完美多頭排列形態</td>
              <td class="px-4 py-3 font-sans text-xs">$732 / $750</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold font-sans text-zinc-900 dark:text-zinc-100">IWM (Russell 2000)</td>
              <td class="px-4 py-3 text-right">$294.65</td>
              <td class="px-4 py-3 font-sans text-xs text-emerald-500">大長陽收復 50MA ($291.2) 和 20MA ($294.5)</td>
              <td class="px-4 py-3 text-center">50</td>
              <td class="px-4 py-3 font-sans text-xs text-emerald-500">底部金叉形態初現，由空轉多修復中</td>
              <td class="px-4 py-3 font-sans text-xs">$291 / $298</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold font-sans text-zinc-900 dark:text-zinc-100">SMH (Semiconductor)</td>
              <td class="px-4 py-3 text-right">$283.52</td>
              <td class="px-4 py-3 font-sans text-xs text-emerald-500">向上缺口創歷史新高，大幅超克 5MA ($266.4)</td>
              <td class="px-4 py-3 text-center">72</td>
              <td class="px-4 py-3 font-sans text-xs text-rose-500">極度超買，KD與RSI均在超買高位，防回調</td>
              <td class="px-4 py-3 font-sans text-xs">$272 / $290</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold font-sans text-zinc-900 dark:text-zinc-100">IGV (Software)</td>
              <td class="px-4 py-3 text-right">$486.53</td>
              <td class="px-4 py-3 font-sans text-xs text-rose-500">破位大跌跌破 50MA ($500.8)，測試 100MA</td>
              <td class="px-4 py-3 text-center">32</td>
              <td class="px-4 py-3 font-sans text-xs text-rose-500">嚴重超賣，日K沿底軌加速下跌，面臨空頭控盤</td>
              <td class="px-4 py-3 font-sans text-xs">$480 / $500</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold font-sans text-zinc-900 dark:text-zinc-100">XLK (Technology)</td>
              <td class="px-4 py-3 text-right">$249.81</td>
              <td class="px-4 py-3 font-sans text-xs text-emerald-500">反彈收復 10MA ($245.5)，於高位防守企穩</td>
              <td class="px-4 py-3 text-center">58</td>
              <td class="px-4 py-3 font-sans text-xs text-amber-500">中性偏多，板塊受半導體及軟體多空對沖</td>
              <td class="px-4 py-3 font-sans text-xs">$244 / $254</td>
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
        <details class="bg-zinc-50 dark:bg-zinc-900 border border-zinc-200 dark:border-zinc-800 rounded-xl p-4">
          <summary class="font-bold text-zinc-800 dark:text-zinc-200 text-sm sm:text-base">8.1 大型科技七巨頭 (META, MSFT, AMZN, GOOGL, TSLA, NVDA, AAPL)</summary>
          <div class="mt-3 space-y-3 pl-4 text-sm leading-relaxed text-zinc-650 dark:text-zinc-400 border-l-2 border-zinc-200 dark:border-zinc-800">
            <p><strong>GOOGL (Alphabet):</strong> 上漲 <strong>+4.12%</strong> 收報 <strong>$367.87</strong>。摩根士丹利大讚其 DeepMind 全新 Gemini Ultra 3.0 大模型具備顯著商業變現力，推升股價報復性反彈收復 20MA。</p>
            <p><strong>AMZN (亞馬遜):</strong> 上漲 <strong>+2.97%</strong> 收報 <strong>$244.37</strong>。原油大瀉引導其龐大的物流倉儲成本顯著下滑，股價重拾 10MA 多頭防線。</p>
            <p><strong>META (Meta Platforms):</strong> 上漲 <strong>+2.74%</strong> 收報 <strong>$574.18</strong>。隨科技大盤回暖，擺脫昨日大跌的陰霾。</p>
            <p><strong>TSLA (特斯拉):</strong> 上漲 <strong>+2.95%</strong> 收報 <strong>$214.28</strong>。市場預期其自動駕駛 (FSD) 最新版將獲國內發照支持，吸引短線資金回流。</p>
            <p><strong>AAPL (蘋果):</strong> 上漲 <strong>+0.28%</strong> 收報 <strong>$295.95</strong>。特朗普透露其將與 Intel 代工合作，市場預計此舉是為防範中東及亞洲地緣供應鏈中斷的避險政策。</p>
            <p><strong>MSFT (微軟):</strong> 上漲 <strong>+0.27%</strong> 收報 <strong>$378.63</strong>。小幅回穩，但由於高利率令 Azure 折現率承壓，跑輸標普。</p>
            <p><strong>NVDA (輝達):</strong> 下跌 <strong>-1.03%</strong> 收報 <strong>$204.67</strong>。部分多頭資金因 Intel-Apple 合作傳聞向 Intel 及 TSM 轉移而高位獲利回吐，但仍守穩 10MA 支撐。</p>
          </div>
        </details>

        <!-- 8.2 AI 硬體 / 半導體重點股 -->
        <details class="bg-zinc-50 dark:bg-zinc-900 border border-zinc-200 dark:border-zinc-800 rounded-xl p-4">
          <summary class="font-bold text-zinc-800 dark:text-zinc-200 text-sm sm:text-base">8.2 AI 硬體 / 半導體重點股 (Intel, TSM, ARM, ASML, AMD, AVGO)</summary>
          <div class="mt-3 space-y-3 pl-4 text-sm leading-relaxed text-zinc-650 dark:text-zinc-400 border-l-2 border-zinc-200 dark:border-zinc-800">
            <p><strong>Intel (INTC):</strong> 大漲 <strong>+9.38%</strong> 收報 <strong>$131.83</strong>。特朗普的 Truth Social 發帖爆料稱 Apple 已同意將部分晶片移交 Intel 本土代工廠生產，激勵其代工業務估值，吸引資金瘋狂掃貨。</p>
            <p><strong>TSM (台積電ADR):</strong> 大漲 <strong>+3.49%</strong> 收報 <strong>$453.84</strong>。機構分析認爲 Apple 的代工需求極大，Intel 本地產能短期無法取代台積電 2nm 最尖端晶片，且美伊協定緩和地緣憂慮，刺激股價創歷史收盤新高。</p>
            <p><strong>MRVL (馬威爾):</strong> 飆升 <strong>+8.71%</strong> 收報 <strong>$324.50</strong>。光通訊光模組爆發性訂單傳聞被多份研究報告確認，股價突破前期阻力大漲。</p>
            <p><strong>AMD (超微):</strong> 上漲 <strong>+0.18%</strong> 收報 <strong>$512.48</strong>。高位窄幅整理，守住 $500 大關。</p>
            <p><strong>AVGO (博通):</strong> 下跌 <strong>-0.28%</strong> 收報 <strong>$393.94</strong>。在高位小幅獲利了結整理。</p>
          </div>
        </details>

        <!-- 8.3 軟體 / SaaS / AI 應用重點股 -->
        <details class="bg-zinc-50 dark:bg-zinc-900 border border-zinc-200 dark:border-zinc-800 rounded-xl p-4">
          <summary class="font-bold text-zinc-800 dark:text-zinc-200 text-sm sm:text-base">8.3 軟體 / SaaS / AI 應用重點股 (CRM, NOW, ADBE, SNOW, PLTR)</summary>
          <div class="mt-3 space-y-3 pl-4 text-sm leading-relaxed text-zinc-650 dark:text-zinc-400 border-l-2 border-zinc-200 dark:border-zinc-800">
            <p><strong>CRM (Salesforce):</strong> 暴跌 <strong>-7.80%</strong> 收報 <strong>$151.67</strong>。受制於利率高企壓制企業雲端 IT 支出，大摩調降其評級至中性，警告其訂閱合約成長將大幅減速，引發板塊去槓桿踩踏。</p>
            <p><strong>NOW (ServiceNow):</strong> 暴跌 <strong>-5.93%</strong> 收報 <strong>$95.48</strong>。受 CRM 拖累破位跌破短期均線，軟體估值重塑拋售潮蔓延。</p>
            <p><strong>ADBE (Adobe):</strong> 大跌 <strong>-4.81%</strong> 收報 <strong>$195.29</strong>。跌破 200MA，高融資壓力對無息 SaaS 的乘數定價構成嚴峻打壓。</p>
            <p><strong>SNOW (Snowflake):</strong> 下跌 <strong>-0.66%</strong> 收報 <strong>$234.52</strong>。於底部低位縮量掙扎整理。</p>
          </div>
        </details>

        <!-- 8.4 AI 電力 / 資料中心 / 能源基礎設施 -->
        <details class="bg-zinc-50 dark:bg-zinc-900 border border-zinc-200 dark:border-zinc-800 rounded-xl p-4">
          <summary class="font-bold text-zinc-800 dark:text-zinc-200 text-sm sm:text-base">8.4 AI 電力 / 資料中心 / 能源基礎設施 (VST, CEG, VRT, ETN, OKLO)</summary>
          <div class="mt-3 space-y-3 pl-4 text-sm leading-relaxed text-zinc-650 dark:text-zinc-400 border-l-2 border-zinc-200 dark:border-zinc-800">
            <p><strong>CEG (星座能源):</strong> 飆升 <strong>+7.97%</strong> 收報 <strong>$274.08</strong>。有傳言稱微軟計畫追加核電購電合約，資金瘋狂追捧核電基建，股價狂拉創歷史收盤新高。</p>
            <p><strong>VRT (維諦):</strong> 大漲 <strong>+6.72%</strong> 收報 <strong>$330.32</strong>。液冷散熱系統需求極端強勁，機構繼續上調目標價至 $350，帶量衝高創歷史新高。</p>
            <p><strong>VST (Vistra):</strong> 暴漲 <strong>+6.42%</strong> 收報 <strong>$163.33</strong>。受益於德州及大西洋中部資料中心用電價格上修，多頭資金高昂買入，創歷史收盤新高。</p>
            <p><strong>ETN (伊頓):</strong> 上漲 <strong>+3.13%</strong> 收報 <strong>$421.77</strong>。受益重電變壓器出貨大超預期，帶量上行。</p>
            <p><strong>OKLO (Oklo):</strong> 上漲 <strong>+3.38%</strong> 收報 <strong>$61.17</strong>。跟隨核能基建主線反彈，突破短期阻力。</p>
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
          <h4 class="font-bold text-zinc-800 dark:text-zinc-200 mb-2">9.1 昨夜已公佈財報重點公司</h4>
          <p class="text-zinc-500 dark:text-zinc-400 leading-relaxed mb-3">
            <strong>目前處於財報季前空窗期：</strong>昨夜無核心巨頭公佈最新財報。市場目前仍持續消化上週 Oracle (ORCL) 與 Adobe (ADBE) 呈現的極端分化財報導引：資料中心軟體需求依然有撐，但純 SaaS 應用面臨企業縮減 IT 預算。
          </p>
        </div>
        <div class="p-5 bg-zinc-50 dark:bg-zinc-900 border border-zinc-200 dark:border-zinc-800 rounded-xl">
          <h4 class="font-bold text-zinc-800 dark:text-zinc-200 mb-2">9.2 未來 1-3 個交易日重要財報日曆</h4>
          <p class="text-zinc-500 dark:text-zinc-400 leading-relaxed">
            由於週五（6月19日）為 Juneteenth 聯邦法定假日，美股休市一天。市場將在下週一（6月22日）重新開啟，市場重點關注：<br>
            - <strong>FDS (FactSet) - 下週一：</strong>金融機構數據終端採購需求。<br>
            - <strong>KMX (CarMax) - 下週二：</strong>中古車零售景氣，觀測消費者微觀承受力。<br>
            - <strong>ACN (埃森哲) - 下週三：</strong>企業數位轉型與 AI 諮詢訂單，為科技軟體最核心微觀風向標。
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
          <strong>摩根大通宏觀研究部 (JPMorgan Chase):</strong> 美伊簽署臨時框架和平協議是一次重大的通膨緩衝劑。霍爾木茲海峽重新開放令原油供應危機解除，油價下行將降低大眾通膨焦慮，並為聯準會提供一定的政策操作空間。小摩預期這會推動先前受利率重創的羅素 2000 中小板塊迎來反彈，但由於新任聯準會主席立場依舊偏鷹，資金仍會極端青睞「有業績剛性防禦」的半導體晶片股與 AI 電力。
        </p>
        <p>
          <strong>期權與 ETF 資金流：</strong>ETF 資金方面，今日資金流向呈現瘋狂的結構性洗牌，大筆買單流入 SMH、IWM 和 XLU，而 XLK 則因 SaaS 的重創呈現淨流出。期權市場中，長週末前避險情緒高昂，VIX 看漲期權 (VIX Calls) 未平倉合約大增，Put/Call 比率降至 0.72 仍反映投資人以衍生品鎖定科技股歷史高位利潤。
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
          今日市場資金大輪動格局確立為<strong>「逃離 SaaS 軟體，移防晶片、電力基建與中小盤」</strong>。隨着美國費城PMI製造業大反彈及原油暴瀉，先前避險性移防大盤巨頭（Microsoft、Meta）和 SaaS 軟體的資金，正大量回流至更具彈性的小盤股（IWM）及受 Apple-Intel 消息刺激的晶片製造股（Intel、TSM）。與此同時，剛性需求大增的電力基建（VST、CEG）與伺服器散熱（VRT）繼續作爲核心抱團點，完全無視利率壓力狂飆。這證明大盤牛市結構依舊健康，資金只是在利率高企下進行極端的「汰弱留強」式重構，高估值且缺乏業績爆點的軟體公司面臨長期出局。
        </p>
      </div>
    </section>

    <!-- 12. 重點關注股觀察 -->
    <section id="watchlist" class="mb-12 scroll-mt-6">
      <h2 class="text-2xl font-bold mb-4 flex items-center gap-2 border-b border-zinc-100 dark:border-zinc-800 pb-2">
        <span class="text-brand-500">12.</span> 重點關注股觀察
      </h2>
      
      <div class="overflow-x-auto border border-zinc-200 dark:border-zinc-800 rounded-xl">
        <table class="min-w-full divide-y divide-zinc-200 dark:divide-zinc-800 text-sm">
          <thead class="bg-zinc-50 dark:bg-zinc-900">
            <tr class="text-zinc-555 dark:text-zinc-400 text-left">
              <th class="px-4 py-3 font-semibold">代碼</th>
              <th class="px-4 py-3 font-semibold text-right">收盤價格 (當日漲跌)</th>
              <th class="px-4 py-3">技術位置與走勢特徵</th>
              <th class="px-4 py-3">交易判定</th>
              <th class="px-4 py-3 text-left">關鍵位置與操作說明</th>
            </tr>
          </thead>
          <tbody class="divide-y divide-zinc-200 dark:divide-zinc-850 font-mono text-zinc-700 dark:text-zinc-300">
            <tr>
              <td class="px-4 py-3 font-semibold font-sans text-zinc-900 dark:text-zinc-100">NVDA</td>
              <td class="px-4 py-3 text-right text-rose-500 font-semibold">$204.67 (-1.03%)</td>
              <td class="px-4 py-3 font-sans">隨科技大盤回調，在 10MA 上方企穩</td>
              <td class="px-4 py-3 font-sans"><span class="px-2 py-0.5 rounded bg-amber-100 dark:bg-amber-950 text-amber-800 dark:text-amber-350 text-xs font-semibold">回踩支撐</span></td>
              <td class="px-4 py-3 font-sans text-xs">AI核心硬體需求堅挺，回調提供良性配置機會。支撐 $202，壓力 $215。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold font-sans text-zinc-900 dark:text-zinc-100">AMD</td>
              <td class="px-4 py-3 text-right text-emerald-500 font-semibold">$512.48 (+0.18%)</td>
              <td class="px-4 py-3 font-sans">高位窄幅震盪，守住 $500 大關</td>
              <td class="px-4 py-3 font-sans"><span class="px-2 py-0.5 rounded bg-zinc-100 dark:bg-zinc-800 text-zinc-800 dark:text-zinc-300 text-xs font-semibold">高位震盪</span></td>
              <td class="px-4 py-3 font-sans text-xs">估值尚需消化。防守 $500 關卡。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold font-sans text-zinc-900 dark:text-zinc-100">AVGO</td>
              <td class="px-4 py-3 text-right text-rose-500 font-semibold">$393.94 (-0.28%)</td>
              <td class="px-4 py-3 font-sans">高位窄幅震盪整理，回補昨日跳空缺口</td>
              <td class="px-4 py-3 font-sans"><span class="px-2 py-0.5 rounded bg-zinc-100 dark:bg-zinc-800 text-zinc-800 dark:text-zinc-300 text-xs font-semibold">高位震盪</span></td>
              <td class="px-4 py-3 font-sans text-xs">多頭趨勢不變。支撐 $385，阻力挑戰 $415。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold font-sans text-zinc-900 dark:text-zinc-100">MRVL</td>
              <td class="px-4 py-3 text-right text-emerald-500 font-semibold">$324.50 (+8.71%)</td>
              <td class="px-4 py-3 font-sans">突破前期高點阻力，量能大幅激增</td>
              <td class="px-4 py-3 font-sans"><span class="px-2 py-0.5 rounded bg-emerald-100 dark:bg-emerald-950 text-emerald-800 dark:text-emerald-350 text-xs font-semibold">繼續強勢</span></td>
              <td class="px-4 py-3 font-sans text-xs">光通信模組訂單超預期爆發。支撐 $310，壓力挑戰 $340。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold font-sans text-zinc-900 dark:text-zinc-100">GOOGL</td>
              <td class="px-4 py-3 text-right text-emerald-500 font-semibold">$367.87 (+4.12%)</td>
              <td class="px-4 py-3 font-sans">大反彈收復 20MA，人氣顯著好轉</td>
              <td class="px-4 py-3 font-sans"><span class="px-2 py-0.5 rounded bg-emerald-100 dark:bg-emerald-950 text-emerald-800 dark:text-emerald-350 text-xs font-semibold">低位修復</span></td>
              <td class="px-4 py-3 font-sans text-xs">大模型變現評級調高。支撐 $355，壓力 $375。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold font-sans text-zinc-900 dark:text-zinc-100">MSFT</td>
              <td class="px-4 py-3 text-right text-emerald-500 font-semibold">$378.63 (+0.27%)</td>
              <td class="px-4 py-3 font-sans">維持 20MA 附近震盪，估值面承壓</td>
              <td class="px-4 py-3 font-sans"><span class="px-2 py-0.5 rounded bg-zinc-100 dark:bg-zinc-800 text-zinc-800 dark:text-zinc-300 text-xs font-semibold">高位震盪</span></td>
              <td class="px-4 py-3 font-sans text-xs">高息折現率下大型科技股受壓。支撐 $372，壓力 $390。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold font-sans text-zinc-900 dark:text-zinc-100">META</td>
              <td class="px-4 py-3 text-right text-emerald-500 font-semibold">$574.18 (+2.74%)</td>
              <td class="px-4 py-3 font-sans">強勁反彈收復 5MA，重回歷史高點區</td>
              <td class="px-4 py-3 font-sans"><span class="px-2 py-0.5 rounded bg-emerald-100 dark:bg-emerald-950 text-emerald-800 dark:text-emerald-350 text-xs font-semibold">繼續強勢</span></td>
              <td class="px-4 py-3 font-sans text-xs">多頭買盤仍具韌性。支撐看 $560，壓力 $585。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold font-sans text-zinc-900 dark:text-zinc-100">AMZN</td>
              <td class="px-4 py-3 text-right text-emerald-500 font-semibold">$244.37 (+2.97%)</td>
              <td class="px-4 py-3 font-sans">突破並收復 10MA 支撐，原油下跌利多</td>
              <td class="px-4 py-3 font-sans"><span class="px-2 py-0.5 rounded bg-emerald-100 dark:bg-emerald-950 text-emerald-800 dark:text-emerald-350 text-xs font-semibold">低位修復</span></td>
              <td class="px-4 py-3 font-sans text-xs">物流運輸成本利多。支撐 $238。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold font-sans text-zinc-900 dark:text-zinc-100">ORCL</td>
              <td class="px-4 py-3 text-right text-emerald-500 font-semibold">$184.29 (+2.09%)</td>
              <td class="px-4 py-3 font-sans">放量反彈創歷史收盤新高</td>
              <td class="px-4 py-3 font-sans"><span class="px-2 py-0.5 rounded bg-emerald-100 dark:bg-emerald-950 text-emerald-800 dark:text-emerald-350 text-xs font-semibold">繼續強勢</span></td>
              <td class="px-4 py-3 font-sans text-xs">資料中心業務能見度明朗。支撐 $180。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold font-sans text-zinc-900 dark:text-zinc-100">CRM</td>
              <td class="px-4 py-3 text-right text-rose-500 font-semibold">$151.67 (-7.80%)</td>
              <td class="px-4 py-3 font-sans">放量長陰跌破短期所有均線，估值重創</td>
              <td class="px-4 py-3 font-sans"><span class="px-2 py-0.5 rounded bg-rose-100 dark:bg-rose-950 text-rose-800 dark:text-rose-350 text-xs font-semibold">破位風險</span></td>
              <td class="px-4 py-3 font-sans text-xs">大摩調降評級，雲IT減速。支撐 $148，壓力 $162。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold font-sans text-zinc-900 dark:text-zinc-100">NOW</td>
              <td class="px-4 py-3 text-right text-rose-500 font-semibold">$95.48 (-5.93%)</td>
              <td class="px-4 py-3 font-sans">放量暴跌，跌破 50MA/100MA，技術面崩潰</td>
              <td class="px-4 py-3 font-sans"><span class="px-2 py-0.5 rounded bg-rose-100 dark:bg-rose-950 text-rose-800 dark:text-rose-350 text-xs font-semibold">破位風險</span></td>
              <td class="px-4 py-3 font-sans text-xs">受CRM評級拖累。離場觀望，防守 $92。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold font-sans text-zinc-900 dark:text-zinc-100">SNOW</td>
              <td class="px-4 py-3 text-right text-rose-500 font-semibold">$234.52 (-0.66%)</td>
              <td class="px-4 py-3 font-sans">在低點縮量盤整，買盤萎靡</td>
              <td class="px-4 py-3 font-sans"><span class="px-2 py-0.5 rounded bg-zinc-100 dark:bg-zinc-800 text-zinc-800 dark:text-zinc-300 text-xs font-semibold">需要觀察</span></td>
              <td class="px-4 py-3 font-sans text-xs">SaaS行業低迷期，觀望。支撐 $230。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold font-sans text-zinc-900 dark:text-zinc-100">ADBE</td>
              <td class="px-4 py-3 text-right text-rose-500 font-semibold">$195.29 (-4.81%)</td>
              <td class="px-4 py-3 font-sans">大跌跌破 $200 心理關卡與 200MA</td>
              <td class="px-4 py-3 font-sans"><span class="px-2 py-0.5 rounded bg-amber-100 dark:bg-amber-950 text-amber-800 dark:text-amber-350 text-xs font-semibold">回踩支撐</span></td>
              <td class="px-4 py-3 font-sans text-xs">SaaS集體失血所致。關鍵防守 $190，壓力 $205。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold font-sans text-zinc-900 dark:text-zinc-100">PLTR</td>
              <td class="px-4 py-3 text-right text-emerald-500 font-semibold">$130.63 (+0.42%)</td>
              <td class="px-4 py-3 font-sans">微幅震盪反彈，守穩 20MA</td>
              <td class="px-4 py-3 font-sans"><span class="px-2 py-0.5 rounded bg-zinc-100 dark:bg-zinc-800 text-zinc-800 dark:text-zinc-300 text-xs font-semibold">需要觀察</span></td>
              <td class="px-4 py-3 font-sans text-xs">防守 20MA 平台支撐 $128。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold font-sans text-zinc-900 dark:text-zinc-100">LITE</td>
              <td class="px-4 py-3 text-right text-rose-500 font-semibold">$873.15 (-4.29%)</td>
              <td class="px-4 py-3 font-sans">跟隨光通信回檔，測試底軌</td>
              <td class="px-4 py-3 font-sans"><span class="px-2 py-0.5 rounded bg-amber-100 dark:bg-amber-950 text-amber-800 dark:text-amber-350 text-xs font-semibold">回踩支撐</span></td>
              <td class="px-4 py-3 font-sans text-xs">回調蓄勢。支撐 $865，阻力 $900。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold font-sans text-zinc-900 dark:text-zinc-100">COHR</td>
              <td class="px-4 py-3 text-right text-emerald-500 font-semibold">$381.12 (+1.39%)</td>
              <td class="px-4 py-3 font-sans">光器件跟漲，重回 10MA</td>
              <td class="px-4 py-3 font-sans"><span class="px-2 py-0.5 rounded bg-zinc-100 dark:bg-zinc-800 text-zinc-800 dark:text-zinc-300 text-xs font-semibold">需要觀察</span></td>
              <td class="px-4 py-3 font-sans text-xs">支撐 $372，壓力 $392。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold font-sans text-zinc-900 dark:text-zinc-100">ANET</td>
              <td class="px-4 py-3 text-right text-emerald-500 font-semibold">$169.72 (+2.41%)</td>
              <td class="px-4 py-3 font-sans">帶量反彈，沿 5MA 走強，逼近高點</td>
              <td class="px-4 py-3 font-sans"><span class="px-2 py-0.5 rounded bg-emerald-100 dark:bg-emerald-950 text-emerald-800 dark:text-emerald-350 text-xs font-semibold">繼續強勢</span></td>
              <td class="px-4 py-3 font-sans text-xs">電網網路基建前景看好。支撐 $162，目標挑戰 $175。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold font-sans text-zinc-900 dark:text-zinc-100">FLNC</td>
              <td class="px-4 py-3 text-right text-emerald-500 font-semibold">$22.62 (+1.39%)</td>
              <td class="px-4 py-3 font-sans">微幅反彈，隨儲能板塊人氣回升</td>
              <td class="px-4 py-3 font-sans"><span class="px-2 py-0.5 rounded bg-zinc-100 dark:bg-zinc-800 text-zinc-800 dark:text-zinc-300 text-xs font-semibold">需要觀察</span></td>
              <td class="px-4 py-3 font-sans text-xs">儲能概念中性整理。支撐 $21.8。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold font-sans text-zinc-900 dark:text-zinc-100">OKLO</td>
              <td class="px-4 py-3 text-right text-emerald-500 font-semibold">$61.17 (+3.38%)</td>
              <td class="px-4 py-3 font-sans">突破盤整阻力，跟隨核能基建主線走強</td>
              <td class="px-4 py-3 font-sans"><span class="px-2 py-0.5 rounded bg-emerald-100 dark:bg-emerald-950 text-emerald-800 dark:text-emerald-350 text-xs font-semibold">繼續強勢</span></td>
              <td class="px-4 py-3 font-sans text-xs">核能政策預期強烈。支撐 $58，阻力 $65。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold font-sans text-zinc-900 dark:text-zinc-100">VST</td>
              <td class="px-4 py-3 text-right text-emerald-500 font-semibold">$163.33 (+6.42%)</td>
              <td class="px-4 py-3 font-sans">多頭帶量噴出，再創收盤歷史最高價</td>
              <td class="px-4 py-3 font-sans"><span class="px-2 py-0.5 rounded bg-emerald-100 dark:bg-emerald-950 text-emerald-800 dark:text-emerald-350 text-xs font-semibold">繼續強勢</span></td>
              <td class="px-4 py-3 font-sans text-xs">德州資料中心購電合約推進。支撐 $152，目標 $170。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold font-sans text-zinc-900 dark:text-zinc-100">CEG</td>
              <td class="px-4 py-3 text-right text-emerald-500 font-semibold">$274.08 (+7.97%)</td>
              <td class="px-4 py-3 font-sans">大漲突破箱體創歷史新高，買盤極為熾烈</td>
              <td class="px-4 py-3 font-sans"><span class="px-2 py-0.5 rounded bg-emerald-100 dark:bg-emerald-950 text-emerald-800 dark:text-emerald-350 text-xs font-semibold">繼續強勢</span></td>
              <td class="px-4 py-3 font-sans text-xs">微軟核電購電合約激勵。支撐 $262，阻力 $285。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold font-sans text-zinc-900 dark:text-zinc-100">ETN</td>
              <td class="px-4 py-3 text-right text-emerald-500 font-semibold">$421.77 (+3.13%)</td>
              <td class="px-4 py-3 font-sans">多頭爆發創高，沿 5MA 繼續走強</td>
              <td class="px-4 py-3 font-sans"><span class="px-2 py-0.5 rounded bg-emerald-100 dark:bg-emerald-950 text-emerald-800 dark:text-emerald-350 text-xs font-semibold">繼續強勢</span></td>
              <td class="px-4 py-3 font-sans text-xs">電網變壓器短缺推高利潤。支撐 $412。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold font-sans text-zinc-900 dark:text-zinc-100">VRT</td>
              <td class="px-4 py-3 text-right text-emerald-500 font-semibold">$330.32 (+6.72%)</td>
              <td class="px-4 py-3 font-sans">爆發式暴漲創歷史新高，液冷需求大熱</td>
              <td class="px-4 py-3 font-sans"><span class="px-2 py-0.5 rounded bg-emerald-100 dark:bg-emerald-950 text-emerald-800 dark:text-emerald-350 text-xs font-semibold">繼續強勢</span></td>
              <td class="px-4 py-3 font-sans text-xs">伺服器液冷冷卻龍頭地位穩固。支撐 $315，阻力看 $350。</td>
            </tr>
          </tbody>
        </table>
      </div>
    </section>

    <!-- 13. 明日交易計畫 / 觀察清單 -->
    <section id="trading-plan" class="mb-12 scroll-mt-6">
      <h2 class="text-2xl font-bold mb-4 flex items-center gap-2 border-b border-zinc-100 dark:border-zinc-800 pb-2">
        <span class="text-brand-500">13.</span> 明日交易計畫 / 觀察清單
      </h2>
      <div class="space-y-4 text-sm sm:text-base leading-relaxed text-zinc-650 dark:text-zinc-400">
        <p><strong>13.1 宏觀觀察：</strong>由於週五休市，緊密監控下週一美債收益率在 4.84% 與 4.46% 位置的穩健度，以及原油價格是否會在地緣政治危機降溫下繼續下試低點，從而徹底緩解全球滯脹隱憂。</p>
        <p><strong>13.2 大盤觀察：</strong>關注標普 500 指數是否能站穩 7500 點整數大關，形成多頭新支撐；而創下歷史收盤新高的 QQQ 與費城半導體指數，需留意超買指標高位降溫，慎防短線衝高回落。</p>
        <p><strong>13.3 板塊與個股觀察：</strong>
          <ul class="list-disc pl-5 space-y-2 mt-2">
            <li><strong>Intel (INTC) &amp; TSM (台積電):</strong> Apple-Intel 消息的具體代工進程與實質訂單確認是半導體主線最核心的催化劑。</li>
            <li><strong>CEG (星座能源) &amp; VRT (維諦):</strong> 電力及液冷散熱雙雄作為牛市剛性大熱點，若出現回踩 5MA/10MA 機會是強勢跟進配置首選。</li>
            <li><strong>CRM &amp; NOW:</strong> SaaS 軟體出現結構性破位下探，短期內需嚴防「接飛刀」風險，在均線未企穩前避免左側抄底。</li>
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
              <td class="px-4 py-3 font-semibold">宏觀利率風險</td>
              <td class="px-4 py-3 text-center"><span class="px-2 py-0.5 rounded bg-rose-100 dark:bg-rose-950 text-rose-800 dark:text-rose-350 text-xs font-semibold">高</span></td>
              <td class="px-4 py-3 text-zinc-500 dark:text-zinc-400 text-xs sm:text-sm leading-relaxed">雖然地緣政治好轉拖累油價大跌，但聯準會偏鷹立場表明利率仍將在「更高更長」位置徘徊，高負債 SaaS 軟體與小盤成長股仍面臨沉重折現估值壓力。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold">行業板塊輪動</td>
              <td class="px-4 py-3 text-center"><span class="px-2 py-0.5 rounded bg-amber-100 dark:bg-amber-950 text-amber-800 dark:text-amber-350 text-xs font-semibold">中高</span></td>
              <td class="px-4 py-3 text-zinc-500 dark:text-zinc-400 text-xs sm:text-sm leading-relaxed">當前資金瘋狂抽離高估值 SaaS 並轉移至晶片和電力基建，板塊分化走向極端。若資金流出加劇，可能誘發軟體板塊個股面臨去槓桿踐踏破位。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold">AI 超買與擁擠度</td>
              <td class="px-4 py-3 text-center"><span class="px-2 py-0.5 rounded bg-amber-100 dark:bg-amber-950 text-amber-800 dark:text-amber-350 text-xs font-semibold">中高</span></td>
              <td class="px-4 py-3 text-zinc-500 dark:text-zinc-400 text-xs sm:text-sm leading-relaxed">費半與電力基建 (VST, CEG) 今日大爆發，SMH 指數 RSI 突破 72 進入超買區。短線籌碼高度擁擠，假期後需防範部分高位利多兌現的大洗盤。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold">地緣政策落差</td>
              <td class="px-4 py-3 text-center"><span class="px-2 py-0.5 rounded bg-zinc-100 dark:bg-zinc-800 text-zinc-800 dark:text-zinc-300 text-xs font-semibold">中</span></td>
              <td class="px-4 py-3 text-zinc-500 dark:text-zinc-400 text-xs sm:text-sm leading-relaxed">美伊雖然簽署臨時和平協議，但仍需關注霍爾木茲海峽的實際通航數據，且特朗普的爆料並未獲得 Apple 及 Intel 官方正式證實。</td>
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
        <p><strong>今日市場結論：</strong>週四美股呈現強烈的報復性反彈與結構性大輪動。美伊敲定臨時和平框架協議引導油價崩跌，大為緩解通膨預期；特朗普透露的 Apple 與 Intel 晶片合作引爆了半導體國產化製造與代工的買盤，費半暴漲 6.42% 創高。雖然標普 500 指數與 QQQ 均上漲並收復 7500，但應用軟體 SaaS 板塊由於企業雲端預算縮減以及利率高企重創大跌。大盤牛市格局在板塊汰弱留強中展現其韌性。</p>
        <p><strong>當前市場階段：</strong><span class="text-emerald-500 font-semibold">強趨勢反彈 / 板塊極端分化輪動。</span></p>
        <p><strong>我的操作傾向：</strong>中性偏樂觀但具備結構防禦。在降息受限、油價大跌的宏觀背景下，避開估值過高且失去支持的 SaaS 軟體；適度在回調時分批建倉配置有強勁業績支撐的晶片巨頭 (Intel, TSM) 以及剛性供電與液冷基建雙龍頭 (CEG, VRT, VST)。</p>
        
        <div class="mt-4 p-4 rounded-xl border border-zinc-200 dark:border-zinc-800 bg-zinc-50/50 dark:bg-zinc-900/50">
          <h4 class="font-bold text-zinc-800 dark:text-zinc-200 mb-2">下週一開盤最值得關注的 5 個訊號</h4>
          <ol class="list-decimal pl-5 space-y-2 text-xs sm:text-sm font-mono text-zinc-600 dark:text-zinc-400">
            <li><strong>Apple &amp; Intel 官方澄清聲明：</strong>是否會發出澄清或正式確認晶片代工合同，此將決定晶片股走勢。</li>
            <li><strong>WTI 原油價格：</strong>是否能站穩 $74/桶，原油走勢將決定通膨焦慮是否會徹底消退。</li>
            <li><strong>QQQ 歷史新高平台：</strong>QQQ 能否頂住利率高企壓力站穩 $740 新高平台。</li>
            <li><strong>SaaS 板塊 (IGV) 止跌信號：</strong>Salesforce (CRM) 能否在 $150 關卡止跌企穩。</li>
            <li><strong>美債 2Y 與 10Y 收益率：</strong>是否會進一步下滑，舒緩科技成長股與小盤股的估值壓力。</li>
          </ol>
        </div>
      </div>
    </section>

  </main>
</div>

<!-- Theme toggle script -->
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
    // Dispatch event to redraw mermaid if needed
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
        label: '當日漲跌幅 (%)',
        data: [0.14, 1.08, 1.91, 1.08, 2.12, 6.42, 4.57],
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

# Save this HTML to reports/2026-06-18-us-stock-closing-daily-report.html inside /Users/wisdom/html-report-skill
target_dir = "/Users/wisdom/html-report-skill/reports"
os.makedirs(target_dir, exist_ok=True)
target_path = os.path.join(target_dir, "2026-06-18-us-stock-closing-daily-report.html")

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
exists = any(item.get("file") == "2026-06-18-us-stock-closing-daily-report.html" for item in manifest)
if not exists:
    new_entry = {
      "file": "2026-06-18-us-stock-closing-daily-report.html",
      "title": "美股收盤日報｜2026-06-18",
      "date": "2026-06-18",
      "description": "美伊敲定和平協議引油價大跌，Intel攜手Apple晶片代工合作引爆晶片狂潮！費半暴漲6.42%，標普重登7500點，三大指數強勢反彈，電力基建及液冷散熱持續改寫歷史新高。"
    }
    manifest.insert(0, new_entry)
    with open(manifest_path, "w", encoding="utf-8") as f:
        json.dump(manifest, f, ensure_ascii=False, indent=2)
    print(f"Updated manifest.json successfully at: {manifest_path}")
else:
    print("manifest.json already contains the entry for 2026-06-18.")
