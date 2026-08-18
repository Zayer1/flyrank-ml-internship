import json

p = 'work/notebooks/capstone.ipynb'
with open(p, 'r', encoding='utf-8') as f:
    nb = json.load(f)

for c in nb['cells']:
    if 'source' in c:
        src = "".join(c['source'])
        
        # 1. Update the Non-Linear Advantage / LogReg comparison
        if "The Non-Linear Advantage:" in src:
            new_lines = []
            for line in src.split('\n'):
                if "The Non-Linear Advantage:" in line:
                    # Rewrite the paragraph slightly to incorporate the fair baseline test
                    new_lines.append("**The Non-Linear Advantage & Imputation Asymmetry:** XGBoost outperforms the Logistic Regression baseline by a staggering ~48 points. To ensure this wasn't simply an artifact of how XGBoost natively routes missing values, we tested a \"fair\" LogReg pipeline equipped with median imputation and one-hot encoding for categorical features. The fair LogReg pipeline achieved a P@50 of 47.60% (±14.39%). The massive remaining gap confirms that SEO decay is highly non-linear and interactive. A linear model might learn \"high traffic = decay\", but XGBoost learns the intersection: a 2-day-old article with massive traffic is a viral spike destined to crash, whereas a 3-year-old article with massive traffic is a stable evergreen pillar.")
                else:
                    new_lines.append(line)
            src_new = '\n'.join(new_lines)
            c['source'] = [l + '\n' for l in src_new.split('\n')]
            c['source'][-1] = c['source'][-1].strip('\n')
            
        # 2. Section 7 Deployment note
        if "## 7. Artifacts" in src:
            if "Deployment Architecture Note" not in src:
                src += "\n\n*Deployment Architecture Note: The GitHub Pages link serves a static frontend UI prototype. The FastAPI/LLaMA 3.1 backend service must be run locally to process predictions and generate Playbook actions.*"
                c['source'] = [l + '\n' for l in src.split('\n')]
                c['source'][-1] = c['source'][-1].strip('\n')

with open(p, 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=1)
print("Notebook patched.")
