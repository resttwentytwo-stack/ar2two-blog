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
| Step 2 | 導覽列升級＋訂房按鈕（預留語言切換位置） | 完成，commit `faf6c52`，2026-10-01 已推上線 |
| Step 2.5 | 搜尋結果外觀：首頁加網站名稱資料、小圖示換成粉紅房子 logo | 完成，commit `4a47e13`，2026-10-01 已推上線 |
| Step 3 | 頁尾升級（地址、聯絡、社群） | Ken 決定不做，頁尾維持只有版權那一行 |
| Step 4 | 文章內頁排版＋更新日期 | 完成，commit `4c01a24`，還沒推上線；常見問題、麵包屑 Ken 同意排到之後 |
| Step 5 | 文章封面圖＋首頁卡片式列表 | 完成：封面三版本交給 Google、內文外觀室內照片（commit `2461b1c`）；首頁卡片＋網站封面 4:3（未 commit） |
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

- 2026-10-01：Step 3 頁尾放 5 項聯絡資訊，資料取自官網 https://ar2two.com 、Ken 確認都正確：地址「高雄市新興區南台路43巷1弄6號」、電話 0988-830-610、LINE https://lin.ee/5NLaWwj 、Facebook https://www.facebook.com/ar2twokh 、Google 地圖（官網上的地點連結，地點名稱「阿爾兔兔 旅店」）。

- 2026-10-01：Step 3 做過一版頁尾（logo、店名、5 項聯絡資訊）預覽後，Ken 決定頁尾只留「© 年份 阿爾兔兔民宿．ar2two.com」那一行，新頁尾檔案已刪除、未 commit。依據：Google 不把每頁重複的頁尾當主要內容（https://www.seroundtable.com/footer-boilerplate-content-google-21941.html ，業界新聞轉述 Google 員工說法），在地排名看 Google 商家檔案（https://support.google.com/business/answer/7091 ）；頁尾聯絡資訊對讀者有小幫助（https://www.nngroup.com/articles/footers/ ），Ken 選擇保持簡潔。之後想加回聯絡資訊，資料見上一條。

- 2026-10-01：Step 4 日期顯示，Ken 選 A：標題下面顯示「發布於 X・最後更新 Y」，有填更新日期才顯示後半段。依據 Google 官方說明（https://developers.google.com/search/docs/appearance/publication-dates ）。寵物友善文章今天補照片、修正房型名稱算一次更新，Ken 同意 `updatedDate: 2026-10-01`。
- 2026-10-01：Step 4 Ken 同意加文章目錄，從段落小標題（h2、h3）自動產生。依據 Google 官方部落格 2009 年文章（https://developers.google.com/search/blog/2009/09/using-named-anchors-to-identify ）：段落有清楚名稱加上目錄，可提高搜尋結果出現「跳到某一段」連結的機會，但由 Google 自動決定。目錄放在日期下面、第一段之前（放第一段之後要另寫處理程式，暫不做）。
- 2026-10-02：Step 4 內文排版 Ken 看過預覽後說不用調整。日期 Ken 選加空格，文章頁與首頁列表統一寫成「2026 年 8 月 24 日」（依全域規則中文與數字之間加半形空格）。
- 2026-10-02：Step 4 的常見問題段落、麵包屑，Ken 同意排到之後：常見問題要 Ken 提供真實問答，跟下一篇文章一起規劃；麵包屑等文章變多、有分類再加。

- 2026-10-02：Step 5 不重新下載官方範本，封面圖與 RSS 直接照 Astro 官方文件做（https://docs.astro.build/en/guides/images/ 、https://docs.astro.build/en/recipes/rss/ ）。Step 6 若需要版面靈感再下載。

