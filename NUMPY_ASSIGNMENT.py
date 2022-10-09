#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np


# In[52]:


# 1. Create a null vector of size 10 but the fifth value which is 1.

null_array=np.zeros(10)
null_array[4]=1
print(null_array)


# In[25]:


# 2. Create a vector with values ranging from 10 to 49.


array2=np.arange(10,50)
array2


# In[28]:


# 3. Create a 3x3 matrix with values ranging from 0 to 8


array3=np.arange(0,9).reshape(3,3)
array3


# In[35]:


# 4. Find indices of non-zero elements from [1,2,0,0,4,0]
array4=[1,2,0,0,4,0]

print(np.nonzero(array4))


# In[45]:


# 5. Create a 10x10 array with random values and find the minimum and maximum values.

array5=np.random.rand(10,10)
print(array5)


print("max value of array is " ,array5.max())

print("min value of array is " ,array5.min())


# In[48]:


# 6. Create a random vector of size 30 and find the mean value.

array6=np.random.rand(30)
print(array6)
print("mean value of an array is " ,array6.mean())


# In[ ]:




