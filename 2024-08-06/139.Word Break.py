from typing import List
#139. Word Break
#Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.
#Note that the same word in the dictionary may be reused multiple times in the segmentation.
# example 1:

# Input: s = "leetcode", wordDict = ["leet","code"]
# Output: true
# Explanation: Return true because "leetcode" can be segmented as "leet code".
# Example 2:

# Input: s = "applepenapple", wordDict = ["apple","pen"]
# Output: true
# Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
# Note that you are allowed to reuse a dictionary word.
# Example 3:

# Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
# Output: false
 

# Constraints:

# 1 <= s.length <= 300
# 1 <= wordDict.length <= 1000
# 1 <= wordDict[i].length <= 20
# s and wordDict[i] consist of only lowercase English letters.
# All the strings of wordDict are unique.

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        #dp[i]  [:i] can be separated or not
        #dp[i] = dp[i - n] if s[i - n: i] n is the length of word
        l = len(s)
        dp = [False] * (l + 1)
        dp[0] = True
        for i in range(1, l + 1):
            for w in wordDict:
                n = len(w)
                if s[i - n: i] == w and dp[i - n]:
                    dp[i] = True
                    break
        return dp[-1]

solution = Solution()
s1 = "leetcode"
wordDict1 = ["leet", "code"]
print(solution.wordBreak(s1, wordDict1))

s2 = "applepenapple"
wordDict2 = ["apple", "pen"]
print(solution.wordBreak(s2, wordDict2)) 

s3 = "catsandog"
wordDict3 = ["cats", "dog", "sand", "and", "cat"]
print(solution.wordBreak(s3, wordDict3))


# test mode
# Test case 1
s1 = "leetcode"
wordDict1 = ["leet", "code"]
assert solution.wordBreak(s1, wordDict1) == True, "Test case 1 failed"

# Test case 2
s2 = "applepenapple"
wordDict2 = ["apple", "pen"]
assert solution.wordBreak(s2, wordDict2) == True, "Test case 2 failed"

# Test case 3
s3 = "catsandog"
wordDict3 = ["cats", "dog", "sand", "and", "cat"]
assert solution.wordBreak(s3, wordDict3) == False, "Test case 3 failed"

print("All test cases passed!")