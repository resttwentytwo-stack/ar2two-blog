# 任務進度檔：演唱會高雄住宿文章＋補強兩個寫文章用的 skill

- 本檔位置：`C:\myself\ar2two-blog\docs\2026-10-06-concert-article-progress.md`
- 開始日期：2026-10-06
- 起因：Ken 選下一篇文章「演唱會高雄住宿」（2026-10-03 候選清單排第二篇）。開工前 Ken 要求盤點前三篇用過的工具與 skill，補進寫文章 skill 與民宿 SEO 寫作 skill。

## 📌 目前狀態摘要

- 整體進度燈號：🟡 部分完成待續（2026-10-08 凌晨 Ken 休息暫停；演唱會文章初稿寫完、自動檢查通過，等 Ken 看預覽）
- **下次從這裡接（2026-10-08 凌晨整理，每項都核對過檔案）**：

  | 項目 | 狀態 | 根據 |
  |---|---|---|
  | 大綱（11 段）、第 4 步收集事實、第 5 步圖片 | ✅ 都經 Ken 確認 | `C:\myself\ar2two-blog\docs\concert-article-outline.md` |
  | 第 6 步初稿 | ✅ 寫完，中文 2,196 字 | `C:\myself\ar2two-blog\src\content\blog\kaohsiung-concert-stay.md` |
  | 第 7 步自動檢查 | ✅ `writing_check` 錯誤 0；`astro build` 成功；`site_audit` 錯誤 0 | 下方第 6～8 步紀錄 |
  | 第 8 步給 Ken 看本機預覽 | ✅ Ken 2026-10-08 看完預覽說 OK；`draft` 改 `false`、`pubDate` 改 2026-10-08（Ken 確認） | 文章檔第 4、6 行 |
  | 待 Ken 回答 1：網址代號 | ✅ Ken 2026-10-08 確認用 `kaohsiung-concert-stay`（全小寫），文章檔已改名 | 文章檔名 |
  | 待 Ken 回答 2：「高雄車站新站體」 | ✅ Ken 2026-10-08 決定保留原寫法 | 文章「隔天可以去哪」段 |
  | 第 9 步 commit／上線 | ✅ 2026-10-08 commit `4674abf` 已推上 GitHub，正式網址 https://blog.ar2two.com/blog/kaohsiung-concert-stay/ 打得開；美麗島、包棟兩篇舊文的回連、sitemap 都確認有出現。**下一步：第 10 步要求建立索引、AI 能見度** | 寫文章 skill 步驟 10 |
  | 第 10 步上線後 | 進行中：① Search Console 要求建立索引 ✅ Ken 2026-10-08 完成（約 2026-10-15 再查有沒有收錄）；② `rank_tracker` 已加「高雄演唱會住宿」✅（只加名單沒查，等收錄後再查）；③ `ai_visibility` 追加第 11 題演唱會題目 ✅ Ken 確認（`C:\myself\seo-toolkit\tools\targets\ar2two-ai-questions.csv`，SEO 工具包還沒 commit）；④ 已上線 4 篇，下一篇到 5 篇要提醒做相關文章區塊 | 寫文章 skill 步驟 10 |
  | 部落格資料夾還沒 commit 的檔案 | 專案規則手冊、`docs\redesign-progress.md`、`public\images\`（開工前就有，不是這次改的） | `git status` |
  | `gsc_volume` 憑證過期 | 要 Ken 重新登入，另外排時間 | 異常表 |
  | `C:\myself\Github_tools_check\` 要不要開 GitHub 位置 | 還沒問 Ken | — |
  | `C:\myself\social-trend-scraper` 沒登記在專案名冊（MD 同步檢查 K13） | 已告訴 Ken，建議由建立它的 session 登記；Ken 還沒回 | 2026-10-07 對話 |

- （以下是 2026-10-07 凌晨的舊狀態表，保留對照）：

  **Ken 的提醒**：演唱會文章要把這次新增的所有工具和流程全部套進來，**從頭重新判斷一次大綱**，不直接沿用現在的大綱草稿。流程照寫文章 skill（全域 blog-article），對照表見 `C:\tmp\ar2two-blog-skill-checklist\寫文章流程總表-2026-10-07.html` 第三節。

  | 項目 | 狀態 | 根據 |
  |---|---|---|
  | 兩個 skill 補強（第 1～13 題、a～f、核對補的 6 項、圖片中文命名） | ✅ 已改、已 commit、已推上 GitHub（claude-global-config `ca1d8b0`、`a1899c2`、`8addf5b`） | git log |
  | 民宿 SEO 寫作 skill、zens-ink skill 的修改 | ✅ 已 commit（`d3c9c48`、`e370212`、`fc4b743`、`b65c9cd`）；**`C:\myself\Github_tools_check\` 沒有 GitHub 位置，只存在本機** | git remote 為空 |
  | `competitor_outline`、說明書、`llms_gen` 登記 | ✅ 已 commit、已推上 GitHub（seo-toolkit `db7eb55`、`a96ee2d`、`87d1bba`，連同 github-tools-check-a8 的 `3d6baaa`、`781a638`，Ken 同意全部推） | git log |
  | llms.txt、llms-full.txt | ✅ 已上線（部落格 `6e49f3d`）。正式網站 `ai_crawler_audit` 100/100；首頁、關於、3 篇文章都 200 | `C:\myself\seo-toolkit\reports\2026-10-07-ar2two-blog-ai-crawler-after.json` |
  | 主要關鍵字「高雄演唱會住宿」 | ✅ Ken 已確認 | 對話 2026-10-06 |
  | 大綱（照新流程重新判斷，11 段） | ✅ Ken 2026-10-07 確認，問完 8 題後的 6 項調整也確認 | `C:\myself\ar2two-blog\docs\concert-article-outline.md` |
  | 「建議不學」飯店清單、兩天一夜行程 | ✅ 飯店清單不學；兩天一夜改寫短段「隔天去哪」（駁二、高雄車站新站體） | 大綱逐段比對表 |
  | 第 4 步收集事實（公開事實查證、問 Ken 的 8 題） | ✅ 2026-10-07 完成；**下一步：第 5 步準備圖片** | 大綱「公開事實查證結果」「Ken 的回答」 |
  | `gsc_volume` 憑證過期 | 要 Ken 重新登入，另外排時間 | 異常表 |
  | `C:\myself\Github_tools_check\` 要不要開 GitHub 位置 | 還沒問 Ken | — |

- 2026-10-07 開工（Ken 說 ok）：第 1 項「步驟 2 結果沿用」✅；第 2 項「補 AI 延伸問題」✅，10 題已寫進大綱，第 10 題（演唱會期間會不會漲價）要問 Ken。第 3 項 `competitor_outline` 已跑完、逐段比對表已寫進大綱（12 項），Ken 確認第 2 項以外照建議定案；第 2 項（兩天一夜行程）Ken 選「只寫短短一段隔天可以去哪」，地點：駁二藝術特區、高雄車站新站體。第 4 項客人故事：Ken 中途喊停 Chrome 做法，改用 `fetch_page`；Dcard 全擋、PTT 讀到 4 篇，補了故事 4（開車停車）與線索，已寫進大綱。第 5 項對照交通型範本 ✅：Ken 確認加「開車來的話」一段，主推附近停車格、兩個停車場當備案。第 6 項站內連結 ✅：正文 6 個連結，Ken 確認。舊文回連 Ken 同意（上線時一起改）。第 7 項：重新判斷版大綱（11 段）Ken 確認 ✅。第 8 項＝第 4 步收集事實：公開事實已查（結果在大綱「公開事實查證結果」），高流轉乘路線 ✅（官方路網圖確認 O1／C14 是輕軌轉乘站）；停車場關閉寫法 ✅ Ken 選「寫交通管制以公告為準＋巨蛋官網停車說明」。公開事實全部完成；問 Ken 民宿這邊的 8 題 ✅（回答記在大綱「Ken 的回答」表）；依回答調整大綱 6 項 ✅ Ken 確認並已改進大綱。**第 4 步收集事實完成。**
- 第 5 步準備圖片：捷運示意圖 ✅ Ken 確認（直式，給手機看）：`C:\myself\ar2two-blog\src\assets\diagrams\美麗島站到各場館-捷運示意圖-阿爾兔兔.svg`，畫圖程式 `C:\myself\ar2two-blog\scripts\draw_concert_mrt_map.py`，備份與手機預覽在 `C:\tmp\ar2two-blog-concert\`。
- 封面 ✅ Ken 確認：Ken 提供 `C:\myself\ar阿爾兔兔\大廳_NEW\DSC_6624.jpg`（夜晚大門），窗內人臉模糊成霧面玻璃樣（Ken 指定），黑板電話 Ken 說不用模糊；裁成 `C:\myself\ar2two-blog\src\assets\photos\民宿大門-夜晚亮燈-阿爾兔兔-1x1.jpg`／`-4x3.jpg`／`-16x9.jpg`（1280 寬）。**第 5 步完成。**
- 第 6～8 步（2026-10-07）：初稿 `C:\myself\ar2two-blog\src\content\blog\gaoxiong-concert-stay.md`（中文 2,196 字，正文站內連結 6 個＋結尾 2 個）。`writing_check` 錯誤 0、提醒 2（標題含網站名稱後寬度 64、結尾是「阿爾兔兔民宿部落格」，版面自動加的，跟其他文章一樣）；`astro build` 成功；`site_audit` 錯誤 0（警告都是全站既有：全站沒 og:image、首頁孤兒頁誤報、美麗島文章一張圖 275KB）。手機版表格被切掉，改成清單。**`draft` 暫時改成 `false` 給 Ken 本機預覽 http://localhost:4321/blog/gaoxiong-concert-stay/ ，還沒 commit。** 待 Ken 確認：網址代號 `gaoxiong-concert-stay`（大綱原本暫定 `kaohsiung-…`，改成跟其他文章一樣的 `gaoxiong-`）；「高雄車站新站體」沒有找官方出處。
- 待處理：民宿資料卡 `C:\myself\seo-toolkit\tools\profiles\ar2two-profile.md` 第 95 列「22:00 後入住拿不到早餐」跟 Ken 2026-10-07 說的不符（早餐跟入住時間無關，只看入住當天 22:00 前有沒有在選單訂好）；深夜入住流程也可補「打電話、比對官方帳號裡的證件、傳密碼」。要動 SEO 工具包，另外問 Ken。
- 高流轉乘查證過程：路線圖 PDF 是純圖片、電腦沒有 PDF 工具，Ken 放行 `[allow-pii]` 兩次都沒讀到；裝了 `pypdf`（`pip install --user`，還留著，Ken 要移除再說）；最後改下載官網路網圖 JPG 直接看。
- 發現：高雄捷運網站用 `fetch_page` 會出現 SSL 憑證錯誤，curl 可以；WebFetch 摘要數字會出錯（寫進寫文章 skill 附錄 2 的候選，要 `[允許改檔]`）。
- 發現 `fetch_page --json` 壞掉（`ModuleNotFoundError: render_page`），`-o` 存檔正常。SEO 工具包只用不改，記下來之後處理。
- 重新判斷大綱的順序（2026-10-07 列給 Ken 看過）：步驟 2 結果沿用（不用再花點數）→ 補 AI 延伸問題 → `competitor_outline` 正式跑一次、逐段比對 → 客人故事補 dcard／ptt 線索 → 對照交通型 7 段範本 → 站內連結 4 條規則 → 給 Ken 確認大綱 → 第 4 步收集事實。
- 注意：`C:\myself\Github_tools_check\.claude\skills\zens-ink\SKILL.html` 是手工排版，不能用 md2html 重新轉（2026-10-07 踩過，已寫進寫文章 skill 附錄 2）。
- **以後要做、這次不做（Ken 2026-10-06 交代要記下）**：目標關鍵字清單 `C:\myself\seo-toolkit\tools\targets\ar2two.csv` 加一欄「負責頁面」，每個字填「官網某某頁」或「部落格某篇」，一張表看出每個字由誰負責、避免官網與部落格互搶。要動 SEO 工具包，也要一個字一個字跟 Ken 確認，另外排時間做。

---

## 📝 任務分析與執行計畫

### 1. 預期成果

- [ ] 寫文章 skill `C:\Users\w1lin\.claude\skills\blog-article\SKILL.md` 補上第 1～8 題的內容。
- [ ] 民宿 SEO 寫作 skill `C:\myself\Github_tools_check\.claude\skills\minsu-seo-writing\SKILL.md` 補上第 10～13 題的內容。
- [ ] 演唱會文章照補完的流程寫完、上線。

### 2. 邊界與禁區

- 允許修改範圍：本專案 `docs\` 與文章；兩個 skill 與它們的 HTML、備份（要 Ken `[允許改檔]`）；（原本第 4 題 C 要在 SEO 工具包新增小工具，改 D 後取消）。
- 禁止修改範圍：官網 https://ar2two.com 不碰；SEO 工具包其他程式只用不改；ZensInk 程式不改。
- 相依性：民宿 SEO 寫作 skill 在 `C:\myself\Github_tools_check\`，那個資料夾有 github-tools-check session 開著，動手前要先確認它沒在動這個資料夾。

---

## 🚀 迭代紀錄

**步驟 1：逐題確認兩個 skill 要補的內容（2026-10-06）**

| 題號 | 內容 | Ken 的決定 |
|---|---|---|
| 1 | 寫文章 skill 附錄 1 工具總表補上每個工具的檔案位置 | 補 |
| 2 | 步驟 2 加「前 10 名重疊比對」（規則見民宿 SEO 寫作 skill `references\keyword-page-grouping.md`） | 加 |
| 3 | 步驟 2 加「其他人也問了／相關搜尋」 | 加 |
| 4 | 抓「其他人也問了」的方式 | 原選 C（新增小工具），測試後 Serper 抓不到，改選 **D：Claude 用 claude-in-chrome 開 Google 台灣搜尋結果自己看**，每篇只查 1～3 個主要字，跳出機器人驗證就停下來請 Ken 處理。不動 SEO 工具包 |
| 5 | 步驟 3 加「站內連結要連到部落格自己的其他文章」；舊文要加回連時先列給 Ken 確認 | 加 |
| 6 | 步驟 4 加「公開資料由 Claude 查證，盡量用官方來源，大綱記下出處網址；找不到官方或來源不一致時問 Ken」 | 加 |
| 7 | 步驟 6 加「會過時的資訊不寫」（例如演唱會場次；改成告訴讀者去哪查） | 加 |
| 8 | 步驟 10 加「主題不在 AI 能見度題目裡，擬新題目給 Ken 確認後追加」 | 加 |
| 9 | 民宿 SEO 寫作 skill 漏的部分：補進原本的 skill 還是新增 | 補進原本的 skill |
| 10 | 民宿 SEO 寫作 skill 第一條規則加例外：民宿自己的事實仍只從資料卡拿；跟民宿無關的公開事實可以寫，條件是官方來源、大綱記出處、Ken 看過大綱 | 同意 |
| 11 | 民宿 SEO 寫作 skill 裡指向不存在的「民宿關鍵字追蹤」skill（`SKILL.md` 開頭與第六節、`references\keyword-page-grouping.md` 開頭與第五節）：改成指向官網用 SEO 總指揮第 2～3 步（`C:\myself\seo-commander\docs\manual.md`）、部落格用寫文章 skill 步驟 1～2，不另外做新 skill | 同意 |
| 12 | `references\page-templates.md` 在地文章範本補：A 交通型文章 7 段（開頭先講答案、捷運／走路／開車、路線示意圖、回程或晚上情況、附近停車、常見問題、結尾連官網訂房）；B 動筆前問民宿主人 4 題（有沒有這類客人、客人怎麼去怎麼回、客人常問常擔心什麼、自己有沒有走過與照片） | 補 |
| 13 | `references\content-brief.md` 第二節加：寫新文章前看「其他人也問了」「相關搜尋」＋LINE 客人問題，整理 2～3 句客人故事；每個擔心都要有一段回答，答不完放常見問題。`search-experience.md` 原段落保留 | 加 |
| 14 | 演唱會文章關鍵字研究照補完的方式開始查 | 待問 |

- 第 4 題做法 C 的事前測試（2026-10-06）：
  - `kd_dr` 存檔 `C:\myself\seo-toolkit\tools\cache\serp-cache.json` 的 34 個字，全部沒有「其他人也問了」「相關搜尋」。
  - 另外直接用 Serper 查「演唱會高雄住宿」（扣 1 次），一樣沒有。
  - Claude 用 Ken 的 Chrome 開 Google 台灣搜同一個字（Ken 同意）：沒有「其他人也問了」；有「其他人也搜尋了以下項目」8 個字（高雄演唱會住宿dcard、高雄巨蛋演唱會住宿、高雄巨蛋附近住宿dcard、高雄巨蛋演唱會住宿推薦、高雄巨蛋住宿推薦dcard、高雄演唱會住宿推薦、高雄流行音樂中心住宿dcard、高雄住宿駁二）。
  - 結論：Serper 抓不到相關搜尋，Google 畫面上卻有，新工具做法 C 不可行，第 4 題要重新決定。
- 備註：前三篇用過的工具來源是 `C:\myself\ar2two-blog\docs\meilidao-article-outline.md`「工具使用紀錄」19 列、`C:\myself\ar2two-blog\docs\baodong-article-outline.md`。
- 備註：LINE 客人常見問題整理 `C:\myself\ar2two-official-line-chat-download\reports\2026-09-26-客人常見問題整理.html` 裡沒有演唱會、巨蛋、世運、流行音樂、衛武營的資料。

---

**步驟 2：兩個 skill 一次改完（2026-10-06，Ken `[允許改檔]`）**

- 事前：用 SendMessage 問 github-tools-check-a8，它回覆不會改 minsu-seo-writing，並提醒避開 `C:\myself\Github_tools_check\` 裡別的未 commit 檔案（zens-ink skill、9/25 與 9/30 進度檔、兩個 .txt 對話紀錄，其中 pastedcontent 那個有 email，不要讀）。
- 寫文章 skill `C:\Users\w1lin\.claude\skills\blog-article\SKILL.md`：流程總覽、步驟 2（重疊比對、claude-in-chrome 看其他人也問了）、步驟 3（站內連結含部落格文章）、步驟 4（公開事實查證）、步驟 6（會過時的資訊不寫）、步驟 10（追加 AI 能見度題目）、附錄 1（加「位置」欄）、附錄 2（Serper 抓不到其他人也問了）。HTML 重新轉出、記成基準，已複製到 `C:\myself\claude-global-config\skills\blog-article\`。
- 民宿 SEO 寫作 skill：`SKILL.md`（description、第一條規則例外、第六節）、`references\keyword-page-grouping.md`（開頭、第五節）、`references\content-brief.md`（第二節加 Serper 限制、第 5 點客人故事）、`references\page-templates.md`（交通型在地文章 7 段、問民宿主人 4 題）。SKILL.html 重新轉出、記成基準；版面程式碼的排版跟舊版不同，所以差異行數多，內容只多了這次的修改。
- `check.py` 合計 0 項。備份在 `C:\tmp\blog-article-skill\`、`C:\tmp\minsu-seo-writing-skill\`。

**步驟 3：評估 marketingskills 的 ai-seo、site-architecture（2026-10-07，Ken 要求）**

- 讀完 `C:\myself\Github_tools_check\tools\marketingskills\skills\ai-seo\SKILL.md`、`C:\myself\Github_tools_check\tools\marketingskills\skills\site-architecture\SKILL.md`（internal linking 一節）。
- 可加進流程的候選（等 Ken 決定）：
  - a（ai-seo）AI 延伸問題：Google AI 回答時會自動延伸查 5～10 個相關問題；步驟 2 列出可能的延伸問題（用搜尋框建議、相關搜尋、客人故事核對，不憑空想），確認文章或部落格其他文章有涵蓋。**Ken 2026-10-07：加**
  - b（ai-seo）每段開頭 2～3 句能單獨成立的答案，拿出來單獨看也看得懂（不用「如上所述」「這個場館」這種要靠前文的寫法）。**Ken 2026-10-07：加**
  - c（ai-seo）文章裡的公開事實直接附出處連結、註明查證日期（不只寫在大綱）。研究顯示附出處、數字讓 AI 引用率提高約 4 成。只有公開事實附出處（民宿自己的事實不用）；出處放段落最後，不放句子中間。**Ken 2026-10-07：加**
  - d（ai-seo）確認部落格 robots.txt 沒擋 AI 爬蟲，用 `ai_crawler_audit` 查一次就好（網站層級，不是每篇）。2026-10-07 看過 https://blog.ar2two.com/robots.txt ：`User-agent: * Allow: /`，沒擋 AI。**Ken 2026-10-07：加進步驟 10 當提醒（改過網站設定或換平台後查一次）**
  - e（site-architecture）站內連結的文字要具體（「美麗島站走回民宿的路線」，不是「點這裡」）。**Ken 2026-10-07：加，並定成 4 條可檢查的規則**（寫進寫文章 skill 步驟 3 列連結、步驟 7 檢查）：
    1. 下限：至少連 1 篇部落格自己的相關文章（有的話）＋至少 2 個官網連結（主題相關頁、訂房首頁）。
    2. 上限：字數 ÷ 300 個，超過要逐一檢討（換算依據：英文每 1,000 字 5～10 個，1 英文字約 1.5～2 中文字）。
    3. 每段最多 2 個；同一網址全文只連一次（結尾訂房按鈕不算）。
    4. 大綱「站內連結」表填 3 欄：放哪一段、連結文字、讀者為什麼會點；寫不出理由就不放。
    - 部落格與官網分開數。連結樣式已有顏色＋底線（`C:\myself\ar2two-blog\src\styles\global.css` 第 73～80 行），不用改。
  - f（site-architecture，網站層級）文章底下加「相關文章」區塊；文章多了以後規劃主題總覽頁（hub）。**Ken 2026-10-07：這次不做**；已上線 5 篇以上做相關文章區塊、8～10 篇做主題總覽頁（2026-10-07 已上線 3 篇）。提醒機制：Claude 長期記憶 `blog-article-count-milestones`，加上寫文章 skill 步驟 10 加一條「上線後數已上線文章數，到 5 篇、8 篇提醒使用者」（跟其他 skill 修改一起改，要 `[允許改檔]`）。
- 不採用：英文 SaaS 的定價檔（pricing.md）、OKF、維基百科／Reddit 經營、付費監測工具（已有 `ai_visibility`）。
- 2026-10-07 Ken `[允許改檔]`：a～e 和 f 的提醒已寫進 `C:\Users\w1lin\.claude\skills\blog-article\SKILL.md`（流程總覽、步驟 2 AI 延伸問題、步驟 3 連結 4 條規則、步驟 6 每段開頭與出處、步驟 7 連結檢查、步驟 10 數文章與 AI 爬蟲、附錄 1 加 `ai_crawler_audit`）。HTML 重新轉出、記成基準，`check.py` 0 項，已複製到 claude-global-config。**還沒 commit**，等 Ken 看過。
- 2026-10-07 Ken 要求實測兩支還沒測的工具（都免費）：
  - `ai_crawler_audit https://blog.ar2two.com`：17 種 AI 爬蟲全部允許，AI 準備度 88/100；扣分在沒有 `llms.txt`（可用 `llms_gen` 產生，另外討論）。另用 GPTBot、ClaudeBot、PerplexityBot、Google-Extended 的身分實際抓美麗島文章，都回 200，Vercel 沒有另外擋。報告 `C:\myself\seo-toolkit\reports\2026-10-07-ar2two-blog-ai-crawler.json`。
  - `drift_baseline`（加 `--skip-cwv` 不用速度 API）：替美麗島文章記下基準（標題、說明、H1、H2 5 個、H3 10 個、結構化資料 1 個），存在 `C:\myself\seo-toolkit\claude_seo\drift-db\baselines.db`。接著 `drift_compare` 比對：所有規則都沒觸發，正常。
  - 兩支都可以在寫文章 skill 附錄 1 改成 ✅，要 `[允許改檔]`。
