import json

p = 'work/notebooks/capstone.ipynb'
with open(p, 'r', encoding='utf-8') as f:
    nb = json.load(f)

for c in nb['cells']:
    if 'source' in c:
        src = "".join(c['source'])
        if "~1,650 declining pages per test split" in src:
            src = src.replace("~1,650 declining pages per test split", "2,000-3,800 declining pages depending on the random split")
            c['source'] = [line + '\n' for line in src.split('\n')]
            c['source'][-1] = c['source'][-1].strip('\n')

with open(p, 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=1)
print("Notebook patched.")
