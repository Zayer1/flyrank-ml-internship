import json

p = 'work/notebooks/capstone.ipynb'
with open(p, 'r', encoding='utf-8') as f:
    nb = json.load(f)

src = """## 6. Ranked recommendations

*The action playbook output — the paper's recommendations section.*

The output of the model feeds a discrete Action Playbook:

1. **Urgent Refresh:** (Prob > 0.7 AND Search Volume > 100) Immediate content update required for high-value targets.
2. **Standard Review:** (Prob > 0.4) Queue for regular audit (includes high-probability pages with low search volume).
3. **Stable / No Action:** Zero-traffic content or stable low-probability content (Prob <= 0.4)."""

lines = [line + '\n' for line in src.split('\n')]
lines[-1] = lines[-1].strip('\n')

nb['cells'][11]['source'] = lines

with open(p, 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=1)
