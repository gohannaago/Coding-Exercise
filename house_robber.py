""" 
198. House Robber
You are a professional robber planning to rob houses along a 
street. Each house has a certain amount of money stashed, 
the only constraint stopping you from robbing each of them 
is that adjacent houses have security systems connected and 
it will automatically contact the police if two adjacent houses
were broken into on the same night.
Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

https://leetcode.com/problems/house-robber/
https://leetcode.com/problems/house-robber/discuss/156523/From-good-to-great.-How-to-approach-most-of-DP-problems.
"""

# My initial attempt
# class Solution:
#     def rob(self, nums: List[int]) -> int:
#         maps = nums
#         inds = set()
#         n = len(nums)
#         maxes = []
        
#         # for robs in range(n//2):
#         while len(inds) < n//2 :
#             rob = max(maps)
#             print("robbing: ", rob)
#             i = nums.index(rob)
#             if  i+1 not in inds and  i-1 not in inds:
#                 maps.remove(rob)
#                 inds.add(i)
#                 maxes.append(rob)
#             else: 
#                 maps.remove(rob)
        
#         return sum(maxes)

#--------------------------------#
# SHOULD FIND RECURSIVE RELATIONSHIP AND IMPLEMENT DYNAMIC PROGRAMMING