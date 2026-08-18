# Week 4 Deliverable: Pick the Stack

**My Constraints & Requirements:**
- **Cost:** 100% Free only.
- **Skill Level:** Highly proficient in Python and ML (the ML Capstone is finished). Comfortable in the terminal, but zero interest in fighting complex frontend JavaScript frameworks.
- **What it needs to do:** Host a static portfolio with a Home page and a Project Detail page (FlyRank ML Capstone).
- **How work must be displayed:** Needs to display long-form reading, Markdown, mathematical LaTeX, and code snippets from Jupyter Notebooks clearly.
- **Dynamic Needs:** Nothing needs to be dynamic yet. I am linking out to my deployed FastAPI backend, so the portfolio itself can be completely static.

**Three Stack Options Considered:**

1. **The Simplest: Notion + Super.so**
   - **How to build:** Write content in Notion, publish via Super.so.
   - **Hosting:** Free on Super.so.
   - **Backend needed?** No.
   - **Trade-off:** Fast to set up, but terrible for rendering Jupyter Notebooks, raw code blocks, and complex ML math. It breaks the way my work needs to be shown.

2. **The Middle Path (Front-runner): Quarto via GitHub Pages**
   - **How to build:** Write in `.ipynb` or Markdown, let Quarto compile it into a static site.
   - **Hosting:** Free on GitHub Pages.
   - **Backend needed?** No.
   - **Trade-off:** Requires installing a CLI and a small learning curve for the build step, but it perfectly and natively renders data science notebooks without fighting UI frameworks.

3. **The Most Powerful: Next.js + Vercel**
   - **How to build:** Build React components and route them using Next.js.
   - **Hosting:** Free on Vercel.
   - **Backend needed?** Yes (serverless functions available), but not needed yet.
   - **Trade-off:** Total design freedom and highly dynamic, but it is massive overkill. Maintaining a React app distracts from the core goal of showcasing ML engineering.

**My Decision & Rationale:**

I am choosing the middle path: **Quarto hosted on GitHub Pages**. 

*Why?* The most critical requirement is that my portfolio must display my ML work accurately—specifically Jupyter Notebooks, PR curves, and code blocks. Quarto is designed specifically for scientific publishing and handles `.ipynb` files natively. 

*Can I maintain this?* Yes. Because there is no backend to manage and the content is written purely in Markdown and Jupyter, maintaining it is as simple as running a `git push`. 

*What about the other two?* I rejected Notion because it can't handle my technical formatting needs (my work would break if I picked the simplest option). I rejected Next.js because it is extreme overkill—I am building a portfolio to prove my ML engineering skills, not to maintain a React app. A backend for the portfolio itself is not needed yet.
