import json

p = 'work/notebooks/capstone.ipynb'
with open(p, 'r', encoding='utf-8') as f:
    nb = json.load(f)

# The content in Cell 14 currently
c14_src = "".join(nb['cells'][14]['source'])

thresh_code = """
print("\\n=== THRESHOLD VALIDATION ===")
y_test_pred_70 = (y_prob >= 0.70).astype(int)
y_test_pred_40 = (y_prob >= 0.40).astype(int)
from sklearn.metrics import precision_score
p70 = precision_score(y_test, y_test_pred_70, zero_division=0)
p40 = precision_score(y_test, y_test_pred_40, zero_division=0)
print(f"Empirical Precision at >0.70 (Urgent): {p70:.2%}")
print(f"Empirical Precision at >0.40 (Standard): {p40:.2%}")
"""

# 1. Clean up Cell 14 (Artifacts Markdown)
md_only = c14_src.replace(thresh_code, "")
# there might be a leading newline left over from the injection
if md_only.startswith("\n"):
    md_only = md_only[1:]

nb['cells'][14]['source'] = [line + '\n' for line in md_only.split('\n')]
if nb['cells'][14]['source']:
    nb['cells'][14]['source'][-1] = nb['cells'][14]['source'][-1].strip('\n')

# 2. Append threshold code to Cell 13 (Playbook Code)
c13_src = "".join(nb['cells'][13]['source'])
c13_src += "\n" + thresh_code.strip('\n')

nb['cells'][13]['source'] = [line + '\n' for line in c13_src.split('\n')]
nb['cells'][13]['source'][-1] = nb['cells'][13]['source'][-1].strip('\n')

# 3. Tone down marketing copy in Cell 17 (Demo Outline)
c17_src = "".join(nb['cells'][17]['source'])
c17_src = c17_src.replace("drastically improves", "improves")
c17_src = c17_src.replace("massive lift", "clear lift")
c17_src = c17_src.replace("eliminated cross-domain leakage", "prevented cross-domain leakage")
c17_src = c17_src.replace("robust GroupShuffleSplit", "repeated random holdout")
c17_src = c17_src.replace("significantly earlier", "earlier")

nb['cells'][17]['source'] = [line + '\n' for line in c17_src.split('\n')]
nb['cells'][17]['source'][-1] = nb['cells'][17]['source'][-1].strip('\n')

with open(p, 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=1)
