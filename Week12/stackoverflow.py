import pandas as pd

df = pd.read_csv('/Users/scott/Downloads/stack-overflow-developer-survey-2021/survey_results_public.csv')
df.set_index('ResponseId')
# print(df.shape)
# print(df.head(10), df.tail(10))
# print(df.value_counts('YearsCodePro'))
print(df.value_counts('ResponseId')).plot.bar()