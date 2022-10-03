# Telecommunication:

# AIS and TRUE are the top telecommunication company in Thailand.
# Marketing research company try to collect the data randomly from 1000 people about the experience to use both service provider.
# However, it found 560 people have experienced to use AIS, whereas 486 people have experienced to use TRUE.
# Test at 2% significance level.

from statsmodels.stats.proportion import proportions_ztest
import numpy as np

alpha = 0.02
success_a, size_a = (560, 1000)
success_b, size_b = (486, 1000)

success = np.array([success_a, success_b])
size = np.array([size_a, size_b])
zscore, pvalue = proportions_ztest(success, size, alternative='two-sided')

print('Zscore: ', zscore)
print('P value: ', pvalue)

if pvalue < alpha:
  print('Reject Null Hypothesis')
else:
  print('Fail to Reject Null Hypothesis')
