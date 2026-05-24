# agy-html-report-skill

一個適用於 Antigravity CLI (agy cli) 的 Skill，能讓 Agent 生成**豐富且具互動性的 HTML 報告**而非 Markdown，並發布到您專屬的 GitHub Pages 網站，以便您可以分享公開的 URL 連結。

> **本專案是一個 GitHub 範本。** 點擊頁面頂部的 ▸ **Use this template** 來建立您自己的副本。在這種情況下，選擇 Fork 是不合適的（Fork 適用於向上游提交 PR；而範本則適用於「複製並獨立分流」，這正是報告所需要的）。

---

## 為什麼？

Antigravity CLI (agy) 預設會為所有輸出使用 Markdown。Markdown 處理純文字很好，但當您的輸出包含數據、對比、程式碼或讀者想要點選尋找的詳細資訊時，您會需要 HTML：

- 互動式**圖表** (Chart.js / Plotly)
- **支援排序 / 搜尋 / 篩選的表格**
- 便於比對多個選項且無需滾動頁面的**分頁標籤 (Tabs)**
- 提供選擇性閱讀深度的**摺疊收合**區域 (Collapsible sections)
- 帶有複製按鈕且高亮顯示的**程式碼塊**
- **Mermaid** 流程圖、**KaTeX** 數學公式
- **深色模式**、**列印樣式表**、**行動裝置響應式佈局**、**OG 連結預覽**

這個 Skill 會引導 Agent 善用上述所有 HTML 優勢，並為您提供一鍵式的發布流程。

請參閱 [即時範例報告](./reports/2026-05-10-example-showcase.html) 以了解實際效果。

---

## 設定 (只需一次，約 3 分鐘)

### 1. 從此範本建立您的儲存庫

點擊本頁面頂部的 ▸ **Use this template → Create a new repository**。自行為儲存庫命名（例如 `reports`）。

### 2. 複製至本地端

```bash
git clone git@github.com:<your-username>/<your-repo>.git ~/reports
cd ~/reports
```

### 3. 將 Skill 安裝至 Antigravity CLI (agy cli)

在本地將 Skill 目錄軟連結（symlink）至 Antigravity 的全域 skills 資料夾中。使用軟連結意味著未來該 Skill 的任何更新（您自己修改或上游更新）都會自動生效。

```bash
mkdir -p ~/.antigravitycli/skills
ln -s "$(pwd)/.antigravitycli/skills/html-report" ~/.antigravitycli/skills/html-report
```

> 不想建立軟連結？也可以直接將資料夾複製過去：`cp -r .antigravitycli/skills/html-report ~/.antigravitycli/skills/`。當 Skill 有變更時再重新複製即可。

### 4. 啟用您新儲存庫的 GitHub Pages

前往 GitHub → 您的儲存庫 → **Settings → Pages** → **Source: Deploy from a branch** → **Branch: `main` / `(root)`** → 按下 Save。首次部署請稍候約 1 分鐘。

### 5. （選填）編輯 `config.json`

通常您**不需要修改任何設定**，發布腳本會自動偵測：
- 本地儲存庫路徑（從腳本在硬碟上的實際位置自動判定，亦支援軟連結）
- GitHub Pages 的網址（從 `git remote origin` 中自動讀取）

只有在以下情況下，才需要編輯 [`.antigravitycli/skills/html-report/config.json`](.antigravitycli/skills/html-report/config.json)：
- 您將儲存庫複製到自動偵測找不到的特殊路徑
- 您想使用自訂網域（請設定 `base_url`）

這就是所有的設定步驟！

---

## 開始使用

在 Antigravity CLI 中，要求 Agent 生成任何報告並提及此 Skill：

```
use the html-report skill to write up the results from runs/exp-42
```

```
make an html-report comparing these three checkpoints
```

```
/html-report   # 如果您的 Agent 支援將其作為斜線指令 (slash command) 觸發
```

Agent 將會：
1. 規劃報告（決定哪些區塊適合使用圖表、表格、分頁標籤或摺疊面板）。
2. 使用 [`templates/base.html`](.antigravitycli/skills/html-report/templates/base.html) 作為起點，在 `reports/<YYYY-MM-DD>-<slug>.html` 產生一個獨立的 HTML 檔案。
3. 執行 [`scripts/publish.py`](.antigravitycli/skills/html-report/scripts/publish.py)，以更新清單檔案（manifest）、自動提交 Git Commit、推送（Push）並輸出網址。
4. 將產生的公開 URL（例如 `https://<you>.github.io/<repo>/reports/2026-05-10-my-report.html`）返回給您。

