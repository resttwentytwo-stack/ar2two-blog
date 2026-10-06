// 給 AI 看的網站導覽說明（https://blog.ar2two.com/llms.txt），格式依 https://llmstxt.org
// 每次建置網站時自動依照目前的文章產生，新文章上線不用手動更新；草稿（draft: true）不列。
// Google 官方表示它的 AI 功能不需要這份檔案，主要給 ChatGPT、Claude、Perplexity 等其他 AI 參考。
import type { APIRoute } from 'astro';
import { getCollection } from 'astro:content';

const SITE = 'https://blog.ar2two.com';

export const GET: APIRoute = async () => {
  const posts = (await getCollection('blog', ({ data }) => !data.draft)).sort(
    (a, b) => b.data.pubDate.valueOf() - a.data.pubDate.valueOf(),
  );

  const lines = [
    '# 阿爾兔兔民宿部落格',
    '',
    '> 我們是高雄的寵物友善包棟民宿阿爾兔兔，這裡分享帶毛小孩旅行、包棟住宿的實用經驗。',
    '',
    '部落格由民宿主人撰寫。訂房、空房與最新價格以民宿官網為準。',
    '',
    '## 文章',
    '',
    ...posts.map((post) => `- [${post.data.title}](${SITE}/blog/${post.id}/): ${post.data.description}`),
    '',
    '## 民宿官網',
    '',
    '- [阿爾兔兔民宿官網](https://ar2two.com/): 查看空房與訂房資訊',
    '',
    '## 關於',
    '',
    `- [關於我們](${SITE}/about/): 部落格與民宿的介紹`,
    '',
    '## 完整內容',
    '',
    `- [全部文章全文](${SITE}/llms-full.txt): 每篇已上線文章的完整內容`,
    '',
  ];

  return new Response(lines.join('\n'), {
    headers: { 'Content-Type': 'text/plain; charset=utf-8' },
  });
};
