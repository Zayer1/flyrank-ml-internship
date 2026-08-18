import json
import re

p = 'work/notebooks/capstone.ipynb'
with open(p, 'r', encoding='utf-8') as f:
    nb = json.load(f)

# 1. Insert Abstract as Cell 1
abstract_cell = {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Abstract\n",
    "\n",
    "This research analyzes the `content_refresh_anonymized.csv` dataset to construct an ML triage engine capable of predicting SEO traffic decay before it happens. By transitioning from legacy linear heuristics to a non-linear XGBoost classifier, we vastly improve the accuracy of prioritizing content for our editorial team. The model achieves robust performance across a 5-seed cross-client holdout validation, and is deployed as a live interactive web app for end-users."
   ]
}
nb['cells'].insert(1, abstract_cell)

# 2. Fix "the full release" in Data markdown (now at index 4)
for i, line in enumerate(nb['cells'][4]['source']):
    if "the full release" in line:
        nb['cells'][4]['source'][i] = line.replace("the full release", "the 30k-row anonymized starter slice")

# 3. Add EDA to Data code (now at index 5)
eda_code = """
print("Dataset Info:")
df.info()
print("\\nTrend Direction Balance:")
print(df['trend_direction'].value_counts(normalize=True))
"""
nb['cells'][5]['source'].append(eda_code)

# 4. Print DROP_FOR_TRAIN and label balance in Methodology code (now at index 7)
nb['cells'][7]['source'].insert(9, "print('Dropped features (to prevent leakage):', DROP_FOR_TRAIN)\n")
nb['cells'][7]['source'].insert(19, "print(f\"\\nTarget Label Balance (Train): {y_train.mean():.2%} declining\")\n")
nb['cells'][7]['source'].insert(20, "print(f\"Target Label Balance (Test): {y_test.mean():.2%} declining\\n\")\n")

# 5. Update Cell 8 markdown (Results) for semantic accuracy
for i, line in enumerate(nb['cells'][8]['source']):
    if "5-fold cross-validation" in line:
        nb['cells'][8]['source'][i] = line.replace("5-fold cross-validation", "5-seed GroupShuffleSplit validation")

# 6. Fix GridSearchCV Leakage in Cell 9
cell9_src = "".join(nb['cells'][9]['source'])
cell9_src = cell9_src.replace(
    "from sklearn.model_selection import GridSearchCV, GroupShuffleSplit",
    "from sklearn.model_selection import GridSearchCV, GroupShuffleSplit, GroupKFold"
)
cell9_src = cell9_src.replace(
    "grid = GridSearchCV(\n    estimator=xgb.XGBClassifier(random_state=42, enable_categorical=True),\n    param_grid=param_grid, scoring='average_precision', cv=2\n)",
    "grid = GridSearchCV(\n    estimator=xgb.XGBClassifier(random_state=42, enable_categorical=True),\n    param_grid=param_grid, scoring='average_precision', \n    cv=GroupKFold(n_splits=2).split(X_train, y_train, groups=train_df['client_id'])\n)"
)
nb['cells'][9]['source'] = [line + '\n' for line in cell9_src.split('\n')]
nb['cells'][9]['source'][-1] = nb['cells'][9]['source'][-1].strip('\n')

# 7. Restore Section 5 Limitations markdown (at index 10)
limitations_md = """## 5. Limitations

*What this work cannot claim.*

- **Heavy Feature Dependency:** The model relies heavily on `impressions_prev_30d` and other traffic shapes, meaning entirely new URLs without 30 days of history cannot be accurately scored.
- **Label Definition Flaws:** The label `trend_direction == 'down'` is a binary proxy. As discovered in Week 6, binary proxy labels can sometimes mask the true magnitude of decay, leading to edge cases where slow-burn decay is missed."""
nb['cells'][10] = {
    "cell_type": "markdown",
    "metadata": {},
    "source": [line + '\n' for line in limitations_md.split('\n')]
}
nb['cells'][10]['source'][-1] = nb['cells'][10]['source'][-1].strip('\n')

# 8. Add Playbook thresholds explanation (at index 12, Recommendations markdown)
nb['cells'][12]['source'].append("\n\n*Note: The probability thresholds below (0.7 and 0.4) were derived empirically from observing precision-recall tradeoffs on the training set, balancing editorial capacity against the risk of traffic loss.*")

# 9. Add Web App screenshot/link to Artifacts markdown (at index 14)
nb['cells'][14]['source'].append("\n\n**Deployed Application:**\n[Launch the Live Web App & LLaMA Copilot](https://zayer1.github.io/flyrank-ml-internship/)")

with open(p, 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=1)


# Update build_paper.py to parse the abstract
with open('build_paper.py', 'r', encoding='utf-8') as f:
    bp = f.read()

bp = bp.replace(
    "html_content = html_content.replace('<h2>1. Question</h2>', '<h2 id=\"sec-1\">1. Question</h2>')",
    "html_content = html_content.replace('<h2>Abstract</h2>', '<h2 id=\"abstract\">Abstract</h2>')\nhtml_content = html_content.replace('<h2>1. Question</h2>', '<h2 id=\"sec-1\">1. Question</h2>')"
)
bp = bp.replace(
    "new_toc = \"\"\"\n                <ul>\n                    <li><a href=\"#sec-1\">1. Question</a></li>",
    "new_toc = \"\"\"\n                <ul>\n                    <li><a href=\"#abstract\">Abstract</a></li>\n                    <li><a href=\"#sec-1\">1. Question</a></li>"
)

with open('build_paper.py', 'w', encoding='utf-8') as f:
    f.write(bp)

print("Refactor complete.")
