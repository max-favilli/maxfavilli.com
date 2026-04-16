import rss from "@astrojs/rss";
import { SITE_DESCRIPTION, SITE_NAME } from "../consts";
import { getPublishedPosts } from "../lib/content";

export async function GET(context) {
  const posts = await getPublishedPosts();

  return rss({
    title: SITE_NAME,
    description: SITE_DESCRIPTION,
    site: context.site,
    items: posts.map((post) => ({
      title: post.data.title,
      pubDate: post.data.pubDate,
      description: post.data.description,
      link: `/posts/${post.data.slug}/`
    }))
  });
}
