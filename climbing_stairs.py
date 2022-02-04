""" 
70. You are climbing a staircase. 
It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. 
In how many distinct ways can you climb to the top?
https://leetcode.com/problems/climbing-stairs/
"""

# My Implementation - 52ms, 13.9mB
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            ways = 1
        elif n == 2:
            ways = 2
        else:
            num = n-2
            ways = 0
            p1 = 1
            p2 = 2
            while num > 0:
                ways = p1 + p2
                p1 = p2
                p2 = ways
                num -= 1
                
        return ways


# Faster Approach (less runtime) 8ms
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 3:
            return n
        
        dp = [0] * (n+1)
        
        dp[0] = 0
        dp[1] = 1
        dp[2] = 2
        dp[3] = 3
        
        for i in range(4, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        
        return dp[n]


# storing variables in a list and reducing number of loops