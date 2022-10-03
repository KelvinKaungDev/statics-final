from scipy.stats import ttest_1samp

weather = [26.5, 28.1, 29.4, 30.5, 30.1, 29.4, 29, 28.8, 28.6, 28.3, 27.5, 26.1]
pop_mean = 30 # average 30 deg
alpha = 0.05
tscore, pvalue = ttest_1samp(weather, pop_mean)
print('T statistics: ', tscore)
print('P value: ', pvalue)

if pvalue < alpha:
  print('The average temp is not 30 degree.')
else:
  print('The temp is average at 30 degree.')