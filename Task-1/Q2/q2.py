import pandas as pd


df = pd.read_csv("Cognizance/Task-1/Q2-Dataset.csv")
print(df)
df1=df.fillna(0)
print(df1)