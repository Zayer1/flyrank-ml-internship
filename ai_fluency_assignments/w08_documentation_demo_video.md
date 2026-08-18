# Week 8+ Deliverable: Documentation and Demo Video

## Demo Video

**Platform:** Loom (free tier, public link)  
**Duration:** ~4 minutes  
**Link:** `https://zayer1.github.io/portfolio/` → "Watch the Demo" button on the capstone project page

The video walks through the live portfolio and the XGBoost prediction demo end-to-end. No slides. No screen effects. Just a real screen recording of a real working system.

---

## Video Structure (Script Reference)

**[0:00 – 0:30] Open the portfolio home page**  
Show the hero claim landing in under ten seconds. Scroll to the FlyRank case study card. Click through to the project detail page.

**[0:30 – 1:30] Walk the case study methodology**  
Highlight the metrics table (XGBoost vs heuristic baseline). Point to the `GroupShuffleSplit` explanation and why it matters. Show the Precision-Recall curve and explain it in plain language: "The further this curve stays toward the top-right corner, the more accurate the model is across all operating thresholds."

**[1:30 – 2:30] Run the live prediction demo**  
Enter realistic input values. Click Run Prediction. Wait for the response (note the cold-start disclaimer in the UI). Show the risk tier result and the probability float.

**[2:30 – 3:30] Show the codebase briefly**  
Open the GitHub repository in a browser tab. Scroll to the `src/api/main.py` FastAPI file. Show the Pydantic input schema and the `predict_proba()` call — this is the part that proves the model is real, not mocked.

**[3:30 – 4:00] Close with the next step**  
Mention the V2 LLaMA-3 Cascade as the next case study, target date September 15, 2026.

---

## Documentation

Full written documentation for the capstone system lives in the GitHub repository:

| Document | Location | Purpose |
|----------|----------|---------|
| `README.md` | Repo root | System overview, quickstart, local setup |
| `V2_PROPOSAL.md` | Repo root | Architecture proposal for the LLaMA-3 cascade extension |
| `w05_model.ipynb` | `work/notebooks/` | Full training pipeline with inline methodology comments |
| `src/api/main.py` | `src/api/` | FastAPI backend with request validation and inference logic |
| `ai_fluency_assignments/` | Repo root | All AI Fluency deliverables, one file per assignment |

The README includes a "How to Run Locally" section with exact commands so any reviewer can spin up the full system without guesswork.
