import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.api import stats as sms

salary = pd.read_csv('./Salary.dat', sep='\s+')
rowlabel = ['less_than_2500 Baht', '25001 - 50000 Baht', '75001 - 100000 Baht', 'More than 100000 Baht']
collabel = ['Male', 'Female']
table = pd.crosstab(salary['salary'], salary['gender'], margins = False)
table.index = rowlabel
table.columns = collabel

table = sms.Table(table) # contingency
print(table.fittedvalues)
