# 任務進度檔：演唱會高雄住宿文章＋補強兩個寫文章用的 skill

- 本檔位置：`C:\myself\ar2two-blog\docs\2026-10-06-concert-article-progress.md`
- 開始日期：2026-10-06
- 起因：Ken 選下一篇文章「演唱會高雄住宿」（2026-10-03 候選清單排第二篇）。開工前 Ken 要求盤點前三篇用過的工具與 skill，補進寫文章 skill 與民宿 SEO 寫作 skill。

## 📌 目前狀態摘要

- 整體進度燈號：🟢 順利推進
- **下次從這裡接（2026-10-06 晚上整理）**：

  **Ken 的提醒**：演唱會文章要把這次新增進來的所有工作（新工具 `competitor_outline`、兩個 skill 補的流程：前 10 名重疊比對、其他人也問了、公開事實查證、會過時資訊不寫、站內連結、AI 能見度追加題目、逐段比對）全部套進來，**從頭重新判斷一次**大綱，不要直接沿用現在的大綱草稿。

  | 項目 | 狀態 | 根據 |
  |---|---|---|
  | 兩個 skill 第 1～13 題修改 | 已完成、已 commit（`C:\myself\Github_tools_check\` `d3c9c48`、`C:\myself\claude-global-config\` `ca1d8b0`），還沒推上 GitHub | 本檔步驟 2、git log |
  | 主要關鍵字「高雄演唱會住宿」 | Ken 已確認 | 對話 2026-10-06 |
  | 大綱草稿（10 段，含 A～E 補充） | 已寫，**Ken 還沒確認段落方向**；依上面提醒要重新判斷 | `C:\myself\ar2two-blog\docs\concert-article-outline.md` |
  | 「建議不學」飯店清單、兩天一夜行程 | Ken 還沒表態 | 大綱「Claude 建議不學的」 |
  | 新工具 `competitor_outline` | 已寫好、測試 4 篇成功、已 commit `db7eb55`（`C:\myself\seo-toolkit\`），還沒推上 GitHub | `C:\myself\seo-toolkit\tools\competitor_outline.py` |
  | 把新工具寫進 skill 第 1、2 項 | 已改（Ken `[允許改檔]`）並 commit：claude-global-config `a1899c2`、Github_tools_check `e370212`，還沒推上 GitHub | 本檔 |
  | 第 3、4 項（`C:\Users\w1lin\.claude\skills\seo-toolkit\SKILL.md`、`C:\myself\seo-toolkit\docs\manual.md`） | 2026-10-07 已改（Ken `[允許改檔]`），HTML 重新轉出、記成基準。seo-toolkit skill 沒有 git（claude-global-config 也沒有它的備份資料夾），備份在 `C:\tmp\seo-toolkit-skill\`。manual 已 commit `a96ee2d` | 本檔 |
  | 第 5 項（`C:\myself\Github_tools_check\.claude\skills\zens-ink\SKILL.md` 第 62 列） | 2026-10-07：先把 10/1 未 commit 的修改單獨補 commit `fc4b743`（Ken 同意），再加 `competitor_outline`。**SKILL.html 是手工排版，不能用 md2html 重新轉**（轉了會少 #### 標題、被 K3 擋，已還原手工版、只手動改一行），已 commit `b65c9cd` | 本檔 |
  | 第 4 步收集事實（公開事實查證、問 Ken 的 7 題） | 還沒開始 | 大綱「待補事實」 |
  | `gsc_volume` 憑證過期 | 要 Ken 重新登入，另外排時間 | 本檔異常表 |

- **SEO 工具包新增 `competitor_outline`（Ken 2026-10-06 同意，破例改 SEO 工具包）**：`C:\myself\seo-toolkit\tools\competitor_outline.py` 已寫好、測試 4 篇成功；`C:\myself\seo-toolkit\seo.py` 加一行登記。都還沒 commit。`seo.py` 裡另有 github-tools-check-a8 加的 pagespeed 那一行（它說短期不 commit、seo.py 不會再改），commit 時只放自己那一行。SEO 工具包說明書 `docs\manual.md` 和 seo-toolkit skill 由 github-tools-check-a8 先改，這邊要補 competitor_outline 說明前先問它。
- **~~要補進寫文章 skill~~（2026-10-06 已改，見上表）**：步驟 3 加「用 `competitor_outline` 整理競爭文章，逐段比對、每項標要補或不學並寫理由，抓同規模民宿文章」（Ken 2026-10-06 確認放步驟 3）；附錄 1 加 `competitor_outline`；民宿 SEO 寫作 skill `references\content-brief.md` 第二節加一句指向寫文章 skill 步驟 3。附錄 2：`parse_html` 的小標題在 `h1`、`h2`、`h3` 欄位；`word_count` 照英文空格算，中文文章不能用（2026-10-06 測試，見 `C:\myself\ar2two-blog\docs\concert-article-outline.md` 工具使用紀錄第 11 列）。
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
