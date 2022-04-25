import pandas as pd
import numpy as np
import sklearn
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression

a = {
    'Company_Name': ['a', 'b', 'c'],
    'Revenue - 2005':[500, 130, 502],
    'Revenue - 2006': [204, 503, 103],
    'Revenue - 2007': [5493, 493, 202],
    'Revenue - 2008': [np.nan, np.nan, np.nan],
}

df = pd.DataFrame(a)
xs = []

for x in df.iterrows():
    xs.append(x)
X = xs
y = LogisticRegression.predict(X)
y


