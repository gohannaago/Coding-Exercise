""" 
238. Product of Array Except Self
Given an integer array nums, return an array answer such that answer[i]
is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit 
in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without 
using the division operation.
https://leetcode.com/problems/product-of-array-except-self/
"""

#O(n) time complexity means single layer of for loops and no nested loops!

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        p = 1
        answer = [1]
        #first loop
        for i in range(n-1):
            p *= nums[i]
            answer.append(p)
        p = 1
        #second loop
        for j in range(n-1,-1,-1):
            answer[j] *= p
            p *= nums[j]
        # reverse list
        # answer.reverse()
        
        return answer