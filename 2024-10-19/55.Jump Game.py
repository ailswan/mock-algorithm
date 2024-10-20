from typing import List

# 55. Jump Game

# You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

# Return true if you can reach the last index, or false otherwise.

 

# Example 1:

# Input: nums = [2,3,1,1,4]
# Output: true
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
# Example 2:

# Input: nums = [3,2,1,0,4]
# Output: false
# Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.
 

# Constraints:

# 1 <= nums.length <= 104
# 0 <= nums[i] <= 105

class Solution:
    def jumpGame(self, nums: List[int]) -> bool:
        # dp, top-down
        # try every possible jump
        # if we exhaust steps, return False
        # if we reach the end, return True

        # [2,3,1,1,4]
        n = len(nums)
        dp = [False] * n # [1, ptr = 0 , i, F, _ , F, i] ptr = max(ptr, i + num[i])   max(3, 5)
        dp[0] = True


        ptr = 0
        for i in range(n):
            if i > ptr:
                return False
            ptr = max(ptr, ptr + nums[i])
        return True
