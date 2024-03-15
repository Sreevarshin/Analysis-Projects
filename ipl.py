#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import warnings
warnings.filterwarnings('ignore')


# In[6]:


ipl=pd.read_csv(r"D:\ipl_2022_dataset.csv")
ipl.head()


# In[7]:


ipl.shape


# In[8]:


ipl.info()


# In[9]:


ipl.columns


# In[10]:


ipl.isnull().sum()


# In[11]:


ipl[ipl['Cost IN $ (000)'].isnull()]


# In[12]:


ipl['COST IN ₹ (CR.)']=ipl['COST IN ₹ (CR.)'].fillna(0)
ipl['Cost IN $ (000)']=ipl['Cost IN $ (000)'].fillna(0)


# In[13]:


ipl[ipl['2021 Squad'].isnull()]


# In[14]:


ipl['2021 Squad']=ipl['2021 Squad'].fillna('Not Participated')


# In[15]:


ipl.isnull().sum()


# In[16]:


teams= ipl[ipl['COST IN ₹ (CR.)']>0]['Team'].unique()
teams


# In[17]:


ipl['status']=ipl['Team'].replace(teams,'sold')
ipl.head()


# In[18]:


ipl[ipl['Player'].duplicated(keep=False)]


# In[19]:


#how many players participated in 2022 ipl auction?
ipl.shape[0] #gives the total no. of rows


# In[20]:


#how many types of players have participated?

types=ipl['TYPE'].value_counts()
types.reset_index()


# In[21]:


plt.pie(types.values, labels=types.index, labeldistance=1.2, autopct='%1.2f%%', shadow=True, startangle=60)
plt.title('Role of players participated', fontsize=15)
plt.plot()


# In[22]:


#players sold and unsold using a bar graph.

plt.figure(figsize=(10,5))
fig=sns.countplot(ipl['status'])
plt.xlabel('Sold or Unsold')
plt.ylabel('Number of players')
plt.title('Sold vs Unsold',fontsize=15)
plt.plot()

for p in fig.patches:
    fig.annotate(format(p.get_height(),'.0f'),(p.get_x()+ p.get_width()/2., p.get_height()), ha='center', va='center',xytext=(0,4), textcoords='offset points')


# In[23]:


ipl.groupby('status')['Player'].count()


# In[24]:


#total no. of players bought by each team.
plt.figure(figsize=(20,10))
fig=sns.countplot(ipl[ipl['Team']!='Unsold']['Team'])
plt.xlabel('Team names')
plt.ylabel('Number of players')
plt.title('Players bought by each team',fontsize=15)
plt.xticks(rotation=70)
plt.plot()
                  


                  


# In[25]:


ipl['retention']=ipl['Base Price']


# In[26]:


ipl['retention'].replace(['2 Cr','40 Lakh','20 Lakh','1 Cr','75 Lakh','50 Lakh','30 Lakh','1.5 Cr'],'From Auction',inplace=True)


# In[27]:


#treating base price
ipl['Base Price'].replace('Draft Pick',0,inplace=True)


# In[28]:


ipl['base_price unit']=ipl['Base Price'].apply(lambda x:str(x).split(' ')[-1])
ipl['base_price']=ipl['Base Price'].apply(lambda x:str(x).split(' ')[0])


# In[29]:


ipl['base_price'].replace('Retained',0,inplace=True)


# In[30]:


ipl.head()


# In[31]:


#total players retained and bought

ipl.groupby(['Team','retention'])['retention'].count()[:-1]


# In[33]:


plt.figure(figsize=(20,10))
fig=sns.countplot(ipl[ipl['Team']!='Unsold']['Team'],hue=ipl['TYPE'])
plt.xlabel('Team names')
plt.ylabel('Number of players')
plt.title('Players in each team')
plt.xticks(rotation=50)


# In[34]:


#HIGHEST AMOUNT SPENT ON A SINGLE PLAYER BY EACH TEAM

ipl[ipl['retention']=='From Auction'].groupby(['Team'])['COST IN ₹ (CR.)'].max()[:-1].sort_values(ascending=False)


# In[36]:


#player retained at maximum price
ipl[ipl['retention']=='Retained'].sort_values(by ='COST IN ₹ (CR.)',ascending=False).head(1)


# In[37]:


#top 5 bowlers
ipl[(ipl['retention']=='From Auction')&(ipl['TYPE']=='BOWLER')].sort_values(by ='COST IN ₹ (CR.)',ascending=False).head()


# In[38]:


#TOP 5 BATTERS
ipl[(ipl['retention']=='From Auction')&(ipl['TYPE']=='BATTER')].sort_values(by ='COST IN ₹ (CR.)',ascending=False).head()


# In[40]:


#TOP 5 ALL ROUNDERS
ipl[(ipl['retention']=='From Auction')&(ipl['TYPE']=='ALL-ROUNDER')].sort_values(by ='COST IN ₹ (CR.)',ascending=False).head()


# In[42]:


ipl=ipl.rename(columns={'2021 Squad':'Prev_team'})


# In[43]:


unsold_players=ipl[(ipl.Prev_team!='Not Participated')&(ipl.Team=='Unsold')][['Player','Prev_team']]


# In[44]:


print(unsold_players)


# In[ ]:




