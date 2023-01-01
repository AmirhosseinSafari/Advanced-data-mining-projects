import pandas as pd

df = pd.read_csv('dataSet.csv')

# print(df[['Job', 'Salsry']])

# Mapping jobs to integers
jobs = {
    'student': 0,
    'employee': 1
}

df["Job"] = df["Job"].map(lambda x: jobs[x])

correlation = df['Job'].corr(df['Salsry'])

print(f'correlation = {correlation}')

if correlation > 0:
    print('-> Variables are positively related.')
elif correlation < 0:
    print('-> Variables are negetively related.')
else:
    print('-> Variables are not related.')