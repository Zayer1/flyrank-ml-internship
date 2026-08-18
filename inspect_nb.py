import json
nb = json.load(open('work/notebooks/capstone.ipynb', encoding='utf-8'))
for i, c in enumerate(nb['cells']):
    source = c['source']
    first_line = source[0][:60].strip() if source else ""
    print(f"{i}: {c['cell_type']} - {first_line}")
