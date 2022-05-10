import pandas as pd
import numpy as np


df=pd.read_csv("Cognizance/Task-1/Q4-Dataset.csv")
# print(df)

a=np.array(df)
# print(a)

b=a[:,2]
c=(np.argsort(b))
print(a[c])
