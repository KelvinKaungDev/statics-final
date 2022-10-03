# Computer case:

# Programmer would like to compare the execution speed (in seconds) for a standard software packages by using three different compilers.
# Programmer tests each compiler using three different computer models, and the data is shown on the provided table:
# a) Test at 5% significance level to find the difference on each computer and compiler

import numpy as np
import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols

df = pd.DataFrame({
  'computer': np.repeat(['Model1', 'Model2', 'Model3'], 3),
  'compiler': np.tile(np.repeat(['1','2','3'], 1), 3),
  'score': [9.9, 8.0, 7.1, 12.5, 10.6, 9.1, 10.8, 9.0, 7.8]
})
print(df)

model = ols('score ~ C(computer) + C(compiler) + C(computer):C(compiler)', data=df).fit()
anova_lm = sm.stats.anova_lm(model, type= 2)
print(anova_lm)
