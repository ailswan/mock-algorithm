from typing import List

# 5. Longest Palindromic Substring
# Given a string s, return the longest palindromic substring in s.

# Example 1:

# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.
# Example 2:

# Input: s = "cbbd"
# Output: "bb"
 

# Constraints:

# 1 <= s.length <= 1000
# s consist of only digits and English letters.

class Solution:
    def getPalindromicSubstring(s: str) -> str:
        # substring l  mid  r   b a b     b | b
        # track length of the substring , keep update res
        # mid  "c b a a a b c e"   "c b b | b b c e"   
        #      |  l       r    |     |  l      r  |
        # "bbb" "bb"
        # Input: s = "b a b a d"
        #             0 1 2 3 4 
        # Output: "bab"
        #"b a  a  a  d"
        # 0 1  2  3  4
        #   l     r
        max_l = 0
        n = len(s)
        start = 0
        for i in range(n):#n = 4  i = 1
            l = r = i # l = r = 1
            cur_l = 1 # a
            while r < n - 1 and s[r] == s[r + 1]: #a == a?  
                r += 1
                cur_l += 1
            while l > 0 and r < n - 1 and s[l - 1] == s[r + 1]:# l r -> a i = 1 b == d?
                cur_l += 2 # cur_l = 3
                l -= 1 # l = 0 r = 2
                r += 1
            if cur_l > max_l:# 3 > 1
                start = l # start = 0
                max_l = cur_l # max_l = 1
        return s[start: start + max_l] # start = 0 [0: 0 + 3]
            
            


            














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