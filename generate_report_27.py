import os

html_content = """<!doctype html>
<html lang="zh-TW" class="scroll-smooth">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <title>美股收盤日報｜2026-05-27</title>
  <meta name="description" content="2026年5月27日美股收盤日報：三大指數齊創盤中歷史新高，道指大漲 182 點再登收盤歷史巔峰！零售財報強勁引領消費股，油價因地緣緩和重挫 5.8%，科技半導體板塊高位歇息整固。">
  <meta property="og:title" content="美股收盤日報｜2026-05-27">
  <meta property="og:description" content="道指標普再創歷史新高！油價暴跌 5.8% 刺激消費與航空股，科技板塊高位整固，Salesforce (CRM) 財報雙超預期。">
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
              50: '#f0fdf4',
              100: '#dcfce7',
              500: '#10b981',
              600: '#059669',
              700: '#047857',
            }
          },
          fontFamily: {
            sans: ['system-ui', 'ui-sans-serif', 'sans-serif']
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
    .toc a:hover, .toc a.active { opacity: 1; color: #10b981; }
    .toc a.active { font-weight: 600; border-left: 2px solid #10b981; padding-left: 0.5rem; margin-left: -0.5rem; }

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
    .tabs > input:checked + label { border-color: #10b981; color: #10b981; font-weight: 600; }
    .tabs > .tab-panel { display: none; width: 100%; padding-top: 1rem; }
    .tabs > input:nth-of-type(1):checked ~ .tab-panel:nth-of-type(1),
    .tabs > input:nth-of-type(2):checked ~ .tab-panel:nth-of-type(2),
    .tabs > input:nth-of-type(3):checked ~ .tab-panel:nth-of-type(3),
    .tabs > input:nth-of-type(4):checked ~ .tab-panel:nth-of-type(4) { display: block; }

    /* Premium styled elements */
    .stat-card {
      background: linear-gradient(135deg, rgba(16,185,129,0.06) 0%, rgba(59,130,246,0.03) 100%);
      border: 1px solid rgba(16,185,129,0.15);
      border-radius: 1rem;
      padding: 1.5rem;
      transition: transform .2s, box-shadow .2s;
    }
    .stat-card:hover { transform: translateY(-2px); box-shadow: 0 8px 24px rgba(16,185,129,0.08); }

    .tag-strong { background-color: rgba(34, 197, 94, 0.15); color: #22c55e; border: 1px solid rgba(34, 197, 94, 0.25); }
    .tag-neutral { background-color: rgba(107, 114, 128, 0.15); color: #9ca3af; border: 1px solid rgba(107, 114, 128, 0.25); }
    .tag-warning { background-color: rgba(234, 179, 8, 0.15); color: #eab308; border: 1px solid rgba(234, 179, 8, 0.25); }
    .tag-danger { background-color: rgba(239, 68, 68, 0.15); color: #ef4444; border: 1px solid rgba(239, 68, 68, 0.25); }

    .grad-text {
      background: linear-gradient(135deg, #10b981, #3b82f6, #6366f1);
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
        <span class="text-sm text-zinc-500"><time datetime="2026-05-27">2026-05-27 (星期三)</time></span>
      </div>
      <h1 class="text-4xl font-extrabold tracking-tight mb-4 grad-text">美股收盤日報｜2026-05-27</h1>
      <p class="text-xl text-zinc-600 dark:text-zinc-400">三大指數齊創盤中歷史新高，道瓊大漲 182 點勇奪收盤歷史巔峰！零售財報暴賺引爆消費股，油價大跌 5.8% 刺激航空股，科技板塊高位歇息整固。</p>
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
              指數震盪微漲、科技高位歇息，板塊良性輪動至消費必需品與醫療保健，市場寬度正常。
            </p>
          </div>
          <div class="space-y-2">
            <p class="text-sm font-semibold text-zinc-400">核心驅動因素</p>
            <p class="text-sm text-zinc-600 dark:text-zinc-300">
              美伊和平談判樂觀預期推動原油價格重挫 5.8%，大幅稀釋通膨擔憂，進而激發零售財報潮強勁爆發、航空與消費板塊大漲，科技半導體與 AI 電力則在連續飆升後迎來健康的短線獲利整固。
            </p>
          </div>
        </div>
        <hr class="border-zinc-200 dark:border-zinc-800">
        <ul class="list-disc pl-5 space-y-2 text-zinc-600 dark:text-zinc-300">
          <li><strong>大盤趨勢：</strong>美股三大指數盤中同步刷新歷史天價。終盤道指上揚 182.60 點 (+0.36%)，標普 500 微漲 0.02%，雙雙刷新收盤歷史最高紀錄；以科技為主的納斯達克微漲 0.07%，科技成長股高歌猛進後轉入橫盤。</li>
          <li><strong>板塊特徵：</strong>消費必需品 (XLP) 與非必需消費 (XLY) 領跑大市。Abercrombie & Fitch (ANF +12%) 與 Bath & Body Works (BBWI +13%) 財報大超預期暴力拉升。科技半導體 (SMH -0.80%) 與 AI 發電 (CEG -3.88%、VST -2.68%) 迎來高位健康回吐。</li>
          <li><strong>資金態度：</strong>良性 Risk-On 下的「價值與消費輪動」。地緣形勢大緩和擊落油價，無風險收益率基本持平，資金從高擁擠度的晶片板塊暫時分流至超跌的民生消費、航空及金融防禦板塊。</li>
        </ul>
      </div>
    </section>

    <!-- 1. 大盤表現總覽 -->
    <section id="indices" class="mb-12 scroll-mt-6">
      <h2 class="text-2xl font-bold mb-4 flex items-center gap-2 border-b border-zinc-100 dark:border-zinc-800 pb-2">
        <span class="text-brand-500">1.</span> 大盤表現總覽
      </h2>
      <div class="grid grid-cols-1 lg:grid-cols-2 gap-8 mb-6">
        <!-- Table -->
        <div class="overflow-x-auto border border-zinc-200 dark:border-zinc-800 rounded-xl">
          <table class="min-w-full divide-y divide-zinc-200 dark:divide-zinc-800 text-sm">
            <thead class="bg-zinc-50 dark:bg-zinc-900">
              <tr>
                <th class="px-4 py-3 text-left font-semibold text-zinc-600 dark:text-zinc-400">指數名稱</th>
                <th class="px-4 py-3 text-right font-semibold text-zinc-600 dark:text-zinc-400">收盤點位</th>
                <th class="px-4 py-3 text-right font-semibold text-zinc-600 dark:text-zinc-400">漲跌幅</th>
                <th class="px-4 py-3 text-center font-semibold text-zinc-600 dark:text-zinc-400">技術狀態</th>
              </tr>
            </thead>
            <tbody class="divide-y divide-zinc-200 dark:divide-zinc-800">
              <tr>
                <td class="px-4 py-3 font-medium">Dow Jones (道瓊)</td>
                <td class="px-4 py-3 text-right font-mono">50,644.28</td>
                <td class="px-4 py-3 text-right font-mono text-emerald-500 font-semibold">+0.36%</td>
                <td class="px-4 py-3 text-center"><span class="px-2 py-0.5 rounded-full text-xs tag-strong">創收盤歷史新高</span></td>
              </tr>
              <tr>
                <td class="px-4 py-3 font-medium">S&P 500 (標普500)</td>
                <td class="px-4 py-3 text-right font-mono">7,520.36</td>
                <td class="px-4 py-3 text-right font-mono text-emerald-500 font-semibold">+0.02%</td>
                <td class="px-4 py-3 text-center"><span class="px-2 py-0.5 rounded-full text-xs tag-strong">創收盤歷史新高</span></td>
              </tr>
              <tr>
                <td class="px-4 py-3 font-medium">Nasdaq Comp (納斯達克)</td>
                <td class="px-4 py-3 text-right font-mono">26,674.74</td>
                <td class="px-4 py-3 text-right font-mono text-emerald-500 font-semibold">+0.07%</td>
                <td class="px-4 py-3 text-center"><span class="px-2 py-0.5 rounded-full text-xs tag-strong">創收盤歷史新高</span></td>
              </tr>
              <tr>
                <td class="px-4 py-3 font-medium">Nasdaq 100 (QQQ)</td>
                <td class="px-4 py-3 text-right font-mono">$729.48</td>
                <td class="px-4 py-3 text-right font-mono text-rose-500 font-semibold">-0.20%</td>
                <td class="px-4 py-3 text-center"><span class="px-2 py-0.5 rounded-full text-xs tag-neutral">高位正常蓄勢</span></td>
              </tr>
              <tr>
                <td class="px-4 py-3 font-medium">Russell 2000 (IWM)</td>
                <td class="px-4 py-3 text-right font-mono">$290.51</td>
                <td class="px-4 py-3 text-right font-mono text-rose-500 font-semibold">-0.02%</td>
                <td class="px-4 py-3 text-center"><span class="px-2 py-0.5 rounded-full text-xs tag-neutral">回踩箱體邊緣</span></td>
              </tr>
              <tr>
                <td class="px-4 py-3 font-medium">SOX 半導體 (SMH)</td>
                <td class="px-4 py-3 text-right font-mono">$592.00</td>
                <td class="px-4 py-3 text-right font-mono text-rose-500 font-semibold">-0.80%</td>
                <td class="px-4 py-3 text-center"><span class="px-2 py-0.5 rounded-full text-xs tag-warning">短線高位乖離整固</span></td>
              </tr>
              <tr>
                <td class="px-4 py-3 font-medium">VIX 恐慌指數</td>
                <td class="px-4 py-3 text-right font-mono">16.78</td>
                <td class="px-4 py-3 text-right font-mono text-rose-500 font-semibold">-1.35%</td>
                <td class="px-4 py-3 text-center"><span class="px-2 py-0.5 rounded-full text-xs tag-strong">避險情緒大幅收縮</span></td>
              </tr>
            </tbody>
          </table>
        </div>

        <!-- Chart -->
        <div class="p-4 border border-zinc-200 dark:border-zinc-800 rounded-xl bg-zinc-50/50 dark:bg-zinc-900/50">
          <h3 class="text-sm font-semibold text-zinc-500 mb-3 uppercase tracking-wider">主要指數單日漲跌幅對比 (%)</h3>
          <div class="chart-wrap">
            <canvas id="returnsChart"></canvas>
          </div>
        </div>
      </div>
      <p class="text-sm text-zinc-500 italic mt-2">
        * 註：三大主要指數盤中同步刷寫歷史新高。在油價暴挫與消費板塊大漲的輪動效應下，道指表現最亮眼，納指與半導體成分股在美光科技、輝達高檔獲利整固下微幅回調，顯示牛市多頭健康的深度輪動。
      </p>
    </section>

    <!-- 2. 盤中走勢復盤 -->
    <section id="timeline" class="mb-12 scroll-mt-6">
      <h2 class="text-2xl font-bold mb-4 flex items-center gap-2 border-b border-zinc-100 dark:border-zinc-800 pb-2">
        <span class="text-brand-500">2.</span> 盤中走勢復盤
      </h2>
      <div class="relative border-l border-zinc-200 dark:border-zinc-800 ml-4 pl-6 space-y-8">
        <div class="relative">
          <span class="absolute -left-10 top-1.5 flex h-8 w-8 items-center justify-center rounded-full bg-brand-50 dark:bg-brand-500/10 text-brand-600 dark:text-brand-400 font-bold border border-brand-200 dark:border-brand-500/20 text-xs">開盤</span>
          <h3 class="text-lg font-bold text-zinc-800 dark:text-zinc-200">09:30 AM — 指數高位震盪，消費板塊直接搶攻</h3>
          <p class="text-sm text-zinc-600 dark:text-zinc-400 mt-1">
            大盤跳空高開，三大指數盤中強勢刷新歷史天價。盤前公佈的 Abercrombie & Fitch (ANF) 與 Bath & Body Works (BBWI) 第一季財報震驚華爾街，引導資金直接流向超跌零售與消費板塊，道指開盤一馬當先。
          </p>
        </div>
        <div class="relative">
          <span class="absolute -left-10 top-1.5 flex h-8 w-8 items-center justify-center rounded-full bg-brand-50 dark:bg-brand-500/10 text-brand-600 dark:text-brand-400 font-bold border border-brand-200 dark:border-brand-500/20 text-xs">油價</span>
          <h3 class="text-lg font-bold text-zinc-800 dark:text-zinc-200">11:00 AM — 原油大跌 5.8%，航空郵輪股狂歡</h3>
          <p class="text-sm text-zinc-600 dark:text-zinc-400 mt-1">
            隨著地緣和平談判樂觀預期發酵，原油價格雪崩跌破 $89 關卡，WTI 狂跌超 5%。能源板塊 (XLE) 應聲急挫，但直接受益於油價暴跌的航空股大爆發，聯合航空 (UAL) 宣布 Starlink 上線消息刺激股價大漲逾 6%。
          </p>
        </div>
        <div class="relative">
          <span class="absolute -left-10 top-1.5 flex h-8 w-8 items-center justify-center rounded-full bg-brand-50 dark:bg-brand-500/10 text-brand-600 dark:text-brand-400 font-bold border border-brand-200 dark:border-brand-500/20 text-xs">歇息</span>
          <h3 class="text-lg font-bold text-zinc-800 dark:text-zinc-200">01:30 PM — 科技半導體板塊走弱，Meta 逆勢護盤</h3>
          <p class="text-sm text-zinc-600 dark:text-zinc-400 mt-1">
            連續幾天狂飆的晶片股（美光科技、輝達）出現高檔獲利了結拋盤。SOX 指數一度跌近 1.2%。然而，Meta (META) 宣佈核心 AI 機構算法大幅升級，股價逆勢飆漲 3.74%，直接提振科技板塊人氣。
          </p>
        </div>
        <div class="relative">
          <span class="absolute -left-10 top-1.5 flex h-8 w-8 items-center justify-center rounded-full bg-brand-50 dark:bg-brand-500/10 text-brand-600 dark:text-brand-400 font-bold border border-brand-200 dark:border-brand-500/20 text-xs">警告</span>
          <h3 class="text-lg font-bold text-zinc-800 dark:text-zinc-200">03:00 PM — 摩根大通警告開銷，金融板塊微幅回軟</h3>
          <p class="text-sm text-zinc-600 dark:text-zinc-400 mt-1">
            JPMorgan Chase (JPM) 盤中重挫超 2.4%，CEO Jamie Dimon 警告今年開支可能比先前預期高出 10 億美元。金融大廠短暫承受估值壓力，但道指依然憑藉消費防禦股（聯合健康、寶僑）大漲而屹立不倒。
          </p>
        </div>
        <div class="relative">
          <span class="absolute -left-10 top-1.5 flex h-8 w-8 items-center justify-center rounded-full bg-brand-50 dark:bg-brand-500/10 text-brand-600 dark:text-brand-400 font-bold border border-brand-200 dark:border-brand-500/20 text-xs">收盤</span>
          <h3 class="text-lg font-bold text-zinc-800 dark:text-zinc-200">04:00 PM — 多頭穩健控盤，道指刷新歷史新高紀錄</h3>
          <p class="text-sm text-zinc-600 dark:text-zinc-400 mt-1">
            尾盤買氣維持堅挺，多頭勢力穩健控盤。道指與標普 500 成功鎖定收盤歷史新高。Salesforce (CRM) 財報於盤後公佈，首季度業績大超預期，但因指引稍微保守，盤後下跌約 2.5%。
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
        <label for="tab-data" class="hover:text-brand-500">重要經濟動態</label>

        <!-- Panel 1 -->
        <div class="tab-panel border-t border-zinc-200 dark:border-zinc-800 mt-2">
          <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
            <div class="stat-card">
              <span class="text-xs font-semibold text-zinc-400 uppercase">2年期美債收益率</span>
              <div class="text-2xl font-bold font-mono mt-1">4.030%</div>
              <span class="text-xs text-emerald-500 font-semibold">↓ 1.5 bps</span>
            </div>
            <div class="stat-card">
              <span class="text-xs font-semibold text-zinc-400 uppercase">10年期美債收益率</span>
              <div class="text-2xl font-bold font-mono mt-1">4.480%</div>
              <span class="text-xs text-emerald-500 font-semibold">↓ 1.0 bps</span>
            </div>
            <div class="stat-card">
              <span class="text-xs font-semibold text-zinc-400 uppercase">30年期美債收益率</span>
              <div class="text-2xl font-bold font-mono mt-1">4.640%</div>
              <span class="text-xs text-emerald-500 font-semibold">↓ 1.0 bps</span>
            </div>
          </div>
          <p class="text-sm text-zinc-600 dark:text-zinc-400 mt-4 leading-relaxed">
            <strong>市場含義：</strong>收益率曲線基本維持在窄幅橫盤整固狀態。10年期國債利率穩定在 4.480% 附近，地緣局勢緩和推動的原油暴跌大幅緩和了二次通膨抬頭的擔憂，但由於即將迎來關鍵的 PCE 數據，債市波動率收縮，為風險資產提供估值安全墊。
          </p>
        </div>

        <!-- Panel 2 -->
        <div class="tab-panel border-t border-zinc-200 dark:border-zinc-800 mt-2">
          <div class="space-y-4">
            <div class="p-4 bg-zinc-100 dark:bg-zinc-900 rounded-lg">
              <h4 class="font-bold text-zinc-800 dark:text-zinc-200">聯準會鷹派立場固化：</h4>
              <p class="text-sm text-zinc-600 dark:text-zinc-300 mt-2">
                即使油價在今日出現大幅度回調，由於中東衝突引發的供應風險並未完全消退，聯準會理事 Lisa Cook 與其他多位官員依然在近期發表了偏向 Hawkish 的表態，暗示如果通膨數據未能維持良性走勢，Fed 有隨時加息的權利。
                <br>• <strong>CME FedWatch 當前定價：</strong>年內降息概率極低。市場基本已經定價了年內「不降息（Hold）」甚至「防禦性升息 1 次」的預期。高利率環境將比原先預期延續得更久。
              </p>
            </div>
            <div class="p-4 bg-zinc-100 dark:bg-zinc-900 rounded-lg">
              <h4 class="font-bold text-zinc-800 dark:text-zinc-200">Kevin Warsh 新政觀察期：</h4>
              <p class="text-sm text-zinc-600 dark:text-zinc-300 mt-2">
                市場正在等待本週四（明日）公佈的美國 PCE 通膨指標以及 Q1 GDP 修正值。這將是新任主席沃什上台後首個重磅宏觀考驗，也是決定 6 月份政策前瞻的關鍵依據。
              </p>
            </div>
          </div>
        </div>

        <!-- Panel 3 -->
        <div class="tab-panel border-t border-zinc-200 dark:border-zinc-800 mt-2">
          <div class="grid grid-cols-2 md:grid-cols-4 gap-4">
            <div class="stat-card">
              <span class="text-xs font-semibold text-zinc-400">美元指數 (DXY)</span>
              <div class="text-xl font-bold font-mono mt-1">99.14</div>
              <span class="text-xs text-rose-500">↓ 0.10%</span>
            </div>
            <div class="stat-card">
              <span class="text-xs font-semibold text-zinc-400">黃金現貨 (Gold)</span>
              <div class="text-xl font-bold font-mono mt-1">$4,433.00</div>
              <span class="text-xs text-rose-500">↓ 1.60%</span>
            </div>
            <div class="stat-card">
              <span class="text-xs font-semibold text-zinc-400">WTI 原油 (WTI)</span>
              <div class="text-xl font-bold font-mono mt-1">$88.17</div>
              <span class="text-xs text-rose-500">↓ 5.80%</span>
            </div>
            <div class="stat-card">
              <span class="text-xs font-semibold text-zinc-400">比特幣 (BTC)</span>
              <div class="text-xl font-bold font-mono mt-1">$75,500</div>
              <span class="text-xs text-rose-500">↓ 1.30%</span>
            </div>
          </div>
          <p class="text-sm text-zinc-600 dark:text-zinc-400 mt-4 leading-relaxed">
            <strong>市場含義：</strong>美伊和平談判樂觀預期令 WTI 原油從 $93 大幅狂跌 5.8% 至 $88.17/桶，這是推動今日消費和通膨鬆綁的最主要因素。黃金在美元小幅反彈和債市避險消退下大跌 1.6% 回調至 $4,433。比特幣在 $75,500 附近震盪整固，市場面臨短線多空分歧。
          </p>
        </div>

        <!-- Panel 4 -->
        <div class="tab-panel border-t border-zinc-200 dark:border-zinc-800 mt-2">
          <div class="p-4 bg-zinc-100 dark:bg-zinc-900 rounded-lg">
            <h4 class="font-bold text-zinc-800 dark:text-zinc-200 flex items-center gap-2">
              <span>美國 5 月 Richmond 聯邦製造業指數</span>
              <span class="px-2 py-0.5 rounded text-xs tag-neutral font-normal">數據偏軟</span>
            </h4>
            <p class="text-sm text-zinc-600 dark:text-zinc-300 mt-3 leading-relaxed">
              今日公佈的美國 5 月 Richmond 聯邦製造業指數表現平平，但市場基本無視此數據，投資者將全部焦點投射於明日（美國時間週四）公佈的<strong>美國第一季個人消費支出 (PCE) 物價指數與 GDP 修正值</strong>，若 PCE 顯示通膨降溫，將直接為沃什主席開啟貨幣寬鬆想像空間。
            </p>
          </div>
        </div>
      </div>
    </section>

    <!-- 4. S&P 500 板塊表現 -->
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
              <td class="px-4 py-3 font-medium">非必需消費 (Consumer Discretionary)</td>
              <td class="px-4 py-3 font-mono">XLY</td>
              <td class="px-4 py-3 text-right font-mono text-emerald-500 font-semibold" data-val="1.10">+1.10%</td>
              <td class="px-4 py-3 text-right font-mono" data-val="2.50">+2.50%</td>
              <td class="px-4 py-3 text-right font-mono" data-val="5.10">+5.10%</td>
              <td class="px-4 py-3 text-xs">零售股財報潮爆發，ANF 與 BBWI 大漲超 12% 引爆買盤，特斯拉 (+1.56%) 助攻。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-medium">2</td>
              <td class="px-4 py-3 font-medium">日常消費 (Consumer Staples)</td>
              <td class="px-4 py-3 font-mono">XLP</td>
              <td class="px-4 py-3 text-right font-mono text-emerald-500 font-semibold" data-val="1.00">+1.00%</td>
              <td class="px-4 py-3 text-right font-mono" data-val="1.80">+1.80%</td>
              <td class="px-4 py-3 text-right font-mono" data-val="3.20">+3.20%</td>
              <td class="px-4 py-3 text-xs">資金大舉輪動至防禦板塊，寶僑 (PG) 狂飆 3.2% 領軍，防禦配置意願高漲。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-medium">3</td>
              <td class="px-4 py-3 font-medium">醫療保健 (Health Care)</td>
              <td class="px-4 py-3 font-mono">XLV</td>
              <td class="px-4 py-3 text-right font-mono text-emerald-500 font-semibold" data-val="0.50">+0.50%</td>
              <td class="px-4 py-3 text-right font-mono" data-val="0.80">+0.80%</td>
              <td class="px-4 py-3 text-right font-mono" data-val="2.10">+2.10%</td>
              <td class="px-4 py-3 text-xs">聯合健康 (UNH) 暴漲 1.98% 強烈捍衛道瓊大盤，板塊補漲。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-medium">4</td>
              <td class="px-4 py-3 font-medium">通信服務 (Communication Services)</td>
              <td class="px-4 py-3 font-mono">XLC</td>
              <td class="px-4 py-3 text-right font-mono text-emerald-500 font-semibold" data-val="0.40">+0.40%</td>
              <td class="px-4 py-3 text-right font-mono" data-val="1.30">+1.30%</td>
              <td class="px-4 py-3 text-right font-mono" data-val="6.50">+6.50%</td>
              <td class="px-4 py-3 text-xs">Meta 逆勢飆漲 3.74% 成最強頂樑柱，Alphabet (+0.43%) 穩步前行。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-medium">5</td>
              <td class="px-4 py-3 font-medium">基礎材料 (Materials)</td>
              <td class="px-4 py-3 font-mono">XLB</td>
              <td class="px-4 py-3 text-right font-mono text-emerald-500 font-semibold" data-val="0.20">+0.20%</td>
              <td class="px-4 py-3 text-right font-mono" data-val="1.10">+1.10%</td>
              <td class="px-4 py-3 text-right font-mono" data-val="2.90">+2.90%</td>
              <td class="px-4 py-3 text-xs">美元微幅回軟刺激金屬，板塊在平盤附近穩健防守。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-medium">6</td>
              <td class="px-4 py-3 font-medium">房地產 (Real Estate)</td>
              <td class="px-4 py-3 font-mono">XLRE</td>
              <td class="px-4 py-3 text-right font-mono text-emerald-500 font-semibold" data-val="0.10">+0.10%</td>
              <td class="px-4 py-3 text-right font-mono" data-val="0.90">+0.90%</td>
              <td class="px-4 py-3 text-right font-mono" data-val="-2.00">-2.00%</td>
              <td class="px-4 py-3 text-xs">收益率略為走穩，地產資金小幅回流，無亮眼表現。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-medium">7</td>
              <td class="px-4 py-3 font-medium">工業 (Industrials)</td>
              <td class="px-4 py-3 font-mono">XLI</td>
              <td class="px-4 py-3 text-right font-mono text-rose-500 font-semibold" data-val="-0.10">-0.10%</td>
              <td class="px-4 py-3 text-right font-mono" data-val="1.90">+1.90%</td>
              <td class="px-4 py-3 text-right font-mono" data-val="5.10">+5.10%</td>
              <td class="px-4 py-3 text-xs">AI 電力基建與重工業股在高漲後出現微幅技術回踩。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-medium">8</td>
              <td class="px-4 py-3 font-medium">公用事業 (Utilities)</td>
              <td class="px-4 py-3 font-mono">XLU</td>
              <td class="px-4 py-3 text-right font-mono text-rose-500 font-semibold" data-val="-0.20">-0.20%</td>
              <td class="px-4 py-3 text-right font-mono" data-val="2.50">+2.50%</td>
              <td class="px-4 py-3 text-right font-mono" data-val="9.50">+9.50%</td>
              <td class="px-4 py-3 text-xs">核電三巨頭 (VST, CEG) 遭遇連飆後的正常利潤回流整理。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-medium">9</td>
              <td class="px-4 py-3 font-medium">科技 (Technology)</td>
              <td class="px-4 py-3 font-mono">XLK</td>
              <td class="px-4 py-3 text-right font-mono text-rose-500 font-semibold" data-val="-0.46">-0.46%</td>
              <td class="px-4 py-3 text-right font-mono" data-val="3.10">+3.10%</td>
              <td class="px-4 py-3 text-right font-mono" data-val="8.50">+8.50%</td>
              <td class="px-4 py-3 text-xs">半導體拉回，微軟 (-0.81%)、輝達 (-1.72%) 高位整固。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-medium">10</td>
              <td class="px-4 py-3 font-medium">金融 (Financials)</td>
              <td class="px-4 py-3 font-mono">XLF</td>
              <td class="px-4 py-3 text-right font-mono text-rose-500 font-semibold" data-val="-0.80">-0.80%</td>
              <td class="px-4 py-3 text-right font-mono" data-val="-0.30">-0.30%</td>
              <td class="px-4 py-3 text-right font-mono" data-val="1.00">+1.00%</td>
              <td class="px-4 py-3 text-xs">摩根大通警告年度成本增加，大行板塊集體向下整理。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-medium">11</td>
              <td class="px-4 py-3 font-medium">能源 (Energy)</td>
              <td class="px-4 py-3 font-mono">XLE</td>
              <td class="px-4 py-3 text-right font-mono text-rose-500 font-semibold" data-val="-2.80">-2.80%</td>
              <td class="px-4 py-3 text-right font-mono" data-val="-3.50">-3.50%</td>
              <td class="px-4 py-3 text-right font-mono" data-val="-5.80">-5.80%</td>
              <td class="px-4 py-3 text-xs">油價暴跌 5.8% 打擊石油和天然氣巨頭估值。</td>
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
      <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
        <div class="p-6 rounded-xl bg-zinc-50 dark:bg-zinc-900 border border-zinc-100 dark:border-zinc-800">
          <h3 class="text-lg font-bold text-zinc-800 dark:text-zinc-200 mb-3 flex items-center gap-2">
            <span class="h-2 w-2 rounded-full bg-emerald-500"></span> 零售與消費板塊大崛起
          </h3>
          <p class="text-sm text-zinc-600 dark:text-zinc-300 leading-relaxed">
            油價崩挫大幅緩解了民生消費端的通膨通脹警報，加上 ANF 與 BBWI Blowout 的強勁財報，消費者信心獲得實質支撐。航空板塊亦迎來狂熱追捧，聯合航空 (UAL) 在公佈了全機 Starlink 上線並對客流預期看好後狂飆 <strong>+6.3%</strong>，郵輪股（Norwegian Cruise Line）亦全線強勁走高。資金大舉從擁擠的科技晶片流出，轉向估值極低的民生實體經濟板塊。
          </p>
        </div>
        <div class="p-6 rounded-xl bg-zinc-50 dark:bg-zinc-900 border border-zinc-100 dark:border-zinc-800">
          <h3 class="text-lg font-bold text-zinc-800 dark:text-zinc-200 mb-3 flex items-center gap-2">
            <span class="h-2 w-2 rounded-full bg-rose-500"></span> 科技與 AI 基建高檔整固
          </h3>
          <p class="text-sm text-zinc-600 dark:text-zinc-300 leading-relaxed">
            VanEck 半導體 ETF (SMH) 收跌 <strong>-0.80%</strong>。輝達 (NVDA -1.72%) 及超微 (AMD -1.75%) 同步遭遇技術回跌，主要是大盤在高位刷新歷史高點後，科技多頭資金部分套現進行板塊輪動。同時，「AI電力三巨頭」亦遭到降溫整固，Constellation Energy (CEG) 下跌 <strong>-3.88%</strong>，Vistra (VST) 下滑 <strong>-2.68%</strong>，Oklo (OKLO) 微跌 <strong>-1.85%</strong>，此輪調整仍屬於多頭行情的正常拉回整固。
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
        <div class="stat-card">
          <span class="text-xs font-semibold text-zinc-400 uppercase">均線參與度 (S&P 500)</span>
          <div class="text-3xl font-extrabold font-mono text-emerald-500 mt-2">74.2%</div>
          <p class="text-xs text-zinc-500 mt-2">高於 50 日均線的股票比例微調至 74.2%，反映在大盤刷新歷史高點之際，部分股票隨大盤進行技術調整。</p>
        </div>
        <div class="stat-card">
          <span class="text-xs font-semibold text-zinc-400 uppercase">NYSE 漲跌家數比</span>
          <div class="text-3xl font-extrabold font-mono text-emerald-500 mt-2">1.2 : 1</div>
          <p class="text-xs text-zinc-500 mt-2">上漲家數與下跌家數基本平分秋色，顯示出在資金進行大規模板塊輪動時市場的多空博弈特徵。</p>
        </div>
        <div class="stat-card">
          <span class="text-xs font-semibold text-zinc-400 uppercase">52週新高 - 新低差值</span>
          <div class="text-3xl font-extrabold font-mono text-emerald-500 mt-2">+112</div>
          <p class="text-xs text-zinc-500 mt-2">創 52 週新高的股票達 142 隻，而新低僅 30 隻，淨新高仍維持在健康的上升軌道中。</p>
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
              <th class="px-4 py-3 text-left font-semibold text-zinc-600 dark:text-zinc-400">ETF 標的</th>
              <th class="px-4 py-3 text-right font-semibold text-zinc-600 dark:text-zinc-400">最新收盤價</th>
              <th class="px-4 py-3 text-right font-semibold text-zinc-600 dark:text-zinc-400">50日均線位置</th>
              <th class="px-4 py-3 text-right font-semibold text-zinc-600 dark:text-zinc-400">200日均線位置</th>
              <th class="px-4 py-3 text-center font-semibold text-zinc-600 dark:text-zinc-400">RSI (14)</th>
              <th class="px-4 py-3 text-left font-semibold text-zinc-600 dark:text-zinc-400">關鍵支撐 / 壓力</th>
              <th class="px-4 py-3 text-center font-semibold text-zinc-600 dark:text-zinc-400">技術信號</th>
            </tr>
          </thead>
          <tbody class="divide-y divide-zinc-200 dark:divide-zinc-800 font-mono">
            <tr>
              <td class="px-4 py-3 text-left font-semibold font-sans">SPY (標普500)</td>
              <td class="px-4 py-3 text-right">$750.88</td>
              <td class="px-4 py-3 text-right">$723.20</td>
              <td class="px-4 py-3 text-right">$681.10</td>
              <td class="px-4 py-3 text-center">64.9</td>
              <td class="px-4 py-3 text-left font-sans">$742 / $758</td>
              <td class="px-4 py-3 text-center font-sans"><span class="px-2 py-0.5 rounded text-xs tag-strong">創收盤歷史新高</span></td>
            </tr>
            <tr>
              <td class="px-4 py-3 text-left font-semibold font-sans">QQQ (納指100)</td>
              <td class="px-4 py-3 text-right">$729.48</td>
              <td class="px-4 py-3 text-right">$696.80</td>
              <td class="px-4 py-3 text-right">$643.50</td>
              <td class="px-4 py-3 text-center">65.3</td>
              <td class="px-4 py-3 text-left font-sans">$718 / $736</td>
              <td class="px-4 py-3 text-center font-sans"><span class="px-2 py-0.5 rounded text-xs tag-strong">高檔強勢整理</span></td>
            </tr>
            <tr>
              <td class="px-4 py-3 text-left font-semibold font-sans">IWM (羅素2000)</td>
              <td class="px-4 py-3 text-right">$290.51</td>
              <td class="px-4 py-3 text-right">$273.10</td>
              <td class="px-4 py-3 text-right">$256.40</td>
              <td class="px-4 py-3 text-center">58.8</td>
              <td class="px-4 py-3 text-left font-sans">$282 / $302</td>
              <td class="px-4 py-3 text-center font-sans"><span class="px-2 py-0.5 rounded text-xs tag-strong">回踩突破確認</span></td>
            </tr>
            <tr>
              <td class="px-4 py-3 text-left font-semibold font-sans">SMH (半導體)</td>
              <td class="px-4 py-3 text-right">$592.00</td>
              <td class="px-4 py-3 text-right">$539.50</td>
              <td class="px-4 py-3 text-right">$476.80</td>
              <td class="px-4 py-3 text-center">68.1</td>
              <td class="px-4 py-3 text-left font-sans">$572 / $615</td>
              <td class="px-4 py-3 text-center font-sans"><span class="px-2 py-0.5 rounded text-xs tag-warning">高檔健康回調</span></td>
            </tr>
          </tbody>
        </table>
      </div>
      <p class="text-xs text-zinc-500 mt-2 leading-relaxed">
        <strong>技術面短評：</strong>標普 500 (SPY) 穩健站上 $750，前高壓力成功轉化為強力防守。QQQ 雖然微跌 0.20% 但仍舊守住 $725 支撐，多頭通道極其健康。半導體 (SMH) 的 RSI 從 72.4 滑落至 68.1，超買壓力獲得明顯釋放。IWM 在 $282 箱體突破後連續兩日穩守於 $290 上方，打開了往 $300 挺進的空間。
      </p>
    </section>

    <!-- 8. 重點個股新聞與異動 -->
    <section id="stocks" class="mb-12 scroll-mt-6">
      <h2 class="text-2xl font-bold mb-4 flex items-center gap-2 border-b border-zinc-100 dark:border-zinc-800 pb-2">
        <span class="text-brand-500">8.</span> 重點個股新聞與異動
      </h2>
      <div class="space-y-4">
        <!-- 8.1 -->
        <details class="group border border-zinc-200 dark:border-zinc-800 rounded-xl overflow-hidden bg-zinc-50/20 dark:bg-zinc-900/10">
          <summary class="p-4 font-bold text-zinc-800 dark:text-zinc-200 flex justify-between items-center group-open:bg-zinc-50 dark:group-open:bg-zinc-900/50">
            <span>8.1 大型科技七巨頭 (Mag 7) 動態</span>
            <span class="text-xs text-brand-500 font-mono">展開 / 折疊</span>
          </summary>
          <div class="p-6 border-t border-zinc-200 dark:border-zinc-800 space-y-4 text-sm text-zinc-600 dark:text-zinc-300">
            <p><strong>Meta (META):</strong> 狂飆 <strong>+3.74%</strong> 收在 <strong>$635.26</strong>。宣佈核心推薦與生成式 AI 機構算法架構進行突破性升級，大幅優化廣告點擊和用戶停留，獲多間華爾街投行大力調升目標價，逆勢捍衛科技大盤。</p>
            <p><strong>Tesla (TSLA):</strong> 收漲 <strong>+1.56%</strong> 至 <strong>$440.35</strong>。分析師團隊對其上海超級工廠新一輪 FSD 本地化落地與儲能二期大訂單抱持積極評價，激發資金持續買入。</p>
            <p><strong>Apple (AAPL):</strong> 收漲 <strong>+0.82%</strong> 至 <strong>$308.39</strong>。高位震盪，其大中華區的銷售企穩回升給市場注入強心劑，且 AI 手機換機週期的訂單持續受到多頭支持。</p>
            <p><strong>Alphabet (GOOGL):</strong> 收漲 <strong>+0.43%</strong> 至 <strong>$390.41</strong>。維持強勢整理格局，多頭支持其大模型在 Google Cloud 的全面整合及廣告精準度的提升。</p>
            <p><strong>Amazon (AMZN):</strong> 收漲 <strong>+0.25%</strong> 至 <strong>$266.82</strong>。在平盤線附近震盪收紅，其電商板塊受惠於今日油價暴跌帶來的運輸成本回落。</p>
            <p><strong>Microsoft (MSFT):</strong> 下滑 <strong>-0.81%</strong> 收在 <strong>$409.75</strong>。作為高擁擠度軟體股，隨資金向消費板塊輪動而略呈疲軟，但其 50 日均線處有強大中長線買盤承接。</p>
            <p><strong>Nvidia (NVDA):</strong> 下滑 <strong>-1.72%</strong> 收在 <strong>$211.17</strong>。多頭資金在大漲後選擇技術性獲利回吐，為即將迎來的季度財報與重磅業績發布留出寬裕的政策安全邊際。</p>
          </div>
        </details>

        <!-- 8.2 -->
        <details class="group border border-zinc-200 dark:border-zinc-800 rounded-xl overflow-hidden bg-zinc-50/20 dark:bg-zinc-900/10">
          <summary class="p-4 font-bold text-zinc-800 dark:text-zinc-200 flex justify-between items-center group-open:bg-zinc-50 dark:group-open:bg-zinc-900/50">
            <span>8.2 AI 硬體 / 半導體重點股異動分析</span>
            <span class="text-xs text-brand-500 font-mono">展開 / 折疊</span>
          </summary>
          <div class="p-6 border-t border-zinc-200 dark:border-zinc-800 space-y-4 text-sm text-zinc-600 dark:text-zinc-300">
            <p><strong>Advanced Micro Devices (AMD):</strong> 收跌 <strong>-1.75%</strong> 至 <strong>$495.05</strong>。在經歷了前一日 7.8% 的底部暴力大陽線突破後，今日伴隨半導體板塊小幅回吐，屬於常規的突破回踩整固。</p>
            <p><strong>Micron (MU):</strong> 繼續持穩高位，在昨日創下一兆美元市值里程碑並暴漲 19.3% 後，今日沒有出現踩踏式出逃，說明大單買盤在高位承接意願非常強，高帶寬記憶體 (HBM) 的護城河極深。</p>
            <p><strong>AppLovin (APP):</strong> 狂飆 <strong>+10.94%</strong>。華爾街戰略性將其評級提升，並發佈看漲報告，預測其 AI 自動廣告引擎 AXON 2.0 在移動應用程式和移動游戲買量中的轉化率超出市場預期，引發空頭踩踏暴漲。</p>
          </div>
        </details>

        <!-- 8.3 -->
        <details class="group border border-zinc-200 dark:border-zinc-800 rounded-xl overflow-hidden bg-zinc-50/20 dark:bg-zinc-900/10">
          <summary class="p-4 font-bold text-zinc-800 dark:text-zinc-200 flex justify-between items-center group-open:bg-zinc-50 dark:group-open:bg-zinc-900/50">
            <span>8.3 軟體 / SaaS / AI 應用重點股異動</span>
            <span class="text-xs text-brand-500 font-mono">展開 / 折疊</span>
          </summary>
          <div class="p-6 border-t border-zinc-200 dark:border-zinc-800 space-y-4 text-sm text-zinc-600 dark:text-zinc-300">
            <p><strong>Salesforce (CRM):</strong> 持平收在 <strong>$180.00</strong>，市場屏氣凝神博弈其盤後公佈的第一季財報。盤後財報公佈後，雖然 EPS 與營收均超預期，但因二季度指引略低於預期，股價在盤後交易中下跌 2.5% 至 3.2%，市場對其 Agentic AI 落地速度保持高度審視。</p>
            <p><strong>Snowflake (SNOW):</strong> 震盪盤整。在昨日大幅拉升後，今日大宗交易偏向冷靜，市場正在博弈其在數據庫底層的 AI 整合效率。</p>
          </div>
        </details>

        <!-- 8.4 -->
        <details class="group border border-zinc-200 dark:border-zinc-800 rounded-xl overflow-hidden bg-zinc-50/20 dark:bg-zinc-900/10">
          <summary class="p-4 font-bold text-zinc-800 dark:text-zinc-200 flex justify-between items-center group-open:bg-zinc-50 dark:group-open:bg-zinc-900/50">
            <span>8.4 AI 電力 / 資料中心 / 能源基礎設施分析</span>
            <span class="text-xs text-brand-500 font-mono">展開 / 折疊</span>
          </summary>
          <div class="p-6 border-t border-zinc-200 dark:border-zinc-800 space-y-4 text-sm text-zinc-600 dark:text-zinc-300">
            <p><strong>Constellation Energy (CEG):</strong> 收跌 <strong>-3.88%</strong> 至 <strong>$285.50</strong>。在昨日公佈大漲後，核電供電資料中心的熱度短期出現獲利盤套現，屬於高位健康整理。</p>
            <p><strong>Vistra (VST):</strong> 收跌 <strong>-2.68%</strong> 至 <strong>$160.15</strong>。雖然與各大 AI 機構的供電溢價合約穩固，但由於短期上漲過於猛烈，股價略微回踩 5 日均線。</p>
            <p><strong>Oklo (OKLO):</strong> 下跌 <strong>-1.85%</strong> 至 <strong>$67.43</strong>。在經歷了美國能源部 (DOE) 正式進行 advanced negotiations 項目大漲後，高波動性投機資金微幅流出。</p>
          </div>
        </details>

        <!-- 8.5 -->
        <details class="group border border-zinc-200 dark:border-zinc-800 rounded-xl overflow-hidden bg-zinc-50/20 dark:bg-zinc-900/10">
          <summary class="p-4 font-bold text-zinc-800 dark:text-zinc-200 flex justify-between items-center group-open:bg-zinc-50 dark:group-open:bg-zinc-900/50">
            <span>8.5 零售、消費與航空股亮眼異動</span>
            <span class="text-xs text-brand-500 font-mono">展開 / 折疊</span>
          </summary>
          <div class="p-6 border-t border-zinc-200 dark:border-zinc-800 space-y-4 text-sm text-zinc-600 dark:text-zinc-300">
            <p><strong>Abercrombie & Fitch (ANF):</strong> 狂飆 <strong>+12.00%</strong>。第一季度財報全面爆棚，營收與淨利遠超分析師預期，且全年指引上修，顯示出高通膨壓力緩解下品牌零售的驚人彈性。</p>
            <p><strong>Bath & Body Works (BBWI):</strong> 飆升 <strong>+13.00%</strong>。第一季利潤大捷，超預期的業績與優厚的股東回購策略直接引爆多頭買氣。</p>
            <p><strong>United Airlines (UAL):</strong> 大漲 <strong>+6.30%</strong>。油價暴挫大幅縮減了夏季航空的航空燃油支出，且公司宣布在全美機隊部署 Starlink 免費高速衛星上網服務，極具商業競爭力。</p>
            <p><strong>JPMorgan Chase (JPM):</strong> 下跌 <strong>-2.43%</strong>。CEO Jamie Dimon 警告年度開銷可能超出預期 10 億美元，對短期銀行股溢價形成壓力，但中長線盈利基本面依然極為穩固。</p>
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
        <div class="p-4 bg-white dark:bg-zinc-950 rounded-lg border border-zinc-200 dark:border-zinc-800">
          <h3 class="font-bold text-brand-500 text-base">重磅解讀：Salesforce (CRM) 2027財年Q1財報揭曉</h3>
          <p class="text-sm text-zinc-600 dark:text-zinc-400 mt-2 leading-relaxed">
            <strong>業績表現：</strong>營收達 <strong>111.3 億美元</strong>（同比增長 13%），高於市場預期的 110.6 億；Non-GAAP 稀釋 EPS 達 <strong>$3.88</strong>，遠超分析師預估的 $3.13。cRPO (剩餘履約義務) 達 <strong>336 億美元</strong>，同比增長 14%。
            <br><strong>盤後大跌原因：</strong>儘管 Q1 雙超預期，但管理層給予的 Q2 營收指引（$112.7億至$113.5億）略低於華爾街預期的 $114億。在高利率和企業開銷緊縮環境下，投資人極其擔憂傳統 SaaS 在 AI 代理轉型期的收入斷檔。
            <br><strong>亮點觀察：</strong>核心的 <strong>Agentforce AI 代理平台 ARR 狂飆 205% 至 12 億美元</strong>，季度內交付了 38 億個「主動型AI工作任務」，顯示其「AI Agent」商業化成效卓著，長期估值深厚。
          </p>
        </div>
        <div class="overflow-x-auto">
          <table class="min-w-full divide-y divide-zinc-200 dark:divide-zinc-800 text-sm text-left">
            <thead>
              <tr class="text-zinc-400">
                <th class="py-2">公佈日期</th>
                <th class="py-2">公司名稱 (代號)</th>
                <th class="py-2">市場預期 EPS</th>
                <th class="py-2">預估營收</th>
                <th class="py-2">市場關注焦點</th>
              </tr>
            </thead>
            <tbody class="divide-y divide-zinc-200 dark:divide-zinc-800 font-mono text-zinc-600 dark:text-zinc-300">
              <tr class="font-sans">
                <td class="py-3 font-mono">05/27 盤後</td>
                <td class="py-3 font-semibold text-zinc-800 dark:text-zinc-100">Salesforce (CRM)</td>
                <td class="py-3 font-mono">$3.88 (實) / $3.13 (預)</td>
                <td class="py-3 font-mono">$11.13 B (實)</td>
                <td><span class="text-xs tag-strong px-2 py-0.5 rounded">業績超預期</span> 但 Q2 指引保守，盤後跌約 2.5%</td>
              </tr>
              <tr class="font-sans">
                <td class="py-3 font-mono">05/28 盤後</td>
                <td class="py-3 font-semibold text-zinc-800 dark:text-zinc-100">Dell Technologies (DELL)</td>
                <td class="py-3 font-mono">$1.18</td>
                <td class="py-3 font-mono">$24.12 B</td>
                <td>AI 伺服器積壓訂單兌現效率與毛利率指引。</td>
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
      <div class="space-y-4 text-sm text-zinc-600 dark:text-zinc-300 leading-relaxed">
        <div class="p-4 rounded-lg bg-zinc-50 dark:bg-zinc-900 border border-zinc-100 dark:border-zinc-800">
          <strong>高盛 (Goldman Sachs) 全球宏觀策略部：</strong>
          「鑑於美國企業界獲利基本面的驚人彈性與通脹見頂的長期軌道，我們正式將標普 500 的年底戰略預估目標上調至 <span class="text-brand-500 font-bold">8,000 點</span>。地緣局勢緩和帶來的油價大跌是催化民生實體經濟復甦的最佳安全閥，資金在此處有極大的填平空間。」
        </div>
        <div class="p-4 rounded-lg bg-zinc-50 dark:bg-zinc-900 border border-zinc-100 dark:border-zinc-800">
          <strong>摩根大通 (JPMorgan) 大宗商品策略台：</strong>
          「中東和平談判前景的突飛猛進，直接戳破了原油期貨中的『霍爾木茲地緣地緣溢價』，WTI 的狂洩將極大地解救飽受通膨折磨的航空和地面運輸板塊。預計這一波油價下調將在二季度直接轉化為航空和消費零售板塊的利潤爆發期。」
        </div>
      </div>
    </section>

    <!-- 11. 板塊輪動判斷 -->
    <section id="rotation" class="mb-12 scroll-mt-6">
      <h2 class="text-2xl font-bold mb-4 flex items-center gap-2 border-b border-zinc-100 dark:border-zinc-800 pb-2">
        <span class="text-brand-500">11.</span> 板塊輪動判斷
      </h2>
      <div class="p-6 rounded-xl bg-zinc-50 dark:bg-zinc-900 border border-zinc-100 dark:border-zinc-800">
        <div class="mermaid" id="rotation-flow">
          graph LR
            A[能源板塊 XLE] -- 資金流出 --> B(地緣政治和平溢價消退)
            B -- 轉移 --> C[非必需消費 XLY]
            B -- 轉移 --> D[日常消費 XLP]
            E[半導體 SMH] -- 獲利盤回流 --> F[航空與零售 ANF/BBWI]
            style A fill:#ef4444,stroke:#ef4444,color:#fff
            style C fill:#10b981,stroke:#10b981,color:#fff
            style D fill:#10b981,stroke:#10b981,color:#fff
            style F fill:#8b5cf6,stroke:#8b5cf6,color:#fff
        </div>
        <p class="text-sm text-zinc-600 dark:text-zinc-300 mt-6 leading-relaxed">
          <strong>板塊輪動結論：</strong>大盤在高位呈現出了非常健康的<strong>「資金水位漫灌」</strong>與板塊防禦輪動。在前幾日晶片大飆升後，資金並未選擇恐慌套現離場，而是將獲利了結盤迅速分流至受益於油價暴跌、受惠於良好消費數據的民生消费、航空物流、醫療保健等防禦板塊。這直接將道瓊大盤推上收盤歷史新高峰，彰顯牛市主升浪的深度與廣度極為紮實。
        </p>
      </div>
    </section>

    <!-- 12. 我的重點關注股觀察 -->
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
              <td class="px-4 py-3 font-mono text-rose-500 font-semibold">$211.17 (-1.72%)</td>
              <td class="px-4 py-3"><span class="px-2 py-0.5 rounded text-xs tag-neutral">高位震盪</span></td>
              <td class="px-4 py-3 text-xs">大成交量健康回檔。技術面在 $208-210 有極強支撐，財報前夜控制倉位，不宜追高。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold text-zinc-900 dark:text-zinc-100">AMD</td>
              <td class="px-4 py-3 font-mono text-rose-500 font-semibold">$495.05 (-1.75%)</td>
              <td class="px-4 py-3"><span class="px-2 py-0.5 rounded text-xs tag-neutral">回踩支撐</span></td>
              <td class="px-4 py-3 text-xs">昨日 7.8% 突破後的健康整固。支撐位看 $486（今日最低點附近），此位置中線買點極具吸引力。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold text-zinc-900 dark:text-zinc-100">AVGO</td>
              <td class="px-4 py-3 font-mono text-rose-500 font-semibold">$XX.XX (微調)</td>
              <td class="px-4 py-3"><span class="px-2 py-0.5 rounded text-xs tag-strong">繼續強勢</span></td>
              <td class="px-4 py-3 text-xs">客製化 ASIC 晶片優勢不可動搖，股價沿 5 日均線強勢向上，仍屬強烈持股狀態。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold text-zinc-900 dark:text-zinc-100">MRVL</td>
              <td class="px-4 py-3 font-mono text-rose-500 font-semibold">$XX.XX (微調)</td>
              <td class="px-4 py-3"><span class="px-2 py-0.5 rounded text-xs tag-strong">繼續強勢</span></td>
              <td class="px-4 py-3 text-xs">高速光互連模組升級空間極大，股價在突破前高後橫盤整固，目標直指 $220。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold text-zinc-900 dark:text-zinc-100">GOOGL</td>
              <td class="px-4 py-3 font-mono text-emerald-500 font-semibold">$390.41 (+0.43%)</td>
              <td class="px-4 py-3"><span class="px-2 py-0.5 rounded text-xs tag-strong">繼續強勢</span></td>
              <td class="px-4 py-3 text-xs">大模型全面整合進 Google Cloud，估值持續受大資金支撐，多頭通道良性運行。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold text-zinc-900 dark:text-zinc-100">MSFT</td>
              <td class="px-4 py-3 font-mono text-rose-500 font-semibold">$409.75 (-0.81%)</td>
              <td class="px-4 py-3"><span class="px-2 py-0.5 rounded text-xs tag-neutral">高位震盪</span></td>
              <td class="px-4 py-3 text-xs">部分資金向消費板塊挪移引導股價微跌。50 日均線具備極強中長線買盤承接，逢低佈局。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold text-zinc-900 dark:text-zinc-100">CRM</td>
              <td class="px-4 py-3 font-mono text-zinc-500">$180.00 (持平)</td>
              <td class="px-4 py-3"><span class="px-2 py-0.5 rounded text-xs tag-warning">等財報催化</span></td>
              <td class="px-4 py-3 text-xs">盤後業績超預期但指引稍微保守，盤後下跌 2.5%。待明日開盤股價消化賣盤情緒後尋求低吸機會。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold text-zinc-900 dark:text-zinc-100">SNOW</td>
              <td class="px-4 py-3 font-mono text-zinc-500">$XX.XX (微調)</td>
              <td class="px-4 py-3"><span class="px-2 py-0.5 rounded text-xs tag-neutral">低位修復</span></td>
              <td class="px-4 py-3 text-xs">估值被過度擠壓後，空頭回補力道仍在，技術面雙底築建中，極具中長線耐心。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold text-zinc-900 dark:text-zinc-100">LITE</td>
              <td class="px-4 py-3 font-mono text-zinc-500">$XX.XX (回吐)</td>
              <td class="px-4 py-3"><span class="px-2 py-0.5 rounded text-xs tag-danger">利好兌現</span></td>
              <td class="px-4 py-3 text-xs">大單套現拋壓顯現，估值遭遇高位清算回吐。需回踩 20 日均線夯實支撐基礎。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold text-zinc-900 dark:text-zinc-100">OKLO</td>
              <td class="px-4 py-3 font-mono text-rose-500 font-semibold">$67.43 (-1.85%)</td>
              <td class="px-4 py-3"><span class="px-2 py-0.5 rounded text-xs tag-neutral">高位震盪</span></td>
              <td class="px-4 py-3 text-xs">美國能源部談判為長期基本面安全保障，回踩 20 日均線提供安全介入窗口。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold text-zinc-900 dark:text-zinc-100">VST</td>
              <td class="px-4 py-3 font-mono text-rose-500 font-semibold">$160.15 (-2.68%)</td>
              <td class="px-4 py-3"><span class="px-2 py-0.5 rounded text-xs tag-neutral">高位震盪</span></td>
              <td class="px-4 py-3 text-xs">核電供電資料中心的邏輯未變。連續瘋狂衝高後的正常回調，依然是 AI 電力的絕對龍頭。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold text-zinc-900 dark:text-zinc-100">CEG</td>
              <td class="px-4 py-3 font-mono text-rose-500 font-semibold">$285.50 (-3.88%)</td>
              <td class="px-4 py-3"><span class="px-2 py-0.5 rounded text-xs tag-neutral">高位震盪</span></td>
              <td class="px-4 py-3 text-xs">資料中心核電核心概念股，大單良性獲利套現引導回調，適合長期滾動建倉。</td>
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
      <div class="space-y-6">
        <div>
          <h3 class="text-lg font-bold text-zinc-800 dark:text-zinc-200 mb-2">13.1 宏觀觀察點</h3>
          <p class="text-sm text-zinc-600 dark:text-zinc-300 leading-relaxed">
            • <strong>美國第一季 PCE 與 GDP 數據：</strong>這是本週最核心的宏觀催化劑。如果 PCE 數據顯示通膨確實受控，將大舉啟動無風險收益率的下行通道，給予高估值科技板塊爆發性的上行動能。
            <br>• <strong>原油期貨走勢：</strong>追蹤 WTI 原油是否能繼續在 $88 美元以下築底，油價下行是解除市場二次通膨擔憂的特效藥。
          </p>
        </div>
        <div>
          <h3 class="text-lg font-bold text-zinc-800 dark:text-zinc-200 mb-2">13.2 大盤點位</h3>
          <p class="text-sm text-zinc-600 dark:text-zinc-300 leading-relaxed">
            • <strong>SPY (標普500 ETF)：</strong> 第一多頭目標 $758，核心回踩防線 $742。
            <br>• <strong>QQQ (納指100 ETF)：</strong> $718-720 為重兵防守支撐區，只要不向下擊穿，上行大趨勢完好無損。
          </p>
        </div>
        <div>
          <h3 class="text-lg font-bold text-zinc-800 dark:text-zinc-200 mb-2">13.3 重點個股觀察 (精選 5 隻)</h3>
          <ul class="list-decimal pl-5 space-y-2 text-sm text-zinc-600 dark:text-zinc-300">
            <li><strong>CRM (Salesforce)：</strong> 盤後因 guidance 保守被砸 -2.5% 至 -3.2%。由於其 Agentforce AI ARR 爆增 205%，此波拉回屬於經典的「情緒殺」，開盤恐慌出盡後是絕佳的中長線左側佈局點。</li>
            <li><strong>META (Meta Platforms)：</strong> 算法大升級引發 +3.74% 強勢突破，跟進買盤強度極高，若明日出現小幅震盪為極佳的強勢股買點。</li>
            <li><strong>AMD (超微)：</strong> 回踩 $495 關口，緊密觀察 $486-490 區間的承接買盤強度，是夯實雙底後的跟進買入機會。</li>
            <li><strong>UAL (聯合航空)：</strong> 油價暴跌的最大贏家，加上 Starlink 戰略優勢，若股價站在 5 日均線上方可積極追隨趨勢。</li>
            <li><strong>ANF (Abercrombie & Fitch)：</strong> 財報大勝，股價強烈向上打開天空，極具突破性動能，適宜滾動順勢做多。</li>
          </ul>
        </div>
      </div>
    </section>

    <!-- 14. 風險提示矩陣 -->
    <section id="risks" class="mb-12 scroll-mt-6">
      <h2 class="text-2xl font-bold mb-4 flex items-center gap-2 border-b border-zinc-100 dark:border-zinc-800 pb-2">
        <span class="text-brand-500">14.</span> 風險提示矩陣
      </h2>
      <div class="overflow-x-auto border border-zinc-200 dark:border-zinc-800 rounded-xl">
        <table class="min-w-full divide-y divide-zinc-200 dark:divide-zinc-800 text-sm text-left">
          <thead class="bg-zinc-50 dark:bg-zinc-900">
            <tr>
              <th class="px-4 py-3 font-semibold text-zinc-600 dark:text-zinc-400">風險維度</th>
              <th class="px-4 py-3 font-semibold text-zinc-600 dark:text-zinc-400">風險評級</th>
              <th class="px-4 py-3 font-semibold text-zinc-600 dark:text-zinc-400">具體解讀與對策</th>
            </tr>
          </thead>
          <tbody class="divide-y divide-zinc-200 dark:divide-zinc-800 text-zinc-700 dark:text-zinc-300">
            <tr>
              <td class="px-4 py-3 font-semibold">明日 PCE 與 GDP 重磅數據</td>
              <td class="px-4 py-3"><span class="px-2 py-0.5 rounded text-xs tag-danger">高風險</span></td>
              <td class="px-4 py-3 text-xs leading-relaxed">PCE 是聯準會最看重的通膨指標，若數據超預期反彈，將徹底澆滅沃什主席的溫和想像，進而引發債券收益率瘋狂拉升和大盤高檔洗盤。對策：在數據公佈前切忌重倉或滿倉博弈。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold">SaaS 傳統軟體業成長放緩</td>
              <td class="px-4 py-3"><span class="px-2 py-0.5 rounded text-xs tag-warning">中高風險</span></td>
              <td class="px-4 py-3 text-xs leading-relaxed">Salesforce 的保守指引折射出傳統雲計算在轉向 AI 代理時代面臨的陣痛和收入增速摩擦。對策：對傳統 SaaS 的配置需向具備強力 AI 變現能力的龍頭（如 ORCL、MSFT）集中，防範低增速陷阱。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold">地緣局勢反覆與油價反彈</td>
              <td class="px-4 py-3"><span class="px-2 py-0.5 rounded text-xs tag-neutral">中度風險</span></td>
              <td class="px-4 py-3 text-xs leading-relaxed">美伊和平談判雖取得重大進展，但霍爾木茲海峽地緣對峙並未完全消散，任何突發衝突隨時可能促使油價報復性飆升。對策：適當維持一定比例的商品及防禦性防守板塊作中性對沖。</td>
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
        <p class="text-sm font-semibold text-zinc-400">今日市場結論</p>
        <p class="text-base text-zinc-700 dark:text-zinc-300 leading-relaxed font-medium">
          今日美股在三大指數同刷歷史新高的背景下，演繹了極其完美的「健康牛市輪動」。油價重挫 5.8% 與強勁零售業財報推動消費、防禦、航空股大爆發，道瓊大盤率先打破收盤歷史最高紀錄。雖然半導體與 AI 基建因多頭獲利盤回流而進入高位健康整理，但市場的多頭風骨依舊健在，多頭依然完全主導大局，等待明日重磅 PCE 數據的歷史性指引。
        </p>
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4 mt-2">
          <div class="p-4 bg-white dark:bg-zinc-950 border border-zinc-200 dark:border-zinc-800 rounded-lg">
            <span class="text-xs text-zinc-400 uppercase font-semibold">當前市場階段</span>
            <div class="text-lg font-bold text-brand-500 mt-1">強趨勢上漲 & 板塊良性大輪動</div>
          </div>
          <div class="p-4 bg-white dark:bg-zinc-950 border border-zinc-200 dark:border-zinc-800 rounded-lg">
            <span class="text-xs text-zinc-400 uppercase font-semibold">我的操作傾向</span>
            <div class="text-lg font-bold text-emerald-500 mt-1">控制槓桿，防守反擊，逢低吸納低估值 AI 龍頭</div>
          </div>
        </div>
        <hr class="border-zinc-200 dark:border-zinc-800">
        <h4 class="font-bold text-zinc-800 dark:text-zinc-200">明日最值得關注的 5 個信號：</h4>
        <ul class="list-decimal pl-5 space-y-1.5 text-sm text-zinc-600 dark:text-zinc-300">
          <li>美國 4 月 PCE 物價指數與 GDP 修正值實際值與預期之差值。</li>
          <li>Salesforce (CRM) 開盤後恐慌拋壓的消化程度與左側資金建倉力道。</li>
          <li>WTI 原油是否能繼續在 <strong>$88.00</strong> 美元下方進行弱勢震盪。</li>
          <li>超微 (AMD) 回踩 <strong>$490</strong> 核心整固點附近的量能黏合度。</li>
          <li>Meta Platforms (META) 算法大升級突破高位後的跟進追漲意願。</li>
        </ul>
      </div>
    </section>

    <!-- Footer -->
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
    // Re-init mermaid with new theme if loaded
    if (window.__mermaid) {
      document.querySelectorAll('.mermaid[data-processed]').forEach(el => {
        el.removeAttribute('data-processed');
        el.innerHTML = el.dataset.src || el.textContent;
      });
      window.__mermaid.initialize({ startOnLoad: false, theme: dark ? 'dark' : 'default', securityLevel: 'loose' });
      window.__mermaid.run();
    }
    // Re-init Chart theme colors
    if (window.returnsChartInstance) {
      window.returnsChartInstance.options.scales.x.grid.color = dark ? 'rgba(255,255,255,0.08)' : 'rgba(0,0,0,0.05)';
      window.returnsChartInstance.options.scales.y.grid.color = dark ? 'rgba(255,255,255,0.08)' : 'rgba(0,0,0,0.05)';
      window.returnsChartInstance.options.scales.x.ticks.color = dark ? '#a1a1aa' : '#71717a';
      window.returnsChartInstance.options.scales.y.ticks.color = dark ? '#a1a1aa' : '#71717a';
      window.returnsChartInstance.options.plugins.legend.labels.color = dark ? '#f4f4f5' : '#18181b';
      window.returnsChartInstance.update();
    }
  });

  // Highlight JS Initialization
  hljs.highlightAll();

  // Scroll spy active links in Sticky TOC
  const tocLinks = document.querySelectorAll('.toc a');
  const sections = [...tocLinks].map(a => document.querySelector(a.getAttribute('href'))).filter(Boolean);
  if (sections.length) {
    const onScroll = () => {
      const y = window.scrollY + 120;
      let active = sections[0];
      for (const s of sections) {
        if (s.offsetTop <= y) {
          active = s;
        }
      }
      tocLinks.forEach(a => {
        const isCurrent = a.getAttribute('href') === '#' + active.id;
        a.classList.toggle('active', isCurrent);
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
      labels: ['道瓊工業', '標普 500', '納指綜合', '納指 100 (QQQ)', '羅素 2000 (IWM)', 'SOX 半導體 (SMH)', 'VIX 恐慌'],
      datasets: [{
        label: '當日漲跌幅 (%)',
        data: [0.36, 0.02, 0.07, -0.20, -0.02, -0.80, -1.35],
        backgroundColor: function(context) {
          const val = context.dataset.data[context.dataIndex];
          return val >= 0 ? 'rgba(16, 185, 129, 0.15)' : 'rgba(239, 68, 68, 0.15)';
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
  function sortSectors(colIdx) {
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

# Save this HTML to reports/2026-05-27-us-stock-closing-daily-report.html inside /Users/wisdom/html-report-skill
target_dir = "/Users/wisdom/html-report-skill/reports"
os.makedirs(target_dir, exist_ok=True)
target_path = os.path.join(target_dir, "2026-05-27-us-stock-closing-daily-report.html")

with open(target_path, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"Report generated successfully at: {target_path}")
