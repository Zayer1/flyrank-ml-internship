# Week 8+ Deliverable (Capstone): Send the Link

## Live Portfolio

**URL:** `https://zayer1.github.io/portfolio/`  
Every page from the sitemap is reachable. The hero claim lands in under ten seconds. The proof (metrics table) is visible above the fold on the project detail page. The prediction demo runs live. The graduate badge is in the footer.

---

## 3-Minute Demo Script

**[0:00 – 0:20] Open the portfolio home page**  
*"This is my portfolio. The headline tells you in one line what I do: I build ML systems that make predictions, not just notebooks. The single case study card below it links to my FlyRank capstone — let me open that."*

**[0:20 – 1:00] Walk the case study**  
*"The first thing you see is the proof — a comparison table showing my XGBoost classifier hitting Precision@50 of 0.71 against a heuristic baseline at 0.44. Same test split, same evaluation metric. That's the core claim. Below it is the methodology: how I defined the decay label, why I used GroupShuffleSplit instead of random split to prevent client-ID leakage, and what features drove the predictions. Nothing in this section is a claim I can't back up with code."*

**[1:00 – 2:00] Run the live demo**  
*"Now here's the part that turns the notebook into a product. This is a live prediction form connected to my FastAPI backend on Render. I'll enter some realistic inputs: 180 days since last update, 800 words, 8 internal links, declining return visits. Hit Run Prediction."*  
*(Wait for response.)*  
*"74% decay probability — flagged as High Risk. That came from the actual trained XGBoost model running on the server right now. Not a mock. Not a hardcoded value."*

**[2:00 – 2:40] Show the AI's contribution**  
*"One place AI did real heavy lifting: I wrote the methodology text in the case study by having my AI assistant challenge every claim I made. Every time I wrote something like 'the model performs well,' it asked me to quantify it. Every vague sentence got tightened. The writing is mine — but the AI was the editor that forced precision."*

**[2:40 – 3:00] Close**  
*"The portfolio is live, the demo runs, and the next case study — the V2 LLaMA-3 cascade — goes live on September 15th. That's the link."*

---

## Build Write-Up

**Stack decision:** Quarto + GitHub Pages for the portfolio, FastAPI + Render for the backend. The choice came down to one constraint: my portfolio's primary job is to accurately display a Jupyter notebook and its outputs, including LaTeX math, code cells, and matplotlib charts. Quarto does this natively. React or Next.js would have required me to build a custom renderer or embed a static image for every chart — adding maintenance cost for zero user-facing benefit.

**The hardest thing that broke:** CORS. The browser silently blocked every request from the GitHub Pages domain to the Render API until I understood that the Same-Origin Policy treats `github.io` and `onrender.com` as completely different security contexts. Adding the `CORSMiddleware` to FastAPI — and understanding *why* it was needed rather than just copying the fix — was the moment the system started working as a whole.

**What I would build next:** V2 LLaMA-3 LoRA Cascade. The current system requires a full feature vector from historical data to make a prediction. Pages with no history get a median-fallback, which is no better than the heuristic we replaced. V2 closes that gap by using a fine-tuned LLM to evaluate raw page content zero-shot, producing a semantic feature that feeds into the same XGBoost model.

---

## Build-in-Public Story

**The real win:** I shipped a machine learning system that a non-technical person can use without opening a terminal. Not a notebook, not a CSV with scores, not a slide deck with metrics — a form, a button, and a number with an interpretation. That's the gap between "data scientist" and "ML engineer," and crossing it during an internship proved it was possible before I had a job title for it.

**The real limitation:** The system is brittle on pages with no history. If you enter zeros for all the engagement signals, the model returns a probability that reflects median performance, not a genuine prediction. The model wasn't designed to handle cold-start pages. I named this limitation on the capstone page rather than hiding it, because the person who knows their system's failure modes is the one you trust to operate it in production.

---

## FlyRank Showcase

Site submitted to the FlyRank showcase for review. Opted in to a featured case study. The graduate badge is live at the bottom of the portfolio home page.
