# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#["can add post","can delete post","can ban user"]
class Car():
    def __init__(self,brand,model,year):
        self.brand = brand
        self.model = model
        self.year = year
        self.odometer = 0
        self.oil_tank = 70
    def car_describe(self):
        car_info = str(self.year) + " " + self.brand.title() + " " + \
                   self.model.title()
        return car_info
    
    def read_odometer(self):
        print("当前里程数为：" + str(self.odometer) + " km.")
    
    def update_odometer(self,kilometer):
        if kilometer >= self.odometer:
            self.odometer = kilometer
        else:
            print("禁止回调里程！")
    def oil_tank_describe(self):
        print("油箱容积为：" + str(self.oil_tank))

c_test = Car("audi","a8",2016)
print(c_test.car_describe())
c_test.oil_tank_describe()