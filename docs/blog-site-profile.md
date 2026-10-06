# 網站設定檔：阿爾兔兔民宿部落格

- 本檔位置：`C:\myself\ar2two-blog\docs\blog-site-profile.md`
- 用途：「寫部落格文章」skill 第 0 步要讀的網站資料。skill 本身只寫通用流程，這個網站專屬的資料都寫在這裡。
- skill 位置：`C:\Users\w1lin\.claude\skills\blog-article\SKILL.md`（全域，2026-10-04 安裝；備份在 `C:\myself\claude-global-config\skills\blog-article\`）

## 網站

| 項目 | 內容 |
|---|---|
| 網址 | https://blog.ar2two.com |
| 技術 | Astro 靜態網站，架在 Vercel，推上 GitHub 後自動上線 |
| 跟官網的關係 | 官網 https://ar2two.com 是另一個網站（WordPress），負責訂房。部落格只負責 SEO 導流，不改官網 |
| 本機預覽 | `astro dev --background`，網址 `http://localhost:4321/` |
| 建置 | `npx astro build`，產出在 `C:\myself\ar2two-blog\dist\` |
| `kd_dr` 用的網域 | `blog.ar2two.com` |
| `ai_visibility` 用的網站代號 | `ar2two`（部落格是官網的子網域，引用部落格也算「有引用」） |
| 給 AI 看的網站導覽 | https://blog.ar2two.com/llms.txt （目錄）、https://blog.ar2two.com/llms-full.txt （全文），由 `C:\myself\ar2two-blog\src\pages\llms.txt.ts`、`C:\myself\ar2two-blog\src\pages\llms-full.txt.ts` 在建置時自動產生，新文章上線不用手動更新（2026-10-07 加入） |

## 事實來源

- 民宿資料卡：`C:\myself\seo-toolkit\tools\profiles\ar2two-profile.md`。寫進文章的價格、規定、距離、時間只能從這裡拿，或 Ken 在對話中親口確認。
- 已下載的官網文字：`C:\tmp\seo-lab\ar2two\site-text\`（2026-09-27 下載，可能過時）。
- 本機照片：`C:\myself\ar阿爾兔兔\`（大廳、房型、路徑照片等）。
- 官網本身有寫錯的地方（例如曾把每人 900 元寫成 700 元），只能當素材，寫進文章前要 Ken 確認。

## 關鍵字

- 目標關鍵字清單：`C:\myself\seo-toolkit\tools\targets\ar2two.csv`
- `gsc_kgr` 要排除的品牌字：`阿爾兔兔,阿爾,ar2two,rabbit`
- 官網已經在搶的大字（部落格不要搶同一個字當主要關鍵字）：例如「高雄包棟民宿」由官網包棟頁 https://ar2two.com/building-price/ 負責。

## 額外寫作規則

- 套用民宿 SEO 寫作 skill：`C:\myself\Github_tools_check\.claude\skills\minsu-seo-writing\SKILL.md`（這個 skill 不會在部落格專案自動載入，要直接去讀）。
  - 大綱格式：同資料夾 `references\content-brief.md`
  - 標題與說明：`references\title-description-rules.md`
  - 圖片：`references\images.md`
  - 黑名單詞與七道檢查：`references\review-checklist.md`
- 房型名稱照官網寫法，不加空格（例如「吊椅2人房」）。
- 「非工程師友好」的比喻優先用民宿營運情境。

## 文章

| 項目 | 內容 |
|---|---|
| 文章資料夾 | `C:\myself\ar2two-blog\src\content\blog\`，一篇一個 `.md`，檔名用英文網址代號（例如 `gaoxiong-meilidao-station-stay.md`） |
| 欄位 | `title`、`description`、`pubDate`、`updatedDate`（選填）、`keywords`（陣列）、`draft`、`cover`（`square`／`standard`／`wide`／`alt`），規定在 `C:\myself\ar2two-blog\src\content.config.ts` |
| 草稿 | 新文章先設 `draft: true`；草稿在本機預覽也看不到，要預覽時暫時改 `false` |
| 封面 | 三種比例放在 `C:\myself\ar2two-blog\src\assets\photos\`。新封面檔名照「照片檔名」規則，比例接在最後，例如 `大廳-包棟長桌-阿爾兔兔-1x1.jpg`、`-4x3.jpg`、`-16x9.jpg`（Ken 2026-10-07 確認；之前的 `主題-cover-1x1.jpg` 英文檔名已上線，不改名） |
| 內文照片 | `C:\myself\ar2two-blog\src\assets\` 底下依類別分資料夾（`photos`、`rooms`、`route`） |
| 照片檔名 | 新照片用中文：`場景或房型-照片內容-阿爾兔兔.jpg`，例如 `吊椅2人房-正面-阿爾兔兔.jpg`；半形「-」、半形數字，不堆關鍵字；已上線的照片不改名。完整規則見 `C:\myself\Github_tools_check\.claude\skills\minsu-seo-writing\references\images.md` 第三節（Ken 2026-10-07 確認部落格照這個規則） |
| 示意圖 | `C:\myself\ar2two-blog\src\assets\diagrams\`，畫圖程式放 `C:\myself\ar2two-blog\scripts\`。新示意圖檔名也用中文，例如 `美麗島站到各場館-捷運示意圖-阿爾兔兔.svg`（Ken 2026-10-07 確認；之前的 `area-map.svg` 等已上線，不改名） |
| 大綱 | `C:\myself\ar2two-blog\docs\主題-article-outline.md` |
| 結尾連結 | 「查看空房與訂房資訊」→ https://ar2two.com ；包棟主題另加「查看包棟方案」→ https://ar2two.com/building-price/ |
| 常用站內連結 | 房型介紹 https://ar2two.com/ar2two-room-introduction/ 、寵物規範 https://ar2two.com/pet-rule/ 、停車資訊 https://ar2two.com/ar2two-parking/ 、早餐 https://ar2two.com/ar2twobreakfast/ |

## 發文前檢查清單

以 `C:\myself\ar2two-blog\CLAUDE.md` 的「發文前檢查清單」為準。

## commit 與上線

- commit 標題：`[YYYY-MM-DD] 簡短敘述`，結尾加共同作者標記。
- 共同作者標記有 email，會被 sensitive-canary 擋下，要 Ken 送新訊息帶 `[allow-pii]`。
- 不放進 commit 的檔案：`C:\myself\ar2two-blog\CLAUDE.md`、`C:\myself\ar2two-blog\public\images\`（2026-10-01 開工前就有的修改，不屬於部落格任務）。
- 推上 GitHub 後 Vercel 自動上線，大約 1～2 分鐘。

## 進度檔

- 部落格進度：`C:\myself\ar2two-blog\docs\redesign-progress.md`（「下次從這裡接」）
- skill 建立進度：`C:\myself\ar2two-blog\docs\2026-10-04-blog-article-skill-progress.md`
