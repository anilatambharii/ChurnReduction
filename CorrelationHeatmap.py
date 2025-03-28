import pandas as pd  # Required for pd.read_csv()
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('sample_churn_data.csv')
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
plt.show()

