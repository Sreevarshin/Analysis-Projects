#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[3]:


df_genre=pd.read_csv(r"D:\SpotifyFeatures.csv")


# In[4]:


df_genre.head()


# In[5]:


plt.title("Duration of the songs in different genres")
sns.color_palette("rocket",as_cmap=True)
sns.barplot(y='genre',x='duration_ms',data=df_genre)
plt.xlabel("Duration in milliseconds")
plt.ylabel("Genres")


# In[6]:


sns.set_style(style="darkgrid")
plt.figure(figsize=(10,5))
famous=df_genre.sort_values("popularity",ascending=False).head(10)
sns.barplot(y='genre',x='popularity',data=famous).set(title="Top 5 geners by popularity")


# In[ ]:




