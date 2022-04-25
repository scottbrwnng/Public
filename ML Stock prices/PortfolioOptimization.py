# Description: This program attempts to optimize a users portfolio using the Efficient Frontier


from pypfopt import expected_returns
from pypfopt import risk_models
from pypfopt.efficient_frontier import EfficientFrontier
from matplotlib.cbook import simple_linear_interpolation
from pandas_datareader import data as web
import pandas as pd
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')

# Get portfolio stock/symbols in the portfolio
# FAANG

assets = ['FB', 'AMZN', 'AAPL', 'NFLX', 'GOOG']

# assign weights to the stocks. all weights must add up to 1
weights = np.array([0.2, 0.2, 0.2, 0.2, 0.2])

# Get stock/portfolio starting date
stockStartDate = '2013-01-01'

# Get the stocks ending date
today = datetime.today().strftime('%Y-%m-%d')
today

# Create a datafrome to store the adjusted close price of the stocks
df = pd.DataFrame()

# Store the adjusted close price of the stock into the dataframe
for stock in assets:
    df[stock] = web.DataReader(
        stock, data_source='yahoo', start=stockStartDate, end=today)['Adj Close']


# visually show the stock/portfolio
title = 'Portfolio Adj. Close Price History'

# get the stocks
my_stocks = df

# Create and plot the graph
for c in my_stocks.columns.values:
    plt.plot(my_stocks[c], label=c)


plt.title(title)
plt.xlabel('Date', fontsize=18)
plt.ylabel('Adj. Price USD ($)', fontsize=18)
plt.legend(my_stocks.columns.values, loc='upper left')
# plt.show()

# Show the daily simple returns
returns = df.pct_change()
# print(returns)

# Create and show the annualized covariance matrix
cov_matrix_annual = returns.cov() * 252
# print(cov_matrix_annual)

# Calculate the portfolio variance
port_variance = np.dot(weights.T, np.dot(cov_matrix_annual, weights))
# print(port_variance)

# Calculate the portfolio volitility aka standard deviation
port_volatility = np.sqrt(port_variance)
# print(port_volatility)

# Calculate annual portfolio return
portfolioSimpleAnnualReturn = np.sum(returns.mean() * weights) * 252
# print(portfolioSimpleAnnualReturn)

# Show the expencted annual return, volatility, and variance
percent_var = str(round(port_variance, 2) * 100) + '%'
percent_vols = str(round(port_volatility, 2) * 100) + '%'
percent_ret = str(round(portfolioSimpleAnnualReturn, 2) * 100) + '%'
print(
    f'Expected annual return: {percent_ret} \nAnnual Volatility: {percent_vols} \nAnnual Variance: {percent_var}')


# Portfolio Optimization

# Calculate the expected returns and the annualized sample covariance matrix of asset returns

mu = expected_returns.mean_historical_return(df)
s = risk_models.sample_cov(df)


# Optimize for max sharp ratio
ef = EfficientFrontier(mu, s)
weights = ef.max_sharpe()
cleaned_weights = ef.clean_weights()
print(cleaned_weights)
ef.portfolio_performance(verbose = True)

#Get the discreet allocation for each share per stock
