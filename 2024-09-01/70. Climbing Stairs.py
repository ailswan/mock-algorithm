from typing import List

# 70. Climbing Stairs

# You are climbing a staircase. It takes n steps to reach the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 

# Example 1:

# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps
# Example 2:

# Input: n = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step
 

# Constraints:

# 1 <= n <= 45

class Solution:
    def climbStairs(self, n: int)->int:
        # two statuses for one stair: come from 1 step or 2 step
        # except corner case  0 1 
        #dp[n] = dp[n - 1] + dp[n - 2]
        #dp[0] = 1
        #dp[1] = 1
        dp = [0] * (n + 1) #n = 3  dp =[0,0,0,0]
        dp[0] = 1
        dp[1] = 1#dp =[1,1,2,3]
        for i in range(2, n + 1): # 2 - 3
            dp[i] = dp[i - 1] + dp[i - 2] # dp[3] = dp[2] + dp[1] = 3
        return dp[n] #3
        #time complexity O(n)
        #space complexity O(n)
        dp1 = 1 # 0
        dp2 = 1 # 1
        for i in range(2, n + 1):
            temp = dp2
            dp2 = dp2 + dp1
            dp1 = temp
        return dp2
        # time complexity O(n)
        # space complexity O(1)
        
            



        

