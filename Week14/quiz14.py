import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

sales_dict = {"cust_id" : ['3005', '3001', '3008', '3001', '3005', '3001', '3005', '3008'],

"sales_id": ['5002', '5002', '5005', '5002', '5005', '5005', '5002', '5005'],

"purch_amt" : [152.50, 270.65, 388.12, 72, 146.33, 209.10, 176.63, 89.90]

}

df = pd.DataFrame(sales_dict)


df = df.sort_values('purch_amt', ascending=False)
print(df[['cust_id', 'purch_amt']])
print(df[['sales_id', 'purch_amt']])





















