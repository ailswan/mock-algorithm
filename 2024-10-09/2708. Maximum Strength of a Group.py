from typing import List 

# 2708. Maximum Strength of a Group
# You are given a 0-indexed integer array nums representing the score of students in an exam. 
# The teacher would like to form one non-empty group of students with maximal strength, where the strength of a group of students of indices i0, i1, i2, ... , ik 
# is defined as nums[i0] * nums[i1] * nums[i2] * ... * nums[ik​].

# Return the maximum strength of a group the teacher can create.

 

# Example 1:

# Input: nums = [3,-1,-5,2,5,-9]
# Output: 1350
# Explanation: One way to form a group of maximal strength is to group the students at indices [0,2,3,4,5]. Their strength is 3 * (-5) * 2 * 5 * (-9) = 1350, which we can show is optimal.
# Example 2:

# Input: nums = [-4,-5,-4]
# Output: 20
# Explanation: Group the students at indices [0, 1] . Then, we’ll have a resulting strength of 20. We cannot achieve greater strength.
 

# Constraints:

# 1 <= nums.length <= 13
# -9 <= nums[i] <= 9
from functools import reduce

class Solution:
    def maxStrength(self, nums: List[int]) -> List[int]:
        # dp, bottom-up
        # try calculating the strength for every possible combination of groups of students, updating the max strength
        # 2 choices:
            # include the number in max strength
            # don't include number in max strength
        # n = len(nums)
        # dp1 = [float("-inf")] * n
        # dp2 = [float("-inf")] * n
        # dp1[0] = nums[0]

        # for i in range(1, n):
        #     dp1[i] = max(dp1[i], dp1[i - 1] * nums[i])


        # backtracking
        # iterate through the input, keep track of the current list of elements
        # at every backtrack call, check if it's the max stregnth, update ans
        # pop from current list

        ans = 0

        def backtrack(start, cur):
            nonlocal ans
            ans = max(ans, reduce((lambda x, y: x * y), cur))

            for i in range(start, len(nums)):
                cur.append(nums[i])
                backtrack(i + 1, cur)
                cur.pop()
        
        backtrack(0, [])
        return ans

# time => O(2^n) where n is the length of nums
# space => O(2^n) for the callstack