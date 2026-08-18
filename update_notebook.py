import json

notebook_path = 'work/notebooks/capstone.ipynb'

with open(notebook_path, 'r', encoding='utf-8') as f:
    nb = json.load(f)

for cell in nb['cells']:
    if cell['cell_type'] == 'markdown':
        source = "".join(cell['source'])
        
        if "5. Limitations" in source and "impressions_prev_30d" not in source:
            source = source.replace(
                "weights overnight.", 
                "weights overnight.\n\n- **Heavy Feature Dependency:** The model relies heavily on `impressions_prev_30d` and other traffic shapes, meaning entirely new URLs without 30 days of history cannot be accurately scored.\n- **Label Definition Flaws:** The label `trend_direction == 'down'` is a binary proxy. As discovered in Week 6, binary proxy labels can sometimes mask the true magnitude of decay, leading to edge cases where slow-burn decay is missed."
            )
            # Reconstruct list of lines for Jupyter format
            cell['source'] = [line + ('\n' if i < len(source.split('\n')) - 1 else '') for i, line in enumerate(source.split('\n'))]

with open(notebook_path, 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=1)

print("Notebook updated successfully.")
