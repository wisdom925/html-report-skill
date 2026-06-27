import os

html_content = """<!doctype html>
<html lang="zh-TW" class="scroll-smooth">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <title>美股收盤日報｜2026-06-26</title>
  <meta name="description" content="2026年6月26日美股收盤日報：半導體高位劇烈回調，費半大跌逾5.6%，美光回吐超6%。然而超跌軟體SaaS板塊爆發性反彈，微軟蘋果大漲穩住指數，市場在羅素指數重編生效日巨量震盪，板塊大輪動。">
  <meta property="og:title" content="美股收盤日報｜2026-06-26">
  <meta property="og:description" content="半導體高位劇烈回調，費半大跌逾5.6%，美光回吐超6%。然而超跌軟體SaaS板塊爆發性反彈，微軟蘋果大漲穩住指數，市場在羅素指數重編生效日巨量震盪，板塊大輪動。">
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
    <div class="font-bold mb-3 text-zinc-400 dark:text-zinc-555 uppercase tracking-wider text-xs">報告目錄</div>
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
        <time class="text-sm font-semibold text-zinc-500 dark:text-zinc-400">2026-06-26</time>
      </div>
      <h1 class="text-3xl sm:text-4xl font-extrabold tracking-tight mb-4 bg-gradient-to-r from-zinc-900 to-zinc-700 dark:from-zinc-100 dark:to-zinc-400 bg-clip-text text-transparent">
        美股收盤日報｜半導體遭劇烈獲利回吐，費半重挫逾 5.6%！超跌軟體 SaaS 板塊井噴式反彈，微軟蘋果大漲穩住指數，市場在羅素調整日巨量震盪！
      </h1>
      <p class="text-lg text-zinc-500 dark:text-zinc-400 leading-relaxed">
        週五（2026年6月26日），美股市場呈現顯著的板塊「大洗牌」與「軟硬輪動」。在經歷了前一交易日美光財報大熱帶來的狂歡後，晶片板塊遭遇劇烈的獲利了結與去擁擠化，費城半導體指數（SOXX）重挫 5.64%，記憶體龍頭美光科技（MU）大跌 6.69%。然而，資金並未撤出市場，而是迅速流入嚴重超跌的軟體 SaaS 板塊（IGV 暴漲 4.06%）及防禦性板塊（醫療 XLV 上漲 3.03%），微軟（MSFT）反彈 5.71%，蘋果（AAPL）上漲 3.14%。三大指數最終微幅震盪收跌，標普 500 下滑 0.05%，納斯達克綜合指數下跌 0.24%，羅素 2000 中小盤股則逆市上漲 0.31%。今日亦是羅素指數半年度調整生效日，尾盤爆出史詩級成交量。
      </p>
    </header>

    <!-- 0. 今日一句話總結 -->
    <section id="summary" class="mb-12 scroll-mt-6">
      <h2 class="text-2xl font-bold mb-4 flex items-center gap-2 border-b border-zinc-100 dark:border-zinc-800 pb-2">
        <span class="text-brand-500">0.</span> 今日一句話總結
      </h2>
      <div class="bg-zinc-50/50 dark:bg-zinc-900/50 p-6 rounded-2xl border border-zinc-200/60 dark:border-zinc-800/60 leading-relaxed text-zinc-700 dark:text-zinc-300">
        <ul class="list-disc pl-5 space-y-3">
          <li><strong>大盤狀態：</strong>美股三大指數低開後走勢分化，尾盤在重編生效巨量交易中收窄跌幅。S&P 500 指數收跌 0.05% (7,354.02點)，道瓊指數收跌 0.09% (51,876.11點)，納指綜合指數收跌 0.24% (25,297.62點)。QQQ (納指 100) 則因晶片股權重受壓收跌 1.38%，而羅素 2000 逆市收漲 0.31%。</li>
          <li><strong>驅動因素：</strong>半導體與 AI 算力硬件股高位集體回踩，資金向估值具備安全邊際的超跌 SaaS 軟體與防禦性大健康輪動。密大消費者信心指數終值上修至 49.5，通膨預期下滑且 10 年期美債息走低至 4.372% 提供宏觀支撐。</li>
          <li><strong>資金流向：</strong>資金從半導體（MU、NVDA、AVGO、MRVL）及重電/電力基建（ETN、VST、CEG）撤出，重回微軟、蘋果、亞馬遜等大市值科技股，並瘋狂掃貨 SaaS 軟體（NOW、SNOW、CRM、PLTR）以及防禦板塊（XLV +3.03%、XLRE +1.46%）。</li>
          <li><strong>市場寬度：</strong>市場寬度維持健康，NYSE 上漲下跌比為 1.5:1，等權重指數顯著跑贏權重指數，說明指數微跌主因是半導體權重龍頭調整，市場實質賺錢效應良好。</li>
          <li><strong>一句話判斷：</strong><span class="text-emerald-500 font-semibold dark:text-emerald-400">晶片擁擠度高位降溫，超跌軟體與大健康板塊挺身而出，市場在羅素指數調整日完成良性輪動。</span></li>
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
            <tr class="text-zinc-500 dark:text-zinc-400 text-left">
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
              <td class="px-4 py-3 text-right">51,876.11</td>
              <td class="px-4 py-3 text-right text-rose-500 font-semibold">-0.09%</td>
              <td class="px-4 py-3 text-right">51,750 - 52,000</td>
              <td class="px-4 py-3 font-sans text-xs text-amber-500 font-semibold">小幅震盪，守穩 20MA，表現穩健</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold font-sans text-zinc-900 dark:text-zinc-100">S&P 500 (標普 500)</td>
              <td class="px-4 py-3 text-right">7,354.02</td>
              <td class="px-4 py-3 text-right text-rose-500 font-semibold">-0.05%</td>
              <td class="px-4 py-3 text-right">7,330 - 7,370</td>
              <td class="px-4 py-3 font-sans text-xs text-emerald-500 font-semibold">近乎持平，守住上升均線，防禦板塊撐盤</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold font-sans text-zinc-900 dark:text-zinc-100">Nasdaq Composite (納指)</td>
              <td class="px-4 py-3 text-right">25,297.62</td>
              <td class="px-4 py-3 text-right text-rose-500 font-semibold">-0.24%</td>
              <td class="px-4 py-3 text-right">25,150 - 25,450</td>
              <td class="px-4 py-3 font-sans text-xs text-amber-500 font-semibold">週線回調逾4.5%，晶片大跌與軟體反彈拉鋸</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold font-sans text-zinc-900 dark:text-zinc-100">Nasdaq 100 / QQQ</td>
              <td class="px-4 py-3 text-right">706.52</td>
              <td class="px-4 py-3 text-right text-rose-500 font-semibold">-1.38%</td>
              <td class="px-4 py-3 text-right">704.00 - 720.00</td>
              <td class="px-4 py-3 font-sans text-xs text-red-500 font-semibold">跌幅較大，受半導體權重板塊劇烈回撤拖累</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold font-sans text-zinc-900 dark:text-zinc-100">Russell 2000 / IWM</td>
              <td class="px-4 py-3 text-right">299.83</td>
              <td class="px-4 py-3 text-right text-emerald-500 font-semibold">+0.31%</td>
              <td class="px-4 py-3 text-right">297.00 - 302.00</td>
              <td class="px-4 py-3 font-sans text-xs text-emerald-500 font-semibold">逆市走強，美債息回落與羅素調整提振</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold font-sans text-zinc-900 dark:text-zinc-100">SOX 半導體指數</td>
              <td class="px-4 py-3 text-right">13,627.04</td>
              <td class="px-4 py-3 text-right text-rose-500 font-semibold">-5.64%</td>
              <td class="px-4 py-3 text-right">13,500 - 14,450</td>
              <td class="px-4 py-3 font-sans text-xs text-red-500 font-semibold">大幅重挫，晶片股獲利了結賣壓沉重，破月線</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold font-sans text-zinc-900 dark:text-zinc-100">VIX 波動率指數</td>
              <td class="px-4 py-3 text-right">18.41</td>
              <td class="px-4 py-3 text-right text-rose-500 font-semibold">-1.18%</td>
              <td class="px-4 py-3 text-right">18.00 - 19.50</td>
              <td class="px-4 py-3 font-sans text-xs text-emerald-500 font-semibold">略微降溫，恐慌情緒高位回落</td>
            </tr>
          </tbody>
        </table>
      </div>

      <div class="h-64 border border-zinc-200 dark:border-zinc-800 rounded-xl p-4 bg-white dark:bg-zinc-900">
        <canvas id="returnsChart"></canvas>
      </div>
    </section>

    <!-- 2. 盤中走勢復盤 -->
    <section id="timeline" class="mb-12 scroll-mt-6">
      <h2 class="text-2xl font-bold mb-4 flex items-center gap-2 border-b border-zinc-100 dark:border-zinc-800 pb-2">
        <span class="text-brand-500">2.</span> 盤中走勢復盤
      </h2>
      
      <div class="mermaid w-full flex justify-center mb-6">
        gantt
          title 2026-06-26 盤中走勢與事件傳導
          dateFormat HH:mm
          axisFormat %H:%M
          
          section 走勢與事件
          盤前: 密大消費者信心公布前，大盤情緒平穩 : 08:30, 09:30
          開盤低開: 科技股受晶片獲利了結拖累，但微軟蘋果強勢 : 09:30, 10:00
          經濟數據: 密大消費者信心終值49.5公佈，通膨預期降溫 : 10:00, 10:30
          午盤拉鋸: 半導體跌幅擴大，軟體股與醫療防禦板塊接棒 : 10:30, 15:30
          尾盤重編: 羅素重編生效，尾盤成交爆出史詩天量，指數跌幅收窄 : 15:30, 16:00
      </div>

      <div class="leading-relaxed text-zinc-600 dark:text-zinc-400 text-sm sm:text-base space-y-4">
        <p>
          <strong>開盤階段：</strong> 晶片龍頭美光科技（MU）在昨日強勢暴漲逾 15% 後，開盤即遭遇沉重的獲利回吐賣壓。Nvidia（NVDA）、Broadcom（AVGO）隨之走低，拖累 SOXX 費半大跌逾 3%。然而，微軟（MSFT）和蘋果（AAPL）因日前硬體調價引發的 Margin 焦慮已被市場充分消化，開盤大幅拉升，軟體 SaaS 板塊亦在 CRM 與 NOW 的帶領下報復性反彈，穩住了大盤指數。
        </p>
        <p>
          <strong>盤中數據公佈：</strong> 早上 10:00，美國公佈密西根大學消費者信心指數 6 官終值為 49.5，略高於初值 48.9，且一年期通膨預期下滑至 4.6%。此數據暗示通膨壓力並未失控，且有汽油價格回軟的緩解效應，10 年期美債收益率進一步回落至 4.372%。債息走軟刺激資金加速輪動至防禦板塊如 XLV（大健康 +3.03%）、XLRE（房地產）及高敏感度軟體板塊。
        </p>
        <p>
          <strong>尾盤羅素生效：</strong> 由於今日是羅素指數半年度重新編制（Russell Reconstitution）生效日，尾盤 30 分鐘大批被動基金進行頭寸調整，市場成交量呈幾何級數放大。納斯達克收盤交叉（Closing Cross）成交額創下 $3340 億美元的紀錄，大筆買盤在最後關頭湧入，推動微軟、蘋果等科技巨頭收盤於今日高點，大盤跌幅大舉收窄，順利完成「去硬件、補軟體」的頭寸大洗牌。
        </p>
      </div>
    </section>

    <!-- 3. 宏觀環境 -->
    <section id="macro" class="mb-12 scroll-mt-6">
      <h2 class="text-2xl font-bold mb-4 flex items-center gap-2 border-b border-zinc-100 dark:border-zinc-800 pb-2">
        <span class="text-brand-500">3.</span> 宏觀環境
      </h2>

      <div class="tabs flex flex-wrap border-b border-zinc-200 dark:border-zinc-800">
        <input type="radio" id="tab-yields" name="macro-tabs" checked>
        <label for="tab-yields" class="border-b-2">3.1 美債收益率</label>
        
        <input type="radio" id="tab-fed" name="macro-tabs">
        <label for="tab-fed" class="border-b-2">3.2 Fed 降息預期</label>
        
        <input type="radio" id="tab-commodities" name="macro-tabs">
        <label for="tab-commodities" class="border-b-2">3.3 匯市與大宗</label>
        
        <input type="radio" id="tab-data" name="macro-tabs">
        <label for="tab-data" class="border-b-2">3.4 當日經濟數據</label>

        <!-- Tab Panel 1 -->
        <div class="tab-panel w-full text-zinc-600 dark:text-zinc-400 text-sm sm:text-base leading-relaxed">
          <h4 class="font-bold text-zinc-800 dark:text-zinc-200 mb-2">短端利率回軟，收益率曲線溫和變動</h4>
          <p class="mb-2">
            美債收益率在平穩的通膨數據與消費者信心數據公佈後，短端收益率有所走軟，緩解了高估值板塊的折現率壓力：
          </p>
          <ul class="list-disc pl-5 space-y-1">
            <li><strong>2年期國債收益率：</strong> 下降至 4.62% 左右。</li>
            <li><strong>5年期國債收益率 (^FVX)：</strong> 收於 <strong>4.130%</strong> (前一交易日 4.163%)，下降 3.3 bps。</li>
            <li><strong>10年期國債收益率 (^TNX)：</strong> 收於 <strong>4.372%</strong> (前一交易日 4.392%)，下降 2.0 bps。</li>
            <li><strong>30年期國債收益率 (^TYX)：</strong> 收於 <strong>4.864%</strong> (前一交易日 4.858%)，微幅上升 0.6 bps。</li>
          </ul>
        </div>

        <!-- Tab Panel 2 -->
        <div class="tab-panel w-full text-zinc-600 dark:text-zinc-400 text-sm sm:text-base leading-relaxed">
          <h4 class="font-bold text-zinc-800 dark:text-zinc-200 mb-2">9月首次降息機率回升至 60% 以上</h4>
          <p>
            隨著密大調查顯示消費者一年期與五年期通膨預期雙雙回落（分別降至 4.6% 和 3.3%），加上昨日 PCE 符合預期，CME FedWatch 顯示 9 月份 FOMC 降息 25 bps 的概率回升至 63%。年內降息次數預期重回 1-2 次（累積 25-50 bps）。市場認為聯準會政策邊際正逐漸轉向溫和，這對高槓桿中小盤股及高成長 SaaS 股是一大利多。
          </p>
        </div>

        <!-- Tab Panel 3 -->
        <div class="tab-panel w-full text-zinc-600 dark:text-zinc-400 text-sm sm:text-base leading-relaxed">
          <h4 class="font-bold text-zinc-800 dark:text-zinc-200 mb-2">原油大跌 3.5%，黃金大漲，比特幣守穩 60k</h4>
          <p>
            <strong>WTI 原油 (USO)：</strong> 原油重歸跌勢，USO 暴跌 <strong>-3.50%</strong> 收於 <strong>$105.48</strong>，主要受需求放緩預期與全球庫存增加影響，有助於平抑通膨壓力。<br>
            <strong>黃金現貨 (GLD)：</strong> 債息與美元走軟，黃金顯著走強，GLD 收漲 <strong>+1.13%</strong> 報 <strong>$373.63</strong>。<br>
            <strong>美元指數 (UUP)：</strong> 美元溫和回軟，UUP 下跌 0.07% 報 <strong>28.46</strong>。<br>
            <strong>加密貨幣：</strong> 比特幣 (BTC) 與以太坊 (ETH) 於底部溫和震盪，BTC-USD 收漲 <strong>+0.53%</strong> 報 <strong>$60,024.3</strong>，收復 60k；ETH-USD 上漲 <strong>+0.75%</strong> 報 <strong>$1,576.62</strong>。
          </p>
        </div>

        <!-- Tab Panel 4 -->
        <div class="tab-panel w-full text-zinc-600 dark:text-zinc-400 text-sm sm:text-base leading-relaxed">
          <h4 class="font-bold text-zinc-800 dark:text-zinc-200 mb-2">6月密西根大學消費者信心指數終值上修</h4>
          <p class="mb-3">
            今日公佈了美國重要宏觀調查數據：
          </p>
          <ul class="list-disc pl-5 space-y-1 mb-3">
            <li><strong>密大消費者信心指數終值：</strong> 實際值 **49.5**，預期值 50.0，前值 48.9 (初值)。</li>
            <li><strong>消費者現況指數：</strong> 實際值 **47.7**，高於前值 45.8。</li>
            <li><strong>消費者預期指數：</strong> 實際值 **50.7**，高於前值 44.1。</li>
            <li><strong>一年期通膨預期：</strong> 降至 **4.6%** (5月為 4.8%)。</li>
            <li><strong>五年期通膨預期：</strong> 降至 **3.3%**。</li>
          </ul>
          <div class="text-xs text-zinc-400 border-t border-zinc-100 dark:border-zinc-800 pt-2">
            > [!NOTE]
            > 雖然消費者信心仍受高物價壓制，但燃料及汽油價格的回落為預期帶來明顯修復，通膨預期的下滑進一步消除了市場對核心通膨反彈的擔憂。
          </div>
        </div>
      </div>
    </section>

    <!-- 4. 板塊表現 -->
    <section id="sectors" class="mb-12 scroll-mt-6">
      <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-4 mb-4 border-b border-zinc-100 dark:border-zinc-800 pb-2">
        <h2 class="text-2xl font-bold flex items-center gap-2">
          <span class="text-brand-500">4.</span> S&P 500 十一個板塊表現 (2026-06-26)
        </h2>
        <input type="text" id="sectorSearch" placeholder="搜尋板塊或 ETF..." class="px-3 py-1.5 text-sm rounded-md border border-zinc-300 dark:border-zinc-700 bg-white dark:bg-zinc-900 focus:outline-none focus:ring-1 focus:ring-brand-500">
      </div>

      <div class="overflow-x-auto border border-zinc-200 dark:border-zinc-800 rounded-xl mb-4">
        <table class="min-w-full divide-y divide-zinc-200 dark:divide-zinc-855 text-sm" id="sectorsTable">
          <thead class="bg-zinc-50 dark:bg-zinc-900 text-zinc-500 dark:text-zinc-400">
            <tr>
              <th class="px-4 py-3 font-semibold text-left cursor-pointer" onclick="sortSectors(0)">排名 ↕</th>
              <th class="px-4 py-3 font-semibold text-left cursor-pointer" onclick="sortSectors(1)">板塊 ↕</th>
              <th class="px-4 py-3 font-semibold text-left cursor-pointer" onclick="sortSectors(2)">ETF ↕</th>
              <th class="px-4 py-3 font-semibold text-right cursor-pointer" onclick="sortSectors(3)">當日漲跌幅 ↕</th>
              <th class="px-4 py-3 font-semibold text-right cursor-pointer" onclick="sortSectors(4)">跑贏/跑輸標普 ↕</th>
              <th class="px-4 py-3 font-semibold text-left">主要驅動因素</th>
            </tr>
          </thead>
          <tbody class="divide-y divide-zinc-200 dark:divide-zinc-855 font-mono text-zinc-700 dark:text-zinc-300">
            <tr class="hover:bg-zinc-50/50 dark:hover:bg-zinc-900/30">
              <td class="px-4 py-3 font-semibold">1</td>
              <td class="px-4 py-3 font-sans font-medium text-zinc-900 dark:text-zinc-100">Health Care (醫療保健)</td>
              <td class="px-4 py-3">XLV</td>
              <td class="px-4 py-3 text-right text-emerald-500 font-semibold" data-val="3.03">+3.03%</td>
              <td class="px-4 py-3 text-right text-emerald-500 font-semibold" data-val="3.08">+3.08%</td>
              <td class="px-4 py-3 font-sans text-xs">大盤科技股劇烈震盪，避險資金瘋狂掃貨大型藥企，板塊創近期最大單日漲幅</td>
            </tr>
            <tr class="hover:bg-zinc-50/50 dark:hover:bg-zinc-900/30">
              <td class="px-4 py-3 font-semibold">2</td>
              <td class="px-4 py-3 font-sans font-medium text-zinc-900 dark:text-zinc-100">Real Estate (房地產)</td>
              <td class="px-4 py-3">XLRE</td>
              <td class="px-4 py-3 text-right text-emerald-500 font-semibold" data-val="1.46">+1.46%</td>
              <td class="px-4 py-3 text-right text-emerald-500 font-semibold" data-val="1.51">+1.51%</td>
              <td class="px-4 py-3 font-sans text-xs">美債 10 年期收益率回落至 4.372%，高敏感度信託與高股息地產大幅受惠</td>
            </tr>
            <tr class="hover:bg-zinc-50/50 dark:hover:bg-zinc-900/30">
              <td class="px-4 py-3 font-semibold">3</td>
              <td class="px-4 py-3 font-sans font-medium text-zinc-900 dark:text-zinc-100">Consumer Staples (必需消費)</td>
              <td class="px-4 py-3">XLP</td>
              <td class="px-4 py-3 text-right text-emerald-500 font-semibold" data-val="0.92">+0.92%</td>
              <td class="px-4 py-3 text-right text-emerald-500 font-semibold" data-val="0.97">+0.97%</td>
              <td class="px-4 py-3 font-sans text-xs">密大信心顯示通膨預期下滑且汽油回軟，支撐大型超市與零售巨頭</td>
            </tr>
            <tr class="hover:bg-zinc-50/50 dark:hover:bg-zinc-900/30">
              <td class="px-4 py-3 font-semibold">4</td>
              <td class="px-4 py-3 font-sans font-medium text-zinc-900 dark:text-zinc-100">Consumer Discretionary (非必需消費)</td>
              <td class="px-4 py-3">XLY</td>
              <td class="px-4 py-3 text-right text-emerald-500 font-semibold" data-val="0.90">+0.90%</td>
              <td class="px-4 py-3 text-right text-emerald-500 font-semibold" data-val="0.95">+0.95%</td>
              <td class="px-4 py-3 font-sans text-xs">亞馬遜大反彈 +2.50%，對沖了汽車零售的疲軟，市場對消費預期改善</td>
            </tr>
            <tr class="hover:bg-zinc-50/50 dark:hover:bg-zinc-900/30">
              <td class="px-4 py-3 font-semibold">5</td>
              <td class="px-4 py-3 font-sans font-medium text-zinc-900 dark:text-zinc-100">Utilities (公用事業)</td>
              <td class="px-4 py-3">XLU</td>
              <td class="px-4 py-3 text-right text-emerald-500 font-semibold" data-val="0.76">+0.76%</td>
              <td class="px-4 py-3 text-right text-emerald-500 font-semibold" data-val="0.81">+0.81%</td>
              <td class="px-4 py-3 font-sans text-xs">債息下行背景下，資金對高股息公用板塊進行防守性配置</td>
            </tr>
            <tr class="hover:bg-zinc-50/50 dark:hover:bg-zinc-900/30">
              <td class="px-4 py-3 font-semibold">6</td>
              <td class="px-4 py-3 font-sans font-medium text-zinc-900 dark:text-zinc-100">Communication Services (通訊)</td>
              <td class="px-4 py-3">XLC</td>
              <td class="px-4 py-3 text-right text-emerald-500 font-semibold" data-val="0.57">+0.57%</td>
              <td class="px-4 py-3 text-right text-emerald-500 font-semibold" data-val="0.62">+0.62%</td>
              <td class="px-4 py-3 font-sans text-xs">Meta (+1.36%) 與大型科技回升，成功對沖了 Alphabet (-1.84%) 的下跌</td>
            </tr>
            <tr class="hover:bg-zinc-50/50 dark:hover:bg-zinc-900/30">
              <td class="px-4 py-3 font-semibold">7</td>
              <td class="px-4 py-3 font-sans font-medium text-zinc-900 dark:text-zinc-100">Financials (金融)</td>
              <td class="px-4 py-3">XLF</td>
              <td class="px-4 py-3 text-right text-emerald-500 font-semibold" data-val="0.22">+0.22%</td>
              <td class="px-4 py-3 text-right text-emerald-500 font-semibold" data-val="0.27">+0.27%</td>
              <td class="px-4 py-3 font-sans text-xs">壓力測試結果提振力道延續，大行在指數調整日迎來被動買盤托盤</td>
            </tr>
            <tr class="hover:bg-zinc-50/50 dark:hover:bg-zinc-900/30">
              <td class="px-4 py-3 font-semibold">8</td>
              <td class="px-4 py-3 font-sans font-medium text-zinc-900 dark:text-zinc-100">Materials (原物料)</td>
              <td class="px-4 py-3">XLB</td>
              <td class="px-4 py-3 text-right text-rose-500 font-semibold" data-val="-0.46">-0.46%</td>
              <td class="px-4 py-3 text-right text-rose-500 font-semibold" data-val="-0.41">-0.41%</td>
              <td class="px-4 py-3 font-sans text-xs">商品市場價格分化，有色金屬與採礦股面臨整理壓力</td>
            </tr>
            <tr class="hover:bg-zinc-50/50 dark:hover:bg-zinc-900/30">
              <td class="px-4 py-3 font-semibold">9</td>
              <td class="px-4 py-3 font-sans font-medium text-zinc-900 dark:text-zinc-100">Energy (能源)</td>
              <td class="px-4 py-3">XLE</td>
              <td class="px-4 py-3 text-right text-rose-500 font-semibold" data-val="-0.46">-0.46%</td>
              <td class="px-4 py-3 text-right text-rose-500 font-semibold" data-val="-0.41">-0.41%</td>
              <td class="px-4 py-3 font-sans text-xs">WTI 原油重挫 3.5% 拖累採油設備與能源股，板塊迎來技術性調整</td>
            </tr>
            <tr class="hover:bg-zinc-50/50 dark:hover:bg-zinc-900/30">
              <td class="px-4 py-3 font-semibold">10</td>
              <td class="px-4 py-3 font-sans font-medium text-zinc-900 dark:text-zinc-100">Industrials (工業)</td>
              <td class="px-4 py-3">XLI</td>
              <td class="px-4 py-3 text-right text-rose-500 font-semibold" data-val="-1.59">-1.59%</td>
              <td class="px-4 py-3 text-right text-rose-500 font-semibold" data-val="-1.54">-1.54%</td>
              <td class="px-4 py-3 font-sans text-xs">前期大漲的重電基建（ETN、GEV、PWR）遭遇高位結利拋售，拖累工業板塊</td>
            </tr>
            <tr class="hover:bg-zinc-50/50 dark:hover:bg-zinc-900/30">
              <td class="px-4 py-3 font-semibold">11</td>
              <td class="px-4 py-3 font-sans font-medium text-zinc-900 dark:text-zinc-100">Technology (資訊科技)</td>
              <td class="px-4 py-3">XLK</td>
              <td class="px-4 py-3 text-right text-rose-500 font-semibold" data-val="-1.87">-1.87%</td>
              <td class="px-4 py-3 text-right text-rose-500 font-semibold" data-val="-1.82">-1.82%</td>
              <td class="px-4 py-3 font-sans text-xs">半導體板塊（SOXX -5.64%）大暴跌，即使微軟蘋果強彈亦難擋板塊深幅拉回</td>
            </tr>
          </tbody>
        </table>
      </div>
      <p class="text-xs text-zinc-400 italic font-sans leading-relaxed">
        * 註：表格支持點擊表頭按數值或字母進行即時排序。市場資金經歷了猛烈的流出科技與工業、流向醫療大健康的「大搬家」。
      </p>
    </section>

    <!-- 5. 主題與風格表現 -->
    <section id="themes" class="mb-12 scroll-mt-6">
      <h2 class="text-2xl font-bold mb-4 flex items-center gap-2 border-b border-zinc-100 dark:border-zinc-800 pb-2">
        <span class="text-brand-500">5.</span> 主題與風格表現
      </h2>
      <div class="grid grid-cols-1 md:grid-cols-2 gap-6 text-sm leading-relaxed text-zinc-650 dark:text-zinc-450">
        <div class="bg-zinc-50/30 dark:bg-zinc-900/10 p-5 rounded-xl border border-zinc-150 dark:border-zinc-850">
          <h4 class="font-bold text-zinc-800 dark:text-zinc-200 mb-2">AI 晶片與半導體 (SMH / SOXX): 利好出盡重挫，費半跌破 5.6%</h4>
          <p>
            美光科技（MU -6.69%）劇烈回踩，宣佈晶片股短期估值擁擠度達頂部。SOXX 暴瀉 5.64%，SMH 跌 3.97%。Nvidia (NVDA) 跌 1.64% 守住關鍵整數關，ASML (-2.53%)、AMD (-2.06%)、AVGO (-3.67%) 全線退潮，資金短期進行避險清倉。
          </p>
        </div>
        <div class="bg-zinc-50/30 dark:bg-zinc-900/10 p-5 rounded-xl border border-zinc-150 dark:border-zinc-850">
          <h4 class="font-bold text-zinc-800 dark:text-zinc-200 mb-2">軟體與 SaaS 板塊 (IGV): 報復性爆發，板塊暴漲 4.06%</h4>
          <p>
            超跌的軟體 SaaS 板塊迎來救贖行情，iShares 軟體 ETF（IGV）暴漲 4.06%。在晶片股大跌的情況下，資金大舉回流。ServiceNow (NOW) 暴漲 9.85%，Snowflake (SNOW) 狂飆 9.65%，Salesforce (CRM) 大漲 5.45%，板塊迎來估值低位修復。
          </p>
        </div>
        <div class="bg-zinc-50/30 dark:bg-zinc-900/10 p-5 rounded-xl border border-zinc-150 dark:border-zinc-850">
          <h4 class="font-bold text-zinc-800 dark:text-zinc-200 mb-2">重電電力與基建: 遭遇高位結利拋售</h4>
          <p>
            前期強勢的 AI 重電設備股今日全面拉回。伊頓 (ETN) 下跌 4.09%，GEV 下跌 3.71%，液冷巨頭 VRT 大跌 6.64% 領跌，顯示高位投機性資金在 Russell Reconstitution 日進行了較大的頭寸減持。
          </p>
        </div>
        <div class="bg-zinc-50/30 dark:bg-zinc-900/10 p-5 rounded-xl border border-zinc-150 dark:border-zinc-850">
          <h4 class="font-bold text-zinc-800 dark:text-zinc-200 mb-2">羅素 2000 與等權標普: 表現亮眼</h4>
          <p>
            由於美債 10 年期收益率降至 4.372%，加上 PCE 數據平穩及密大通膨預期下滑，中小盤股逆市上揚 0.31%。等權重標普大幅跑贏標普 500 權重指數，顯示大盤內部廣度實質好轉，並非恐慌性普跌。
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
          <div class="text-2xl font-bold font-mono text-zinc-900 dark:text-zinc-100">S&P 500: 55%</div>
          <div class="text-zinc-400 dark:text-zinc-500 text-xs mt-1">Nasdaq 100: 40%</div>
        </div>
        <div class="bg-zinc-50/50 dark:bg-zinc-900/40 p-4 rounded-xl border border-zinc-200 dark:border-zinc-800 text-center">
          <div class="text-zinc-400 dark:text-zinc-500 font-bold uppercase tracking-wider text-xs mb-1">上漲/下跌家數 (NYSE)</div>
          <div class="text-2xl font-bold font-mono text-emerald-500 dark:text-emerald-400">1,820 : 1,210</div>
          <div class="text-zinc-400 dark:text-zinc-500 text-xs mt-1">比例: 1.50 (買盤占優)</div>
        </div>
        <div class="bg-zinc-50/50 dark:bg-zinc-900/40 p-4 rounded-xl border border-zinc-200 dark:border-zinc-800 text-center">
          <div class="text-zinc-400 dark:text-zinc-500 font-bold uppercase tracking-wider text-xs mb-1">52週新高 - 新低差值</div>
          <div class="text-2xl font-bold font-mono text-emerald-500 dark:text-emerald-400">+82</div>
          <div class="text-zinc-400 dark:text-zinc-500 text-xs mt-1">NYSE 新高 112 / 新低 30</div>
        </div>
      </div>
      <p class="text-sm leading-relaxed text-zinc-650 dark:text-zinc-350">
        儘管納斯達克 100 指數因晶片股拖累表現不佳，但全市場上漲家數顯著多於下跌家數。上漲/下跌家數比（A/D Ratio）在 NYSE 達到 1.50，主要是資金回流中低位股票及防禦保健板塊，大盤未現系統性恐慌。
      </p>
    </section>

    <!-- 7. 技術面分析 -->
    <section id="technical" class="mb-12 scroll-mt-6">
      <h2 class="text-2xl font-bold mb-4 flex items-center gap-2 border-b border-zinc-100 dark:border-zinc-800 pb-2">
        <span class="text-brand-500">7.</span> 技術面分析
      </h2>
      
      <div class="overflow-x-auto border border-zinc-200 dark:border-zinc-800 rounded-xl mb-4">
        <table class="min-w-full divide-y divide-zinc-200 dark:divide-zinc-850 text-sm">
          <thead class="bg-zinc-50 dark:bg-zinc-900">
            <tr class="text-zinc-550 dark:text-zinc-400 text-left">
              <th class="px-4 py-3 font-semibold">ETF 名稱</th>
              <th class="px-4 py-3 font-semibold text-right">最新價格</th>
              <th class="px-4 py-3 font-semibold text-right">20MA</th>
              <th class="px-4 py-3 font-semibold text-right">50MA</th>
              <th class="px-4 py-3 font-semibold text-right">RSI (14)</th>
              <th class="px-4 py-3 font-semibold text-right">關鍵支撐</th>
              <th class="px-4 py-3 font-semibold text-right">關鍵壓力</th>
              <th class="px-4 py-3 font-semibold text-left">技術狀態與操作策略</th>
            </tr>
          </thead>
          <tbody class="divide-y divide-zinc-200 dark:divide-zinc-850 font-mono text-zinc-700 dark:text-zinc-300">
            <tr>
              <td class="px-4 py-3 font-semibold font-sans text-zinc-900 dark:text-zinc-100">SPY (標普 500)</td>
              <td class="px-4 py-3 text-right">728.99</td>
              <td class="px-4 py-3 text-right">730.20</td>
              <td class="px-4 py-3 text-right">715.50</td>
              <td class="px-4 py-3 text-right">51</td>
              <td class="px-4 py-3 text-right">725.00</td>
              <td class="px-4 py-3 text-right">736.00</td>
              <td class="px-4 py-3 font-sans text-xs text-amber-500">跌破20MA但收盤收復大半，RSI中性，維持區間震盪</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold font-sans text-zinc-900 dark:text-zinc-100">QQQ (納指 100)</td>
              <td class="px-4 py-3 text-right">706.52</td>
              <td class="px-4 py-3 text-right">710.80</td>
              <td class="px-4 py-3 text-right">695.10</td>
              <td class="px-4 py-3 text-right">46</td>
              <td class="px-4 py-3 text-right">700.00</td>
              <td class="px-4 py-3 text-right">718.00</td>
              <td class="px-4 py-3 font-sans text-xs text-red-500">短線失守20MA，MACD高位死叉，面臨均線級別回調</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold font-sans text-zinc-900 dark:text-zinc-100">IWM (羅素 2000)</td>
              <td class="px-4 py-3 text-right">299.83</td>
              <td class="px-4 py-3 text-right">295.40</td>
              <td class="px-4 py-3 text-right">290.20</td>
              <td class="px-4 py-3 text-right">54</td>
              <td class="px-4 py-3 text-right">295.00</td>
              <td class="px-4 py-3 text-right">304.00</td>
              <td class="px-4 py-3 font-sans text-xs text-emerald-500">逆勢走高，MACD金叉，形成底部向上突破走勢</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold font-sans text-zinc-900 dark:text-zinc-100">SMH (半導體)</td>
              <td class="px-4 py-3 text-right">611.61</td>
              <td class="px-4 py-3 text-right">620.50</td>
              <td class="px-4 py-3 text-right">580.20</td>
              <td class="px-4 py-3 text-right">48</td>
              <td class="px-4 py-3 text-right">600.00</td>
              <td class="px-4 py-3 text-right">635.00</td>
              <td class="px-4 py-3 font-sans text-xs text-red-500">跌破20MA，回踩50MA支撐，高位洗盤，暫停追高</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold font-sans text-zinc-900 dark:text-zinc-100">IGV (軟體)</td>
              <td class="px-4 py-3 text-right">88.20</td>
              <td class="px-4 py-3 text-right">85.10</td>
              <td class="px-4 py-3 text-right">87.00</td>
              <td class="px-4 py-3 text-right">53</td>
              <td class="px-4 py-3 text-right">84.00</td>
              <td class="px-4 py-3 text-right">90.00</td>
              <td class="px-4 py-3 font-sans text-xs text-emerald-500">強勢突破50MA，底部雙底確立，MACD低位金叉向上</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold font-sans text-zinc-900 dark:text-zinc-100">XLK (科技股)</td>
              <td class="px-4 py-3 text-right">181.11</td>
              <td class="px-4 py-3 text-right">183.40</td>
              <td class="px-4 py-3 text-right">178.60</td>
              <td class="px-4 py-3 text-right">49</td>
              <td class="px-4 py-3 text-right">178.00</td>
              <td class="px-4 py-3 text-right">186.00</td>
              <td class="px-4 py-3 font-sans text-xs text-amber-500">隨費半走弱，考驗50MA，短期均線有糾纏震盪之虞</td>
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
        <details class="group bg-zinc-50 dark:bg-zinc-900/50 p-4 rounded-xl border border-zinc-200/80 dark:border-zinc-800/80">
          <summary class="font-bold text-zinc-800 dark:text-zinc-200">8.1 大型科技七巨頭 (MSFT & AAPL 引領強勢反彈)</summary>
          <div class="mt-3 text-sm text-zinc-600 dark:text-zinc-400 leading-relaxed space-y-2">
            <p>
              <strong>MSFT (微軟) (+5.71%, $372.97):</strong> 宣佈收購傳聞與 Azure 大客戶雲端訂單激增，加上 SaaS 板塊大反彈，微軟成為今日最耀眼巨頭，成功收復月線。
            </p>
            <p>
              <strong>AAPL (蘋果) (+3.14%, $283.78):</strong> 日前因記憶體組件調漲售價引發的需求擔憂被大摩等投行報告化解，投行稱 AI 功能（Apple Intelligence）的剛需將維持高升級率，吸引低位買盤。
            </p>
            <p>
              <strong>AMZN (亞馬遜) (+2.50%, $232.69):</strong> 雲端運算 (AWS) 利潤率預期改善，股價探底回升。
            </p>
            <p>
              <strong>GOOGL (Alphabet) (-1.84%, $337.39):</strong> DeepMind 部門因人才外流和內部重組問題引發市場對其 AI 領先地位的質質，股價逆市走跌。
            </p>
          </div>
        </details>

        <details class="group bg-zinc-50 dark:bg-zinc-900/50 p-4 rounded-xl border border-zinc-200/80 dark:border-zinc-800/80">
          <summary class="font-bold text-zinc-800 dark:text-zinc-200">8.2 AI 硬體 / 半導體重點股異動分析 (美光大跌, 擁擠度去化)</summary>
          <div class="mt-3 text-sm text-zinc-600 dark:text-zinc-400 leading-relaxed space-y-2">
            <p>
              <strong>MU (美光科技) (-6.69%, $1,132.33):</strong> 昨日暴漲 15.8% 後利多出盡，股價深幅拉回。雖然 HBM 產能售罄至 2027 年，但短線獲利盤湧出，引領晶片股退潮。
            </p>
            <p>
              <strong>NVDA (輝達) (-1.64%, $192.53):</strong> 一度跌穿 $190，尾盤在被動基金調整中獲資金托盤，跌幅收窄，暫受守 50MA 上方。
            </p>
            <p>
              <strong>AVGO (博通) (-3.67%, $365.02) & MRVL (馬威爾) (-5.15%, $266.77):</strong> 晶片硬體概念股全面殺估值，資金轉出。
            </p>
          </div>
        </details>

        <details class="group bg-zinc-50 dark:bg-zinc-900/50 p-4 rounded-xl border border-zinc-200/80 dark:border-zinc-800/80">
          <summary class="font-bold text-zinc-800 dark:text-zinc-200">8.3 軟體 / SaaS / AI 應用重點股異動分析 (NOW, SNOW, CRM 井噴)</summary>
          <div class="mt-3 text-sm text-zinc-600 dark:text-zinc-400 leading-relaxed space-y-2">
            <p>
              <strong>NOW (ServiceNow) (+9.85%, $98.34):</strong> 雲端工作流 AI 工具需求爆發，昨日暴跌後迎來強力空頭擠壓（Short Squeeze），暴漲近 10%。
            </p>
            <p>
              <strong>SNOW (Snowflake) (+9.65%, $248.96):</strong> 數據倉庫需求強勁，吸引前期低配的共同基金，股價創單日最大漲幅。
            </p>
            <p>
              <strong>CRM (Salesforce) (+5.45%, $158.37):</strong> Agentic AI 產品線定價權確認，低估值優勢吸引機構買盤。
            </p>
            <p>
              <strong>PLTR (Palantir) (+5.28%, $112.93):</strong> 國防及商業大單續簽，股價持續走強。
            </p>
          </div>
        </details>

        <details class="group bg-zinc-50 dark:bg-zinc-900/50 p-4 rounded-xl border border-zinc-200/80 dark:border-zinc-800/80">
          <summary class="font-bold text-zinc-800 dark:text-zinc-200">8.4 AI 電力 / 資料中心 / 能源基礎設施重點股分析 (重電調整)</summary>
          <div class="mt-3 text-sm text-zinc-600 dark:text-zinc-400 leading-relaxed space-y-2">
            <p>
              <strong>ETN (伊頓) (-4.09%, $402.68):</strong> 工業基建龍頭在連漲後，今日遭遇大單賣出，資金獲利回吐，回踩 20MA。
            </p>
            <p>
              <strong>VRT (維諦) (-6.64%, $303.95):</strong> 液冷散熱題材短期超買嚴重，今日大瀉近 7%，回補先前缺口。
            </p>
            <p>
              <strong>GEV (GE Vernova) (-3.71%, $1,045.17) & CEG (星座能源) (-1.74%, $264.02):</strong> 電網及核能發電題材高位震盪，分化加劇。
            </p>
          </div>
        </details>
      </div>
    </section>

    <!-- 9. 財報日曆與解讀 -->
    <section id="earnings" class="mb-12 scroll-mt-6">
      <h2 class="text-2xl font-bold mb-4 flex items-center gap-2 border-b border-zinc-100 dark:border-zinc-800 pb-2">
        <span class="text-brand-500">9.</span> 財報日曆與解讀
      </h2>
      <div class="bg-zinc-50 dark:bg-zinc-900/60 p-6 rounded-xl border border-zinc-200 dark:border-zinc-800 text-sm sm:text-base leading-relaxed">
        <h4 class="font-bold text-zinc-800 dark:text-zinc-200 mb-2">9.1 昨夜公佈財報解讀 (美光業績消化)</h4>
        <p class="mb-4">
          美光科技（MU）公佈的強勁財報在昨日刺激股價飆升 15.8% 後，今日出現「利多兌現」的回撤。大行分析指出，HBM 產能的完全售罄至 2027 年已是不爭的事實，但短期因存儲荒反噬下游（推升微軟、蘋果成本）所造成的科技巨頭震盪，限制了晶片板塊的進一步上攻，造成短期震盪。
        </p>
        <h4 class="font-bold text-zinc-800 dark:text-zinc-200 mb-2">9.2 接下來重要財報日曆</h4>
        <p>
          下週將進入 6 月底的相對財報真空期。市場關注點將逐漸轉移至 7 月中旬開啟的 Q2 財報季，屆時金融巨頭（JPM、BAC）與科技巨頭的實際利潤率表現將是決定大盤能否突破歷史高點的關鍵。
        </p>
      </div>
    </section>

    <!-- 10. 機構觀點與資金流 -->
    <section id="institution" class="mb-12 scroll-mt-6">
      <h2 class="text-2xl font-bold mb-4 flex items-center gap-2 border-b border-zinc-100 dark:border-zinc-800 pb-2">
        <span class="text-brand-500">10.</span> 機構觀點與資金流
      </h2>
      <div class="grid grid-cols-1 md:grid-cols-2 gap-6 text-sm leading-relaxed text-zinc-650 dark:text-zinc-350">
        <div class="bg-zinc-50/50 dark:bg-zinc-900/30 p-5 rounded-xl border border-zinc-200/60 dark:border-zinc-800/60">
          <h4 class="font-bold text-zinc-850 dark:text-zinc-200 mb-2">羅素指數重編引發史詩級成交量</h4>
          <p>
            高盛交易台報告指出，今日是 **Russell Reconstitution（羅素指數半年度調整）** 生效日。尾盤指數基金進行被動換倉，導致納斯達克和紐交所的收盤交叉（Closing Cross）成交量暴增至創紀錄的 $334B。機構透露，今天大型科技股尾盤的急拉和半導體的被動減持，很大程度是由於指數權重調整被動交易引發的資金洗牌。
          </p>
        </div>
        <div class="bg-zinc-50/50 dark:bg-zinc-900/30 p-5 rounded-xl border border-zinc-200/60 dark:border-zinc-800/60">
          <h4 class="font-bold text-zinc-850 dark:text-zinc-200 mb-2">機構對「軟硬輪動」持積極態度</h4>
          <p>
            摩根大通宏觀策略師表示，資金從擁擠的 AI 晶片硬體股，輪動到低估值的 SaaS 軟體（如 CRM、NOW）和醫療防禦板塊，是牛市健康發展的特徵。晶片股高位去擁擠化，能有效降低市場的短線系統性風險，為大盤提供了長線的承接底座，並非牛市結束。
          </p>
        </div>
      </div>
    </section>

    <!-- 11. 板塊輪動判斷 -->
    <section id="rotation" class="mb-12 scroll-mt-6">
      <h2 class="text-2xl font-bold mb-4 flex items-center gap-2 border-b border-zinc-100 dark:border-zinc-800 pb-2">
        <span class="text-brand-500">11.</span> 板塊輪動判斷
      </h2>
      <div class="bg-zinc-50 dark:bg-zinc-900 p-6 rounded-2xl border border-zinc-200 dark:border-zinc-800 leading-relaxed text-sm sm:text-base text-zinc-700 dark:text-zinc-300">
        <p class="mb-3">
          當前市場資金的輪動呈現出清晰的<strong>「軟硬交替、防禦托底」</strong>特徵：
        </p>
        <ol class="list-decimal pl-5 space-y-2">
          <li><strong>晶片與基建高位休整：</strong> AI 硬體板塊（半導體、重電基建）由於短線漲幅巨大、籌碼擁擠，正經歷良性的去槓桿和獲利了結。</li>
          <li><strong>SaaS 軟體迎來修復：</strong> 經歷了數月殺估值的軟體股（CRM、NOW、SNOW）在估值回歸合理區間後，吸引了原本配置在半導體的輪動資金，短線爆發力強。</li>
          <li><strong>大健康與防禦托盤：</strong> XLV 板塊大漲 3.03% 說明避險資金在大盤科技股大洗牌之際，積極流入高股息、穩健的醫藥巨頭，確保了大盤指數不出現恐慌性重挫。</li>
        </ol>
      </div>
    </section>

    <!-- 12. 重點關注股觀察 -->
    <section id="watchlist" class="mb-12 scroll-mt-6">
      <h2 class="text-2xl font-bold mb-4 flex items-center gap-2 border-b border-zinc-100 dark:border-zinc-800 pb-2">
        <span class="text-brand-500">12.</span> 重點關注股觀察
      </h2>
      
      <div class="overflow-x-auto border border-zinc-200 dark:border-zinc-800 rounded-xl mb-4">
        <table class="min-w-full divide-y divide-zinc-200 dark:divide-zinc-850 text-sm">
          <thead class="bg-zinc-50 dark:bg-zinc-900">
            <tr class="text-zinc-550 dark:text-zinc-400 text-left">
              <th class="px-4 py-3 font-semibold">代號</th>
              <th class="px-4 py-3 font-semibold text-right">當日收盤</th>
              <th class="px-4 py-3 font-semibold text-right">漲跌幅</th>
              <th class="px-4 py-3 font-semibold text-center">決策判定標籤</th>
              <th class="px-4 py-3 font-semibold">觀察與交易策略</th>
            </tr>
          </thead>
          <tbody class="divide-y divide-zinc-200 dark:divide-zinc-850 font-mono text-zinc-700 dark:text-zinc-300">
            <tr>
              <td class="px-4 py-3 font-semibold font-sans">NVDA</td>
              <td class="px-4 py-3 text-right">192.53</td>
              <td class="px-4 py-3 text-right text-rose-500">-1.64%</td>
              <td class="px-4 py-3 text-center"><span class="px-2 py-0.5 rounded bg-blue-100 dark:bg-blue-950 text-blue-800 dark:text-blue-350 text-xs font-semibold">回踩支撐</span></td>
              <td class="px-4 py-3 font-sans text-xs">跟隨費半回撤，在 50MA 上方有明顯承接，注意 $190 整數關口支撐</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold font-sans">AMD</td>
              <td class="px-4 py-3 text-right">521.58</td>
              <td class="px-4 py-3 text-right text-rose-500">-2.06%</td>
              <td class="px-4 py-3 text-center"><span class="px-2 py-0.5 rounded bg-blue-100 dark:bg-blue-950 text-blue-800 dark:text-blue-350 text-xs font-semibold">回踩支撐</span></td>
              <td class="px-4 py-3 font-sans text-xs">隨板塊回調，目前於 $520 附近震盪，等待成交量萎縮的止跌信號</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold font-sans">AVGO</td>
              <td class="px-4 py-3 text-right">365.02</td>
              <td class="px-4 py-3 text-right text-rose-500">-3.67%</td>
              <td class="px-4 py-3 text-center"><span class="px-2 py-0.5 rounded bg-amber-100 dark:bg-amber-950 text-amber-800 dark:text-amber-350 text-xs font-semibold">高位震盪</span></td>
              <td class="px-4 py-3 font-sans text-xs">大漲過後遭遇估值清洗，考驗下方的 $360 均線支撐，先觀望</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold font-sans">MRVL</td>
              <td class="px-4 py-3 text-right">266.77</td>
              <td class="px-4 py-3 text-right text-rose-500">-5.15%</td>
              <td class="px-4 py-3 text-center"><span class="px-2 py-0.5 rounded bg-blue-100 dark:bg-blue-950 text-blue-800 dark:text-blue-350 text-xs font-semibold">回踩支撐</span></td>
              <td class="px-4 py-3 font-sans text-xs">大起大落，今日吞噬昨日大部分漲幅，考驗前期平台支撐，觀望為主</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold font-sans">GOOGL</td>
              <td class="px-4 py-3 text-right">337.39</td>
              <td class="px-4 py-3 text-right text-rose-500">-1.84%</td>
              <td class="px-4 py-3 text-center"><span class="px-2 py-0.5 rounded bg-gray-100 dark:bg-gray-800 text-gray-800 dark:text-gray-300 text-xs font-semibold">需要觀察</span></td>
              <td class="px-4 py-3 font-sans text-xs">巨頭中表現偏弱，受 DeepMind 重組消息拖累，目前跌破短期均線</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold font-sans">MSFT</td>
              <td class="px-4 py-3 text-right">372.97</td>
              <td class="px-4 py-3 text-right text-emerald-500">+5.71%</td>
              <td class="px-4 py-3 text-center"><span class="px-2 py-0.5 rounded bg-emerald-100 dark:bg-emerald-950 text-emerald-800 dark:text-emerald-350 text-xs font-semibold">繼續強勢</span></td>
              <td class="px-4 py-3 font-sans text-xs">大漲收復失地，Azure 預期與軟體買盤暴增，收在今日高點，多頭結構完整</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold font-sans">META</td>
              <td class="px-4 py-3 text-right">550.25</td>
              <td class="px-4 py-3 text-right text-emerald-500">+1.36%</td>
              <td class="px-4 py-3 text-center"><span class="px-2 py-0.5 rounded bg-amber-100 dark:bg-amber-950 text-amber-800 dark:text-amber-350 text-xs font-semibold">高位震盪</span></td>
              <td class="px-4 py-3 font-sans text-xs">窄幅收紅，維持在 $540 - $560 平台，等待方向選擇</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold font-sans">AMZN</td>
              <td class="px-4 py-3 text-right">232.69</td>
              <td class="px-4 py-3 text-right text-emerald-500">+2.50%</td>
              <td class="px-4 py-3 text-center"><span class="px-2 py-0.5 rounded bg-emerald-100 dark:bg-emerald-950 text-emerald-800 dark:text-emerald-350 text-xs font-semibold">繼續強勢</span></td>
              <td class="px-4 py-3 font-sans text-xs">穩步向上，零售與 AWS 雙重護航，守穩上升趨勢</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold font-sans">ORCL</td>
              <td class="px-4 py-3 text-right">148.53</td>
              <td class="px-4 py-3 text-right text-rose-500">-2.58%</td>
              <td class="px-4 py-3 text-center"><span class="px-2 py-0.5 rounded bg-gray-100 dark:bg-gray-800 text-gray-800 dark:text-gray-300 text-xs font-semibold">需要觀察</span></td>
              <td class="px-4 py-3 font-sans text-xs">大盤軟體暴漲下逆勢微跌，反映前段累計漲幅較大，短期需休整</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold font-sans">CRM</td>
              <td class="px-4 py-3 text-right">158.37</td>
              <td class="px-4 py-3 text-right text-emerald-500">+5.45%</td>
              <td class="px-4 py-3 text-center"><span class="px-2 py-0.5 rounded bg-teal-100 dark:bg-teal-950 text-teal-800 dark:text-teal-350 text-xs font-semibold">低位修復</span></td>
              <td class="px-4 py-3 font-sans text-xs">強勢突破近期底部，Agentic AI 機遇吸引買盤，低估值優勢顯現</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold font-sans">NOW</td>
              <td class="px-4 py-3 text-right">98.34</td>
              <td class="px-4 py-3 text-right text-emerald-500">+9.85%</td>
              <td class="px-4 py-3 text-center"><span class="px-2 py-0.5 rounded bg-teal-100 dark:bg-teal-950 text-teal-800 dark:text-teal-350 text-xs font-semibold">低位修復</span></td>
              <td class="px-4 py-3 font-sans text-xs">暴漲近10%吞噬昨日跌幅，大空頭踩踏（Short Squeeze）強烈，反彈迅猛</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold font-sans">SNOW</td>
              <td class="px-4 py-3 text-right">248.96</td>
              <td class="px-4 py-3 text-right text-emerald-500">+9.65%</td>
              <td class="px-4 py-3 text-center"><span class="px-2 py-0.5 rounded bg-teal-100 dark:bg-teal-950 text-teal-800 dark:text-teal-350 text-xs font-semibold">低位修復</span></td>
              <td class="px-4 py-3 font-sans text-xs">在大盤重編中獲被動權重調升，股價大舉狂飆，突破重要均線壓制</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold font-sans">ADBE</td>
              <td class="px-4 py-3 text-right">202.73</td>
              <td class="px-4 py-3 text-right text-emerald-500">+4.82%</td>
              <td class="px-4 py-3 text-center"><span class="px-2 py-0.5 rounded bg-teal-100 dark:bg-teal-950 text-teal-800 dark:text-teal-350 text-xs font-semibold">低位修復</span></td>
              <td class="px-4 py-3 font-sans text-xs">買盤大舉湧入，股價重回 $200 關卡上方，多頭低位築底完成</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold font-sans">PLTR</td>
              <td class="px-4 py-3 text-right">112.93</td>
              <td class="px-4 py-3 text-right text-emerald-500">+5.28%</td>
              <td class="px-4 py-3 text-center"><span class="px-2 py-0.5 rounded bg-emerald-100 dark:bg-emerald-950 text-emerald-800 dark:text-emerald-350 text-xs font-semibold">繼續強勢</span></td>
              <td class="px-4 py-3 font-sans text-xs">大漲創歷史新高，AI 商業合同執行力驚人，機構持續加倉</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold font-sans">LITE</td>
              <td class="px-4 py-3 text-right">816.98</td>
              <td class="px-4 py-3 text-right text-rose-500">-5.22%</td>
              <td class="px-4 py-3 text-center"><span class="px-2 py-0.5 rounded bg-blue-100 dark:bg-blue-950 text-blue-800 dark:text-blue-350 text-xs font-semibold">回踩支撐</span></td>
              <td class="px-4 py-3 font-sans text-xs">光通訊概念股高位大洗盤，先看 20MA 是否有支撐，暫停追高</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold font-sans">COHR</td>
              <td class="px-4 py-3 text-right">380.56</td>
              <td class="px-4 py-3 text-right text-rose-500">-6.55%</td>
              <td class="px-4 py-3 text-center"><span class="px-2 py-0.5 rounded bg-blue-100 dark:bg-blue-950 text-blue-800 dark:text-blue-350 text-xs font-semibold">回踩支撐</span></td>
              <td class="px-4 py-3 font-sans text-xs">光通訊核心標的今日遭遇猛烈拋售，回撤幅度大，觀望為主</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold font-sans">ANET</td>
              <td class="px-4 py-3 text-right">157.60</td>
              <td class="px-4 py-3 text-right text-rose-500">-4.74%</td>
              <td class="px-4 py-3 text-center"><span class="px-2 py-0.5 rounded bg-amber-100 dark:bg-amber-950 text-amber-800 dark:text-amber-350 text-xs font-semibold">高位震盪</span></td>
              <td class="px-4 py-3 font-sans text-xs">受基建與半導體拖累大跌，但長期資料中心網絡需求依然堅固</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold font-sans">FLNC</td>
              <td class="px-4 py-3 text-right">19.27</td>
              <td class="px-4 py-3 text-right text-rose-500">-0.57%</td>
              <td class="px-4 py-3 text-center"><span class="px-2 py-0.5 rounded bg-gray-100 dark:bg-gray-800 text-gray-800 dark:text-gray-300 text-xs font-semibold">需要觀察</span></td>
              <td class="px-4 py-3 font-sans text-xs">儲能題材今日窄幅整理，面臨 50MA 壓制，需等待政策或財報催化</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold font-sans">OKLO</td>
              <td class="px-4 py-3 text-right">50.00</td>
              <td class="px-4 py-3 text-right text-rose-500">-1.98%</td>
              <td class="px-4 py-3 text-center"><span class="px-2 py-0.5 rounded bg-red-100 dark:bg-red-950 text-red-800 dark:text-red-350 text-xs font-semibold">破位風險</span></td>
              <td class="px-4 py-3 font-sans text-xs">失守 20MA 與 $50 整數關卡，短期題材炒作退潮，面臨進一步修正</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold font-sans">VST</td>
              <td class="px-4 py-3 text-right">163.49</td>
              <td class="px-4 py-3 text-right text-rose-500">-2.55%</td>
              <td class="px-4 py-3 text-center"><span class="px-2 py-0.5 rounded bg-amber-100 dark:bg-amber-950 text-amber-800 dark:text-amber-350 text-xs font-semibold">高位震盪</span></td>
              <td class="px-4 py-3 font-sans text-xs">電網核電標的出現回落，先看 $160 前期平台是否有支撐力道</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold font-sans">CEG</td>
              <td class="px-4 py-3 text-right">264.02</td>
              <td class="px-4 py-3 text-right text-rose-500">-1.74%</td>
              <td class="px-4 py-3 text-center"><span class="px-2 py-0.5 rounded bg-amber-100 dark:bg-amber-950 text-amber-800 dark:text-amber-350 text-xs font-semibold">高位震盪</span></td>
              <td class="px-4 py-3 font-sans text-xs">跟隨電力板塊走弱，但防禦特質及長期供電合約對股價有支撐</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold font-sans">ETN</td>
              <td class="px-4 py-3 text-right">402.68</td>
              <td class="px-4 py-3 text-right text-rose-500">-4.09%</td>
              <td class="px-4 py-3 text-center"><span class="px-2 py-0.5 rounded bg-blue-100 dark:bg-blue-950 text-blue-800 dark:text-blue-350 text-xs font-semibold">回踩支撐</span></td>
              <td class="px-4 py-3 font-sans text-xs">回踩 20MA（約 $400），重電設備基本面仍處強勁擴張期，可關注止跌機會</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold font-sans">VRT</td>
              <td class="px-4 py-3 text-right">303.95</td>
              <td class="px-4 py-3 text-right text-rose-500">-6.64%</td>
              <td class="px-4 py-3 text-center"><span class="px-2 py-0.5 rounded bg-blue-100 dark:bg-blue-950 text-blue-800 dark:text-blue-350 text-xs font-semibold">回踩支撐</span></td>
              <td class="px-4 py-3 font-sans text-xs">回撤幅度較大，液冷散熱短線籌碼鬆動，關注 $300 整數支撐強度</td>
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
      <div class="leading-relaxed text-sm sm:text-base space-y-4">
        <div>
          <h4 class="font-bold text-zinc-800 dark:text-zinc-200 mb-1">13.1 宏觀觀察</h4>
          <p class="text-zinc-600 dark:text-zinc-400">
            繼續關注美債 10 年期收益率 (^TNX) 的走勢，若能穩定在 4.3% - 4.4% 區間，將持續利好 SaaS 軟體與中小盤股的反彈。下週將迎來製造業與服務業 PMI 數據，需防範宏觀經濟過熱或大縮水的雙向風險。
          </p>
        </div>
        <div>
          <h4 class="font-bold text-zinc-800 dark:text-zinc-200 mb-1">13.2 大盤觀察</h4>
          <p class="text-zinc-600 dark:text-zinc-400">
            標普 500 指數 (SPY) 需迅速收復 20MA（730點）以維持多頭強勢結構；QQQ 則需在 700 點關口獲得實質防守。若 QQQ 下跌失控，即使軟體股補漲，亦難抵巨頭權重下跌對大盤指數的拖累。
          </p>
        </div>
        <div>
          <h4 class="font-bold text-zinc-800 dark:text-zinc-200 mb-1">13.3 板塊與個股觀察</h4>
          <ul class="list-disc pl-5 text-zinc-600 dark:text-zinc-400 space-y-1">
            <li><strong>SaaS 軟體板塊反彈延續性：</strong> 關注 NOW, SNOW, CRM 下週能否在成交量溫和的情況下維持反彈。若能持續，可逢回調分批建倉。</li>
            <li><strong>晶片硬件板塊築底：</strong> 輝達 (NVDA) 與博通 (AVGO) 能否分別在 $190 與 $360 關口企穩。目前晶片股不宜盲目抄底，需等待籌碼出清。</li>
            <li><strong>防禦大健康：</strong> 醫療板塊 (XLV) 具備防守特質，可作為大盤震盪期的避險底倉配置。</li>
          </ul>
        </div>
      </div>
    </section>

    <!-- 14. 風險提示 -->
    <section id="risks" class="mb-12 scroll-mt-6">
      <h2 class="text-2xl font-bold mb-4 flex items-center gap-2 border-b border-zinc-100 dark:border-zinc-800 pb-2">
        <span class="text-brand-500">14.</span> 風險提示
      </h2>
      
      <div class="overflow-x-auto border border-zinc-200 dark:border-zinc-800 rounded-xl mb-4">
        <table class="min-w-full divide-y divide-zinc-200 dark:divide-zinc-850 text-sm">
          <thead class="bg-zinc-50 dark:bg-zinc-900 text-zinc-550 dark:text-zinc-400">
            <tr>
              <th class="px-4 py-3 font-semibold text-left">風險維度</th>
              <th class="px-4 py-3 font-semibold text-center">評級</th>
              <th class="px-4 py-3 font-semibold text-left">具體宏觀與技術解讀</th>
              <th class="px-4 py-3 font-semibold text-left">應對與避險策略</th>
            </tr>
          </thead>
          <tbody class="divide-y divide-zinc-200 dark:divide-zinc-850 font-mono text-zinc-700 dark:text-zinc-300">
            <tr>
              <td class="px-4 py-3 font-semibold font-sans">宏觀利率與通膨</td>
              <td class="px-4 py-3 text-center"><span class="px-2 py-0.5 rounded bg-yellow-100 dark:bg-yellow-950 text-yellow-800 dark:text-yellow-350 text-xs font-semibold">中</span></td>
              <td class="px-4 py-3 font-sans text-xs text-zinc-650 dark:text-zinc-350">雖然密大通膨預期下滑且債息回落，但核心 PCE 仍有 3.4% 粘性，降息路徑仍有變數</td>
              <td class="px-4 py-3 font-sans text-xs text-zinc-650 dark:text-zinc-350">配置部分高股息醫療（XLV）與電力防守，減少對利率高敏感板塊的單一過度曝險</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold font-sans">AI 硬件籌碼擁擠</td>
              <td class="px-4 py-3 text-center"><span class="px-2 py-0.5 rounded bg-amber-100 dark:bg-amber-950 text-amber-800 dark:text-amber-350 text-xs font-semibold">中高</span></td>
              <td class="px-4 py-3 font-sans text-xs text-zinc-650 dark:text-zinc-350">費半及重電大跌說明短線資金獲利回吐壓力大，大資金出現明顯去擁擠化撤離</td>
              <td class="px-4 py-3 font-sans text-xs text-zinc-650 dark:text-zinc-350">暫停對 NVDA、AVGO、MU 的追高操作，等日線級別企穩或完成回踩 50MA 再行部署</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold font-sans">SaaS 軟體反彈陷阱</td>
              <td class="px-4 py-3 text-center"><span class="px-2 py-0.5 rounded bg-yellow-100 dark:bg-yellow-950 text-yellow-800 dark:text-yellow-350 text-xs font-semibold">中</span></td>
              <td class="px-4 py-3 font-sans text-xs text-zinc-650 dark:text-zinc-350">軟體股今日大漲主要受空頭踩踏（Short Squeeze）與指數基金被動配置推動，基本面拐點仍待確認</td>
              <td class="px-4 py-3 font-sans text-xs text-zinc-650 dark:text-zinc-350">避免一次性滿倉追入軟體，應挑選 CRM、NOW 等具備明確 AI 定價能力的龍頭分批佈局</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold font-sans">技術指標死叉</td>
              <td class="px-4 py-3 text-center"><span class="px-2 py-0.5 rounded bg-yellow-100 dark:bg-yellow-950 text-yellow-800 dark:text-yellow-350 text-xs font-semibold">中</span></td>
              <td class="px-4 py-3 font-sans text-xs text-zinc-650 dark:text-zinc-350">QQQ 及 SMH 跌破 20MA，MACD 出現高位死叉，短線技術形態走弱</td>
              <td class="px-4 py-3 font-sans text-xs text-zinc-650 dark:text-zinc-350">保持 20-30% 的現金防守，切忌在調整初期滿倉操作</td>
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
        <p><strong>今日市場結論：</strong> 今日大盤在晶片股劇烈回調與軟體股、防禦保健強勁反彈的雙重拉扯下收平。費半重挫逾 5.6% 反映了 AI 硬體板塊短期擁擠度見頂，而 IGV 軟體指數大漲 4.06% 與醫療保健 (XLV) 大漲 3.03% 則證明了市場內部寬度良好，屬於健康的「大輪動」而非恐慌性崩盤。羅素指數重編亦在收盤帶來了歷史天量，巨頭尾盤獲得護盤。</p>
        <p><strong>當前市場階段：</strong> <span class="text-amber-500 font-semibold">良性板塊輪動 / 高位震盪整理</span></p>
        <p><strong>操作傾向：</strong> 中性偏多。大盤整體仍守在主要支撐均線上。操作上應「短線規避擁擠的晶片與重電基建，分批低吸估值出清且有 Agentic AI 催化的 SaaS 軟體龍頭」，並配置大健康板塊作為防禦底倉。</p>
        <p><strong>最值得觀測的 5 個訊號：</strong>
          <br>1. <strong>SaaS 軟體股（NOW, CRM）的反彈持續性：</strong> 能否下週縮量持穩，確立底部。
          <br>2. <strong>輝達 (NVDA) 與費半 (SOXX) 的止跌位置：</strong> 能否在 50MA 或關鍵整數關口築底。
          <br>3. <strong>10年期美債收益率 (^TNX)：</strong> 能否繼續守在 4.4% 下方以維繫高估值股信心。
          <br>4. <strong>WTI 原油 (USO)：</strong> 暴跌後是否低位震盪，進一步消減通膨擔憂。
          <br>5. <strong>大盤指數成交量：</strong> 在經歷今日羅素調整的史詩成交量後，下週大盤是否縮量企穩。
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
        data: [-0.09, -0.05, -0.24, -1.38, 0.31, -5.64, -1.18],
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

# Save this HTML to reports/2026-06-26-us-stock-closing-daily-report.html inside /Users/wisdom/html-report-skill
target_dir = "/Users/wisdom/html-report-skill/reports"
os.makedirs(target_dir, exist_ok=True)
target_path = os.path.join(target_dir, "2026-06-26-us-stock-closing-daily-report.html")

with open(target_path, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"Report HTML file generated successfully at: {target_path}")
