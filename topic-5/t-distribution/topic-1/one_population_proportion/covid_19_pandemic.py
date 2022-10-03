#  Covid-19 pandemic:

#  Ministry of Public Health indicated that only 1% of patient who infect covid-19 will have a serious condition.
#  However, the researcher collect 1000 patients and it found that 22 patients have a serious condition.
#  Test at 10% significance level


from statsmodels.stats.proportion import proportions_ztest

count = 22
sample = 1000
value = 0.01 # hypo value 1%
alpha = 0.1 # 10% significance level

zscore, pvalue = proportions_ztest(count, sample, value)
print('Z statistics: ', zscore)
print('P value: ', pvalue)

if pvalue < alpha:
  print('Reject Null Hypothesis')
else:
  print('Fail to reject Null Hypothesis')
