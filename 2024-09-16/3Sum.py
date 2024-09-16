from typing import List

# 15. 3Sum

# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.

 

# Example 1:

# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation: 
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not matter.
# Example 2:

# Input: nums = [0,1,1]
# Output: []
# Explanation: The only possible triplet does not sum up to 0.
# Example 3:

# Input: nums = [0,0,0]
# Output: [[0,0,0]]
# Explanation: The only possible triplet sums up to 0.
 

# Constraints:

# 3 <= nums.length <= 3000
# -10^5 <= nums[i] <= 10^5

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # i j k
        # sort 
        # loop i as fix position in the nums
        # j, k start as left and right side of the window [i + 1, n - 1 ] 
        # check is sum of the three element == 0 , append three values to the res
        res = []
        nums.sort()
        n = len(nums)
        i = 0
        while i < n - 2:
            if nums[i] > 0:
                return res
            while i > 0 and nums[i] == nums[i - 1]:
                i += 1
            j, k = i + 1, n - 1
            print(i, j, k)
            while j < k:
                cur_sum = nums[i] + nums[j] + nums[k] 
                if cur_sum == 0:
                    res.append([nums[i], nums[j], nums[k]])
                    k -= 1
                    j += 1
                if cur_sum > 0:
                    k -= 1
                if cur_sum < 0:
                    j += 1
                while  i + 1 < j < k and nums[j] == nums[j - 1]:
                    j += 1
                while  j < k < n - 1 and nums[k] == nums[k + 1]:
                    k -= 1
            i += 1
        return res
    # time complexity O(n * n)
    # space complexity O(log n) 
nums = [-1,0,1,2,-1,-4] # Output: [[-1,-1,2],[-1,0,1]]
#        -4 -1  -1  0  1   2
#        0  1   2   3  4  5
solution = Solution()
res = solution.threeSum(nums)
print(res)


