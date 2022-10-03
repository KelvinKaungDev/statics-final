# The doctor would like to analyze weight changes of anorexia girls who are undergoing a cognitive behavioral therapy.
# Use anorexia.dat to solve each problem

# (a)Construct 95% confidence interval for the Bayesian population mean change on the first therapy
# (b)Construct 99% confidence interval for the Bayesian population mean change on the third therapy

from itertools import groupby
import numpy as np
import pandas as pd
from scipy.stats import t

patient = pd.read_csv('http://stat4ds.rwth-aachen.de/data/Anorexia.dat', sep='\s+')
diff = patient['after'] - patient['before']
patient['diff'] = diff
first = patient.loc[patient['therapy'] == 'cb']['diff'].describe()
m1 = first.loc['mean']
s1 = first.loc['std']
n1 = first.loc['count']
first_posterior = t(loc = m1, scale = s1/np.sqrt(n1), df=n1-1)
print(first_posterior)
print(first_posterior.interval(0.95))

third = patient.loc[patient['therapy'] == 'c']['diff'].describe()
m2 = third.loc['mean']
s2 = third.loc['std']
n2 = third.loc['count']
third_posterior = t(loc = m2 , scale = s2/np.sqrt(n2), df = n2 - 1)
print(third_posterior)
print(third_posterior.interval(0.99))
