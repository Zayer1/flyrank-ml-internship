import json
import subprocess

notebook_path = 'work/notebooks/capstone.ipynb'

with open(notebook_path, 'r', encoding='utf-8') as f:
    nb = json.load(f)

for cell in nb['cells']:
    if cell['cell_type'] == 'markdown':
        source = "".join(cell['source'])
        
        if "6. Ranked recommendations" in source:
            if "Playbook:\n1." in source:
                source = source.replace("Playbook:\n1.", "Playbook:\n\n1.")
            if "Playbook:\r\n1." in source:
                source = source.replace("Playbook:\r\n1.", "Playbook:\n\n1.")
            
            # Reconstruct list of lines
            cell['source'] = [line + ('\n' if i < len(source.split('\n')) - 1 else '') for i, line in enumerate(source.split('\n'))]

with open(notebook_path, 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=1)

print("Notebook updated.")
