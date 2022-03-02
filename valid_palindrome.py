""" 
125. Valid Palindrome
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters 
and removing all non-alphanumeric characters, it reads the same forward and backward. 
Alphanumeric characters include letters and numbers.
https://leetcode.com/problems/valid-palindrome/
"""
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Remove all non-alphanumeric characters
        # convert to all lowercase 
        s = ''.join(filter(str.isalnum, s)).lower()
        
        # Check if palindrome
        count = (len(s) // 2) - 1
        
        ans = True
        # Implement a while loop starting from middle
        while count >= 0 :
            # print(count)
            if s[count] == s[-(count + 1)]:
                count -= 1
                continue
            else:
                return False
            
        
        return True
        