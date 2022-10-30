#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
df =pd.read_csv("C:/Users/YBUCK MAX/Desktop/Python Project/Climate change/CO2 emissions by energy source World 1990-2017  - Central and South America.csv")
df


# In[3]:


from glob import glob
# Build your `wrangle` function
def wrangle(filepath):
    df= pd.read_csv(filepath)
    return df
# Use this cell to test your wrangle function and explore the data
df = wrangle("C:/Users/YBUCK MAX/Desktop/Python Project/Climate change/CO2 emissions by energy source World 1990-2017  - Central and South America.csv")
#df
#Use glob to create the list files containing the filenames 

files = glob("C:/Users/YBUCK MAX/Desktop/Python Project/Climate change/CO2 emissions by energy source World 1990-2017*.csv")
files


# In[9]:


# Combine your wrangle function, a list comprehension
# and pd.concat to create a DataFrame df
import numpy as np
frames = []
for file in files:
    df=wrangle(file)
    frames.append(df)
    continent = ["Central and South America", "Eurasia", "Africa", "Asia Pacific", "Europe", "Middle East", "North America"]
    arr = np.repeat(continent, len(df) // len(continent))
    df['continent'] = pd.Series(arr, index=df.index[:len(arr)])
    
df = pd.concat(frames, ignore_index=True)
print(df.info())


# In[55]:


# Combine your wrangle function, a list comprehension
# and pd.concat to create a DataFrame df
import numpy as np
frames = []
for file in files:
    df=wrangle(file)
    frames.append(df)
    continent = ["Central and South America", "Eurasia", "Africa", "Asia Pacific", "Europe", "Middle East", "North America"]
    ntimes= 1 #number of times to repeat
    df['continent'] = [i for i in continent for _ in range(ntimes)] 
    #for i in range(len(continent)):
        #df.assign(continent = lambda x: continent[0:7])
        #i += 1
                  
    #df['continent'] = np.tile(np.arange(len(df)), 1)
df = pd.concat(frames, ignore_index=True)
print(df.info())


# In[56]:


df.head(10)


# In[ ]:





# In[ ]:




