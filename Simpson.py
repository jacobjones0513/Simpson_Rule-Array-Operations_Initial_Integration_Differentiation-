
# coding: utf-8

# In[1]:

#import the math package in order to utilize sin and e in our function.

import math
import numpy as np

#Prepare for array
approx = []

#input function
def f(x):
    return math.sin(x)*math.exp(-x)

#Define trapezoid rule with limits (a,b)and width of interval or "bins" (h) using (s) to 
#represent formula in which we call the function defined above.
#The for loop will run calculations a number of times dependent upon a given N.
def trapezoid(N):
    a = 0.0
    b = math.pi
    h = (b-a)/N
    s = 0.5*f(a) + 0.5*f(b)
    for k in range(1,N):
        s += f(a+k*h)

    return(h*s)
#Print the value calculated at N=40
print(trapezoid(40))


# In[49]:

#Define simpson rule with limits (a,b) already defined above, then re-defining width of bins (h) and using (s) to 
#represent formula where we have called the function above (f(x)).
#The for loop will run calculations a number of times dependent upon a given N.
def simpson(N):
    h=(b-a)/(N)
    s=(f(a)+f(b))
    for i in range(1,int(N/2)):
        s += 4*f(a+h*2*(i-1))
    for i in range(1,int(N/2-1)):
        s += 2*f(a+2*i*h)
    s = s*h/3
    
    return s
#Print the value calculated at N=40
print(simpson(40))
      
    
    


# In[50]:

#Using an a array and numpy "savetxt" function I have called for the first 20 values calculated by the simpson and
#the trapezoid method and formatted them so that their accuracy may be compared. 
for N in range(2,41,2):
    approx.append([N,trapezoid(N),simpson(N)])
    
    savefile = np.savetxt(fname='intel.txt',X=approx,fmt='%.f %.8f %.8f',header='Bins/Trapezoid/Simpson')


# In[ ]:



