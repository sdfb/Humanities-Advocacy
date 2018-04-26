
# coding: utf-8

# In[28]:

import json
from requests import get
from bs4 import BeautifulSoup
  


# In[29]:



state = 'PA'  ## enter two-letter state abbreviation
district = '14'  ## enter congressional district
url = 'https://securegrants.neh.gov/publicquery/main.aspx?q=1&a=0&n=0&o=0&ot=0&k=0&f=0&s=1&sv={0}&cd=1&cdv={1}&p=0&d=0&y=1&yf=2010&yt=2018&prd=0&cov=0&prz=0&wp=0&ob=year&or=DESC'.format(state, district)

## For all congressional districts in the state, use the following url ## 

# url = 'https://securegrants.neh.gov/publicquery/main.aspx?q=1&a=0&n=0&o=0&ot=0&k=0&f=0&s=1&sv={0}&cd=1&p=0&d=0&y=1&yf=2010&yt=2018&prd=0&cov=0&prz=0&wp=0&ob=year&or=DESC'.format(state)

response = get(url)
grants = response.text
soup = BeautifulSoup(grants, 'html.parser')
grantees = soup.find_all("span", class_="largeplain")
titles = soup.find_all("span", class_="largeitalic")
grantees_list = []
titles_list = []

for g in grantees:
    grantees_list.append(g.get_text())
for t in titles:
    titles_list.append(t.get_text())
length = len(grantees_list)
grants = {}
for i in range(0,length):
    grants[titles_list[i]] = grantees_list[i]
for key, value in grants.items():
    print(key, value)


# In[ ]:



