# Airline case:

# An airline industry indicate that only 40% of customer proceed the online check-in.
# To increase the percentage the airline is consider to use ads to communicate with customer.
# A random sample of 400 customers and 225 customers check-in online. Use 1% significance level to test the hypothesis.

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
