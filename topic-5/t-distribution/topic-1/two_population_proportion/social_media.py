#  Social Media:

#  In the social media platform, TikTok user upload at least 1 millions short video in a day.
#  However, the researcher would like to compare the humor and education video in TikTok platform, and they found that 795 of 1000 are humor and 178 of 500 are education.
#  Test at 10% significance level.


from statsmodels.stats.proportion import proportions_ztest
import numpy as np

alpha = 0.1
success_a, size_a = (795, 1000)
success_b, size_b = (178, 500)
success = np.array([success_a, success_b])
size = np.array([size_a, size_b])

zscore, pvalue = proportions_ztest(success, size, alternative='two-sided')

print('Z score: ', zscore)
print('P value: ', pvalue)

if pvalue < alpha:
  print('Reject Null Hypothesis')
else:
  print('Fail to Reject Null Hypothesis')
