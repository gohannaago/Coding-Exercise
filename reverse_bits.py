""" 
190. Reverse bits of a given 32 bits unsigned integer
https://leetcode.com/problems/reverse-bits/
"""

class Solution:
    def reverseBits(self, n: int) -> int:
        # convert to binary
        n = f'{n:032b}'

        # reverse binary
        n = list(n)
        n.reverse()
        # convert back to integer
        n = (''.join(n))
        
        out = int(n,2)

        return out