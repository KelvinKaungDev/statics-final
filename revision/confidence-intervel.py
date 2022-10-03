# The observations on number of hours of daily TV watching for the 10 subjects in the 2018 GSS who identified themselves as Islamic were 0, 0, 1, 1, 1, 2, 2, 3, 3, 4.
# (a) Construct and interpret a 95% confidence interval for the population mean.
# (b) Suppose the observation of 4 was incorrectly recorded as 24. What would you obtain for the 95% confidence interval? What does this suggest about potential effects of outliers on confidence intervals for means?

no_of_hrs = [0,0,1,1,1,2,2,3,3,4]
import statsmodels.stats.api as sms
print(sms.DescrStatsW(no_of_hrs).tconfint_mean())

no_of_hrs = [0,0,1,1,1,2,2,3,3,24]
import statsmodels.stats.api as sms
print(sms.DescrStatsW(no_of_hrs).tconfint_mean())


#import modules
import numpy as np
import scipy.stats as st
#define given sample data
data = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
#Calculate the sample parameters
confidenceLevel = 0.95   # 95% CI given
degrees_freedom = len(data)-1  #degree of freedom = sample size-1
sampleMean = np.mean(data)    #sample mean
sampleStandardError = st.sem(data)  #sample standard error
#create 95% confidence interval for the population mean
confidenceInterval = st.t.interval(alpha=confidenceLevel, df=degrees_freedom, loc=sampleMean, scale=sampleStandardError)
#print the 95% confidence interval for the population mean
print('The 95% confidence interval for the population mean :',confidenceInterval)

#import modules
import numpy as np
import scipy.stats as st
#define given sample data
data = [0, 0, 1, 1, 1, 2, 2, 3, 3, 24]
#Calculate the sample parameters
confidenceLevel = 0.95   # 95% CI given
degrees_freedom = len(data)-1  #degree of freedom = sample size-1
sampleMean = np.mean(data)    #sample mean
sampleStandardError = st.sem(data)  #sample standard error
#create 95% confidence interval for the population mean
confidenceInterval = st.t.interval(alpha=confidenceLevel, df=degrees_freedom, loc=sampleMean, scale=sampleStandardError)
#print the 95% confidence interval for the population mean
print('The 95% confidence interval for the population mean :',confidenceInterval)
