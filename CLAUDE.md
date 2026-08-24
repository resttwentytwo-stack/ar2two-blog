## 專案背景

這是【阿爾兔兔民宿部落格】，跟阿爾兔兔民宿的官網（WordPress，正式網域 `artwo2.com`）是**兩個完全獨立的網站**，只靠超連結互相導流，沒有資料或後台整合：

- 官網：`https://artwo2.com`（WordPress，負責訂房）
- 部落格：預計掛在 `https://blog.artwo2.com`（本專案，Astro 靜態網站，負責 SEO 導流內容）

部落格目的：
1. 針對「高雄市寵物友善民宿」「高雄包棟民宿」等關鍵字寫 SEO 文章，把流量導回官網訂房頁
2. 順便累積民宿經營內容，未來可能轉化成「民宿經營管理課程」的教材草稿
3. 讓 Ken（非工程師）練習用 Claude Code 維護網站

Ken 不寫程式，也不太熟技術名詞，溝通時請用白話、生活化比喻說明，避免拋出未解釋的術語。

## 文章怎麼寫（給未來的 Claude Code 對話參考）

文章一律由 Claude Code 撰寫初稿，Ken 只負責提供素材、確認與修改。**每次要新增文章前，先跟 Ken 收集以下資訊，不要自己編造民宿的實際資訊（設施、規定、地址等）**：

1. 這篇文章想吸引什麼樣的讀者／情境（例如「帶貓來高雄玩」「多人包棟聚會」）
2. 想主打的 SEO 關鍵字
3. 跟阿爾兔兔本身相關、需要寫進文章的實際資訊（設施、規定、周邊景點等）
4. 有沒有現成照片可用（若有，之後手動放進 `public/` 或文章資料夾）
5. 文章結尾要不要放導購連結／CTA（預設放「查看空房與訂房資訊」連結到 `https://artwo2.com`）

拿到素材後，在 `src/content/blog/` 新增一個 `.md` 檔（檔名用英文 slug），frontmatter 需包含 `title`、`description`、`pubDate`、`keywords`（陣列）、`draft`（草稿先設 `true`，Ken 確認後再改 `false`），格式可參考既有的範例文章 `gaoxiong-pet-friendly-homestay-guide.md`。

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
