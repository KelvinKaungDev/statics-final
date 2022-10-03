# Netflix case:
# Netflix would like to study the relationship between viewership program and viewer age (18 years or less, 19 –35 years, 36 –59 years and 60 years or older).
# A sample of 250 Netflix viewers in each age group is randomly selected and the results was shown in the following table:
# test the hypothesis at 5% significant level

import numpy as np
from scipy.stats import chi2_contingency

data = [[213, 202, 154, 73], [37, 48, 96, 177]]
chi, p, df, expected = chi2_contingency(data)

print('P value: ')
alpha = 0.05
if p < alpha:
  print('Reject Null Hypothesis')
else:
  print('Fail to Reject Null Hypothesis')
