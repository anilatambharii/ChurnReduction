'''import pandas as pd
from scipy.stats import f_oneway

# Load dataset
df = pd.read_csv("sample_churn_data.csv")

# Normalize column names (strip spaces, lowercase)
df.columns = df.columns.str.strip().str.lower()

# Verify if 'churn' column exists
if 'churn' not in df.columns:
    print("Error: 'churn' column is missing!")
    print("Available columns:", df.columns)
    exit()

# Perform ANOVA test
for col in ['usage_freq', 'payment_delay', 'support_tickets']:
    group1 = df[df['churn'] == 0][col]
    group2 = df[df['churn'] == 1][col]
    
    stat, p = f_oneway(group1, group2)
    print(f"{col} ANOVA p-value: {p:.4f}")
'''
import pandas as pd
from scipy.stats import mannwhitneyu

# Load dataset
df = pd.read_csv("sample_churn_data.csv")

# Normalize column names (strip spaces, lowercase)
df.columns = df.columns.str.strip().str.lower()

for col in ['usage_freq', 'payment_delay', 'support_tickets']:
    group1 = df[df['churn'] == 0][col]
    group2 = df[df['churn'] == 1][col]
    
    if len(group1) > 5 and len(group2) > 5:  # Ensure minimum sample size
        stat, p = mannwhitneyu(group1, group2)
        print(f"{col} Mann-Whitney U p-value: {p}")
    else:
        print(f"Not enough samples for {col}")
