from typing import List
#977. Squares of a Sorted Array
# Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

# Example 1:

# Input: nums = [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
# Explanation: After squaring, the array becomes [16,1,0,9,100].
# After sorting, it becomes [0,1,9,16,100].
# Example 2:

# Input: nums = [-7,-3,2,3,11]
# Output: [4,9,9,49,121]
# Constraints:

# 1 <= nums.length <= 104
# -104 <= nums[i] <= 104
# nums is sorted in non-decreasing order.
#Follow up: Squaring each element and sorting the new array is very trivial, could you find an O(n) solution using a different approach?

class Solution:
    def getSquaresSorted(self, nums: List[int]) -> List[int]:
        # try linear solution
        # we have to square each number
        # 3 scenarios: 0 --> 0, positive --> positive, negative --> positive
        # zero => always comes first in output
        # smaller negative, larger positive
        # we want to compare the absolute value of the negative and positive numbers
        # **** populate the answer list with the squared values of the larger absolute value ***
        # left and right poitners, 0, len(n) - 1

        n = len(nums)
        l,r = 0, n - 1
        ans = [1] * n
        # [-9,-4, 0, 6]
        #        lr
        # [36，81]
        while l < r:
            if abs(nums[l]) > abs(nums[r]):            # [-9,-4, 0, 6, 9] -> [0, 16, 36]
                ans[l], ans[r] = nums[r], nums[l]
                l += 1
                r -= 1
            elif nums[l] == 0 or nums[r] == 0:     
                
                
            