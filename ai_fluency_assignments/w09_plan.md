# Week 8+ Deliverable (Part 3): The Plan to Keep Building

## The 30-Minute "Add a New Case Study" Checklist

When the next project is done, I can add a new case study to this portfolio in under 30 minutes by following this checklist:

1. **Create the case study file (10 min):** Add a new `projects/project-name.qmd` file. Use the existing FlyRank capstone page as the template — keep the same three-beat structure (Problem → Work → Proof).
2. **Drop in the assets (5 min):** Add any charts, screenshots, or diagrams to `assets/images/project-name/`. Reference them in the `.qmd` file with relative paths.
3. **Add the card to the home page (5 min):** Add a new project card to `index.qmd`. Same HTML structure as the existing FlyRank card — copy, paste, update the title, description, and link.
4. **Build and verify locally (5 min):** Run `quarto preview` to check the layout, confirm the new page renders correctly, verify the nav link works.
5. **Commit and push (5 min):** `git add . && git commit -m "Add [project name] case study" && git push`. GitHub Actions deploys automatically within 60 seconds.

My AI workspace (this Antigravity session) already knows my stack, identity kit, and writing voice. I will keep this conversation context active — every future case study I draft, I can paste in the raw notes and ask it to write the three-beat version in my established voice without re-explaining the setup.

---

## The Next Project to Add

**Project:** V2 LLaMA-3 LoRA Cascade — Zero-Shot SEO Virality Predictor

This is the natural sequel to the FlyRank capstone. Where V1 (XGBoost) requires structured historical tabular data, V2 uses a fine-tuned LLaMA-3 model to evaluate raw URL content and structural features zero-shot, producing a semantic virality score without needing historical click data. The two models cascade: V2 provides features for V1 on pages with no history.

**Target add date:** September 15, 2026.

**Concrete reminder:** Calendar reminder set for September 15, 2026: *"Add V2 cascade case study to portfolio — the methodology doc is in V2_PROPOSAL.md, write the three-beat version."*
