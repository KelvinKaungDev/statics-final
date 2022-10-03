# one way ANOVA example
import scipy.stats as stats

group1 = [15, 12, 13, 14, 18, 17, 17, 15, 19, 25]
group2 = [30, 32, 35, 33, 34, 30, 40, 28, 39, 35]
group3 = [42, 44, 43, 39, 38, 45, 39, 47, 43, 35]

#levene test one way
levene, pvalue = stats.levene(group1, group2, group3, center="median")

print('Levene: ', levene)
print('P value: ', pvalue)