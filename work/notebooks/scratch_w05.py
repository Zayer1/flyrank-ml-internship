import pandas as pd
import numpy as np
from sklearn.model_selection import GroupShuffleSplit
from sklearn.metrics import roc_auc_score
import xgboost as xgb
import warnings
warnings.filterwarnings('ignore')

print("--- 1. Loading Data ---")
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(current_dir, '..', '..', 'data', 'raw', 'content_refresh_anonymized.csv')
df = pd.read_csv(data_path)
print(f"Initial raw dataset shape: {df.shape}")

# Create target label before dropping its source
df['is_declining_label'] = (df['trend_direction'] == 'down').astype(int)

# Define leaky features and targets
LEAKY_FEATURES = ['trend_direction', 'trend_pct']
TARGET = 'is_declining_label'

# Drop leaky features
df_clean = df.drop(columns=LEAKY_FEATURES)
print(f"Dataset shape after dropping leaky features {LEAKY_FEATURES}: {df_clean.shape}")

print("\n--- 2. Splitting Data (GroupShuffleSplit) ---")
# Split into train/test grouping by client_id to prevent leakage
gss = GroupShuffleSplit(n_splits=1, test_size=0.2, random_state=42)
train_idx, test_idx = next(gss.split(df_clean, groups=df_clean['client_id']))

train_df = df_clean.iloc[train_idx].copy()
test_df = df_clean.iloc[test_idx].copy()
print(f"train_df shape: {train_df.shape} (Client count: {train_df['client_id'].nunique()})")
print(f"test_df shape: {test_df.shape} (Client count: {test_df['client_id'].nunique()})")

print("\n--- 3. Defining Features (X) and Target (y) ---")
# Drop IDs, Target, and outcome-window metrics from X to prevent leakage
DROP_FOR_TRAIN = [
    'client_id', 'content_id', TARGET,
    'impressions_last_30d', 'clicks_last_30d', 'sessions_last_30d',
    'impressions_90d', 'clicks_90d', 'pageviews_90d', 'sessions_90d', 
    'users_90d', 'engaged_sessions_90d', 'ai_sessions_90d', 'scroll_events_90d'
]

X_train = train_df.drop(columns=DROP_FOR_TRAIN)
y_train = train_df[TARGET]
X_test = test_df.drop(columns=DROP_FOR_TRAIN)
y_test = test_df[TARGET]

print(f"X_train shape: {X_train.shape} | y_train shape: {y_train.shape}")
print(f"X_test shape: {X_test.shape} | y_test shape: {y_test.shape}")

# Convert categorical columns for XGBoost
cat_cols = X_train.select_dtypes(include=['object']).columns
print(f"Converting categorical columns to 'category' dtype for XGBoost: {list(cat_cols)}")
for col in cat_cols:
    X_train[col] = X_train[col].astype('category')
    X_test[col] = X_test[col].astype('category')

print("\n--- 4. Training XGBoost ---")
# Train XGBoost with categorical support
model = xgb.XGBClassifier(
    random_state=42, 
    enable_categorical=True,
    max_depth=3, # Keep it shallow to prevent extreme overfitting
    n_estimators=100
)
model.fit(X_train, y_train)
print("Model trained successfully.")

print("\n--- 5. Evaluating against Week 4 Baseline ---")
# Predict probabilities on test set
y_prob = model.predict_proba(X_test)[:, 1]
print(f"y_prob shape: {y_prob.shape}")

# Re-create Baseline on test_df
test_df['baseline_stale'] = (test_df["days_since_last_update"] >= 180).astype(int)
test_df['baseline_visible'] = (test_df["impressions_90d"] >= 500).astype(int)
test_df['baseline_score'] = (test_df['baseline_stale'] * test_df['baseline_visible'] * test_df["impressions_90d"]).fillna(0)

# Evaluate ML Precision@50
ml_top_50_idx = np.argsort(y_prob)[::-1][:50]
ml_precision_50 = y_test.iloc[ml_top_50_idx].mean()

# Evaluate Baseline Precision@50
baseline_top_50_idx = np.argsort(test_df['baseline_score'].values)[::-1][:50]
baseline_precision_50 = y_test.iloc[baseline_top_50_idx].mean()

total_declining_in_test = y_test.sum()
ml_global_recall = y_test.iloc[ml_top_50_idx].sum() / total_declining_in_test
baseline_global_recall = y_test.iloc[baseline_top_50_idx].sum() / total_declining_in_test

# Evaluate ROC-AUC (Global performance)
ml_roc_auc = roc_auc_score(y_test, y_prob)
baseline_roc_auc = roc_auc_score(y_test, test_df['baseline_score'])

print("\n=== METRIC COMPARISON (TEST SET) ===")
print(f"Total declining pages in test set: {total_declining_in_test}")
print(f"Baseline Precision@50: {baseline_precision_50:.2%}")
print(f"ML Precision@50:       {ml_precision_50:.2%}")
print(f"Baseline Global Recall (from Top 50): {baseline_global_recall:.2%}")
print(f"ML Global Recall (from Top 50):       {ml_global_recall:.2%}")
print(f"Baseline ROC-AUC:      {baseline_roc_auc:.4f}")
print(f"ML ROC-AUC:            {ml_roc_auc:.4f}")

print("\n--- 6. Feature Importances ---")
importances = pd.DataFrame({
    'feature': X_train.columns,
    'importance': model.feature_importances_
}).sort_values('importance', ascending=False)
print(importances.head(10))
