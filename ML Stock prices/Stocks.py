import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.linear_model import LinearRegression, LogisticRegression, LogisticRegressionCV
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
plt.style.use('bmh')

# Store the data into a frame
# Trying to fix dates being read as string, required to be float

df = pd.read_csv('/Users/scott/Desktop/GitHub/Public/ML Stock prices/NFLX.csv')

# Shows how many rows and columns
# print(df.shape)

plt.figure(figsize=(16, 8))
plt.title('Netflix')
plt.xlabel('Days')
plt.ylabel('Close price in USD ($)')
plt.plot(df['Close'])
plt.show() #Shows closing price data before prediction




df = df[['Close']]


# Create new variable to predict x days out into the future
future_days = 25


# Create new column (target) shifted x units/days up
df['Prediction'] = df[['Close']].shift(-future_days)


# Create the feature data set x and convert it to a numpy array and remove the last x rows/days
x = np.array(df.drop(['Prediction'], 1))[:-future_days]


# Create target data set (y) and convert it to a numpy array and get all of the targetg values except the last 'x' rows
y = np.array(df['Prediction'])[:-future_days]


# Split the data into 75% training and 25% Testing
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25)


# Create the models
# Create decsiion tree regressor model
tree = DecisionTreeRegressor().fit(x_train, y_train)

# Create linear regression model
lr = LinearRegression().fit(x_train, y_train)


# Get the last x rows of the feature data set
x_future = df.drop(['Prediction'], 1)[:-future_days]
x_future = x_future.tail(future_days)
x_future = np.array(x_future)


# Show the model tree prediction
tree_prediction = tree.predict(x_future)
print(tree_prediction)


# Show the model linear regression prediction
lr_prediction = lr.predict(x_future)
print(lr_prediction)

# Visualize the data
predictions = tree_prediction

valid = df[x.shape[0]:]
valid['Predictions'] = predictions
plt.figure(figsize=(16, 8))
plt.title('model')
plt.xlabel('Days')
plt.ylabel('Close Price USD ($)')
plt.plot(df['Close'])
plt.plot(valid['Close', 'Predictions'])
plt.legend(['Orig', 'Val', 'Pred'])
plt.show()
