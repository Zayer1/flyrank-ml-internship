# Week 1 Deliverable: What Are You Proving?

## Proof Statement

I am proving that I can design and deploy a production-grade Machine Learning system — not just train a model in a notebook and call it done.

My capstone is an end-to-end XGBoost classifier that predicts SEO traffic decay probability across thousands of pages, trained on real anonymized data with rigorous leakage controls (`GroupShuffleSplit` on `client_id`), evaluated on hard metrics (Precision@50 and Global Recall) against a manually-crafted heuristic baseline, and deployed as a live, rate-limited FastAPI service behind an authenticated endpoint. The interactive frontend lets a non-technical stakeholder run real-time inference on any set of page metrics without touching a line of Python.

**Who this is for:** ML engineering leads and technical hiring managers at growth-stage companies who need engineers that can own the full loop — not just the Jupyter notebook, but the API, the evaluation framework, and the shipped product.

**The one action:** Open the GitHub repository, read the methodology, and run the live demo themselves.

**Why a CV can't prove this:** A CV can claim "built ML models" — anyone can write that. This proof exists at a live URL, produces real predictions from a real model, and includes a methodology section that shows exactly how I prevented data leakage, why I chose my evaluation metrics, and where the model still fails. You cannot fake that with bullet points.
