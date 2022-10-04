# Computer case:

# Programmer would like to compare the execution speed (in seconds) for a standard software packages by using three different compilers.
# Programmer tests each compiler using three different computer models, and the data is shown on the provided table:
# a) Test at 5% significance level to find the difference on each computer and compiler

import numpy as np
import pandas as pd


df = pd.DataFrame({'Computer': np.repeat(['Model 1', 'Model 2', 'Model 3'], 3),
  'Compiler': np.tile(np.repeat(['Compiler 1', 'Compiler 2', ' Compiler 3'], 1), 3),
  'score': [9.9, 8.0, 7.1, 12.5, 10.6, 9.1, 10.8, 9.0, 7.8]})


print(df)

import statsmodels.api as sm
from statsmodels.formula.api import ols


model = ols('score ~ C(Computer) + C(Compiler)', data = df).fit()
print(sm.stats.anova_lm(model, tpy=2))
