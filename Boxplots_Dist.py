import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('sample_churn_data.csv')

print("Columns in the dataset:", df.columns)

for col in df.columns:
    sns.boxplot(x=df.columns[0], y=col, data=df)
    plt.title(f"{col} Distribution")
    plt.show()
