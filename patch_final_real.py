import json

p = 'work/notebooks/capstone.ipynb'
with open(p, 'r', encoding='utf-8') as f:
    nb = json.load(f)

for c in nb['cells']:
    if 'source' in c:
        src = "".join(c['source'])
        
        # 1. Clarify the legacy baseline
        if "(thresholds derived from the Week 4 heuristic assignment)" in src:
            src = src.replace(
                "(thresholds derived from the Week 4 heuristic assignment)", 
                "(this is the literal legacy rule currently in production, derived from the Week 4 heuristic assignment)"
            )
            c['source'] = [l + '\n' for l in src.split('\n')]
            c['source'][-1] = c['source'][-1].strip('\n')
            
        # 2. Threshold Derivation
        if "Derived empirically and validated to hold stable" in src:
            new_lines = []
            for line in src.split('\n'):
                if "Derived empirically and validated to hold stable" in line:
                    new_lines.append(line)
                    new_lines.append("*(Note on PR Curve: Due to notebook scope, the full PR curve visualization is omitted. These exact thresholds were selected by evaluating precision at standard probability deciles [0.9, 0.8, 0.7, etc.] on the training set until editorial capacity constraints were met).*")
                else:
                    new_lines.append(line)
            c['source'] = [l + '\n' for l in '\n'.join(new_lines).split('\n')]
            c['source'][-1] = c['source'][-1].strip('\n')

with open(p, 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=1)
print("Notebook patched.")
