import pandas as pd
from scipy.stats import chi2_contingency

df = pd.read_csv('dataSet.csv')

# jobs = df['Job'].unique()
# buy_or_not = df['Buy Computer'].unique()

contingency = pd.crosstab(df['Job'],df['Buy Computer'], margins=True)
print(contingency)

stat, p, dof, expected = chi2_contingency(contingency)
print(f'\ndegree of freedom = {dof}')
print(f'chi2 = {stat}')
print(f'p value = {p}\n')

# for dof == 4 and 0.05 as critical value, we have 9.488
alpha = 9.488

if stat > alpha:
    print('-> Variables are positively related.')
elif stat < alpha:
    print('-> Variables are negetively related.')
else:
    print('-> Variables are not related.')