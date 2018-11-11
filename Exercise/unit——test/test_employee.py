# -*- coding: utf-8 -*-
"""
Created on Wed Aug  1 17:39:06 2018

@author: Editi
"""

import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    def setup(self):
        self.yang = Employee('yang','tom',5000)
        
    def test_given_default_raise(self):
        self.yang.give_raise() 
        self.assertEqual(self.yang.salary,10000)
        
    def test_given_new_raise(self):
        self.yang.give_raise(10000)
        self.assertEqual(self.yang.salary,15000)
        
unittest.main()
        
        
        
        
        