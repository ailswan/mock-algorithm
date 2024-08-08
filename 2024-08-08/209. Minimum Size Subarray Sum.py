from typing import List

# 209. Minimum Size Subarray Sum
# Given an array of positive integers nums and a positive integer target, return the minimal length of a 
# subarray
#  whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.


# Example 1:

# Input: target = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: The subarray [4,3] has the minimal length under the problem constraint.


# Example 2:

# Input: target = 4, nums = [1,4,4]
# Output: 1


# Example 3:

# Input: target = 11, nums = [1,1,1,1,1,1,1,1]
# Output: 0
 

# Constraints:

# 1 <= target <= 109
# 1 <= nums.length <= 105
# 1 <= nums[i] <= 104
 

# Follow up: If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log(n)).
 

class Solution:
    def getMinSumSubArray(self, nums: List[int], target: int) -> int: #return the size of the subarray
        # left, right pointers, iterate through the array
        # keep left ptr at 0, move the right ptr and accumulate curr_sum
        # continuously checkign against the target (GTE)
        # if current subarray is greater than target, move the left ptr
        # *** we know we want to keep moving the right pointer all the way through the input array (it must iterate through all the numbers) ***
        # 2, 3, 1, 2, 4, 3
        # l        r
        # Input: target = 7, nums = [2,3,1,2,4,3]
        ans = float("inf")
        curr_sum = 0
        l,r = 0, 0
        n = len(nums) # 6

        while l < n and r < n:                 # r = index 3
            curr_sum += nums[r]      # curr_sum = 6 + 2  
            while curr_sum >= target: #8  - 2 > 7
                ans = min(r - l + 1, ans)
                curr_sum -= nums[l]  # curr_sum = curr_sum - 2 => 5
                l += 1               # l = 1
            r += 1               # r = 3
            # ans = min(r - l + 1, ans) # ans = 4

        return ans