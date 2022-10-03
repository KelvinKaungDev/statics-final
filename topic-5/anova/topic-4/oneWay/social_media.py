# Social media:

# The researcher would like to find the difference of average spending time (minutes) on each social network platform (Facebook, YouTube, and TikTok). They randomly selected 10 people and collect their spending time. The data is illustrated as the following table:
# a)Test the equality of variance at 5%
# b)Test the difference of average spending times on each social network at 5%
# c)Test 5% significance level at Tukey HSD and draw box

import scipy.stats as stats
import pandas as pd
import numpy as np
from statsmodels.stats.multicomp import pairwise_tukeyhsd

Facebook = [34, 24, 31, 29, 30, 28, 32, 26, 37, 26]
Youtube = [84, 91, 78, 79, 82, 88, 85, 81, 90, 85]
Tiktok = [52, 54, 43, 49, 48, 55, 49, 57, 53, 55]

levene, pvalue = stats.levene(Facebook, Youtube, Tiktok, center="median")

print('Levene: ', levene)
print('P value: ', pvalue)

# a
alpha = 0.05 # equality of variance
if pvalue < alpha:
  print('Reject Null Hypothesis')
else:
  print('Fail to Reject Null Hypothesis')

anova, pvalue = stats.f_oneway(Facebook, Youtube, Tiktok)

print('ANOVA: ', anova)
print('P value: ', pvalue)

# b
alpha = 0.05 #  difference of mean (average)
if pvalue < alpha:
  print('Reject Null Hypothesis')
else:
  print('Fail to Reject Null Hypothesis')

# c
score = Facebook + Youtube + Tiktok
df = pd.DataFrame({
  'score': score,
  'groups': np.repeat(['Facebook', 'Youtube', 'Tiktok'], repeats=10)
})

tukey = pairwise_tukeyhsd(endog = df['score'], groups = df['groups'], alpha = 0.05)
print(tukey)
