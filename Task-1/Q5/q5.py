import pandas as pandas
from matplotlib import pyplot as plt 
a=[]*171
b=[]*171
j=0
for i in range(700,2401):
    if(i%10==0):
        print("x=: ",i)
        a.append(i)   
        y=10*i**2+2*i
        b.append(y)
        j=j+1
        print("y=:",y)

contentx=str(a)
contenty=str(b)
with open("Cognizance/Task-1/houseprice.csv","w") as f:
     f.write(contentx)
     f.write(contenty)
     f.close()
            
plt.plot(a,b)
plt.grid()
font1 = {'family':'serif','color':'blue','size':20}
font2 = {'family':'serif','color':'darkred','size':15}
plt.title("Price of the houses in sq.ft",fontdict=font1 )
plt.xlabel("square feet",fontdict=font2)
plt.ylabel("Prices in 10 million",fontdict=font2)
plt.show()



