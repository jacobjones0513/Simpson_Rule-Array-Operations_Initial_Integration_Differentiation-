
# coding: utf-8

# In[17]:

import numpy as np

#Load, select, and label data using numpy "loadtxt" function. 
data = np.loadtxt('co2_mm_mlo.txt')
inter = np.copy(data[:,4])
month = np.copy(data[:,1])


#Using the numpy "where" to select mpnth of December 
#Then use "squeeze" function to limit dimensionality.
december = np.where(month==12)
np.squeeze(december)

#Selecting only interpolated data during the month of December.
co2=inter[december]

#Using the "max" and "min" function to determine the highest and 
#lowest points in data set.
maximum = np.max(co2)
minimum = np.min(co2)

print(maximum, minimum)


# In[ ]:



