#!/usr/bin/env python
# coding: utf-8

# In[2]:


import requests


# In[4]:


req = requests.get("https://en.wikipedia.org/wiki/Harvard_University")


# In[5]:


req


# In[6]:


type(req)


# In[7]:


dir(req)


# In[8]:


page = req.text
page


# In[9]:


from bs4 import BeautifulSoup


# In[10]:


soup = BeautifulSoup(page, 'html.parser')


# In[11]:


soup


# In[12]:


type(page)


# In[13]:


type(soup)


# In[14]:


print(soup.prettify())


# In[15]:


soup.title


# In[16]:


"title" in dir(soup)


# In[17]:


soup.p


# In[18]:


len(soup.find_all("p"))


# In[19]:


soup.table["class"]


# In[20]:


[t["class"] for t in soup.find_all("table") if t.get("class")]


# In[21]:


my_list = []
for t in soup.find_all("table"):
    if t.get("class"):
        my_list.append(t["class"])
my_list


# In[22]:


table_html = str(soup.find_all("table", "wikitable")[2])


# In[23]:


from IPython.core.display import HTML

HTML(table_html)


# In[24]:


rows = [row for row in soup.find_all("table", "wikitable")[2].find_all("tr")]
rows


# In[25]:


rem_nl = lambda s:s.replace("\n", "")


# In[26]:


def power(x, y):
    return x**y

power(2, 3)


# In[27]:


def print_greeting():
    print("Hello!")
    
print_greeting()


# In[28]:


def get_multiple(x, y=1):
    return x*y

print("With x and y: ", get_multiple(10, 2))
print("With x only: ", get_multiple(10))


# In[29]:


def print_special_greeting(name, leaving=False, condition="nice"):
    print("Hi", name)
    print("How are you doing in this", condition, "day?")
    if leaving:
        print("Please come back!")


# In[30]:


print_special_greeting("John")


# In[31]:


print_special_greeting("John", True, "rainy")


# In[32]:


print_special_greeting("John", True)


# In[33]:


print_special_greeting("John", condition="horrible")


# In[34]:


def print_siblings(name, *siblings):
    print(name, "has the following siblings:")
    for sibling in siblings:
        print(sibling)
    print()
        
print_siblings("John", "Ashley", "Lauren", "Arthur")
print_siblings("Mike", "John")
print_siblings("Terry")


# In[35]:


def print_brothers_sisters(name, **siblings):
    print(name, "has the following siblings:")
    for sibling in siblings:
        print(sibling, ":", siblings[sibling])
    print()
    
print_brothers_sisters("John", Ashley="sister", Lauren="sister", Arthur="brother")


# In[36]:


columns = [rem_nl(col.get_text()) for col in rows[0].find_all("th") if col.get_text()]
columns


# In[51]:


indexes = [rem_nl(row.find("th").get_text()) for row in rows[1:]]
indexes


# In[38]:


HTML(table_html)


# In[40]:


to_num = lambda s: s[-1] == "%" and int(s[:-1]) or None


# In[41]:


values = [to_num(rem_nl(value.get_text())) for row in rows[1:] for value in row.find_all("td")]
values


# In[50]:


stacked_values = zip(*[values[i::3] for i in range(len(columns))])
list(stacked_values)


# In[43]:


HTML(table_html)


# In[44]:


def print_args(arg1, arg2, arg3):
    print(arg1, arg2, arg3)

print_args(1, 2, 3)

print_args([1, 10], [2, 20], [3, 30])


# In[45]:


parameters = [100, 200, 300]

p1 = parameters[0]
p2 = parameters[1]
p3 = parameters[2]

print_args(p1, p2, p3)


# In[46]:


p4, p5, p6 = parameters

print_args(p4, p5, p6)


# In[47]:


print_args(*parameters)


# In[52]:


{ind: value for ind, value in zip(indexes, stacked_values)}


# In[53]:


import pandas as pd


# In[54]:


stacked_values = zip(*[values[i::3] for i in range(len(columns))])
df = pd.DataFrame(stacked_values, columns=columns, index=indexes)
df


# In[55]:


HTML(table_html)


# In[56]:


columns = [rem_nl(col.get_text()) for col in rows[0].find_all("th") if col.get_text()]
stacked_values = zip(*[values[i::3] for i in range(len(columns))])
data_dicts = [{col: val for col, val in zip(columns, col_values)} for col_values in stacked_values]
data_dicts


# In[57]:


pd.DataFrame(data_dicts, index=indexes)


# In[58]:


stacked_by_col = [values[i::3] for i in range(len(columns))]
stacked_by_col


# In[59]:


data_lists = {col: val for col, val in zip(columns, stacked_by_col)}
data_lists


# In[60]:


pd.DataFrame(data_lists, index=indexes)


# In[61]:


df.dtypes


# In[62]:


df.dropna()


# In[63]:


df.dropna(axis=1)


# In[64]:


df_clean = df.fillna(0).astype(int)
df_clean


# In[65]:


df_clean.dtypes


# In[66]:


df_clean.describe()


# In[67]:


import numpy as np


# In[68]:


df_clean.values


# In[69]:


type(df_clean.values)


# In[70]:


np.mean(df_clean.Undergrad)


# In[71]:


np.std(df_clean)


# In[72]:


df_clean["Undergrad"]


# In[73]:


df_clean.Undergrad


# In[74]:


df_clean.iloc[0]


# In[75]:


df_clean.ix["Asian/Pacific Islander"]


# In[76]:


df_clean.ix[0]


# In[77]:


df_clean.loc["White/non-Hispanic", "Graduate"]


# In[78]:


df_clean.iloc[3, 1]


# In[79]:


df_clean.ix[3, "Graduate"]


# In[80]:


df_flat = df_clean.stack().reset_index()
df_flat.columns = ["race", "source", "percentage"]
df_flat


# In[81]:


grouped = df_flat.groupby("race")
grouped.groups


# In[82]:


type(grouped)


# In[83]:


mean_percs = grouped.mean()
mean_percs


# In[84]:


type(mean_percs)


# In[85]:


for name, group in df_flat.groupby("source", sort=True):
    print(name)
    print(group)


# In[86]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[87]:


mean_percs.plot(kind="bar");

