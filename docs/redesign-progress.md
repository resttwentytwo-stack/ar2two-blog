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
| Step 4 | 文章內頁排版＋更新日期 | 完成，commit `4c01a24`，2026-10-03 已推上線；常見問題、麵包屑 Ken 同意排到之後 |
| Step 5 | 文章封面圖＋首頁卡片式列表 | 完成，commit `2461b1c`、`361b422`，2026-10-03 已推上線 |
| Step 6 | 關於我們頁面 | 完成，commit `7a54ca8`，2026-10-03 已推上線並確認 |
| Step 7 | RSS 訂閱（可選） | 建議先不做，等文章變多再說 |

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

- 2026-10-03：Step 6 關於我們頁草稿，內容取自官網 https://ar2two.com 首頁（Our Story、房型、合法民宿、國旅卡）與寵物友善文章 Ken 確認過的資訊。導覽列加「關於我們」（手機版跟「文章列表」一樣隱藏），所以頁尾版權那行也加「關於我們」連結，讓手機讀者找得到。官網自己寫的捷運步行時間有「3 分鐘」「5 分鐘」兩種，文章寫 4 分鐘，草稿暫不寫分鐘數。

- 2026-10-03：關於我們頁 Ken 確認：作者名字只放 Ken；捷運美麗島站與六合夜市步行 4 分鐘（官網寫 3、5 分鐘的地方不一致，以 4 分鐘為準）；要放免費早餐，文字取自官網「老江紅茶免費早餐，直接送到民宿」，年數依 Ken 更正為 63 年（官網寫 58 年是舊資料），只放在關於我們頁，不另寫文章。

## 裝潢以外的插單

- 2026-10-03：準備包棟文章素材。來源是官網包棟頁 https://ar2two.com/building-price/ ，Ken 確認以下內容現在都正確（第 7 項由 Ken 更正）：
  1. 平日包棟每人 700 元：最少 10 人，任選 3 間房含公共空間，合計 9,000 元，押金 2,500 元，只限 3 月和 11 月（Ken 確認）。
  2. 平日包棟 4 間房（任選）：合計 10,800 元，只限 3 月和 11 月（Ken 確認）。
  3. 平日包 6 間房：合計 13,000 元。
  4. 星期五包棟：合計 14,000 元（不含押金）。
  5. 星期六包棟：合計 17,000 元（不含押金）。
  6. 包棟入住前一天在大廳擺 1 張長桌、10 張馬卡龍椅，讓大家一起吃東西、聊天。
  7. 透過所有訂房平台訂 6 間房（阿爾兔兔官方網站、LINE 預訂除外），另收包棟清潔費 3,000 元，寵物每隻收 500 元清潔費。
  8. 取消政策：預訂時付清全額；入住前 10 天以前取消收 30% 手續費；4～9 天取消扣 50%；3 天內不得取消、不退款；包棟不接受延期。
  - 官網把星期五和假日都標成「選項 3」，Ken 確認只是編號打錯。文章用「平日、星期五、星期六」分類。
