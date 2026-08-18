import pandas as pd
import numpy as np
import json
import xgboost as xgb
from sklearn.model_selection import GroupShuffleSplit
from sklearn.metrics import precision_score

# Load data and config
df = pd.read_csv('data/raw/content_refresh_anonymized.csv')
with open('config.json', 'r') as f:
    config = json.load(f)

# 1. Filter out 'new' and 'flat' to see if P@50 drops
df_filtered = df[~df['trend_direction'].isin(['new', 'flat'])].copy()
df_filtered['is_declining_label'] = (df_filtered['trend_direction'] == 'down').astype(int)

# Prepare matrices
y = df_filtered['is_declining_label']
groups = df_filtered['client_id']

# Apply DROP_FOR_TRAIN
cols_to_drop = [c for c in config['DROP_FOR_TRAIN'] if c in df_filtered.columns] + ['is_declining_label']
X = df_filtered.drop(columns=cols_to_drop, errors='ignore')

# Encode categoricals as 'category'
cat_cols = X.select_dtypes(include=['object', 'category']).columns
for col in cat_cols:
    X[col] = X[col].astype('category')

# Use 1 seed just to test P@50 on hard cases
gss = GroupShuffleSplit(n_splits=1, test_size=0.2, random_state=42)
train_idx, test_idx = next(gss.split(X, y, groups))

X_train, y_train = X.iloc[train_idx], y.iloc[train_idx]
X_test, y_test = X.iloc[test_idx], y.iloc[test_idx]

model = xgb.XGBClassifier(
    enable_categorical=True,
    max_depth=3,
    n_estimators=100,
    random_state=42,
    tree_method='hist'
)
model.fit(X_train, y_train)
y_prob = model.predict_proba(X_test)[:, 1]

# Sort top 50
top_indices = np.argsort(y_prob)[-50:][::-1]
y_test_top50 = y_test.iloc[top_indices]
p50 = y_test_top50.mean()

print(f"XGBoost P@50 on hard cases (no 'new'/'flat'): {p50:.2%}")

# 2. Test Compound Urgent Rule on the FULL dataset
df_full = df.copy()
df_full['is_declining_label'] = (df_full['trend_direction'] == 'down').astype(int)
y_full = df_full['is_declining_label']
groups_full = df_full['client_id']

cols_to_drop_f = [c for c in config['DROP_FOR_TRAIN'] if c in df_full.columns] + ['is_declining_label']
X_full = df_full.drop(columns=cols_to_drop_f, errors='ignore')

for col in cat_cols:
    if col in X_full.columns:
        X_full[col] = X_full[col].astype('category')

train_idx_f, test_idx_f = next(gss.split(X_full, y_full, groups_full))

X_train_f, X_test_f = X_full.iloc[train_idx_f], X_full.iloc[test_idx_f]
y_train_f, y_test_f = y_full.iloc[train_idx_f], y_full.iloc[test_idx_f]

model.fit(X_train_f, y_train_f)
y_prob_f = model.predict_proba(X_test_f)[:, 1]

# Compound rule: prob > 0.70 AND search_volume > 100
sv = df_full.loc[X_test_f.index, 'search_volume'].fillna(0)
urgent_mask = (y_prob_f > 0.70) & (sv > 100)

if urgent_mask.sum() > 0:
    urgent_p = y_test_f[urgent_mask].mean()
    print(f"Compound Urgent Precision: {urgent_p:.2%} (N={urgent_mask.sum()})")
else:
    print("Compound Urgent Precision: N/A (0 pages flagged)")
