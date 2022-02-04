#%%
class Solution:
    def searchInsert(self, nums, target) -> int:
        # Return index when target in nums
        if target in nums:
            out = nums.index(target)
        
        # Find where target would fit in list --> halving
        else:
            ind = len(nums)//2
            while not nums[ind] <= target and nums[ind+1] >= target:
                print(ind)
                if target < nums[ind] and ind >= 1:
                    print("lower")
                    ind = (ind // 2)
                    if ind == 0:
                        if nums[0] > target:
                            out = 0
                        else:
                            out = 1
                        break
          
                elif target > nums[ind] and ind <= len(nums):
                    print("upper")
                    ind = ind + (ind//2)
                    if ind == len(nums)-1:
                        if  nums[-1] < target:
                            out = len(nums)
                        else:
                            out = ind
                        break
                # elif target == nums[ind]:
                out = ind
            
        return out
                    
#%%