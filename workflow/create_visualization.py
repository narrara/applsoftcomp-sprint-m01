import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

merged_data_table = pd.read_csv('./data/preprocessed/merged-mortality-gdp.csv')
# child mortality rate (Y-axis) versus GDP per capita (X-axis)
sns.scatterplot(data=merged_data_table, x='gdp_capita', y='mortality_rate', hue='year')

#save the scatter plot
plt.savefig('./paper/figs/mortality_vs_gdp.png')


plt.show()
