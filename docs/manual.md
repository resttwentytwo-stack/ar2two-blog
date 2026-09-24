# ar2two-blog 說明書

- 本檔位置：`C:\myself\ar2two-blog\docs\manual.md`
- 配對 HTML：`C:\myself\ar2two-blog\docs\manual.html`

## 這個專案在做什麼

阿爾兔兔民宿部落格 blog.ar2two.com。

寫 SEO 文章，把流量導回官網 ar2two.com 的訂房頁。官網是另一個網站，由 `C:\myself\ar2two-siteground` 處理 SEO。

## 使用規範

寫文章、發文前檢查、commit 規則，只寫在 `C:\myself\ar2two-blog\CLAUDE.md`，這裡不重複。

## 安裝了哪些程式

- Astro：產生靜態網站的工具，設定在 `C:\myself\ar2two-blog\astro.config.mjs`。
- Vercel：網站主機，推上 GitHub 後自動部署。
- GitHub：版本控制。

帳號、網域、部署的設定紀錄見 `C:\myself\ar2two-blog\PROGRESS.md`。

## 架構

每個檔案負責什麼，見 `CLAUDE.md` 的「專案地圖」。

| 檔案 | 用途 |
|---|---|
| `C:\myself\ar2two-blog\CLAUDE.md` | 專案規則與專案地圖 |
| `C:\myself\ar2two-blog\CLAUDE-overview.html` | `CLAUDE.md` 的閱讀版 |
| `C:\myself\ar2two-blog\PROGRESS.md` | 部署與帳號設定的進度紀錄 |
| `C:\myself\ar2two-blog\src\content\blog\` | 部落格文章 |
| `C:\myself\ar2two-blog\docs\html-md-registry.json` | 配對清單，給 MD 同步檢查用 |
