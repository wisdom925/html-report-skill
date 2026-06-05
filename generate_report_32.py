import os
import json

html_content = """<!doctype html>
<html lang="zh-TW" class="scroll-smooth">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <title>美股收盤日報｜2026-06-03</title>
  <meta name="description" content="2026年6月3日美股收盤日報：美股大盤自歷史高點回落！中東地緣局勢驟緊，WTI原油大漲2.18%突破 $95 關口，ISM 服務通膨指標飆升，美債10年期利率攀升至 4.49%，標普500結束九連陽。盤後博通 (AVGO) 業績亮眼但因維持全年指引盤後大跌 6.29%，CrowdStrike (CRWD) 宣佈1拆4拆股但盤後震盪。">
  <meta property="og:title" content="美股收盤日報｜2026-06-03">
  <meta property="og:description" content="地緣政治升溫油價暴漲，大盤自高位回撤，標普終結九連陽！博通盤後跌6%營收超預期，CrowdStrike宣佈1拆4拆股。">
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
  <main class="space-y-4">
    <header class="mb-8">
      <div class="text-xs font-semibold text-zinc-400 dark:text-zinc-500 uppercase tracking-wider mb-2">Daily Closing Report</div>
      <h1 class="text-4xl font-extrabold tracking-tight mb-2 grad-text">美股收盤日報｜2026-06-03</h1>
      <p class="text-xl text-zinc-650 dark:text-zinc-400">美股自歷史高位回調！中東地緣局勢驟緊，WTI 原油大漲並突破 $95，通膨隱憂刺激 10 年期美債收益率攀升至 4.49%。三大指數齊收跌，標普跌 0.74% 終結九連陽，道指重挫逾 620 點。博通 (AVGO) 業績強勁但指引未超預期盤後重挫，CrowdStrike (CRWD) 宣布 1 拆 4 拆股但盤後震盪，市場由 AI 狂熱重回宏觀地緣拉鋸，資金防禦性流入能源板塊。</p>
      <div class="flex items-center gap-4 text-xs text-zinc-400 dark:text-zinc-500 mt-4 border-t border-zinc-100 dark:border-zinc-800 pt-4">
        <span>發布時間：2026-06-04 08:00 (Local Time)</span>
        <span>分析師：Antigravity AI</span>
      </div>
    </header>

    <!-- 0. 今日一句話總結 -->
    <section id="summary" class="mb-12 scroll-mt-6">
      <h2 class="text-2xl font-bold mb-4 flex items-center gap-2 border-b border-zinc-100 dark:border-zinc-800 pb-2">
        <span class="text-brand-500">0.</span> 今日一句話總結
      </h2>
      <div class="p-6 rounded-xl border border-zinc-200 dark:border-zinc-800 bg-zinc-50/50 dark:bg-zinc-900/50 space-y-4">
        <p class="text-sm text-zinc-600 dark:text-zinc-300 leading-relaxed">
          昨夜美股高位遇冷，受到中東美伊地緣局勢惡化及 ISM 服務業價格指數大幅升溫的雙重打擊，WTI原油拉升逾 2.18% 突破 $95 關口，引發市場對於通膨死灰復燃的焦慮。美債 10 年期收益率攀升至 4.490% 限制了成長股的估值空間，多頭九連陽的狂歡戛然而止。資金呈現避險 (Risk-off) 調倉，防禦性流入油氣能源與水電基建，而高位的科技巨頭（如微軟、輝達）與 SaaS 軟體板塊跌幅居前。
          <br><br>
          <strong>今日市場狀態：</strong><span class="font-bold text-rose-500">指數高位回踩，寬度全面惡化，地緣與利率雙利空點燃避險，AI 主線短期降溫整固。</span>
        </p>
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
                <td class="px-4 py-3 text-right">50,687.07</td>
                <td class="px-4 py-3 text-right text-rose-500 font-semibold">-1.21%</td>
                <td class="px-4 py-3 text-right">50,650.12 - 51,280.95</td>
                <td class="px-4 py-3 text-left font-sans text-xs text-rose-500">失守 5 日均線！地緣政經雙擊下，傳統與藍籌工業股遭遇獲利盤踩踏。</td>
              </tr>
              <tr>
                <td class="px-4 py-3 font-semibold font-sans text-zinc-900 dark:text-zinc-100">S&P 500</td>
                <td class="px-4 py-3 text-right">7,553.68</td>
                <td class="px-4 py-3 text-right text-rose-500 font-semibold">-0.74%</td>
                <td class="px-4 py-3 text-right">7,545.10 - 7,605.20</td>
                <td class="px-4 py-3 text-left font-sans text-xs text-rose-500">終結九連陽！高位長陰跌穿 5 日均線，下方考驗 7,530 的 10 日線支撐。</td>
              </tr>
              <tr>
                <td class="px-4 py-3 font-semibold font-sans text-zinc-900 dark:text-zinc-100">Nasdaq Composite</td>
                <td class="px-4 py-3 text-right">26,853.98</td>
                <td class="px-4 py-3 text-right text-rose-500 font-semibold">-0.89%</td>
                <td class="px-4 py-3 text-right">26,820.40 - 27,050.15</td>
                <td class="px-4 py-3 text-left font-sans text-xs text-rose-500">回撤整固。受巨頭普跌及利率上升壓制，日K線跌破 5 日線。</td>
              </tr>
              <tr>
                <td class="px-4 py-3 font-semibold font-sans text-zinc-900 dark:text-zinc-100">Nasdaq 100 / QQQ</td>
                <td class="px-4 py-3 text-right">30,571.24</td>
                <td class="px-4 py-3 text-right text-rose-500 font-semibold">-0.29%</td>
                <td class="px-4 py-3 text-right">30,520.10 - 30,700.50</td>
                <td class="px-4 py-3 text-left font-sans text-xs text-emerald-500">相對偏強。在個別硬體及博通常規交易時間支撐下，回調幅度小於綜合指數。</td>
              </tr>
              <tr>
                <td class="px-4 py-3 font-semibold font-sans text-zinc-900 dark:text-zinc-100">Russell 2000 / IWM</td>
                <td class="px-4 py-3 text-right">2,893.50</td>
                <td class="px-4 py-3 text-right text-rose-500 font-semibold">-1.30%</td>
                <td class="px-4 py-3 text-right">2,888.50 - 2,930.20</td>
                <td class="px-4 py-3 text-left font-sans text-xs text-rose-500">回吐補漲。小盤股對高融資利率高度敏感，美債收益率飆升下重跌。</td>
              </tr>
              <tr>
                <td class="px-4 py-3 font-semibold font-sans text-zinc-900 dark:text-zinc-100">SOX 半導體指數</td>
                <td class="px-4 py-3 text-right">13,916.96</td>
                <td class="px-4 py-3 text-right text-emerald-500 font-semibold">+2.04%</td>
                <td class="px-4 py-3 text-right">13,620.50 - 13,980.20</td>
                <td class="px-4 py-3 text-left font-sans text-xs text-emerald-500">逆市走強！受 ASML、ARM、博通及以太網大廠 ANET 大會行情支持收紅。</td>
              </tr>
              <tr>
                <td class="px-4 py-3 font-semibold font-sans text-zinc-900 dark:text-zinc-100">VIX 恐慌指數</td>
                <td class="px-4 py-3 text-right">16.20</td>
                <td class="px-4 py-3 text-right text-emerald-500 font-semibold">+0.31%</td>
                <td class="px-4 py-3 text-right">15.90 - 16.50</td>
                <td class="px-4 py-3 text-left font-sans text-xs text-rose-500">避險抬頭。伴隨大盤回跌及地緣恐慌，溫和升破 16 關口。</td>
              </tr>
            </tbody>
          </table>
        </div>
        <div class="stat-card flex flex-col justify-between">
          <div>
            <h4 class="font-bold text-zinc-800 dark:text-zinc-200">當日指數回報動態對比</h4>
            <p class="text-xs text-zinc-400 mt-1">反映各主要指數的單日相對強弱。地緣與利率焦慮壓制大盤，半導體 (SOX) 一枝獨秀，Russell 2000 與道指跌幅最深。</p>
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
          graph TD
            ADP_ISM[ADP就業+12.2萬 & ISM服務價格攀升至71.3] -->|雙擊通膨預期| Yields[10Y 美債收益率飆至 4.490%]
            Geopolitics[美伊在中東爆發摩擦] -->|威脅霍爾木茲海峽航道| Oil[WTI 原油暴漲 2.18% 突破 $95]
            Yields & Oil -->|壓制風險偏好| Markets[標普 500 / 納指自高位回撤]
            Markets -->|資金尋求防禦避險| Sectors[能源板塊 XLE +0.62% 逆市奪冠]
            Markets -->|財報觀望盤整| AfterHours[博通盤後跌6% / CrowdStrike拆股劇震]
        </div>
      </div>

      <div class="relative border-l border-zinc-200 dark:border-zinc-800 ml-4 space-y-6">
        <div class="relative pl-6">
          <div class="absolute -left-1.5 top-1.5 w-3 h-3 rounded-full bg-brand-500"></div>
          <time class="text-xs text-zinc-400 font-mono">08:15 AM</time>
          <h4 class="font-bold text-zinc-900 dark:text-zinc-100">5 月 ADP 就業數據出爐，薪資黏性增強</h4>
          <p class="text-sm text-zinc-600 dark:text-zinc-400 mt-1">
            美國 5 月 ADP 私營部門新增就業人數錄得 12.2 萬，高於預估的 12.0 萬。儘管就業增速呈平穩放緩態勢，但留在原職的員工薪資年增率依舊高達 4.4%，暗示勞動力成本存在一定黏性，削弱了降息空間。
          </p>
        </div>
        <div class="relative pl-6">
          <div class="absolute -left-1.5 top-1.5 w-3 h-3 rounded-full bg-brand-500"></div>
          <time class="text-xs text-zinc-400 font-mono">10:00 AM</time>
          <h4 class="font-bold text-zinc-900 dark:text-zinc-100">ISM 服務業 PMI 超預期，價格分項暴跳</h4>
          <p class="text-sm text-zinc-650 dark:text-zinc-400 mt-1">
            美國 5 月 ISM 服務業 PMI 錄得 54.5%（預期 53.7%，前值 53.6%），表明服務業活動穩健擴張。然而，最受關注的<strong>價格分項指標躥升至 71.3%</strong>，創下自 2022 年 8 月以來的最高水平，顯示二次通膨壓力極大。10年期美債利率直奔 4.49%，三大股指開盤迅速跳水。
          </p>
        </div>
        <div class="relative pl-6">
          <div class="absolute -left-1.5 top-1.5 w-3 h-3 rounded-full bg-brand-500"></div>
          <time class="text-xs text-zinc-400 font-mono">11:30 AM</time>
          <h4 class="font-bold text-zinc-900 dark:text-zinc-100">中東美伊局勢惡化，原油大漲避險升溫</h4>
          <p class="text-sm text-zinc-650 dark:text-zinc-400 mt-1">
            有情報顯示美國與伊朗在波斯灣空域發生局勢對峙，市場擔憂霍爾木茲海峽（Strait of Hormuz）原油輸送通道可能受阻。WTI 原油期貨應聲大漲 2.18% 突破 $95 關口。高油價進一步增強了市場對大宗商品通膨重燃的疑慮，避險情緒高漲，大型科技巨頭普跌，資金湧入石油板塊避險。
          </p>
        </div>
        <div class="relative pl-6">
          <div class="absolute -left-1.5 top-1.5 w-3 h-3 rounded-full bg-brand-500"></div>
          <time class="text-xs text-zinc-400 font-mono">02:00 PM</time>
          <h4 class="font-bold text-zinc-900 dark:text-zinc-100">聯準會公佈褐皮書，確認經濟溫和與物價平穩</h4>
          <p class="text-sm text-zinc-650 dark:text-zinc-400 mt-1">
            聯準會發布 6 月經濟狀況褐皮書，指出美國多數轄區經濟小幅或溫和擴張，消費者支出維持穩定，部分地區工資增速放緩。由於報告缺乏改變聯準會當前鷹派觀點的增量利多，美債利率仍橫盤於 4.490% 附近，指數低位弱勢震盪。
          </p>
        </div>
        <div class="relative pl-6">
          <div class="absolute -left-1.5 top-1.5 w-3 h-3 rounded-full bg-brand-500"></div>
          <time class="text-xs text-zinc-400 font-mono">04:00 PM</time>
          <h4 class="font-bold text-zinc-900 dark:text-zinc-100">尾盤獲利盤踩踏收最低，大盤九連陽告終</h4>
          <p class="text-sm text-zinc-650 dark:text-zinc-400 mt-1">
            尾盤多頭部隊選擇避險結算，道指狂洩 620 點，標普 500 下挫 0.74%，收於日內低位，完美終結了此前九個交易日以來的上漲勢頭。盤後博通 (AVGO) 業績強勁但指引平淡盤後重挫 6%，CrowdStrike (CRWD) 宣佈拆股，引導盤後市場劇烈洗盤。
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
                <p class="text-lg font-bold font-mono mt-1 text-rose-500">4.090%</p>
                <span class="text-xs text-rose-500">+1.0 Bps</span>
              </div>
              <div class="p-3 bg-white dark:bg-zinc-800 rounded-lg border border-zinc-100 dark:border-zinc-700">
                <span class="text-xs text-zinc-400">10年期美債收益率</span>
                <p class="text-lg font-bold font-mono mt-1 text-rose-500">4.490%</p>
                <span class="text-xs text-rose-500">+4.0 Bps</span>
              </div>
              <div class="p-3 bg-white dark:bg-zinc-800 rounded-lg border border-zinc-100 dark:border-zinc-700">
                <span class="text-xs text-zinc-400">30年期美債收益率</span>
                <p class="text-lg font-bold font-mono mt-1 text-rose-500">4.630%</p>
                <span class="text-xs text-rose-500">+3.0 Bps</span>
              </div>
            </div>
            <p class="text-xs text-zinc-500 leading-relaxed pt-2 border-t border-zinc-200 dark:border-zinc-850">
              <strong>收益率曲線解讀：</strong>受 ISM 服務業通膨指標飆升以及原油大漲的雙重助推，10年期及30年期國債收益率全天放量跳升。2Y-10Y 倒掛程度略微收窄至 -40.0Bps。收益率曲線的扁平化顯示市場大幅定價了「長端利率 Higher for longer」的通膨溢價，對遠期科技成長股的融資環境及估值空間產生負面擠壓。
            </p>
          </div>
        </div>

        <!-- Panel 2: Fed -->
        <div class="tab-panel">
          <div class="p-4 bg-zinc-50 dark:bg-zinc-900 border border-zinc-200 dark:border-zinc-800 rounded-xl space-y-3">
            <h4 class="font-bold text-zinc-800 dark:text-zinc-200">CME FedWatch 當前降息預估：</h4>
            <ul class="list-disc pl-5 text-sm space-y-2 text-zinc-650 dark:text-zinc-350">
              <li><strong>6 月 17 日 FOMC 議息預期：</strong>維持現行 3.50% - 3.75% 利率區間不變的機率由昨天的 98.2% 攀升至 **98.4%**，降息 25Bps 的可能性微乎其微（1.6%）。</li>
              <li><strong>年內降息次數預期：</strong>市場預期年內降息次數已穩定在 1 次，首次降息窗口大幅向 11-12 月推遲，降息的迫切性在強就業和服務業通膨壓力面前被大幅削弱。</li>
              <li><strong>官員態度：</strong>聯準會官員的基調在數據公佈後顯得更為審慎，多位官員在私下場合暗示若地緣局勢引發原油價格突破 $100 且服務通膨維持高位，年內將不再具備任何寬鬆條件。</li>
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
                <p class="text-sm font-bold font-mono mt-1">99.18</p>
                <span class="text-xs text-rose-500">+0.06%</span>
              </div>
              <div class="p-3 bg-white dark:bg-zinc-800 rounded-lg border border-zinc-100 dark:border-zinc-700">
                <span class="text-xs text-zinc-400">WTI 原油 (紐約)</span>
                <p class="text-sm font-bold font-mono mt-1 text-rose-500">$95.80</p>
                <span class="text-xs text-rose-500">+2.18%</span>
              </div>
              <div class="p-3 bg-white dark:bg-zinc-800 rounded-lg border border-zinc-100 dark:border-zinc-700">
                <span class="text-xs text-zinc-400">黃金現貨 (Gold)</span>
                <p class="text-sm font-bold font-mono mt-1 text-rose-500">$2,465.20</p>
                <span class="text-xs text-rose-500">-0.75%</span>
              </div>
              <div class="p-3 bg-white dark:bg-zinc-800 rounded-lg border border-zinc-100 dark:border-zinc-700">
                <span class="text-xs text-zinc-400">比特幣 (BTC)</span>
                <p class="text-sm font-bold font-mono mt-1 text-rose-500">$64,721</p>
                <span class="text-xs text-rose-500">-4.25%</span>
              </div>
            </div>
            <p class="text-xs text-zinc-500 leading-relaxed pt-2 border-t border-zinc-200 dark:border-zinc-850">
              <strong>資金流向分析：</strong>美元指數持穩在 99.18 附近偏多運行。地緣因素主導下，WTI 原油與 Brent 原油（大漲近 2% 至 $97.81）暴拉。高收益率引導黃金在歷史高位回吐避險買盤，跌幅 0.75%。比特幣受到流動性收緊與 ETF 連續失血拖累重挫 4.25% 回防 $64,000 關口，市場資金強烈偏向 Risk-off。
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
                    <td class="py-2.5 font-semibold">5月 ADP 私營新增就業 (萬)</td>
                    <td class="py-2.5 text-center">08:15 AM</td>
                    <td class="py-2.5 text-right font-mono font-bold text-rose-500">12.2</td>
                    <td class="py-2.5 text-right font-mono">12.0</td>
                    <td class="py-2.5 text-right font-mono">11.5</td>
                    <td class="py-2.5">略高於預期，顯示就業市場仍有較強的底盤支持，薪資增幅 4.4% 維持高位。</td>
                  </tr>
                  <tr>
                    <td class="py-2.5 font-semibold">5月 ISM 服務業 PMI</td>
                    <td class="py-2.5 text-center">10:00 AM</td>
                    <td class="py-2.5 text-right font-mono font-bold text-rose-500">54.5%</td>
                    <td class="py-2.5 text-right font-mono">53.7%</td>
                    <td class="py-2.5 text-right font-mono">53.6%</td>
                    <td class="py-2.5">擴張強勁。新訂單與商業活動火熱，證實實體需求韌性，支持利率高位停留。</td>
                  </tr>
                  <tr>
                    <td class="py-2.5 font-semibold">ISM 服務業價格指數</td>
                    <td class="py-2.5 text-center">10:00 AM</td>
                    <td class="py-2.5 text-right font-mono font-bold text-rose-500">71.3%</td>
                    <td class="py-2.5 text-right font-mono">--</td>
                    <td class="py-2.5 text-right font-mono">68.5%</td>
                    <td class="py-2.5 text-rose-500 font-bold">通膨警報！創下 2022 年 8 月以來的最高增速，證實服務通膨重現黏性。</td>
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
              <td class="px-4 py-3 text-right font-mono text-emerald-500 font-semibold" data-val="0.62">+0.62%</td>
              <td class="px-4 py-3 text-right font-mono" data-val="4.50">+4.50%</td>
              <td class="px-4 py-3 text-right font-mono" data-val="0.20">+0.20%</td>
              <td class="px-4 py-3 text-xs">中東美伊軍事摩擦升溫，霍爾木茲航道受阻預期推高油價，ExxonMobil 及 Chevron 吸金。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-medium">2</td>
              <td class="px-4 py-3 font-medium">公用事業 (Utilities)</td>
              <td class="px-4 py-3 font-mono">XLU</td>
              <td class="px-4 py-3 text-right font-mono text-emerald-500 font-semibold" data-val="0.12">+0.12%</td>
              <td class="px-4 py-3 text-right font-mono" data-val="0.90">+0.90%</td>
              <td class="px-4 py-3 text-right font-mono" data-val="-1.30">-1.30%</td>
              <td class="px-4 py-3 text-xs">AI 資料中心用電需求依舊，具備防守特質，板塊隨大盤避險買盤逆市收漲。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-medium">3</td>
              <td class="px-4 py-3 font-medium">資訊科技 (Information Technology)</td>
              <td class="px-4 py-3 font-mono">XLK</td>
              <td class="px-4 py-3 text-right font-mono text-emerald-500 font-semibold" data-val="0.09">+0.09%</td>
              <td class="px-4 py-3 text-right font-mono" data-val="0.80">+0.80%</td>
              <td class="px-4 py-3 text-right font-mono" data-val="18.20">+18.20%</td>
              <td class="px-4 py-3 text-xs">晶片與軟體強烈拉鋸，博通（AVGO）、ARM 及以太網 ANET 上漲勉強抵消微軟和輝達大跌。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-medium">4</td>
              <td class="px-4 py-3 font-medium">原材料 (Materials)</td>
              <td class="px-4 py-3 font-mono">XLB</td>
              <td class="px-4 py-3 text-right font-mono text-rose-500 font-semibold" data-val="-0.08">-0.08%</td>
              <td class="px-4 py-3 text-right font-mono" data-val="0.25">+0.25%</td>
              <td class="px-4 py-3 text-right font-mono" data-val="-1.20">-1.20%</td>
              <td class="px-4 py-3 text-xs">美債利率大幅拉升抑制大宗商品高位交易情緒，基本金屬及礦業小幅回軟。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-medium">5</td>
              <td class="px-4 py-3 font-medium">醫療保健 (Health Care)</td>
              <td class="px-4 py-3 font-mono">XLV</td>
              <td class="px-4 py-3 text-right font-mono text-rose-500 font-semibold" data-val="-0.10">-0.10%</td>
              <td class="px-4 py-3 text-right font-mono" data-val="0.70">+0.70%</td>
              <td class="px-4 py-3 text-right font-mono" data-val="1.70">+1.70%</td>
              <td class="px-4 py-3 text-xs">大盤回吐中防守性一般，受生技與製藥大廠個股漲跌互現影響小幅收跌。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-medium">6</td>
              <td class="px-4 py-3 font-medium">工業 (Industrials)</td>
              <td class="px-4 py-3 font-mono">XLI</td>
              <td class="px-4 py-3 text-right font-mono text-rose-500 font-semibold" data-val="-0.12">-0.12%</td>
              <td class="px-4 py-3 text-right font-mono" data-val="0.60">+0.60%</td>
              <td class="px-4 py-3 text-right font-mono" data-val="1.90">+1.90%</td>
              <td class="px-4 py-3 text-xs">高融資利率壓力令重型基建與航太軍工出現回調，僅 Eaton（ETN）及 Quanta（PWR）逆市上揚。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-medium">7</td>
              <td class="px-4 py-3 font-medium">通訊服務 (Communication Services)</td>
              <td class="px-4 py-3 font-mono">XLC</td>
              <td class="px-4 py-3 text-right font-mono text-rose-500 font-semibold" data-val="-0.12">-0.12%</td>
              <td class="px-4 py-3 text-right font-mono" data-val="-0.50">-0.50%</td>
              <td class="px-4 py-3 text-right font-mono" data-val="11.50">+11.50%</td>
              <td class="px-4 py-3 text-xs">谷歌（GOOGL）融資利空未除續走軟，抵消 Meta 當日強勢逆市反彈對板塊的拉動。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-medium">8</td>
              <td class="px-4 py-3 font-medium">房地產 (Real Estate)</td>
              <td class="px-4 py-3 font-mono">XLRE</td>
              <td class="px-4 py-3 text-right font-mono text-rose-500 font-semibold" data-val="-0.28">-0.28%</td>
              <td class="px-4 py-3 text-right font-mono" data-val="-1.10">-1.10%</td>
              <td class="px-4 py-3 text-right font-mono" data-val="-2.50">-2.50%</td>
              <td class="px-4 py-3 text-xs">美債長端利率跳升至 4.49%，直接打擊房地產信託與商業地產融資成本。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-medium">9</td>
              <td class="px-4 py-3 font-medium">日常消費品 (Consumer Staples)</td>
              <td class="px-4 py-3 font-mono">XLP</td>
              <td class="px-4 py-3 text-right font-mono text-rose-500 font-semibold" data-val="-0.33">-0.33%</td>
              <td class="px-4 py-3 text-right font-mono" data-val="-0.50">-0.50%</td>
              <td class="px-4 py-3 text-right font-mono" data-val="0.80">+0.80%</td>
              <td class="px-4 py-3 text-xs">非日常通膨升溫預期壓抑防禦股，資金在重債高股息必選消費巨頭中進行獲利了結。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-medium">10</td>
              <td class="px-4 py-3 font-medium">非日常消費品 (Consumer Discretionary)</td>
              <td class="px-4 py-3 font-mono">XLY</td>
              <td class="px-4 py-3 text-right font-mono text-rose-500 font-semibold" data-val="-0.46">-0.46%</td>
              <td class="px-4 py-3 text-right font-mono" data-val="-2.10">-2.10%</td>
              <td class="px-4 py-3 text-right font-mono" data-val="2.50">+2.50%</td>
              <td class="px-4 py-3 text-xs">特斯拉（TSLA）遭小摩喊賣下跌近 2%，零售與餐飲巨頭亦隨消費者支出焦慮全線下滑。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-medium">11</td>
              <td class="px-4 py-3 font-medium">金融 (Financials)</td>
              <td class="px-4 py-3 font-mono">XLF</td>
              <td class="px-4 py-3 text-right font-mono text-rose-500 font-semibold" data-val="-0.61">-0.61%</td>
              <td class="px-4 py-3 text-right font-mono" data-val="-0.40">-0.40%</td>
              <td class="px-4 py-3 text-right font-mono" data-val="0.20">+0.20%</td>
              <td class="px-4 py-3 text-xs">倒掛收窄利差理應改善，但大盤高位踩踏避險潮令銀行、投行及保險龍頭全線走弱。</td>
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
          <h3 class="text-lg font-bold text-emerald-500 mt-1">石油能源與水電基礎施工</h3>
          <p class="text-sm text-zinc-500 mt-2 leading-relaxed">
            油價大漲 2.18% 支撐 XLE 走強。電網變壓與電網改造施工巨頭 Quanta Services (PWR) 暴漲 2.52%，Eaton (ETN) 上漲 0.76% 刷新收盤新高，顯示公用電力基建抗震性強。
          </p>
        </div>
        <div class="p-5 rounded-xl border border-zinc-200 dark:border-zinc-800 bg-white dark:bg-zinc-900">
          <span class="text-xs font-semibold text-zinc-400">最弱風格</span>
          <h3 class="text-lg font-bold text-rose-500 mt-1">高估值 SaaS 軟體與小盤價值</h3>
          <p class="text-sm text-zinc-500 mt-2 leading-relaxed">
            利率直奔 4.5% 對高倍數 SaaS 軟體構成二次打擊。Salesforce (CRM) 大跌 4.19%，ServiceNow (NOW) 下挫 5.70%，軟體 ETF (IGV) 不斷下探支撐，羅素 2000 同時領跌大盤。
          </p>
        </div>
        <div class="p-5 rounded-xl border border-zinc-200 dark:border-zinc-800 bg-white dark:bg-zinc-900">
          <span class="text-xs font-semibold text-zinc-400">輪動特徵</span>
          <h3 class="text-lg font-bold text-amber-500 mt-1">AI 晶片高位震盪，避險防禦調倉</h3>
          <p class="text-sm text-zinc-500 mt-2 leading-relaxed">
            前幾日領漲的輝達（NVDA -3.07%）、微軟（MSFT -3.24%）高位回撤，資金大筆出逃，部分流入以太網龍頭 ANET (+2.70%) 與 ASML (+0.74%) 等有確定事件支持的晶片股，整體晶片股進入強震整理。
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
          <p class="text-sm text-zinc-655 dark:text-zinc-400 mt-2 leading-relaxed">
            S&P 500 高於 50MA 比例回落至 <strong>61.2%</strong> (前值 64.8%)；Nasdaq 100 比例跌至 <strong>57.1%</strong> (前值 59.5%)。這顯示出隨著昨夜大盤回撤，底層多數中小盤股的短期均線受到破壞，高位分化顯著。
          </p>
        </div>
        <div class="p-5 rounded-xl bg-zinc-50 dark:bg-zinc-900 border border-zinc-100 dark:border-zinc-800">
          <h4 class="font-bold text-zinc-800 dark:text-zinc-200">6.2 漲跌家數與新高</h4>
          <p class="text-sm text-zinc-655 dark:text-zinc-400 mt-2 leading-relaxed">
            <strong>NYSE 交易所：</strong>上漲 980 家，下跌 1,840 家。新高 45 家，新低 32 家。<br>
            <strong>Nasdaq 交易所：</strong>上漲 1,350 家，下跌 2,680 家。新高 52 家，新低 98 家。<br>
            下跌家數達到上漲家數的近 2 倍。新低股數量顯著攀升，市場賺錢效應迅速降溫。
          </p>
        </div>
        <div class="p-5 rounded-xl bg-zinc-50 dark:bg-zinc-900 border border-zinc-100 dark:border-zinc-800">
          <h4 class="font-bold text-zinc-800 dark:text-zinc-200">6.3 內部指標與量能</h4>
          <p class="text-sm text-zinc-655 dark:text-zinc-400 mt-2 leading-relaxed">
            <strong>Put/Call 比例：</strong>0.78 (前值 0.71)，看跌期權買盤顯著增加，顯示資金在高位積極佈防。量能與前一交易日基本持平，屬於典型的高位放量獲利了結與避險對沖，非系統性恐慌暴跌。
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
              <td class="px-4 py-3 text-right">$755.37</td>
              <td class="px-4 py-3 text-right">$746.20</td>
              <td class="px-4 py-3 text-right">$731.50</td>
              <td class="px-4 py-3 text-right">$685.10</td>
              <td class="px-4 py-3 text-center">61.2</td>
              <td class="px-4 py-3 font-sans text-xs text-left">$750 / $762</td>
              <td class="px-4 py-3 font-sans text-xs text-rose-500 font-semibold text-left">跌破 5MA，面臨高位多頭獲利了結</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold font-sans text-zinc-900 dark:text-zinc-100">QQQ (Nasdaq 100)</td>
              <td class="px-4 py-3 text-right">$744.45</td>
              <td class="px-4 py-3 text-right">$736.00</td>
              <td class="px-4 py-3 text-right">$722.80</td>
              <td class="px-4 py-3 text-right">$680.50</td>
              <td class="px-4 py-3 text-center">60.8</td>
              <td class="px-4 py-3 font-sans text-xs text-left">$738 / $750</td>
              <td class="px-4 py-3 font-sans text-xs text-zinc-500 font-semibold text-left">回踩 5MA 平台，守護主要上升軌道</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold font-sans text-zinc-900 dark:text-zinc-100">IWM (Russell 2000)</td>
              <td class="px-4 py-3 text-right">$289.35</td>
              <td class="px-4 py-3 text-right">$288.50</td>
              <td class="px-4 py-3 text-right">$286.00</td>
              <td class="px-4 py-3 text-right">$272.50</td>
              <td class="px-4 py-3 text-center">49.5</td>
              <td class="px-4 py-3 font-sans text-xs text-left">$285 / $293</td>
              <td class="px-4 py-3 font-sans text-xs text-rose-500 font-semibold text-left">跌穿 20MA，突破未果重回箱體震盪</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold font-sans text-zinc-900 dark:text-zinc-100">SMH (Semiconductors)</td>
              <td class="px-4 py-3 text-right">$297.80</td>
              <td class="px-4 py-3 text-right">$275.00</td>
              <td class="px-4 py-3 text-right">$257.00</td>
              <td class="px-4 py-3 text-right">$219.00</td>
              <td class="px-4 py-3 text-center">71.0</td>
              <td class="px-4 py-3 font-sans text-xs text-left">$285 / $305</td>
              <td class="px-4 py-3 font-sans text-xs text-rose-500 font-semibold text-left">高位震盪！超買 RSI 高居 71，警防盤後利空洗盤</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold font-sans text-zinc-900 dark:text-zinc-100">IGV (Software)</td>
              <td class="px-4 py-3 text-right">$81.54</td>
              <td class="px-4 py-3 text-right">$90.50</td>
              <td class="px-4 py-3 text-right">$92.00</td>
              <td class="px-4 py-3 text-right">$89.80</td>
              <td class="px-4 py-3 text-center">32.1</td>
              <td class="px-4 py-3 font-sans text-xs text-left">$80 / $88</td>
              <td class="px-4 py-3 font-sans text-xs text-rose-500 font-semibold text-left">加速破位，RSI 逼近超賣，尋找 200 日線支持</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold font-sans text-zinc-900 dark:text-zinc-100">XLK (Technology)</td>
              <td class="px-4 py-3 text-right">$198.39</td>
              <td class="px-4 py-3 text-right">$193.50</td>
              <td class="px-4 py-3 text-right">$189.20</td>
              <td class="px-4 py-3 text-right">$176.00</td>
              <td class="px-4 py-3 text-center">58.2</td>
              <td class="px-4 py-3 font-sans text-xs text-left">$192 / $200</td>
              <td class="px-4 py-3 font-sans text-xs text-zinc-500 font-semibold text-left">勉強守住 5MA，晶片雖撐但受軟體劇烈拖累</td>
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
        <div class="mt-4 space-y-3 text-sm text-zinc-650 dark:text-zinc-400">
          <p><strong>NVDA (Nvidia) -3.07% ($219.46)：</strong>Computex 大會狂熱氣氛稍歇，隨著大盤利率走高與地緣危機，投機買盤高位套現，股價跌穿 $220 關口，呈現技術性獲利回吐，但長線上行趨勢尚未破壞。</p>
          <p><strong>MSFT (Microsoft) -3.24% ($426.99)：</strong>遭受大筆高管及內部人出售持股新聞的打擊，遭遇強烈賣壓，跌幅在巨頭中居前，考驗 20 日均線（$425）的支撐強度。</p>
          <p><strong>AAPL (Apple) -1.33% ($311.02)：</strong>WWDC 2026 前期多頭獲利回防，受大盤走弱影響，股價跌穿 5 日均線至 $311，短線進入觀望期。</p>
          <p><strong>GOOGL (Alphabet) -0.97% ($354.92)：</strong>延續 800 億美元融資利空後的疲軟尋底，波克夏私募配售消息雖在昨日提供一定心理安全邊際，但並未帶來實質性反彈，股價微跌。</p>
          <p><strong>AMZN (Amazon) -0.39% ($255.53)：</strong>機房基建成本壓力與零售業務增長疑慮共振，在高位窄幅波動，形態偏防守。</p>
          <p><strong>META (Meta Platforms) +1.68% ($607.66)：</strong>當日唯一逆市收漲的科技巨頭。受惠於新推出的 Llama-3 企業端 AI 工具的強勁定價權，吸引逢低買盤買入，表現耀眼。</p>
          <p><strong>TSLA (Tesla) -1.94% ($415.50)：</strong>摩根大通在當日重申對特斯拉的「賣出」評級，指出其自動駕駛 FSD 的商業化路徑依然過於遙遠、估值嚴重高估，股價承壓大跌。</p>
        </div>
      </details>

      <!-- 8.2 半導體 -->
      <details class="mb-4 p-4 rounded-xl border border-zinc-200 dark:border-zinc-800 bg-zinc-50/50 dark:bg-zinc-900/50">
        <summary class="font-bold text-zinc-800 dark:text-zinc-200 text-base">8.2 AI 硬體 / 半導體重點股異動分析</summary>
        <div class="mt-4 space-y-3 text-sm text-zinc-650 dark:text-zinc-400">
          <p><strong>AVGO (Broadcom) $459.97 (Flat / 盤後 -6.29% 至 $420.30)：</strong>常規交易時間受板塊情緒支持收平。盤後發布 Q2 財報，雖營收年增 48% 達 $22.19B 及 EPS $2.44 擊敗市場預期，但因維持全年 AI 晶片目標於 $110B 未予調高，盤後引發獲利了結，暴跌 6.29%。</p>
          <p><strong>ANET (Arista Networks) +2.70% ($403.27)：</strong>受大摩將其評級調升為「超配」並給予 $420 目標價刺激，指其在乙太網路交換機與超大規模資料中心網絡的市場份額將持續吞噬對手，逆市走強。</p>
          <p><strong>ARM (ARM Holdings) +1.88% ($410.27)：</strong>英特爾與 AMD 相繼在其架構上推出新產品，在 Computex 年會特許授權主線發揮下，維持逆市上行。</p>
          <p><strong>ASML (ASML) +0.74% ($1,472.60)：</strong>據悉阿斯麥年內將順利向台積電交付首台最新的 High-NA EUV 光刻設備，提振其在荷蘭及美股市場的溢價，逆市收綠。</p>
          <p><strong>MU (Micron Technology) +0.73% ($1,071.91)：</strong>受惠於其 HBM3E 產能被輝達完全包下且供不應求的長線預期，展現極強韌性，創下收盤新高。</p>
          <p><strong>DELL (Dell Technologies) -3.30% ($420.95)：</strong>受 AI 伺服器短線擁擠交易退潮以及高管套現消息影響，跟隨輝達大幅回吐。</p>
          <p><strong>MRVL (Marvell Technology) -4.90% ($276.54)：</strong>大漲 32.52% 後，受短線嚴重超買偏離度過高影響，遭遇預期內的大筆獲利了結盤，跌 4.90%，缺口未回補。</p>
        </div>
      </details>

      <!-- 8.3 軟體 -->
      <details class="mb-4 p-4 rounded-xl border border-zinc-200 dark:border-zinc-800 bg-zinc-50/50 dark:bg-zinc-900/50">
        <summary class="font-bold text-zinc-800 dark:text-zinc-200 text-base">8.3 軟體 / SaaS / AI 應用重點股異動分析</summary>
        <div class="mt-4 space-y-3 text-sm text-zinc-650 dark:text-zinc-400">
          <p><strong>NOW (ServiceNow) -5.70% ($783.64)：</strong>SaaS 估值體系面臨二次下修威脅，在大盤回調中被作為高估值流動性來源拋售，跌破多條短中期均線，破位顯著。</p>
          <p><strong>PLTR (Palantir) -6.18% ($142.86)：</strong>短線跟隨大盤成長股回歸理性，爆量跌逾 6% 回踩 20 日線，多頭結構面臨考驗。</p>
          <p><strong>ORCL (Oracle) -5.43% ($229.85)：</strong>在高位遭獲利盤回吐打擊，由於市場對即將來臨的軟體業績及電網用電限制產生疑慮，股價大跌。</p>
          <p><strong>CRM (Salesforce) -4.19% ($192.43)：</strong>在業績大跌後缺乏催化，維持陰跌態勢，跌穿 $195 後短線趨勢偏淡。</p>
        </div>
      </details>

      <!-- 8.4 AI 電力 -->
      <details class="mb-4 p-4 rounded-xl border border-zinc-200 dark:border-zinc-850 bg-zinc-50/50 dark:bg-zinc-900/50">
        <summary class="font-bold text-zinc-800 dark:text-zinc-200 text-base">8.4 AI 電力 / 資料中心 / 能源基礎設施重點股分析</summary>
        <div class="mt-4 space-y-3 text-sm text-zinc-650 dark:text-zinc-400">
          <p><strong>PWR (Quanta Services) +2.52% ($711.73)：</strong>電力網工程承包需求爆表，作爲最大的高壓電網基建商，大筆資金因防禦性將其買入，創下歷史收盤新高。</p>
          <p><strong>ETN (Eaton Corporation) +0.76% ($420.82)：</strong>變壓器訂單積壓及電網升級基本面極為強勁，逆市大盤上揚，收盤創歷史新高。</p>
          <p><strong>CEG (Constellation Energy) -2.36% ($266.22)：</strong>隨電力股短線高位回調，但防守買盤在 $265 依然強大，中線維持高位震盪格局。</p>
          <p><strong>VST (Vistra Corp) -2.50% ($154.03)：</strong>此前暴漲 14.22% 後遭遇短線技術性回撤整理，高位獲利了結盤顯著，資金向更穩定的 XLE 能源板塊分流。</p>
          <p><strong>OKLO (Oklo Inc.) -3.04% ($13.10)：</strong>小盤投機核能股熱度退潮，因大筆內部人拋售申報，股價跟隨大盤退潮。</p>
        </div>
      </details>
    </section>

    <!-- 9. 財報日曆與解讀 -->
    <section id="earnings" class="mb-12 scroll-mt-6">
      <h2 class="text-2xl font-bold mb-4 flex items-center gap-2 border-b border-zinc-100 dark:border-zinc-800 pb-2">
        <span class="text-brand-500">9.</span> 財報日曆與財報解讀
      </h2>
      <div class="p-6 rounded-xl border border-zinc-200 dark:border-zinc-800 space-y-4 bg-zinc-50/30 dark:bg-zinc-900/30">
        <h3 class="text-lg font-bold text-zinc-950 dark:text-zinc-50">9.1 已公佈財報解讀</h3>
        
        <div class="border-l-4 border-emerald-500 pl-4 space-y-2 mb-4">
          <p class="font-bold text-zinc-900 dark:text-zinc-100">Broadcom Inc. (AVGO.US) - Q2 2026 財報</p>
          <ul class="list-disc pl-5 text-sm text-zinc-650 dark:text-zinc-400 space-y-1">
            <li><strong>業績表現：</strong>營收 $22.19 億美元（年增 48%），高於市場預期的 $22.01 億美元；非 GAAP 稀釋 EPS 報 $2.44，高於預估的 $2.40。</li>
            <li><strong>業務細節：</strong>AI 半導體銷售狂飆 200% 至 $10.8 億美元，但軟體基礎設施（VMware 整合）進展平穩。</li>
            <li><strong>市場反應：</strong>雖然季報表現優異，但因管理層沒有上調全年 AI 晶片銷售預期（維持 $110 億美元），被急躁的短線投機客判定為「超預期程度不夠」，股價盤後大跌 6.29% 至 $420.30。</li>
          </ul>
        </div>

        <div class="border-l-4 border-emerald-500 pl-4 space-y-2">
          <p class="font-bold text-zinc-900 dark:text-zinc-100">CrowdStrike Holdings (CRWD.US) - Q1 2027 財報</p>
          <ul class="list-disc pl-5 text-sm text-zinc-650 dark:text-zinc-400 space-y-1">
            <li><strong>業績表現：</strong>營收 $1.39 億美元（年增 30%），高於預期的 $1.36 億美元；非 GAAP EPS 報 $1.10，擊敗預估的 $1.07。</li>
            <li><strong>核心亮點：</strong>年度經常性收入 (ARR) 穩步增長，並宣佈進行 <strong>1 拆 4 的拆股計劃</strong>（將於 6 月 25 日登記，7 月 2 日正式開始拆股交易）。</li>
            <li><strong>市場反應：</strong>業績與指引雙 Beat 並伴隨拆股利多，但高估值科技股避險氛圍重，股價盤後先是暴漲 8%，隨後回吐大部分漲幅，維持在平盤附近寬幅震盪。</li>
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
            <tbody class="divide-y divide-zinc-250 dark:divide-zinc-855 text-zinc-700 dark:text-zinc-300">
              <tr>
                <td class="py-2">06-04 盤後</td>
                <td class="py-2 font-semibold">Lululemon (LULU)</td>
                <td class="py-2 text-right font-mono">$2.40</td>
                <td class="py-2 text-right font-mono">$2.20B</td>
                <td class="py-2">北美中產階級消費疲軟情況是否持續，以及中國市場增長是否見頂。</td>
              </tr>
              <tr>
                <td class="py-2">06-04 盤後</td>
                <td class="py-2 font-semibold">DocuSign (DOCU)</td>
                <td class="py-2 text-right font-mono">$0.83</td>
                <td class="py-2 text-right font-mono">$725M</td>
                <td class="py-2">企業端合約簽署需求在裁員和緊縮背景下的續約率與產品線擴展情況。</td>
              </tr>
              <tr>
                <td class="py-2">06-04 盤後</td>
                <td class="py-2 font-semibold">C3.ai (AI)</td>
                <td class="py-2 text-right font-mono">-$0.15</td>
                <td class="py-2 text-right font-mono">$92M</td>
                <td class="py-2">企業級 AI 應用的合約簽署增長與聯邦訂單對其年報收入的提振。</td>
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
        <p><strong>摩根大通喊賣特斯拉：</strong>摩根大通分析師發布報告重申對 Tesla 的「減持」評級，指其馬斯克薪資爭議削弱治理，且 FSD 在大眾車型上的商業化轉化率將低於樂觀預期，重估其汽車主業的毛利威脅，將目標價設定在低位，引發機構投機資金流出。</p>
        <p><strong>大摩對以太網路（ANET）調升評級：</strong>摩根士丹利（Morgan Stanley）出具報告稱，Arista Networks 將在 2026-2027 年的 AI 以太網路集群中取得主導地位，並將其列為板塊首選股，目標價調升至 $420，吸引大宗買單逆市瘋搶。</p>
        <p><strong>期權市場大宗避險異動：</strong>受週五非農報告及中東地緣影響，SPY 與 QQQ 盤中看跌期權（Put）大宗合約交易激增 320%，特別是集中在 6月5日到期的平值 Put。顯示高位獲利的大型機構正在通過期權工具對其美股多頭倉位進行鎖定或對沖，避險防禦心理強烈。</p>
      </div>
    </section>

    <!-- 11. 板塊輪動判斷 -->
    <section id="rotation" class="mb-12 scroll-mt-6">
      <h2 class="text-2xl font-bold mb-4 flex items-center gap-2 border-b border-zinc-100 dark:border-zinc-800 pb-2">
        <span class="text-brand-500">11.</span> 板塊輪動判斷
      </h2>
      <p class="text-sm text-zinc-600 dark:text-zinc-300 leading-relaxed">
        <strong>資金呈現「高位落袋，退守防禦」特徵：</strong>昨夜的板塊輪動代表了典型的 Risk-off 退守。在標普創下歷史新高的九連陽後，地緣軍事突發摩擦及 ISM 服務業價格上行，直接激發了短線投機客將科技與半導體巨頭高位變現。資金退守至<strong>原油能源 (XLE)</strong>、<strong>電網電能施工 (PWR, ETN)</strong> 及 <strong>XLU 公用事業</strong>等防禦安全屋。
        <br><br>
        SaaS 軟體應用則由於前期破位與企業 AI 計算開支擠壓的疑慮，淪為最主要的「失血池」。這輪輪動是多頭高位超買後的健康調降，在非農就業報告公佈前，大宗資金選擇退防防守，AI 晶片主線暫時降溫，但並未發生系統性資金出逃美股的恐慌。
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
              <td class="px-4 py-3 font-mono text-rose-500 font-semibold">$219.46 (-3.07%)</td>
              <td class="px-4 py-3"><span class="px-2 py-0.5 rounded text-xs tag-warning">回踩支撐</span></td>
              <td class="px-4 py-3 text-xs">隨大盤遭遇獲利回吐，跌穿 $220 平台，關注下方 10 日線 $212 支撐力度。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold text-zinc-900 dark:text-zinc-100">AMD</td>
              <td class="px-4 py-3 font-mono text-rose-500 font-semibold">$440.00 (-1.80%)</td>
              <td class="px-4 py-3"><span class="px-2 py-0.5 rounded text-xs tag-neutral">高位震盪</span></td>
              <td class="px-4 py-3 text-xs">Computex 利多釋放後回檔，跌穿 5 日均線，短線將圍繞 20 日線震盪。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold text-zinc-900 dark:text-zinc-100">AVGO</td>
              <td class="px-4 py-3 font-mono text-zinc-500 font-semibold">$459.97 (Flat)</td>
              <td class="px-4 py-3"><span class="px-2 py-0.5 rounded text-xs tag-warning">利好兌現</span></td>
              <td class="px-4 py-3 text-xs">常規收平。盤後業績佳但指引無超常爆點，大跌 6% 至 $420，需等待回踩完成。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold text-zinc-900 dark:text-zinc-100">MRVL</td>
              <td class="px-4 py-3 font-mono text-rose-500 font-semibold">$276.54 (-4.90%)</td>
              <td class="px-4 py-3"><span class="px-2 py-0.5 rounded text-xs tag-warning">短線過熱</span></td>
              <td class="px-4 py-3 text-xs">暴漲後回踩 5MA 洗籌，RSI 自 74 超買區回落，跳空缺口不破中線依然看好。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold text-zinc-900 dark:text-zinc-100">GOOGL</td>
              <td class="px-4 py-3 font-mono text-rose-500 font-semibold">$354.92 (-0.97%)</td>
              <td class="px-4 py-3"><span class="px-2 py-0.5 rounded text-xs tag-warning">回踩支撐</span></td>
              <td class="px-4 py-3 text-xs">維持在融資缺口下震盪尋底，波克夏私募配售提供底部防守，關注 $350 心理關口。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold text-zinc-900 dark:text-zinc-100">MSFT</td>
              <td class="px-4 py-3 font-mono text-rose-500 font-semibold">$426.99 (-3.24%)</td>
              <td class="px-4 py-3"><span class="px-2 py-0.5 rounded text-xs tag-warning">回踩支撐</span></td>
              <td class="px-4 py-3 text-xs">高管大筆拋售打擊情緒，K線長陰砸向 20 日線，短線需要整理消化。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold text-zinc-900 dark:text-zinc-100">META</td>
              <td class="px-4 py-3 font-mono text-emerald-500 font-semibold">$607.66 (+1.68%)</td>
              <td class="px-4 py-3"><span class="px-2 py-0.5 rounded text-xs tag-strong">繼續強勢</span></td>
              <td class="px-4 py-3 text-xs">逆市大漲，受 Llama-3 企業定價利多刺激，站穩均線組上方，展現極強抗震性。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold text-zinc-900 dark:text-zinc-100">AMZN</td>
              <td class="px-4 py-3 font-mono text-rose-500 font-semibold">$255.53 (-0.39%)</td>
              <td class="px-4 py-3"><span class="px-2 py-0.5 rounded text-xs tag-neutral">高位震盪</span></td>
              <td class="px-4 py-3 text-xs">股價在高位區間窄幅橫盤，高利率打擊估值，但 AWS 長期多頭不變。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold text-zinc-900 dark:text-zinc-100">ORCL</td>
              <td class="px-4 py-3 font-mono text-rose-500 font-semibold">$229.85 (-5.43%)</td>
              <td class="px-4 py-3"><span class="px-2 py-0.5 rounded text-xs tag-warning">回踩支撐</span></td>
              <td class="px-4 py-3 text-xs">自高位遭遇大筆獲利盤拋售，回吐至 20 日線，觀望等待企穩。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold text-zinc-900 dark:text-zinc-100">CRM</td>
              <td class="px-4 py-3 font-mono text-rose-500 font-semibold">$192.43 (-4.19%)</td>
              <td class="px-4 py-3"><span class="px-2 py-0.5 rounded text-xs tag-danger">破位風險</span></td>
              <td class="px-4 py-3 text-xs">技術面破位明顯，K線沿 5MA 陰跌，在 SaaS 寒冬未見曙光前切忌盲目抄底。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold text-zinc-900 dark:text-zinc-100">NOW</td>
              <td class="px-4 py-3 font-mono text-rose-500 font-semibold">$783.64 (-5.70%)</td>
              <td class="px-4 py-3"><span class="px-2 py-0.5 rounded text-xs tag-danger">破位風險</span></td>
              <td class="px-4 py-3 text-xs">跌穿 100 日線核心均線，高估值 SaaS 遭遇擠壓，短線退防防守。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold text-zinc-900 dark:text-zinc-100">SNOW</td>
              <td class="px-4 py-3 font-mono text-rose-500 font-semibold">$170.92 (-4.92%)</td>
              <td class="px-4 py-3"><span class="px-2 py-0.5 rounded text-xs tag-danger">破位風險</span></td>
              <td class="px-4 py-3 text-xs">跌回大跌起點，Summit 新品未獲資金買賬，短期轉為弱勢防守。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold text-zinc-900 dark:text-zinc-100">ADBE</td>
              <td class="px-4 py-3 font-mono text-rose-500 font-semibold">$473.60 (-2.70%)</td>
              <td class="px-4 py-3"><span class="px-2 py-0.5 rounded text-xs tag-neutral">高位震盪</span></td>
              <td class="px-4 py-3 text-xs">下週核心財報前震盪洗籌，觀望為主，不宜在此位置新開重倉。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold text-zinc-900 dark:text-zinc-100">PLTR</td>
              <td class="px-4 py-3 font-mono text-rose-500 font-semibold">$142.86 (-6.18%)</td>
              <td class="px-4 py-3"><span class="px-2 py-0.5 rounded text-xs tag-warning">回踩支撐</span></td>
              <td class="px-4 py-3 text-xs">高位長陰下殺跌破 5 日線，測試 20 日線，多頭籌碼出現鬆動。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold text-zinc-900 dark:text-zinc-100">LITE</td>
              <td class="px-4 py-3 font-mono text-rose-500 font-semibold">$67.48 (-0.80%)</td>
              <td class="px-4 py-3"><span class="px-2 py-0.5 rounded text-xs tag-neutral">高位震盪</span></td>
              <td class="px-4 py-3 text-xs">隨光通訊概念高位整理，波動不大，基本面保持平穩。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold text-zinc-900 dark:text-zinc-100">COHR</td>
              <td class="px-4 py-3 font-mono text-rose-500 font-semibold">$188.65 (-1.00%)</td>
              <td class="px-4 py-3"><span class="px-2 py-0.5 rounded text-xs tag-neutral">高位震盪</span></td>
              <td class="px-4 py-3 text-xs">大會炒作退潮，資金流入防守，高位量能平穩，中線趨勢健康。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold text-zinc-900 dark:text-zinc-100">ANET</td>
              <td class="px-4 py-3 font-mono text-emerald-500 font-semibold">$403.27 (+2.70%)</td>
              <td class="px-4 py-3"><span class="px-2 py-0.5 rounded text-xs tag-strong">繼續強勢</span></td>
              <td class="px-4 py-3 text-xs">大摩上調評級大漲，逆市創歷史收盤新高，乙太網多頭龍頭地位穩固。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold text-zinc-900 dark:text-zinc-100">FLNC</td>
              <td class="px-4 py-3 font-mono text-rose-500 font-semibold">$23.63 (-2.00%)</td>
              <td class="px-4 py-3"><span class="px-2 py-0.5 rounded text-xs tag-neutral">需要觀察</span></td>
              <td class="px-4 py-3 text-xs">高利率預期對儲能重壓，股價震盪破位，尋求 50 日均線止跌。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold text-zinc-900 dark:text-zinc-100">OKLO</td>
              <td class="px-4 py-3 font-mono text-rose-500 font-semibold">$13.10 (-3.04%)</td>
              <td class="px-4 py-3"><span class="px-2 py-0.5 rounded text-xs tag-neutral">需要觀察</span></td>
              <td class="px-4 py-3 text-xs">小盤核能高管申報減持打擊投機熱度，重回箱體下尋底，宜避開。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold text-zinc-900 dark:text-zinc-100">VST</td>
              <td class="px-4 py-3 font-mono text-rose-500 font-semibold">$154.03 (-2.50%)</td>
              <td class="px-4 py-3"><span class="px-2 py-0.5 rounded text-xs tag-neutral">高位震盪</span></td>
              <td class="px-4 py-3 text-xs">前日大漲後健康回踩，獲利盤高位平倉，電價上調邏輯仍提供中線底氣。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold text-zinc-900 dark:text-zinc-100">CEG</td>
              <td class="px-4 py-3 font-mono text-rose-500 font-semibold">$266.22 (-2.36%)</td>
              <td class="px-4 py-3"><span class="px-2 py-0.5 rounded text-xs tag-warning">回踩支撐</span></td>
              <td class="px-4 py-3 text-xs">大盤回吐中跟隨回撤，考驗 20 日線，中期牛市結構未變。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold text-zinc-900 dark:text-zinc-100">ETN</td>
              <td class="px-4 py-3 font-mono text-emerald-500 font-semibold">$420.82 (+0.76%)</td>
              <td class="px-4 py-3"><span class="px-2 py-0.5 rounded text-xs tag-strong">繼續強勢</span></td>
              <td class="px-4 py-3 text-xs">變壓器訂單背書，逆市創歷史收盤新高，牛市主升段不宜言頂。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold text-zinc-900 dark:text-zinc-100">VRT</td>
              <td class="px-4 py-3 font-mono text-rose-500 font-semibold">$117.41 (-0.92%)</td>
              <td class="px-4 py-3"><span class="px-2 py-0.5 rounded text-xs tag-neutral">高位震盪</span></td>
              <td class="px-4 py-3 text-xs">高位微跌震盪，液冷散熱景氣度尚可，沿 10 日均線碎步整固。</td>
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
      <div class="space-y-4 text-sm text-zinc-650 dark:text-zinc-400">
        <p><strong>13.1 宏觀觀察：</strong>明日將公佈初請失業金人數。在週五大非農前，市場預期將持續偏向觀望。需密切盯防 10年期美債利率是否會放量升破 4.52% 的警戒位置，以及原油價格是否會因為地緣局勢突發惡化而站穩 $96 以上，從而引發更深的大盤估值回吐。</p>
        <p><strong>13.2 大盤觀察：</strong>標普 500 下方關鍵防守位在 7,530（10日線），跌破則轉向 7,480-7,500 箱體下軌整理。QQQ 下方支撐看 $738-$740。若博通盤後大跌在明早引發晶片板塊集體跳空，需要留意開盤半小時內的拋壓力度，切忌盲目接飛刀。</p>
        <p><strong>13.3 板塊與個股觀察：</strong>
          <ul class="list-decimal pl-5 space-y-1">
            <li><strong>AVGO (博通)：</strong>盤後大跌 6% 至 $420.30。若明天常規時間回踩 $415-$420 區域企穩，可以視為中線極佳的 AI ASIC 龍頭低吸卡位點。</li>
            <li><strong>CRWD (CrowdStrike)：</strong>盤後業績佳並宣佈 1 拆 4 拆股。明天常規交易時間若能守在 $760 點位之上，將對低迷的 SaaS 軟體板塊注入強心針。</li>
            <li><strong>XLE (能源) / PWR (電網基建)：</strong>作為當前抗利率、抗地緣的防禦堡壘，若油價維持在 $95 上方，可繼續逢低分批加倉對沖科技股波動。</li>
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
              <td class="px-4 py-3 font-semibold text-zinc-900 dark:text-zinc-100">地緣政治與通膨風險</td>
              <td class="px-4 py-3 text-center"><span class="px-2 py-0.5 rounded text-xs tag-danger">高風險</span></td>
              <td class="px-4 py-3 text-xs">美伊中東局勢突然惡化。若霍爾木茲海峽發生實際性軍事封鎖或油輪遇襲，油價迅速突破 $100 將重演 2022 年大宗商品通膨噩夢，迫使聯準會重新考慮升息。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold text-zinc-900 dark:text-zinc-100">宏觀利率與債市風險</td>
              <td class="px-4 py-3 text-center"><span class="px-2 py-0.5 rounded text-xs tag-warning">中高風險</span></td>
              <td class="px-4 py-3 text-xs">ISM 服務價格升至 71.3% 及 ADP 強勁。若週五非農再度爆表，10 年期美債利率放量衝破 4.52% 阻力，將對高位成長股及中小盤估值構成持續殺估值威脅。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold text-zinc-900 dark:text-zinc-100">AI 晶片短線超買回吐</td>
              <td class="px-4 py-3 text-center"><span class="px-2 py-0.5 rounded text-xs tag-warning">中等風險</span></td>
              <td class="px-4 py-3 text-xs">博通 (AVGO) 財報未能給出超預期的指引增量，盤後大跌 6%。半導體板塊 RSI 此前高居 74 嚴重超買，短線有回調洗盤、平抑乖離率的技術性需求。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold text-zinc-900 dark:text-zinc-100">SaaS 應用技術破位</td>
              <td class="px-4 py-3 text-center"><span class="px-2 py-0.5 rounded text-xs tag-danger">高風險</span></td>
              <td class="px-4 py-3 text-xs">Salesforce、ServiceNow、Snowflake 均呈加速破位，SaaS 企業端預算被擠壓。在利潤轉化未獲大廠證實前，技術性尋底過程尚未結束，切忌左側重倉。</td>
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
        <p class="text-sm text-zinc-650 dark:text-zinc-300 leading-relaxed">
          <strong>今日市場結論：</strong>美股在連續創高後迎來健康調整，地緣油價大漲與 ISM 服務通膨強勁推高了債券利率，誘發多頭獲利盤了結避險。大盤標普結束九連上漲，板塊表現分化，資金向能源、基建避險。盤後博通指引未大超預期而大跌，預示次日半導體板塊將面臨洗盤壓力，大盤短期轉向箱體整固。
        </p>
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4 text-sm">
          <div class="space-y-2">
            <span class="text-xs font-semibold text-zinc-400">當前市場階段</span>
            <p class="text-base font-bold text-zinc-800 dark:text-zinc-200">高位震盪 / 避險健康回踩</p>
          </div>
          <div class="space-y-2">
            <span class="text-xs font-semibold text-zinc-400">操作傾向 (中性)</span>
            <p class="text-base font-bold text-zinc-800 dark:text-zinc-200">持股觀望。逢低低吸高業績確定性的博通等晶片龍頭，防禦增配原油能源 XLE，嚴格規避破位 SaaS 軟體。</p>
          </div>
        </div>
        <div class="p-4 bg-zinc-50 dark:bg-zinc-900 rounded-lg border border-zinc-100 dark:border-zinc-800">
          <span class="text-xs font-semibold text-zinc-400 block mb-2">最值得關注的 5 個訊號</span>
          <ul class="list-decimal pl-5 text-xs text-zinc-650 dark:text-zinc-350 space-y-1">
            <li><strong>WTI 原油價格：</strong>觀察是否會突破 $96 阻力，直接點燃二次通膨焦慮。</li>
            <li><strong>10年期美債利率：</strong>是否突破 4.52% 的日內高點並向 4.55% 衝擊。</li>
            <li><strong>博通 (AVGO) 開盤表現：</strong>盤後大跌 6.29% 後，常規時間是否有抄底買盤在 $420 附近卡位。</li>
            <li><strong>CrowdStrike (CRWD) 拆股效應：</strong>其在平盤附近能否止跌，從而拉動低迷的 SaaS 板塊。</li>
            <li><strong>初請失業金人數：</strong>非農就業報告公佈前，最後一個勞動力市場宏觀指標。</li>
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
        data: [-1.21, -0.74, -0.89, -0.29, -1.30, 2.04, 0.31],
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

# Save this HTML to reports/2026-06-03-us-stock-closing-daily-report.html inside /Users/wisdom/html-report-skill
target_dir = "/Users/wisdom/html-report-skill/reports"
os.makedirs(target_dir, exist_ok=True)
target_path = os.path.join(target_dir, "2026-06-03-us-stock-closing-daily-report.html")

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
exists = any(item.get("file") == "2026-06-03-us-stock-closing-daily-report.html" for item in manifest)
if not exists:
    new_entry = {
      "file": "2026-06-03-us-stock-closing-daily-report.html",
      "title": "美股收盤日報｜2026-06-03",
      "date": "2026-06-03",
      "description": "美股自歷史高位回調！中東地緣局勢驟緊，WTI原油大漲2.18%突破 $95 關口，ISM 服務通膨指標飆升，美債10年期利率攀升至 4.49%，標普500結束九連陽。盤後博通 (AVGO) 業績亮眼但因維持全年指引盤後大跌 6.29%，CrowdStrike (CRWD) 宣佈1拆4拆股但盤後震盪。"
    }
    manifest.insert(0, new_entry)
    with open(manifest_path, "w", encoding="utf-8") as f:
        json.dump(manifest, f, ensure_ascii=False, indent=2)
    print(f"Updated manifest.json successfully at: {manifest_path}")
else:
    print("manifest.json already contains the entry for 2026-06-03.")
