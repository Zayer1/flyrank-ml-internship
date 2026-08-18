import pandas as pd
import numpy as np
import json
from sklearn.model_selection import GroupShuffleSplit
from sklearn.metrics import precision_score
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder

df = pd.read_csv('data/raw/content_refresh_anonymized.csv')
with open('config.json', 'r') as f:
    config = json.load(f)

df['is_declining_label'] = (df['trend_direction'] == 'down').astype(int)
y = df['is_declining_label']
groups = df['client_id']

cols_to_drop = [c for c in config['DROP_FOR_TRAIN'] if c in df.columns] + ['trend_direction', 'trend_pct', 'is_declining_label']
X = df.drop(columns=cols_to_drop, errors='ignore')

# Identify numerical and categorical columns
num_cols = X.select_dtypes(include=['int64', 'float64']).columns
cat_cols = X.select_dtypes(include=['object', 'category']).columns

# Better preprocessing for LogReg: Median imputation for nums, frequent for cats
preprocessor = ColumnTransformer(
    transformers=[
        ('num', Pipeline(steps=[
            ('imputer', SimpleImputer(strategy='median')),
            ('scaler', StandardScaler())
        ]), num_cols),
        ('cat', Pipeline(steps=[
            ('imputer', SimpleImputer(strategy='most_frequent')),
            ('onehot', OneHotEncoder(handle_unknown='ignore'))
        ]), cat_cols)
    ])

pipeline_lr = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('classifier', LogisticRegression(random_state=42, max_iter=1000))
])

# 5-Seed Evaluation
gss = GroupShuffleSplit(n_splits=5, test_size=0.2, random_state=42)
lr_p50s = []

for train_idx, test_idx in gss.split(X, y, groups):
    X_train, X_test = X.iloc[train_idx], X.iloc[test_idx]
    y_train, y_test = y.iloc[train_idx], y.iloc[test_idx]
    
    pipeline_lr.fit(X_train, y_train)
    y_prob = pipeline_lr.predict_proba(X_test)[:, 1]
    
    top_indices = np.argsort(y_prob)[-50:][::-1]
    p50 = y_test.iloc[top_indices].mean()
    lr_p50s.append(p50)

print(f"Fair LogReg P@50: {np.mean(lr_p50s):.2%} +/- {np.std(lr_p50s):.2%}")
