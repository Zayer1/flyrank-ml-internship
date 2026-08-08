# Agent instructions

Before any task in this repo: **read `skills/README.md`** — it is the router.
Find the task in its table and load exactly **one** skill (plus `skills/flyrank/flyrank-data/SKILL.md`
whenever the task touches the data). Do not load every skill; keep context small.

Ground rules for this repo:
- Search the repo before assuming something is missing or not implemented.
- One task per conversation; finish and verify before starting the next.
- Never commit datasets (CI blocks them). Never print private data, client names, or raw queries.
- The intern validates your output — end each task by running the notebook top to bottom.

# Current Project State (Added Aug 4)
- **Status:** Week 4 (`w04_baseline_score.ipynb`) is completely finished, audited, and submitted. The next active assignment is Week 5 (Machine Learning).
- **Capstone Choice:** The user selected the "Freestyle Lane: Future Growth / Recovery Prediction" (time-series forecasting). 
- **Week 5 Strategy:** For `w05_model.ipynb`, train an XGBoost probability classifier on the 30k starter dataset. Use a `GroupShuffleSplit` on `client_id` to prevent leakage. You must evaluate the ML model against the Week 4 heuristic baseline on the exact same test split using Precision@50 and Global Recall to mathematically prove the need for non-linear ML.
- **User Profile:** The user is highly competent in ML theory and strictly despises "wrapper" AI development. Do not patronize them with basic API tutorials. Always focus on raw mathematical implementations, edge cases (e.g. recall failures), and core applied ML architecture. Treat them as a peer researcher.

# Learned Rules
- **Video Processing:** Always prioritize headless CLI extractors (like yt-dlp) for parsing videos to save RAM. Only fallback to spinning up the browser subagent if the CLI fails, or if visual context is absolutely necessary.
