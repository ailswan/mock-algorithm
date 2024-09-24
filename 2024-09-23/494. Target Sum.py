from typing import List
# 494. Target Sum
# You are given an integer array nums and an integer target.

# You want to build an expression out of nums by adding one of the symbols '+' and '-' before each integer in nums and then concatenate all the integers.

# For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1 and concatenate them to build the expression "+2-1".
# Return the number of different expressions that you can build, which evaluates to target.

 

# Example 1:

# Input: nums = [1,1,1,1,1], target = 3
# Output: 5
# Explanation: There are 5 ways to assign symbols to make the sum of nums be target 3.
# -1 + 1 + 1 + 1 + 1 = 3
# +1 - 1 + 1 + 1 + 1 = 3
# +1 + 1 - 1 + 1 + 1 = 3
# +1 + 1 + 1 - 1 + 1 = 3
# +1 + 1 + 1 + 1 - 1 = 3
# Example 2:

# Input: nums = [1], target = 1
# Output: 1
 

# Constraints:

# 1 <= nums.length <= 20
# 0 <= nums[i] <= 1000
# 0 <= sum(nums[i]) <= 1000
# -1000 <= target <= 1000

# edge cases:
# when length of num is 1, return 1
# no validity check that target can be reached... return -1
# 

class Solution:
    def targetSum(self, nums: List[int], target: int) -> str:
        # maybe sorting the input in increasing order
        # after sorting input, I group the elements by the same values
        # get a list of the unique elements, see if there is a combination of them to reach the target
        # from the frequency count of the unique elements, I generate combinations of outputs

        ans = 0
        
        nums.sort()
        counts = Counter(nums) #{1:3} 2^3
        # [1,1,1], target = 1 --> [-1,1,1] or [1,-1,1] or [1,1,-1]
        # [1,1,1], target = -1 --> [-1,-1,1] or [1,-1,-1]
        # uniq = list(counts.keys())

        # generate a uniq list of elements that contains 1 instance of all even counts, and 2 instances of all odd counts

        total = 0
        for idx, u in enumerate(uniq):
            if target == total:
                ans += 1
                break
            elif total < target:
                total += u
            else:
                total -= u
        if total != target:
            return -1
        
        # for every uniq element, check their count
        # if there are at least 2 counts of the uniq element... there are 2 combinations (negative in the first element, or negative in second element)
        # if there are 3 counts.... 
        class Solution:
            def findTargetSumWays(self, nums: List[int], target: int) -> int:
                s = sum(nums)
                if s < target or (s - target) % 2:
                    return 0
                n = (s - target) // 2       # useless numbers
                
                f = [0] * (n + 1)
                f[0] = 1
                for x in nums:
                    for j in range(n, x - 1, -1):
                        f[j] += f[j - x]
                return f[n]
            
        
        
        class Solution:
            def findTargetSumWays(self, nums, target):
            _sum = sum(nums)
            if target < -_sum or target > _sum:
                return 0
            dp = [0] * (2 * _sum + 1)
            dp[nums[0] + _sum] = 1
            dp[-nums[0] + _sum] += 1

            for i in range(1, len(nums)):
                _next = [0] * (2 * _sum + 1)
                for s in range(2 * _sum + 1):
                    if dp[s] > 0:
                        _next[s + nums[i]] += dp[s]
                        _next[s - nums[i]] += dp[s]
                dp = _next
            return dp[target + _sum]
