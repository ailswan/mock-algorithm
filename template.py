from typing import List


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