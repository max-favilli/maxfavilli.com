export const SITE_NAME =
  import.meta.env.PUBLIC_SITE_NAME || "I didn't know.";

export const DISPLAY_SITE_TITLE =
  import.meta.env.PUBLIC_DISPLAY_SITE_TITLE || "I didn't know.";

export const SITE_TAGLINE =
  import.meta.env.PUBLIC_SITE_TAGLINE ||
  "I am exploring the space between why and why not.";

export const SITE_DESCRIPTION =
  "A personal blog about IT, AI, investing, politics, culture, and independent thinking.";

export const CONTACT_EMAIL =
  import.meta.env.PUBLIC_CONTACT_EMAIL || "hello@example.com";

export const GUIDE_TITLE = "Agentic Engineering";
export const GUIDE_SUBTITLE = "a practical guide";

export const NAV_SECTIONS = [
  "IT",
  "AI",
  "Investing",
  "Free Thinking",
  "Politics",
  "Movies"
] as const;
