#!/usr/bin/env python
# coding: utf-8

#Requirements
#pip3 install requests
#pip3 install bs4


# ## Basic fundamentals of web scraping

# import these two modules bs4 for selecting HTML tags easily
from bs4 import BeautifulSoup
#from firebase_admin import db
#ref = db.reference('server/saving-data/fireblog')
# requests module is easy to operate some people use urllib but I prefer this one because it is easy to use.
import requests
import json

wiki=requests.get("https://en.wikipedia.org/wiki/List_of_California_wildfires")
soup=BeautifulSoup(wiki.text,'html')

# ### find html tags with classes

table_list = []
overview=soup.find_all('table',class_='wikitable sortable')
for z in overview:
    table_list.append(z)
    #print(z.text)

#hardcoded table location in array for now, go back later to fix
#notableFire = table_list[4]
locations = []
for i in table_list[4].findAll('a'):
    href = i.get('title')
    href = str(href)
    if 'California' in href:
        locations.append(href)
    else:
        continue

jsonF = json.dumps(locations)
with open('firelocdata.json', 'w') as f:
    json.dump(locations, f)
