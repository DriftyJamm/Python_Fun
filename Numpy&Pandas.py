import pandas as pd
import numpy as np

data = {
    'Name': ['Alice', 'Bob', 'Charlie', np.nan, 'Eve'],
    'Age': [25, np.nan, 30, 22, 29],
    'Salary': [50000, 54000, np.nan, 43000, 60000],
    'Department': ['HR', 'Finance', 'IT', 'HR', np.nan]
}

df = pd.DataFrame(data)
print(df)

df['Name'].fillna('Unknown', inplace=True)
df['Salary'].fillna(df['Salary'].mean(), inplace=True)
df.dropna(subset=['Department'], inplace=True)
df['Age'].fillna(df['Age'].median(), inplace=True)
print(df)

mean_salary = np.mean(df['Salary'])
print("Mean Salary:", mean_salary)

max_age = np.max(df['Age'])
print("Max Age:", max_age)

sorted_df = df.sort_values(by='Age')
print(sorted_df)

avg_salary = df.groupby('Department')['Salary'].mean()
print(avg_salary)


