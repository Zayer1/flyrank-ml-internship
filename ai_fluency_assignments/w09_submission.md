# Week 9 Deliverable: Launch & Keep Building (Checkpoint 2)

## 1. The "Where It Breaks" List

Before launching, I spent time trying to break my interactive prediction tool. Below is the honest triage log of my findings:

### Fixed-Nows (Resolved before launch):
* **Garbage numeric inputs:** If a user typed negative numbers or strings into the "traffic_decay" boxes, the backend would throw a `422 Unprocessable Entity` validation error. 
  * *The Fix:* Added HTML input validation attributes (`min="0" type="number"`) and added a Pydantic schema validation layer on the FastAPI backend to catch invalid values and return clean, user-friendly warnings.
* **Double submission spamming:** Double-clicking the "Run Prediction" button triggered multiple parallel API calls, which could easily exhaust my Render free tier rate limit.
  * *The Fix:* Modified the submit event listener to immediately disable the button and change its text to `"Running Inference..."` until the API fetch completes.

### Known Limitations (Named honestly, not hidden):
* **Render Free Tier Cold Starts:** Because the backend is hosted on Render's free tier, the server spins down after 15 minutes of inactivity. The first visitor to run a prediction will experience a cold-start delay of 30-50 seconds while the instance wakes up. (Documented in the UI with a warning message).
* **Feature Vector Completeness:** The XGBoost model expects a complete set of features to predict decay. If the user doesn't know some metrics, the tool falls back to using median values calculated from the starter dataset, which lowers prediction confidence.

---

## 2. Launch Details
- **Live URL:** `https://zayer1.github.io/flyrank-ml-internship` (Deployed over HTTPS via GitHub Pages).
- **Favicon & Preview:** Favicon configured, page titles set properly, and the social preview card checked and verified using `OpenGraph.xyz`.
- **FlyRank Graduate Badge:** Installed in the footer of `index.html` linking directly to the FlyRank verification portal.

### Analytics Proof:
I installed **Cloudflare Web Analytics** (free, cookie-less, and privacy-friendly) to track visitors.
* Tracking script tag successfully embedded in the `<head>` of the portfolio site.
* Dashboard shows active page views coming from desktop and mobile referrals.

---

## 3. The Plan to Keep Building

### The 30-Minute Case Study Checklist:
1. **Gather Proof (10 mins):** Extract the final test metrics, Precision-Recall curves, and feature importance arrays from the Jupyter notebook.
2. **Tell the Story (15 mins):** Draft the project page using the three-beat shape (Question, Methodology, Results).
3. **Format & Commit (5 mins):** Compile to static HTML using Quarto and `git push` to deploy it instantly.

### The Next Project to Add:
- **Project Name:** The V2 LLaMA-3 LoRA Model Cascade (Zero-Shot URL virality analysis combined with XGBoost predictions).
- **Target Add Date:** September 15, 2026.
- **Calendar Reminder:** Set a bi-weekly reminder to commit V2 API development updates. I have preserved this Antigravity workspace to maintain context and code continuity for the V2 build.
