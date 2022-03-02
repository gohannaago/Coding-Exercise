""" 
242. Valid Anagram
Given two strings s and t, return true if t is an anagram of s, 
and false otherwise.

An Anagram is a word or phrase formed by rearranging 
the letters of a different word or phrase, 
typically using all the original letters exactly once.
https://leetcode.com/problems/valid-anagram/
"""

## first implementation using sorted
def isAnagram(self, s: str, t: str) -> bool:
    return sorted(s) == sorted(t)

## second implementation by using dict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_s = {}
        count_t = {}
        
        for i in s:
            if i not in count_s:
                count_s[i] = 0
            count_s[i] += 1
                
        for i in t:
            if i not in count_t:
                count_t[i] = 0
            count_t[i] += 1
        
        print(count_t)
        print(count_s)
                
        # repeat counter
        for char in count_s:
            print(char)
            print(count_s[char], count_t[char])
            if count_s[char] == count_t[char]:
                continue
            else:
                return "false"
        return "true"

## third implementation using Counter
## Counter initializes counts to 0 so easier than dict
from collections import Counter

def isAnagram(self, s: str, t: str) -> bool:
    c_s = Counter(s)
    c_t = Counter(t)
    
    return c_s == c_t

# fourth implementation using sets
def isAnagram(self, s: str, t: str) -> bool:
    c_s = set(s)
    c_t = set(t)
    
    for i in c_s:
        if s.count(i) == t.count(i): #count in string
            continue
        else:
            return False
        
    for j in c_t:
        if s.count(j) == t.count(j):
            continue
        else:
            return False
    return True