- 2026-10-07 llms.txt（Ken 同意做、選做法 B 網站自動產生）：新增 `C:\myself\ar2two-blog\src\pages\llms.txt.ts`，每次建置依已上線文章產生 `https://blog.ar2two.com/llms.txt`（中文標題、官網訂房連結、草稿不列；內容只用網站上已有的文字）。本機建置成功（5 頁），`http://localhost:4321/llms.txt` 可打開。Ken 看過 llms.txt 說 OK。
  - Ken 要求也做 llms-full.txt：新增 `C:\myself\ar2two-blog\src\pages\llms-full.txt.ts`，每篇已上線文章全文（文章小標題降一級；圖片相對路徑網站外打不開，改成「［圖片：照片說明］」）；llms.txt 加一行連到它。本機 `ai_crawler_audit http://localhost:4321`：88 → 96（只有 llms.txt）→ **100**（兩個都有）。**等 Ken 看 llms-full.txt 本機預覽，還沒 commit、還沒上線**。
  - 2026-10-07 核對後補的 6 項（Ken `[允許改檔]`）：寫文章 skill 附錄 1（`ai_crawler_audit`、`llms_gen`、`drift_baseline`／`drift_compare` 改 ✅）、步驟 10 加「改版面前後跑 drift」、附錄 2 加「`[allow-pii]` 一個標籤只夠一個指令」「手工排版 HTML 不能用轉檔工具重新產生」；網站設定檔加 llms.txt 那一列；`C:\myself\seo-toolkit\seo.py` 新增 `ZENS_INK_EXTRA` 登記 `llms_gen`（不改 ZensInk 程式）。HTML 都重新轉出、記成基準，`check.py` 0 項。**都還沒 commit**。總表：`C:\tmp\ar2two-blog-skill-checklist\寫文章流程總表-2026-10-07.html`
  - github-tools-check-a8 請求：在寫文章 skill 步驟 5、網站設定檔加「圖片中文檔名」規則（它說 Ken 已同意，規則在 `C:\myself\Github_tools_check\.claude\skills\minsu-seo-writing\references\images.md` 第三節）。Ken 2026-10-07 確認：部落格照這個規則，官網不用。已改寫文章 skill 步驟 5、網站設定檔「照片檔名」一列，HTML 同步、記成基準，`check.py` 0 項，已通知對方。**還沒 commit**。Ken 2026-10-07 再確認（`[允許改檔]`）：新封面、新 SVG 示意圖也用中文檔名（例如 `大廳-包棟長桌-阿爾兔兔-1x1.jpg`、`美麗島站到各場館-捷運示意圖-阿爾兔兔.svg`），已改網站設定檔封面、示意圖兩列。
  - 發現：`llms_gen` 沒登記在 SEO 工具包統一入口（`seo.py llms_gen` 找不到，要用 `python -m zens_ink.llms_gen`），但 `C:\Users\w1lin\.claude\skills\seo-toolkit\SKILL.md` 寫成可直接用。之後一起處理。

## ⚠ 異常與還原

| 狀態 | 事項 | 處理 |
|---|---|---|
| 🟡 | `gsc_volume` 失敗：Google 登入憑證過期（`oauth2.googleapis.com/token` 回 HTTP 400） | 沒有重試。要 Ken 重新登入（`C:\myself\seo-toolkit\zens_ink\setup_gsc.py`），另外排時間；這次不影響判斷（10/3 查過演唱會是 0） |
