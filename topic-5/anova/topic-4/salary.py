# Salary case:

# The recruiter company would like to know the association between the range of salary and education level. Then they decide to randomly collect the data from private employee. Use salary.csv to perform the following problem:
# a) Create the two-way contingency table
# b) Perform the Chi-square test with 5% significance level

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

salary = pd.read_csv('/Users/kaunghtetoo/Desktop/Salary.csv')
rowlabel = ['Less than 25000 Baht', '25001 - 50000 Baht', '50001 - 75000 Baht', '75001 - 100000 Baht', 'More than 100000 Baht']
collabel = ['Bachelor', 'Master', 'Doctoral']
table = pd.crosstab(salary['Salary'], salary['Education'], margins = False)
table.index = rowlabel
table.columns = collabel
table
print(type(table))
import statsmodels.api as sm
contigency = sm.stats.Table(table)
print(contigency)
print(type(contigency))
