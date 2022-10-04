#The 2018 General Social Survey (GSS) in the U.S. asked “Do you believe in hell?”
#Of the 1142 respondents, 814 said yes and 328 said no.
#The ML estimate of π is πˆ = 814/1142 = 0.713,
#and you can check that the 95% score confidence interval (4.7) is (0.686, 0.738).
#How does this compare to a Bayesian estimate and posterior interval?


from statsmodels.stats.proportion import proportion_confint
proportion_confint(814, 1142, method='jeffreys')

import pymc3
from scipy.stats import beta
beta_dist = beta.rvs(size = 5000000, a = 814.5, b = 328.5)
print(pymc3.stats.hdi(beta_dist, alpha=0.05))

import numpy as np
print('[',np.quantile(beta_dist, 0.025),',', np.quantile(beta_dist, 0.975),']')

from pymc3 import  *
import numpy as np
import pandas as pd

patient = pd.read_csv('http://stat4ds.rwth-aachen.de/data/Anorexia.dat', sep='\s+')
diff = patient['after'] - patient['before']
patient['diff'] = diff
print(patient.loc[patient['therapy'] == 'cb']['diff'].describe())
diffCB = patient.loc[patient['therapy'] == 'cb']['diff']

data = dict(y = diffCB)
B0=10**(-7)
with Model() as model:
# define highly disperse priors for variance and mean
    sigma = InverseGamma('sigma', B0, B0, testval=1.)
    intercept = Normal('Intercept', 0, sigma=1/B0)
# define likelihood function for normal responses
    likelihood = Normal('y',mu=intercept,sigma=sigma,observed=diffCB)
    trace = sample(50000, cores=2)  # 100000 posterior samples
np.mean(trace['Intercept'])

np.std(trace['Intercept'])
pymc3.stats.hdi(trace['Intercept'], alpha=0.05)
