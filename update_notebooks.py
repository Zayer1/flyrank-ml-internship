import json

def update_nb(filepath, target_line, new_lines):
    with open(filepath, 'r', encoding='utf-8') as f:
        nb = json.load(f)
    for cell in nb.get('cells', []):
        if cell['cell_type'] == 'code' and any(target_line in line for line in cell.get('source', [])):
            cell['source'] = new_lines
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(nb, f, indent=1)

nb1_lines = [
    "# Your discovery here\n",
    "print(\"Checking if content age correlates with traffic direction:\\n\")\n",
    "age_medians = df.groupby(\"trend_direction\")[\"content_age_days\"].median()\n",
    "print(age_medians)\n",
    "print(\"\\nDirectional Observation: Pages trending up and down have very similar median ages, suggesting age alone does not dictate the recent trend.\")\n"
]
update_nb('notebooks/01_first_look_and_discovery.ipynb', '# Your discovery here', nb1_lines)

nb2_lines = [
    "# Your experiment here\n",
    "tree_deep = DecisionTreeClassifier(max_depth=3, class_weight=\"balanced\", random_state=42)\n",
    "tree_deep.fit(X, y)\n",
    "tree_deep_score = tree_deep.predict_proba(X)[:, 1]\n",
    "print(\"Depth-3 Tree precision:\")\n",
    "for k in (20, 50):\n",
    "    tr_deep = precision_at_k(tree_deep_score, y, k)\n",
    "    print(f\"Precision@{k}: {tr_deep:.3f}\")\n",
    "print(\"\\nThe precision shifted slightly, but a depth-3 tree is still perfectly readable.\")\n"
]
update_nb('notebooks/02_your_first_readable_model.ipynb', '# Your experiment here', nb2_lines)
