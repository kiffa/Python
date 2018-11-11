# -*- coding: utf-8 -*-
"""
Created on Tue Aug  7 18:03:14 2018

@author: Editi
"""

import matplotlib.pyplot as plt

input_values = [1,2,3,4,5]
squares = [1,4,9,16,25]
#plt.plot(input_values,squares,linewidth=5)

#设置标题，并给坐标轴加标签
plt.title("Squares Table", fontsize=24)
plt.xlabel("Value",fontsize=14)
plt.ylabel("Square of value",fontsize=14)

#设置刻度标记大小
plt.tick_params(axis='both',labelsize=14)
plt.plot(input_values,squares,linewidth=5)
plt.show()