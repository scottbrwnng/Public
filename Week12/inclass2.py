import pandas as pd
import numpy as np

# Create and reshape lists
df = np.arange(0, 20)
df = np.reshape(df, (4, 5))

df1 = np.arange(0, 25)
df1 = np.reshape(df1, (5, 5))

# Combines together
df = pd.DataFrame(df)
df1 = pd.DataFrame(df1)
frames = [df, df1]
df2 = pd.concat(frames)
print(df2)

# Replaces all values with 72
df3 = df2.mask(df2 < 100, 72)
print(df3)

# prints summary stats
print(df3.describe())
