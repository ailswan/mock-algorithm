from tpying import List

# 213. House Robber II

# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.

# Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

 

# Example 1:

# Input: nums = [2,3,2]
# Output: 3
# Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.
# Example 2:

# Input: nums = [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
# Total amount you can rob = 1 + 3 = 4.
# Example 3:

# Input: nums = [1,2,3]
# Output: 3
 

# Constraints:

# 1 <= nums.length <= 100
# 0 <= nums[i] <= 1000

class Solution:
    def houseRobber2(self, nums: List[int]) -> int:
        # each house has two choices 
        # dp[0] = max(nums[-1],nums[0])
        # dp[1] = max(dp[0], nums[-1]+nums[i])
        # if i is odd : dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
        # if i is even: dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
        # sum of odd index house  check the max(sum - last, sum - first)
        # sum of even index house [1, 3, 1, 2]

        # input = [1,3,1,3,100] output = 103
        #          0 1 2 3 4
        # scenario1
        #rob first house dp1[i] = max(dp[i - 2] + nums[i], dp[i - 1]).  [1,3,1,3]
        # dp1[0] = nums[0] dp1[1] = dp1[0]   if i = n - 1 dp[i] = dp[i - 1] 
        # scenario2 dp2[i] = max(dp[i - 2] + nums[i], dp[i - 1])
        #not first house               [100,1,3,1]
        # dp2[0] = 0 dp2[1] = nums[1] if i = n - 2 dp[i] = dp[i - 1] 

        # input = [2,7,7,7,4] output = 14
        #         0 1  2 3 4
        n = len(nums)
        dp1 = [0] * n 
        dp2 = [0] * n
        if n == 1:
            return nums[0]
        dp1[0], dp1[1] = nums[0], nums[0]
        dp2[0], dp2[1] = 0, nums[1]
        for i in range(2, n): # i = 4  dp1 [2, 2, 9, 9, 9]     # dp2 [0, 7, 7,14, 14]
            if i == n - 1:
                dp1[i] = dp1[i - 1]
            else:
                dp1[i] = max(dp1[i - 2] + nums[i], dp1[i - 1])
            dp2[i] = max(dp2[i - 2] + nums[i], dp2[i - 1])
        return max(dp1[n - 1], dp2[n - 1]) #11
        
    #time complexity O(n)
    #space complexity O(n)

 

 class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0 or nums is None:
            return 0

        if len(nums) == 1:
            return nums[0]

        return max(self.rob_simple(nums[:-1]), self.rob_simple(nums[1:]))

    def rob_simple(self, nums: List[int]) -> int:
        t1 = 0
        t2 = 0
        for current in nums:
            temp = t1
            t1 = max(current + t2, t1)
            t2 = temp

        return t1