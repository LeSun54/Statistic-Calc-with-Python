
# coding: utf-8

# In[ ]:


data1 = [1,2,3,4,5,2,3,4,1,-1,-20,4,10,4,4]
import numpy as np


# In[ ]:


def mean(data):
    return (sum(data))/(len(data))
def median(data):
    sdata = sorted(data)
    index = (len(data) - 1)// 2
    return sdata [index]
def mode (data):
    modecnt = 0
    for i in range(len(data)):
        icount = data.count (data[i])
        if icount > modecnt:
            mode = data [i]
            modecnt = icount
        return mode
def variance (data):
    mu = mean (data)
    return sum([(xi - mu) **2 for xi in data])/ len(data)
def stddev (data):
    return np.sqrt(variance (data))


# In[ ]:


mean (data1)


# In[ ]:


median (data1)


# In[ ]:


mode (data1)


# In[ ]:


variance (data1)


# In[ ]:


stddev (data1)