位於 `https://<you>.github.io/<repo>/` 的首頁會列出所有已生成的報告（並提供篩選輸入框）。

---

## 系統需求

- `git`, `python3` (≥ 3.8), `bash`
- 擁有推送權限的 GitHub 帳號（已設定 SSH 金鑰或憑證協助程式）

不需要安裝 `jq`，不需要 `node`，也沒有繁瑣的打包編譯步驟（Build step）。發布腳本使用純 Python 標準函式庫編寫。

---

## 架構原理

```
your-repo/
├── index.html                ← 首頁；讀取 reports/manifest.json
├── reports/
│   ├── manifest.json         ← 包含 {file, title, date, description} 的報告清單
│   └── *.html                ← 每次生成且獨立的 HTML 報告檔案
└── .antigravitycli/
    └── skills/
        └── html-report/      ← 軟連結目標
            ├── SKILL.md      ← Agent 讀取並遵循的行為指南
            ├── config.json   ← 選填的路徑與 base_url 覆寫設定
            ├── templates/
            │   └── base.html ← 起始範本，Agent 會複製並豐富其內容
            └── scripts/
                └── publish.py
```

此 Skill 直接存放在**報告生成的同一個儲存庫中**。這是刻意設計的：
- 您只需要管理單個 Git 儲存庫。
- Skill 原始碼與發布範例一同隨附，讓您在套用範本之前能看清所有細節。
- 如果您在 Antigravity CLI 中直接打開此儲存庫，該 Skill 就會自動載入為專案專屬 Skill（此時無需建立軟連結）。

---

## 自訂外觀

- 編輯 [`templates/base.html`](.antigravitycli/skills/html-report/templates/base.html) 以變更預設字型、色彩、載入的函式庫或版面佈局。Agent 會將此檔案複製為每份新報告的起點。
- 編輯 [`index.html`](index.html) 來重新設計報告列表首頁的樣式。
- 編輯 [`SKILL.md`](.antigravitycli/skills/html-report/SKILL.md) 以調整 Agent 的行為模式（例如更偏好哪些圖表庫、高標品質定義等）。Skill 指南是最強大的微調槓桿——請根據您的喜好進行客製化。

---

## 拉取上游更新

如果您希望跟隨本專案後續的優化更新：

```bash
git remote add upstream https://github.com/wisdom925/html-report-skill.git
git fetch upstream
# 僅更新 Skill 相關檔案，保留您自己寫好的 reports/ 報告目錄
git checkout upstream/main -- .antigravitycli/ index.html
```

---

## 為什麼是範本（Template）而不是 Fork？

| | Fork | Template (範本) |
|---|---|---|
| 預設追蹤上游變更 | 是 | 否 |
| 設計用於向源專案提交 PR | 是 | 否 |
| 提交歷史（Commit History）完全獨立 | 共享 | 獨立屬於您 |
| 適合「複製並獨立分流」 | 否 | **是** |

您將會在這個儲存庫中寫滿**您自己的報告**。您肯定不希望 GitHub 介面上一直顯示「此分支領先/落後上游 xx 個 Commit」的提示。因此，GitHub Template（範本）是此場景下最合適的原始模型。

---

## 草稿模式 (Draft mode)

如果您對 Agent 說 *"先寫草稿就好，暫時不要 Push"*，Agent 在執行發布腳本時會自動帶入 `--draft` 參數。此時僅會更新本地端的清單檔案（manifest），而不會進行 Git Commit 或 Push。您將會直接拿回本地檔案的絕對路徑而非網址。

---

## 常見問題排除

- **`ERROR: ... is not a git repository`**：表示您的 `local_repo_path`（或自動偵測到的路徑）不指向一個有效的 Git 儲存庫。請將專案 clone 到該路徑，或者在 `config.json` 中顯式設定 `local_repo_path`。
- **`git push` 失敗**：請檢查您的 SSH/HTTPS 連線與 GitHub 權限。報告檔案此時已儲存在本地的 Commit 中，待網路或權限排除後手動執行 `git push` 即可。
- **Pages 網址顯示 404**：GitHub Pages 啟用後需要大約 1 分鐘的時間進行首度部署。請稍候並重新整理網頁。
- **Mermaid 或 KaTeX 無法正常載入**：它們是透過 CDN (jsdelivr) 載入，請開啟瀏覽器的開發者工具主控台（Console）檢查是否有 CSP 安全政策攔截或網路問題。

---

## 授權條款

MIT。詳見 [LICENSE](LICENSE)。
