## Practice #1

# Anorexia Case:
# The doctor would like to analyze weight changes of anorexia girls who are undergoing a cognitive behavioral therapy.
# Use anorexia.dat to solve each problem:

# (a)Compute for the first therapy (cb) the mean and standard deviation of changes (differences between before and after)

# (b)Refer to last question, compute 95% confidence interval of mean difference

# (c)Compute 95% confidence interval between the difference of the first therapy and the control group in the experimental study

import numpy as np
import pandas as pd

Anor = pd.read_csv(r"C:\Users\iamte\Downloads\Anorexia.dat", sep = '\s+')
#print(Anor.head(3))
diff =  Anor['after'] - Anor['before']
Anor['diff'] = diff
print(Anor.loc[Anor['therapy'] == 'cb']['diff'].describe())

changeCB = Anor.loc[Anor['therapy'] == 'cb']['diff']

import statsmodels.stats.api as sms

# Q1A) conduct 95% confidence mean change
print(sms.DescrStatsW(changeCB).tconfint_mean())

# Q1B) conduct 99% confidence mean change
print(sms.DescrStatsW(changeCB).tconfint_mean(alpha = 0.01))

from scipy.stats import t
import numpy as np

def t2ind_confint(y1, y2, equal_var=True, alpha = 0.05):
    n1 = len(y1)
    n2 = len(y2)
    var1 = np.var(y1)*n1/(n1-1)
    var2 = np.var(y2)*n2/(n2-1)

    if equal_var:
        df = n1 + n2 - 2
    else:
        df = (var1 / n1 + var2 / n2)**2 / (var1**2 / (n1**2 * (n1 - 1)) +
                                           var2**2 / (n2**2 * (n2 - 1)))

    mean_diff = np.mean(y1) - np.mean(y2)
    confint = mean_diff + np.array([-1, 1])
    conf = 1 - alpha
    return mean_diff, confint, conf, df

Anor = pd.read_csv(r"C:\Users\iamte\Downloads\Anorexia.dat", sep = '\s+')
diff =  Anor['after'] - Anor['before']
Anor['diff'] = diff
cogbehav = Anor.loc[Anor['therapy'] == 'cb']['diff']
control = Anor.loc[Anor['therapy'] == 'c']['diff']

## Two population sample when data have equal variance
mean_diff, confint, conf, df = t2ind_confint(cogbehav, control)
print('Mean1 - Mean2 =', mean_diff)
print(conf, 'Confidence Interval: ', confint)


## Two population sample when data have unequal variance
mean_diff, confint,conf, df = t2ind_confint(cogbehav, control, equal_var=False)
print('Mean1 - Mean2 = ', mean_diff)
print(conf, 'Confidence Interval: ', confint)
