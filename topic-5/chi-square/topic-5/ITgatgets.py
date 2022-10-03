# IT gadgets case:

# The IT company wishes to study the relationship between gender and IT gadget consumption.
# The survey randomly selected people are

import numpy as np
from scipy.stats import chi2_contingency
import pandas as pd

# H0 -> test if 2 categories are different
data = [[65, 37, 45], [26, 74, 55]]
df = pd.DataFrame({
  'Gender': np.repeat(['Male', 'Female'], 3),
  'Gatgets' : np.tile(np.repeat(['Smart Watch', 'Earbuds', 'Tablet'], 1), 2),
  'score': [65, 37, 45, 26, 74, 55],
})

print(df)
chi_stat, p, dof, expected = chi2_contingency(data)
a = chi2_contingency(data)
alpha = 0.5
if p <= alpha:
  print('Reject Null Hypothesis')
else:
  print('Fail to Reject Null Hypothesis')
