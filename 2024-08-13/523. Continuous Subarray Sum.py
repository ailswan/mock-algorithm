from typing import List

# 523. Continuous Subarray Sum

# Given an integer array nums and an integer k, return true if nums has a good subarray or false otherwise.

# A good subarray is a subarray where:

# its length is at least two, and
# the sum of the elements of the subarray is a multiple of k.
# Note that:

# A subarray is a contiguous part of the array.
# An integer x is a multiple of k if there exists an integer n such that x = n * k. 0 is always a multiple of k.

# Example 1:

# Input: nums = [23,2,4,6,7], k = 6
# Output: true
# Explanation: [2, 4] is a continuous subarray of size 2 whose elements sum up to 6.
# Example 2:

# Input: nums =  k = 6
# Output: true[23,2,6,4,7], prefix-sum method
# Explanation: [23, 2, 6, 4, 7] is an continuous subarray of size 5 whose elements sum up to 42.
# 42 is a multiple of 6 because 42 = 7 * 6 and 7 is an integer.
# Example 3:

# Input: nums = [23,2,6,4,7], k = 13
# Output: false
 

# Constraints:

# 1 <= nums.length <= 105
# 0 <= nums[i] <= 109
# 0 <= sum(nums[i]) <= 231 - 1
# 1 <= k <= 231 - 1

class Solution:
  def isGoodContinuousSubarraySum(self, nums: List[int], k: int) -> bool:
    # iterate through nums
    # generate list of the prefix-sum 
    # [23,2,4,6,7] k = 6
    #   23 25 29 35 42
    #      
    # {
    #   23, 25, 31
    # }
    # check if any elements in pre-fix sum is a multiple of k (preFix)
    if nums[0] % k == 0:
      return True
    #{0: -1, 5: 0 , 1: 1, 5: 3 }
    #   23        25 29 35 42
    #   3*k + 5    4*k = 3*k + k*1
    #   5
    for i in range(1, len(nums)):
      nums[i] += nums[i - 1]
      if nums[i] % k == 0:
        return True
      #23 % 6 == 0?   remd= 23 % 6 = 5
      # 2 + 5 = 7            7 % 6 = 1
      # 4 + 1 = 5            5 % 6 = 5
    #index  3 - 0
    return False
  
#   class Solution:
#     def checkSubarraySum(self, nums: List[int], k: int) -> bool:
#         pres = defaultdict(int)
#         pre = 0
#         for i, n in enumerate(nums): 
#             last = pre
#             pre += n
#             pre %= k  
#             if pre in pres:
#                 return True
#             pres[last] = i
#         return False
