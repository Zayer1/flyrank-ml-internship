# Week 4 Deliverable: Empty but Live — Ship a Blank Page

## Proof of Live Deployment

The portfolio scaffold was deployed live to GitHub Pages before any real content was added.

**Live URL (blank scaffold):** `https://zayer1.github.io/portfolio/`  
**Stack:** Quarto static site → GitHub Pages (free HTTPS, no server)

---

## What "Empty But Live" Looked Like

The first deployed version of the portfolio contained exactly:
- A single `index.qmd` Quarto file with my name and one placeholder line: *"ML Engineer. Work in progress."*
- A `_quarto.yml` configuration file specifying the output format and theme.
- The GitHub Actions workflow file that automatically rebuilds and deploys on every `git push` to `main`.

That's it. No case studies, no metrics, no charts. Just a real URL, loading over real HTTPS, confirmed working on my phone before any content existed.

---

## Why This Step Matters

Most people wait until everything is "ready" before deploying. Deploying the empty scaffold first forces you to solve the hardest part — the CI/CD pipeline, the domain routing, the HTTPS certificates — when there is nothing important at stake yet. If the deployment breaks on a blank page, that is a fast, safe failure. If it breaks after weeks of work, that is an expensive one.

For a Quarto site on GitHub Pages specifically, the two common traps are:
1. Forgetting to set `output-dir: docs` in `_quarto.yml` (GitHub Pages needs the HTML in a `/docs` folder)
2. Forgetting to add a `.nojekyll` file, which tells GitHub Pages to stop trying to process the files with its own static site engine

Both were caught and fixed at the empty-scaffold stage.

---

## Phone Confirmation

Opened `https://zayer1.github.io/portfolio/` on a physical mobile device (Chrome, Android). Page loaded correctly over HTTPS. The placeholder text was readable and the layout did not break on a narrow screen.
