from typing import List

# 1060. Missing Element in Sorted Array

# Given an integer array nums which is sorted in ascending order and all of its elements are unique and given also an integer k, return the kth missing number starting from the leftmost number of the array.

# Example 1:

# Input: nums = [4,7,9,10], k = 1
# Output: 5
# Explanation: The first missing number is 5.

# Example 2:

# Input: nums = [4,7,9,10], k = 3
# Output: 8
# Explanation: The missing numbers are [5,6,8,...], hence the third missing number is 8.

# Example 3:

# Input: nums = [1,2,4], k = 3
# Output: 6
# Explanation: The missing numbers are [3,5,6,7,...], hence the third missing number is 6.
 

# Constraints:
# 1 <= nums.length <= 5 * 10^4
# 1 <= nums[i] <= 10^7
# nums is sorted in ascending order, and all the elements are unique.
# 1 <= k <= 10^8
 

# Follow up: Can you find a logarithmic time complexity (i.e., O(log(n))) solution?

class Solution:
    def findMissingNumber(self, nums: List[int], k: int) -> int:
        # Input: nums = [4,7,9,10], k = 3
        # Output: 8
        # 4   7  9 10  13  n = 4  mid = n//2    1 2 3 4 5 820            k  = 5  
        #                                       0 1 2 3 4  5        
        #  5 6 8                                      l r
        # 0   1  2  3
        #     lm r     
        # BS  
        #  2  , nums[mid] - nums[l] = 5 - 2 = 3 >= k in the left side: r = m  7 - 4 = 3 - 1 < k: l
        # else in the right side: l = m 
        l, r, n = 0, len(nums) - 1, len(nums)
        while l < r - 1:                # l = 3, r = 4
            mid = (r + l) // 2 # 3
            left_n = mid - l # 1
            right_n = r - mid
            left_missing_n = nums[mid] - nums[l] - left_n # 4 - 3 - 1 = 0
            #right_missing_n = nums[l] - nums[mid] - right_n # 0
            if left_missing_n >= k: # in the left side move the r to mid
                r = mid
            else:
                l = mid
                k -= left_missing_n # k -=0
        return nums[l] + k if nums[r] - nums[l] > k else nums[l] + k + 1   #820- 5 > k 5 + 5 
    
    # time complexity  O(log(n))
    # space complexity O(1)
    



