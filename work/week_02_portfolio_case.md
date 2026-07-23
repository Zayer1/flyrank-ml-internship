### Voice Card
**"Direct, unapologetically technical, precise, zero fluff."**

### FlyRank Predictive Pipeline (In Progress)

**The Problem**
FlyRank currently uses static, handwritten `if/then` rules to identify which decaying web pages to refresh. This manual approach is accurate only 24% of the time, wasting human editorial hours. I was handed a raw dataset of 30,000 pages and tasked with proving that a machine learning model can beat that 24% baseline.

**What I Did**
I spent Week 2 defining the strict mathematical bounds of the problem before entering the data pipeline phase. I mapped the business need to a Supervised Scoring task and defined our unit of analysis (1 row = 1 page). I established a rigorous target threshold (>80% traffic growth, based on analyzing the top quartile of historical data) and locked our evaluation metric to Precision at Top K. **Additionally, I audited all 44 variables to build an engineering-grade Data Dictionary, mapping the domain logic and isolating toxic labels to prevent data leakage.**

**The Outcome (So Far)**
I transformed an unstructured business request into a clearly defined, executable machine learning task. We now know exactly what metric we are optimizing for, we have a deep understanding of the dataset's domain logic, and we have a baseline (24%) we have to beat during the upcoming training phase.

### The Before & After (Generic AI vs. Edited)

**Generic AI (The Before):**
*"I utilized results-driven data analysis to leverage key SEO metrics, empowering the content team to synergize their efforts and drive impactful growth."*

**My Voice (The After):**
*"I translated an ambiguous business problem into a strict Supervised Scoring task, auditing the dataset's domain logic and defining the exact target thresholds required to beat a 24% baseline."*
