// llms.txt 的完整版（https://blog.ar2two.com/llms-full.txt）：每篇已上線文章的全文，給 AI 一次讀完。
// 跟 llms.txt 一樣，每次建置網站時自動依照目前的文章產生；草稿（draft: true）不列。
import type { APIRoute } from 'astro';
import { getCollection } from 'astro:content';

const SITE = 'https://blog.ar2two.com';

// 日期寫成「2026-10-03」
const ymd = (date: Date) => date.toISOString().slice(0, 10);

// 文章原稿整理成給 AI 讀的樣子：
// 1. 小標題降一級（## → ###），文章標題才是 ##，結構不會混在一起
// 2. 圖片的網址是原始碼裡的相對路徑（../../assets/…），網站外打不開，改成「［圖片：照片說明］」
const tidy = (body: string) =>
  body
    .trim()
    .replace(/^(#{1,5}) /gm, '#$1 ')
    .replace(/!\[([^\]]*)\]\([^)]*\)/g, (_, alt) => `［圖片：${alt}］`);

export const GET: APIRoute = async () => {
  const posts = (await getCollection('blog', ({ data }) => !data.draft)).sort(
    (a, b) => b.data.pubDate.valueOf() - a.data.pubDate.valueOf(),
  );

  const sections = posts.map((post) => {
    const dates = [`發布：${ymd(post.data.pubDate)}`];
    if (post.data.updatedDate) dates.push(`最後更新：${ymd(post.data.updatedDate)}`);
    return [
      `## ${post.data.title}`,
      '',
      `- 網址：${SITE}/blog/${post.id}/`,
      `- ${dates.join('，')}`,
      `- 摘要：${post.data.description}`,
      '',
      tidy(post.body ?? ''),
      '',
    ].join('\n');
  });

  const text = [
    '# 阿爾兔兔民宿部落格：全部文章',
    '',
    '> 我們是高雄的寵物友善包棟民宿阿爾兔兔，這裡分享帶毛小孩旅行、包棟住宿的實用經驗。',
    '',
    '部落格由民宿主人撰寫。訂房、空房與最新價格以民宿官網 https://ar2two.com/ 為準。',
    '文章目錄見 https://blog.ar2two.com/llms.txt',
    '',
    ...sections,
  ].join('\n');

  return new Response(text, {
    headers: { 'Content-Type': 'text/plain; charset=utf-8' },
  });
};
