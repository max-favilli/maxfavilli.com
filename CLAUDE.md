# CLAUDE.md — maxfavilli.com

Collaboration rules for this repo. Read before acting.

## Always sanity-check design, UX, and content decisions against current consensus

Whenever the user asks for a design, UX, copy, layout, SEO, or content-strategy choice — and especially when they ask "does this make sense?" — **do not just implement what's requested**. First check the choice against what is generally considered good practice today:

- **UX consensus**: Nielsen Norman Group heuristics, common patterns across well-designed editorial blogs (Daring Fireball, Stratechery, kottke, The Morning Brew, etc.), accessibility norms (WCAG, screen-reader a11y), and mobile-first expectations.
- **Content-maker / creator-economy consensus**: current best practices around cross-posting, newsletter growth, social distribution (LinkedIn, Substack, X), and how thoughtful indie writers actually handle things today — not 2015 marketing playbooks.
- **SEO consensus**: Google's recent guidance (E-E-A-T, helpful-content signals, structured data), current opinions on canonical URLs for cross-posted content, outbound link handling, etc.
- **Modern trends**: what newer thoughtful publications are doing right now. If the user's request matches a pattern that's falling out of favor (e.g. "Read more" link antipattern, giant hero sections with no content, cookie banners in editorial layouts), say so.

Tell the user explicitly when a requested pattern is:
- **Standard and fine** → implement it.
- **Conventional but slightly suboptimal** → implement it but flag the tradeoff in one sentence.
- **Against current consensus** → push back with a short, opinionated explanation and a concrete alternative before implementing.

Don't be preachy, don't lecture, don't list every caveat. One or two sentences of honest judgment, then either do it or propose the alternative. The user runs Claude and Codex side-by-side to compare outputs — shallow "yes, done" answers lose to Codex. Direct, informed opinion wins.

## This project's fixed direction

- **Goal**: personal blog that supports career positioning in IT/AI. Must feel credible, thoughtful, and professionally useful — never whimsical, never corporate-generic.
- **Brief**: "Editorial Signal" — Daring Fireball restraint, modernized. Strong typography (Fraunces + Source Serif 4 + Josefin Sans), warm cream paper background with subtle texture, terracotta accent, real ink-on-paper contrast.
- **Stack**: Astro 6 static site + Markdown content collections + GitHub Pages hosting. No Supabase, no client-side backend.
- **Comments**: off-site (Substack + LinkedIn) with curated "Responses" block on-site for SEO and quality signal. No on-site comment system.

If a request would push the site away from any of these, say so before acting.

## Code-level preferences

- Keep components small and typed. Frontmatter changes go through `src/content.config.ts` (Zod schema).
- No emojis in code or UI copy unless explicitly requested.
- No comments in code unless the *why* is non-obvious.
- Never add features, abstractions, or fallbacks beyond what the task requires.
- After non-trivial changes, run `npm run build` and confirm clean output + page count before declaring done.

## Assets

- Original WordPress dump lives at `C:\Users\Favilli\OneDrive - JACK WOLFSKIN\tmp\dump-mf\`. Some files are OneDrive on-demand placeholders and may need to be manually hydrated by the user before copying.
- Real post cover images go in `public/images/posts/`. Author portrait is `public/images/author/max.jpg`.

## Content workflow

- Source of truth: this repo. Posts are cross-posted *from* here to Substack and LinkedIn manually.
- Each post's frontmatter can set `substackUrl`, `linkedinUrl`, and a curated `responses[]` array (see schema in `src/content.config.ts`).
- When generating post bodies from external sources (Wayback scrapes, WP dumps), always flag to the user that the reconstructed text should be reviewed before publishing — it is a draft, not the user's words.
