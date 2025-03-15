import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
file_path = '/content/drive/MyDrive/googleplaystore.csv'
data = pd.read_csv(file_path)

# Filter and clean data
data = data.dropna(subset=['Rating'])
data = data[data['Rating'] <= 5]

# Create the violin plot
plt.figure(figsize=(12, 8))
sns.violinplot(x='Category', y='Rating', data=data)
plt.xticks(rotation=90)
plt.title('Rating Distribution by Category')
plt.xlabel('App Category')
plt.ylabel('App Rating')
plt.show()
