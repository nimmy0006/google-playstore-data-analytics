import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Creating a sample dataset
data = {
    'App': ['App A', 'App B', 'App C', 'App D', 'App E', 'App F', 'App G', 'App H'],
    'Category': ['Game', 'Finance', 'Health', 'Social', 'Game', 'Finance', 'Health', 'Social'],
    'Rating': [4.5, 3.8, 4.9, 2.1, 4.0, 3.5, 4.7, 1.8],
    'Reviews': [1500, 2300, 5400, 1200, 3200, 4100, 5000, 1800],
    'Sentiment': ['Positive', 'Neutral', 'Positive', 'Negative', 'Neutral', 'Negative', 'Positive', 'Negative']
}

# Create DataFrame
df = pd.DataFrame(data)

# Filter data: only apps with more than 1000 reviews
df_filtered = df[df['Reviews'] > 1000]

# Get top 5 categories by number of apps
top_5_categories = df_filtered['Category'].value_counts().head(5).index
df_top_categories = df_filtered[df_filtered['Category'].isin(top_5_categories)]

# Create rating groups
def categorize_rating(rating):
    if rating <= 2:
        return '1-2 stars'
    elif rating <= 4:
        return '3-4 stars'
    else:
        return '4-5 stars'

df_top_categories['Rating Group'] = df_top_categories['Rating'].apply(categorize_rating)

# Group by category and rating group, then get sentiment distribution
sentiment_distribution = df_top_categories.groupby(['Category', 'Rating Group', 'Sentiment'])['Sentiment'].count().unstack(fill_value=0)

# Plotting a stacked bar chart
sentiment_distribution.plot(kind='bar', stacked=True, figsize=(10, 6))
plt.title('Sentiment Distribution by Rating Group and Category')
plt.xlabel('Category and Rating Group')
plt.ylabel('Number of Reviews')
plt.legend(title='Sentiment')
plt.tight_layout()
plt.show()
