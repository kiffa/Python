# -*- coding: utf-8 -*-
"""
Created on Tue Aug  7 20:42:04 2018

@author: Editi
"""

import matplotlib.pyplot as plt

from random_walk import RandomWalk

while True:
    
    rw = RandomWalk()
    rw.fill_walk()
    
    plt.figure(dpi=128, figsize=(10, 6))
     
    point_numbers = list(range(rw.num_points))
    plt.plot(rw.x_values, rw.y_values,linewidth=1)
    plt.scatter(0,0,c='yellow', edgecolors='none',s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', 
                edgecolor='none', s=100)
    
    plt.axis('off')#隐藏坐标轴
    
    plt.show()
    
    
    keep_running = input("是否继续生成？(y/n)")
    if keep_running == 'n':
        break
    