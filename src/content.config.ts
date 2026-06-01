import { defineCollection, z } from 'astro:content';

const blog = defineCollection({
  type: 'content',
  schema: z.object({
    title: z.string(),
    excerpt: z.string(),
    publishDate: z.coerce.date(),
    category: z.string(),
    tags: z.array(z.string()).default([]),
    readTime: z.string(),
    coverImage: z.string().url(),
    featured: z.boolean().default(false),
    lang: z.string().default('en'),
  }),
});

export const collections = {
  blog,
};