# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 08:28:30 2018

@author: Editi
"""

def NumOfJweInStone(J,S):
    count = 0
    for s in S:
        if s in J:
            count += 1
        else:
            continue
    return count

jw = 'siV'
st = 'HhishiVsi'
sum = NumOfJweInStone(jw,st)
print(sum)
str.lo