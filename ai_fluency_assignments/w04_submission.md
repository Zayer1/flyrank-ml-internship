# Week 4 Deliverable: Pick the Stack

**My Constraints & Requirements:**
- **Cost:** 100% Free.
- **Skill Level:** Highly proficient in Python, ML, and Data Science. Comfortable with the terminal. Zero desire to write complex React/JavaScript frontend logic.
- **Display Needs:** Must natively render Jupyter Notebooks (`.ipynb`), mathematical equations (LaTeX), and Python code blocks.
- **Dynamic Needs:** None. No backend required yet. This is a static portfolio to display my FlyRank Capstone and V2 Proposal.

**Three Stack Options Considered:**

1. **The Simplest: Notion + Super.so**
   - **How it works:** Write everything in Notion, use Super.so free tier to publish it as a website.
   - **Hosting:** Super.so / Notion (Free).
   - **Backend:** No.
   - **Trade-off:** Extremely fast to set up, but terrible for rendering Jupyter notebooks or complex Python code blocks natively. It wouldn't show my ML work properly.

2. **The Middle Path (Front-runner): Quarto via GitHub Pages**
   - **How it works:** A scientific publishing system built specifically for data scientists. It natively converts `.ipynb` files and Markdown into a beautiful, static website.
   - **Hosting:** GitHub Pages (Free).
   - **Backend:** No.
   - **Trade-off:** Requires a bit of terminal setup and a build step (CI/CD via GitHub Actions), but perfectly renders my actual ML work with zero JavaScript required.

3. **The Most Powerful: Next.js + Vercel**
   - **How it works:** A full-stack React framework.
   - **Hosting:** Vercel (Free).
   - **Backend:** Yes (Serverless functions), though I don't need it.
   - **Trade-off:** Total design freedom and highly dynamic, but massive overkill. I would spend all my time debugging React components instead of showcasing my XGBoost models. High maintenance burden.

**My Decision & Rationale:**
I am choosing **Option 2: Quarto hosted on GitHub Pages**. 

*Why?* The most critical requirement is that my portfolio must display my ML work accurately—specifically Jupyter Notebooks, PR curves, and code blocks. Quarto is literally designed for scientific and data science publishing, handling `.ipynb` files natively. 

*Can I maintain this?* Yes, effortlessly. Because there is no backend to manage and the content is written in Markdown/Jupyter, maintaining it is as simple as running a `git push`. 

*What about the other two?* I rejected Notion because it can't handle my technical formatting needs, and I rejected Next.js because it is extreme overkill. I am building a portfolio to prove my ML engineering skills, not to maintain a complex React app. A backend is absolutely not necessary right now.
