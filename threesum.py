""" 
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, 
and j != k, and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets.
https://leetcode.com/problems/3sum/
"""

nums = [-1,0,1,2,-1,-4]

# output -> return a list of 3 numbers from input where they all sum to 0
# output -> [[-1,-1,2],[-1,0,1]]
# all solutions in the output must be unique (cannot contain duplicates)
# [2, -1, -1] is the same as [-1, -1, 2] 



def solution(nums):
    nums.sort()
    # sorted(numes)
    sol = []
    # Iterate through each element in nums
    # for i in range(len(nums)):
    #     for j in range(i+1, len(nums)):
    #         for k in range(j+1, len(nums)):
    #             if nums[i]+ nums[j] + nums[k] == 0:
    #                 if [nums[i], nums[j], nums[k]] not in sol:
    #                     sol.append(list((nums[i], nums[j], nums[k])))
    
    # Expanding from twosum
    # for i in range(len(nums)):
    #     for j in range(i+1, len(nums)):
    #         if -(nums[i]+ nums[j]) in nums[j+1:] and [nums[i], nums[j], nums[k]] not in sol:
    #             sol.append(list((nums[i], nums[j], nums[k])))]
                
    
    for i in range(len(nums)):
        # fix 1 number, then perform 2sum on the other two with target -nums[i]
        # target = 4
        target = -nums[i]
        
        d = set()
        for j in range(i+1,len(nums)):
            # nums[j] = -1
            # check in d if you have seen the solution
            d.add(target - nums[j])
            if j>i+1 and nums[j] in d and [nums[i], target - nums[j],nums[j]] not in sol and target - nums[j] != nums[j]:
                sol.append([nums[i], target - nums[j], nums[j]])
    return sol
  
# 1. sort list (so same elements are next to each other)
# 2. can compare if solution is in sol

# time complexity: o(n^3)
# time complexity for sorting: o(nlogn)

# optimal is o(n^2)

# 2sum
# o(n)

# 3sum -> 2sum + 1 more

# in 2sum, you iterate through the list and store the target - element seen in a dict
# if you encounter any key in the dict -> you automatically know it adds up to the target

# 2sum without in

# return the two the numbers that sum to target
# def twosum(nums, target):
#     d = set()
#     # {key1: value1, key2: value2}
#     for i in range(len(nums)):
#         d.add(target - nums[i])
#         if i > 0 and nums[i] in d:
#             out = [nums[i], target - nums[i]]
#         # d[key] = value
#     return out
        
# advantages of dict
# lookup is o(1) eg. d[key], if key in d
# key in dict o(1)
# el in list o(n)

# print(twosum([1,1,4], 2)) # [1,1]

# el in list -> o(n)



nums = [-1,0,1,2,-1,-4]
print(solution(nums)) # -> [[-1,-1,2],[-1,0,1]]