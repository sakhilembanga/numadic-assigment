#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


df = pd.read_csv('C:/Users/Deviare User/Downloads/EV_Registration_Dataset.csv')


# In[4]:


df


# In[5]:


df.isnull()


# In[6]:


df.isnull().sum()


# In[7]:


df = df.dropna()
df


# In[9]:


print(df.duplicated())


# In[11]:


print(df.drop_duplicates())


# I could not find an errors to be corrected.

# In[ ]:




