# maxfavilli.com

Static personal blog scaffold for GitHub Pages.

## Stack

- Astro static site
- Markdown content
- SEO-first page structure
- Supabase-ready auth and comments

## Quick start

Requires Node.js `22.12.0` or newer.

1. Install dependencies:

```bash
npm install
```

2. Copy environment variables:

```bash
cp .env.example .env
```

3. Start the dev server:

```bash
npm run dev
```

## Notes

- The repository is safe for public hosting as long as only browser-safe public variables are used in `.env`.
- Do not commit private tokens, OAuth client secrets, or Supabase service-role keys.
- Update `SITE_URL` before production so canonical URLs, sitemap output, and SEO metadata are correct.
