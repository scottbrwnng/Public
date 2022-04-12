
import pandas as pd
df = pd.read_csv('/Users/scott/Downloads/titanic.csv')
df.info()
print(df.value_counts('Survived'))
survived_stats = df.value_counts('Survived')
survived_ratio = survived_stats[1]/((survived_stats[0] + survived_stats[1]))


# print(f"the % who survived is {survived_ratio}")
# column = df["Age"]
# print(f"The oldest person was {column.max()} years old")
# perished_df = df.loc[df['Survived'] == 0]
# column = perished_df['Age']
# print(f"The oldest person to pass away was {column.max()} years old")

df.set_index('PassengerId')
print(df['PassengerId'].value_counts())
print(df['Age'].mean())
print(df[['PassengerId', 'Survived']])
