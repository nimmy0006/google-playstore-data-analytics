import plotly.express as px

# Aggregate installs by category and date
category_installs = df.groupby(['Date', 'Category'])['Installs'].sum().reset_index()

# Choose the date range (example: January to March)
start_date = '2024-01-01'
end_date = '2024-03-31'
filtered_data = category_installs[(category_installs['Date'] >= start_date) & (category_installs['Date'] <= end_date)]

# Plot the grouped bar chart
fig = px.bar(filtered_data, 
             x='Date', 
             y='Installs', 
             color='Category', 
             barmode='group',
             title='Top App Categories by Installs Over Time')

fig.update_layout(xaxis_title='Date', yaxis_title='Total Installs')
fig.show()
