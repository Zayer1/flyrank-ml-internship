# Week 7 Deliverable (Part 2): Survive the Crit — Checkpoint 1

## Design Review Submission

**Submitted alongside:** Week 1 proof statement — *"I am proving I can design and deploy a production-grade ML system: trained XGBoost classifier predicting SEO decay, deployed as a live FastAPI endpoint with an interactive frontend."*

**Reviewer:** A technical hiring manager at a B2B SaaS company (ML/data-adjacent team).

**Two questions asked first:**
- *"In ten seconds, what do I do?"*
- *"Do you believe I'm good at it?"*

---

## Reviewer Feedback

**On the ten-second question:**
> "I can see it's machine learning for SEO, but in ten seconds I couldn't tell if you were an ML researcher, a data analyst, or an engineer. The hero section has your name big and then a long sentence. I needed to read all of it to get the point."

**On credibility:**
> "Once I found the metrics table comparing your model to the baseline, yes — that's convincing evidence. But I had to scroll past three sections to find it. If you're proving engineering skill, the proof should be visible above the fold."

**Other feedback collected:**
- The input labels on the prediction form (e.g., "internal_link_count") have no explanation. A non-technical reviewer doesn't know if entering "12" is a realistic or nonsensical value.
- The PR curve chart title says "Model Performance" — the reviewer didn't know what a PR curve was and wanted a one-sentence explanation in plain language.
- Dark background + dark chart background = charts feel "heavy." A lighter chart background would help readability. (Mentioned once, unprompted.)
- No favicon on the portfolio site, so the browser tab just shows a blank page icon.

---

## Sorted: Must-Fix vs Nice-to-Have

### Must-Fix (fixed on live site before this submission):
1. **Hero claim not landing in 10 seconds** — Rewrote the hero headline to a single sharp line: *"I build ML systems that make predictions, not just notebooks."* Subtext in one sentence only.
2. **Proof not visible above the fold** — Moved the metrics comparison table (XGBoost vs baseline) to the very top of the project detail page, immediately after the problem statement.
3. **Input labels with no guidance** — Added placeholder text with realistic ranges to every form input (e.g., `Typical: 12 links, range 0–200`).
4. **Missing favicon** — Added a `∑` symbol as an SVG favicon, consistent with the identity kit.

### Nice-to-Have (acknowledged, not fixed for launch):
- PR curve plain-language caption (will add in the next content pass)
- Lighter chart background variant (low priority — does not affect the proof)
- Dark mode toggle (pure visual preference)

---

## Evidence: Must-Fixes on the Live Site

All four must-fixes are now live at `https://zayer1.github.io/portfolio/`. The hero rewrite and metrics table repositioning are visible immediately on page load. The form placeholders and favicon are active on the capstone project detail page.
