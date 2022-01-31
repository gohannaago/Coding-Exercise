""" 
3. Longest Substring Without Repeating Characters
Given a string s, find the length of the longest substring without repeating characters.
https://leetcode.com/problems/longest-substring-without-repeating-characters/
"""

## My Attempt ##
# def lengthOfLongestSubstring(s):
#     """
#     :type s: str
#     :rtype: int
#     """
    
#     slist = list(s)
#     maxnum = 1
#     for i in range(len(slist)):
#         for j in range(i+1,len(slist)):
#             print("[", i , ":", j, "]")
#             if (slist[j] not in slist[i:j]):
#                 if j-i+1 > maxnum:
#                     maxnum = j-i+1
#                     print("current maxnum = ", maxnum)
#                     print("current substring = ", slist[i:j+1])
#             else:
#                 break
    
#     return maxnum

# print("result is ", lengthOfLongestSubstring("pwwkew"))

# ----------------------------------------------------- #
# solution without explicitly converting string into list

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        sub = ''
        for char in s:
            if char not in sub:
                sub += char
                ans = max(ans, len(sub))
            else:
                cut = sub.index(char)
                sub = sub[cut+1:] + char
        return ans