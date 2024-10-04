from typing import List

# 72. Edit Distance

# Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

# You have the following three operations permitted on a word:

# Insert a character
# Delete a character
# Replace a character
 

# Example 1:

# Input: word1 = "horse", word2 = "ros"
# Output: 3
# Explanation: 
# horse -> rorse (replace 'h' with 'r')
# rorse -> rose (remove 'r')
# rose -> ros (remove 'e')
# Example 2:

# Input: word1 = "intention", word2 = "execution"
# Output: 5
# Explanation: 
# intention -> inention (remove 't')
# inention -> enention (replace 'i' with 'e')
# enention -> exention (replace 'n' with 'x')
# exention -> exection (replace 'n' with 'c')
# exection -> execution (insert 'u')
 

# Constraints:

# 0 <= word1.length, word2.length <= 500
# word1 and word2 consist of lowercase English letters.

class Solution:
    def editDistance(self, word1: str, word2: str) -> int:
        # " h o o s r s e" j
                        #  j
        # " r o o s "  i 
                #    i
        #  chr_i != chr_j  delete  j += 1 d += 1
        #                  replace i += 1 j += 1  d += 1
        #                  insert  i += 1 d += 1
        #  dp[i][j] = min(dp[i][j - 1] + 1, dp[i - 1][j - 1] + 1, dp[i - 1][j] + 1)       if chr_i != chr_j  else 0 i +=1 j += 1

        # input: "a"
        # output: "hjjja"
        m, n = len(word1), len(word2)
        if m == 0 or n == 0:
            return max(m, n)
        dp = [[0] * m for i in range(n)]
        for i in range(n):#1
            for j in range(m): #0
                if word1[j] == word2[i]:
                    if i > 0 and j > 0:
                        dp[i][j] = dp[i - 1][j - 1]
                    else:
                        dp[i][j] = max(i, j)
                    # i == 0 j == 0
                else:                           # i = 3; j = 0      # dp[2][0]?
                    if i == 0 and j == 0:
                        dp[i][j] = 1
                    elif j == 0:
                        dp[i][j] = i + 1
                    elif i == 0:
                        dp[i][j] = j + 1
                    else:
                        dp[i][j] = min(dp[i][j - 1] + 1, dp[i - 1][j - 1] + 1, dp[i - 1][j] + 1)  
        return dp[n - 1][m - 1]

