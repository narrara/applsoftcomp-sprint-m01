import pandas as pd

# Tidy dataset II

# Load and tidy
data_table = pd.read_csv('./data/raw/gdp-data.csv')
print(data_table.head())

# Use pd.melt(), pd.pivot_table(), or custom code
tidy_data_table = data_table.melt(id_vars=['geo', 'name'], var_name='year', value_name='gdp_capita')

# Save tidy data
tidy_data_csv = './data/preprocessed/tidy-gdp-data.csv'
tidy_data_table.to_csv(tidy_data_csv, index=False)