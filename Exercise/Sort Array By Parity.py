# -*- coding: utf-8 -*-
"""
Created on Mon Sep 24 16:10:40 2018
Input: [3,1,2,4]
Output: [2,4,3,1]
The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.
 
@author: Editi
"""

class Solution:
    def sortArrayByParity(A):
        """
        :type A: List[int]
        :rtype: List[int]
        通过使用匿名函数lambda，对A的元素进行取余，并将进行处理的元素排序
        """
        A.sort(key = lambda x: x % 2)
        return A   
                    
        
A = [3,1,2,4]
rs = Solution.sortArrayByParity(A)
print(rs)