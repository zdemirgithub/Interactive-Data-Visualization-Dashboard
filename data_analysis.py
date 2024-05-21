import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv('data.csv')

# Data preprocessing and analysis
# Example: Calculate summary statistics, visualize data

# Example visualization
sns.barplot(x='category', y='value', data=df)
plt.title('Average Value by Category')
plt.xlabel('Category')
plt.ylabel('Average Value')
plt.show()
