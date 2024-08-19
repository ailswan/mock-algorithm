from typing import List

# 896. Monotonic Array
# An array is monotonic if it is either monotone increasing or monotone decreasing.

# An array nums is monotone increasing if for all i <= j, nums[i] <= nums[j]. An array nums is monotone decreasing if for all i <= j, nums[i] >= nums[j].

# Given an integer array nums, return true if the given array is monotonic, or false otherwise.


# Example 1:

# Input: nums = [1,2,2,3]
# Output: true
# Example 2:

# Input: nums = [6,5,4,4]
# Output: true
# Example 3:

# Input: nums = [1,3,2]
# Output: false
 

# Constraints:

# 1 <= nums.length <= 105
# -105 <= nums[i] <= 105\

class Solution:
  def isMonotonic(self, nums: List[int]) -> bool:
    # iterate through the array
    # first check the first 2 elements, see if is_inc or is_dec
    # we can check each number with the number next to it
    # keep a is_inc boolean, set it to True at first
    # if number keeps increasing, then it's True, otherwise return False


    # Input: nums = [1,2,2,3]
    if len(nums) == 1:
      return True

    is_inc = nums[0] <= nums[1]   # 1 <= 2? True
    
    for i in range(1, len(nums) - 1):
      if is_inc and nums[i] <= nums[i + 1]:   # True and 2 <= 2? True   # True and 2 <= 3? True
        continue
      elif not is_inc and nums[i] >= nums[i + 1]:
        continue
      else:
        return False
    
    return True

# time => (N)
# space => (1)