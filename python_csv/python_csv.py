#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os


# In[2]:


os.getcwd()


# In[4]:


path = "C:\\Users\\User\Documents\Programming\st2195_assignment_2"


# In[6]:


os.chdir(path)


# In[7]:


os.getcwd()


# In[8]:


import beautifulsoup as bs4


# In[9]:


from bs4 import BeautifulSoup
import pandas as pd
import requests
import csv


# In[10]:


url = "https://en.wikipedia.org/wiki/Comma-separated_values"


# In[11]:


r = requests.get(url)


# In[12]:


html_content = r.text


# In[13]:


soup = BeautifulSoup (html_content, "html.parser")


# In[14]:


print(soup.prettify)


# In[15]:


print(soup.title.name)


# In[16]:


print(soup.title)


# In[17]:


print(soup.title.name)


# In[19]:


print(soup.title.string)


# In[21]:


print(soup.title.parent.name)


# In[22]:


ths = soup.find(id = "Example")


# In[23]:


table = ths.findNext('pre').text


# In[24]:


print(table)


# In[25]:


t1 = ths.findNext('pre')


# In[26]:


t2 = t1.findNext('pre')


# In[27]:


print(t2)


# In[29]:


f = open('car.csv', 'w')


# In[30]:


f.write(table)


# In[31]:


f.close()


# In[32]:


df2 = pd.read_csv('car.csv')


# In[33]:


df2


# In[ ]:





# In[ ]:




