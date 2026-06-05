# Project Context

## Background

Years ago, the blog was managed through a self-hosted WordPress installation on purchased hosting. The original content may be lost, but there may still be a ZIP archive somewhere.

The current plan is to rebuild the blog as a static website that can be created and updated collaboratively in Claude or Codex sessions. If the old ZIP is later recovered, its contents should be migrated into the new format where possible.

## Key Decisions Made

- The blog will be built as a static Astro 6 site with Markdown content collections
- Hosting choice: GitHub Pages (private repo)
- Comments: off-site (Substack + LinkedIn), curated "Responses" block on-site
- No on-site comment system, no Supabase, no client-side backend
- Typography: Fraunces + Source Serif 4 + Josefin Sans ("Editorial Signal" brief)

## Why This Direction

This setup was chosen because it is:

- Ultra-cheap (GitHub Pages hosting)
- Practical to maintain via Claude Code or Codex sessions
- Good for SEO and long-term ownership of content
- Flexible enough to migrate old WordPress content (done — original posts recovered from WP dump)

## Comments

Comments happen off-site on Substack and LinkedIn. Selected high-quality responses are curated into each post's frontmatter (`responses[]` array) and rendered on-site for SEO and quality signal. No on-site comment system or authentication.

## Publishing and Career Goals

The blog is intended to support more than personal publishing.

It should help:

- Reuse or republish content on Substack
- Promote posts on LinkedIn
- Increase visibility in the IT world
- Strengthen professional positioning
- Support career development and potential job search

This means the site should look credible, thoughtful, and professionally useful without feeling corporate or generic.

## Content Areas

The planned writing areas are:

- IT
- AI
- Investing
- Free Thinking
- Politics
- Movies

## Visual Preferences

The preferred visual direction is minimalist.

Reference point:

- Daring Fireball style restraint

But with these additions:

- A small image for every post
- A modernized, cleaner presentation
- A persistent small About/Contact box on every page
- A sidebar containing one box with the latest post from each section

## Desired Homepage Layout

The homepage should be mostly a roll of latest posts.

Alongside it, there should be a compact sidebar that includes:

1. About/Contact box
2. Latest IT post
3. Latest AI post
4. Latest Investing post
5. Latest Free Thinking post
6. Latest Politics post
7. Latest Movies post

The About/Contact box should sit near the top of the sidebar, on either the top right or top left depending on the chosen layout.

## Preferred Theme Direction

Three theme directions were proposed, and the recommended one is:

- Editorial Signal

Why it fits:

- Closest to the requested minimalist/editorial style
- Good for readability and SEO
- Strong fit for both personal essays and professional positioning
- Minimal without looking outdated

## SEO Priority

SEO is considered very important for this project.

The site should be built from the start with:

- Clean semantic HTML
- Good metadata
- Canonical URLs
- Open Graph support
- Twitter/X cards
- Sitemap
- RSS
- Structured data
- Fast page loads
- Optimized images

## Future-Proofing

The project should be organized so that if development ever needs to restart from scratch, these documents are enough to recover:

- The hosting/auth decisions
- The blog purpose and scope
- The intended visual style
- The content areas
- The layout expectations
- The migration goal from possible WordPress backups