- 2026-10-02：Step 5 封面照片 Ken 不採用房型照片，改用 `C:\myself\ar阿爾兔兔\部落客照片\` 的 3 張（外觀、狗狗在室內、狗狗在門口），複製到 `C:\myself\ar2two-blog\src\assets\photos\`，原檔未動。另產生 3 張加上「引用媽寶濟斯嘟嘟拍攝照片」的新照片（檔名加 `-credit`），字型 jf open 粉圓 v2.1（SIL OFL 1.1，https://github.com/justfont/open-huninn-font ，下載到 `C:\tmp\fonts\jf-openhuninn-2.1.ttf`，不放進專案），不加底色：外觀棕色字放在原標籤上方、左緣切齊；門口深灰字放在原標籤下方；室內白色字放右下角。Ken 確認可以。照片授權 Ken 沒有明確回答，只要求標註拍攝者。

- 2026-10-02：Step 5 照片用法 Ken 選 A：門口那張（狗狗在民宿門口）當寵物友善文章的封面，外觀與室內兩張放進文章內文，放哪一段與照片說明要先擬好給 Ken 確認。

- 2026-10-02：Step 5 封面比例：Ken 要以手機與 Google 官方為主，讀者主要從 Google 搜尋與 AI 搜尋進來，Facebook 分享預覽不考慮。依 Google 文章圖片說明（https://developers.google.com/search/docs/appearance/structured-data/article ）提供 1:1、4:3、16:9 三版，存成 `C:\myself\ar2two-blog\src\assets\photos\pet-friendly-cover-1x1.jpg`、`-4x3.jpg`、`-16x9.jpg`（1:1 是整張原圖；4:3 保留上方標籤；16:9 切掉上方標籤，引用文字重加在右上角）。三版只放進給 Google 看的文章資料，畫面上不顯示。另依 Google Discover 說明（https://developers.google.com/search/docs/appearance/google-discover ）在全站加上 `max-image-preview:large`。文章設定新增可不填的 `cover` 欄位（square／standard／wide／alt）。
- 2026-10-02：照片說明（alt）依 Google 圖片說明（https://developers.google.com/search/docs/appearance/google-images ）撰寫，Ken 確認：封面「白色馬爾濟斯開心待在高雄寵物友善民宿阿爾兔兔的門口」；外觀「高雄包棟民宿阿爾兔兔的整棟外觀，藍綠色窗框搭配木門」；室內「白色馬爾濟斯在阿爾兔兔民宿的公共空間，毛小孩可以一起待在室內」。狗狗品種 Ken 確認是馬爾濟斯，名字未確認，不寫。

- 2026-10-02：外觀、室內照片放進寵物友善文章「歡迎認識阿爾兔兔民宿」那一段：外觀放在介紹最前面（小字「阿爾兔兔民宿整棟外觀」），室內放在介紹清單後、房型參考前（小字「毛小孩可以一起待在公共空間」），用加了引用文字的版本。前面 1～6 點通用建議不放阿爾兔兔照片，避免像廣告。Ken 同意這個位置。

- 2026-10-03：首頁改成卡片式列表（封面在上、標題日期摘要在下），文章頁在日期下方顯示封面。網站上的封面比例 Ken 照建議用 4:3（首頁卡片與文章頁相同），保留「阿爾兔兔民宿」標籤又不會把標題擠太下面。暫時的比例切換鈕已刪除。
- 2026-10-03：Ken 指示之後裝潢步驟照 Claude 的建議直接執行，不用逐項詢問，除非 Ken 喊停。

## 裝潢以外的插單

- 2026-10-01：寵物友善文章補上幔幔、闔家兩個房型的照片（從 `C:\myself\ar2two-blog\public\images\rooms\` 複製到 `C:\myself\ar2two-blog\src\assets\rooms\` 並縮到 1600px 寬，原始檔未動）。房型名稱依官網房型介紹頁（https://ar2two.com/ar2two-room-introduction/）逐字對應、拿掉樓層標註：旅程 吊椅2人房、幔幔 公主2人房、闔家 親子樓中樓3人房、悠然 蛋椅鄉村4人房、趣味 親子樓中樓4人房、雀屏 文青4人房（官網該頁沒有雀屏，名稱由 Ken 提供）。照片說明與 alt 文字已更新，照片檔名不動，順序依人數由少到多。已 commit `5a299f9`，2026-10-01 已推上線。這個異動跟版面裝潢分開 commit。

## 下次從這裡接（2026-10-01 暫停時的狀態）

1. Step 2（`faf6c52`）與 Step 2.5（`4a47e13`）已於 2026-10-01 推上線，正式網站確認過：導覽列、網站名稱資料、新小圖示都在，舊的 favicon.svg 已移除。
2. Ken 可以到 Google Search Console 的「網址檢查」對首頁按「要求建立索引」，讓 Google 早點更新網站名稱與小圖示（要 Ken 本人登入操作）。
3. Step 3 頁尾 Ken 決定不做。Step 4 已改好，commit 後下一步是 Step 5 文章封面圖＋首頁卡片式列表（要重新下載官方範本當參考，先問 Ken 放哪裡）。
4. 還沒確認的事：
   - 下一篇旅客文章「包棟資訊、房型」是不是新文章、內容要寫什麼。
   - 經營者部落格之後另開，網址與名稱屆時再討論。
   - 官網 https://ar2two.com 的網站名稱設定（另一個專案）要不要調整。

## 待處理／注意事項

- 2026-10-01 開工時，工作區有兩個不是本任務的未 commit 異動，commit 時一律不打包：
  - `C:\myself\ar2two-blog\CLAUDE.md`：改成引用全域規則的精簡版，配對的 `C:\myself\ar2two-blog\CLAUDE-overview.html` 尚未同步。
  - `C:\myself\ar2two-blog\public\images\rooms\`：2 張原始尺寸房間照片（約 16 MB、25 MB），網站沒有任何地方用到。
