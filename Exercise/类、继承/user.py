# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
class User():
    def __init__(self,first_name,last_name,age,sex,birth):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.sex = sex
        self.birth = birth
        self.login_attempts = 0
        
    def describe_user(self):
        print("Username: " + self.first_name.title() + self.last_name.title())
        print("Age: " + str(self.age))
        print("Sex: " + self.sex.title())
        print("Birth: " + self.birth)
    
    def greet_user(self):
        print("Welcome back " + self.first_name.title() + " " + self.last_name)
        
    def read_login_attempts(self):
        print(self.login_attempts)
    
    def increment_login_attempts(self,plus):
        self.login_attempts += plus
        
    def reset_login_attempts(self):
        self.login_attempts = 0
        
class Admin(User):
    def __init__(self,first_name,last_name,age,sex,birth):
        super().__init__(first_name,last_name,age,sex,birth)
        self.privileges = ["can add post","can delete post","can ban user"]
    
    def show_privileges(self):
        for privilieges in self.privileges:
            print(privilieges)
            
admin = Admin('jack','wu','21','male','19970111')
admin.show_privileges()