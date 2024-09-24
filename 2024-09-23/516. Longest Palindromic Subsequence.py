from typing import List 

# 516. Longest Palindromic Subsequence

# Given a string s, find the longest palindromic subsequence's length in s.

# A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.

 

# Example 1:

# Input: s = "bbbab"
# Output: 4
# Explanation: One possible longest palindromic subsequence is "bbbb".
# Example 2:

# Input: s = "cbbd"
# Output: 2
# Explanation: One possible longest palindromic subsequence is "bb".
 

# Constraints:

# 1 <= s.length <= 1000
# s consists only of lowercase English letters.

class Solution:
    def longestPalindromic(self, s: str) -> int:
        # s = "a b b b a b"
        #        0 1 2 3 4
        #      l         r
        #  loop mid expand l and r
        #   l r in the range  if l == r : move l, r, if l != r: (1) move l (2) move r (3)move both l and r
        #    during process: tracking max_length of palindromic
        n = len(s)
        max_length = 0
        dp=[[0] * n for _ in range(n)] #   value  dp[l][r] means str[l: r + 1]  max length of palindrom
        l = n - 1

        #s = "b b a a b" n = 5 
        #     0 1 2 3 4
        #       l     r
        while l >= 0: # 0 
            r = l # 0          
            while r < n:
                if r == l:
                    dp[l][r] = 1 
                elif s[l] == s[r]:
                    dp[l][r] = dp[l + 1][r - 1] + 2# dp[1][2] = 1 dp[1][3] = 1  dp[2][3] + 2
                else: # a b b b b b a
                      #          lr 
                    dp[l][r] = max(dp[l + 1][r], dp[l][r - 1])
                r += 1
            l -= 1
        return dp[0][n - 1]
    #time complexity O(n^2)
    # space complexity O(n^2)

# [
#     [0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0],
# ]
        
                


            




        
        for t in range(n * 2 - 1):
            m = t // 2
            l = m - t % 2
            r = m + t % 2
            dp[m][m] = 1
            while l >= 0 and r < n - 1:
                if s[l] == s[r]:
                    l -= 1
                    r += 1
                    dp[m][l] += 1
                    dp[m][r] += 1
                else:
                    # a c b b b r a 
                    # s[l - 1] and s[r + 1]
                    
                    


   








