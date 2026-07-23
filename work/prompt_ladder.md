# Prompt Ladder: FlyRank Predictive Pipeline

## The Baseline
**Prompt:** "Write python code to predict traffic growth from SEO data."

**Output Excerpt:**
```python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

df = pd.read_csv('seo_data.csv')
X = df.drop('traffic_growth', axis=1)
y = df['traffic_growth']
X_train, X_test, y_train, y_test = train_test_split(X, y)
model = LinearRegression()
model.fit(X_train, y_train)
```

**Notes:**
- **What changed:** (Baseline)
- **What improved:** N/A
- **What failed:** It gave me a generic Linear Regression model on made-up column names (`seo_data.csv`). It treated the problem as a continuous regression task rather than our specific classification/ranking task. 
- **What I would try next:** Give it the real context (the actual dataset name and our specific target definition).

---

## Version 1
**Prompt:** "Write python code for a Supervised Scoring task to predict traffic growth. The dataset is content_refresh_anonymized.csv. 1 row = 1 page. The target is a binary indicator of >80% growth."

**Output Excerpt:**
```python
df = pd.read_csv('content_refresh_anonymized.csv')
df['target'] = (df['trend_pct'] > 0.80).astype(int)
X = df.drop(['target'], axis=1)
y = df['target']
clf = RandomForestClassifier()
clf.fit(X_train, y_train)
```

**Notes:**
- **What changed:** Added **Real Context** (dataset name, unit of analysis, binary target definition).
- **What improved:** The model shifted from a generic regression task to the correct binary classification task (Supervised Scoring) operating on our actual data structure.
- **What failed:** It included the `trend_direction` and `trend_pct` columns as features in `X`. Because the target is derived from `trend_pct`, this causes massive data leakage. The model is mathematically invalid.
- **What I would try next:** Add a constraint to explicitly drop the toxic labels.

---

## Version 2
**Prompt:** "Write python code for a Supervised Scoring task to predict traffic growth. The dataset is content_refresh_anonymized.csv. 1 row = 1 page. The target is a binary indicator of >80% growth. Constraint: You must drop the 'trend_direction' and 'trend_pct' columns from the feature set to prevent data leakage."

**Output Excerpt:**
```python
X = df.drop(['target', 'trend_direction', 'trend_pct'], axis=1)
# ... training code ...
predictions = clf.predict(X_test)
print(f"Accuracy: {accuracy_score(y_test, predictions)}")
print(f"F1 Score: {f1_score(y_test, predictions)}")
```

**Notes:**
- **What changed:** Added **Constraints** (dropping toxic labels).
- **What improved:** The script correctly prevented data leakage. The model is now mathematically sound and forces the algorithm to learn from the actual features instead of the answer key.
- **What failed (The "This didn't help" moment):** The output evaluated the model using global Accuracy and F1-score. This was a step backward operationally. Our editors can only refresh 50 pages a month; global accuracy across 30,000 rows tells us absolutely nothing about how good our top 50 recommendations are. 
- **What I would try next:** Specify the evaluation quality criteria.

---

## Version 3
**Prompt:** "Write python code for a Supervised Scoring task to predict traffic growth. The dataset is content_refresh_anonymized.csv. 1 row = 1 page. The target is a binary indicator of >80% growth. Constraint: You must drop the 'trend_direction' and 'trend_pct' columns from the feature set to prevent data leakage. Quality Criteria: Do not use global accuracy. Evaluate the model strictly using Precision at Top K (where K=50)."

**Output Excerpt:**
```python
probabilities = clf.predict_proba(X_test)[:, 1]
results = pd.DataFrame({'actual': y_test, 'prob': probabilities})
top_50 = results.sort_values(by='prob', ascending=False).head(50)
precision_at_50 = top_50['actual'].mean()
print(f"Precision at Top 50: {precision_at_50:.2f}")
```

**Notes:**
- **What changed:** Added **Quality Criteria** (Precision at Top K).
- **What improved:** The evaluation metric now perfectly aligns with the business workflow. It tells the editor exactly how many of the 50 manual refresh slots were correctly allocated to high-growth pages.
- **What failed:** The code just prints a raw float value to the console. To hand this to an editor, we need a readable, actionable list of the pages.
- **What I would try next:** Define a specific output format.

---

## Version 4
**Prompt:** "Write python code for a Supervised Scoring task to predict traffic growth. The dataset is content_refresh_anonymized.csv. 1 row = 1 page. The target is a binary indicator of >80% growth. Constraint: You must drop the 'trend_direction' and 'trend_pct' columns from the feature set to prevent data leakage. Quality Criteria: Do not use global accuracy. Evaluate the model strictly using Precision at Top K (where K=50). Output Format: Output the code as a single clean block, and include code that prints a formatted markdown table showing the Top 10 predicted page IDs and their risk scores."

**Output Excerpt:**
```python
top_10 = results.sort_values(by='prob', ascending=False).head(10)
print("| Page ID | Predicted Growth Probability |")
print("|---------|------------------------------|")
for idx, row in top_10.iterrows():
    print(f"| {idx} | {row['prob']:.4f} |")
```

**Notes:**
- **What changed:** Added **Output Format** (Markdown table).
- **What improved:** The final output of the script is now immediately readable by non-technical stakeholders (editors) who can just copy-paste the markdown table into their workflow.
- **What failed:** The model it built under the hood was an unbound Random Forest. Without limits, it memorized the training data (overfitting), making the predictions dangerously unreliable on live data.
- **What I would try next:** Add a constraint on the model architecture to force generalization.

---

## Version 5
**Prompt:** "Write python code for a Supervised Scoring task to predict traffic growth. The dataset is content_refresh_anonymized.csv. 1 row = 1 page. The target is a binary indicator of >80% growth. Constraint 1: Drop the 'trend_direction' and 'trend_pct' columns to prevent data leakage. Constraint 2: Use a tree-based model but restrict max_depth to 4 to prevent overfitting. Quality Criteria: Evaluate the model strictly using Precision at Top K (where K=50). Output Format: Print a formatted markdown table showing the Top 10 predicted page IDs and their growth probabilities."

**Output Excerpt:**
```python
clf = RandomForestClassifier(max_depth=4, random_state=42)
clf.fit(X_train, y_train)
# ... ranking and markdown table generation ...
```

**Notes:**
- **What changed:** Added a second **Constraint** (`max_depth=4`).
- **What improved:** The model is now forced to generalize instead of memorizing the exam. The script is completely production-ready: it prevents leakage, avoids overfitting, evaluates on the correct business metric, and outputs a stakeholder-friendly table.
- **What failed:** Nothing. This is a robust, engineered prompt.
- **What I would try next:** Deploy the script.

---

## Final Reusable Prompt
**Context:** We are building a Supervised Scoring task to predict SEO traffic growth based on historical metrics. 
**Goal:** Write a Python script to train the model and output actionable recommendations.
**Constraints:** 
1. Dataset is `content_refresh_anonymized.csv` (1 row = 1 page).
2. The target is a binary indicator representing >80% growth.
3. You MUST drop the `trend_direction` and `trend_pct` columns from the feature set to prevent data leakage. 
4. Use a tree-based model restricted to `max_depth=4` to prevent overfitting.
**Quality Criteria:** Evaluate the model exclusively using Precision at Top K (where K=50). Do not use global accuracy metrics.
**Output Format:** Output the complete code in a single block. Ensure the script prints a formatted markdown table showing the Top 10 predicted page IDs and their growth probabilities for the editorial team.
