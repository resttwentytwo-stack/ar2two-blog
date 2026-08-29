## 專案背景

這是【阿爾兔兔民宿部落格】，跟阿爾兔兔民宿的官網（WordPress，正式網域 `ar2two.com`，注意拼法是 a-r-2-two，不是 artwo2）是**兩個完全獨立的網站**，只靠超連結互相導流，沒有資料或後台整合：

- 官網：`https://ar2two.com`（WordPress，架在 SiteGround，負責訂房）
- 部落格：`https://blog.ar2two.com`（本專案，Astro 靜態網站，架在 Vercel，負責 SEO 導流內容）

部落格目的：
1. 針對「高雄市寵物友善民宿」「高雄包棟民宿」等關鍵字寫 SEO 文章，把流量導回官網訂房頁
2. 順便累積民宿經營內容，未來可能轉化成「民宿經營管理課程」的教材草稿
3. 讓 Ken（非工程師）練習用 Claude Code 維護網站

Ken 不寫程式，也不太熟技術名詞，溝通時請用白話、生活化比喻說明，避免拋出未解釋的術語。

## 溝通風格與排版規範

- **語言風格**：一律使用**繁體中文（台灣習慣用語）**，自然如合夥人對話，**嚴格禁用**「旨在」、「總的來說」、「綜上所述」、「顯而易見」等生硬 AI 詞彙。
- **非工程師友好**：避免拋出未解釋的技術名詞，改用「日常生活或民宿營運比喻」說明功能原理，優先告知「這個步驟能解決什麼問題、省下多少時間」。
- **中文排版細節**：
  - 中英文與數字之間**必須加入一個半形空格**（例如：這篇文章大約 3 分鐘讀完、串接 Google Analytics）。
  - 保留英文專有名詞與品牌原有名稱（例如：Astro、Vercel、SEO、WordPress）。

## 文章怎麼寫（給未來的 Claude Code 對話參考）

文章一律由 Claude Code 撰寫初稿，Ken 只負責提供素材、確認與修改。**每次要新增文章前，先跟 Ken 收集以下資訊，不要自己編造民宿的實際資訊（設施、規定、地址等）**：

1. 這篇文章想吸引什麼樣的讀者／情境（例如「帶貓來高雄玩」「多人包棟聚會」）
2. 想主打的 SEO 關鍵字
3. 跟阿爾兔兔本身相關、需要寫進文章的實際資訊（設施、規定、周邊景點等）
4. 有沒有現成照片可用（若有，之後手動放進 `public/` 或文章資料夾）
5. 文章結尾要不要放導購連結／CTA（預設放「查看空房與訂房資訊」連結到 `https://ar2two.com`）

拿到素材後，在 `src/content/blog/` 新增一個 `.md` 檔（檔名用英文 slug），frontmatter 需包含 `title`、`description`、`pubDate`、`keywords`（陣列）、`draft`（草稿先設 `true`，Ken 確認後再改 `false`），格式可參考既有的範例文章 `gaoxiong-pet-friendly-homestay-guide.md`。

## Git commit 命名規則

每次 commit，標題行（第一行）一律用這個格式：

```
[YYYY-MM-DD] 簡短敘述
```

- `YYYY-MM-DD`：commit 當天的日期
- 簡短敘述：一句話講清楚這次改了什麼

需要更詳細的說明時，可以在標題行下方空一行後補充（例如改了哪些檔案、為什麼要改）。

## 開發協作守則

1. **先出計劃，確認再動**：處理批次調整文章內容、新增/修改文章結構、或建立新的頁面邏輯前，先用條列式說明「處理邏輯與預期成果」，等 Ken 確認後再動手執行。
2. **刪除/覆蓋既有內容前，先查清楚完整影響範圍**：執行任何可能清空或覆蓋既有檔案內容的操作前（例如批次改寫多篇文章的 frontmatter、重新產生某個資料夾），要先完整追蹤該操作實際會動到的**每一個**檔案/資料範圍，一次跟 Ken 講清楚，不要只講到當下想到的一部分就去問，避免 Ken 基於不完整的資訊同意，事後才發現還有別的內容也被動到。

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
