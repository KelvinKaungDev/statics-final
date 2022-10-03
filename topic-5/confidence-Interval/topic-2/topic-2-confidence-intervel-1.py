# Anorexia Case:
# The doctor would like to analyze weight changes of anorexia girls who are undergoing a cognitive behavioral therapy.
# Use anorexia.dat to solve each problem:

# (a)Compute for the first therapy (cb) the mean and standard deviation of changes (differences between before and after)

# (b)Refer to last question, compute 95% confidence interval of mean difference

# (c)Compute 95% confidence interval between the difference of the first therapy and the control group in the experimental study

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

patient= pd.read_csv(r"/Users/kaunghtetoo/Desktop/Anorexia.dat", sep= '\s+')
print(patient.head(3))
diff = patient['after'] -patient['before']; # the mean and standard deviation of changes
patient['diff'] = diff
print(patient.loc[patient['therapy'] == 'cb']['diff'].describe())

diffCB= patient.loc[patient['therapy'] == 'cb']['diff']
import statsmodels.stats.api as sms

# conduct 95% confidence mean change
print(sms.DescrStatsW(diffCB).tconfint_mean())

#conduct 99% confidence mean change
print(sms.DescrStatsW(diffCB).tconfint_mean(alpha = 0.01))

import numpy as np
from scipy.stats import t
def t2ind_confint(y1, y2, equal_var = True, alpha = 0.05):
# y1, y2: vectors or data frames of values for groups A and B
    n1 = len(y1); n2 = len(y2)
    v1 = np.var(y1)*n1/(n1-1); v2 = np.var(y2)*n2/(n2-1)
    if equal_var:
        df=n1+n2-2
        vardiff = ((n1-1)*v1+(n2-1)*v2)/(n1+n2-2)*(1/n1 + 1/n2)
    else:
        df = (v1/n1 + v2/n2)**2/(v1**2/(n1**2*(n1-1)) + v2**2/(n2**2*(n2-1)))
        vardiff = v1/n1 + v2/n2
    se = np.sqrt(vardiff)
    qt = t.ppf(1 - alpha/2, df)      # t quantile for 100(1-alpha)% CI
    mean_diff = np.mean(y1) - np.mean(y2)
    confint = mean_diff + np.array([-1, 1]) * qt * se
    conf = 1 - alpha
    return mean_diff, confint, conf, df


cogbehav = patient.loc[patient['therapy']=='cb']['diff']
control = patient.loc[patient['therapy']=='c']['diff']

mean_diff, confint, conf, df = t2ind_confint(cogbehav,control)
## Two population sample when data have equal variance
print('mean1 - mean2 =', mean_diff)      # assume equal variances
print(conf, 'confidence interval:', confint)
print('df =', df)

## Two population sample when data have unequal variance
mean_diff, confint, conf, df = t2ind_confint(cogbehav,control, equal_var=False)
print(conf, 'confidence interval:', confint)
print('df =', df)
print(mean_diff)

import numpy as np
from scipy.stats import norm
def prop2_confint(y1, n1, y2, n2, alpha = 0.05):
# y1, y2 : numbers of successes in groups A and B
# n1, n2 : sample sizes in groups A and B
    prop1 = y1/n1; prop2 = y2/n2
    var = prop1*(1 - prop1)/n1 + prop2*(1 - prop2)/n2
    se = np.sqrt(var)
    qz = norm.ppf(1 - alpha/2)        # standard normal quantile
    prop_diff = prop1 - prop2
    confint = prop_diff + np.array([-1, 1]) * qz * se
    conf = 1 - alpha
    return prop_diff, confint, conf   # returns diff, CI, level

    # call the function for data on prayers and coronary surgery
prop_diff, confint, conf = prop2_confint(315, 604, 304, 597)
print('prop1 - prop2 =', prop_diff)
print(conf, 'confidence interval:', confint)
