# Week 1 Deliverable: Draw the Path — Portfolio Sitemap + Toolkit

## Portfolio Sitemap

```
https://zayer1.github.io/portfolio/
│
├── Home (index.html)
│   ├── Hero: one-line claim + CTA to capstone
│   ├── FlyRank ML Capstone (primary case study card)
│   └── Contact / GitHub link
│
└── Project: FlyRank ML Capstone (project detail page)
    ├── The Problem (heuristic limits of manual SEO triage)
    ├── The Architecture (XGBoost + GroupShuffleSplit + FastAPI)
    ├── The Proof (Precision@50 vs baseline, PR curve)
    ├── Live Demo (embedded prediction form → Render API)
    └── CTA: "Read the V2 Proposal" → V2_PROPOSAL.md
```

No dynamic backend needed for the portfolio itself. The only live API call is the capstone prediction form which connects to a separately hosted Render instance.

## Free Toolkit Chosen

| Tool | Purpose |
|------|---------|
| **Quarto** | Compiles `.ipynb` and `.md` to clean static HTML |
| **GitHub Pages** | Free HTTPS hosting for the static portfolio |
| **Render (Free Tier)** | Hosts the FastAPI + XGBoost inference backend |
| **VS Code + Python** | All ML development and notebook authoring |
| **Antigravity IDE** | AI pair-programming workspace for the entire build |

## AI Workspace Setup Note

My Antigravity session is configured with full project context: it has read access to the entire repo including `V2_PROPOSAL.md`, the model notebooks, and the FastAPI server code. This means the AI assistant understands my exact technical stack, my evaluation metrics, and my identity kit — so every prompt I send it already knows who I am and what I'm proving. I am not starting each session cold.
