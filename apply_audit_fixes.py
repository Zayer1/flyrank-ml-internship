import json
import re

notebook_path = 'work/notebooks/capstone.ipynb'
nb = json.load(open(notebook_path, 'r', encoding='utf-8'))

# Cell 1: Keep question as is, we will implement the 365 day filter in code.

# Cell 3: Data markdown
for i, cell in enumerate(nb['cells']):
    if cell['cell_type'] == 'markdown' and "## 2. Data" in "".join(cell['source']):
        source = "".join(cell['source'])
        source = source.replace(
            "We excluded rows where `ga4_data_available` or `gsc_data_available` were false to avoid structural zeros.",
            "We focused strictly on the core features present in the dataset."
        )
        cell['source'] = [line + '\n' for line in source.split('\n')]
        cell['source'][-1] = cell['source'][-1].strip('\n')

# Cell 4: Code for Data
for i, cell in enumerate(nb['cells']):
    if cell['cell_type'] == 'code' and "import pandas" in "".join(cell['source']):
        code = """import pandas as pd
df = pd.read_csv('data/raw/content_refresh_anonymized.csv')
# Enforce mature content filter as defined in research question
df = df[df['content_age_days'] > 365].copy()"""
        cell['source'] = [line + '\n' for line in code.split('\n')]
        cell['source'][-1] = cell['source'][-1].strip('\n')

# Cell 8: Baseline threshold
for i, cell in enumerate(nb['cells']):
    if cell['cell_type'] == 'code' and "baseline_stale" in "".join(cell['source']):
        source = "".join(cell['source'])
        source = source.replace("days_since_last_update >= 180", "days_since_last_update >= 104")
        cell['source'] = [line + '\n' for line in source.split('\n')]
        cell['source'][-1] = cell['source'][-1].strip('\n')

# Cell 11: Playbook markdown
for i, cell in enumerate(nb['cells']):
    if cell['cell_type'] == 'markdown' and "## 6. Recommendations" in "".join(cell['source']):
        source = """## 6. Ranked recommendations

The output of the model feeds a discrete Action Playbook incorporating W07 ROI logic:

1. **Urgent Refresh:** (Prob > 0.7 AND Search Volume > 100). High probability of decay with actual traffic value worth saving.
2. **Standard Review:** (Prob > 0.4). Queue for regular audit.
3. **Basement Trap:** (Impressions Prev 30d == 0 OR Prob < 0.4). Content is either permanently stabilized, or mathematically cannot drop further (zero traffic)."""
        cell['source'] = [line + '\n' for line in source.split('\n')]
        cell['source'][-1] = cell['source'][-1].strip('\n')

# Cell 12: Playbook code
for i, cell in enumerate(nb['cells']):
    if cell['cell_type'] == 'code' and "def assign_action(" in "".join(cell['source']):
        code = """def assign_action(row):
    prob = row['decay_prob']
    impressions = row['impressions_prev_30d']
    search_volume = row['search_volume']
    
    if impressions == 0:
        return 'Basement Trap'
    elif prob > 0.7 and search_volume > 100:
        return 'Urgent Refresh'
    elif prob > 0.4:
        return 'Standard Review'
    else:
        return 'Basement Trap'

# Apply the action logic
# Assuming we have a dataframe `test_df` with the model predictions
if 'decay_prob' in test_df.columns:
    test_df['Action'] = test_df.apply(assign_action, axis=1)
"""
        cell['source'] = [line + '\n' for line in code.split('\n')]
        cell['source'][-1] = cell['source'][-1].strip('\n')

# Cell 14: Section 7 Output Code
for i, cell in enumerate(nb['cells']):
    if cell['cell_type'] == 'code' and "".join(cell['source']).strip() == "pass" and i == 14:
        code = """import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(10, 6))
sns.histplot(test_df['decay_prob'], bins=50, kde=True, color='skyblue')
plt.title('Distribution of XGBoost Decay Probabilities (Test Set)')
plt.xlabel('Probability of Decay')
plt.ylabel('URL Count')
plt.axvline(x=0.7, color='red', linestyle='--', label='Urgent Threshold')
plt.legend()
plt.tight_layout()
plt.savefig('docs/prob_dist.png')
plt.show()"""
        cell['source'] = [line + '\n' for line in code.split('\n')]
        cell['source'][-1] = cell['source'][-1].strip('\n')

# Cell 16: Social Post fix
for i, cell in enumerate(nb['cells']):
    if cell['cell_type'] == 'markdown' and "9. ML-12 Deliverables" in "".join(cell['source']):
        source = "".join(cell['source'])
        source = source.replace("5. Call to Action: Deploying this saves 40 hours a week.", "5. Call to Action: ML Triaging drastically improves Precision@50 over legacy rules.")
        cell['source'] = [line + '\n' for line in source.split('\n')]
        cell['source'][-1] = cell['source'][-1].strip('\n')


with open(notebook_path, 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=1)

print("Applied audit fixes to notebook.")
