# posterior interval for a proportion using the Jeffreys prior, which is the beta(0.5, 0.5) distribution, for the example in Section 4.7.3 about the proportion believing in hell

from statsmodels.stats.proportion import proportion_confint
proportion_confint(814, 1142, method='jeffreys')    # 95% Jefferys posterior interval

import pymc3
from scipy.stats import beta

beta_dist = beta.rvs(size = 5000000, a = 814.5, b = 328.5)
print(pymc3.stats.hpd(beta_dist, alpha=0.05))       # 95% HPD interval when use Jeffreys prior

import numpy as np
print('[',np.quantile(beta_dist, 0.025),',', np.quantile(beta_dist, 0.975),']')     # ordinary 95% posterior interval


# find a posterior interval for the mean weight change of anorexic girls


# continue analysis from Section B.4.3 with Anor data file
# (required is the variable: changeCB )

# code from B.4.3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

Anor = pd.read_csv('http://stat4ds.rwth-aachen.de/data/Anorexia.dat', sep='\s+')
Anor.head(3)

change = Anor['after'] - Anor['before']
Anor['change'] = change         # add new variable to the data frame
Anor.loc[Anor['therapy'] == 'cb']['change'].describe()

bins=list(range(-10,30,5))   # histogram with pre-specified bins:
plt.hist(Anor.loc[Anor['therapy']=='cb']['change'],
                     bins, edgecolor='k')
plt.xlabel('Weight change'); plt.ylabel('Frequency')
changeCB = Anor.loc[Anor['therapy'] == 'cb']['change']

import statsmodels.stats.api as sms
sms.DescrStatsW(changeCB).tconfint_mean() # default alpha=0.05
sms.DescrStatsW(changeCB).tconfint_mean(alpha=0.01)
# code from B.4.3

import numpy as np
from pymc3 import  *

data = dict(y = changeCB)
B0=10**(-7)                     # using priors: inverse gamma
with Model() as model:
    # define highly disperse priors for variance and mean
    sigma = InverseGamma('sigma', B0, B0, testval=1.)
    intercept = Normal('Intercept', 0, sigma=1/B0)
    # define likelihood function for normal responses
    likelihood = Normal('y',mu=intercept,sigma=sigma,observed=changeCB)
    trace = sample(50000, cores=2)  # 100000 posterior samples

np.mean(trace['Intercept'])                         # mean of posterior distribution
np.std(trace['Intercept'])                          # standard deviation of posterior dist.
pymc3.stats.hpd(trace['Intercept'], alpha=0.05)     # 95% posterior interval

