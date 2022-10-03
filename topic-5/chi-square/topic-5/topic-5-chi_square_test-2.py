# Chi Sqaured Test Comparing Multiple Proportions in Contingency Tables

import pandas as pd
import matplotlib.pyplot as plt

Data = pd.read_csv('http://stat4ds.rwth-aachen.de/data/Happy.dat', sep='\s+')
rowlabel = ['Married', 'Divorced/Seperated', 'Never Married']
collabel = ['Very happy', 'Pretty happy', 'Not too happy']
table = pd.crosstab(Data['marital'], Data['happiness'], margins=False) # row, col
x = table
table.index = rowlabel
table.columns = collabel
print(table)
# conditional distributions on happiness (proportions within rows):

proptable = pd.crosstab(Data['marital'], Data['happiness'], normalize='index')
proptable.index = rowlabel
proptable.columns = collabel
print(proptable)

import statsmodels.api as sm # expected frequencies under H0: independence
table = sm.stats.Table(table) # contingency table
print(table.fittedvalues)

X2 = table.test_nominal_association() # chi-squared test of independence
print(X2)

print(table.standardized_resids) # standardized residuals
Data.loc[Data['happiness'] == 1, 'happiness'] = 'Very' # loc[col, row]
Data.loc[Data['happiness'] == 2, 'happiness'] = 'Pretty'
Data.loc[Data['happiness'] == 3, 'happiness'] = 'Not too'
Data.loc[Data['marital'] == 1, 'marital'] = 'Married'
Data.loc[Data['marital'] == 2, 'marital'] = 'Div/Sep'
Data.loc[Data['marital'] == 3, 'marital'] = 'Never Married'
# print(Data)

from statsmodels.graphics.mosaicplot import mosaic
fig, _ = mosaic(Data, ['marital', 'happiness'], statistic=True)
plt.xlabel('Marital')
plt.ylabel('happiness')
plt.show()
