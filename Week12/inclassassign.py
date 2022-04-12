import pandas as pd
df = pd.read_csv('/Users/scott/Downloads/data.csv')
# Makes a copy of df
df2 = df.copy()
df2 = [df, df2]
# Combines df with df2
df2 = pd.concat(df2)

# Removes Maxpulse column
# df2 = df2.drop(['Maxpulse'], axis=1)     <--- Commented out for printing 13th - 18th rows
# Value of calories in 18th row
row18 = list(df2.loc[18, 'Calories'])[1]
# Std deviation of pulse
std_dev_pulse = df2['Pulse'].std()
# Finds highest pulse in sample
highest_pulse = df2['Pulse'].max()
#Mode of duration
df2mode = int(df2['Duration'].mode())
# Maxpulse rows 13-18
maxpulse = df2.iloc[13:18, df2.columns.get_loc('Maxpulse')]
# Mean calories when pulse is 90
cal = []
for x in df2['Pulse']:
    if x == 90:
        cal = df2['Calories']





print(f"The value of calories in the 18th row is {row18}")
print(f"The standard deviation of the pulse column is {std_dev_pulse}")
print(f"The highest pulse in the sample is {highest_pulse}")
print(f"The mode of the duration is {df2mode}")
print(f"The maxpulse for rows 13 through 18 is: \n{maxpulse}")
print(f"The mean calories when pulse is 90 is {cal.mean()}")
