# -*- coding: utf-8 -*-
"""
Created on Wed Aug 29 11:40:18 2018

@author: Editi
"""

import requests
import pygal
from pygal.style import LightColorizedStyle as LCS,LightenStyle as LS

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print("Status code:", r.status_code)

response_dict = r.json()

print("Total respositories:", response_dict['total_count'])

repo_dicts = response_dict['items']
print("Respositories returned:", len(repo_dicts))

names, stars = [],[]
repo_dict = repo_dicts[0]
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])

my_style = LS('#333666', base_styles=LCS)
            
my_config = pygal.Config()
my_config.x_labels_rotation = 45
my_config.show_legend = False

chart = pygal.Bar(style=my_style,x_lable_rotation=45,shoe_legden=False)
chart.title = 'Most-Starred Python Projects on Github'
chart.x_labels = names

chart.add('', stars)
chart.render_to_file('Python_repos.svg')
              