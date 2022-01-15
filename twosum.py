"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
"""

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        #for loop indices
        # for each element, check if target - nums[i] exists in num
        
        for i in range(len(nums)):
            if (target - nums[i]) in nums[i+1:]:
                ans = [i,nums[i+1:].index(target - nums[i])+(i+1)]
                break
            else:
                continue
        
        #return the indices
        return ans