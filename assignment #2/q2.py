import pandas as pd

df = pd.read_csv('dataSet.csv')
# print(pd.isnull(df))
# print(df[df.isna().any(axis=1)])
# print(df.head())

students = df.loc[df['Job'] == 'student']
employee = df.loc[df['Job'] == 'employee']

not_nulls_df = df[~df.isna().any(axis=1)]
not_nulls_students = not_nulls_df.loc[not_nulls_df['Job'] == 'student']
not_nulls_employee = not_nulls_df.loc[not_nulls_df['Job'] == 'employee']

mean_student_sal = not_nulls_students["Salsry"].mean()
mean_employee_sal = not_nulls_employee["Salsry"].mean()

new_students = students.fillna(mean_student_sal)
new_employee = employee.fillna(mean_employee_sal)

print("students dataframe filled with mean of their salaries:")
print(new_students)

print("employees dataframe filled with mean of their salaries:")
print(new_employee)

# df = new_students.append(new_employee)
dfs_list = [new_students, new_employee]
df = pd.concat(dfs_list)
print(df)