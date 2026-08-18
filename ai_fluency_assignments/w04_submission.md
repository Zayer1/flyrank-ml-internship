# Week 4 Deliverable: Pick the Stack

**My Constraints & Requirements:**
- **Cost:** 100% Free only.
- **Skill Level:** Highly proficient in Python and ML (the ML Capstone is finished). Comfortable in the terminal, but zero interest in fighting complex frontend JavaScript frameworks.
- **What it needs to do:** Host a static portfolio with a Home page and a Project Detail page (FlyRank ML Capstone).
- **How work must be displayed:** Needs to display long-form reading, Markdown, mathematical LaTeX, and code snippets from Jupyter Notebooks clearly.
- **Dynamic Needs:** Nothing needs to be dynamic yet. I am linking out to my deployed FastAPI backend, so the portfolio itself can be completely static.

**Three Stack Options Considered:**

1. **Notion + Super.so (Simplest):** Free, no backend. Fast setup, but breaks my ML work (can't render Jupyter notebooks or complex math properly).
2. **Quarto + GitHub Pages (Front-runner):** Free, no backend. Slight learning curve for the CLI, but perfectly and natively renders Jupyter notebooks without fighting UI frameworks.
3. **Next.js + Vercel (Most Powerful):** Free, optional backend. Total design freedom, but massive overkill and a maintenance distraction from core ML engineering.

**My Decision & Rationale:**

I am choosing the middle path: **Quarto hosted on GitHub Pages**. 

*Why?* The most critical requirement is that my portfolio must display my ML work accurately—specifically Jupyter Notebooks, PR curves, and code blocks. Quarto is designed specifically for scientific publishing and handles `.ipynb` files natively. 

*Can I maintain this?* Yes. Because there is no backend to manage and the content is written purely in Markdown and Jupyter, maintaining it is as simple as running a `git push`. 

*What about the other two?* I rejected Notion because it can't handle my technical formatting needs (my work would break if I picked the simplest option). I rejected Next.js because it is extreme overkill—I am building a portfolio to prove my ML engineering skills, not to maintain a React app. A backend for the portfolio itself is not needed yet.
