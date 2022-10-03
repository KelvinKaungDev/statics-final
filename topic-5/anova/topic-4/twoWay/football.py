# Football game:

# The researcher would like to test the difference goal in football match.
# They decide to collect the data from the first 3 week of the league (first, second and third) from each team (home and away).
# The data is provided as the following table:
# a) Test 5% significance level at both factors and interaction


import numpy as np
import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols

df = pd.DataFrame({
  'week': np.repeat(['first', 'second', 'third'], 10),
  'match': np.tile(np.repeat(['home', 'away'], 5), 3),
  'score': [23, 24, 22, 28, 30, 14, 15, 18, 13, 20,
            31, 33, 28, 30, 25, 21, 22, 25, 21, 19,
            35, 34, 32, 30, 28, 26, 24, 21, 25, 20]
})

print(df)
model = ols('score ~ C(week) + C(match) + C(week):C(match)', data=df).fit()
anova_lm = sm.stats.anova_lm(model, typ =2)
print(anova_lm)
