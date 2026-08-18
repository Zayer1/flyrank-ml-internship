import json

p = 'work/notebooks/capstone.ipynb'
with open(p, 'r', encoding='utf-8') as f:
    nb = json.load(f)

def replace_in_notebook(old_str, new_str, cell_hint=None):
    for c in nb['cells']:
        if 'source' in c:
            src = "".join(c['source'])
            if cell_hint and cell_hint not in src:
                continue
            if old_str in src:
                src = src.replace(old_str, new_str)
                c['source'] = [line + '\n' for line in src.split('\n')]
                c['source'][-1] = c['source'][-1].strip('\n')

# 1. Fix Section 5 (Limitations) provider_used contradiction
replace_in_notebook(
    "- **Missingness Exploitation Checked:** The `provider_used` feature is 71% missing, but is a top-5 important feature. We also noted that `position_tier` could be a binned duplicate of `avg_position`. To test this, we explicitly ran a 5-fold ablation study dropping `provider_used`, `model_used`, and `position_tier` entirely. The XGBoost P@50 barely moved (dropping from 97.6% to 96.0%), which tells us the model is not relying on missingness artifacts to achieve its performance.",
    "- **Missingness Exploitation Checked:** Earlier iterations of this model showed `provider_used` (71% missing) as a top feature, raising concerns that XGBoost was exploiting its missingness pattern. To prevent this, we explicitly moved `provider_used`, `model_used`, and the potentially leaky `position_tier` to the `DROP_FOR_TRAIN` exclusion list. The model never sees them, yet still achieves 96.0% P@50, proving the core behavioral signal is robust."
)

# 2. Section 6 Compound Urgent rule
replace_in_notebook(
    "| **> 0.70** | Urgent Refresh | ~97% |",
    "| **> 0.70 & Vol > 100** | Urgent Refresh | ~81% |"
)
replace_in_notebook(
    "| **> 0.40** | Standard Review | ~85% |",
    "| **> 0.40 & Vol <= 100** | Standard Review | ~62% |"
)
replace_in_notebook(
    "*(Derived empirically from training set Precision-Recall tradeoffs)*",
    "*(Derived empirically from the test set evaluating the compound playbook rules)*"
)

# 3. Dial back Employer Summary language
replace_in_notebook(
    "**1. Proved a clear lift over legacy heuristics**",
    "**1. Measured a clear directional lift over legacy heuristics**"
)
replace_in_notebook(
    "**2. Prevented cross-domain leakage**",
    "**2. Controlled for cross-domain leakage**"
)
replace_in_notebook(
    "By grouping holdouts strictly by `client_id`, we eliminated the risk of the model memorizing a client's specific baseline traffic. The 96.0% Precision@50 score is an honest evaluation of the model's ability to generalize to completely unseen web properties.",
    "By grouping holdouts strictly by `client_id`, we minimized the risk of the model memorizing a client's specific baseline traffic, providing a more honest evaluation of the model's ability to generalize to completely unseen web properties."
)
replace_in_notebook(
    "The model successfully identifies decaying content earlier than legacy heuristic models.",
    "The model successfully identifies content structurally at risk of decay with high precision."
)
replace_in_notebook(
    "predicting SEO traffic decay before it happens",
    "identifying early signals of SEO traffic decay"
)

# 4. Section 2 Seasonality/Missingness
replace_in_notebook(
    "We also note several retained features exhibit high missingness: `provider_used` (71% NaN), `word_count` (26% NaN), and `search_volume` (8% NaN).",
    "We also note several features exhibit high missingness: `provider_used` (71% NaN), `word_count` (26% NaN), and `search_volume` (8% NaN). Furthermore, this dataset is a snapshot from a single month (March 2026), meaning macro seasonality is not captured in the training data."
)

# 5. Section 4 LogReg Tuning / CV Split
replace_in_notebook(
    "Feature-equivalent Logistic Regression",
    "Logistic Regression baseline (Zero-imputed)"
)
replace_in_notebook(
    "We use nested Cross-Validation.",
    "We use nested Cross-Validation. *Note: the inner loop uses `GroupKFold(n_splits=2)` which is a thin CV given the client count, and is a known source of noise in hyperparameter selection.*"
)

# 6. Additional Limitations (79M row & Groq Leak)
limitation_addition = """
- **Sample Size vs Warehouse:** This model was trained on a 30,000-row sample, whereas the full production data warehouse contains ~79M rows. The extreme P@50 lift observed here may compress or revert to the mean when scaled to the full dataset.
- **Third-Party AI Data Leaks:** The Action Playbook currently passes parsed DataFrame contents to the Groq LLaMA 3.1 Copilot. In production, feeding non-anonymized client traffic data into external AI APIs is a strict violation of data privacy policies. A localized LLM or strict PII redaction layer is required before full deployment.
"""
replace_in_notebook(
    "### Missingness",  # Just to find a place to insert in Section 5
    limitation_addition + "\n### Missingness",
    cell_hint="## 5. Limitations"
)
# If the above didn't match because ### Missingness wasn't there, let's just append to the cell.
for c in nb['cells']:
    if 'source' in c and "## 5. Limitations" in "".join(c['source']):
        src = "".join(c['source'])
        if "Sample Size vs Warehouse" not in src:
            src += "\n" + limitation_addition
            c['source'] = [line + '\n' for line in src.split('\n')]
            c['source'][-1] = c['source'][-1].strip('\n')

with open(p, 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=1)
print("Notebook patched.")
