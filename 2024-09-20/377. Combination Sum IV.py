from typing import List
 
#  377. Combination Sum IV
# Given an array of distinct integers nums and a target integer target, return the number of possible combinations that add up to target.

# The test cases are generated so that the answer can fit in a 32-bit integer.


# Example 1:

# Input: nums = [1,2,3], target = 4
# Output: 7
# Explanation:
# The possible combination ways are:
# (1, 1, 1, 1)
# (1, 1, 2)
# (1, 2, 1)
# (1, 3)
# (2, 1, 1)
# (2, 2)
# (3, 1)
# Note that different sequences are counted as different combinations.

# Example 2:

# Input: nums = [9], target = 3
# Output: 0
 

# Constraints:

# 1 <= nums.length <= 200
# 1 <= nums[i] <= 1000
# All the elements of nums are unique.
# 1 <= target <= 1000
 

# Follow up: What if negative numbers are allowed in the given array? How does it change the problem? What limitation we need to add to the question to allow negative numbers?

class Solution:
    def combinationSum(self, nums: List[int], target: int) -> int:
        # backtracking
        # keep a running count of combinations that sum to target
        # edge case => if smallest number in nums is larger than target, return 0
        
        # Input: nums = [1,2,3], target = 4
        ans = 0

        if min(nums) > target:
            return ans
        
        def backtrack(first, cur, remaining):                              # backtrack(0, [1], 3)                          # backtrack(0, [1,1], 2)        # backtrack(0, [1,1, 1], 1)         # backtrack(0, [1,1,1,1], 0)
            # base case
            nonlocal ans
            if remaining == 0:                                                                                                                                                                      # remaining == 0? True
                ans += 1                                                                                                                                                                            # ans = 1
                cur = cur[:]
                return
            if remaining < 0:
                return

            for i in range(first, len(nums)):       # i = 0; 0 ~ 3              # i = 0; 0 ~ 3
                cur.append(nums[i])                 # cur = [1]                 # cur = [1, 1]
                backtrack(first, cur, remaining - nums[i])    # backtrack(0, [1], 4 - 1)      # backtrack(0, [1, 1], 3 - 1)
                cur.pop()
        
        backtrack(0, [], target)            # backtrack(0, [], 4)
        return ans
    
    #nums =[1,2,3]
# target = 4
#  output: 4
# target =
# 32
# epect :7

solution = Solution()
print(solution.combinationSum([1,2,3], 32))

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # dp[i] += dp[i - n]for n in nums i <= n
        dp = [1] + [0] * target
        for i in range(target + 1):
            for n in nums:
                if n <= i:
                    dp[i] += dp[i - n]
        return dp[target]