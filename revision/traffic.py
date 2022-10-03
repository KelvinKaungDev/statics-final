from scipy.stats import ttest_1samp

data = [55, 85, 90, 30, 45, 65, 25, 72, 103, 35]
value = 60
alpha = 0.05 # 5% significance level

tscore, pvalue = ttest_1samp(data, value)
print('T statistics: ', tscore)
print('P value: ', pvalue)

if pvalue < alpha:
  print('Time spending on the road is not at least 60min.')
else:
  print('Time spending on the road is at leat 60min.')
