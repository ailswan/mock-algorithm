# 78. Subsets
# Given an integer array nums of unique elements, return all possible 
# subsets
#  (the power set).

# The solution set must not contain duplicate subsets. Return the solution in any order.

# Example 1:

# Input: nums = [1,2,3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
# Example 2:

# Input: nums = [0]
# Output: [[],[0]]
 
# Constraints:

# 1 <= nums.length <= 10
# -10 <= nums[i] <= 10
# All the numbers of nums are unique.


class Solution:
  def findSubset(self, nums: List[int]) -> int:
    # backtracking
    # traverse through input and add the element to our current list
    # add current_list to answer after iterating through the input


    # input: [1,2,3]
    # Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

    ans = []

    def backtrack(start, curr_list = []):       
      ans.append(curr_list[:])                  # ans = [[]]
      for i in range(start, len(nums)):         # i = 1
        curr_list.append(nums[i])               # curr_list = [1]
        backtrack(i + 1, curr_list)                                   # backtrack(1, [1])         ans.append([1]) -> [[], [1]]        # backtrack(2, [1])
        curr_list.pop()                         # curr_list = [1] --> [] --> [1]
    
    backtrack(0, [])
    return ans

# time => (N *2 ^ N)    SUBSETS OF n NUMBER 2^n
# space => (N * 2 ^ N)  recursion stack AND the backtrack