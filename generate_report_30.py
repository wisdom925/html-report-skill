import os
import json

html_content = """<!doctype html>
<html lang="zh-TW" class="scroll-smooth">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <title>美股收盤日報｜2026-06-01</title>
  <meta name="description" content="2026年6月1日美股收盤日報：標普與納指同創收盤歷史新高！輝達 (Nvidia) 創辦人黃仁勳在台北 Computex 發表重磅 RTX Spark 與 Vera Rubin 新晶片平台，股價狂飆 6.26% 領航 AI 算力基建。中東地緣衝突升溫導致 WTI 原油狂飆 4.8% 至 $93.50，美債收益率與美元同步走高，Meta 執行高管減持暴跌 5.10%，特斯拉因過估值與需求放緩回撤 4.54%。">
  <meta property="og:title" content="美股收盤日報｜2026-06-01">
  <meta property="og:description" content="輝達黃仁勳重磅 AI 晶片引爆算力狂潮，標普納指同創歷史收盤新高！地緣局勢緊張致油價與美債利率拉升，Meta 暴跌 5.1%，特斯拉跌 4.5%，市場寬度收窄演繹極限輪動。">
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
        <span class="text-sm text-zinc-500"><time datetime="2026-06-01">2026-06-01 (星期一)</time></span>
      </div>
      <h1 class="text-4xl font-extrabold tracking-tight mb-4 grad-text">美股收盤日報｜2026-06-01</h1>
      <p class="text-xl text-zinc-600 dark:text-zinc-400">標普與納指同創歷史收盤新高！輝達 (Nvidia) 創辦人黃仁勳在台北 Computex 發表重磅 RTX Spark 超級 PC 晶片與下一代 Vera Rubin AI 算力平台，刺激股價暴漲 6.26%，引領半導體及微軟大漲。中東地緣局勢緊張激發油價飆升 4.8%，美債收益率上行至 4.475%，Meta 執行高管減持暴跌 5.10%，特斯拉因過估值與需求放緩回撤 4.54%。</p>
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
              指數續創高、內部現分化；AI 晶片與能源護盤，高估值與個別利空股承受回吐壓力。
            </p>
          </div>
          <div class="space-y-2">
            <p class="text-sm font-semibold text-zinc-400">核心驅動因素</p>
            <p class="text-sm text-zinc-600 dark:text-zinc-300">
              台北 Computex 2026 於本周開幕，輝達創辦人黃仁勳星期日發表主線演講，正式揭曉 Arm 架構 RTX Spark 超級電腦晶片與即將量產的 Vera Rubin AI 平台，激勵股價暴衝 6.26% 引領科技股上攻。然而，美國 5 月 ISM 製造業 PMI 升至 54.0% 超出預期，促使美債 10 年期收益率拉升至 4.475%，加上中東局勢突然惡化，地緣政治風險令 WTI 原油暴漲 4.8% 突破 $93.50，高利率與通膨焦慮令小盤股 (Russell 2000) 翻綠。與此同時，Meta 受高管執行預先減持打擊重挫 5.10%，特斯拉因過估值與銷售放緩下挫 4.54%，限制了大盤漲幅。
            </p>
          </div>
        </div>
        <hr class="border-zinc-200 dark:border-zinc-800">
        <ul class="list-disc pl-5 space-y-2 text-zinc-600 dark:text-zinc-300">
          <li><strong>大盤趨勢：</strong>美股三大指數呈現分化偏強走勢，標普 500 收漲 0.26% 報 7,599.96 點，納斯達克漲 0.42% 報 27,086.81 點，雙雙刷新收盤歷史新高，標普盤中首度突破 7,600 大關；道指微升 0.09% 報 51,078.94 點，維持在 51,000 點上方。小盤股指數 (Russell 2000) 跌 0.47% 跑輸。</li>
          <li><strong>資金態度：</strong>資金高度聚焦高確定性的 AI 龍頭（Nvidia、博通）及對沖通膨的能源板塊（XLE）。由於美債利率上行與地緣升溫，小盤股、房地產與公用事業受到資金流出擠壓。</li>
          <li><strong>市場寬度：</strong>指數強而寬度偏弱。NYSE 與 Nasdaq 的下跌家數皆大於上漲家數，主力資金主要在半導體與石油巨頭抱團，市場參與度呈現一定程度的收窄。</li>
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
                <td class="px-4 py-3 text-right">51,078.94</td>
                <td class="px-4 py-3 text-right text-emerald-500 font-semibold">+0.09%</td>
                <td class="px-4 py-3 text-right">50,767.32 - 51,161.10</td>
                <td class="px-4 py-3 text-left font-sans text-xs">維持高位震盪，守穩 51,000 大關與短期均線。</td>
              </tr>
              <tr>
                <td class="px-4 py-3 font-semibold font-sans text-zinc-900 dark:text-zinc-100">S&P 500</td>
                <td class="px-4 py-3 text-right">7,599.96</td>
                <td class="px-4 py-3 text-right text-emerald-500 font-semibold">+0.26%</td>
                <td class="px-4 py-3 text-right">7,562.61 - 7,599.96</td>
                <td class="px-4 py-3 text-left font-sans text-xs text-emerald-500">歷史收盤新高！站在所有主要均線之上，強勢多頭結構。</td>
              </tr>
              <tr>
                <td class="px-4 py-3 font-semibold font-sans text-zinc-900 dark:text-zinc-100">Nasdaq Composite</td>
                <td class="px-4 py-3 text-right">27,086.81</td>
                <td class="px-4 py-3 text-right text-emerald-500 font-semibold">+0.42%</td>
                <td class="px-4 py-3 text-right">26,913.12 - 27,190.21</td>
                <td class="px-4 py-3 text-left font-sans text-xs text-emerald-500">歷史收盤新高！輝達大漲帶動，加速上行突破。</td>
              </tr>
              <tr>
                <td class="px-4 py-3 font-semibold font-sans text-zinc-900 dark:text-zinc-100">Nasdaq 100 / QQQ</td>
                <td class="px-4 py-3 text-right">22,250.00</td>
                <td class="px-4 py-3 text-right text-emerald-500 font-semibold">+0.55%</td>
                <td class="px-4 py-3 text-right">22,120.00 - 22,350.00</td>
                <td class="px-4 py-3 text-left font-sans text-xs text-emerald-500">歷史收盤新高！極度強勢，受晶片與微軟力挺跑贏。</td>
              </tr>
              <tr>
                <td class="px-4 py-3 font-semibold font-sans text-zinc-900 dark:text-zinc-100">Russell 2000 / IWM</td>
                <td class="px-4 py-3 text-right">2,905.76</td>
                <td class="px-4 py-3 text-right text-rose-500 font-semibold">-0.47%</td>
                <td class="px-4 py-3 text-right">2,895.10 - 2,925.20</td>
                <td class="px-4 py-3 text-left font-sans text-xs">小幅回踩，受美債長端利率攀升與通膨壓力壓抑。</td>
              </tr>
              <tr>
                <td class="px-4 py-3 font-semibold font-sans text-zinc-900 dark:text-zinc-100">SOX 半導體指數</td>
                <td class="px-4 py-3 text-right">12,965.65</td>
                <td class="px-4 py-3 text-right text-emerald-500 font-semibold">+1.06%</td>
                <td class="px-4 py-3 text-right">12,820.40 - 13,010.50</td>
                <td class="px-4 py-3 text-left font-sans text-xs text-emerald-500">強勁長陽線，逼近前高，Computex 催化最火熱賽道。</td>
              </tr>
              <tr>
                <td class="px-4 py-3 font-semibold font-sans text-zinc-900 dark:text-zinc-100">VIX 恐慌指數</td>
                <td class="px-4 py-3 text-right">15.99</td>
                <td class="px-4 py-3 text-right text-emerald-500 font-semibold">+4.80%</td>
                <td class="px-4 py-3 text-right">15.20 - 16.20</td>
                <td class="px-4 py-3 text-left font-sans text-xs">低位回升，反映中東局勢不確定性及對沖期權交易。</td>
              </tr>
            </tbody>
          </table>
        </div>
        <div class="stat-card flex flex-col justify-between">
          <div>
            <h4 class="font-bold text-zinc-800 dark:text-zinc-200">當日指數回報動態對比</h4>
            <p class="text-xs text-zinc-400 mt-1">反映各主要指數的單日相對強弱程度，半導體與科技股明顯占優。</p>
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
        <p class="text-sm text-zinc-500 mb-4 font-bold text-center">資金情緒與地緣變局流向圖：</p>
        <div class="mermaid text-center" id="rotation-flow">
          graph LR
            Computex[Computex台北開幕] -->|黃仁勳重磅AI新品| NVDA[輝達狂飆6.26%與博通大漲]
            ISM[美國5月ISM PMI達54.0] -->|製造業強勁擴張| Yields[10Y美債收益率升至4.475%]
            MiddleEast[以色列地緣衝突擴大] -->|中東局勢再告急| Oil[WTI原油狂噴4.8%至$93.50]
            Yields & Oil -->|壓低中小盤與高估值股| Retrace[特斯拉下挫與Meta暴跌]
            NVDA & XLE[能源大漲3.1%] -->|雙核巨頭護盤| S_P[標普/納指收盤同創歷史新高]
        </div>
      </div>

      <div class="relative border-l-2 border-zinc-200 dark:border-zinc-800 ml-4 pl-8 space-y-8">
        <div class="relative">
          <span class="absolute -left-10 top-1.5 flex h-8 w-8 items-center justify-center rounded-full bg-brand-50 dark:bg-brand-500/10 text-brand-600 dark:text-brand-400 font-bold border border-brand-200 dark:border-brand-500/20 text-xs">開盤</span>
          <h3 class="text-lg font-bold text-zinc-800 dark:text-zinc-200">09:30 AM — 輝達 Computex 效應激發高開，大算力領漲</h3>
          <p class="text-sm text-zinc-600 dark:text-zinc-400 mt-1">
            三大指數開盤齊漲。市場極度興奮於黃仁勳在 Computex 上展示的「RTX Spark」超級 PC 晶片與宣布 Rubin 平台的量產計畫，輝達 (NVDA) 跳空高開 3% 展現主宰力，帶領費半指數快速衝高。微軟 (MSFT) 同步走強，充當多頭另一核心。
          </p>
        </div>
        <div class="relative">
          <span class="absolute -left-10 top-1.5 flex h-8 w-8 items-center justify-center rounded-full bg-brand-50 dark:bg-brand-500/10 text-brand-600 dark:text-brand-400 font-bold border border-brand-200 dark:border-brand-500/20 text-xs">數據</span>
          <h3 class="text-lg font-bold text-zinc-800 dark:text-zinc-200">10:00 AM — 製造業 PMI 超預期，美債利率拉升，板塊迅速分化</h3>
          <p class="text-sm text-zinc-600 dark:text-zinc-400 mt-1">
            ISM 製造業 PMI 公布為 54.0%，大幅好於預期的 53.0% 並創兩年來新高。雖然證實美國實體經濟的強韌度，但其分項價格指數反彈使市場對聯準會的降息預期再度降溫。10 年期美債收益率從 4.45% 拉升至 4.475%。高負債的中小盤股 (Russell 2000) 隨即翻綠。
          </p>
        </div>
        <div class="relative">
          <span class="absolute -left-10 top-1.5 flex h-8 w-8 items-center justify-center rounded-full bg-brand-50 dark:bg-brand-500/10 text-brand-600 dark:text-brand-400 font-bold border border-brand-200 dark:border-brand-500/20 text-xs">突發</span>
          <h3 class="text-lg font-bold text-zinc-800 dark:text-zinc-200">01:30 PM — 中東地緣衝突驟然升級，原油飆升引導避險</h3>
          <p class="text-sm text-zinc-600 dark:text-zinc-400 mt-1">
            中東地緣局勢再度爆發，市場傳出以色列擴大在黎巴嫩的軍事行動，使美伊間的停火草案面臨破裂危險。WTI 原油狂噴 4.8% 一舉突破 $93.50，能源板塊 (XLE) 應聲暴漲。避險情緒帶動美元指數走強。
          </p>
        </div>
        <div class="relative">
          <span class="absolute -left-10 top-1.5 flex h-8 w-8 items-center justify-center rounded-full bg-brand-50 dark:bg-brand-500/10 text-brand-600 dark:text-brand-400 font-bold border border-brand-200 dark:border-brand-500/20 text-xs">尾盤</span>
          <h3 class="text-lg font-bold text-zinc-800 dark:text-zinc-200">04:00 PM — 輝達狂飆 6.26% 頂天立地，標普與納指創收盤新高</h3>
          <p class="text-sm text-zinc-600 dark:text-zinc-400 mt-1">
            尾盤多頭部隊在輝達 (NVDA 收漲 6.26% 報 $224.36) 與博通 (AVGO +2.41%) 等大算力晶片股中瘋狂抱團，抵消了 Meta (-5.10% 高管減持) 與特斯拉 (-4.54%) 的暴跌拖累。標普 500 最終收在 7,599.96 點，納指亦同創歷史收盤最高。
          </p>
        </div>
      </div>
    </section>

    <!-- 3. 宏觀環境 -->
    <section id="macro" class="mb-12 scroll-mt-6">
      <h2 class="text-2xl font-bold mb-4 flex items-center gap-2 border-b border-zinc-100 dark:border-zinc-800 pb-2">
        <span class="text-brand-500">3.</span> 宏觀環境分析
      </h2>

      <div class="tabs border border-zinc-200 dark:border-zinc-800 rounded-xl overflow-hidden bg-zinc-50/50 dark:bg-zinc-900/50 p-4">
        <input type="radio" id="tab-yield" name="macro-tabs" checked>
        <label for="tab-yield" class="hover:text-brand-500">美債收益率</label>

        <input type="radio" id="tab-fed" name="macro-tabs">
        <label for="tab-fed" class="hover:text-brand-500">Fed 降息預期</label>

        <input type="radio" id="tab-commodities" name="macro-tabs">
        <label for="tab-commodities" class="hover:text-brand-500">大宗及加密貨幣</label>

        <input type="radio" id="tab-data" name="macro-tabs">
        <label for="tab-data" class="hover:text-brand-500">重要經濟數據</label>

        <!-- Panel 1 -->
        <div class="tab-panel border-t border-zinc-200 dark:border-zinc-800 mt-2">
          <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
            <div class="stat-card">
              <span class="text-xs font-semibold text-zinc-400 uppercase">2年期美債收益率</span>
              <div class="text-2xl font-bold font-mono mt-1">4.050%</div>
              <span class="text-xs text-rose-500 font-semibold">↑ 4.0 bps</span>
            </div>
            <div class="stat-card">
              <span class="text-xs font-semibold text-zinc-400 uppercase">10年期美債收益率</span>
              <div class="text-2xl font-bold font-mono mt-1">4.475%</div>
              <span class="text-xs text-rose-500 font-semibold">↑ 2.5 bps</span>
            </div>
            <div class="stat-card">
              <span class="text-xs font-semibold text-zinc-400 uppercase">30年期美債收益率</span>
              <div class="text-2xl font-bold font-mono mt-1">4.990%</div>
              <span class="text-xs text-rose-500 font-semibold">↑ 38.0 bps</span>
            </div>
          </div>
          <p class="text-sm text-zinc-600 dark:text-zinc-400 mt-4 leading-relaxed">
            <strong>市場含義：</strong>收益率曲線因製造業景氣度走強與地緣政治風險而顯著陡峭化 (Bear Steepening)，特別是 30 年期長端國債在財政赤字規模焦慮與避險通膨定價中突破至 4.99%。雖然 10 年期美債利率小幅上揚至 4.475% 對高倍數科技板塊帶來少許擾動，但超預期的製造業 PMI 與輝達 Computex 晶片引導的極端高確定性，依然成功壓倒了利率上行壓力。
          </p>
        </div>

        <!-- Panel 2 -->
        <div class="tab-panel border-t border-zinc-200 dark:border-zinc-800 mt-2">
          <div class="space-y-4">
            <div class="p-4 bg-zinc-100 dark:bg-zinc-900 rounded-lg">
              <h4 class="font-bold text-zinc-800 dark:text-zinc-200">經濟擴張拉長 Higher-For-Longer 利率週期：</h4>
              <p class="text-sm text-zinc-600 dark:text-zinc-300 mt-2">
                強勁的 5 月製造業 PMI 數據與地緣政治帶來的潛在原油二次通膨壓力，促使市場對於近幾個月的降息定價幾乎消退。
                <br>• <strong>CME FedWatch 定價：</strong>6 月 16-17 日 FOMC 利率維持在 3.50%-3.75% 區間的機率為 99.0%。年內降息預期已被向後推遲至 11 月和 12 月。聯準會官員的發言預計將持續維持鷹派，以壓制任何二次通膨的火苗。
              </p>
            </div>
          </div>
        </div>

        <!-- Panel 3 -->
        <div class="tab-panel border-t border-zinc-200 dark:border-zinc-800 mt-2">
          <div class="grid grid-cols-2 md:grid-cols-4 gap-4">
            <div class="stat-card">
              <span class="text-xs font-semibold text-zinc-400">美元指數 (DXY)</span>
              <div class="text-xl font-bold font-mono mt-1">99.16</div>
              <span class="text-xs text-emerald-500">↑ 0.07%</span>
            </div>
            <div class="stat-card">
              <span class="text-xs font-semibold text-zinc-400">黃金現貨 (Gold)</span>
              <div class="text-xl font-bold font-mono mt-1">$4,520.00</div>
              <span class="text-xs text-rose-500">↓ 0.20%</span>
            </div>
            <div class="stat-card">
              <span class="text-xs font-semibold text-zinc-400">WTI 原油 (WTI)</span>
              <div class="text-xl font-bold font-mono mt-1">$93.50</div>
              <span class="text-xs text-emerald-500">↑ 4.80%</span>
            </div>
            <div class="stat-card">
              <span class="text-xs font-semibold text-zinc-400">比特幣 (BTC)</span>
              <div class="text-xl font-bold font-mono mt-1">$71,200</div>
              <span class="text-xs text-rose-500">↓ 3.30%</span>
            </div>
          </div>
          <p class="text-sm text-zinc-600 dark:text-zinc-400 mt-4 leading-relaxed">
            <strong>市場含義：</strong>地緣政治是今日大宗商品的绝对主宰。以色列在黎巴嫩境內的軍事行動擴大，引發 WTI 原油狂噴 4.8% 至 $93.50，極大地加劇了通膨擔憂。強勢美元 (DXY 上探 99.16) 和 10 年期美債利率走高，限制了黃金的反彈步伐。比特幣 (BTC) 則因避險情緒的上升，高位遭遇獲利了結而下跌 3.3% 盤整至 $71,200。
          </p>
        </div>

        <!-- Panel 4 -->
        <div class="tab-panel border-t border-zinc-200 dark:border-zinc-800 mt-2">
          <div class="overflow-x-auto">
            <table class="min-w-full divide-y divide-zinc-200 dark:divide-zinc-800 text-sm">
              <thead class="bg-zinc-50 dark:bg-zinc-900">
                <tr>
                  <th class="px-4 py-2 text-left font-semibold text-zinc-600 dark:text-zinc-400">數據項目</th>
                  <th class="px-4 py-2 text-center font-semibold text-zinc-600 dark:text-zinc-400">公佈值</th>
                  <th class="px-4 py-2 text-center font-semibold text-zinc-600 dark:text-zinc-400">預期值</th>
                  <th class="px-4 py-2 text-center font-semibold text-zinc-600 dark:text-zinc-400">前值</th>
                  <th class="px-4 py-2 text-left font-semibold text-zinc-600 dark:text-zinc-400">市場解讀</th>
                </tr>
              </thead>
              <tbody class="divide-y divide-zinc-200 dark:divide-zinc-800 font-mono">
                <tr>
                  <td class="px-4 py-2 text-zinc-900 dark:text-zinc-100 font-sans">美國5月ISM製造業PMI</td>
                  <td class="px-4 py-2 text-center font-semibold text-emerald-500">54.0%</td>
                  <td class="px-4 py-2 text-center">53.0%</td>
                  <td class="px-4 py-2 text-center">52.7%</td>
                  <td class="px-4 py-2 text-left font-sans text-xs text-zinc-500">連續第5個月保持擴張，新訂單 (56.8%) 與產出 (54.3%) 強勁，但價格指數回升印證通膨粘性。</td>
                </tr>
              </tbody>
            </table>
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
              <td class="px-4 py-3 text-right font-mono text-emerald-500 font-semibold" data-val="3.10">+3.10%</td>
              <td class="px-4 py-3 text-right font-mono" data-val="2.50">+2.50%</td>
              <td class="px-4 py-3 text-right font-mono" data-val="-2.10">-2.10%</td>
              <td class="px-4 py-3 text-xs">中東衝突驟然升級推動 WTI 原油暴漲 4.8%，石油巨頭集體大爆發。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-medium">2</td>
              <td class="px-4 py-3 font-medium">資訊科技 (Information Technology)</td>
              <td class="px-4 py-3 font-mono">XLK</td>
              <td class="px-4 py-3 text-right font-mono text-emerald-500 font-semibold" data-val="0.80">+0.80%</td>
              <td class="px-4 py-3 text-right font-mono" data-val="3.20">+3.20%</td>
              <td class="px-4 py-3 text-right font-mono" data-val="18.50">+18.50%</td>
              <td class="px-4 py-3 text-xs">輝達黃仁勳 Computex 發表重磅 RTX Spark 與 Vera Rubin 激勵股價暴狂飆 6.26%，微軟大漲護航。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-medium">3</td>
              <td class="px-4 py-3 font-medium">原材料 (Materials)</td>
              <td class="px-4 py-3 font-mono">XLB</td>
              <td class="px-4 py-3 text-right font-mono text-emerald-500 font-semibold" data-val="0.30">+0.30%</td>
              <td class="px-4 py-3 text-right font-mono" data-val="0.80">+0.80%</td>
              <td class="px-4 py-3 text-right font-mono" data-val="-1.20">-1.20%</td>
              <td class="px-4 py-3 text-xs">ISM 製造業 PMI 優於預期，實體工業金屬需求預期向好。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-medium">4</td>
              <td class="px-4 py-3 font-medium">日常消費品 (Consumer Staples)</td>
              <td class="px-4 py-3 font-mono">XLP</td>
              <td class="px-4 py-3 text-right font-mono text-emerald-500 font-semibold" data-val="0.20">+0.20%</td>
              <td class="px-4 py-3 text-right font-mono" data-val="0.40">+0.40%</td>
              <td class="px-4 py-3 text-right font-mono" data-val="1.50">+1.50%</td>
              <td class="px-4 py-3 text-xs">市場在高位劇烈波動，部分防禦性低風險資金買入大消費避險。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-medium">5</td>
              <td class="px-4 py-3 font-medium">金融 (Financials)</td>
              <td class="px-4 py-3 font-mono">XLF</td>
              <td class="px-4 py-3 text-right font-mono text-emerald-500 font-semibold" data-val="0.10">+0.10%</td>
              <td class="px-4 py-3 text-right font-mono" data-val="0.20">+0.20%</td>
              <td class="px-4 py-3 text-right font-mono" data-val="0.80">+0.80%</td>
              <td class="px-4 py-3 text-xs">利率上行擴大商業銀行利差利好，但地緣政治避險情緒限制了漲幅。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-medium">6</td>
              <td class="px-4 py-3 font-medium">工業 (Industrials)</td>
              <td class="px-4 py-3 font-mono">XLI</td>
              <td class="px-4 py-3 text-right font-mono text-emerald-500 font-semibold" data-val="0.10">+0.10%</td>
              <td class="px-4 py-3 text-right font-mono" data-val="0.50">+0.50%</td>
              <td class="px-4 py-3 text-right font-mono" data-val="1.20">+1.20%</td>
              <td class="px-4 py-3 text-xs">ISM 生產分項 (54.3%) 走高，對航空製造與重工基建帶來局部買盤。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-medium">7</td>
              <td class="px-4 py-3 font-medium">醫療保健 (Health Care)</td>
              <td class="px-4 py-3 font-mono">XLV</td>
              <td class="px-4 py-3 text-right font-mono text-rose-500 font-semibold" data-val="-0.30">-0.30%</td>
              <td class="px-4 py-3 text-right font-mono" data-val="-0.20">-0.20%</td>
              <td class="px-4 py-3 text-right font-mono" data-val="0.50">+0.50%</td>
              <td class="px-4 py-3 text-xs">市場在大算力主線下極為分化，醫療防禦板塊缺乏熱度，小幅失血。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-medium">8</td>
              <td class="px-4 py-3 font-medium">非必需消費品 (Consumer Discretionary)</td>
              <td class="px-4 py-3 font-mono">XLY</td>
              <td class="px-4 py-3 text-right font-mono text-rose-500 font-semibold" data-val="-0.40">-0.40%</td>
              <td class="px-4 py-3 text-right font-mono" data-val="0.80">+0.80%</td>
              <td class="px-4 py-3 text-right font-mono" data-val="4.20">+4.20%</td>
              <td class="px-4 py-3 text-xs">特斯拉重挫 4.54% 與亞馬遜下撤 1.23%，對非必需消費板塊造成重壓。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-medium">9</td>
              <td class="px-4 py-3 font-medium">公用事業 (Utilities)</td>
              <td class="px-4 py-3 font-mono">XLU</td>
              <td class="px-4 py-3 text-right font-mono text-rose-500 font-semibold" data-val="-0.50">-0.50%</td>
              <td class="px-4 py-3 text-right font-mono" data-val="-1.50">-1.50%</td>
              <td class="px-4 py-3 text-right font-mono" data-val="-5.80">-5.80%</td>
              <td class="px-4 py-3 text-xs">長端美債利率拉升直接壓低高分紅板塊估值，資金獲利回吐。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-medium">10</td>
              <td class="px-4 py-3 font-medium">房地產 (Real Estate)</td>
              <td class="px-4 py-3 font-mono">XLRE</td>
              <td class="px-4 py-3 text-right font-mono text-rose-500 font-semibold" data-val="-0.60">-0.60%</td>
              <td class="px-4 py-3 text-right font-mono" data-val="-1.80">-1.80%</td>
              <td class="px-4 py-3 text-right font-mono" data-val="-4.50">-4.50%</td>
              <td class="px-4 py-3 text-xs">10年期美債收益率從 4.45% 走高對房貸融資與地產REITs構成利空。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-medium">11</td>
              <td class="px-4 py-3 font-medium">通信服務 (Communication Services)</td>
              <td class="px-4 py-3 font-mono">XLC</td>
              <td class="px-4 py-3 text-right font-mono text-rose-500 font-semibold" data-val="-1.80">-1.80%</td>
              <td class="px-4 py-3 text-right font-mono" data-val="0.50">+0.50%</td>
              <td class="px-4 py-3 text-right font-mono" data-val="8.50">+8.50%</td>
              <td class="px-4 py-3 text-xs">權重巨頭 Meta 暴跌 5.10% 及 Alphabet 跌 1.26%，直接將通信板塊拉入深淵。</td>
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
        <div class="stat-card">
          <h4 class="font-bold text-zinc-800 dark:text-zinc-200 flex items-center gap-2">
            <span class="w-2.5 h-2.5 rounded-full bg-emerald-500"></span> 半導體 (SMH/SOXX) 極致抱團
          </h4>
          <p class="text-xs text-zinc-600 dark:text-zinc-400 mt-2 leading-relaxed">
            輝達 Computex 晶片大作戰吹響了算力物理層的進攻號角，整個半導體板塊強烈 Risk-On。博通 (AVGO +2.41%) 與光通訊模組板塊持續上行，強勢對抗大盤因利率上升帶來的逆風。
          </p>
        </div>
        <div class="stat-card">
          <h4 class="font-bold text-zinc-800 dark:text-zinc-200 flex items-center gap-2">
            <span class="w-2.5 h-2.5 rounded-full bg-amber-500"></span> AI 電力與儲能高位整固
          </h4>
          <p class="text-xs text-zinc-600 dark:text-zinc-400 mt-2 leading-relaxed">
            在經歷前期狂暴的拔估值後，AI 電力概念龍頭 (CEG、VST) 在今日出現一定的高位震盪洗籌。油價飆升和實體製造業景氣度走高為能源和公用事業帶來了分化的底色。
          </p>
        </div>
        <div class="stat-card">
          <h4 class="font-bold text-zinc-800 dark:text-zinc-200 flex items-center gap-2">
            <span class="w-2.5 h-2.5 rounded-full bg-rose-500"></span> 小盤股與防禦價值承壓
          </h4>
          <p class="text-xs text-zinc-600 dark:text-zinc-400 mt-2 leading-relaxed">
            Russell 2000 (IWM) 和等權標普 (RSP) 在今日表現較差。美債利率的二次上行對小盤股與債務偏高的中小企業形成顯著壓力，資金在非必要之時再度撤離高負債賽道。
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
        <div class="p-6 rounded-xl bg-zinc-50 dark:bg-zinc-900 border border-zinc-100 dark:border-zinc-800">
          <h4 class="font-bold text-zinc-500 text-xs uppercase mb-3">均線參與度</h4>
          <ul class="space-y-2 text-sm">
            <li class="flex justify-between">
              <span class="text-zinc-600 dark:text-zinc-400">S&P 500 高於 50日線比例</span>
              <span class="font-mono font-bold text-amber-500">64.2% (小幅下滑)</span>
            </li>
            <li class="flex justify-between">
              <span class="text-zinc-600 dark:text-zinc-400">S&P 500 高於 200日線比例</span>
              <span class="font-mono font-bold text-emerald-500">72.8%</span>
            </li>
            <li class="flex justify-between">
              <span class="text-zinc-600 dark:text-zinc-400">Nasdaq 100 高於 50日線比例</span>
              <span class="font-mono font-bold text-emerald-500">68.5%</span>
            </li>
          </ul>
        </div>
        <div class="p-6 rounded-xl bg-zinc-50 dark:bg-zinc-900 border border-zinc-100 dark:border-zinc-800">
          <h4 class="font-bold text-zinc-500 text-xs uppercase mb-3">NYSE & Nasdaq 漲跌比例</h4>
          <ul class="space-y-2 text-sm">
            <li class="flex justify-between">
              <span class="text-zinc-600 dark:text-zinc-400">NYSE 上漲 / 下跌</span>
              <span class="font-mono font-bold text-rose-500">1,382 / 1,642 (0.84)</span>
            </li>
            <li class="flex justify-between">
              <span class="text-zinc-600 dark:text-zinc-400">Nasdaq 上漲 / 下跌</span>
              <span class="font-mono font-bold text-rose-500">1,750 / 2,340 (0.75)</span>
            </li>
            <li class="flex justify-between">
              <span class="text-zinc-600 dark:text-zinc-400">52週新高 / 新低 (合計)</span>
              <span class="font-mono font-bold text-emerald-500">217 / 113</span>
            </li>
          </ul>
        </div>
        <div class="p-6 rounded-xl bg-zinc-50 dark:bg-zinc-900 border border-zinc-100 dark:border-zinc-800">
          <h4 class="font-bold text-zinc-500 text-xs uppercase mb-3">內部情緒與量能指標</h4>
          <ul class="space-y-2 text-sm">
            <li class="flex justify-between">
              <span class="text-zinc-600 dark:text-zinc-400">McClellan Oscillator</span>
              <span class="font-mono font-bold text-rose-500">-15.20</span>
            </li>
            <li class="flex justify-between">
              <span class="text-zinc-600 dark:text-zinc-400">Put/Call Ratio (對沖度)</span>
              <span class="font-mono font-bold text-amber-500">0.78 (避險小幅升溫)</span>
            </li>
            <li class="flex justify-between">
              <span class="text-zinc-600 dark:text-zinc-400">VIX Term Structure</span>
              <span class="font-mono font-bold text-emerald-500">期現正常 (Contango)</span>
            </li>
          </ul>
        </div>
      </div>
      <p class="text-xs text-zinc-500 mt-4 leading-relaxed">
        <strong>寬度解讀：</strong>雖然標普 500 與納指收盤創下歷史新高，但上漲下跌家數之比卻明顯小於 1.00，均線參與度亦出現微幅下滑。這說明今日市場的上漲是典型的「極限權重抱團」，主力資金將倉位集中在大算力半導體和原油板塊中，多數個股反而在高利率與高油價壓力下出現下跌，這是短線需要警戒的多頭擁擠信號。
      </p>
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
              <td class="px-4 py-3 text-right">$758.20</td>
              <td class="px-4 py-3 text-right">$742.00</td>
              <td class="px-4 py-3 text-right">$728.00</td>
              <td class="px-4 py-3 text-right">$682.00</td>
              <td class="px-4 py-3 text-center">68.2</td>
              <td class="px-4 py-3 font-sans text-xs text-left">$750 / $762</td>
              <td class="px-4 py-3 font-sans text-xs text-emerald-500 font-semibold text-left">多頭強勢突破，逼近超買區</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold font-sans text-zinc-900 dark:text-zinc-100">QQQ (Nasdaq 100)</td>
              <td class="px-4 py-3 text-right">$552.10</td>
              <td class="px-4 py-3 text-right">$538.00</td>
              <td class="px-4 py-3 text-right">$519.00</td>
              <td class="px-4 py-3 text-right">$472.00</td>
              <td class="px-4 py-3 text-center">69.8</td>
              <td class="px-4 py-3 font-sans text-xs text-left">$545 / $558</td>
              <td class="px-4 py-3 font-sans text-xs text-emerald-500 font-semibold text-left">歷史收盤新高，RSI 觸及邊界</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold font-sans text-zinc-900 dark:text-zinc-100">IWM (Russell 2000)</td>
              <td class="px-4 py-3 text-right">$218.50</td>
              <td class="px-4 py-3 text-right">$220.00</td>
              <td class="px-4 py-3 text-right">$218.00</td>
              <td class="px-4 py-3 text-right">$209.00</td>
              <td class="px-4 py-3 text-center">49.5</td>
              <td class="px-4 py-3 font-sans text-xs text-left">$215 / $223</td>
              <td class="px-4 py-3 font-sans text-xs text-amber-500 font-semibold text-left">跌破20日均線，趨向區間震盪</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold font-sans text-zinc-900 dark:text-zinc-100">SMH (Semiconductors)</td>
              <td class="px-4 py-3 text-right">$282.40</td>
              <td class="px-4 py-3 text-right">$268.00</td>
              <td class="px-4 py-3 text-right">$252.00</td>
              <td class="px-4 py-3 text-right">$215.00</td>
              <td class="px-4 py-3 text-center">72.5</td>
              <td class="px-4 py-3 font-sans text-xs text-left">$275 / $290</td>
              <td class="px-4 py-3 font-sans text-xs text-rose-500 font-semibold text-left">技術面嚴重超買，需警戒高位回調</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold font-sans text-zinc-900 dark:text-zinc-100">IGV (Software)</td>
              <td class="px-4 py-3 text-right">$92.30</td>
              <td class="px-4 py-3 text-right">$90.00</td>
              <td class="px-4 py-3 text-right">$88.00</td>
              <td class="px-4 py-3 text-right">$82.00</td>
              <td class="px-4 py-3 text-center">58.4</td>
              <td class="px-4 py-3 font-sans text-xs text-left">$90 / $95</td>
              <td class="px-4 py-3 font-sans text-xs text-zinc-400 font-semibold text-left">中性偏多，多頭蓄勢突破上方平台</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold font-sans text-zinc-900 dark:text-zinc-100">XLK (Technology)</td>
              <td class="px-4 py-3 text-right">$235.10</td>
              <td class="px-4 py-3 text-right">$224.00</td>
              <td class="px-4 py-3 text-right">$212.00</td>
              <td class="px-4 py-3 text-right">$190.00</td>
              <td class="px-4 py-3 text-center">71.0</td>
              <td class="px-4 py-3 font-sans text-xs text-left">$228 / $238</td>
              <td class="px-4 py-3 font-sans text-xs text-rose-500 font-semibold text-left">長陽拉升，RSI 進駐 70 超買大門</td>
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
        <details class="p-4 border border-zinc-200 dark:border-zinc-800 rounded-xl bg-zinc-50/30 dark:bg-zinc-900/30">
          <summary class="font-bold text-zinc-800 dark:text-zinc-200">8.1 大型科技七巨頭 (Magnificent Seven) 表現</summary>
          <div class="mt-4 pl-4 border-l-2 border-brand-500 space-y-3 text-sm text-zinc-600 dark:text-zinc-300">
            <p>• <strong>NVDA (+6.26%, $224.36)：</strong>輝達成為全場絕對焦點！黃仁勳在 Computex Keynote 宣佈 Arm-based 「RTX Spark」超級 PC 晶片（Grace CPU + Blackwell GPU，與 MediaTek 合作研發），意圖全面重塑 AI PC 生態圈；同時確認下一代 Vera Rubin 旗艦 AI 算力平台（搭載 Vera CPU 及 Rubin GPU）已投入量產，使推理成本再暴降。股價拔地而起大漲 6.26%，強烈主導市場情緒。</p>
            <p>• <strong>MSFT (+2.50%, $461.50)：</strong>作為 RTX Spark 首批戰略夥伴，預計秋季推出極致 Windows AI PC 新筆記型電腦。長陽大突破，創收盤歷史新高。</p>
            <p>• <strong>META (-5.10%, $592.23)：</strong>股價暴跌。SEC 監管文件披露包括 COO Javier Olivan 及副總裁等多名核心高管執行了 Rule 10b5-1 預先安排的大規模股權出售。此外，市場對其高達 $1450億 的 2026 年高 Capex 投資回報率依舊抱持懷疑，導致短線多頭高位踩踏。</p>
            <p>• <strong>TSLA (-4.54%, $178.50)：</strong>股價重挫破位。面臨估值溢價質疑，同時受壓於中美兩大主力市場 EV 需求增速的明顯放緩。此外，NHTSA 對 FSD 技術的安全質疑和 SpaceX IPO 傳言亦令投資者權衡馬斯克精力的分散。</p>
            <p>• <strong>AAPL (-1.38%, $188.40)：</strong>受 NVIDIA RTX Spark 重新定義 AI PC 生態的壓力，市場擔心 Mac 產品線面臨 Windows on Arm陣營的強烈狙擊。</p>
            <p>• <strong>GOOGL (-1.26%, $175.20) / AMZN (-1.23%, $267.30)：</strong>跟隨科技板塊大盤進行高位籌碼交換與技術性修正。</p>
          </div>
        </details>

        <!-- 8.2 AI硬體/半導體重點股 -->
        <details class="p-4 border border-zinc-200 dark:border-zinc-800 rounded-xl bg-zinc-50/30 dark:bg-zinc-900/30">
          <summary class="font-bold text-zinc-800 dark:text-zinc-200">8.2 AI 硬體 / 半導體重點股異動分析</summary>
          <div class="mt-4 pl-4 border-l-2 border-brand-500 space-y-3 text-sm text-zinc-600 dark:text-zinc-300">
            <p>• <strong>AVGO (+2.41%, $452.33)：</strong>做為客製化 AI ASIC 霸主，博通受到 Nvidia 宣示生態圈擴張的強烈烘托，高盛上調其目標價，股價爆量拉升。</p>
            <p>• <strong>AMD (-1.20%, $489.24)：</strong>Nvidia 提前宣布下一代 Rubin 平台進入全面生產，給 AMD 即將發表的 MI350/MI400 算力系列帶來強大防守壓力，股價跌破 $490。</p>
            <p>• <strong>MU (+1.10%) / TSM (+1.85%)：</strong>高頻寬記憶體 (HBM) 需求火爆及台積電做為 Rubin 晶片唯一晶圓代工廠的超高確定性，推動股價穩步走強。</p>
          </div>
        </details>

        <!-- 8.3 軟體/SaaS -->
        <details class="p-4 border border-zinc-200 dark:border-zinc-800 rounded-xl bg-zinc-50/30 dark:bg-zinc-900/30">
          <summary class="font-bold text-zinc-800 dark:text-zinc-200">8.3 軟體 / SaaS / AI 應用重點股異動</summary>
          <div class="mt-4 pl-4 border-l-2 border-brand-500 space-y-3 text-sm text-zinc-600 dark:text-zinc-300">
            <p>• <strong>PLTR (+1.80%, $45.20)：</strong>Agentic AI 成為 Computex 熱詞，Palantir 作為 Agentic AI 企業端落地先驅，獲買盤逢低卡位，股價沿 10 日線強勢爬升。</p>
            <p>• <strong>ORCL (+0.20%) / NOW (+0.40%)：</strong>受益於微軟重振 Windows AI PC 的信心注入，軟體估值中樞維持平穩。</p>
          </div>
        </details>

        <!-- 8.4 AI電力與基礎設施 -->
        <details class="p-4 border border-zinc-200 dark:border-zinc-800 rounded-xl bg-zinc-50/30 dark:bg-zinc-900/30">
          <summary class="font-bold text-zinc-800 dark:text-zinc-200">8.4 AI 電力 / 資料中心 / 能源基礎設施分析</summary>
          <div class="mt-4 pl-4 border-l-2 border-brand-500 space-y-3 text-sm text-zinc-600 dark:text-zinc-300">
            <p>• <strong>VST (+0.50%, $138.20) / CEG (-0.20%, $292.10)：</strong>核能及獨立發電題材在高位展開健康換手，ISM 製造業數據表明實體工業擴張對電網基建和電力保證有強勁需求，限制了其回吐空間。</p>
            <p>• <strong>ETN (+0.60%) / GEV (+1.10%)：</strong>電網變壓器及清潔發電渦輪需求依然訂單飽滿，高利率環境中仍表現出強勁防禦力。</p>
          </div>
        </details>
      </div>
    </section>

    <!-- 9. 財報日曆與解讀 -->
    <section id="earnings" class="mb-12 scroll-mt-6">
      <h2 class="text-2xl font-bold mb-4 flex items-center gap-2 border-b border-zinc-100 dark:border-zinc-800 pb-2">
        <span class="text-brand-500">9.</span> 財報日曆與財報解讀
      </h2>
      <div class="p-6 rounded-xl bg-zinc-50 dark:bg-zinc-900 border border-zinc-100 dark:border-zinc-800 space-y-4">
        <div>
          <h4 class="font-bold text-zinc-800 dark:text-zinc-200">9.1 昨夜已公佈財報的重點公司</h4>
          <p class="text-sm text-zinc-600 dark:text-zinc-400 mt-1">上周戴爾科技 (DELL) 及 Snowflake (SNOW) 的強勁業績效應在今日依然在半導體和軟體中發酵，多頭機構持續執行高確定性回補。</p>
        </div>
        <hr class="border-zinc-200 dark:border-zinc-800">
        <div>
          <h4 class="font-bold text-zinc-800 dark:text-zinc-200">9.2 接下來 1-3 個交易日重要財報</h4>
          <div class="overflow-x-auto mt-2">
            <table class="min-w-full divide-y divide-zinc-200 dark:divide-zinc-800 text-sm">
              <thead class="bg-zinc-100 dark:bg-zinc-900">
                <tr>
                  <th class="px-4 py-2 text-left font-semibold text-zinc-600 dark:text-zinc-400">公布時間</th>
                  <th class="px-4 py-2 text-left font-semibold text-zinc-600 dark:text-zinc-400">公司名稱 (代號)</th>
                  <th class="px-4 py-2 text-center font-semibold text-zinc-600 dark:text-zinc-400">EPS 預期</th>
                  <th class="px-4 py-2 text-center font-semibold text-zinc-600 dark:text-zinc-400">營收預期</th>
                  <th class="px-4 py-2 text-left font-semibold text-zinc-600 dark:text-zinc-400">市場關注核心焦點</th>
                </tr>
              </thead>
              <tbody class="divide-y divide-zinc-200 dark:divide-zinc-800 font-mono text-zinc-700 dark:text-zinc-300">
                <tr>
                  <td class="px-4 py-2 font-sans">6月2日 盤後</td>
                  <td class="px-4 py-2 font-sans font-semibold">CrowdStrike (CRWD)</td>
                  <td class="px-4 py-2 text-center">$0.89</td>
                  <td class="px-4 py-2 text-center">$905.5M</td>
                  <td class="px-4 py-2 font-sans text-xs text-left">網路安全終端滲透率及 AI 平台 Falcon 帶來的年度經常性營收 (ARR) 增速。</td>
                </tr>
                <tr>
                  <td class="px-4 py-2 font-sans">6月3日 盤後</td>
                  <td class="px-4 py-2 font-sans font-semibold">Lululemon (LULU)</td>
                  <td class="px-4 py-2 text-center">$2.40</td>
                  <td class="px-4 py-2 text-center">$2.20B</td>
                  <td class="px-4 py-2 font-sans text-xs text-left">北美地區高端消費需求是否有疲軟跡象及中國市場的擴張指引。</td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </section>

    <!-- 10. 機構觀點與資金流 -->
    <section id="institutional" class="mb-12 scroll-mt-6">
      <h2 class="text-2xl font-bold mb-4 flex items-center gap-2 border-b border-zinc-100 dark:border-zinc-800 pb-2">
        <span class="text-brand-500">10.</span> 機構觀點與資金流
      </h2>
      <div class="space-y-4 text-sm text-zinc-600 dark:text-zinc-300">
        <div class="p-4 rounded-xl bg-zinc-50 dark:bg-zinc-900 border border-zinc-100 dark:border-zinc-800">
          <h4 class="font-bold text-zinc-800 dark:text-zinc-200">華爾街大行看 Computex：AI 半導體將保持 90% 以上市占</h4>
          <p class="mt-2 leading-relaxed">
            高盛 (Goldman Sachs) 發表針對台北 Computex 的重磅分析，指出輝達提前量產 Vera Rubin 平台直接粉碎了其他競爭對手的「窗口期幻想」。Rubin 將引進最尖端的 HBM4 記憶體架構和超低推理耗能，高盛認為這將確保輝達在 AI 數據中心的垄断地位至少維持至 2027 年，因此將輝達目標價從 $210 調升至 $245。
          </p>
        </div>
        <div class="p-4 rounded-xl bg-zinc-50 dark:bg-zinc-900 border border-zinc-100 dark:border-zinc-800">
          <h4 class="font-bold text-zinc-800 dark:text-zinc-200">ETF 資金流向：科技與能源 ETF 淨流入雙核並進</h4>
          <p class="mt-2 leading-relaxed">
            上周數據顯示，美股 ETF 淨流入資金達 120 億美元。其中資訊科技 ETF（XLK）與半導體 ETF（SMH）吸引了近半數資金；而由於中東緊張情勢突然加劇，能源板塊 ETF（XLE）今日成交量較 20 日均值放大 80%，顯示大資金利用能源板塊來對沖宏觀通膨和地緣風險的動作極其顯著。
          </p>
        </div>
      </div>
    </section>

    <!-- 11. 板塊輪動判斷 -->
    <section id="rotation" class="mb-12 scroll-mt-6">
      <h2 class="text-2xl font-bold mb-4 flex items-center gap-2 border-b border-zinc-100 dark:border-zinc-800 pb-2">
        <span class="text-brand-500">11.</span> 板塊輪動判斷
      </h2>
      <p class="text-sm text-zinc-600 dark:text-zinc-300 leading-relaxed">
        <strong>大盤多頭趨勢的「防禦性變奏」：</strong>當前的板塊輪動呈现出極具智慧的組合拳。雖然 10年期美債利率攀升至 4.475% 給小盤股和公用事業帶來壓力，但多頭大資金沒有選擇全面恐慌退場，而是靈活地在<strong>「AI 算力基建」</strong>（高確定性增長）與<strong>「能源板塊」</strong>（對沖油價與通膨）之間建立了鋼鐵雙壁。
        <br><br>
        這種「一邊買入大晶片、一邊加倉石油巨頭」的自我防禦性配置，既維持了標普與納指在歷史高點上的良性整理，也表明市場依然由理性的 Risk-On 資金主導。在大算力（輝達、博通）及能源龍頭不倒的背景下，大盤高位牛市的基本格局難以被輕易扭轉。
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
              <td class="px-4 py-3 font-mono text-emerald-500 font-semibold">$224.36 (+6.26%)</td>
              <td class="px-4 py-3"><span class="px-2 py-0.5 rounded text-xs tag-strong">繼續強勢</span></td>
              <td class="px-4 py-3 text-xs">Computex 大放異彩，RTX Spark 與 Rubin 震撼發表，帶量突破新高，目標直指 $240。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold text-zinc-900 dark:text-zinc-100">AMD</td>
              <td class="px-4 py-3 font-mono text-rose-500 font-semibold">$489.24 (-1.20%)</td>
              <td class="px-4 py-3"><span class="px-2 py-0.5 rounded text-xs tag-warning">回踩支撐</span></td>
              <td class="px-4 py-3 text-xs">輝達新品壓力下回調。正在測試 20 日線 $485 支撐，靜待自身 Computex 期間新片發布催化。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold text-zinc-900 dark:text-zinc-100">AVGO</td>
              <td class="px-4 py-3 font-mono text-emerald-500 font-semibold">$452.33 (+2.41%)</td>
              <td class="px-4 py-3"><span class="px-2 py-0.5 rounded text-xs tag-strong">繼續強勢</span></td>
              <td class="px-4 py-3 text-xs">客製化晶片 ASIC 與網絡架構領頭羊，爆量突破，均線強勢向上，上行空間完全打開。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold text-zinc-900 dark:text-zinc-100">MRVL</td>
              <td class="px-4 py-3 font-mono text-emerald-500 font-semibold">$207.25 (+0.79%)</td>
              <td class="px-4 py-3"><span class="px-2 py-0.5 rounded text-xs tag-strong">繼續強勢</span></td>
              <td class="px-4 py-3 text-xs">光通訊高速傳輸需求旺盛，沿 10 日均線平穩走高，繼續持股。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold text-zinc-900 dark:text-zinc-100">GOOGL</td>
              <td class="px-4 py-3 font-mono text-rose-500 font-semibold">$175.20 (-1.26%)</td>
              <td class="px-4 py-3"><span class="px-2 py-0.5 rounded text-xs tag-neutral">高位震盪</span></td>
              <td class="px-4 py-3 text-xs">高位籌碼交換，受資金向微軟及輝達分流影響而收縮，短期於 $173 附近有均線卡位。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold text-zinc-900 dark:text-zinc-100">MSFT</td>
              <td class="px-4 py-3 font-mono text-emerald-500 font-semibold">$461.50 (+2.50%)</td>
              <td class="px-4 py-3"><span class="px-2 py-0.5 rounded text-xs tag-strong">繼續強勢</span></td>
              <td class="px-4 py-3 text-xs">創歷史收盤新高，與 NVDA 深度綁定攜手開闢 Windows AI PC 龐大版圖，長線穩健。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold text-zinc-900 dark:text-zinc-100">META</td>
              <td class="px-4 py-3 font-mono text-rose-500 font-semibold">$592.23 (-5.10%)</td>
              <td class="px-4 py-3"><span class="px-2 py-0.5 rounded text-xs tag-warning">回踩支撐</span></td>
              <td class="px-4 py-3 text-xs">受高管拋售與高 Capex 焦慮打擊回踩 50 日均線 $588 支撐，暫時轉為觀望。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold text-zinc-900 dark:text-zinc-100">AMZN</td>
              <td class="px-4 py-3 font-mono text-rose-500 font-semibold">$267.30 (-1.23%)</td>
              <td class="px-4 py-3"><span class="px-2 py-0.5 rounded text-xs tag-neutral">高位震盪</span></td>
              <td class="px-4 py-3 text-xs">AWS 雲端算力需求依舊極強，股價跟隨大盤小幅盤整，上升趨勢結構未破。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold text-zinc-900 dark:text-zinc-100">ORCL</td>
              <td class="px-4 py-3 font-mono text-emerald-500 font-semibold">$203.75 (+0.20%)</td>
              <td class="px-4 py-3"><span class="px-2 py-0.5 rounded text-xs tag-neutral">高位震盪</span></td>
              <td class="px-4 py-3 text-xs">受惠於 Windows AI 生態預期，在 $200 支撐平台上穩健洗籌，蓄勢挑戰前高。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold text-zinc-900 dark:text-zinc-100">CRM</td>
              <td class="px-4 py-3 font-mono text-rose-500 font-semibold">$232.10 (-0.15%)</td>
              <td class="px-4 py-3"><span class="px-2 py-0.5 rounded text-xs tag-neutral">低位修復</span></td>
              <td class="px-4 py-3 text-xs">前期大跌後在底部企穩，均線黏合，正等待 AI 應用轉化利潤的明確催化劑。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold text-zinc-900 dark:text-zinc-100">NOW</td>
              <td class="px-4 py-3 font-mono text-emerald-500 font-semibold">$895.20 (+0.40%)</td>
              <td class="px-4 py-3"><span class="px-2 py-0.5 rounded text-xs tag-strong">繼續強勢</span></td>
              <td class="px-4 py-3 text-xs">SaaS 大龍頭走勢強韌，沿 10 日線緩慢爬行，中長期上升通道依然完美。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold text-zinc-900 dark:text-zinc-100">SNOW</td>
              <td class="px-4 py-3 font-mono text-emerald-500 font-semibold">$195.40 (+0.50%)</td>
              <td class="px-4 py-3"><span class="px-2 py-0.5 rounded text-xs tag-strong">繼續強勢</span></td>
              <td class="px-4 py-3 text-xs">上周財報大捷爆發後，今日高位健康消化賣盤，守穩跳空缺口，多頭格局強悍。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold text-zinc-900 dark:text-zinc-100">ADBE</td>
              <td class="px-4 py-3 font-mono text-rose-500 font-semibold">$488.20 (-0.30%)</td>
              <td class="px-4 py-3"><span class="px-2 py-0.5 rounded text-xs tag-neutral">高位震盪</span></td>
              <td class="px-4 py-3 text-xs">高位橫盤整理，短期方向尚不明朗，靜待月中自身財報指引。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold text-zinc-900 dark:text-zinc-100">PLTR</td>
              <td class="px-4 py-3 font-mono text-emerald-500 font-semibold">$45.20 (+1.80%)</td>
              <td class="px-4 py-3"><span class="px-2 py-0.5 rounded text-xs tag-strong">繼續強勢</span></td>
              <td class="px-4 py-3 text-xs">Agentic AI 第一品牌，機構連續加碼，股價逼近新高，上行無阻力。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold text-zinc-900 dark:text-zinc-100">LITE</td>
              <td class="px-4 py-3 font-mono text-rose-500 font-semibold">$68.50 (-0.40%)</td>
              <td class="px-4 py-3"><span class="px-2 py-0.5 rounded text-xs tag-neutral">高位震盪</span></td>
              <td class="px-4 py-3 text-xs">光通訊配套元件走勢分化，受利率長端收益率上升影響小幅震盪。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold text-zinc-900 dark:text-zinc-100">COHR</td>
              <td class="px-4 py-3 font-mono text-emerald-500 font-semibold">$192.10 (+0.80%)</td>
              <td class="px-4 py-3"><span class="px-2 py-0.5 rounded text-xs tag-strong">繼續強勢</span></td>
              <td class="px-4 py-3 text-xs">800G 光模組熱度不減，技術面在 5 日線上方獲得強力支持。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold text-zinc-900 dark:text-zinc-100">ANET</td>
              <td class="px-4 py-3 font-mono text-emerald-500 font-semibold">$388.40 (+1.10%)</td>
              <td class="px-4 py-3"><span class="px-2 py-0.5 rounded text-xs tag-strong">繼續強勢</span></td>
              <td class="px-4 py-3 text-xs">資料中心超高速交換機龍頭，訂單持續爆棚，股價穩步走強突破平台。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold text-zinc-900 dark:text-zinc-100">FLNC</td>
              <td class="px-4 py-3 font-mono text-rose-500 font-semibold">$24.50 (-1.60%)</td>
              <td class="px-4 py-3"><span class="px-2 py-0.5 rounded text-xs tag-neutral">需要觀察</span></td>
              <td class="px-4 py-3 text-xs">儲能板塊對高融資利率高度敏感，今日隨美債利率走高而回軟。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold text-zinc-900 dark:text-zinc-100">OKLO</td>
              <td class="px-4 py-3 font-mono text-rose-500 font-semibold">$13.80 (-2.10%)</td>
              <td class="px-4 py-3"><span class="px-2 py-0.5 rounded text-xs tag-neutral">需要觀察</span></td>
              <td class="px-4 py-3 text-xs">小盤核能概念投機性較強，受小盤股指數走低拖累回調，短期觀望。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold text-zinc-900 dark:text-zinc-100">VST</td>
              <td class="px-4 py-3 font-mono text-emerald-500 font-semibold">$138.20 (+0.50%)</td>
              <td class="px-4 py-3"><span class="px-2 py-0.5 rounded text-xs tag-neutral">高位震盪</span></td>
              <td class="px-4 py-3 text-xs">電力龍頭，在 $135 平台上方高位震盪洗盤，製造業數據提振，結構完整。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold text-zinc-900 dark:text-zinc-100">CEG</td>
              <td class="px-4 py-3 font-mono text-rose-500 font-semibold">$292.10 (-0.20%)</td>
              <td class="px-4 py-3"><span class="px-2 py-0.5 rounded text-xs tag-neutral">高位震盪</span></td>
              <td class="px-4 py-3 text-xs">高位獲利回吐，小幅整理，於 $290 關口獲得短期支撐。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold text-zinc-900 dark:text-zinc-100">ETN</td>
              <td class="px-4 py-3 font-mono text-emerald-500 font-semibold">$382.40 (+0.60%)</td>
              <td class="px-4 py-3"><span class="px-2 py-0.5 rounded text-xs tag-strong">繼續強勢</span></td>
              <td class="px-4 py-3 text-xs">AI 電網變壓器巨頭，高景氣與實體擴張共振，形態極為抗跌，沿均線穩健向上。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold text-zinc-900 dark:text-zinc-100">VRT</td>
              <td class="px-4 py-3 font-mono text-emerald-500 font-semibold">$112.50 (+1.20%)</td>
              <td class="px-4 py-3"><span class="px-2 py-0.5 rounded text-xs tag-strong">繼續強勢</span></td>
              <td class="px-4 py-3 text-xs">AI 液冷基礎設施龍頭，輝達晶片極端熱量管理必配，獲長多機構大力追捧。</td>
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
      <div class="space-y-4 text-sm text-zinc-600 dark:text-zinc-300">
        <div>
          <h4 class="font-bold text-zinc-800 dark:text-zinc-200">13.1 宏觀與技術關鍵觀察點</h4>
          <p class="mt-1 leading-relaxed">
            • <strong>美債收益率天花板：</strong>密切關注 10 年期美債利率是否會突破並站穩 <strong>4.50%</strong>。若站穩，需警惕小盤股 Russell 2000 的進一步失血破位及科技成長股倍數的局部壓縮。
            <br>• <strong>WTI 原油與通膨對沖：</strong>地緣情勢若繼續激化，WTI 原油升破 <strong>$95</strong> 將引爆全市場對二次通膨的深層焦慮，屆時需果斷增加能源板塊 (XLE) 持倉做對沖。
          </p>
        </div>
        <hr class="border-zinc-200 dark:border-zinc-800">
        <div>
          <h4 class="font-bold text-zinc-800 dark:text-zinc-200">13.2 明日觀察名單 (Watchlist)</h4>
          <p class="mt-1 leading-relaxed">
            1. <strong>NVDA (輝達)：</strong>強勢帶量突破，觀察 $225 關口能否徹底站穩，並觀察 Computex 上合作夥伴的進一步反響。
            <br>2. <strong>XLE (能源板塊 ETF)：</strong>地緣局勢直接催化劑，若原油高位盤整，能源板塊將成為多頭避險的最核心港灣。
            <br>3. <strong>META (Meta)：</strong>觀察 50 日均線 $588 處的支撐有效性。若放量跌破，需減倉以防估值二次修正。
            <br>4. <strong>CRWD (CrowdStrike)：</strong>明日盤後發布財報，做為 AI 網絡安全終端龍頭，其業績將直接指引整個 SaaS / 軟體板塊的防守情緒。
          </p>
        </div>
      </div>
    </section>

    <!-- 14. 風險提示 -->
    <section id="risks" class="mb-12 scroll-mt-6">
      <h2 class="text-2xl font-bold mb-4 flex items-center gap-2 border-b border-zinc-100 dark:border-zinc-800 pb-2">
        <span class="text-brand-500">14.</span> 風險提示（視覺化風險矩陣）
      </h2>
      <div class="overflow-x-auto border border-zinc-200 dark:border-zinc-800 rounded-xl">
        <table class="min-w-full divide-y divide-zinc-200 dark:divide-zinc-800 text-sm">
          <thead class="bg-zinc-50 dark:bg-zinc-900">
            <tr>
              <th class="px-4 py-3 text-left font-semibold text-zinc-600 dark:text-zinc-400">風險維度</th>
              <th class="px-4 py-3 text-center font-semibold text-zinc-600 dark:text-zinc-400">評級</th>
              <th class="px-4 py-3 text-left font-semibold text-zinc-600 dark:text-zinc-400">具體威脅解讀與因應方案</th>
            </tr>
          </thead>
          <tbody class="divide-y divide-zinc-200 dark:divide-zinc-800 text-zinc-700 dark:text-zinc-300">
            <tr>
              <td class="px-4 py-3 font-semibold text-zinc-900 dark:text-zinc-100">地緣政治與油價飆升</td>
              <td class="px-4 py-3 text-center"><span class="px-2 py-0.5 rounded text-xs tag-danger font-bold">高</span></td>
              <td class="px-4 py-3 text-xs leading-relaxed">以黎衝突升級引爆 WTI 原油突破 $93.50，原油飆漲將極大推升二次通膨憂慮，延後聯聯儲降息時程。因應：加倉 XLE 能源股對沖。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold text-zinc-900 dark:text-zinc-100">宏觀利率與債市陡峭化</td>
              <td class="px-4 py-3 text-center"><span class="px-2 py-0.5 rounded text-xs tag-warning font-bold">中高</span></td>
              <td class="px-4 py-3 text-xs leading-relaxed">ISM PMI 54.0% 走強推升 10年期美債利率至 4.475% 且 30年期飆上 4.99%。長端收益率大幅攀升壓低了分紅股及小盤股估值。因應：控制 Russell 2000 倉位。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold text-zinc-900 dark:text-zinc-100">AI 算力板塊擁擠度</td>
              <td class="px-4 py-3 text-center"><span class="px-2 py-0.5 rounded text-xs tag-warning font-bold">中</span></td>
              <td class="px-4 py-3 text-xs leading-relaxed">輝達和博通日線 RSI 分別達 72.5 和 71，顯示短線上行買盤極度擁擠，部分板塊高位現分化（如 AMD 回調）。因應：不盲目追高，等待分時均線支撐回踩。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold text-zinc-900 dark:text-zinc-100">個股高管執行減持</td>
              <td class="px-4 py-3 text-center"><span class="px-2 py-0.5 rounded text-xs tag-neutral font-bold">低中</span></td>
              <td class="px-4 py-3 text-xs leading-relaxed">Meta 多名高管集體售股重挫 5.10%。高管減持極易引發高位多頭短線踩踏。因應：嚴守 50 日均線關鍵防線，跌破則減倉防守。</td>
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
      <div class="p-6 rounded-xl bg-zinc-50 dark:bg-zinc-900 border border-zinc-100 dark:border-zinc-800 space-y-4">
        <ul class="list-disc pl-5 space-y-2 text-zinc-600 dark:text-zinc-300 text-sm">
          <li><strong>今日市場結論：</strong>指數續創歷史新高，內部呈現顯著的極限分化。輝達 Computex 晶片引爆算力基建瘋狂買盤，但中東地緣政治危機加劇和製造業數據強勁推高了美債利率與油價，導致小盤股、大消費與個別高估值及高管減持股承受下挫壓力。</li>
          <li><strong>當前市場階段：</strong>高位牛市震盪與極限板塊良性輪動期。</li>
          <li><strong>操作傾向：</strong>維持中性偏多，聚焦高確定性。嚴格禁止盲目追高超買股（如輝達、博通），配置上以大算力物理基建（輝達、博通）為多頭核心，並分配適度倉位至能源板塊（XLE）對沖地緣通膨風險。</li>
          <li><strong>最值得關注的 5 個訊號：</strong>10年期美債利率是否會突破並站上 4.50%、WTI原油是否會飆上 $95.00、輝達股價能否在 $225 穩固防線、Crowdstrike 明日盤後財報解讀、以及下半周非農就業報告。</li>
        </ul>
      </div>
    </section>

  </main>
</div>

<!-- Vanilla JS Tab switching & Table utilities -->
<script>
  // Theme Toggle Logic
  const themeToggle = document.getElementById('theme-toggle');
  themeToggle.addEventListener('click', () => {
    const dark = document.documentElement.classList.toggle('dark');
    localStorage.theme = dark ? 'dark' : 'light';

    // Re-init mermaid with new theme if loaded
    if (window.__mermaid) {
      document.querySelectorAll('.mermaid[data-processed]').forEach(el => {
        el.removeAttribute('data-processed');
        el.innerHTML = el.getAttribute('data-original-code') || el.innerHTML;
      });
      window.__mermaid.initialize({ startOnLoad: false, theme: dark ? 'dark' : 'default', securityLevel: 'loose' });
      window.__mermaid.run();
    }
  });

  // Keep a copy of raw mermaid codes for re-renders on theme change
  document.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll('.mermaid').forEach(el => {
      el.setAttribute('data-original-code', el.innerHTML);
    });
    initTOCScrollspy();
  });

  // Scrollspy for Toc Highlight
  function initTOCScrollspy() {
    const links = document.querySelectorAll('.toc a');
    const sections = Array.from(links).map(link => document.querySelector(link.getAttribute('href')));

    const onScroll = () => {
      const scrollPos = window.scrollY + 100;
      let activeIdx = 0;
      for (let i = 0; i < sections.length; i++) {
        if (sections[i] && sections[i].offsetTop <= scrollPos) {
          activeIdx = i;
        }
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
        data: [0.09, 0.26, 0.42, 0.55, -0.47, 1.06, 4.80],
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

# Save this HTML to reports/2026-06-01-us-stock-closing-daily-report.html inside /Users/wisdom/html-report-skill
target_dir = "/Users/wisdom/html-report-skill/reports"
os.makedirs(target_dir, exist_ok=True)
target_path = os.path.join(target_dir, "2026-06-01-us-stock-closing-daily-report.html")

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
exists = any(item.get("file") == "2026-06-01-us-stock-closing-daily-report.html" for item in manifest)
if not exists:
    new_entry = {
      "file": "2026-06-01-us-stock-closing-daily-report.html",
      "title": "美股收盤日報｜2026-06-01",
      "date": "2026-06-01",
      "description": "標普納指同創歷史收盤新高！輝達黃仁勳台北 Computex 重磅推出 RTX Spark 超級電腦晶片，股價狂飆 6.26% 領漲半導體，中東局勢緊張致 WTI 原油大漲 4.80%，高官拋售令 Meta 重挫 5.10%，特斯拉回跌 4.54% 破位。"
    }
    manifest.insert(0, new_entry)
    with open(manifest_path, "w", encoding="utf-8") as f:
        json.dump(manifest, f, ensure_ascii=False, indent=2)
    print(f"Updated manifest.json successfully at: {manifest_path}")
else:
    print("manifest.json already contains the entry for 2026-06-01.")
