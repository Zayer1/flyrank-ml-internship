import json
nb = json.load(open('work/notebooks/capstone.ipynb', encoding='utf-8'))
for i, c in enumerate(nb['cells']):
    src = "".join(c.get("source", []))[:60].replace("\n", "\\n")
    print(f"{i}: {c.get('cell_type')} - {src}")
