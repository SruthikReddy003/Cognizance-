from sklearn.linear_model import LinearRegression
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split

df=pd.read_csv('Cognizance\Resources\Task-3\Q4.csv')
print(df)
df.plot(kind='scatter',x='bmi',y='charges')
plt.show()

# Spliting the data for supervised training
x_train,x_test,y_train,y_test=train_test_split(df.bmi,df.charges) 

plt.scatter(x_train,y_train,label='Training Data',color='r',alpha=.7)
plt.scatter(x_test,y_test,label='Testing Data',color='g',alpha=.7)
plt.legend()
plt.title("Test Train Split")
plt.show()

# Creating Linera Regression
lr=LinearRegression()
lr.fit(x_train.values.reshape(-1,1),y_train.values)
predictions = lr.predict(x_test.values.reshape(-1,1))
plt.plot(x_test,predictions,label='Linear Regression',color='b')
plt.scatter(x_test, y_test,label='Actual test data',color='g',alpha=.7)
plt.show()

#  Printing the score of the Linear Regression
print("Score of the ML algo: ",lr.score(x_test.values.reshape(-1,1),y_test.values))

