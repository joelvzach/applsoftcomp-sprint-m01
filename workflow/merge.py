import pandas as pd

gdp = pd.read_csv('../data/preprocessed/gdp-data.csv')
mortality = pd.read_csv('../data/preprocessed/child-motality.csv')

data = pd.merge(gdp,mortality, how='outer')

data.to_csv('../data/preprocessed/merge_data.csv')