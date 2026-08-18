# Week 10 Deliverable: Send the Link (Capstone Submission)

**Live Portfolio URL:** `https://zayer1.github.io/flyrank-ml-internship`

---

## 1. The Build Write-Up

### The Stack Decision and Why:
I selected a stack of **Quarto + GitHub Pages** for the portfolio site, linked via REST API to a **FastAPI backend** running on **Render**. 

As an ML engineer, my core priority was displaying code, LaTeX math, and data science notebooks without getting bogged down in complex frontend JavaScript frameworks. Quarto natively compiles Jupyter notebooks (`.ipynb`) into high-performance, clean static HTML. This allowed me to deploy the static pages for free on GitHub Pages while hosting my actual XGBoost model in a separate, secure python container.

### The Hardest Thing That Broke:
Cross-Origin Resource Sharing (CORS) security policies broke our initial connection between the GitHub Pages domain and Render. Because web browsers block cross-domain fetch requests to prevent scripts from executing across different origins, the frontend was completely blind to the model. I resolved this by adding custom CORS middleware into the FastAPI server configurations, explicitly whitelisting the GitHub Pages origin, and enforcing token authentication headers (`X-API-Key`) to protect the inference route.

### What to Build Next:
Next, I am upgrading the backend from the classical tabular XGBoost engine to the **V2 LLaMA-3 LoRA Cascade**. This will combine classical structured data prediction with semantic, zero-shot URL evaluation to generate rich, conversational optimization playbooks.

---

## 2. The 3-5 Minute Demo Script

- **[0:00 - 0:45] Intro:** "Hi, I'm Zayer. Today I'm walking you through my FlyRank ML Capstone. The goal of this portfolio is to mathematically prove I can predict SEO traffic decay using Machine Learning instead of relying on generic heuristics."
- **[0:45 - 1:45] The Core Case Study:** "Here is the Quarto project page. I've documented my entire pipeline: extracting raw CSV metrics, implementing a `GroupShuffleSplit` on `client_id` to prevent data leakage, and training our XGBoost model to a Precision@50 that beats the baseline."
- **[1:45 - 3:00] The Live Inference Tool:** "Let's run a prediction. If I enter these metric values for a page that has lost backlinks and has had no content updates in 6 months, and click 'Run Prediction', the frontend queries our live Render backend. As you can see, it returns a 74% decay probability, flagging it as High Risk."
- **[3:00 - 3:45] AI Build Partner Highlight:** "One area where AI did the heavy lifting was translating my raw model outputs into an interactive user experience. My AI assistant helped write the asynchronous Javascript `fetch` logic and styled the validation warnings, allowing me to focus entirely on the python modeling."
- **[3:45 - 4:30] Conclusion:** "The portfolio is fully responsive, optimized for mobile screens, and ready to scale. Thanks for watching!"

---

## 3. The Build-in-Public Story

### The Win:
I successfully bypassed the typical "toy project" trap. Instead of leaving my XGBoost model locked inside a private local Jupyter notebook where no one can interact with it, I built a production-style deployment. I wrapped the model in a secure API, established rate-limiting, and wired it to a responsive UI that a non-technical manager can use to run predictions on demand.

### The Limitation:
The current pipeline is heavily dependent on tabular inputs. If an editor wants to evaluate a brand new page that has no historical click or traffic data, the XGBoost model has no features to work with and defaults to a median baseline. This limitation is exactly what inspired the V2 Cascade proposal, which integrates LLMs to perform semantic, zero-shot analysis on raw text inputs when historical tabular features do not exist.

---

## 4. The Graduate Badge & Showcase
- The **FlyRank Graduate Badge** is permanently installed in the page footer.
- The repository and live domain have been submitted to the FlyRank showcase for final review.
- Opted-in to showcase the XGBoost SEO decay tool as a featured project.
