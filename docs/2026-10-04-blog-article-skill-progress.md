# 任務進度檔：建立「寫部落格文章」skill

- 本檔位置：`C:\myself\ar2two-blog\docs\2026-10-04-blog-article-skill-progress.md`
- 開始日期：2026-10-04
- 起因：Ken 在寫完「美麗島 住宿」文章後，要求把所有 SEO 工具、skill、tool、plugin 中可以用來做文章的，整理成一份寫文章的 skill，往後任何部落格文章都照它做。

## 📌 目前狀態摘要

- 整體進度燈號：✅ 完成（2026-10-06）
- **下次從這裡接**：本任務沒有待辦了。唯一留著的事：SEO 工具包 `C:\myself\seo-toolkit\` 沒有 GitHub 位置，`1522a3a`、`4bbcdd5` 只存在本機（見步驟 10），要不要開 GitHub 位置之後再問 Ken。
- 關鍵決定／目前採用方式：
  - 架構：一個**全域通用** skill ＋ 每個部落格專案一份**網站設定檔**（Ken 2026-10-04 同意）。
  - skill 正式版在全域 `C:\Users\w1lin\.claude\skills\blog-article\`，備份在 `C:\myself\claude-global-config\skills\blog-article\`；部落格專案只留網站設定檔。
- 剩餘待辦：
  1. ~~skill 第 10 步、附錄 2 補 `ai_visibility` 內容~~：2026-10-05 已完成（Ken `[允許改檔]`），HTML 重新轉出、記成基準、check 0 項，已複製到 claude-global-config。
  2. ~~2026-10-05 補跑~~：已跑完，結果在步驟 7。
  3. ~~commit、推上 GitHub~~：2026-10-06 完成，見步驟 10。

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
- 更正（步驟 5）：刪除前跟 Ken 說草稿「已經在 Git 有備份」是錯的，草稿從沒 commit 過。實際備份在 `C:\tmp\ar2two-blog-skill-draft\`，以及全域與 `C:\myself\claude-global-config\` 的正式版本，內容相同。

---

## ⚠ 異常與還原

| 狀態 | 事項 | 處理 |
|---|---|---|
| 🟡 | `rank_tracker` 顯示「高雄寵物友善住宿」不在前 20 名，但 Search Console 平均第 10.6 名，兩邊對不上 | 原因待查，已寫進 skill 踩雷紀錄 |
| 🟢 | `ai_visibility` 執行時 Gemini 多次回 503（忙線） | 工具會自動補問；2026-10-04 那次 30 次全部有回答，見步驟 7 |
| 🟢 | 2026-10-05 早上 7:00 排程失敗：連不上網路（`getaddrinfo failed`） | 已加網路重試，見步驟 8 |

**步驟 6：AI 能見度報告的提醒通知（2026-10-04）**

- 起因：Ken 指出每週排程「SEO AI 能見度 - 阿爾兔兔」跑完沒有通知，不知道要去看報告。
- Ken 選擇：Windows 提醒型通知（停在螢幕上直到按掉）＋ 每次登入檢查、沒看過就再提醒。
- 新增 `C:\myself\seo-toolkit\tools\notify_ai_visibility.ps1`（找最新報告、沒看過就跳通知，加 `-Force` 可強制測試）、`C:\myself\seo-toolkit\tools\open_latest_ai_report.cmd`（通知的「打開報告」按鈕：用記事本打開報告並記成已看過，記在 `C:\myself\seo-toolkit\tools\usage\ai_visibility-seen.txt`）。
- 修改 `C:\myself\seo-toolkit\tools\run_ai_visibility.cmd`：跑完呼叫通知。
- 新增 Windows 工作排程「SEO AI 能見度 - 未讀提醒」：登入 1 分鐘後執行通知程式。
- 測試：手動觸發通知，Ken 按「打開報告」後已看過紀錄正常寫入。
- 待辦：skill 第 10 步要補上「排程跑完會跳提醒、按打開報告」；SEO 工具包這 3 個檔案還沒 commit。

**步驟 7：`ai_visibility` 實測結果（2026-10-04，阿爾兔兔）**

- 報告：`C:\myself\seo-toolkit\reports\2026-10-04\ai-visibility-ar2two-002114\report.txt`
- 執行時間約 2 小時（00:21～02:20），10 題 × 3 次 ＝ 30 次全部有回答，沒有失敗。用掉 Gemini 31 次呼叫、Google 搜尋 65 次（每月免費 5,000 次）。
- 總計：提到品牌 12/30 次（40%），引用官網 6/30 次（20%）。
- 強項：「包棟＋帶狗」（q3）、直接問阿爾兔兔（q5），都是提到 3/3、引用官網 3/3。
- 半強：單問「寵物友善民宿」（q1、q6）會提到 3/3，但引用的是 petview.app、asiayo.com 等第三方網站，不是官網。
- 完全沒出現：包棟聚會（q2、q7）、火車站／美麗島附近（q4、q9）、六人房（q8）、寵物友善飯店（q10）。
- 跟 2026-09-30 比較：9/30 只問 5 題、9 次失敗、只拿到 6 次回答，百分比不能直接比。兩次都有回答的題目中，q3 兩次都是 3/3，結果穩定。
- 2026-10-05 補跑結果：報告 `C:\myself\seo-toolkit\reports\2026-10-05\ai-visibility-ar2two-212902\report.txt`
  - 執行時間約 5.5 小時（2026-10-05 21:29～10-06 03:05），Gemini 忙線很多，比 skill 寫的「約 2 小時」久很多。
  - 26 次回答、4 次失敗（q5、q6、q8），總計提到品牌 9 次（35%）、引用官網 8 次（31%）。有失敗，百分比不跟 10-04 直接比，只比各題。
  - 變好：q1「高雄寵物友善住宿」引用官網 0/3 → 3/3。
  - 不變：q3 包棟＋帶狗仍是 3/3、3/3；q5 品牌字 2/2 提到也引用。
  - 仍然 0：q2、q7 包棟聚會，q4、q9 火車站／美麗島，q8 六人房，q10 寵物友善飯店。10-03 上線的包棟、美麗島兩篇文章還沒看到效果。
  - 看得到網址的引用都是官網（首頁、房型介紹頁），還沒看到部落格網址（多數引用只顯示網域，看不出是哪一頁）。

**步驟 8：排程加網路重試、skill 補內容的決定（2026-10-05）**

- 2026-10-05 早上 7:00 排程失敗：電腦剛睡醒網路還沒通。Ken 用 `[允許改檔]` 同意修改 `C:\myself\seo-toolkit\tools\run_ai_visibility.cmd`（本檔「禁止修改範圍」原本寫 SEO 工具包只用不改，這次是 Ken 同意的例外）。
- 修改內容：執行前先連一次 Gemini 網址，連不上就每 5 分鐘再試，最多 6 次，6 次都失敗就記錄放棄。改之前的舊版備份在本次對話的暫存資料夾（`run_ai_visibility.cmd.bak`）。
- 意外發現：`.cmd` 檔裡的中文（UTF-8）會被電腦用系統編碼讀錯，拆成指令執行而報錯；加 `chcp 65001` 反而更亂。最後改成全英文，執行紀錄訊息也是英文。舊版的中文說明很可能一直在背景默默報錯。
- 測試：用複製檔測「連不到的網址」→ 試 6 次後放棄；「正確網址」→ 第 1 次就執行。之後在背景正式補跑（2026-10-05 21:29 開始）。
- 通知測試：用 `-Force` 觸發，Ken 確認有跳出通知，按「打開報告」後已看過紀錄更新（21:10）。
- Ken 同意 skill 要補的內容：
  - 步驟 10 `ai_visibility`：實際花費（30 次呼叫、約 65 次搜尋）、實際時間（約 2 小時，放背景跑）、Gemini 常忙線（兩次都沒失敗才能比百分比）、每週排程與提醒通知用法（測試加 `-Force`）。
  - 附錄 2 踩雷紀錄：`.cmd` 只能寫英文；電腦剛睡醒網路沒通，已加重試。
  - 阿爾兔兔自己的結果只寫在本檔（步驟 7），不寫進 skill。
- `C:\myself\seo-toolkit\tools\open_latest_ai_report.cmd` 開頭中文說明也改成英文（Ken 同意）。Ken 第一次按按鈕沒反應（點擊沒傳到檔案），再跳一次通知後按「打開報告」正常，已看過紀錄更新（22:28）。
- commit（SEO 工具包，master）：`1522a3a` 排程通知與重試 3 個檔案、`4bbcdd5` 打開報告按鈕改英文。claude-global-config：`4f129a9` skill 補內容。都還沒推上 GitHub。

**步驟 9：skill 執行時間改成「約 2～6 小時」（2026-10-06，Ken `[允許改檔]`）**

- 修改 `C:\Users\w1lin\.claude\skills\blog-article\SKILL.md` 第 193 行：「約 2 小時」改成「約 2～6 小時，看 Gemini 忙不忙」，並註明 10-04 約 2 小時、10-05 約 5.5 小時。
- HTML 重新轉出、記成基準，`check.py` 合計 0 項。
- 已複製到 `C:\myself\claude-global-config\skills\blog-article\`，另備份在 `C:\tmp\blog-article-skill\`。

**步驟 10：commit 與推上 GitHub（2026-10-06，Ken 確認清單後同意推）**

- 部落格 `C:\myself\ar2two-blog\`：`55ae4c8` 只放本檔，已推上 GitHub（main）。`CLAUDE.md`、`docs/redesign-progress.md`、`public/images/` 不是這個任務改的，沒放。
- claude-global-config：`4f129a9`（步驟 8）、`4e1f16e`（步驟 9）已推上 GitHub（master）。
- 更正：之前寫「SEO 工具包要推 `1522a3a`、`4bbcdd5`」是錯的。`C:\myself\seo-toolkit\` 沒有設定任何 GitHub 位置，這兩個 commit 只存在本機。
- 本檔這次的更新（步驟 10、狀態改成完成）另外 commit 一次（Ken `[allow-pii]` 同意）。
