import { defineCollection } from "astro:content";
import { glob } from "astro/loaders";
import { z } from "astro/zod";

const posts = defineCollection({
  loader: glob({ base: "./src/content/posts", pattern: "**/*.md" }),
  schema: ({ image }) =>
    z.object({
      title: z.string(),
      slug: z.string(),
      pubDate: z.coerce.date(),
      summary: z.string().max(220),
      category: z.enum([
        "IT",
        "AI",
        "Investing",
        "Free Thinking",
        "Politics",
        "Movies"
      ]),
      tags: z.array(z.string()).default([]),
      coverImage: image(),
      coverAlt: z.string(),
      thumbImage: image().optional(),
      description: z.string().max(180),
      canonicalUrl: z.string().url().optional(),
      substackUrl: z.string().url().optional(),
      linkedinUrl: z.string().url().optional(),
      responses: z
        .array(
          z.object({
            author: z.string(),
            authorUrl: z.string().url().optional(),
            source: z.string().optional(),
            sourceUrl: z.string().url().optional(),
            date: z.coerce.date().optional(),
            body: z.string()
          })
        )
        .default([]),
      draft: z.boolean().default(false)
    })
});

const guide = defineCollection({
  loader: glob({ base: "./src/content/guide", pattern: "**/*.md" }),
  schema: z.object({
    title: z.string(),
    slug: z.string(),
    order: z.number(),
    description: z.string().max(220)
  })
});

export const collections = { posts, guide };
