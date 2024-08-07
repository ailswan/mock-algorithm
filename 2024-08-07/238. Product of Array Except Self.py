from typing import List
# 238. Product of Array Except Self

# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.

# Example 1:

# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]

# Example 2:

# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]
 

# Constraints:

# 2 <= nums.length <= 105
# -30 <= nums[i] <= 30
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.


class Solution():
    def find_product(self, nums:List[int]):
        # perform a 2 iteration pass, front and back, in the array
        # forward pass -> skip the current val, multiply every other number we encounter
        # backward pass -> take the intermediate and multiply by the numbers except the current val
         # 1  2 | 3 | 4  5
         #        i
    # ans/l1  1   2    6  24
    # R   60  60  20   5  1
    # ans 60  60  40   30  24
        ans_l = [1] * len(nums)
        ans_r = [1] * len(nums)

        for i in range(1, len(nums)):
            ans_l[i] = ans_l[i - 1] * nums[i - 1]

        # 1, 1, 2, 6
        
        for i in range(len(nums) - 2, -1, -1):
            ans[i] =  * nums[i + 1]
            

        # 1, 1, 2, 6
        return ans



# class Tests(unitTest.testCase):

# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]
    
# ans = [1, 1, 1, 1]
# ans = [2, 3, 4, 1]










 
#139. Word Break
#this is a template for mock questions
# class Solution:
#     def wordBreak(self, s: str, wordDict: List[str]) -> bool:
#         #dp[i]  [:i] can be separated or not
#         #dp[i] = dp[i - n] if s[i - n: i] n is the length of word
#         l = len(s)
#         dp = [False] * (l + 1)
#         dp[0] = True
#         for i in range(1, l + 1):
#             for w in wordDict:
#                 n = len(w)
#                 if s[i - n: i] == w and dp[i - n]:
#                     dp[i] = True
#                     break
#         return dp[-1]

# solution = Solution()
# s1 = "leetcode"
# wordDict1 = ["leet", "code"]
# print(solution.wordBreak(s1, wordDict1))

# s2 = "applepenapple"
# wordDict2 = ["apple", "pen"]
# print(solution.wordBreak(s2, wordDict2)) 

# s3 = "catsandog"
# wordDict3 = ["cats", "dog", "sand", "and", "cat"]
# print(solution.wordBreak(s3, wordDict3))


# # test mode
# # Test case 1
# s1 = "leetcode"
# wordDict1 = ["leet", "code"]
# assert solution.wordBreak(s1, wordDict1) == True, "Test case 1 failed"

# # Test case 2
# s2 = "applepenapple"
# wordDict2 = ["apple", "pen"]
# assert solution.wordBreak(s2, wordDict2) == True, "Test case 2 failed"

# # Test case 3
# s3 = "catsandog"
# wordDict3 = ["cats", "dog", "sand", "and", "cat"]
# assert solution.wordBreak(s3, wordDict3) == False, "Test case 3 failed"

# print("All test cases passed!")