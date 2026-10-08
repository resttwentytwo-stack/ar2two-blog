## 專案背景

這是【阿爾兔兔民宿部落格】，跟阿爾兔兔民宿的官網（WordPress，正式網域 `ar2two.com`，注意拼法是 a-r-2-two，不是 artwo2）是**兩個完全獨立的網站**，只靠超連結互相導流，沒有資料或後台整合：

- 官網：`https://ar2two.com`（WordPress，架在 SiteGround，負責訂房）
- 部落格：`https://blog.ar2two.com`（本專案，Astro 靜態網站，架在 Vercel，負責 SEO 導流內容）

部落格目的：
1. 針對「高雄市寵物友善民宿」「高雄包棟民宿」等關鍵字寫 SEO 文章，把流量導回官網訂房頁
2. 順便累積民宿經營內容，未來可能轉化成「民宿經營管理課程」的教材草稿
3. 讓 Ken（非工程師）練習用 Claude Code 維護網站

## 專案地圖

開始改東西前，先知道每個檔案負責什麼、放在哪：

- `src/content/blog/*.md`：每篇文章一個檔案，frontmatter（標題、描述等設定）跟內文都寫在這裡。
- `src/content.config.ts`：規定文章 frontmatter 要有哪些欄位（title、description、pubDate、keywords、draft）。
- `src/layouts/BaseLayout.astro`：全站共用的版面框架，SEO 用的 meta 標籤設定也在這裡。
- `src/pages/index.astro`：首頁，會列出所有文章。
- `src/pages/blog/[...slug].astro`：單篇文章頁面的樣板，套用在每一篇文章上。
- `public/`：放靜態檔案的地方，之後文章要用的圖片手動放進來。
- `astro.config.mjs`：Astro 網站的整體設定。
- `PROGRESS.md`：部署與帳號設定的進度記錄（GitHub、Vercel、DNS 等資訊），跟建置/上線流程有關的事查這裡。
- `CLAUDE.md`：這份規則手冊本身。

## 溝通風格與排版規範

比照全域 `CLAUDE.md`(`C:\Users\w1lin\.claude\CLAUDE.md`)第 3 節(繁中台灣用語、禁用生硬 AI 詞彙、非工程師友好比喻、中英文數字間半形空格)。本專案補充：
- 「非工程師友好」比喻優先用「日常生活或民宿營運」情境舉例。
- 常見保留原文的專有名詞舉例：Astro、Vercel、SEO、WordPress。

## 文章怎麼寫（給未來的 Claude Code 對話參考）

文章一律由 Claude Code 撰寫初稿，Ken 只負責提供素材、確認與修改。**不論是新增文章，還是修改既有文章裡的事實內容（設施、規定、地址等），都要先跟 Ken 收集或核對正確資訊，不要自己編造或憑印象修改**。每次要新增文章前，先跟 Ken 收集以下資訊：

1. 這篇文章想吸引什麼樣的讀者／情境（例如「帶貓來高雄玩」「多人包棟聚會」）
2. 想主打的 SEO 關鍵字
3. 跟阿爾兔兔本身相關、需要寫進文章的實際資訊（設施、規定、周邊景點等）
4. 有沒有現成照片可用（若有，之後手動放進 `public/` 或文章資料夾）
5. 文章結尾要不要放導購連結／CTA（預設放「查看空房與訂房資訊」連結到 `https://ar2two.com`）

拿到素材後，在 `src/content/blog/` 新增一個 `.md` 檔（檔名用英文 slug），frontmatter 需包含 `title`、`description`、`pubDate`、`keywords`（陣列）、`draft`（草稿先設 `true`，Ken 確認後再改 `false`），格式可參考既有的範例文章 `gaoxiong-pet-friendly-homestay-guide.md`。

### 發文前檢查清單

把 `draft` 從 `true` 改成 `false` 正式發佈前，過一遍這份清單：

- [ ] 中文與英文／數字之間有加半形空格
- [ ] 主打的 SEO 關鍵字有自然出現在標題和文章前段
- [ ] `description` 長度適中（約 50–160 字元），讀起來通順、不是關鍵字堆砌
- [ ] 用到的圖片都補上 alt 文字（給搜尋引擎和視障讀者看的圖片說明）
- [ ] 文末有放導購 CTA 連結（或已跟 Ken 確認這篇不需要）
- [ ] frontmatter 五個欄位（`title`／`description`／`pubDate`／`keywords`／`draft`）都填齊
- [ ] 文章裡提到的民宿設施、規定等資訊已經跟 Ken 核對過，不是憑印象或猜測寫的

## Git commit 命名規則

比照全域 `CLAUDE.md` 第 6 節：標題行(第一行)一律用 `[YYYY-MM-DD] 簡短敘述` 格式，需要更詳細說明時可在標題行下方空一行後補充(例如改了哪些檔案、為什麼要改)。

## 開發協作守則

比照全域 `CLAUDE.md` 第 4 節(先出計劃確認再動、刪除覆蓋前查清楚完整範圍、不確定就主動確認不要腦補)。本專案的應用場景：
1. 處理批次調整文章內容、新增/修改文章結構、或建立新的頁面邏輯前，先用條列式說明「處理邏輯與預期成果」。
2. 批次改寫多篇文章的 frontmatter、重新產生某個資料夾前，先完整追蹤實際會動到的每一個檔案。
3. Ken 提供的文字素材（口頭描述、群組訊息、筆記）可能有錯字、講到一半、前後不一致的情況，發現時要具體指出哪裡有疑慮，跟 Ken 確認清楚後再寫進文章或改動檔案。

## 踩雷紀錄

記錄之前發生過的具體狀況，避免重蹈覆轍。之後只要發生「以為只改一個地方，結果影響到其他地方」之類的失誤，都補一條進來（格式：日期、發生什麼事、以後要注意什麼）。

- **2026-08-26 官網網域名稱寫錯**：一開始把官網網域誤寫成 `artwo2.com`，正確應該是 `ar2two.com`（a-r-2-two）。這兩個字長得很像，之後提到官網網址時要再三確認拼法，不要憑印象打。

## Development

When starting the dev server, use background mode:

```
astro dev --background
```

Manage the background server with `astro dev stop`, `astro dev status`, and `astro dev logs`.

## Documentation

Full documentation: https://docs.astro.build

Consult these guides before working on related tasks:

- [Adding pages, dynamic routes, or middleware](https://docs.astro.build/en/guides/routing/)
- [Working with Astro components](https://docs.astro.build/en/basics/astro-components/)
- [Using React, Vue, Svelte, or other framework components](https://docs.astro.build/en/guides/framework-components/)
- [Adding or managing content](https://docs.astro.build/en/guides/content-collections/)
- [Adding styles or using Tailwind](https://docs.astro.build/en/guides/styling/)
- [Supporting multiple languages](https://docs.astro.build/en/guides/internationalization/)
