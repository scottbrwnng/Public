
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression, LogisticRegressionCV
from sklearn.model_selection import train_test_split

df = pd.read_excel('/Users/scott/Desktop/Alchemy Project/Alchemy Broker Data(Cleaned, Null to Zero).xlsx', index_col='broker_name')

# Create target data set and convert it to a numpy array and get all of the targetg values except the last 'x' rows

list1 = ['GWP - 2013', 'GWP - 2014', 'GWP - 2015', 'GWP - 2017', 'GWP - 2018', 'GWP - 2019']


df = df[list1]

X_train, X_test, y_train, y_test = train_test_split(df) 

reg = LinearRegression()
reg.fit(df,df['GWP - 2019'])



plt.plot(X_train, y_train, label='Training Data', color='r', alpha =.7)
plt.plot(X_test, y_test, label='Testing Data', color='g', alpha=.7)
plt.show()

