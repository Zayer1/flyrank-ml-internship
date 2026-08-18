import json

p = 'work/notebooks/capstone.ipynb'
with open(p, 'r', encoding='utf-8') as f:
    nb = json.load(f)

src = ''.join(nb['cells'][9]['source'])
src += "\n- **Evaluation Variance:** The headline evaluation metrics are derived from a single `GroupShuffleSplit` on 7 held-out clients. While sufficient to prove superiority over the heuristic baseline, k-fold cross-validation would be required to rule out sensitivity to this specific test split."
src += "\n- **Action Granularity Loss:** For operational simplicity, truly dead pages (zero traffic) and stable low-probability pages were collapsed into a single \"Stable / No Action\" label. This intentionally trades analytical granularity for workflow simplicity."

lines = [line + '\n' for line in src.split('\n')]
lines[-1] = lines[-1].strip('\n')

nb['cells'][9]['source'] = lines

with open(p, 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=1)
