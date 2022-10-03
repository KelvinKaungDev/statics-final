from scipy.stats import ttest_rel

pre = [30, 31, 34, 40, 36, 35, 34, 30, 38, 39]
post = [30, 31, 32, 38, 32, 31, 32, 29, 28, 30]

tscore, pvalue = ttest_rel(pre, post)
print('T statistics: ', tscore)
print('P value: ', pvalue)
