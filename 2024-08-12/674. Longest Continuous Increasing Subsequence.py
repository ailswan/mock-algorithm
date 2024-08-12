from typing import List


# 674. Longest Continuous Increasing Subsequence

# Given an unsorted array of integers nums, return the length of the longest continuous increasing subsequence (i.e. subarray). The subsequence must be strictly increasing.

# A continuous increasing subsequence is defined by two indices l and r (l < r) such that it is [nums[l], nums[l + 1], ..., nums[r - 1], nums[r]] and for each l <= i < r, nums[i] < nums[i + 1].

 

# Example 1:

# Input: nums = [1,3,5,4,7]
# Output: 3
# Explanation: The longest continuous increasing subsequence is [1,3,5] with length 3.
# Even though [1,3,5,7] is an increasing subsequence, it is not continuous as elements 5 and 7 are separated by element
# 4.

# Example 2:

# Input: nums = [2,2,2,2,2]
# Output: 1
# Explanation: The longest continuous increasing subsequence is [2] with length 1. Note that it must be strictly
# increasing.
 

# Constraints:

# 1 <= nums.length <= 10^4
# -10^9 <= nums[i] <= 10^9

class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        # Input: nums = [1,3,5,4,7] # Output: 3
        # 1 3 5  - 3 length
        #   1,3,5,4,7
        #   0 1 2 3 4
        #            l r       
        # two pointers l,  r . keep moving r to checking it's increasing or not
        # if it is not increasing: reset the l & r & update the res

        # input: [1]
        # expected output: 1
        res = 0
        n = len(nums)# 1
        if not n:
            return 0
        l, r = 0, 0 
        if n == 1: # the edge case
            return 1
        while r < n - 1:# r = 0 < 0
            while r < n - 1 and nums[r + 1] > nums[r]:# r = 4 < 4 and 7 > 4?        # nums[i - 1] < nums[i]
                r += 1 # r = 4
            res = max(res, r - l + 1)# res max(0,  4- 3 + 1) 2   res = 3
            l = r = r + 1 # l = r = 5
        return res # 3
    # time complexity O(n)
    # space complexity O(1)



