from typing import List
# 1249. Minimum Remove to Make Valid Parentheses
# Given a string s of '(' , ')' and lowercase English characters.

# Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.

# Formally, a parentheses string is valid if and only if:

# It is the empty string, contains only lowercase characters, or
# It can be written as AB (A concatenated with B), where A and B are valid strings, or
# It can be written as (A), where A is a valid string.

# Constraints:

# 1 <= s.length <= 105
# s[i] is either '(' , ')', or lowercase English letter.

# Example 1:

# Input: s = "lee(t(c)o)de)"
# Output: "lee(t(c)o)de"
# Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.
# Example 2:

# Input: s = "a)b(c)d"
# Output: "ab(c)d"
# Example 3:

# Input: s = "))(("
# Output: ""
# Explanation: An empty string is also valid.


class Solution:
    def validParentheses(self, s:str) -> str:
        # stack  ( push index  into stack, ) pop the stack[-1] if stack 
        # "lee(t(c)o)de))"
        #     3 5         7 9   12
        # stor the deleted index.
        # when the stack empty : if ), remove . if char, append to res. if (. 
        # finish loop of string, ( in stack. remove
        #s = "a ) b ( c ) d"
        #     0 1 2 3 4 5 6
        removeIdx = []
        stack = []
        for i in range(len(s)):# 7  i = 6  removeIdx=[1] stack=[]
            if s[i] == '(':
                stack.append(i)
            if s[i] == ')':
                if stack:
                    stack.pop()
                else:
                    removeIdx.append(i)
        if stack:
            removeIdx = removeIdx + stack
        removeIdx = set(removeIdx) #removeIdx = {1}
        res = ''
        for i in range(len(s)): # "a  b ( c ) d"
            if i not in removeIdx:
                res += s[i]
        return res


        




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