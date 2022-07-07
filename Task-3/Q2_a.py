import numpy as np 
import pandas as pd
np.random.seed(100) 
a = np.random.uniform(1,50, 20)
print(a)
b=np.clip(a,15,45)
print(b)