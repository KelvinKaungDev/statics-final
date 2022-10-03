# Salary case:
# The recruiter company would like to know the association between the range of salary and education level.
# Then they decide to randomly collect the data from private employees. Use salary.csv to perform the following problem:

# (a)Create the two-way contingency table
# (b)Perform the Chi-Square test with 5% significance level

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
salary= pd.read_csv(r'C:\Users\iamte\OneDrive\Desktop\ABAC\Stat I\Salary.csv')
rowlabel= ['Less than 25000 Baht', '25001 -50000 Baht', '50001 -75000 Baht', '75001 -100000 Baht', 'More than 100000 Baht']
collabel= ['Bachelor', 'Master', 'Doctoral']
table = pd.crosstab(salary['Salary'], salary['Education'], margins = False)
table.index= rowlabel
table.columns= collabel
table

## Perform contingency table

import statsmodels.api as sm
table = sm.stats.Table(table)
print(table.fittedvalues)

## Perform Chi-Square Test

Chi_Square = table.test_nominal_association()
print(Chi_Square)
