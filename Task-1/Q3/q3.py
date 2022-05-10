import pandas as pd 
from matplotlib import pyplot as plt 

d1=dict()
dataset = []
count=0

with open("Cognizance/Task-1/abt.txt") as f:
    data=f.read()
    dataset=data.split()

for i in range( len(dataset) ):
    
    while True :

        word = dataset[i]

        if ( word[-1] == "," 
        or word[-1] == "."
        or word[-1] == ":" ) :

            dataset[i] = word[ : -1 ]

        else : break
        
for i in range (len(dataset)):
    if(len(dataset[i])>=6):
        count=count +1
    
print("\n")   

for word in dataset:
    if word in d1:
        d1[word]=d1[word]+1
    else:
        d1[word]=1  
        
print(d1)    #We could clearly see that the word "Python" repeted 4 times       
print("\nNo.of words with length >=6 are ",count )

# Now we are making a function which returns the most repeated word in the dictionary and its frequnecy 
'''
Note: ".items()" should be used as we are comparing the key vs freq in the dict.
'''
def frqword(d1):
    max =0 
    for w,f in d1.items():
        if f>max:
            max=f
            maxword=w
    return max,maxword    

max,maxword=frqword(d1)
print("\n",maxword,"Repeted ",max," times")