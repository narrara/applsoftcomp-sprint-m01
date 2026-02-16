import pandas as pd

# Tidy dataset I

# Load and tidy
data_table = pd.read_csv('./data/raw/child-motality.csv')
print(data_table.head())
# Use pd.melt(), pd.pivot_table(), or custom code
tidy_data_table = data_table.melt(id_vars=['geo', 'name'], var_name='year', value_name='mortality_rate')

# Save tidy data
tidy_data_csv = './data/preprocessed/tidy-child-mortality.csv'
tidy_data_table.to_csv(tidy_data_csv, index=False)