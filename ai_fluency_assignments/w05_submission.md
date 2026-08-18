# Week 5 Deliverable: Ship the Ugly One

## Live URL

**Portfolio:** `https://zayer1.github.io/portfolio/`  
**Capstone Product (embedded demo):** `https://zayer1.github.io/flyrank-ml-internship`

All pages from the sitemap are reachable:
- Home page (hero + case study card) ✅
- FlyRank ML Capstone project detail page ✅
- Contact/GitHub link ✅

---

## One Real Person's Reaction

**Who:** A senior data scientist working on growth analytics (relevant field — they evaluate ML-heavy portfolios regularly).

**What I asked:** "Open this link and tell me in 30 seconds what I do and whether the proof lands."

**Their exact feedback:**
> "Okay — you clearly built something real, I can tell from the metrics table. But the prediction tool on the capstone page just froze for about 8 seconds with zero feedback and I genuinely thought it had crashed. Also, showing `0.742918` as the output means nothing to me without knowing if that's good or bad. Map it to a risk tier. And the hero text is too long — I had to read three sentences before I understood your claim."

**What I noted:** The latency UX problem is the most urgent thing. Cold-starting a free Render instance takes 30-50 seconds, and with no loading spinner the user has zero feedback during that wait. The raw float output is the second issue — probabilities need a human-readable risk translation. The hero text length is a minor polish issue.

---

## The "Still Ugly" List

1. **No loading spinner** during the XGBoost inference API call (user sees a frozen UI during Render cold start).
2. **Raw float output** (`0.742918`) instead of a human-readable risk tier (e.g., `High Risk — 74%`).
3. **Hero text too long** — the one-line claim takes three sentences to land.
4. **No graceful error state** — if the API times out or returns a 422, the page shows nothing; no user-facing error message.
5. **Chart images not compressed** — the Precision-Recall curve PNG is unoptimized and slows mobile load noticeably.
