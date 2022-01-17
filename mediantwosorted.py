""" 
4. Median of Two Sorted Arrays
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
The overall run time complexity should be O(log (m+n)).
https://leetcode.com/problems/median-of-two-sorted-arrays/
"""

# My Attempt
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
            
        m = len(nums1)
        n = len(nums2)
        
        if m == 0:
            merged = nums2
        elif n == 0:
            merged = nums1
        else:
            # make a merged sorted list
            merged = []
            for i in range(m):
                for j in range(n):
                    if nums1[i] > nums2[j]:
                        print("top")
                        merged.append(nums2[j])
                        if j == n-1 and i != m-1:
                            merged += nums1[i:m]
                        continue
                    else:
                        print("bottom")
                        merged.append(nums1[i])
                        if i == m-1 and j != n-1:
                            merged += nums2[j:n]
                        break
        
        print(merged)
        # print(m+n)
        
        if (m+n)%2 == 0:
            # print("median two val = ", merged[((m+n)/2)-1], ", ", merged[(m+n)/2])
            median = (float(merged[((m+n)//2)-1]) + float(merged[(m+n)//2])) /2
        else:
            # print("median index = ", (m+n)//2)
            median = merged[(m+n)//2]
            
        return median

""" 
Issue with this implementation is that value check for the second array does
not start from where it left off
"""

# Example 
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        lenght = len(nums1) + len(nums2)
        nums1.append(float('inf')) #acts as an unbounded upper value for comparison
        nums2.append(float('inf'))
        mid = lenght // 2 + 1
        last = prev = 0
        left = right = 0
        while mid:
            prev = last
            if nums1[left] < nums2[right]:
                last = nums1[left]
                left += 1
            else:
                last = nums2[right]
                right += 1
            mid -= 1
        return last if lenght % 2 else (prev + last) / 2

#------------------------#
#done own implementation
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        
        i = 0
        j = 0
        
        nums1.append(float('inf')) #acts as an unbounded upper value for comparison
        nums2.append(float('inf'))
        
        merged = []
        while len(merged) <= ((m+n)//2):
            # print("len(merged): ", len(merged))
            if nums1[i] <= nums2[j]:
                merged.append(nums1[i])
                print(nums1[i])
                i += 1
            else:
                merged.append(nums2[j])
                print(nums2[j])
                j += 1
            
        if (m+n)%2: #when odd number 
            ans = merged[-1]
        else:
            ans = (merged[-1] +merged[-2])/2
            
        return ans