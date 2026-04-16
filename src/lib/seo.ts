import { SITE_DESCRIPTION, SITE_NAME } from "../consts";

type SeoInput = {
  title?: string;
  description?: string;
  image?: string;
  canonical?: string;
  type?: "website" | "article";
  publishedTime?: string;
};

export function buildSeo(input: SeoInput = {}) {
  const title = input.title ? `${input.title} | ${SITE_NAME}` : SITE_NAME;

  return {
    title,
    description: input.description || SITE_DESCRIPTION,
    image: input.image || "/images/og-default.svg",
    canonical: input.canonical,
    type: input.type || "website",
    publishedTime: input.publishedTime
  };
}
