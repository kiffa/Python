# -*- coding: utf-8 -*-
"""
Created on Tue Aug  7 21:42:35 2018

@author: Editi
"""
import pygal
from die import Die

die1 = Die()
die2 = Die()

results = [die1.roll() * die2.roll()
             for roll_num in range(10000)]
#列表的用法，for循环生成的值会直接带入表达式进行运算，得到的值将会加入列表
max_result = die1.num_sides + die2.num_sides 
frequencies = [results.count(value) for value in range(2,max_result+1)]
#列表的用法，for循环生成的值会直接带入表达式进行运算，得到的值将会加入列表

hist = pygal.Bar()
hist.title = "Results of rolling two D6 10000 times."
hist.x_title = "Results"
hist.x_labels = [str(x) for x in range(2,max_result+1)]  
#遍历所有可能的数字
  
hist.y_title ="Frequency of Result" 

hist.add('D6 * D6', frequencies)
hist.render_to_file('die_visual.svg')
   
print(frequencies)