import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

const blog = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/blog' }),
  schema: ({ image }) => z.object({
    title: z.string(),
    description: z.string(),
    pubDate: z.coerce.date(),
    updatedDate: z.coerce.date().optional(),
    keywords: z.array(z.string()).optional(),
    draft: z.boolean().default(false),
    // 封面：三種比例都交給 Google（官方建議 1:1、4:3、16:9），alt 是照片說明
    cover: z
      .object({
        square: image(),
        standard: image(),
        wide: image(),
        alt: z.string(),
      })
      .optional(),
  }),
});

export const collections = { blog };
