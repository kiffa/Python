# -*- coding: utf-8 -*-
"""
Created on Wed Aug  1 17:18:57 2018

@author: Editi
"""

class Employee():
    def __init__(self,first_name,last_name,salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary
        
    def give_raise(self,add_salary=5000):
        add_desicion = input("是否按照默认数字加薪？ (yes/no)\n")
        if add_desicion == 'yes':
            add_salary_mark = True
        else:
            add_salary_mark = False
        if add_salary_mark:
            self.salary = int(self.salary) + int(add_salary)
        else:
            add_salary = int(input("请输入要增加的薪资数："))
            self.salary = int(self.salary) + int(add_salary)
            
    def employee_describe(self):
        empoly_info = self.first_name + " " + \
                      self.last_name + " " + \
                      str(self.salary)
        return empoly_info.title()
    
    
new_empolyee = Employee('yang','tom',5000)
print(new_empolyee.employee_describe())
new_empolyee.give_raise()
print(new_empolyee.employee_describe())