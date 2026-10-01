# 部落格版面裝潢進度

- 本檔位置：`C:\myself\ar2two-blog\docs\redesign-progress.md`
- 開始日期：2026-10-01
- 做法：保留現有部落格，參考 Astro 官方 blog template，一次換一塊零件（A 方法）。
- 不能動的東西：Search Console 驗證標籤、結構化資料（JSON-LD）、文章網址 `/blog/xxx/`、frontmatter 的 `keywords` 與 `draft` 欄位。
- 裝潢前的回復點：commit `f9549dd`。

## 參考範本

- 官方 blog template 下載在 session 暫存資料夾，只供參考，不放進專案。
- 範本版本：astro ^7.3.5、@astrojs/mdx ^8.0.2、@astrojs/rss ^4.0.19。
- 範本零件：Header、HeaderLink、Footer、BaseHead、FormattedDate、BlogPost 版面、global.css、about 頁、blog 列表頁、rss.xml.js。

## 步驟狀態

| 步驟 | 內容 | 狀態 |
|---|---|---|
| Step 0 | 下載範本、建立本進度檔 | 完成 |
| Step 1 | 全站配色與中文字型 | 完成，commit `3a5430a`，2026-10-01 已推上線 |
| Step 2 | 導覽列升級＋訂房按鈕（預留語言切換位置） | 已改好、建置通過，等 Ken 確認後 commit |
| Step 3 | 頁尾升級（地址、聯絡、社群） | 未開始 |
| Step 4 | 文章內頁排版＋更新日期 | 未開始 |
| Step 5 | 文章封面圖＋首頁卡片式列表 | 未開始 |
| Step 6 | 關於我們頁面 | 未開始 |
| Step 7 | RSS 訂閱（可選） | 未開始 |

## 決策紀錄

- 2026-10-01：Ken 確認走 A 方法，先做版面裝潢，中英切換之後再議。
- 2026-10-01：Step 1 主色調延續現有暖棕色系（背景 `#fdfaf6`、重點色 `#b5651d`、文字 `#2b2420`），只調質感不換大方向。
- 2026-10-01：Step 1 字型採混搭，標題思源宋體（Noto Serif TC），內文思源黑體（Noto Sans TC），從 Google Fonts 載入。
- 2026-10-01：Step 1 新增 `C:\myself\ar2two-blog\src\styles\global.css` 放全站共用樣式（原本樣式只寫在版面檔，管不到文章內文），修改 `C:\myself\ar2two-blog\src\layouts\BaseLayout.astro` 引用它並載入字型。
- 2026-10-01：首頁大標題與搜尋結果標題改成「高雄寵物友善民宿・包棟民宿住宿指南」（原本是「阿爾兔兔民宿部落格」與「首頁」），理由是部落格主要用來搶關鍵字導流。左上角導覽列維持「阿爾兔兔民宿部落格」當招牌。修改 `C:\myself\ar2two-blog\src\pages\index.astro`。
- 2026-10-01：首頁大標題下方小字改成「我們是高雄的寵物友善包棟民宿阿爾兔兔，這裡分享帶毛小孩旅行、包棟住宿的實用經驗。」（Ken 選定，直接表明身分）。
- 2026-10-01：首頁 description 改成「高雄寵物友善民宿、高雄包棟民宿怎麼選？阿爾兔兔民宿主人分享帶毛小孩旅行、多人包棟住宿的實用經驗與挑選重點。」
- 2026-10-01：Step 2 logo 來源 `C:\myself\ar阿爾兔兔\阿爾兔兔logo.png`（777x761、透明背景、粉紅色房子造型），複製到 `C:\myself\ar2two-blog\src\assets\brand\ar2two-logo.png`，原檔未動。
- 2026-10-01：Step 2 配色 Ken 比較 A（全棕色）／B（全粉紅）／C（棕色＋粉紅訂房鈕）三種預覽後選 A，訂房按鈕與全站重點色同為焦糖棕。預覽用的暫時切換鈕已刪除。
- 2026-10-01：Step 2 新增 `C:\myself\ar2two-blog\src\components\Header.astro`：logo＋站名、「文章列表」、圓角「查看空房・訂房」按鈕，導覽列固定在畫面上方；手機版隱藏「文章列表」。原清單的漢堡選單暫不做（目前只有 2 個項目），項目變多再考慮。

