# Week 8+ Deliverable (Part 2): Plant Your Flag — Domain + Badge

## Live Domain

**Portfolio URL:** `https://zayer1.github.io/portfolio/`  
**Protocol:** HTTPS ✅ (GitHub Pages provides free TLS certificates automatically for all `*.github.io` domains)  
**Confirmed on:** Android (Chrome) and desktop (Firefox, Chrome)

Note: I am using the clean GitHub Pages subdomain as my "domain" for this build. Budget for a custom domain (e.g., `zayer.dev`) is allocated for the V2 launch when the portfolio has the LLaMA-3 cascade demo as a second case study — at that point the domain investment has compounding value.

---

## Analytics Installed

Installed **Cloudflare Web Analytics** (free, privacy-first, no cookie banner required).

Setup steps:
1. Created a free Cloudflare account and added my site to Web Analytics.
2. Cloudflare provided a single `<script>` snippet with a unique beacon token.
3. Added the script to the `<head>` of the Quarto layout template so it appears on every page.
4. Deployed via `git push` → GitHub Actions rebuilt and deployed automatically.
5. Verified the analytics dashboard shows an active beacon and is recording page views.

The dashboard now shows real visitor data: page views, unique visitors, top referrers, and device breakdown. I can see when the link was shared and whether visitors are reaching the capstone project page.

---

## Launch Hygiene Checks

| Check | Status |
|-------|--------|
| Social share preview (OG tags) | ✅ Added `og:title`, `og:description`, `og:image` to Quarto YAML front matter. Verified with `opengraph.xyz`. |
| Favicon | ✅ Custom `∑` SVG favicon, matches identity kit |
| Page titles | ✅ Each page has a unique descriptive `<title>` tag |
| All links open correctly on phone | ✅ Verified on Android Chrome |
| HTTPS on final URL | ✅ GitHub Pages automatic TLS |

---

## FlyRank Graduate Badge

The FlyRank graduate badge has been installed in the footer of the portfolio's `index.qmd` file. The badge links to the FlyRank internship verification page at `https://internship.flyrank.ai`.

The badge is visible on the live site at `https://zayer1.github.io/portfolio/` — scroll to the bottom of the home page.
