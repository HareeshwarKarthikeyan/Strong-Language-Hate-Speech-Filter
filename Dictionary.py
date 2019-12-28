#!/usr/bin/env python
# coding: utf-8

# In[14]:


import numpy as np


# In[16]:


dictionary = dict()
data = open("glove.twitter.27B.200d.txt",encoding='utf8')
for line in data:
    values = line.split()
    word = values[0]
    try:
        coefs = np.asarray(values[1:],dtype='float32')
    except Exception as e:
        pass
    dictionary[word] = coefs
data.close()
    
    


# In[ ]:





# In[ ]:




