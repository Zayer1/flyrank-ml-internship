import json

p = 'work/notebooks/capstone.ipynb'
with open(p, 'r', encoding='utf-8') as f:
    nb = json.load(f)

for i, line in enumerate(nb['cells'][7]['source']):
    if "y_train.mean()" in line:
        nb['cells'][7]['source'][i] = line.replace("y_train.mean()", "train_df[TARGET].mean()")
    if "y_test.mean()" in line:
        nb['cells'][7]['source'][i] = line.replace("y_test.mean()", "test_df[TARGET].mean()")

with open(p, 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=1)
