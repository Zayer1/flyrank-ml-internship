import json

with open('work/notebooks/capstone.ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)

with open('capstone_outputs.txt', 'w', encoding='utf-8') as out:
    for i, c in enumerate(nb['cells']):
        if c['cell_type'] == 'code' and c.get('outputs'):
            out.write(f'=== CELL {i} OUTPUTS ===\n')
            for o in c['outputs']:
                if o.get('text'):
                    out.write(''.join(o['text']))
                if o.get('data'):
                    for k, v in o['data'].items():
                        if 'text' in k:
                            out.write(''.join(v))
                out.write('\n')
            out.write('\n')

print('Done')
