Just wrapped up my Machine Learning Capstone project at FlyRank, and I'm thrilled to share the result: an AI-powered Predictive SEO Triage Agent.

At a high level, the system ingests URL traffic data and uses an XGBoost classifier (achieving 96% Precision@50) to predict which pages are mathematically guaranteed to lose SEO traffic, allowing content teams to intervene proactively.

But building the model was only half the battle. Here are two massive lessons I learned about applied, professional ML:

1. A model is not a product (The Design Decision) I quickly realized that handing a marketing team an array of raw probabilities is practically useless. I made the architectural decision to build a full FastAPI backend and integrate a LLaMA 3.1 generative proxy. The system now takes the raw XGBoost math and translates it into a human-readable, step-by-step action playbook. Packaging the ML into a tangible, marketable product was a huge leveling-up moment for me.

2. Acknowledging limitations honestly (The Cold-Start Problem) The V1 model is powerful, but it has a glaring limitation: "Zero-History Blindness." Because the strongest predictive feature relies on 30-day historical impressions, the model is functionally blind when evaluating brand new URLs. Instead of hiding this, I documented it rigorously and designed a V2 Zero-Shot Architecture Proposal (a model cascade utilizing a structural web crawler and a fine-tuned LoRA model) to solve it at scale. I would love any feedback from the senior engineering team on my V2 architecture proposal!

A huge thank you to the team at @FlyRank for providing an environment that values rigorous, honest engineering. I learned what it really takes to handle messy production data and build transparent ML systems.

📺 Check out the live demo video here: https://drive.google.com/file/d/1LSExa-aZnrJzGWZENp1QDAgoyPuh43Nn/view?usp=sharing
🔗 Read the full project & architecture here: https://zayer1.github.io/flyrank-ml-internship/

#MachineLearning #AI #DataScience #XGBoost #LLMs #Engineering #BuildInPublic
