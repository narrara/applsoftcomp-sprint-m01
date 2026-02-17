import pandas as pd

# Merge datasets

# Load datasets
mortality_data = pd.read_csv('./data/preprocessed/tidy-child-mortality.csv')
gdp_data = pd.read_csv('./data/preprocessed/tidy-gdp-data.csv')

# Merge datasets
tidy_data_table = mortality_data.merge(gdp_data, on=['geo', 'name', 'year'])

# Save merged data
tidy_data_csv = './data/preprocessed/merged-mortality-gdp.csv'
tidy_data_table.to_csv(tidy_data_csv, index=False)