# 任務進度檔：建立「寫部落格文章」skill

- 本檔位置：`C:\myself\ar2two-blog\docs\2026-10-04-blog-article-skill-progress.md`
- 開始日期：2026-10-04
- 起因：Ken 在寫完「美麗島 住宿」文章後，要求把所有 SEO 工具、skill、tool、plugin 中可以用來做文章的，整理成一份寫文章的 skill，往後任何部落格文章都照它做。

## 📌 目前狀態摘要

- 整體進度燈號：🟢 順利推進（已安裝到全域，剩 ai_visibility 結果與 commit）
- 關鍵決定／目前採用方式：
  - 架構：一個**全域通用** skill ＋ 每個部落格專案一份**網站設定檔**（Ken 2026-10-04 同意）。
  - skill 正式版在全域 `C:\Users\w1lin\.claude\skills\blog-article\`，備份在 `C:\myself\claude-global-config\skills\blog-article\`；部落格專案只留網站設定檔。
- 剩餘待辦：
  1. 補上 `ai_visibility` 這次實測的結果（2026-10-04 背景執行中），改 skill 要 Ken 的 `[允許改檔]`。
  2. commit：部落格專案、claude-global-config 各一次（需要 Ken 新訊息帶 `[allow-pii]`）。

---

## 📝 任務分析與執行計畫

### 1. 預期成果 (Outcome)

- [ ] 最終狀態描述：在任何部落格專案開對話，Claude 都看得到「寫部落格文章」skill，照 0～10 步驟寫文章；每個專案的網站資料寫在自己的網站設定檔。
- [ ] 完成定義 (DoD)：
  - 全域 skill 已安裝、已備份。
  - 阿爾兔兔部落格的網站設定檔已建立。
  - skill 裡列的工具都實測過（✅ 或 ⚠ 寫清楚限制），沒實測的明確標出。
  - Ken 看過 HTML 說明書並同意。

### 2. 邊界與禁區 (Constraints)

- 允許修改範圍：
  - `C:\myself\ar2two-blog\docs\` 底下新增的草稿、進度檔、網站設定檔。
  - 確認後新增 `C:\Users\w1lin\.claude\skills\blog-article\`，以及 `C:\myself\claude-global-config\` 的備份。
- **禁止修改範圍**：
  - SEO 工具包的程式（`C:\myself\seo-toolkit\`）：只用不改。發現工具的問題記在踩雷紀錄，要改程式先問 Ken。
  - 民宿 SEO 寫作 skill（`C:\myself\Github_tools_check\.claude\skills\minsu-seo-writing\`）：只引用，不改。
  - 官網 `https://ar2two.com`：不碰。
- 相依性影響評估：全域 skill 一放進去，所有專案都會看到它的簡介。草稿階段不放全域，避免沒確認過的內容影響其他專案。

### 3. 檔案清單

| 檔案 | 用途 |
|---|---|
| `C:\myself\ar2two-blog\docs\skill-draft\blog-article\SKILL.md` | skill 本體草稿 |
| `C:\myself\ar2two-blog\docs\skill-draft\blog-article\SKILL.html` | 給 Ken 看的 HTML 說明書（由 `C:\myself\md-sync-html-excel-slides-guard\tools\md2html.py` 從 SKILL.md 轉出） |
| `C:\myself\ar2two-blog\docs\blog-site-profile.md` | 阿爾兔兔部落格的網站設定檔 |
| `C:\myself\ar2two-blog\docs\blog-site-profile.html` | 網站設定檔的 HTML 版 |
| 本檔 | 進度檔 |

---

## 🚀 迭代紀錄 (Iteration)

**步驟 1：盤點與實測工具（2026-10-03～04）**

