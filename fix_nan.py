import json

p = 'work/notebooks/capstone.ipynb'
with open(p, 'r', encoding='utf-8') as f:
    nb = json.load(f)

c9 = "".join(nb['cells'][9]['source'])
c9 = c9.replace(
"""    preprocessor = ColumnTransformer(
        transformers=[
            ('num', StandardScaler(), num_cols),
            ('cat', OneHotEncoder(handle_unknown='ignore'), cat_cols_pl)
        ])""",
"""    from sklearn.impute import SimpleImputer
    num_pipe = Pipeline([('imputer', SimpleImputer(strategy='constant', fill_value=0)), ('scaler', StandardScaler())])
    cat_pipe = Pipeline([('imputer', SimpleImputer(strategy='most_frequent')), ('ohe', OneHotEncoder(handle_unknown='ignore'))])
    
    preprocessor = ColumnTransformer(
        transformers=[
            ('num', num_pipe, num_cols),
            ('cat', cat_pipe, cat_cols_pl)
        ])"""
)

nb['cells'][9]['source'] = [line + '\n' for line in c9.split('\n')]
nb['cells'][9]['source'][-1] = nb['cells'][9]['source'][-1].strip('\n')

with open(p, 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=1)
