import json

p = 'work/notebooks/capstone.ipynb'
with open(p, 'r', encoding='utf-8') as f:
    nb = json.load(f)

# Patch Cell 6 (Index 5 because cells are 0-indexed in array)
cell6_source = """# Create target label before dropping its source
df['is_declining_label'] = (df['trend_direction'] == 'down').astype(int)
TARGET = 'is_declining_label'

# Drop leaky features and outcome-window metrics to prevent time-travel leakage
import json
with open('../../config.json', 'r') as f:
    config = json.load(f)
DROP_FOR_TRAIN = config.get("DROP_FOR_TRAIN", [])
if TARGET not in DROP_FOR_TRAIN:
    DROP_FOR_TRAIN.append(TARGET)

# Split into train/test grouping by client_id
gss = GroupShuffleSplit(n_splits=1, test_size=0.2, random_state=42)
train_idx, test_idx = next(gss.split(df, groups=df['client_id']))

train_df = df.iloc[train_idx].copy()
test_df = df.iloc[test_idx].copy()

X_train = train_df.drop(columns=[c for c in DROP_FOR_TRAIN if c in train_df.columns])
y_train = train_df[TARGET]
X_test = test_df.drop(columns=[c for c in DROP_FOR_TRAIN if c in test_df.columns])
y_test = test_df[TARGET]

print(f"Train set: {X_train.shape[0]} rows, {train_df['client_id'].nunique()} clients")
print(f"Test set: {X_test.shape[0]} rows, {test_df['client_id'].nunique()} clients")"""

nb['cells'][5]['source'] = [line + '\n' for line in cell6_source.split('\n')]
nb['cells'][5]['source'][-1] = nb['cells'][5]['source'][-1].strip('\n')

# Patch Cell 8 (Index 7)
cell8_source = """import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.model_selection import GridSearchCV, GroupShuffleSplit
import os

cat_cols = X_train.select_dtypes(include=['object', 'category']).columns
for col in cat_cols:
    X_train[col] = X_train[col].astype('category')
    X_test[col] = X_test[col].astype('category')
    df[col] = df[col].astype('category')

# 1. Cross-Validation Loop for robust metrics
print("=== 5-SEED GROUP SHUFFLE SPLIT EVALUATION ===")
gss_cv = GroupShuffleSplit(n_splits=5, test_size=0.2, random_state=42)
ml_precisions = []
ml_recalls = []
lr_precisions = []
lr_recalls = []
base_precisions = []
base_recalls = []

X_all = df.drop(columns=[c for c in DROP_FOR_TRAIN if c in df.columns])
y_all = df[TARGET]
groups_all = df['client_id']

for i, (tr_idx, te_idx) in enumerate(gss_cv.split(X_all, y_all, groups_all)):
    X_tr, y_tr = X_all.iloc[tr_idx].copy(), y_all.iloc[tr_idx].copy()
    X_te, y_te = X_all.iloc[te_idx].copy(), y_all.iloc[te_idx].copy()
    te_df = df.iloc[te_idx].copy()
    
    # Baseline
    te_df['baseline_stale'] = (te_df["days_since_last_update"] >= 104).astype(int)
    te_df['baseline_visible'] = (te_df["impressions_90d"] >= 500).astype(int)
    te_df['baseline_score'] = (te_df['baseline_stale'] * te_df['baseline_visible'] * te_df["impressions_90d"]).fillna(0)
    
    # Logistic Regression (needs numeric)
    X_tr_num = X_tr.select_dtypes(include=[np.number]).fillna(0)
    X_te_num = X_te.select_dtypes(include=[np.number]).fillna(0)
    lr = Pipeline([('scaler', StandardScaler()), ('lr', LogisticRegression(max_iter=1000))])
    lr.fit(X_tr_num, y_tr)
    lr_prob = lr.predict_proba(X_te_num)[:, 1]
    
    # XGBoost
    xgb_model = xgb.XGBClassifier(random_state=42+i, enable_categorical=True, max_depth=3, n_estimators=100)
    xgb_model.fit(X_tr, y_tr)
    xgb_prob = xgb_model.predict_proba(X_te)[:, 1]
    
    tot_decl = y_te.sum()
    base_idx = np.argsort(te_df['baseline_score'].values)[::-1][:50]
    lr_idx = np.argsort(lr_prob)[::-1][:50]
    xgb_idx = np.argsort(xgb_prob)[::-1][:50]
    
    base_precisions.append(y_te.iloc[base_idx].mean())
    base_recalls.append(y_te.iloc[base_idx].sum() / tot_decl)
    lr_precisions.append(y_te.iloc[lr_idx].mean())
    lr_recalls.append(y_te.iloc[lr_idx].sum() / tot_decl)
    ml_precisions.append(y_te.iloc[xgb_idx].mean())
    ml_recalls.append(y_te.iloc[xgb_idx].sum() / tot_decl)

print(f"Baseline P@50: {np.mean(base_precisions):.2%} ± {np.std(base_precisions):.2%}")
print(f"LogReg P@50:   {np.mean(lr_precisions):.2%} ± {np.std(lr_precisions):.2%}")
print(f"XGBoost P@50:  {np.mean(ml_precisions):.2%} ± {np.std(ml_precisions):.2%}")
print(f"XGBoost Recall:{np.mean(ml_recalls):.2%} ± {np.std(ml_recalls):.2%}")

# 2. Hyperparameter Tuning
print("\\n=== HYPERPARAMETER TUNING ===")
param_grid = {'max_depth': [3, 5], 'n_estimators': [50, 100, 150]}
grid = GridSearchCV(
    estimator=xgb.XGBClassifier(random_state=42, enable_categorical=True),
    param_grid=param_grid, scoring='average_precision', cv=2
)
grid.fit(X_train, y_train)
print(f"Best params: {grid.best_params_}")

# 3. Final Model & Export
final_model = grid.best_estimator_
final_model.fit(X_train, y_train)
y_prob = final_model.predict_proba(X_test)[:, 1]
test_df['decay_prob'] = y_prob

os.makedirs('../../api', exist_ok=True)
final_model.save_model('../../api/xgb_model.json')
print("Model saved to api/xgb_model.json")"""

nb['cells'][7]['source'] = [line + '\n' for line in cell8_source.split('\n')]
nb['cells'][7]['source'][-1] = nb['cells'][7]['source'][-1].strip('\n')

with open(p, 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=1)
