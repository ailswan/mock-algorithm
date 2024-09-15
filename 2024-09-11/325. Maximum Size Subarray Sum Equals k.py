from typing import List
#325. Maximum Size Subarray Sum Equals k
# Given an integer array nums and an integer k, return the maximum length of a 
# subarray
#  that sums to k. If there is not one, return 0 instead.
# Example 1:

# Input: nums = [1,-1,5,-2,3], k = 3
# Output: 4
# Explanation: The subarray [1, -1, 5, -2] sums to 3 and is the longest.
# Example 2:

# Input: nums = [-2,-1,2,1], k = 1
# Output: 2
# Explanation: The subarray [-1, 2] sums to 1 and is the longest.
 

# Constraints:

# 1 <= nums.length <= 2 * 10^5
# -10^4 <= nums[i] <= 10^4
# -10^9 <= k <= 10^9


class Solution:
    def maxSubarray(self, nums: List[int], k: int) -> int:
        # prefix sum, keep a running sum of the elements
        # use a hashtable to store the existing sums and their length <sum, length>
        # look for complements that sum to k with the running sum
        # return the length


        # Input: nums = [1,-1,5,-2,3], k = 3

        pSum = 0
        longest_subarray = 0
        subarrays = {}

        for i, num in enumerate(nums):                                          # i = 3, num = -2
            pSum += num                                                         # pSum = 3
            
            if pSum == k:                                                       # 3 == k?
                longest_subarray = max(longest_subarray, i + 1)                 # longest_subarray = 3
            comp = pSum - k                                                     # comp = 3 - 3 => 0
            if comp in subarrays:
                longest_subarray = max(longest_subarray, i - subarrays[pSum])       # i - subarrays[pSum] => 3 - 1 = 2
            
            if pSum not in subarrays:
                subarrays[pSum] = i                           # subarrays => { 1: 0, 0: 1, 5: 2 }
        
        return longest_subarray

# time => O(N) where N length nums
# space => O(N) N is the length of nums