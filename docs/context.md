# Project Context

## Background

Years ago, the blog was managed through a self-hosted WordPress installation on purchased hosting. The original content may be lost, but there may still be a ZIP archive somewhere.

The current plan is to rebuild the blog as a static website that can be created and updated collaboratively in Claude or Codex sessions. If the old ZIP is later recovered, its contents should be migrated into the new format where possible.

## Key Decisions Made

- The blog will be built as a static website
- Hosting choice: GitHub Pages
- Comment/auth backend: Supabase
- Posts will be written in Markdown

## Why This Direction

This setup was chosen because it should be:

- Ultra-cheap
- Practical to maintain
- Suitable for collaborative updates in Claude or Codex
- Flexible enough to migrate old WordPress content later
- Good for SEO and long-term ownership of content

## Comments and Authentication Requirements

The site should support user comments.

Authentication should ideally support:

- Google
- Microsoft
- GitHub
- X/Twitter
- Facebook

The repo may be public, so security constraints are important:

- No secrets in the repository
- No private tokens committed
- No Supabase service-role or admin credentials in frontend code
- Security should rely on proper backend/auth rules, not hidden client-side config

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
