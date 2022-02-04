""" 
Write a function that takes an unsigned integer and returns the 
number of '1' bits it has (also known as the Hamming weight).
https://leetcode.com/problems/number-of-1-bits/
"""

# Initial Apprach - O(n)
# class Solution:
#     def hammingWeight(self, n: int) -> int:
#         # Initialize Sum
#         sums = 0
#         # Initialize input
#         # num = n
        
#         # Use a while loop
#         while n >0:
#             print(n%2)
#             sums += (n%2)
#             n = n //2
            
#         return sums

# faster bitwise solution 

    def hammingWeight(self, n: int) -> int:
        # n = bin(n)
        return n.bit_count()

# Convert to binary and then list of strings and count
    def hammingWeight(self, n: int) -> int:
        q = list(str(bin(n)))
        # print(q)
        c = q.count('1')
        # print(c)
        return c