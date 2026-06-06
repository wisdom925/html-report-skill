import os
import json

html_content = """<!doctype html>
<html lang="zh-TW" class="scroll-smooth">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <title>美股收盤日報｜2026-06-05</title>
  <meta name="description" content="2026年6月5日美股收盤日報：5月非農大增17.2萬爆冷大超預期，引爆降息預期重估！美債收益率狂飆至4.55%，科技與半導體遭血洗，納指跌4.2%、費半暴跌10.26%，標普跌2.6%，創2025年10月以來最慘單日表現，市場避險情緒急速升溫。">
  <meta property="og:title" content="美股收盤日報｜2026-06-05">
  <meta property="og:description" content="非農大增17.2萬引爆美債收益率飆升，科技板塊遭血洗，費半大跌10.26%，標普創大跌2.60%寫下多月來最慘單日表現，防禦板塊逆市受捧。">
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
        <time class="text-sm font-semibold text-zinc-500 dark:text-zinc-400">2026-06-05</time>
      </div>
      <h1 class="text-3xl sm:text-4xl font-extrabold tracking-tight mb-4 bg-gradient-to-r from-zinc-900 to-zinc-700 dark:from-zinc-100 dark:to-zinc-400 bg-clip-text text-transparent">
        美股收盤日報｜非農大超預期降息預期重挫！美債狂飆科技與半導體遭血洗，費半崩跌10.26%，標普寫下多月來最慘單日表現
      </h1>
      <p class="text-lg text-zinc-500 dark:text-zinc-450 leading-relaxed">
        美國5月非農新增就業人數大增17.2萬人，遠超市場預估，重燃市場對通膨和聯準會「更久更高」利率政策的擔憂。美債收益率全面拉升，10年期美債衝上4.55%，觸發高估值科技與AI板塊的恐慌性拋售。費城半導體大跌10.26%，標普500大跌2.6%，市場呈現極端的避險調倉。
      </p>
    </header>

    <!-- 0. 今日一句話總結 -->
    <section id="summary" class="mb-12 scroll-mt-6">
      <h2 class="text-2xl font-bold mb-4 flex items-center gap-2 border-b border-zinc-100 dark:border-zinc-800 pb-2">
        <span class="text-brand-500">0.</span> 今日一句話總結
      </h2>
      <div class="p-5 rounded-xl bg-sky-50/50 dark:bg-sky-950/20 border border-sky-100 dark:border-sky-900/50 space-y-3">
        <ul class="list-disc pl-5 space-y-2 text-zinc-700 dark:text-zinc-300 text-sm sm:text-base leading-relaxed">
          <li><strong>大盤全面崩瀉：</strong>非農就業大超預期，引發市場強烈降息重估。標普 500 下跌 2.60%，納斯達克指數大跌 4.20%，道瓊下跌 1.30%，小盤股羅素 2000 下瀉 3.50%，費城半導體崩跌 10.26% 創下今年最大單日跌幅。</li>
          <li><strong>非農爆冷大增：</strong>美國 5 月新增非農就業 17.2 萬，高出預期 8.5 萬整整一倍，失業率維持 4.3%，薪資增速同比 3.4% 略微上行。美債 10 年期收益率飆升 8.0 Bps 至 4.55%，債市定價聯準會年內僅降息 0-1 次。</li>
          <li><strong>避險調倉劇烈：</strong>資金呈現顯著的「Risk-off 擁擠科技」與「避險湧入防禦」。半導體板塊與七巨頭全面失血，唯消費必需品（XLP）、醫療保健（XLV）與房地產（XLRE）逆勢上揚。</li>
          <li><strong>今日市場狀態：</strong><span class="px-2 py-0.5 rounded bg-rose-100 dark:bg-rose-950 text-rose-800 dark:text-rose-350 font-semibold text-xs sm:text-sm">指數暴跌，寬度惡化，AI與晶片板塊領瀉，市場進入中期高位整理。</span></li>
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
            <tr class="text-zinc-550 dark:text-zinc-400 text-left">
              <th class="px-4 py-3 font-semibold">指數名稱</th>
              <th class="px-4 py-3 font-semibold text-right">收盤點位</th>
              <th class="px-4 py-3 font-semibold text-right">漲跌點</th>
              <th class="px-4 py-3 font-semibold text-right">漲跌幅</th>
              <th class="px-4 py-3 font-semibold text-right">日內高點</th>
              <th class="px-4 py-3 font-semibold text-right">日內低點</th>
              <th class="px-4 py-3 font-semibold">技術狀態</th>
            </tr>
          </thead>
          <tbody class="divide-y divide-zinc-200 dark:divide-zinc-850 font-mono text-zinc-700 dark:text-zinc-300">
            <tr>
              <td class="px-4 py-3 font-semibold font-sans text-zinc-900 dark:text-zinc-100">Dow Jones (道瓊)</td>
              <td class="px-4 py-3 text-right">50,866.78</td>
              <td class="px-4 py-3 text-right text-rose-500 font-semibold">-695.15</td>
              <td class="px-4 py-3 text-right text-rose-500 font-semibold">-1.30%</td>
              <td class="px-4 py-3 text-right">51,250.00</td>
              <td class="px-4 py-3 text-right">50,810.00</td>
              <td class="px-4 py-3 font-sans text-xs text-rose-500 font-semibold">跌破 5MA/10MA</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold font-sans text-zinc-900 dark:text-zinc-100">S&P 500 (標普 500)</td>
              <td class="px-4 py-3 text-right">7,383.74</td>
              <td class="px-4 py-3 text-right text-rose-500 font-semibold">-200.57</td>
              <td class="px-4 py-3 text-right text-rose-500 font-semibold">-2.60%</td>
              <td class="px-4 py-3 text-right">7,495.00</td>
              <td class="px-4 py-3 text-right">7,378.00</td>
              <td class="px-4 py-3 font-sans text-xs text-rose-500 font-semibold">跌破 20MA 關鍵均線</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold font-sans text-zinc-900 dark:text-zinc-100">Nasdaq Composite (納指)</td>
              <td class="px-4 py-3 text-right">25,709.43</td>
              <td class="px-4 py-3 text-right text-rose-500 font-semibold">-1121.53</td>
              <td class="px-4 py-3 text-right text-rose-500 font-semibold">-4.20%</td>
              <td class="px-4 py-3 text-right">26,250.00</td>
              <td class="px-4 py-3 text-right">25,680.00</td>
              <td class="px-4 py-3 font-sans text-xs text-rose-500 font-semibold">跌破 20MA，回防 50MA</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold font-sans text-zinc-900 dark:text-zinc-100">Nasdaq 100 (納指 100)</td>
              <td class="px-4 py-3 text-right">28,948.24</td>
              <td class="px-4 py-3 text-right text-rose-500 font-semibold">-1459.57</td>
              <td class="px-4 py-3 text-right text-rose-500 font-semibold">-4.80%</td>
              <td class="px-4 py-3 text-right">30,100.00</td>
              <td class="px-4 py-3 text-right">28,880.00</td>
              <td class="px-4 py-3 font-sans text-xs text-rose-500 font-semibold">跌破 20MA/50MA</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold font-sans text-zinc-900 dark:text-zinc-100">Russell 2000 (羅素 2000)</td>
              <td class="px-4 py-3 text-right">2,833.50</td>
              <td class="px-4 py-3 text-right text-rose-500 font-semibold">-101.83</td>
              <td class="px-4 py-3 text-right text-rose-500 font-semibold">-3.50%</td>
              <td class="px-4 py-3 text-right">2,910.00</td>
              <td class="px-4 py-3 text-right">2,828.00</td>
              <td class="px-4 py-3 font-sans text-xs text-rose-500 font-semibold">抹平前日漲幅陷入箱體</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold font-sans text-zinc-900 dark:text-zinc-100">SOX 半導體指數</td>
              <td class="px-4 py-3 text-right">12,220.76</td>
              <td class="px-4 py-3 text-right text-rose-500 font-semibold">-1396.74</td>
              <td class="px-4 py-3 text-right text-rose-500 font-semibold">-10.26%</td>
              <td class="px-4 py-3 text-right">13,300.00</td>
              <td class="px-4 py-3 text-right">12,180.00</td>
              <td class="px-4 py-3 font-sans text-xs text-rose-500 font-semibold">跌穿 50MA，創最大單日調整</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold font-sans text-zinc-900 dark:text-zinc-100">VIX 波動率指數</td>
              <td class="px-4 py-3 text-right">21.51</td>
              <td class="px-4 py-3 text-right text-emerald-500 font-semibold">+5.12</td>
              <td class="px-4 py-3 text-right text-emerald-500 font-semibold">+31.24%</td>
              <td class="px-4 py-3 text-right">22.80</td>
              <td class="px-4 py-3 text-right">17.50</td>
              <td class="px-4 py-3 font-sans text-xs text-emerald-500 font-semibold">突破 20 點警示大關</td>
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

      <div class="flex flex-col space-y-6 relative before:absolute before:inset-0 before:left-4 before:w-0.5 before:bg-zinc-200 dark:before:bg-zinc-800 mb-8">
        <!-- Event 1 -->
        <div class="flex gap-6 relative items-start">
          <div class="w-8 h-8 rounded-full bg-brand-500 text-white flex items-center justify-center font-bold text-xs shrink-0 z-10 shadow-sm">盤前</div>
          <div class="bg-zinc-50 dark:bg-zinc-900 p-4 rounded-xl border border-zinc-200 dark:border-zinc-800 text-sm grow">
            <span class="text-xs text-zinc-400 font-semibold">08:30 AM</span>
            <h4 class="font-bold text-zinc-800 dark:text-zinc-200 mt-1">5月非農數據爆冷強勁</h4>
            <p class="text-zinc-550 dark:text-zinc-400 mt-1 leading-relaxed">
              美國勞工部公佈5月非農就業報告，大增 17.2 萬，超預期 8.5 萬整整一倍，且前兩個月數據合計上修 9.3 萬。美元與美債收益率直線飆升，10年期美債收益率瞬間拉升至 4.55%，黃金與比特幣等風險資產開盤前急速跳水。
            </p>
          </div>
        </div>

        <!-- Event 2 -->
        <div class="flex gap-6 relative items-start">
          <div class="w-8 h-8 rounded-full bg-brand-500 text-white flex items-center justify-center font-bold text-xs shrink-0 z-10 shadow-sm">開盤</div>
          <div class="bg-zinc-50 dark:bg-zinc-900 p-4 rounded-xl border border-zinc-200 dark:border-zinc-800 text-sm grow">
            <span class="text-xs text-zinc-400 font-semibold">09:30 AM</span>
            <h4 class="font-bold text-zinc-800 dark:text-zinc-200 mt-1">股指全線低開，晶片板塊雪崩</h4>
            <p class="text-zinc-550 dark:text-zinc-400 mt-1 leading-relaxed">
              科技股首當其衝承受估值下壓，半導體板塊（SOXX）低開低走。AMD、Arm、台積電ADR全面殺跌。唯有防禦性的消費必需品（XLP）與醫療（XLV）小幅高開，展現了抗震避險屬性。
            </p>
          </div>
        </div>

        <!-- Event 3 -->
        <div class="flex gap-6 relative items-start">
          <div class="w-8 h-8 rounded-full bg-brand-500 text-white flex items-center justify-center font-bold text-xs shrink-0 z-10 shadow-sm">午盤</div>
          <div class="bg-zinc-50 dark:bg-zinc-900 p-4 rounded-xl border border-zinc-200 dark:border-zinc-800 text-sm grow">
            <span class="text-xs text-zinc-400 font-semibold">12:30 PM</span>
            <h4 class="font-bold text-zinc-800 dark:text-zinc-200 mt-1">降息預期冰封，利率敏感資產遭拋</h4>
            <p class="text-zinc-550 dark:text-zinc-400 mt-1 leading-relaxed">
              市場對6月份與7月份聯準會降息的概率快速歸零，全年降息預期萎縮至 0-1 次。羅素 2000 指數抹去前日全部補漲大跌 3.5%，比特幣跌破 $60,000 大關，科技板塊恐慌性拋售加速。
            </p>
          </div>
        </div>

        <!-- Event 4 -->
        <div class="flex gap-6 relative items-start">
          <div class="w-8 h-8 rounded-full bg-brand-500 text-white flex items-center justify-center font-bold text-xs shrink-0 z-10 shadow-sm">尾盤</div>
          <div class="bg-zinc-50 dark:bg-zinc-900 p-4 rounded-xl border border-zinc-200 dark:border-zinc-800 text-sm grow">
            <span class="text-xs text-zinc-400 font-semibold">04:00 PM</span>
            <h4 class="font-bold text-zinc-800 dark:text-zinc-200 mt-1">恐慌拋售，費半收跌 10.26% 創歷史慘烈調整</h4>
            <p class="text-zinc-550 dark:text-zinc-400 mt-1 leading-relaxed">
              尾盤毫無買盤支撐，三大指數悉數收在接近全日最低點。半導體板塊崩跌，AMD 大跌 10.9%，Arm 狂瀉 12.8%，台積電 ADR 大跌 6.6%。最終標普 500 下跌 2.60%，VIX 狂飆至 21.51 警示水平。
            </p>
          </div>
        </div>

        <!-- Event 5 -->
        <div class="flex gap-6 relative items-start">
          <div class="w-8 h-8 rounded-full bg-brand-500 text-white flex items-center justify-center font-bold text-xs shrink-0 z-10 shadow-sm">盤後</div>
          <div class="bg-zinc-50 dark:bg-zinc-900 p-4 rounded-xl border border-zinc-200 dark:border-zinc-800 text-sm grow">
            <span class="text-xs text-zinc-400 font-semibold">04:15 PM</span>
            <h4 class="font-bold text-zinc-800 dark:text-zinc-200 mt-1">科技股持續陰跌，下週聚焦 CPI 與利率會議</h4>
            <p class="text-zinc-550 dark:text-zinc-400 mt-1 leading-relaxed">
              避險情緒持續，盤後個股維持弱勢整理。下週將公佈的 5 月 CPI 數據與聯準會利率會議成為市場生死判官。
            </p>
          </div>
        </div>
      </div>

      <!-- Timeline visual flow in Mermaid -->
      <div class="p-4 bg-zinc-50 dark:bg-zinc-900 rounded-xl border border-zinc-200 dark:border-zinc-800 text-center">
        <h3 class="text-xs font-semibold text-zinc-500 mb-4 uppercase tracking-wider">今日市場運作邏輯 (Mermaid)</h3>
        <pre class="mermaid bg-transparent">
graph TD
    NFP[5月非農大增 17.2萬 遠超預期] --> Yield[10Y美債收益率狂飆至 4.55%]
    Yield --> RateExpect[6月降息機率降至 3% 以下 / 年內降息預期降溫]
    RateExpect --> GrowthSell[高估值成長股與科技股遭血洗]
    GrowthSell --> TechCrash[納指大跌 4.2% / 費半狂瀉 10.26%]
    Yield --> Defensive[資金湧入防禦性板塊 XLP/XLV]
    Defensive --> RelStrength[消費必需品 XLP (+2.1%) 與醫療 XLV (+1.5%) 逆勢走強]
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
        <label for="tab3">3.3 美元與大宗商品</label>
        
        <input type="radio" id="tab4" name="macro-tabs">
        <label for="tab4">3.4 當日重要數據</label>

        <!-- Panel 1: Yields -->
        <div class="tab-panel w-full">
          <div class="p-4 bg-zinc-50 dark:bg-zinc-900 border border-zinc-200 dark:border-zinc-800 rounded-xl">
            <h4 class="font-bold text-zinc-800 dark:text-zinc-200 mb-3">美債收益率走勢與含義</h4>
            <div class="grid grid-cols-1 sm:grid-cols-3 gap-4 mb-4">
              <div class="p-3 bg-white dark:bg-zinc-800 rounded-lg border border-zinc-100 dark:border-zinc-700">
                <span class="text-xs text-zinc-400 font-semibold">2年期美債收益率 (2Y)</span>
                <p class="text-lg font-bold font-mono mt-1 text-rose-500">4.17%</p>
                <span class="text-xs text-rose-500">+14.0 Bps</span>
              </div>
              <div class="p-3 bg-white dark:bg-zinc-800 rounded-lg border border-zinc-100 dark:border-zinc-700">
                <span class="text-xs text-zinc-400 font-semibold">10年期美債收益率 (10Y)</span>
                <p class="text-lg font-bold font-mono mt-1 text-rose-500">4.55%</p>
                <span class="text-xs text-rose-500">+8.0 Bps</span>
              </div>
              <div class="p-3 bg-white dark:bg-zinc-800 rounded-lg border border-zinc-100 dark:border-zinc-700">
                <span class="text-xs text-zinc-400 font-semibold">30年期美債收益率 (30Y)</span>
                <p class="text-lg font-bold font-mono mt-1 text-rose-500">4.70%</p>
                <span class="text-xs text-rose-500">+8.0 Bps</span>
              </div>
            </div>
            <p class="text-xs sm:text-sm text-zinc-500 leading-relaxed">
              <strong>收益率解讀：</strong>由於非農就業報告大超預期，顯示出就業市場極具韌性。債市收益率出現「熊市扁平化」（Bear Flattening）的狂飆。2年期美債收益率大漲 14 個基點至 4.17%，10年期美債收益率大漲至 4.55%。這重創了科技股與成長股的折現模型，是今日大盤暴跌的宏觀核心原因。
            </p>
          </div>
        </div>

        <!-- Panel 2: FedWatch -->
        <div class="tab-panel w-full">
          <div class="p-4 bg-zinc-50 dark:bg-zinc-900 border border-zinc-200 dark:border-zinc-800 rounded-xl">
            <h4 class="font-bold text-zinc-800 dark:text-zinc-200 mb-3">CME FedWatch 聯邦基金利率期貨預期</h4>
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-4 mb-4">
              <div class="p-3 bg-white dark:bg-zinc-800 rounded-lg border border-zinc-100 dark:border-zinc-700">
                <span class="text-xs text-zinc-400 font-semibold">6月17日 FOMC 會議降息機率</span>
                <p class="text-lg font-bold font-mono mt-1 text-zinc-650 dark:text-zinc-300">3.0%</p>
                <span class="text-xs text-zinc-400">維持利率於 5.25%-5.50% 機率為 97.0%</span>
              </div>
              <div class="p-3 bg-white dark:bg-zinc-800 rounded-lg border border-zinc-100 dark:border-zinc-700">
                <span class="text-xs text-zinc-400 font-semibold">7月29日 FOMC 會議降息機率</span>
                <p class="text-lg font-bold font-mono mt-1 text-zinc-650 dark:text-zinc-300">0.0%</p>
                <span class="text-xs text-zinc-400">維持利率不變機率約 96.0%，年內降息次數預期降至0-1次。</span>
              </div>
            </div>
            <p class="text-xs sm:text-sm text-zinc-500 leading-relaxed">
              <strong>貨幣政策分析：</strong>非農大熱重擊了聯聯準會年內的降息路徑。6月降息的機率只剩下 3.0%，市場對7月降息基本完全放棄。市場甚至開始預期，若是通膨在下半年未見降溫，聯聯準會甚至需要重新考慮加息。
            </p>
          </div>
        </div>

        <!-- Panel 3: Dollar & Commodities -->
        <div class="tab-panel w-full">
          <div class="p-4 bg-zinc-50 dark:bg-zinc-900 border border-zinc-200 dark:border-zinc-800 rounded-xl">
            <h4 class="font-bold text-zinc-800 dark:text-zinc-200 mb-3">美元、黃金、原油與加密貨幣</h4>
            <div class="grid grid-cols-2 sm:grid-cols-4 gap-4 mb-4 font-mono">
              <div class="p-3 bg-white dark:bg-zinc-800 rounded-lg border border-zinc-100 dark:border-zinc-700">
                <span class="text-xs text-zinc-400 font-sans">美元指數 (DXY)</span>
                <p class="text-sm sm:text-base font-bold mt-1 text-rose-500">100.80</p>
                <span class="text-xs text-rose-500">+0.55%</span>
              </div>
              <div class="p-3 bg-white dark:bg-zinc-800 rounded-lg border border-zinc-100 dark:border-zinc-700">
                <span class="text-xs text-zinc-400 font-sans">黃金現貨 (Gold)</span>
                <p class="text-sm sm:text-base font-bold mt-1 text-rose-500">$4,330.00</p>
                <span class="text-xs text-rose-500">-1.95%</span>
              </div>
              <div class="p-3 bg-white dark:bg-zinc-800 rounded-lg border border-zinc-100 dark:border-zinc-700">
                <span class="text-xs text-zinc-400 font-sans">Brent 原油</span>
                <p class="text-sm sm:text-base font-bold mt-1 text-rose-500">$93.09</p>
                <span class="text-xs text-rose-500">-1.26%</span>
              </div>
              <div class="p-3 bg-white dark:bg-zinc-800 rounded-lg border border-zinc-100 dark:border-zinc-700">
                <span class="text-xs text-zinc-400 font-sans">比特幣 (BTC)</span>
                <p class="text-sm sm:text-base font-bold mt-1 text-rose-500">$59,770</p>
                <span class="text-xs text-rose-500">-4.40%</span>
              </div>
            </div>
            <p class="text-xs sm:text-sm text-zinc-500 leading-relaxed">
              <strong>資金流向分析：</strong>強勁的就業數據推動美元反彈，DXY 攀升至 100.80。在強美元與高利率的雙重打擊下，黃金大跌 1.95% 報 $4,330 左右，原油回落 1.26%。比特幣跌破 $60,000 整數關口，大跌 4.40%，顯示出市場中投機性高流動性資金大舉流出。
            </p>
          </div>
        </div>

        <!-- Panel 4: Data -->
        <div class="tab-panel w-full">
          <div class="p-4 bg-zinc-50 dark:bg-zinc-900 border border-zinc-200 dark:border-zinc-800 rounded-xl">
            <h4 class="font-bold text-zinc-800 dark:text-zinc-200 mb-3">今日公佈重要經濟數據</h4>
            <div class="overflow-x-auto">
              <table class="min-w-full text-xs sm:text-sm divide-y divide-zinc-200 dark:divide-zinc-800">
                <thead>
                  <tr class="text-zinc-550 dark:text-zinc-400 text-left">
                    <th class="py-2">指標名稱</th>
                    <th class="py-2 text-right">實際值</th>
                    <th class="py-2 text-right">預期值</th>
                    <th class="py-2 text-right">前值</th>
                    <th class="py-2 pl-4">市場解讀</th>
                  </tr>
                </thead>
                <tbody class="divide-y divide-zinc-200 dark:divide-zinc-850 text-zinc-700 dark:text-zinc-300">
                  <tr>
                    <td class="py-2.5 font-semibold">5月新增非農就業 (萬)</td>
                    <td class="py-2.5 text-right font-mono font-bold text-rose-500">17.2</td>
                    <td class="py-2.5 text-right font-mono">8.5</td>
                    <td class="py-2.5 text-right font-mono">23.5</td>
                    <td class="py-2.5 pl-4 text-rose-500">大超預期一倍，反映勞動力市場異常強韌，對降息不利。</td>
                  </tr>
                  <tr>
                    <td class="py-2.5 font-semibold">5月失業率</td>
                    <td class="py-2.5 text-right font-mono font-bold text-zinc-650">4.3%</td>
                    <td class="py-2.5 text-right font-mono">4.3%</td>
                    <td class="py-2.5 text-right font-mono">4.3%</td>
                    <td class="py-2.5 pl-4">與預期持平，就業市場並未顯著惡化。</td>
                  </tr>
                  <tr>
                    <td class="py-2.5 font-semibold">5月平均每小時薪資年率</td>
                    <td class="py-2.5 text-right font-mono font-bold text-rose-500">3.4%</td>
                    <td class="py-2.5 text-right font-mono">3.3%</td>
                    <td class="py-2.5 text-right font-mono">3.4%</td>
                    <td class="py-2.5 pl-4 text-rose-500">高於預期的3.3%，薪資上行加劇了市場對「工資-通膨」螺旋的擔憂。</td>
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
          <span class="text-brand-500">4.</span> S&P 500 十一個板塊表現
        </h2>
        <input type="text" id="sectorSearch" placeholder="搜尋板塊或 ETF..." class="px-3 py-1.5 text-sm rounded-md border border-zinc-300 dark:border-zinc-700 bg-white dark:bg-zinc-900 focus:outline-none focus:ring-1 focus:ring-brand-500">
      </div>

      <div class="overflow-x-auto border border-zinc-200 dark:border-zinc-800 rounded-xl">
        <table class="min-w-full divide-y divide-zinc-200 dark:divide-zinc-800 text-sm" id="sectorsTable">
          <thead class="bg-zinc-50 dark:bg-zinc-900 select-none">
            <tr>
              <th onclick="sortSectors(0)" class="cursor-pointer hover:bg-zinc-100 dark:hover:bg-zinc-800 px-4 py-3 text-left font-semibold text-zinc-650 dark:text-zinc-400">排名 ▲▼</th>
              <th onclick="sortSectors(1)" class="cursor-pointer hover:bg-zinc-100 dark:hover:bg-zinc-800 px-4 py-3 text-left font-semibold text-zinc-650 dark:text-zinc-400">板塊 ▲▼</th>
              <th onclick="sortSectors(2)" class="cursor-pointer hover:bg-zinc-100 dark:hover:bg-zinc-800 px-4 py-3 text-left font-semibold text-zinc-650 dark:text-zinc-400">ETF ▲▼</th>
              <th onclick="sortSectors(3)" class="cursor-pointer hover:bg-zinc-100 dark:hover:bg-zinc-800 px-4 py-3 text-right font-semibold text-zinc-650 dark:text-zinc-400">當日漲跌幅 ▲▼</th>
              <th onclick="sortSectors(4)" class="cursor-pointer hover:bg-zinc-100 dark:hover:bg-zinc-800 px-4 py-3 text-right font-semibold text-zinc-650 dark:text-zinc-400">近5日 ▲▼</th>
              <th onclick="sortSectors(5)" class="cursor-pointer hover:bg-zinc-100 dark:hover:bg-zinc-800 px-4 py-3 text-right font-semibold text-zinc-650 dark:text-zinc-400">近1月 ▲▼</th>
              <th class="px-4 py-3 text-left font-semibold text-zinc-650 dark:text-zinc-400">主要驅動</th>
            </tr>
          </thead>
          <tbody class="divide-y divide-zinc-200 dark:divide-zinc-800">
            <tr>
              <td class="px-4 py-3 font-medium">1</td>
              <td class="px-4 py-3 font-medium">必需消費 (Consumer Staples)</td>
              <td class="px-4 py-3 font-mono">XLP</td>
              <td class="px-4 py-3 text-right font-mono text-emerald-500 font-semibold" data-val="2.10">+2.10%</td>
              <td class="px-4 py-3 text-right font-mono" data-val="0.90">+0.90%</td>
              <td class="px-4 py-3 text-right font-mono" data-val="0.50">+0.50%</td>
              <td class="px-4 py-3 text-zinc-500">大盤暴跌下，資金瘋狂湧入民生必需品板塊進行高純度避險。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-medium">2</td>
              <td class="px-4 py-3 font-medium">醫療保健 (Health Care)</td>
              <td class="px-4 py-3 font-mono">XLV</td>
              <td class="px-4 py-3 text-right font-mono text-emerald-500 font-semibold" data-val="1.50">+1.50%</td>
              <td class="px-4 py-3 text-right font-mono" data-val="1.10">+1.10%</td>
              <td class="px-4 py-3 text-right font-mono" data-val="3.20">+3.20%</td>
              <td class="px-4 py-3 text-zinc-550">避險情緒主導，默沙東及生技醫療股逆市獲得資金承接。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-medium">3</td>
              <td class="px-4 py-3 font-medium">房地產 (Real Estate)</td>
              <td class="px-4 py-3 font-mono">XLRE</td>
              <td class="px-4 py-3 text-right font-mono text-emerald-500 font-semibold" data-val="1.10">+1.10%</td>
              <td class="px-4 py-3 text-right font-mono" data-val="0.80">+0.80%</td>
              <td class="px-4 py-3 text-right font-mono" data-val="-2.10">-2.10%</td>
              <td class="px-4 py-3 text-zinc-500">前期超跌重壓板塊，今日出現部分超跌空頭回補（Short covering）。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-medium">4</td>
              <td class="px-4 py-3 font-medium">公用事業 (Utilities)</td>
              <td class="px-4 py-3 font-mono">XLU</td>
              <td class="px-4 py-3 text-right font-mono text-emerald-500 font-semibold" data-val="0.86">+0.86%</td>
              <td class="px-4 py-3 text-right font-mono" data-val="0.20">+0.20%</td>
              <td class="px-4 py-3 text-right font-mono" data-val="0.10">+0.10%</td>
              <td class="px-4 py-3 text-zinc-500">防禦分紅資金湧入，電網等重電設施在避險市中維持綠盤。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-medium">5</td>
              <td class="px-4 py-3 font-medium">金融 (Financials)</td>
              <td class="px-4 py-3 font-mono">XLF</td>
              <td class="px-4 py-3 text-right font-mono text-emerald-500 font-semibold" data-val="0.21">+0.21%</td>
              <td class="px-4 py-3 text-right font-mono" data-val="1.80">+1.80%</td>
              <td class="px-4 py-3 text-right font-mono" data-val="3.10">+3.10%</td>
              <td class="px-4 py-3 text-zinc-500">收益率狂飆對銀行淨息差有一定支撐，銀行龍頭收平，板塊微綠。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-medium">6</td>
              <td class="px-4 py-3 font-medium">原材料 (Materials)</td>
              <td class="px-4 py-3 font-mono">XLB</td>
              <td class="px-4 py-3 text-right font-mono text-rose-500 font-semibold" data-val="-0.02">-0.02%</td>
              <td class="px-4 py-3 text-right font-mono" data-val="0.10">+0.10%</td>
              <td class="px-4 py-3 text-right font-mono" data-val="0.20">+0.20%</td>
              <td class="px-4 py-3 text-zinc-500">強美元壓制大宗商品，礦業巨頭微幅收跌。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-medium">7</td>
              <td class="px-4 py-3 font-medium">工業 (Industrials)</td>
              <td class="px-4 py-3 font-mono">XLI</td>
              <td class="px-4 py-3 text-right font-mono text-rose-500 font-semibold" data-val="-0.60">-0.60%</td>
              <td class="px-4 py-3 text-right font-mono" data-val="0.20">+0.20%</td>
              <td class="px-4 py-3 text-right font-mono" data-val="0.80">+0.80%</td>
              <td class="px-4 py-3 text-zinc-500">受益於重電與基建支撐跌幅較窄，但仍隨大盤承壓。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-medium">8</td>
              <td class="px-4 py-3 font-medium">非必需消費 (Consumer Discretionary)</td>
              <td class="px-4 py-3 font-mono">XLY</td>
              <td class="px-4 py-3 text-right font-mono text-rose-500 font-semibold" data-val="-1.00">-1.00%</td>
              <td class="px-4 py-3 text-right font-mono" data-val="-0.80">-0.80%</td>
              <td class="px-4 py-3 text-right font-mono" data-val="0.50">+0.50%</td>
              <td class="px-4 py-3 text-zinc-500">亞馬遜與特斯拉等大市值消費股遭遇高估值拋售，拖累板塊。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-medium">9</td>
              <td class="px-4 py-3 font-medium">能源 (Energy)</td>
              <td class="px-4 py-3 font-mono">XLE</td>
              <td class="px-4 py-3 text-right font-mono text-rose-500 font-semibold" data-val="-1.26">-1.26%</td>
              <td class="px-4 py-3 text-right font-mono" data-val="-0.30">-0.30%</td>
              <td class="px-4 py-3 text-right font-mono" data-val="3.10">+3.10%</td>
              <td class="px-4 py-3 text-zinc-500">以黎停火協議預期及美元飆升，打壓油價 Brent 跌至 $93 附近。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-medium">10</td>
              <td class="px-4 py-3 font-medium">資訊科技 (Technology)</td>
              <td class="px-4 py-3 font-mono">XLK</td>
              <td class="px-4 py-3 text-right font-mono text-rose-500 font-semibold" data-val="-1.60">-1.60%</td>
              <td class="px-4 py-3 text-right font-mono" data-val="-0.90">-0.90%</td>
              <td class="px-4 py-3 text-right font-mono" data-val="5.20">+5.20%</td>
              <td class="px-4 py-3 text-zinc-500">主要權重股微軟、蘋果、輝達悉數下跌，板塊高位整理回調。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-medium">11</td>
              <td class="px-4 py-3 font-medium">通信服務 (Communication Services)</td>
              <td class="px-4 py-3 font-mono">XLC</td>
              <td class="px-4 py-3 text-right font-mono text-rose-500 font-semibold" data-val="-2.65">-2.65%</td>
              <td class="px-4 py-3 text-right font-mono" data-val="-1.20">-1.20%</td>
              <td class="px-4 py-3 text-right font-mono" data-val="2.10">+2.10%</td>
              <td class="px-4 py-3 text-zinc-500">重災區之一。Meta 大跌 5.5% 拖累，資金大幅撤離高擁擠通信巨頭。</td>
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
          <h3 class="text-lg font-bold text-emerald-500 mt-1">經典防禦避險風格全面崛起</h3>
          <p class="text-sm text-zinc-500 mt-2 leading-relaxed">
            無風險利率狂飆促使資金出逃，流入極具防禦屬性的高股息、民生消費（XLP +2.1%）與醫療保健（XLV +1.5%）。這是一次非常乾脆的資金高防禦撤退。
          </p>
        </div>
        <div class="p-5 rounded-xl border border-zinc-200 dark:border-zinc-800 bg-white dark:bg-zinc-900">
          <span class="text-xs font-semibold text-zinc-400">最弱風格</span>
          <h3 class="text-lg font-bold text-rose-500 mt-1">AI 晶片去槓桿與高估值科技踩踏</h3>
          <p class="text-sm text-zinc-500 mt-2 leading-relaxed">
            費半指數大跌 10.26% 創下近年最慘案。半導體 ETF（SMH）跌破多條支撐。ARM 暴跌 12.8%，AMD 跌 10.9%，美光大跌 9.45%。在利率飆升時，高估值成長股迎來了集體殺估值的多頭踩踏。
          </p>
        </div>
        <div class="p-5 rounded-xl border border-zinc-200 dark:border-zinc-800 bg-white dark:bg-zinc-900">
          <span class="text-xs font-semibold text-zinc-400">輪動特徵</span>
          <h3 class="text-lg font-bold text-amber-500 mt-1">全面轉向 Risk-off 避險防守</h3>
          <p class="text-sm text-zinc-500 mt-2 leading-relaxed">
            前日的「小盤股補漲狂歡」今日全面熄火，羅素 2000 大跌 3.5% 表明投機資金全面退潮。等權標普 500 (RSP) 大跌 1.45%，跌幅雖小於標普權重指數（-2.60%），但表明這是一次市場寬度極速惡化的普跌市。
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
          <h4 class="font-bold text-zinc-800 dark:text-zinc-200 text-sm">6.1 均線參與度</h4>
          <p class="text-sm text-zinc-650 dark:text-zinc-400 mt-2 leading-relaxed font-mono">
            S&P 500 站上 50MA 比例從 64.2% 大幅滑落至 <strong>48.5%</strong>；Nasdaq 100 站上 50MA 比例跌至 <strong>41.2%</strong> (前值 59.5%)。短期內，多數科技成分股已破位並跌穿中短期均線支持。
          </p>
        </div>
        <div class="p-5 rounded-xl bg-zinc-50 dark:bg-zinc-900 border border-zinc-100 dark:border-zinc-800">
          <h4 class="font-bold text-zinc-800 dark:text-zinc-200 text-sm">6.2 漲跌家數與新高</h4>
          <p class="text-sm text-zinc-650 dark:text-zinc-400 mt-2 leading-relaxed">
            <strong>NYSE 交易所：</strong>漲跌比急墜至約 <strong>1:3.8</strong>，新高個股大幅收窄至 52 家，新低個股激增至 280 家。<br>
            <strong>Nasdaq 交易所：</strong>上漲 890 家，下跌 3,892 家（比例約為 <strong>1:4.4</strong>），新高 25 家，新低達 310 家，多頭情緒冰封。
          </p>
        </div>
        <div class="p-5 rounded-xl bg-zinc-50 dark:bg-zinc-900 border border-zinc-100 dark:border-zinc-800">
          <h4 class="font-bold text-zinc-800 dark:text-zinc-200 text-sm">6.3 其他內部指標</h4>
          <p class="text-sm text-zinc-650 dark:text-zinc-400 mt-2 leading-relaxed font-mono">
            <strong>Put/Call 比例：</strong>飆升至 <strong>0.92</strong> (前值 0.72)，顯示在科技股崩盤下，市場購買看跌期權對沖保護的意願急速上升。VIX 指數大漲 31% 衝上 21.51，暗示短線情緒出現恐慌跡象。
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
              <th class="px-4 py-3 text-left font-semibold text-zinc-650 dark:text-zinc-400">ETF代號</th>
              <th class="px-4 py-3 text-right font-semibold text-zinc-650 dark:text-zinc-400">最新收盤</th>
              <th class="px-4 py-3 text-right font-semibold text-zinc-650 dark:text-zinc-400">20 MA</th>
              <th class="px-4 py-3 text-right font-semibold text-zinc-650 dark:text-zinc-400">50 MA</th>
              <th class="px-4 py-3 text-right font-semibold text-zinc-650 dark:text-zinc-400">200 MA</th>
              <th class="px-4 py-3 text-center font-semibold text-zinc-650 dark:text-zinc-400">RSI (14)</th>
              <th class="px-4 py-3 text-left font-semibold text-zinc-650 dark:text-zinc-400">關鍵支撐 / 壓力</th>
              <th class="px-4 py-3 text-left font-semibold text-zinc-650 dark:text-zinc-400">技術趨勢判定</th>
            </tr>
          </thead>
          <tbody class="divide-y divide-zinc-200 dark:divide-zinc-800 font-mono text-zinc-700 dark:text-zinc-300">
            <tr>
              <td class="px-4 py-3 font-semibold font-sans text-zinc-900 dark:text-zinc-100">SPY (S&P 500)</td>
              <td class="px-4 py-3 text-right">$744.22</td>
              <td class="px-4 py-3 text-right">$749.50</td>
              <td class="px-4 py-3 text-right">$736.00</td>
              <td class="px-4 py-3 text-right">$689.00</td>
              <td class="px-4 py-3 text-center">46</td>
              <td class="px-4 py-3 font-sans text-xs text-left">$735 / $750</td>
              <td class="px-4 py-3 font-sans text-xs text-rose-500 font-semibold text-left">跌破 20MA，回踩 50MA 尋求支撐</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold font-sans text-zinc-900 dark:text-zinc-100">QQQ (Nasdaq 100)</td>
              <td class="px-4 py-3 text-right">$705.06</td>
              <td class="px-4 py-3 text-right">$738.50</td>
              <td class="px-4 py-3 text-right">$726.00</td>
              <td class="px-4 py-3 text-right">$683.00</td>
              <td class="px-4 py-3 text-center">38</td>
              <td class="px-4 py-3 font-sans text-xs text-left">$700 / $725</td>
              <td class="px-4 py-3 font-sans text-xs text-rose-500 font-semibold text-left">跌破20/50MA，短線技術性破位</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold font-sans text-zinc-900 dark:text-zinc-100">IWM (Russell 2000)</td>
              <td class="px-4 py-3 text-right">$288.26</td>
              <td class="px-4 py-3 text-right">$288.50</td>
              <td class="px-4 py-3 text-right">$286.00</td>
              <td class="px-4 py-3 text-right">$273.00</td>
              <td class="px-4 py-3 text-center">42</td>
              <td class="px-4 py-3 font-sans text-xs text-left">$280 / $290</td>
              <td class="px-4 py-3 font-sans text-xs text-rose-500 font-semibold text-left">抹平全部漲幅，重新陷入箱體整理</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold font-sans text-zinc-900 dark:text-zinc-100">SMH (Semiconductors)</td>
              <td class="px-4 py-3 text-right">$627.53</td>
              <td class="px-4 py-3 text-right">$695.00</td>
              <td class="px-4 py-3 text-right">$670.00</td>
              <td class="px-4 py-3 text-right">$598.00</td>
              <td class="px-4 py-3 text-center">32</td>
              <td class="px-4 py-3 font-sans text-xs text-left">$620 / $660</td>
              <td class="px-4 py-3 font-sans text-xs text-rose-500 font-semibold text-left">跌穿 50MA，RSI 逼近超賣</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold font-sans text-zinc-900 dark:text-zinc-100">IGV (Software)</td>
              <td class="px-4 py-3 text-right">$95.85</td>
              <td class="px-4 py-3 text-right">$100.20</td>
              <td class="px-4 py-3 text-right">$98.50</td>
              <td class="px-4 py-3 text-right">$92.00</td>
              <td class="px-4 py-3 text-center">39</td>
              <td class="px-4 py-3 font-sans text-xs text-left">$95 / $98</td>
              <td class="px-4 py-3 font-sans text-xs text-rose-500 font-semibold text-left">跌穿短期均線，呈現探底弱勢</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold font-sans text-zinc-900 dark:text-zinc-100">XLK (Technology)</td>
              <td class="px-4 py-3 text-right">$193.17</td>
              <td class="px-4 py-3 text-right">$194.20</td>
              <td class="px-4 py-3 text-right font-mono">$190.50</td>
              <td class="px-4 py-3 text-right">$177.00</td>
              <td class="px-4 py-3 text-center">45</td>
              <td class="px-4 py-3 font-sans text-xs text-left">$190 / $196</td>
              <td class="px-4 py-3 font-sans text-xs text-rose-500 font-semibold text-left">回踩 50MA (190) 平台尋求支撐</td>
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
          <p><strong>NVDA (Nvidia) -3.03% ($212.04)：</strong>晶片龍頭未能擺脫大盤的系統性拋盤，盤中一度大跌 5.9% 至 $205.84。尾盤有買盤介入，收於 $212.04。短期高位面臨獲利盤與高折現率的雙重打壓。</p>
          <p><strong>GOOGL (Alphabet) -1.31% ($367.32)：</strong>在巨頭中相對抗跌，回踩 $365 平台。前幾日上漲釋放了部分需求，中線多頭格局目前正在磨平。</p>
          <p><strong>AAPL (Apple) -1.20% ($313.86)：</strong>下週將迎來 WWDC 2026 大會，買盤防禦性進駐限制了跌幅。在七巨頭中表現出最佳的抗震性。</p>
          <p><strong>MSFT (Microsoft) -1.31% ($422.43)：</strong>跌破 5MA 短期均線，隨大盤受壓回調。中線上升通道依然保持。</p>
          <p><strong>AMZN (Amazon) -3.10% ($252.78)：</strong>跌幅較大，市場擔心聯準會維持「更高、更久」的基準利率會壓制下半年的消費與雲支出，股價重回 $250 支撐。</p>
          <p><strong>META (Meta Platforms) -5.50% ($593.00)：</strong>暴跌 5.5%，直接砸穿 20MA 和 50MA 支撐。受累於 AI 資本開支預期重壓，引發高位調倉拋售。</p>
          <p><strong>TSLA (Tesla) -6.60% ($391.00)：</strong>跌幅居前，失守 $400 整數關口。除了高利率對其電車銷售和估值壓制外，公司的比特幣持倉在今天比特幣大跌時引發的潛在減值也打擊了買家情緒。</p>
        </div>
      </details>

      <!-- 8.2 半導體 -->
      <details class="mb-4 p-4 rounded-xl border border-zinc-200 dark:border-zinc-800 bg-zinc-50/50 dark:bg-zinc-900/50">
        <summary class="font-bold text-zinc-800 dark:text-zinc-200 text-base">8.2 AI 硬體 / 半導體重點股異動分析</summary>
        <div class="mt-4 space-y-3 text-sm text-zinc-650 dark:text-zinc-400">
          <p><strong>AVGO (Broadcom) -3.86% ($402.75)：</strong>延續了昨日財報發布後 12.59% 的暴跌。AI 晶片全年營收維持不變的指引讓高預期的市場大失所望，面臨估值重修，兩日累計下瀉超 16%。</p>
          <p><strong>AMD (Advanced Micro Devices) -10.90% ($465.60)：</strong>半導體大跌重災區。作為估值偏高、擁擠度較高的次龍頭，遭遇算法拋售踩踏，暴跌 10.90%，失守多條均線。</p>
          <p><strong>ARM (ARM Holdings) -12.80% ($142.30)：</strong>本日晶片板塊跌幅最慘。受到大盤去擁擠和高估值修正的踩踏，且市場傳出大股東計畫部分減持的傳言，暴跌 12.80%，兩日累計跌去約 20%。</p>
          <p><strong>MU (Micron Technology) -9.45% ($970.60)：</strong>美光股價跌破 $1000 整數大關，報收 $970.60。在降息預期落空、美債收益率飆升的背景下，面臨猛烈回調。</p>
          <p><strong>TSM (TSMC ADR) -6.60% ($415.00)：</strong>遭遇系統性拋盤衝擊，大跌 6.60%，回吐了前幾日的所有漲幅，回踩 $410-$415 支撐區。</p>
        </div>
      </details>

      <!-- 8.3 軟體 -->
      <details class="mb-4 p-4 rounded-xl border border-zinc-200 dark:border-zinc-800 bg-zinc-50/50 dark:bg-zinc-900/50">
        <summary class="font-bold text-zinc-800 dark:text-zinc-200 text-base">8.3 軟體 / SaaS / AI 應用重點股異動分析</summary>
        <div class="mt-4 space-y-3 text-sm text-zinc-650 dark:text-zinc-400">
          <p><strong>ORCL (Oracle) -9.70% ($213.41)：</strong>軟件巨頭甲骨文暴跌 9.70%，主要受高利率重壓與市場對下半年雲伺服器訂單釋放放緩的擔憂影響。</p>
          <p><strong>CRM (Salesforce) -1.10% ($186.67)：</strong>跌幅受限，由於前期已出現過大跌，估值壓力提前釋放，在 $185 附近磨底。</p>
          <p><strong>PLTR (Palantir) -4.40% ($135.53)：</strong>跟隨科技板塊回撤，跌穿 20MA，回踩短期支撐平台。</p>
        </div>
      </details>

      <!-- 8.4 AI 電力 -->
      <details class="mb-4 p-4 rounded-xl border border-zinc-200 dark:border-zinc-850 bg-zinc-50/50 dark:bg-zinc-900/50">
        <summary class="font-bold text-zinc-800 dark:text-zinc-200 text-base">8.4 AI 電力 / 資料中心 / 能源基礎設施重點股分析</summary>
        <div class="mt-4 space-y-3 text-sm text-zinc-650 dark:text-zinc-400">
          <p><strong>VST (Vistra Corp.) -1.56% ($151.30)：</strong>電力需求基本面強勁，雖然跟隨科技板塊回撤，但跌幅極小，展現出良好的抗跌韌性。</p>
          <p><strong>CEG (Constellation Energy) -1.46% ($263.35)：</strong>核能發電龍頭小幅回調 1.46%，明顯強於普通科技板塊，中線核能供電邏輯不變。</p>
          <p><strong>OKLO (Oklo Inc.) -5.95% ($61.50)：</strong>小核能概念股波動巨大，大跌 5.95%，重回 20MA 附近，高位套現壓力仍然存在。</p>
        </div>
      </details>
    </section>

    <!-- 9. 財報日曆與財報解讀 -->
    <section id="earnings" class="mb-12 scroll-mt-6">
      <h2 class="text-2xl font-bold mb-4 flex items-center gap-2 border-b border-zinc-100 dark:border-zinc-800 pb-2">
        <span class="text-brand-500">9.</span> 財報日曆與財報解讀
      </h2>

      <div class="space-y-4">
        <!-- Broadcom -->
        <div class="p-5 rounded-xl border border-zinc-200 dark:border-zinc-800 bg-zinc-50/40 dark:bg-zinc-900/40">
          <div class="flex items-center justify-between mb-2">
            <h4 class="font-bold text-zinc-800 dark:text-zinc-200 text-base">Broadcom (AVGO) 財報消化反應</h4>
            <span class="px-2 py-0.5 rounded bg-rose-100 dark:bg-rose-950 text-rose-800 dark:text-rose-350 text-xs font-semibold">兩日下挫 >16%</span>
          </div>
          <div class="text-sm text-zinc-600 dark:text-zinc-400 space-y-2 leading-relaxed">
            <p><strong>營收表現：</strong>第二季度財報業績良好，但管理層在電話會議中並未上調全年 110 億美元的 AI 晶片營收預期。這與市場「激進的樂觀預估」產生衝突。</p>
            <p><strong>估值修正：</strong>被視為是典型的「Sell the News」行為。多頭踩踏與利率攀升形成合力，拖累半導體板塊走弱。</p>
          </div>
        </div>

        <!-- Lululemon -->
        <div class="p-5 rounded-xl border border-zinc-200 dark:border-zinc-800 bg-zinc-50/40 dark:bg-zinc-900/40">
          <div class="flex items-center justify-between mb-2">
            <h4 class="font-bold text-zinc-800 dark:text-zinc-200 text-base">Lululemon (LULU) 常規交易大跌</h4>
            <span class="px-2 py-0.5 rounded bg-rose-100 dark:bg-rose-950 text-rose-800 dark:text-rose-350 text-xs font-semibold">常規大跌 11.5%</span>
          </div>
          <div class="text-sm text-zinc-600 dark:text-zinc-400 space-y-2 leading-relaxed">
            <p><strong>下修指引：</strong>公司下修 Q2 及全年業績指引，指出北美市場消費者需求放緩，高估值下市場容錯率極低。股價大跌 11.5% 收於低位，引發對可選消費板塊的集體擔憂。</p>
          </div>
        </div>
      </div>
    </section>

    <!-- 10. 機構觀點與資金流 -->
    <section id="institution" class="mb-12 scroll-mt-6">
      <h2 class="text-2xl font-bold mb-4 flex items-center gap-2 border-b border-zinc-100 dark:border-zinc-800 pb-2">
        <span class="text-brand-500">10.</span> 機構觀點與資金流
      </h2>
      <div class="p-5 bg-zinc-50 dark:bg-zinc-900 rounded-xl border border-zinc-200 dark:border-zinc-800 text-sm space-y-4">
        <div>
          <h4 class="font-bold text-zinc-800 dark:text-zinc-200 flex items-center gap-2">
            <span class="w-1.5 h-1.5 rounded-full bg-brand-500"></span> 摩根大通宏觀策略團隊：
          </h4>
          <p class="text-zinc-600 dark:text-zinc-400 mt-1 pl-3.5 leading-relaxed">
            「5月份強勁的就業數據直接掐斷了近期的降息幻覺。我們目前正處於『Higher for longer』利率的重訂價過程中。對於前期極其擁擠且溢價偏高的 AI 晶片板塊，無風險利率上行將觸發嚴重的分母端估值重估。」
          </p>
        </div>
        <div>
          <h4 class="font-bold text-zinc-800 dark:text-zinc-200 flex items-center gap-2">
            <span class="w-1.5 h-1.5 rounded-full bg-brand-500"></span> 高盛交易台：
          </h4>
          <p class="text-zinc-600 dark:text-zinc-400 mt-1 pl-3.5 leading-relaxed">
            「這是一次強烈的『去槓桿、去擁擠』的去風險操作。半導體指數（SOX）出現了極致的拋壓，但防禦性消費品（XLP）與醫療（XLV）獲得了顯著的長線避險資金流入。這表明資金只是在防守而非全面退場。」
          </p>
        </div>
      </div>
    </section>

    <!-- 11. 板塊輪動判斷 -->
    <section id="rotation" class="mb-12 scroll-mt-6">
      <h2 class="text-2xl font-bold mb-4 flex items-center gap-2 border-b border-zinc-100 dark:border-zinc-800 pb-2">
        <span class="text-brand-500">11.</span> 板塊輪動判斷
      </h2>
      <p class="text-sm sm:text-base text-zinc-600 dark:text-zinc-450 leading-relaxed">
        當前市場正處於<strong>「避險防禦、科技重創」</strong>的劇烈板塊輪動中。就業市場的大熱重擊降息預期，促使美債 10 年期收益率升至 4.55% 以上。高估值的半導體（SOXX）與成長股面臨多頭撤離去槓桿。這股資金流向了民生消費（XLP）、醫療保健（XLV）等具備抗通膨、避險屬性的高息/防禦板塊。在下週 CPI 與利率決議落地前，市場預計將保持以防守為主的 Risk-off 整理狀態，科技板塊仍需縮量尋底。
      </p>
    </section>

    <!-- 12. 我的重點關注股觀察 -->
    <section id="watchlist" class="mb-12 scroll-mt-6">
      <h2 class="text-2xl font-bold mb-4 flex items-center gap-2 border-b border-zinc-100 dark:border-zinc-800 pb-2">
        <span class="text-brand-500">12.</span> 重點關注股觀察
      </h2>
      <div class="overflow-x-auto border border-zinc-200 dark:border-zinc-800 rounded-xl">
        <table class="min-w-full divide-y divide-zinc-200 dark:divide-zinc-800 text-sm">
          <thead class="bg-zinc-50 dark:bg-zinc-900">
            <tr class="text-zinc-550 dark:text-zinc-400 text-left">
              <th class="px-4 py-3 font-semibold">個股代號</th>
              <th class="px-4 py-3 font-semibold text-right">當日漲跌</th>
              <th class="px-4 py-3 font-semibold">趨勢狀態</th>
              <th class="px-4 py-3 font-semibold">決策標籤</th>
              <th class="px-4 py-3">關鍵動態 / 支撐壓力</th>
            </tr>
          </thead>
          <tbody class="divide-y divide-zinc-200 dark:divide-zinc-850 font-mono text-zinc-700 dark:text-zinc-300">
            <tr>
              <td class="px-4 py-3 font-semibold font-sans text-zinc-900 dark:text-zinc-100">NVDA</td>
              <td class="px-4 py-3 text-right text-rose-500 font-semibold">-3.03%</td>
              <td class="px-4 py-3 font-sans">跌破 5MA 短期均線</td>
              <td class="px-4 py-3 font-sans">
                <span class="px-2 py-0.5 rounded bg-amber-100 dark:bg-amber-950 text-amber-800 dark:text-amber-350 text-xs font-semibold">高位震盪</span>
              </td>
              <td class="px-4 py-3 font-sans text-xs">跟隨晶片股下挫，盤中一度大跌 5.9% 報 $205.84，尾盤收回，支撐 $210。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold font-sans text-zinc-900 dark:text-zinc-100">AMD</td>
              <td class="px-4 py-3 text-right text-rose-500 font-semibold">-10.90%</td>
              <td class="px-4 py-3 font-sans">跌破 20MA 及 50MA</td>
              <td class="px-4 py-3 font-sans">
                <span class="px-2 py-0.5 rounded bg-rose-100 dark:bg-rose-950 text-rose-800 dark:text-rose-350 text-xs font-semibold">破位風險</span>
              </td>
              <td class="px-4 py-3 font-sans text-xs">大跌 10.9% 跌破 $500 大關，技術指標走壞，回防 $460。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold font-sans text-zinc-900 dark:text-zinc-100">AVGO</td>
              <td class="px-4 py-3 text-right text-rose-500 font-semibold">-3.86%</td>
              <td class="px-4 py-3 font-sans">跌破 50MA 支撐</td>
              <td class="px-4 py-3 font-sans">
                <span class="px-2 py-0.5 rounded bg-rose-100 dark:bg-rose-950 text-rose-800 dark:text-rose-350 text-xs font-semibold">破位風險</span>
              </td>
              <td class="px-4 py-3 font-sans text-xs">連續兩天放量拋售，累跌逾 16%，短線考驗 $400 整數支撐。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold font-sans text-zinc-900 dark:text-zinc-100">GOOGL</td>
              <td class="px-4 py-3 text-right text-rose-500 font-semibold">-1.31%</td>
              <td class="px-4 py-3 font-sans">20MA 平台盤整</td>
              <td class="px-4 py-3 font-sans">
                <span class="px-2 py-0.5 rounded bg-zinc-100 dark:bg-zinc-800 text-zinc-800 dark:text-zinc-300 text-xs font-semibold">需要觀察</span>
              </td>
              <td class="px-4 py-3 font-sans text-xs">相對抗跌，回踩 $365 平台。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold font-sans text-zinc-900 dark:text-zinc-100">META</td>
              <td class="px-4 py-3 text-right text-rose-500 font-semibold">-5.50%</td>
              <td class="px-4 py-3 font-sans">跌穿 20MA 及 50MA</td>
              <td class="px-4 py-3 font-sans">
                <span class="px-2 py-0.5 rounded bg-rose-100 dark:bg-rose-950 text-rose-800 dark:text-rose-350 text-xs font-semibold">破位風險</span>
              </td>
              <td class="px-4 py-3 font-sans text-xs">大跌 5.5%，受累於 AI 資本開支預期拖累，下看 $580。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold font-sans text-zinc-900 dark:text-zinc-100">VST</td>
              <td class="px-4 py-3 text-right text-rose-500 font-semibold">-1.56%</td>
              <td class="px-4 py-3 font-sans">20MA 平台防守</td>
              <td class="px-4 py-3 font-sans">
                <span class="px-2 py-0.5 rounded bg-amber-100 dark:bg-amber-950 text-amber-800 dark:text-amber-350 text-xs font-semibold">高位震盪</span>
              </td>
              <td class="px-4 py-3 font-sans text-xs">防禦性強，大電力需求邏輯不變，守在 $150 上方。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold font-sans text-zinc-900 dark:text-zinc-100">CEG</td>
              <td class="px-4 py-3 text-right text-rose-500 font-semibold">-1.46%</td>
              <td class="px-4 py-3 font-sans">20MA 平台防守</td>
              <td class="px-4 py-3 font-sans">
                <span class="px-2 py-0.5 rounded bg-amber-100 dark:bg-amber-950 text-amber-800 dark:text-amber-350 text-xs font-semibold">高位震盪</span>
              </td>
              <td class="px-4 py-3 font-sans text-xs">核能發電受大盤拖累微調，守穩 $260 主要支撐。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold font-sans text-zinc-900 dark:text-zinc-100">ETN</td>
              <td class="px-4 py-3 text-right text-rose-500 font-semibold">-0.80%</td>
              <td class="px-4 py-3 font-sans">5MA 平台抗震</td>
              <td class="px-4 py-3 font-sans">
                <span class="px-2 py-0.5 rounded bg-emerald-100 dark:bg-emerald-950 text-emerald-800 dark:text-emerald-350 text-xs font-semibold">繼續強勢</span>
              </td>
              <td class="px-4 py-3 font-sans text-xs">重電龍頭極其抗跌，資金流入防禦工業基建，支撐 $415。</td>
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
      <div class="space-y-4 text-sm sm:text-base leading-relaxed text-zinc-660 dark:text-zinc-400">
        <p><strong>13.1 宏觀觀察：</strong>關注債市收益率是否會持續在 4.55% 以上攀升。若 10年期美債衝上 4.60% 關口，高估值科技股將面臨二次估值修正。美元指數在 101.00 處的阻力以及黃金期貨的止跌反彈是觀測資金逃離深度的關鍵指標。</p>
        <p><strong>13.2 大盤觀察：</strong>標普 500 的 50MA 平台位於 7,360 點，此處不可失守，否則大盤將徹底轉入中線修正。納指 100 急需收復 29,200 點以上以穩定多頭信心。若 VIX 持續高於 20，大盤調整時間將會被拉長。</p>
        <p><strong>13.3 個股關注：</strong>
          <ul class="list-disc pl-5 space-y-1">
            <li><strong>AMD / ARM：</strong>本日暴跌超 10%，關注週一開盤後是否有短線超賣的博反彈機會。</li>
            <li><strong>XLP / XLV：</strong>防禦板塊若能維持強勢，可小量配置作為防禦大盤的護盾。</li>
            <li><strong>NVDA：</strong>關注是否能在 $210 企穩，作爲整個 AI 半導體主線的信心風向標。</li>
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
        <table class="min-w-full divide-y divide-zinc-200 dark:divide-zinc-800 text-sm">
          <thead class="bg-zinc-50 dark:bg-zinc-900">
            <tr class="text-zinc-550 dark:text-zinc-400 text-left">
              <th class="px-4 py-3 font-semibold">風險維度</th>
              <th class="px-4 py-3 font-semibold text-center">評級</th>
              <th class="px-4 py-3">具體解讀</th>
            </tr>
          </thead>
          <tbody class="divide-y divide-zinc-200 dark:divide-zinc-850 text-zinc-700 dark:text-zinc-300">
            <tr>
              <td class="px-4 py-3 font-semibold">高利率與通膨風險</td>
              <td class="px-4 py-3 text-center">
                <span class="px-2 py-0.5 rounded bg-red-100 dark:bg-red-950 text-red-800 dark:text-red-350 text-xs font-semibold">高 (High)</span>
              </td>
              <td class="px-4 py-3 text-xs sm:text-sm">非農大熱重擊降息路徑。美聯儲長期維持高利率將大幅抬升資金成本，重創科技成長股估值。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold">AI板塊去擁擠去槓桿</td>
              <td class="px-4 py-3 text-center">
                <span class="px-2 py-0.5 rounded bg-red-100 dark:bg-red-950 text-red-800 dark:text-red-350 text-xs font-semibold">高 (High)</span>
              </td>
              <td class="px-4 py-3 text-xs sm:text-sm">費半與 SMH 一日大跌 10%，顯示出 AI 晶片前期擁擠度極高，短線槓桿盤出逃與技術性踩踏風險尚未出清。</td>
            </tr>
            <tr>
              <td class="px-4 py-3 font-semibold">流動性與波動率風險</td>
              <td class="px-4 py-3 text-center">
                <span class="px-2 py-0.5 rounded bg-amber-100 dark:bg-amber-950 text-amber-800 dark:text-amber-350 text-xs font-semibold">中高 (Medium-High)</span>
              </td>
              <td class="px-4 py-3 text-xs sm:text-sm">VIX 飆升至 21.51。波動率的快速攀升通常伴隨槓桿清算，短期將放大日內震盪。</td>
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
      <div class="space-y-4 text-sm sm:text-base leading-relaxed text-zinc-655 dark:text-zinc-400">
        <p><strong>今日市場結論：</strong>強勁就業數據引發的宏觀利率巨震重創了市場。在無風險利率飆升至 4.55% 的背景下，此前過度擁擠的 AI 半導體板塊經歷了劇烈的去槓桿與估值修正，引導大盤出現高位技術性破位。避險板塊逆市走高說明資金並未徹底流出股市，而是縮回掩體防守。</p>
        <p><strong>當前市場階段：</strong><span class="px-2 py-0.5 rounded bg-rose-100 dark:bg-rose-950 text-rose-800 dark:text-rose-350 font-bold text-xs sm:text-sm">中期高位調整與強烈的 Risk-off 避險調倉</span></p>
        <p><strong>我的操作傾向：</strong>防守第一，嚴控倉位。短線內暫停加倉任何半導體與高估值科技股，多看少動；可適度將部分資金轉入消費必需品 (XLP) 或醫療 (XLV) 等防守型價值板塊，静待下週 CPI 數據與聯準會利率會議的靴子落地。</p>
        <p><strong>最值得關注的 5 個訊號：</strong>
          <ol class="list-decimal pl-5 space-y-1">
            <li>美債 10 年期收益率是否會站穩 4.55% 並向 4.60% 衝刺。</li>
            <li>費城半導體指數（SOX）在 12,000 點處的買盤承接力。</li>
            <li>比特幣能否迅速收復 $60,000 大關以穩定投機資金情緒。</li>
            <li>避險板塊 XLP 與 XLV 的資金流入持續性。</li>
            <li>下週三公佈的 5 月美國 CPI 數據與週四聯準會主席講話。</li>
          </ol>
        </p>
      </div>
    </section>

    <!-- Footer -->
    <footer class="mt-16 pt-8 border-t border-zinc-200 dark:border-zinc-800 text-xs sm:text-sm text-zinc-500 flex flex-col sm:flex-row justify-between gap-4">
      <div>Generated by the <a href="https://github.com" class="underline hover:text-zinc-950 dark:hover:text-zinc-100"><code>html-report</code></a> Antigravity CLI skill.</div>
      <div class="no-print">報告版本：v1.34 | 數據更新自紐約收盤時間 16:00</div>
    </footer>

  </main>
</div>

<script>
  // Theme toggle
  document.getElementById('theme-toggle').addEventListener('click', () => {
    const dark = document.documentElement.classList.toggle('dark');
    localStorage.theme = dark ? 'dark' : 'light';
    
    // Re-render chart for dark/light grids
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
      let activeIdx = 0;
      sections.forEach((sec, idx) => {
        if (sec.offsetTop <= y) activeIdx = idx;
      });
      tocLinks.forEach((a, idx) => a.classList.toggle('active', idx === activeIdx));
    };
    window.addEventListener('scroll', onScroll, { passive: true });
    onScroll();
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
        data: [-1.30, -2.60, -4.20, -4.80, -3.50, -10.26, 31.24],
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

    // Update markers in table headers
    const headers = table.querySelectorAll('thead th');
    headers.forEach((h, idx) => {
      if (idx < 6) {
        let baseText = h.innerText.replace(/[▲▼]/g, '').trim();
        if (idx === colIdx) {
          h.innerText = baseText + ' ' + (currentSortAsc ? '▲' : '▼');
        } else {
          h.innerText = baseText + ' ▲▼';
        }
      }
    });

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

# Save this HTML to reports/2026-06-05-us-stock-closing-daily-report.html inside /Users/wisdom/html-report-skill
target_dir = "/Users/wisdom/html-report-skill/reports"
os.makedirs(target_dir, exist_ok=True)
target_path = os.path.join(target_dir, "2026-06-05-us-stock-closing-daily-report.html")

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
exists = any(item.get("file") == "2026-06-05-us-stock-closing-daily-report.html" for item in manifest)
if not exists:
    new_entry = {
      "file": "2026-06-05-us-stock-closing-daily-report.html",
      "title": "美股收盤日報｜2026-06-05",
      "date": "2026-06-05",
      "description": "5月非農新增就業17.2萬爆冷大超預期，引爆降息預期重估！美債收益率狂飆至4.55%，科技與半導體遭血洗，納指跌4.2%、費半大跌10.26%，標普跌2.6%，創2025年10月以來最慘單日表現。"
    }
    manifest.insert(0, new_entry)
    with open(manifest_path, "w", encoding="utf-8") as f:
        json.dump(manifest, f, ensure_ascii=False, indent=2)
    print(f"Updated manifest.json successfully at: {manifest_path}")
else:
    print("manifest.json already contains the entry for 2026-06-05.")
