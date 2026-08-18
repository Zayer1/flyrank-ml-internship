import nbformat
import os

nb_path = r'work\notebooks\capstone.ipynb'

with open(nb_path, 'r', encoding='utf-8') as f:
    nb = nbformat.read(f, as_version=4)

def set_code(cell_index, code):
    nb.cells[cell_index].source = code

set_code(2, '''pass''')

set_code(4, '''import pandas as pd
import numpy as np
from sklearn.model_selection import GroupShuffleSplit
import xgboost as xgb
import warnings
warnings.filterwarnings('ignore')

# Load dataset robustly
data_path = '../../data/raw/content_refresh_anonymized.csv'
df = pd.read_csv(data_path)
print(f"Dataset shape: {df.shape}")''')

set_code(6, '''# Create target label before dropping its source
df['is_declining_label'] = (df['trend_direction'] == 'down').astype(int)
TARGET = 'is_declining_label'

# Drop leaky features and outcome-window metrics to prevent time-travel leakage
DROP_FOR_TRAIN = [
    'client_id', 'content_id', 'trend_direction', 'trend_pct', TARGET,
    'impressions_last_30d', 'clicks_last_30d', 'sessions_last_30d',
    'impressions_90d', 'clicks_90d', 'pageviews_90d', 'sessions_90d', 
    'users_90d', 'engaged_sessions_90d', 'ai_sessions_90d', 'scroll_events_90d',
    'ctr', 'avg_position', 'engagement_rate', 'scroll_rate', 'ai_traffic_pct', 'impression_tier'
]

# Split into train/test grouping by client_id
gss = GroupShuffleSplit(n_splits=1, test_size=0.2, random_state=42)
train_idx, test_idx = next(gss.split(df, groups=df['client_id']))

train_df = df.iloc[train_idx].copy()
test_df = df.iloc[test_idx].copy()

X_train = train_df.drop(columns=DROP_FOR_TRAIN)
y_train = train_df[TARGET]
X_test = test_df.drop(columns=DROP_FOR_TRAIN)
y_test = test_df[TARGET]

print(f"Train set: {X_train.shape[0]} rows, {train_df['client_id'].nunique()} clients")
print(f"Test set: {X_test.shape[0]} rows, {test_df['client_id'].nunique()} clients")''')

set_code(8, '''# Convert categorical columns for XGBoost
cat_cols = X_train.select_dtypes(include=['object', 'category']).columns
for col in cat_cols:
    X_train[col] = X_train[col].astype('category')
    X_test[col] = X_test[col].astype('category')

# Train Model
model = xgb.XGBClassifier(random_state=42, enable_categorical=True, max_depth=3, n_estimators=100)
model.fit(X_train, y_train)
y_prob = model.predict_proba(X_test)[:, 1]

# Re-create Baseline on test_df
test_df['baseline_stale'] = (test_df["days_since_last_update"] >= 180).astype(int)
test_df['baseline_visible'] = (test_df["impressions_90d"] >= 500).astype(int)
test_df['baseline_score'] = (test_df['baseline_stale'] * test_df['baseline_visible'] * test_df["impressions_90d"]).fillna(0)

# Evaluate ML vs Baseline Top 50
ml_top_50_idx = np.argsort(y_prob)[::-1][:50]
baseline_top_50_idx = np.argsort(test_df['baseline_score'].values)[::-1][:50]

total_declining = y_test.sum()
print("=== METRIC COMPARISON (TEST SET) ===")
print(f"Baseline Precision@50: {y_test.iloc[baseline_top_50_idx].mean():.2%}")
print(f"ML Precision@50:       {y_test.iloc[ml_top_50_idx].mean():.2%}")
print(f"Baseline Global Recall (Top 50): {y_test.iloc[baseline_top_50_idx].sum() / total_declining:.2%}")
print(f"ML Global Recall (Top 50):       {y_test.iloc[ml_top_50_idx].sum() / total_declining:.2%}")

# Export Model
import os
os.makedirs('../../api', exist_ok=True)
model.save_model('../../api/xgb_model.json')
print("Model saved to api/xgb_model.json")''')

set_code(10, '''importances = pd.DataFrame({
    'feature': X_train.columns,
    'importance': model.feature_importances_
}).sort_values('importance', ascending=False)
print("Top Honest Feature Importances:")
print(importances.head(5))''')

set_code(12, '''def assign_action(prob):
    if prob > 0.7: return "Urgent Refresh"
    elif prob > 0.4: return "Standard Review"
    else: return "Basement Trap"

test_df['decay_probability'] = y_prob
test_df['action'] = test_df['decay_probability'].apply(assign_action)
print(test_df[['content_id', 'decay_probability', 'action']].sort_values(by='decay_probability', ascending=False).head(5))''')

set_code(14, '''pass''')

with open(nb_path, 'w', encoding='utf-8') as f:
    nbformat.write(nb, f)

print('Capstone notebook correctly injected with w05 code.')
