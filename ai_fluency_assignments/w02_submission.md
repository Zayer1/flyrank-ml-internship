# Week 2 Deliverable: Frame It as Cases

## The FlyRank ML Capstone — Three-Beat Case Study

---

### Beat 1: The Problem

SEO teams at growth companies spend hours each week manually triaging hundreds of web pages to guess which ones are at risk of losing traffic. The heuristics they use — things like "pages not updated in 6 months are risky" or "pages with fewer than 500 words decay faster" — are based on intuition and are not validated against historical data.

There is no probability signal. They cannot tell you *how likely* a page is to decay, only that it *might* based on a gut-feel rule. The result is wasted content budget spent refreshing pages that were never at risk, while genuinely decaying pages slip through the cracks.

**The specific claim I was testing:** Can a supervised ML model, trained on historical traffic and content metadata, produce a more accurate decay probability than a simple heuristic threshold — and can that model be deployed in a way that a non-technical editor can actually use?

---

### Beat 2: The Work

I trained an XGBoost probability classifier on the FlyRank anonymized content refresh dataset (~30,000 rows of real page metadata and traffic history).

The critical engineering decisions:
- **Label Definition:** A page was labeled as "decaying" if it lost >15% organic traffic over the next 90-day window after the observation snapshot.
- **Leakage Prevention:** I used `GroupShuffleSplit` with `groups=client_id` to ensure no client's pages appeared in both the training and test sets. This prevents the model from memorizing client-specific traffic patterns that it would never see on a new client.
- **Evaluation Metrics:** Standard accuracy is useless here because decaying pages are rare (class imbalance). I used Precision@50 (the precision of the top 50 highest-risk predictions) and Global Recall (what fraction of all truly decaying pages we caught) — the same metrics the Week 4 heuristic baseline was evaluated on.
- **Deployment:** I wrapped the trained XGBoost model in a FastAPI server with `slowapi` rate-limiting (100 requests/hour) and `X-API-Key` authentication, deployed on Render's free tier.

---

### Beat 3: The Proof

The XGBoost classifier outperformed the heuristic baseline on both evaluation metrics on the same held-out test split:

| Metric | Heuristic Baseline | XGBoost Model |
|--------|-------------------|---------------|
| Precision@50 | ~0.44 | ~0.71 |
| Global Recall | ~0.38 | ~0.62 |

The model's feature importance analysis confirmed that recency signals (days since last update) and engagement signals (scroll depth, return visits) drove the most predictive power — validating that the heuristic intuition was pointing at the right signals, but thresholding them too crudely.

The live prediction form at `https://zayer1.github.io/flyrank-ml-internship` allows any user to input page metrics and receive a real-time decay probability from the model in under 2 seconds on a warm server.
