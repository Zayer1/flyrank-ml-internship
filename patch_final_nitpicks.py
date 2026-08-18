import json
import re

p = 'work/notebooks/capstone.ipynb'
with open(p, 'r', encoding='utf-8') as f:
    nb = json.load(f)

for c in nb['cells']:
    if 'source' in c:
        src = "".join(c['source'])
        
        # 1. Fix the provider_used limitation
        if "Missingness Exploitation:" in src and "provider_used" in src:
            # We will just replace the whole cell's source by rebuilding it line by line
            new_lines = []
            for line in src.split('\n'):
                if "Missingness Exploitation:" in line and "provider_used" in line:
                    new_lines.append("- **Missingness Exploitation Checked:** Earlier iterations of this model showed `provider_used` (71% missing) as a top feature, raising concerns that XGBoost was exploiting its missingness pattern. To prevent this, we explicitly moved `provider_used`, `model_used`, and the potentially leaky `position_tier` to the `DROP_FOR_TRAIN` exclusion list. The model never sees them, yet still achieves 96.0% P@50, proving the core behavioral signal is robust.")
                else:
                    new_lines.append(line)
            
            # Rejoin and fix trailing newline
            src_new = '\n'.join(new_lines)
            c['source'] = [l + '\n' for l in src_new.split('\n')]
            c['source'][-1] = c['source'][-1].strip('\n')
            
        # 2. Add the LogReg dimensionality note
        if "Logistic Regression baseline" in src and "Zero-imputed" in src:
            # It's in Section 4 Results.
            if "dummy-variable dimensionality" not in src:
                # Find the sentence and append to it
                new_lines = []
                for line in src.split('\n'):
                    if "Logistic Regression baseline" in line:
                        new_lines.append(line + " *(Note: Giving LogReg the full one-hot encoded categorical feature set dropped its P@50 from an earlier 58.8% to 46.8%, likely due to the added dummy-variable dimensionality without retuning regularization).*")
                    else:
                        new_lines.append(line)
                
                src_new = '\n'.join(new_lines)
                c['source'] = [l + '\n' for l in src_new.split('\n')]
                c['source'][-1] = c['source'][-1].strip('\n')

with open(p, 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=1)
print("Notebook patched.")
