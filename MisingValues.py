#!/usr/bin/env python
# coding: utf-8

# In[22]:


import pandas as pd
data=pd.read_csv('F:\Study Material\Python\Data_Preprocessing\Data.csv')


# In[27]:


list(data.columns)


# In[28]:


data


# In[23]:


x=data.iloc[:,:-1].values


# In[24]:


x


# In[25]:


from sklearn.preprocessing import Imputer
imputer=Imputer(missing_values='NaN',strategy='mean',axis=0)
imputer=imputer.fit(x[:,1:3])
x[:,1:3]=imputer.transform(x[:,1:3])


# In[26]:


x


# In[ ]:




