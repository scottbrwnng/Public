from turtle import pd
import pandas as pd

dict = {'ID': [1001, 1002, 1003, 1004], 'Department': ['Information Systems', 'Accounting', 'Economics', 'Marketing']}

df = pd.DataFrame(dict)

new_view = df.set_index('ID')

print(new_view.loc[1001, 'Department'])