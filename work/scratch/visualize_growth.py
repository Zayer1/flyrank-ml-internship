import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df = pd.read_csv('data/raw/content_refresh_anonymized.csv')

# Filter for pages with meaningful traffic to avoid division by zero/noise
valid = df[df['sessions_prev_30d'] > 10].copy()

# Calculate growth percentage
valid['growth_pct'] = ((valid['sessions_last_30d'] - valid['sessions_prev_30d']) / valid['sessions_prev_30d']) * 100

# Clamp outliers for visualization (limit to -100% to +300% growth)
valid['growth_pct_clamped'] = valid['growth_pct'].clip(lower=-100, upper=300)

# Create the plot
plt.figure(figsize=(10, 6))
sns.histplot(valid['growth_pct_clamped'], bins=50, kde=True, color='#4A90E2')

plt.title('Distribution of Traffic Growth (Month over Month)', fontsize=14, pad=15)
plt.xlabel('Traffic Growth Percentage (%)', fontsize=12)
plt.ylabel('Number of Pages', fontsize=12)

# Add vertical lines for Quartiles
plt.axvline(valid['growth_pct'].median(), color='red', linestyle='--', label=f"Median ({valid['growth_pct'].median():.0f}%)")
plt.axvline(valid['growth_pct'].quantile(0.75), color='green', linestyle='--', label=f"Top 25% ({valid['growth_pct'].quantile(0.75):.0f}%)")

plt.legend()
plt.tight_layout()

# Save to artifacts directory
plt.savefig(r'C:\Users\Admin\.gemini\antigravity-ide\brain\457eb36c-14c0-4f50-b0de-fc599c5ac069\growth_distribution.png', dpi=300)
print("Visualization saved.")
