# Google case:

# Google is the top search engine company. However, Microsoft Corporation try to develop web browser for search engine.
# Hence, researcher would like to collect the data from people randomly and it found that 410 of 500 use google search engine, while 370 from 500 use Microsoft search engine.
# Use five percent significance level to test the difference between both search engine.


from statsmodels.stats.proportion import proportions_ztest
import numpy as np

success_a, size_a = (410, 500)
success_b, size_b = (370, 500)
success = np.array([success_a, success_b])
size = np.array([size_a, size_b])
alpha = 0.05

zscore, pvalue = proportions_ztest(success, size, alternative='two-sided')

print('Zscore: ', zscore)
print('P value: ', pvalue)

if pvalue < alpha:
  print('Reject Null Hypothesis')
else:
  print('Fail to Reject Null Hypothesis')
