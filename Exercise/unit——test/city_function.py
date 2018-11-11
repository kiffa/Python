# -*- coding: utf-8 -*-
"""
Created on Wed Aug  1 16:34:16 2018

@author: Editi
"""

def city_describe(city_name,city_country,city_population = ""):
    if city_population:  
        city_info = city_name + " , " + city_country + " , poplutation: " + city_population 
    else:
        city_info = city_name + " , " + city_country
    return city_info.title()

#city_name = input("Plesas input a city's name: ")
#city_country = input("Please input the city's location: ")
#print(city_describe(city_name,city_country))

