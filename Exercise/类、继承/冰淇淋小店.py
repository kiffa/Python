# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
class Restaurant():
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.restaurant_served = 0
    
    def describe_restaurant(self):
        print("This restaurant is " + self.restaurant_name.title())
        print(", and its cuisine type is " + self.cuisine_type.title())
        
    def open_restaurant(self):
        print("Opening.")
    
    def read_restaurant_serverd(self):
        print("可接待人数：" + str(self.restaurant_served))
    
    def set_restayrant_serverd(self,number):
        self.restaurant_served = number
    
    def increment_serverd(self):
        self.restaurant_served += self.restaurant_served
        print("今天接待了" + str(self.restaurant_served) + "位客人。")
        
class IceCreamStand(Restaurant):
    def __init__(self,restaurant_name,cuisine_type):
        super().__init__(restaurant_name,cuisine_type)
        self.flavors = ['milk','chocolate','strawberry','venilla']
    
    def describe_IceCream_flavors(self):
        for flavors in self.flavors:
            print(flavors + " IceCream")

Ice_Cream = IceCreamStand("Lemon's House",'dessert')
Ice_Cream.describe_IceCream_flavors()