#!/usr/bin/env python
# coding: utf-8

# In[2]:


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


# In[4]:


# Combine your wrangle function, a list comprehension
# and pd.concat to create a DataFrame df
#import numpy as np
#frames = []
#for file in files:
    #df=wrangle(file)
    #frames.append(df)
    #continent = ["Central and South America", "Eurasia", "Africa", "Asia Pacific", "Europe", "Middle East", "North America"]
    #ntimes= 1 #number of times to repeat
    #df['continent'] = [i for i in continent for _ in range(ntimes)] 
#df = pd.concat(frames, ignore_index=True)


# In[5]:


# Combine your wrangle function, a list comprehension
# and pd.concat to create a DataFrame df
import numpy as np
frames = []
for file in files:
    df=wrangle(file)
    frames.append(df)
df = pd.concat(frames, ignore_index=True)
print(df.info())


# In[13]:


#Add a column for continent in existing dataframe 
continent = ["Central and South America", "Eurasia", "Africa", "Asia Pacific", "Europe", "Middle East", "North America"]
continent = [
    c for c in continent
    for _ in range(len(df) // len(continent))
]

df['continent'] = continent


# In[14]:


df.head(10)


# In[15]:


df.describe()


# In[16]:


#Percentage of missing values in the dataframe and dropping the other column
df.isnull().sum()/len(df)
df.drop(["Other"], axis=1)


# In[71]:


#Loading the emission data for the world and reporting the emisison data

df1 =pd.read_csv("C:/Users/YBUCK MAX/Desktop/Python Project/Climate change/CO2 emissions by energy source - World.csv")
df1
import plotly.express as px

fig1 = px.line(df1, x='Year', y=['Coal', 'Oil', 'Natural gas', 'Other'], title='The Planets Emissions by Year and Type', labels={
    "value":"Carbon Emissions",
    "variable":"Source"
})
fig1


# In[73]:


df_cont = df.groupby(["continent"])['Coal', 'Oil', 'Natural gas'].mean()
df_cont.plot()
plt.xticks(rotation=45)
plt.rcParams["figure.figsize"] = (20, 12)
plt.show()


# In[49]:


#Percentage of change in emission for Central and South America between 1990 to 2017
print("Central and South America")
df_CS_America = df.loc[df['continent'] == "Central and South America"]
df_CS_America[['Coal','Oil','Natural gas']].pct_change()


# In[54]:


#Percentage of change in emission for Eurasia between 1990 to 2017
print("Eurasia")
df_Eurasia = df.loc[df['continent'] == "Eurasia"]
df_Eurasia[['Coal','Oil','Natural gas']].pct_change()


# In[51]:


#Percentage of change in  emission for AFRICA between 1990 to 2017
print("Africa")
df_Africa = df.loc[df['continent'] == "Africa"]
df_Africa[['Coal','Oil','Natural gas']].pct_change()


# In[55]:


#Percentage of change in  emission for Asia Pacific between 1990 to 2017
print("Asia Pacific")
df_Asia_Pacific = df.loc[df['continent'] == "Asia Pacific"]
df_Asia_Pacific[['Coal','Oil','Natural gas']].pct_change()


# In[62]:


#Percentage of change in  emission for Europe between 1990 to 2017
print("Europe")
df_Europe = df.loc[df['continent'] == "Europe"]
df_Europe[['Coal','Oil','Natural gas']].pct_change()


# In[57]:


#Percentage of change in  emission for Middle East between 1990 to 2017
print("Middle East")
df_Middle_East = df.loc[df['continent'] == "Middle East"]
df_Middle_East[['Coal','Oil','Natural gas']].pct_change()


# In[68]:


#Percentage of change in  emission for Asia Pacific between 1990 to 2017
print("North America")
df_North_America = df.loc[df['continent'] == "North America"]
df_North_America[['Coal','Oil','Natural gas']].pct_change()


# In[67]:


#top 5 polluters of the world
#df_coal = df.groupby(["Year"])['Coal'].mean().sort_values()
#df_coal.head()


#What continent has the smallest carbon pollution

#What continent is closest to being neutral fossil usage over the decades?


# In[ ]:





# In[ ]:




