
import pandas as pd
import numpy as np
filename = '/Users/scott/Downloads/medical_analysis.txt'
filename2 = '/Users/scott/Downloads/survey_results_public.csv'

df = pd.read_csv(filename, sep='\t', index_col='ID')
df2 = pd.read_csv(filename2, index_col='ResponseId')

# Replaces values equal to 'Less than 1 year' in yearscode column
df2['YearsCode'].replace('Less than 1 year', 0, inplace=True)
df2['YearsCode'].replace('More than 50 years', 50, inplace=True)


df2.YearsCode.unique()  # Prints all unique values
df2.YearsCode.astype(float)  # Changes YearsCode dtype
df2.YearsCode.median()

df2.columns

df2.LanguageHaveWorkedWith.str.contains('Python').sum()
df2.LanguageHaveWorkedWith.str.contains('C#').sum()
df2.LanguageHaveWorkedWith.value_counts()