- 2026-10-01：Ken 看了 Google 手機搜尋結果截圖，覺得「阿爾兔兔民宿部落格」這個招牌沒有人會想點。Ken 一度選定招牌改成「高雄包棟民宿指南」，後來查了 Google 官方網站名稱說明（https://developers.google.com/search/docs/appearance/site-names ，要求網站名稱簡短、獨一無二，不要用泛用描述名稱），Ken 同意網站名稱維持「阿爾兔兔民宿部落格」，吸引點擊交給每一頁的標題。另查到犬哥網站（https://frankknow.com/best-blogging-platform/ ）標題有接「| 犬哥網站」，搜尋結果沒顯示是 Google 拿掉了重複的名稱。
- 2026-10-01：查到官網 https://ar2two.com 的網站名稱設定是一長串關鍵字，依 Google 說明很可能不會被採用。官網是另一個專案，這次不處理，之後另外討論。
- 2026-10-01：Ken 同意部落格分成兩個：`blog.ar2two.com` 專心做旅客內容（包棟、寵物友善、房型），經營者內容（派案系統、早餐預訂系統等 Google Sheets 工具與經營心得）另開新部落格，放在 `C:\myself\` 底下，等要寫第一篇經營文章時再建，網址與名稱屆時再討論。
- 2026-10-01：Ken 提到下一篇旅客文章的主題是「包棟資訊、房型」。是不是新文章、要寫哪些內容，還沒確認。

## 裝潢以外的插單

- 2026-10-01：寵物友善文章補上幔幔、闔家兩個房型的照片（從 `C:\myself\ar2two-blog\public\images\rooms\` 複製到 `C:\myself\ar2two-blog\src\assets\rooms\` 並縮到 1600px 寬，原始檔未動）。房型名稱依官網房型介紹頁（https://ar2two.com/ar2two-room-introduction/）逐字對應、拿掉樓層標註：旅程 吊椅2人房、幔幔 公主2人房、闔家 親子樓中樓3人房、悠然 蛋椅鄉村4人房、趣味 親子樓中樓4人房、雀屏 文青4人房（官網該頁沒有雀屏，名稱由 Ken 提供）。照片說明與 alt 文字已更新，照片檔名不動，順序依人數由少到多。已 commit `5a299f9`，2026-10-01 已推上線。這個異動跟版面裝潢分開 commit。

## 下次從這裡接（2026-10-01 暫停時的狀態）

1. Step 2 的 commit 等 Ken 確認。要放進去的檔案：
   - `C:\myself\ar2two-blog\src\components\Header.astro`
   - `C:\myself\ar2two-blog\src\assets\brand\ar2two-logo.png`
   - `C:\myself\ar2two-blog\src\layouts\BaseLayout.astro`
   - `C:\myself\ar2two-blog\src\styles\global.css`
   - `C:\myself\ar2two-blog\docs\redesign-progress.md`
   - 標題預定：`[2026-10-01] 版面裝潢 Step 2：導覽列加上 logo 與訂房按鈕`
   - commit 訊息含 Claude 協助標註的 email，會被隱私外掛擋下，Ken 的訊息要加 `[allow-pii]`。
2. Step 2 還沒推上線。推之前要先列 commit 清單給 Ken 確認。
3. 這一步跟部落格無關：MD 同步檢查要求登記 `C:\myself\singsong`（2026-10-01 07:30 出現，裡面只有 2 張 jpg、1 支 mp4）。已處理：2026-10-01 Ken 確認「不是專案」，已登記進 `C:\myself\md-sync-html-excel-slides-guard\data\projects.json` 的 `not_projects`。
4. 上面都處理完後，進入 Step 3 頁尾。第一個問題是請 Ken 提供要放的地址、聯絡方式、社群連結，不能自己填。

## 待處理／注意事項

- 2026-10-01 開工時，工作區有兩個不是本任務的未 commit 異動，commit 時一律不打包：
  - `C:\myself\ar2two-blog\CLAUDE.md`：改成引用全域規則的精簡版，配對的 `C:\myself\ar2two-blog\CLAUDE-overview.html` 尚未同步。
  - `C:\myself\ar2two-blog\public\images\rooms\`：2 張原始尺寸房間照片（約 16 MB、25 MB），網站沒有任何地方用到。
