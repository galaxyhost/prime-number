#!/usr/bin/env python
# coding: utf-8

# In[38]:


import math
flag =0
lists =[]
for i in range(10,100):
    flag=0
    for j in range(2,i):
        
            if(i%j==0):
                flag=1
                break
                
    if(flag==0):    
        lists.append(i)
print(lists)
              
              
    


# In[ ]:




