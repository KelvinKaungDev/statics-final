from scipy.stats import ttest_ind

spar = [54, 48, 39, 99, 48, 71, 82, 37, 63, 43]
hema = [67, 23, 50, 79, 45, 55]
alpha = 0.1

tscore, pvalue = ttest_ind(spar, hema)
print('T score: ', tscore)
print('P value: ', pvalue)

if pvalue < alpha:
  print('Reject Null Hypothesis')
else:
  print('Fail to reject Null Hypothesis')
  