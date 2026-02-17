# Sprint Project 01

## Project Directory

### Folders
- data: raw and preprocessed csv files
- workflows: data cleaning and visualization scripts
- notebooks: notebook for initial work
- paper: documentation and visualization


Data
``` text
data/
├──preprocessed
├──raw
```

Workflow
``` text
workflow/
├──process_mortality.py
├──process_gdp.py
├──merge_data.py
```

Notebooks
``` text
notebooks/
├── data-format-viz.ipynb
```

Paper
```text
paper/
├──figs
├──README.md
```

### Data
#### Intial Data Exploration
Created a Jupyter notebook [`data-format-viz.ipynb`](https://github.com/narrara/applsoftcomp-sprint-m01/blob/master/notebooks/data-format-viz.ipynb) in the notebooks folder for initial data exploration and to add the initial code to be used and then modified in the workflow scripts.


#### Data Prep
##### Datasets
- dataset I: [child-motality.csv](https://github.com/narrara/applsoftcomp-sprint-m01/blob/master/data/raw/child-motality.csv)
- dataset II: [gdp-data.csv](https://github.com/narrara/applsoftcomp-sprint-m01/blob/master/data/raw/gdp-data.csv)

##### Data Cleaning
As the raw datasets are not tidy, they have then been transformed into tidy format. Instead of having year columns listing multiple observations, `year` became its own column on each dataset.
- [tidy-child-mortality](https://github.com/narrara/applsoftcomp-sprint-m01/blob/master/data/preprocessed/tidy-child-mortality.csv): `child_mortality` column added during transformation
- [tidy-gdp-data](https://github.com/narrara/applsoftcomp-sprint-m01/blob/master/data/preprocessed/tidy-gdp-data.csv): `gdp_capita` column added during trasnformation

The tidy datasets were then merged into a single dataset on the `geo`, `name`, and `year` columns. The following columns exist in the merged dataset: `geo`, `name`, `mortality_rate`, `gdp_capita`, and `year`
- [merged-mortality-gdp](https://github.com/narrara/applsoftcomp-sprint-m01/blob/master/data/preprocessed/merged-mortality-gdp.csv)



#### Data Vizualization
Scatter plot is used to show gdp and mortality rates across the years.
![mortality vs gdp over the years](/paper/figs/mortality_vs_gdp.png)

### Findings
Based on the scatter plot, we can observe a negative relationship. As the GDP per capita increases, child mortality rate decreases. Also, over the years, GDP has increased and the child mortality rate has decreased. In the 1800s and 1900s, the world had more child deaths and very low GDP. As the time passed, even with low GDP, child mortality has decreased.