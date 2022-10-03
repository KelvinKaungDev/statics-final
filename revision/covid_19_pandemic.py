from statsmodels.stats.proportion import proportions_ztest

count = 22
sample = 1000
value = 0.01 # hypo value 1%
alpha = 0.1 # 10% significance level

zscore, pvalue = proportions_ztest(count, sample, value)
print('Z statistics: ', zscore)
print('P value: ', pvalue)

if pvalue < alpha:
  print('Reject Null Hypothesis')
else:
  print('Fail to reject Null Hypothesis')
