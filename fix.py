import pandas as pd

df = pd.read_csv('/Users/cw2/Desktop/fantasy football 5/csv/2023/weekly-stats.csv')

# Drop the 'Week 1' column
df = df.drop('Week 2', axis=1)

# Save the updated DataFrame to a new CSV file
df.to_csv('/Users/cw2/Desktop/fantasy football 5/csv/2023/weekly-stats.csv', index=False)
