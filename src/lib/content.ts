import { getCollection } from "astro:content";
import type { Post } from "../types";

export async function getPublishedPosts(): Promise<Post[]> {
  const posts = await getCollection("posts", ({ data }) => !data.draft);

  return posts.sort(
    (a, b) => b.data.pubDate.getTime() - a.data.pubDate.getTime()
  );
}

export function getLatestPostByCategory(posts: Post[]) {
  return posts.reduce<Record<string, Post>>((acc, post) => {
    if (!acc[post.data.category]) {
      acc[post.data.category] = post;
    }

    return acc;
  }, {});
}

export function getPostsByCategory(posts: Post[]) {
  return posts.reduce<Record<string, Post[]>>((acc, post) => {
    const categoryPosts = acc[post.data.category] ?? [];
    categoryPosts.push(post);
    acc[post.data.category] = categoryPosts;

    return acc;
  }, {});
}

export function slugifyCategory(category: string) {
  return category.toLowerCase().replace(/\s+/g, "-");
}

export function formatDate(date: Date) {
  return new Intl.DateTimeFormat("en", {
    year: "numeric",
    month: "short",
    day: "numeric"
  }).format(date);
}
