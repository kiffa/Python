# -*- coding: utf-8 -*-
"""
Created on Wed May 30 18:41:04 2018

@author: hasee
"""

import requests
from bs4 import BeautifulSoup
import re
sum = 0
r = requests.get('https://book.douban.com/subject/27199470/comments/')
soup = BeautifulSoup(r.text,'lxml')
pattern = soup.find_all('p','commen-content')
for item in pattern:
    print(item,string)
pattern_s = re.compile('<span class="user-stars allstar(.*?)rating"')
p = re.findall(pattern_s,r.text)
for star in p:
    sum += int(star)
print(sum)
