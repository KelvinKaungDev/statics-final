#  Swimming case:

#  The professional coach try to train athletic with new technology by testing pre-and-post result.
#  hey try to collect the time speed of 50M freestyle from 10 athletics and the results is provided as the following table:


from scipy.stats import ttest_rel

pre = [30, 31, 34, 40, 36, 35, 34, 30, 38, 39]
post = [30, 31, 32, 38, 32, 31, 32, 29, 28, 30]

tscore, pvalue = ttest_rel(pre, post)
print('T statistics: ', tscore)
print('P value: ', pvalue)
