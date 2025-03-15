import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
file_path = '/content/drive/MyDrive/googleplaystore.csv'
data = pd.read_csv(file_path)

# Clean and convert columns to numeric, handling errors
data['Installs'] = pd.to_numeric(data['Installs'].str.replace('[+,]', '', regex=True), errors='coerce')
data['Reviews'] = pd.to_numeric(data['Reviews'], errors='coerce')
data['Rating'] = pd.to_numeric(data['Rating'], errors='coerce')

# Drop rows with missing or invalid values
data.dropna(subset=['Installs', 'Reviews', 'Rating'], inplace=True)

# Correlation matrix
correlation = data[['Installs', 'Reviews', 'Rating']].corr()

# Heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(correlation, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Heatmap of Installs, Reviews, and Rating')
plt.show()
