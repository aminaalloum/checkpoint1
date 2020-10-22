#!/usr/bin/env python
# coding: utf-8

# In[9]:


listofnumbers = []
for i in range (2000,3201):
    if (i%7==0 and i%5 !=0 ):
        listofnumbers.append(i)
        print(listofnumbers)
        
        
    
    


# In[10]:


x= input ("donner un nombre:")
x


# In[14]:


x= int(input("donner un nombre :"))
x 


# In[ ]:


def fact(x):
    f=1
    for i in range (1,x+1):
x= int(input("nombre:"))
 f=f*i
return f
print (fact(x))


# In[3]:


dictio={}

for i in range (1,12) :
    n=i*i
    dictio[i]={n}
    
    print(dictio)
    


# In[4]:


import numpy as np
array=np.array([[0, 1] ,[2 ,3] ,[4, 5]])
list=array.tolist()
list


# In[5]:


x=[0,1,2]
y=[2,1,0]
np.cov(x,y)


# In[ ]:


import numpy as np
import random
import math
c=50
h=30
x=int(input)
np.sqrt[(2*c*d)/h]


# In[ ]:




