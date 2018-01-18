
# coding: utf-8

# In[11]:

import numpy as np
import matplotlib.pyplot as plt

#Calling for data using numpy functions
data = np.loadtxt('co2_mm_mlo.txt')
#Selecting data to be used and assigning them a variable.
trend = np.copy(data[:,5])
month = np.copy(data[:,2])
#Establishing arrays
change = []
time = []

#Using a "for-loop" to run through selected data and compute approximate derivative using
#the "Central-Difference Method" then storing the calculated data in an array using the 
#"append function"so that we can plot it. 
for i in range(1,trend.size-1):
    s = (trend[i+1]-trend[i-1])/2
    change.append(s)

#Establishing the amount of months to plot by using a "for-loop".    
for k in range(1,month.size-1):
    time.append(k)
    
#PLotting the Change in Trend as calculated using the "Central Difference Method" versus the change
#in time
plt.scatter(time, change)    
plt.xlabel('Change in Time')
plt.ylabel('Change in Trend')
plt.title('Derivative of Seasonally Adjusted Trend')
plt.show()


# In[ ]:




# In[ ]:



