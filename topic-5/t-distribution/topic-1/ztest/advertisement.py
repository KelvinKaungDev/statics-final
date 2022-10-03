#  Advertisement case:

# The soft-drink industry requires the models in soft- drink ads must appear to be at most 30 years.
# Also recall that a sample of 20 people is randomly selected at a shopping mall.
# User these provided data to test the hypothesis at 5% significance level.

from statsmodels.stats.weightstats import ztest

data = [23, 26, 32, 33, 21, 29, 28, 36, 34, 41, 21, 30, 29, 37, 16, 25, 24, 23, 38, 19]
alpha = 0.05
value = 30
zscore, pvalue = ztest(data, value=30)
print('Z statistics: ', zscore)
print('P value: ', pvalue)

if pvalue < alpha:
  print('Reject Null Hypothesis')
else:
  print('Fail to reject Null Hypothesis')
