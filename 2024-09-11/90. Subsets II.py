from typing import List

# 90. Subsets II
# Given an integer array nums that may contain duplicates, return all possible 
# subsets
#  (the power set).

# The solution set must not contain duplicate subsets. Return the solution in any order.



# Example 1:

# Input: nums = [1,2,2]
# Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]0
# Example 2:

# Input: nums = [0]
# Output: [[],[0]]
 

# Constraints:

# 1 <= nums.length <= 10
# -10 <= nums[i] <= 10

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # subsets.... backtracking
        # to avoid duplicates, we need to sort the input
        # at each backtrack call, add the current list to the answer

        # Input: nums = [1,2,2]
        # Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
        ans = []
        nums.sort()

        def backtrack(first, cur):      # first = 0, cur = []                           # first = 1, [1]                    # first = 2, cur = [1, 2]
            ans.append(cur[:])          # ans = [[]]                                    # ans = [[], [1]]                   # ans = [[], [1], [1, 2]]


            for i in range(first, len(nums)):               # i = 0, range = 0 ~ 3      # i = 2, range = 1 ~ 3              # i = 2, range = 2 ~ 3
                if i != first and nums[i] == nums[i - 1]:   # 0 != 0 and 1 == 2? False  # 1 != 1 and 2 == 2? True           # 2 != 2 and 2 == 2? True
                    continue
                cur.append(nums[i])                         # cur = [1]                 # cur = [1, 2]
                backtrack(i + 1, cur)                       # backtrack(0 + 1, [1])     # backtrack(1 + 1, [1, 2])
                cur.pop()                                                               # cur = [1]
            
        backtrack(0, [])    # backtrack(0, [])
        return ans

# time => O(N*logN + N * 2^N) where N is the length of the input
# space => O(N * 2^N)