- 2026-10-03：包棟文章待補事實，Ken 回覆：
  1. 大廳照片用 `C:\myself\ar阿爾兔兔\大廳_NEW\大廳壓縮\` 裡的「大廳外向內」「大廳內向外」兩張（約 130 KB，寬 1,477 像素，夠用，不另找原始檔）。
  2. 包棟時每位入住旅客都有免費早餐：基本床位 19 人就是 19 份，加 3 床就是 22 份。加床每床酌收 500 元（Ken 沒有說是不是每晚計，文章照原話寫「每床 500 元」）。
  3. 晚上 10 點後關大廳窗戶、不在巷弄吵鬧的規定沒有變。
  4. 交叉比對官網後 Ken 確認：狗狗只接受中小型犬；包棟規定另有「退房前把大廳垃圾整理好放在垃圾桶旁，關掉冷氣和電燈」；大廳現在固定擺長桌和馬卡龍椅，不是只有包棟前一天才擺（官網包棟頁之後會更新）；選 3 間房的方案（每人 700 元，只限 3 月和 11 月），另外 3 間不會再租給其他客人。4 間房方案剩下的 2 間也不會租給其他客人（Ken 確認），所以文章寫成「不管選哪一種包棟方案，整棟都只住你們這一團」。
  5. 上線後 Ken 補充（2026-10-03）：訂房平台訂房，寵物每隻每天收 500 元；官網或官方 LINE 直接訂包棟，每間房一隻寵物免費（6 間房 6 隻）；包棟取消規定照官網包棟頁。文章已改「帶毛小孩一起包棟」段落和兩題常見問題。

- 2026-10-01：寵物友善文章補上幔幔、闔家兩個房型的照片（從 `C:\myself\ar2two-blog\public\images\rooms\` 複製到 `C:\myself\ar2two-blog\src\assets\rooms\` 並縮到 1600px 寬，原始檔未動）。房型名稱依官網房型介紹頁（https://ar2two.com/ar2two-room-introduction/）逐字對應、拿掉樓層標註：旅程 吊椅2人房、幔幔 公主2人房、闔家 親子樓中樓3人房、悠然 蛋椅鄉村4人房、趣味 親子樓中樓4人房、雀屏 文青4人房（官網該頁沒有雀屏，名稱由 Ken 提供）。照片說明與 alt 文字已更新，照片檔名不動，順序依人數由少到多。已 commit `5a299f9`，2026-10-01 已推上線。這個異動跟版面裝潢分開 commit。

## 下次從這裡接（2026-10-03 暫停時的狀態）

1. 版面裝潢 Step 0～6 都已完成並推上線（Step 3 Ken 決定不做；Step 7 RSS 建議先不做）。最後推上線的 commit 是 `7a54ca8`。
2. 目前在寫旅客文章「包棟資訊、房型」：
   - 包棟方案 8 項事實 Ken 已確認，見本檔決策紀錄「準備包棟文章素材」那一條。
   - 關鍵字已用 SEO 工具包查過，報告在 `C:\myself\seo-toolkit\reports\2026-10-03-ar2two-blog-baodong-kd.json`。建議主打「高雄包棟民宿10人」：官網包棟頁 https://ar2two.com/building-price/ 已經在搶「高雄包棟民宿」，部落格改搶人數長尾字，再導回官網。
   - 大綱已擬好：`C:\myself\ar2two-blog\docs\baodong-article-outline.md`。寫法照 Github_tools_check 專案裡的「民宿 SEO 寫作」skill（minsu-seo-writing），這個 skill 不會在部落格專案自動載入，要直接去讀。
   - 3 個待補事實 Ken 都已確認，見決策紀錄。
   - 草稿已寫好（2026-10-03）：`C:\myself\ar2two-blog\src\content\blog\gaoxiong-whole-house-homestay-10-people.md`，`draft: true`。事實只用民宿資料卡 `C:\myself\seo-toolkit\tools\profiles\ar2two-profile.md` 和本檔已確認的內容。`C:\myself\seo-toolkit\tools\writing_check.py` 錯誤 0 個，提醒 7 個：6 個是 Ken 已確認的 ⚠ 事實，1 個是說明文字裡「10人」沒空格（為了跟關鍵字寫法一致）。
   - 新增照片，都放在 `C:\myself\ar2two-blog\src\assets\photos\`：兩張大廳照，加上從「大廳外向內」裁出的封面 `baodong-cover-1x1.jpg`、`baodong-cover-4x3.jpg`、`baodong-cover-16x9.jpg`。
   - 2026-10-03 Ken 看過草稿說 OK，已改 `draft: false`，發文前檢查清單跑過、建置成功（共 4 頁）。房型名稱照官網寫法不加空格（例如「吊椅2人房」），跟寵物友善文章一致。
   - 2026-10-03 已 commit `d470f8f` 並推上線，https://blog.ar2two.com/blog/gaoxiong-whole-house-homestay-10-people/ 確認可以打開，首頁也列出這篇。配對清單已登記 `docs/*-outline.md`。
   - 包棟文章完成。2026-10-03 Ken 已在 Google Search Console 對這篇、首頁、關於我們頁都完成要求建立索引。Sitemap（`sitemap-index.xml`）2026-09-11 已提交、狀態成功，不用重交。之後可做：官網包棟頁「包棟前一天才擺長桌」、步行時間的寫法要更新（另一個專案）。
   - MD 同步檢查：大綱檔還沒登記分類，等 Ken 用 `[允許改檔]` 同意在配對清單的「不是說明書」名單加 `docs/*-outline.md`。
3. Ken 2026-10-03 的指示：照 Claude 的建議直接執行，不用逐項詢問，除非 Ken 喊停。commit 和推上線一樣要 Ken 的訊息帶 `[allow-pii]`，合併成一次問。回覆一律用繁體中文。
4. 其他還沒處理的事：
   - 民宿資料卡標 ⚠ 的兩項，Ken 已確認：步行到美麗島站、六合夜市都是 4 分鐘；老江紅茶 63 年。資料卡屬於 SEO 工具包專案，要在那邊更新。
   - 官網 https://ar2two.com 的網站名稱設定、早餐「58 年」舊資料（另一個專案）要不要調整。
   - 經營者部落格之後另開，網址與名稱屆時再討論。
   - 2026-10-02 MD 同步檢查擋過 `C:\myself\AI-agent_Ken\docs\diagrams\docs03-housekeeping-overview.html` 沒有同步，那是 ai-agent-ken session 的工作，不在本專案處理。

## 待處理／注意事項

- 2026-10-01 開工時，工作區有兩個不是本任務的未 commit 異動，commit 時一律不打包：
  - `C:\myself\ar2two-blog\CLAUDE.md`：改成引用全域規則的精簡版，配對的 `C:\myself\ar2two-blog\CLAUDE-overview.html` 尚未同步。
  - `C:\myself\ar2two-blog\public\images\rooms\`：2 張原始尺寸房間照片（約 16 MB、25 MB），網站沒有任何地方用到。
