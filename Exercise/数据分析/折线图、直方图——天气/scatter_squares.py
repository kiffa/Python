# -*- coding: utf-8 -*-
"""
Created on Tue Aug  7 18:15:53 2018

@author: Editi
"""

import matplotlib.pylab as plt

x_values = list(range(1,1001))
y_values = [x**3 for x in x_values]
plt.scatter(x_values, y_values,
            edgecolor='none', s=35)

plt.title("Scatter Squares", fontsize=24)
plt.xlabel("Value",fontsize=14)
plt.ylabel("Square of Value",fontsize=14)

plt.tick_params(axis='both',which='major',labelsize=14)

plt.axis([0,1100,0,1100000000])

plt.show()
plt.savefig('squares_plot.png', bbox_inches = 'tight')