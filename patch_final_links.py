import json

p = 'work/notebooks/capstone.ipynb'
with open(p, 'r', encoding='utf-8') as f:
    nb = json.load(f)

for c in nb['cells']:
    if 'source' in c:
        src = "".join(c['source'])
        
        if "Deployment Architecture Note:" in src:
            new_lines = []
            for line in src.split('\n'):
                if "Deployment Architecture Note:" in line:
                    # Replace the existing architecture note with a slightly expanded one containing repo links
                    new_lines.append("*Deployment Architecture Note: The live GitHub Pages deployment serves a static frontend UI prototype (source: `docs/index.html`, `docs/app.js`). The companion backend—which uses FastAPI to serve the XGBoost predictions and LLaMA 3.1 for summarization—is designed to be run locally (source: `api/server.py`). The ML model artifacts are stored in `api/artifacts/`.*")
                else:
                    new_lines.append(line)
            src_new = '\n'.join(new_lines)
            c['source'] = [l + '\n' for l in src_new.split('\n')]
            c['source'][-1] = c['source'][-1].strip('\n')

with open(p, 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=1)
print("Notebook patched.")
