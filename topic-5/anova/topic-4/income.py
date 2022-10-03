import pandas as pd
from statsmodels.formula.api import ols
import statsmodels.api as sm
import matplotlib.pyplot as plt

income = pd.read_csv('/Users/kaunghtetoo/Desktop/Stastics-Final/final_practise/topic-5/anova/topic-4/Salary.dat', sep='\s+')
print(income.head())

fit = ols(formula = 'income ~ C(race)', data=income).fit()
print(fit.summary())

print(sm.stats.anova_lm(fit)) # anova table

# perform tukey comparison of multiple
import statsmodels.stats.multicomp as mc
comp = mc.MultiComparison(income['income'], income['race'])
post_hoc_res = comp.tukeyhsd()
# print(post_hoc_res.summary())

post_hoc_res.plot_simultaneous(ylabel='race', xlabel='mean income difference')
fit2 = ols(formula ='income ~ C(race) + education ', data = income).fit()
print(sm.stats.anova_lm(fit2, typ=2)) # typ = 2 doesn't include mean_sq
plt.show()
