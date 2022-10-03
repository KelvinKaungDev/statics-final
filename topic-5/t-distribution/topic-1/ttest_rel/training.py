# Training program:

# The organization found that their employees lack the functional skill on business intelligence.
# Then they decide to send their employees to learn on it.
# However, they would like to test the training course is good or not by testing their employee before and after training.
# The result is provided on the following table:


from scipy.stats import ttest_rel

pre = [67, 74, 58, 45, 78, 79, 661, 83, 70, 69]
post = [89, 75, 64, 71, 80, 82, 92, 81, 73, 75]

tscore, pvalue = ttest_rel(pre, post)
print('T statistics: ', tscore)
print('P value: ', pvalue)
