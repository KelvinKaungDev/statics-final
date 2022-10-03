from statsmodels.stats.proportion import proportions_ztest

count = 225
sample = 400
value = 0.4
alpha = 0.01
zscore, pvalue = proportions_ztest(count, sample, value)

print('Z statistics: ', zscore)
print('P value: ', pvalue)

if pvalue < alpha:
  print('Reject Null Hypothesis')
else:
  print('Fail to reject Null Hypothesis')
