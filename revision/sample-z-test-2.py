# Q1) Traffic case:

# Thai people spend at least 60 minutes on the road everyday.
# However, Ministry of transport believe that BTS and MRT can reduce the time spending on the road.
# Then they decide to collect the data from 10 randomly people and test the hypothesis at 5% significance level.

from statsmodels.stats.weightstats import ztest
data = [55, 85, 90, 30, 45, 65, 25, 72, 103, 35]
alpha = 0.05
zscore, pvalue= ztest(data, value = 60)
print("Z statistics: ", zscore)
print("P value: ", pvalue)

if( pvalue< alpha):
    print("Reject Null Hypothesis")
else:
    print("Fail to reject Null Hypothesis")
