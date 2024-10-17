from typing import List
# 334. Increasing Triplet Subsequence

# Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.

 

# Example 1:

# Input: nums = [1,2,3,4,5]
# Output: true
# Explanation: Any triplet where i < j < k is valid.
# Example 2:

# Input: nums = [5,4,3,2,1]
# Output: false
# Explanation: No triplet exists.
# Example 3:

# Input: nums = [2,1,5,0,4,6]
# Output: true
# Explanation: The triplet (3, 4, 5) is valid because nums[3] == 0 < nums[4] == 4 < nums[5] == 6.
 

# Constraints:

# 1 <= nums.length <= 5 * 105
# -231 <= nums[i] <= 231 - 1
 

# Follow up: Could you implement a solution that runs in O(n) time complexity and O(1) space complexity?

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        # brute force => triple nested loop....
        # to find i, we iterate through the array until we come across a smaller number than nums[i - 1]
        # to find j, nums[j] > nums[i]
        # to find k, nums[k] > nums[j]

        # Input: nums = [2, 1, 5, 0, 4, 6]
        #                   i  j k
        #                     idx
        ans = False
        i = 0
        j = 1
        k = 2
        smallest = (float("inf"), None) # (element, index)
        largest = (float("-inf"), None)

        for idx, num in enumerate(nums):
            if num < nums[i]:
                i = idx
            elif nums[i] < nums[j] and idx > j and num < nums[j]:
                j = idx
            elif nums[j] < nums[k] and idx > k and num > nums[k]:
                k = idx
        
        return nums[i] < nums[j] < nums[k] and i < j < k


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = second = float('inf')
        for n in nums:
            if n <= first:
                first = n
            elif n <= second:
                second = n
            else:
                return True
        return False
