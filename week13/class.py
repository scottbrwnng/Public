
import pandas as pd
import numpy as np

people = {
    'first': ['Corey', 'Jane', 'John', 'Chris', np.nan, None, 'NA'],
    'last': ['Schafer', 'Doe', 'Doe', 'Schafer', np.nan, np.nan, 'Missing'],
    'email': ['Corey.Schafer@gmail.com', 'JaneDoe@gmail.com', 'JohnDoe@gmail.com', None, np.nan, np.nan, 'Missing'],
    'age': ['33', '55', '63', '36', None, None, 'Missing']
}

df = pd.DataFrame(people)

# df = df['age'].replace('Missing', 'zero')
df = df.fillna(method='ffill', axis=1)

