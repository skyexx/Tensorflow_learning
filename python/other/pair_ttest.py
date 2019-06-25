from scipy import stats
import pandas as pd
import numpy as np
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm
from statsmodels.stats.multicomp import pairwise_tukeyhsd

paired = pd.read_csv("pair_ttest.csv")
paired.head()
t,p=stats.ttest_rel(paired["A"],paired["B"])
stats.ttest_1samp(paired,0)
