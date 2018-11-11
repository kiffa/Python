# -*- coding: utf-8 -*-
"""
Created on Fri Sep 21 10:55:29 2018
Given an array of integers, return indices of the two numbers such that they
 add up to a specific target.
You may assume that each input would have exactly one solution, 
and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

@author: Editi
"""

class Solution(object):
    def twoSum(nums, target):
        if len(nums) <= 1:
            return False
        buff_dict = {}
        for i in range(len(nums)):
            if nums[i] in buff_dict:
                print(nums[i])
                return [buff_dict[nums[i]], i]
            else:
                buff_dict[target - nums[i]] = i
nums = [2, 7, 11, 15]
target = 9
s = Solution.twoSum(nums, target)
print(s)

