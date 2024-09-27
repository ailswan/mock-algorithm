from typing import List

# 169. Majority Element

# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

# Example 1:

# Input: nums = [3,2,3]
# Output: 3
# Example 2:

# Input: nums = [2,2,1,1,1,2,2]
# Output: 2
 

# Constraints:

# n == nums.length
# 1 <= n <= 5 * 104
# -109 <= nums[i] <= 109
 

# Follow-up: Could you solve the problem in linear time and in O(1) space?

class Solution:
    def majority(self, nums: List[int]) -> int:
       # [2,2,1,1,1,2,2]# Output: 2
       #  counter 
       # sort  1112222
       #  m_v   m_c 
       

# Boyer-Moore Voting Algorithm

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = None
        count = 0
        
        # First pass: Find candidate for majority element
        for num in nums:
            if count == 0:
                candidate = num
                count = 1
            elif num == candidate:
                count += 1
            else:
                count -= 1
        
        # Second pass: Verify candidate is majority element
        count = 0
        for num in nums:
            if num == candidate:
                count += 1
        
        if count > len(nums) // 2:
            return candidate
        else:
            return -1  # No majority element found
