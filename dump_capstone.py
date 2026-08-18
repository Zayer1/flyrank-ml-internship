import json
import sys

with open('work/notebooks/capstone.ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)

with open('capstone_dump_utf8.txt', 'w', encoding='utf-8') as out:
    for i, c in enumerate(nb['cells']):
        ct = c['cell_type']
        out.write(f'=== CELL {i} ({ct}) ===\n')
        out.write(''.join(c['source']))
        out.write('\n\n')

print(f'Done: {len(nb["cells"])} cells')
