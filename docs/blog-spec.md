# Blog Specification

## Goal

Build a personal blog as a static website managed in Codex sessions, hosted on GitHub Pages, with Supabase used for comments and authentication.

The site should be:

- Minimalist
- Fast
- SEO-friendly
- Easy to update with Markdown posts
- Structured so old WordPress content can be migrated later if recovered

## Chosen Stack

- Hosting: GitHub Pages
- Content format: Markdown posts
- Comments and auth: Supabase
- Auth providers planned:
  - Google
  - Microsoft
  - GitHub
  - X/Twitter
  - Facebook

## Content Scope

The blog will focus on these sections:

- IT
- AI
- Investing
- Free Thinking
- Politics
- Movies

## Strategic Purpose

The blog is not just a publishing outlet. It should also support:

- Republishing the same content on Substack
- Promoting posts on LinkedIn
- Building a stronger professional public profile in the IT world
- Supporting career development and future job search

The site should therefore feel personal, credible, intelligent, and professionally useful.

## Information Architecture

## Core Pages

- Home
- Post pages
- Category/tag archives
- Optional future pages:
  - About
  - Now
  - Projects

## Homepage

The homepage should primarily be a reverse-chronological roll of latest posts.

### Sidebar

Every page should include a persistent sidebar, ideally on the top right or top left depending on final layout.

The sidebar should contain:

1. A very concise About/Contact box
2. One compact box for the latest post in each main section:
   - IT
   - AI
   - Investing
   - Free Thinking
   - Politics
   - Movies

## Post Presentation

- Every post should have a small image
- The image should appear in listing views and on the post page
- Posts should be clean and readable, with typography prioritized over decoration

## Visual Direction

## Selected Direction

The preferred direction is an editorial/minimalist design inspired by the restraint of Daring Fireball, but modernized and made more polished.

Working theme name:

- Editorial Signal

## Characteristics

- Minimalist layout
- Main content column plus narrow sidebar
- Concise, high-signal presentation
- Strong typography
- Clean post stream on homepage
- Small image for every post
- Serious and thoughtful tone
- Suitable for both personal writing and professional positioning

## Suggested Tone

- Intelligent
- Personal
- Independent
- Professional without looking corporate

## SEO Requirements

SEO is a top priority from the start.

The site should be designed to support:

- Clean URLs and slugs
- Strong metadata per post
- Canonical URLs
- Open Graph tags
- Twitter/X cards
- XML sitemap
- RSS feed
- robots.txt
- Structured data / JSON-LD for articles
- Good internal linking
- Fast page load
- Optimized images
- Clear semantic HTML

## Content Model

Each Markdown post should support at least:

- title
- slug
- date
- summary
- category
- tags
- cover image
- description
- canonical URL
- draft flag

This model should be designed so recovered WordPress content can later be mapped into it.

## Comments and Auth

Comments should be backed by Supabase and tied to stable post identifiers such as slug.

Requirements:

- Browser-safe public auth configuration only in frontend code
- No secrets committed to the public repository
- Security enforced through Supabase policies
- Social login support through the chosen providers

## Hosting Notes

GitHub Pages was chosen because it is ultra-cheap and simple.

This means:

- The repository can be public
- Frontend code must never include secrets
- Public keys/config intended for browser use are acceptable
- Any privileged behavior should remain outside the static frontend

## Future Migration

If an old WordPress ZIP or export is found later, the project should support migration of:

- Posts
- Pages
- Images/media
- Potentially comments if data is available

The content model and routing should make that migration straightforward.
