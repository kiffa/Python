# -*- coding: utf-8 -*-
"""
Created on Tue Aug  7 21:39:03 2018

@author: Editi
"""

from random import randint

class Die():
    
    def __init__(self,num_sides=6):
        self.num_sides = num_sides
        
        
    def roll(self):
        return randint(1,self.num_sides)