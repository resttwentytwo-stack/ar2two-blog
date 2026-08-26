# 阿爾兔兔民宿部落格 - 建置進度記錄

最後更新：2026-08-26

## 專案背景

- 這是【阿爾兔兔民宿】獨立於官網（WordPress）之外的新部落格專案
- 部落格跟官網是**兩個獨立網站**，只靠超連結互相導流（部落格文章導回官網訂房），沒有資料/後台整合
- 技術選擇：**Astro**（靜態部落格網站產生器），文章用 Markdown 檔案管理
- 目的：SEO 導流到官網訂房、累積內容資產（未來可能轉成民宿經營課程教材）、Ken 練習用 Claude Code 維護網站

## ⚠️ 重要：官網正式網域名稱更正（2026-08-26）

之前的記錄誤把官網網域寫成 `artwo2.com`，**實際正確拼法是 `ar2two.com`**（a-r-2-two，不是 a-r-t-w-o-2）。

- 官網：`https://ar2two.com`（WordPress，架在 **SiteGround**，負責訂房）
- 部落格網域：`https://blog.ar2two.com`（已設定完成，見下方）
- 專案本身的 repo 名稱 / Vercel 專案名稱仍叫 `artwo2-blog`（當初取名時筆誤，暫不影響功能，之後有空再考慮要不要重新命名）
- CLAUDE.md 已同步修正

## 帳號資訊

- 專案本機路徑：`C:\myself\artwo2-blog`
- GitHub 帳號：`resttwentytwo-stack`（注意拼字，中間是 rest-t-wentytwo，不是 restwentytwo）
- GitHub 倉庫：`https://github.com/resttwentytwo-stack/artwo2-blog`（Public）
- Vercel 帳號：已用同一組 GitHub 帳號登入 Vercel（Hobby / 免費方案），Vercel 專案名稱 `artwo2-blog`
- 網域註冊在 GoDaddy，但 **DNS 記錄實際由 SiteGround 管理**（GoDaddy 只是註冊商，名稱伺服器指向 SiteGround）
- SiteGround 帳號：登入信箱 `bootaitan1@gmail.com`

## 整體流程與目前進度

| # | 步驟 | 狀態 |
|---|---|---|
| 1 | 建立 Astro 部落格骨架、SEO 基本設定、範例文章 | ✅ 完成 |
| 2 | 本機 Git 版本紀錄 | ✅ 完成 |
| 3 | 註冊 GitHub 帳號 | ✅ 完成 |
| 4 | 建立 GitHub 倉庫 | ✅ 完成 |
| 5 | 推送程式碼到 GitHub（用 GitHub Desktop） | ✅ 完成 |
| 6 | 註冊 Vercel 帳號（用 GitHub 登入）、完成 2FA | ✅ 完成 |
| 7 | Vercel 匯入 `artwo2-blog` 倉庫並部署 | ✅ 完成，暫時網址 `https://artwo2-blog-emm0fq8hz-resttwentytwo-stack.vercel.app`（另有短網址 `artwo2-blog.vercel.app`） |
| 8 | 在 Vercel 專案加入自訂網域 `blog.ar2two.com` | ✅ 完成（一開始誤加成 `blog.artwo2.com`，已移除改正） |
| 9 | 到 SiteGround DNS Zone Editor 新增 CNAME 記錄（`blog` → `1cbe594060458ae7.vercel-dns-017.com.`） | ✅ 完成，SiteGround 顯示「CNAME record is created.」 |
| 10 | 等待 DNS 生效，確認 `blog.ar2two.com` 可以正常開啟 | ⬜ 進行中（SiteGround 提示最長可能要等 72 小時，通常會更快） |
| 11 | 確認 SEO 是否正常（sitemap、canonical、meta）、範例文章內容核實 | ⬜ 尚未開始（範例文章內容目前是通用示範寫法，非阿爾兔兔實際規定，需要 Ken 提供正確資訊後才能發佈） |

## 下次接續時該做的事

1. 打開瀏覽器訪問 `https://blog.ar2two.com`，確認 DNS 已生效、網站正常顯示（如果還沒生效，過一陣子再試）
2. 到 Vercel 專案的 Domains 頁面確認 `blog.ar2two.com` 狀態變成「Valid Configuration」
3. 確認網站顯示正常後，可以請 Ken 在官網 `ar2two.com` 上加一個連結導去部落格
4. 核實範例文章 `src/content/blog/gaoxiong-pet-friendly-homestay-guide.md` 的內容（寵物規定、設施等），確認無誤後把 frontmatter 的 `draft` 改成 `false` 正式發佈

## 給未來 Claude Code 對話的提醒

- Ken 是非工程師，技術操作要用白話說明，涉及帳號登入/密碼一律由 Ken 自己操作，Claude Code 不經手帳密
- 這台電腦的自動化終端機（PowerShell 工具）**不支援互動式登入**（不能跳出瀏覽器登入視窗、SSH 也連不出去），需要登入授權的操作要嘛請 Ken 自己在瀏覽器/GitHub Desktop 操作，要嘛用 Claude Code 的瀏覽器自動化工具開新分頁操作（新分頁會共用同一個 Chrome 個人檔案的登入狀態）
- **官網正式網域是 `ar2two.com`，不是 `artwo2.com`**——這兩個字很像，容易打錯，之後提到官網網址時務必再三確認拼法
- 網域註冊在 GoDaddy，但 DNS 記錄要去 **SiteGround**（Site Tools → Domain → DNS Zone Editor）改，不是在 GoDaddy 改
- 範例文章 `src/content/blog/gaoxiong-pet-friendly-homestay-guide.md` 內容是示範用，發佈前需要 Ken 核實或提供阿爾兔兔實際的寵物規定/設施資訊
