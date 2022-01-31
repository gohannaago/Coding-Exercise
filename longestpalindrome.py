""" 
5. Longest Palindromic Substring
Given a string s, return the longest palindromic substring in s.
https://leetcode.com/problems/longest-palindromic-substring/
"""
# MY Implementation
# Exceeds time limit within leet code 

# class Solution:
#     def longestPalindrome(self, s: str) -> str:
        
#         #initialize shortest output
#         output = s[0]
        
#         def checker(a,b): #start index a, b
#             num = 0
#             while a-num > 0 and b+num < len(s)-1:
#                 if s[a-num-1] == s[b+num+1]:
#                     num += 1
#             return num
        
#         for i in range(0, len(s)-1):
#             if i>0 and s[i-1] == s[i+1]: #odd length palindrome
#                 print("input: ", i-1, "to ", i+1)
#                 size = checker(i-1, i+1)
#                 print("size = ", size)
#                 print(s[(i-1-size):(i+size+2)])
#                 if len(s[(i-1-size):(i+size+2)]) > len(output):
#                     output = s[(i-1-size):(i+size+2)]

#             if s[i] == s[i+1]: #even length palindrome
#                 print("input: ", i, "to ", i+1)
#                 size = checker(i, i+1)
#                 print("size = ", size)
#                 print(s[(i-size):(i+size+2)])
#                 if len(s[(i-size):(i+size+2)]) > len(output):
#                     output = s[(i-size):(i+size+2)]
                
                
#         return output
#%%
#  --------------------------------- #
# expansion from center implementation
# from center method
# save the indices rather than the whole array
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s is "":
            return s
        
        min_i = max_i = 0
        
        for i in range(len(s)):
            print("at index ", i)
            even_min, even_max = self.checker(s,i,i+1)
            odd_min, odd_max = self.checker(s,i,i)
            
            if (even_max - even_min) > (odd_max - odd_min) and (even_max - even_min) > max_i - min_i:
                max_i = even_max
                min_i = even_min
                print("cond 1 ", min_i, " to ", max_i)
            

            #odd palindrome
            if (even_max - even_min) < (odd_max - odd_min) and (odd_max - odd_min) > max_i - min_i:
                max_i = odd_max
                min_i = odd_min
                print("cond 2 ", min_i, " to ", max_i)
                
        return s[min_i:max_i+1]
    
    def checker(self,s,a,b):
        while a> 0 and b< len(s) and s[a] == s[b]:
            a-= 1
            b+= 1
        return a,b
#%%