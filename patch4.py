import json

p = 'work/notebooks/capstone.ipynb'
with open(p, 'r', encoding='utf-8') as f:
    nb = json.load(f)

# Cell 10 (importances) is at index 10
cell10_src = """importances = pd.DataFrame({
    'feature': X_train.columns,
    'importance': final_model.feature_importances_
}).sort_values('importance', ascending=False)
print("Top Honest Feature Importances:")
print(importances.head(5))"""

nb['cells'][10]['source'] = [line + '\n' for line in cell10_src.split('\n')]
nb['cells'][10]['source'][-1] = nb['cells'][10]['source'][-1].strip('\n')

with open(p, 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=1)