- 修改內容：盤點 SEO 工具包 35 支工具、總 SEO 程式、全域與 Github_tools_check 的 skill、claude-seo 參考說明、marketingskills、plugin、內建 skill；實際跑過其中 19 項。
- 結果：記在 `C:\myself\ar2two-blog\docs\meilidao-article-outline.md` 的「工具使用紀錄」。
- 備註：
  - Ken 指出第 3 步（擬大綱）、第 4 步（收集事實）一開始漏列工具，補上 `fetch_page`＋`parse_html`、`mirror.py`、已下載的官網文字。
  - Ken 要求全部重新盤點一次，之後補測 `competitor_gap`、`keyword_cluster`、`search_intent`、`gsc_kgr`、`rank_tracker`。

**步驟 2：決定架構（2026-10-04）**

- Ken 的需求：skill 不只給民宿文章用，以後其他部落格也要用。
- 決定：全域通用 skill ＋ 每個專案一份網站設定檔。「要不要套用民宿寫作規則」寫在網站設定檔，不另外寫民宿版 skill。
- Ken 決定：
  - Search Console 要求建立索引由 Ken 手動做，不用 claude-in-chrome。
  - `ai_visibility` 一定要放進流程，並當場執行一次。

**步驟 3：建立草稿（2026-10-04）**

- 修改內容：建立本進度檔、SKILL.md 草稿、HTML 說明書、網站設定檔。
- 預期變化：Ken 打開 HTML 說明書檢查內容。

**步驟 4：MD 同步檢查登記（2026-10-04）**

- Ken 用 `[允許改檔]` 同意後，配對清單 `C:\myself\ar2two-blog\docs\html-md-registry.json` 新增：SKILL.md ↔ SKILL.html、blog-site-profile.md ↔ blog-site-profile.html 兩組配對；不是說明書加 `docs/*-progress.md`。
- 兩份說明書用 `C:\myself\md-sync-html-excel-slides-guard\guard\approve.py` 記成基準，`check.py` 檢查結果 0 項。
- 影響：SKILL.md 與網站設定檔之後每次修改都要 Ken 的 `[允許改檔]`；改 MD 後要用 `C:\myself\md-sync-html-excel-slides-guard\tools\md2html.py` 重新轉出 HTML。

**步驟 5：安裝到全域（2026-10-04，Ken 看過 HTML 說明書同意、用 `[允許改檔]` 同意 A～D）**

- A：新增 `C:\Users\w1lin\.claude\skills\blog-article\SKILL.md`、`SKILL.html`（HTML 重新轉出，頁首來源路徑指向全域）。
- B：全域配對清單 `C:\myself\md-sync-html-excel-slides-guard\data\global-registry.json` 加 `skills/blog-article/SKILL.md ↔ SKILL.html`，SKILL.md 記成基準。
- C：備份到 `C:\myself\claude-global-config\skills\blog-article\`；該專案配對清單登記 `skills/*/SKILL.md` 為不是說明書、`skills/*/SKILL.html` 免配對；說明書 `docs\manual.md` 備份表加一列並重新轉出 HTML、記成基準。
- D：刪除部落格專案的草稿資料夾 `C:\myself\ar2two-blog\docs\skill-draft\`，配對清單拿掉草稿那組配對；網站設定檔的 skill 位置改成全域路徑，重新轉出 HTML、記成基準。
- 更正：刪除前跟 Ken 說草稿「已經在 Git 有備份」是錯的，草稿從沒 commit 過。實際備份在 `C:\tmp\ar2two-blog-skill-draft\`，以及全域與 `C:\myself\claude-global-config\` 的正式版本，內容相同。

---

## ⚠ 異常與還原

| 狀態 | 事項 | 處理 |
|---|---|---|
| 🟡 | `rank_tracker` 顯示「高雄寵物友善住宿」不在前 20 名，但 Search Console 平均第 10.6 名，兩邊對不上 | 原因待查，已寫進 skill 踩雷紀錄 |
| 🟡 | `ai_visibility` 執行時 Gemini 多次回 503（忙線） | 工具會自動補問，等跑完再看結果 |
