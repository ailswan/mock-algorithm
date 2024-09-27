from typing import List

# 287. Find the Duplicate Number

# Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

# There is only one repeated number in nums, return this repeated number.

# You must solve the problem without modifying the array nums and using only constant extra space.

 

# Example 1:

# Input: nums = [1,3,4,2,2]
# Output: 2
# Example 2:

# Input: nums = [3,1,3,4,2]
# Output: 3
# Example 3:

# Input: nums = [3,3,3,3,3]
# Output: 3
 

# Constraints:

# 1 <= n <= 10^5
# nums.length == n + 1
# 1 <= nums[i] <= n
# All the integers in nums appear only once except for precisely one integer which appears two or more times.

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Input: nums = [1,3,4,2,2]  # Output: 2   1 ~ 4 n = 4  i < n + 1
        #  index i + 1 == value in the nums
        # interate length: p1
        #   1  3  4  2  2 
        #   0  1  2  3  4
        #          slowfast 
        # visited   cycle 
        slow, fast = 0, 0
        slow = nums[slow]
        fast = nums[nums[fast]]
        n = len(nums)
        while nums[slow] != nums[fast]:
            slow = nums[slow]
            fast = nums[nums[fast]]
        p1, p2 = 0, slow
        while p1 != p2:
            p1 = nums[p1]
            p2 = nums[p2]
        return p1


# formula for finding the entrance of the cycle: 2(F + a) = F + nC + a
# input => nums = [3,1,3,4,2]
#                  0 1 2 3 4
# output => 3
#  1 - 2 \
#         9 -  1~ n
#   4- 3 /
input = [2,5,9,6,9,3,8,9,7,1]
#        0 1 2 3 4 5 6 7 8 9
#input = [2,5,10,6,9,3,8,4,7,1]
#         0 1 2 3 4 5 6 7 8 9
# output => 9

# input: [1 2 3]
#         0 1 2

solution = Solution()
print(solution.findDuplicate(input))
