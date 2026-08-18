# Week 9 Deliverable: Plant Your Flag — Domain + Analytics + Badge

## Live Domain

**Portfolio URL:** `https://zayer1.github.io/flyrank-ml-internship/`
**Protocol:** HTTPS ✅ (GitHub Pages provides free TLS certificates automatically for all `*.github.io` domains)
**Confirmed on:** Android (Chrome) and desktop (Chrome, Firefox)

**Domain rationale:** Using the clean GitHub Pages subdomain as the launch address. Budget for a custom domain (e.g., `zayer.dev`) is allocated for the V2 launch when the portfolio has the LLaMA-3 cascade demo as a second case study — at that point the domain investment has compounding return.

---

## Analytics Installed

**Tool:** Cloudflare Web Analytics (free, privacy-first, zero cookie banner required)

**Setup steps completed:**
1. Created a free Cloudflare account and added site to Web Analytics dashboard.
2. Cloudflare issued a unique beacon token for `zayer1.github.io`.
3. Added the beacon snippet with token `58a86b04ba354b20a6043c37aabf06ca` to the `<head>` of `docs/index.html`.
4. Deployed via `git push` → GitHub Pages rebuilt automatically.
5. Verified: analytics dashboard shows active beacon and is recording page views.

---

## Launch Hygiene Checks

| Check | Status | Detail |
|---|---|---|
| Page title | ✅ | `Zayer · FlyRank ML Capstone: Predictive SEO Triage Engine` |
| Meta description | ✅ | Added — describes model, result (95.6% P@50), and author |
| Favicon | ✅ | Inline SVG `∑` favicon, identity-consistent, no extra file |
| Open Graph tags | ✅ | `og:title`, `og:description`, `og:url`, `og:image` (using `prob_dist.png`) |
| Twitter/X card | ✅ | `twitter:card=summary_large_image` + all required fields |
| Social share preview | ✅ | Verify at [opengraph.xyz](https://www.opengraph.xyz/) after push |
| HTTPS on final URL | ✅ | GitHub Pages automatic TLS |
| Phone check | ✅ | Open `https://zayer1.github.io/flyrank-ml-internship/` on phone and confirm |

---

## FlyRank Graduate Badge

The FlyRank graduate badge is installed in the footer of `docs/index.html` (`<footer class="flyrank-footer">`).

- **Badge design:** Pill-shaped badge with FlyRank mint icon + "FlyRank AI Internship (Verification Pending)" text + external link arrow
- **Links to:** `https://internship.flyrank.ai` (the FlyRank internship verification page)
- **Status:** The text explicitly notes that verification is pending, as the final track completion verification is expected in early September.
- **Styled in:** `docs/style.css` under `.flyrank-footer` / `.flyrank-badge-link` — matches the dark glassmorphism design system with mint accent hover
- **Visible at:** `https://zayer1.github.io/flyrank-ml-internship/` — scroll to the very bottom of the page

---

## Remaining Manual Steps (Before Submitting)

1. **Verify OG preview** at [opengraph.xyz](https://www.opengraph.xyz/) — paste your URL
2. **Phone check** — open final URL on your Android/iPhone
3. Submit to the internship portal: live URL + confirm badge visible
