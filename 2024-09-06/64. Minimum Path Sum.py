from typing import List

# 64. Minimum Path Sum

# Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

# Note: You can only move either down or right at any point in time.

 

# Example 1:

# | (1) | (3) | (1) |
# -------------------
# |  1  |  5  | (1) |
# -------------------
# |  4  |  2  | (1) |


# Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
# Output: 7
# Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.
# Example 2:

# Input: grid = [[1,2,3],[4,5,6]]
# Output: 12
 

# Constraints:

# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 200
# 0 <= grid[i][j] <= 200

class Solution:
    def miniPath(self, grid: List[List[int]]) -> int:
        #         dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
        #first row dp[0][j] = dp[0][j - 1] + grid[0][j]
        #first col dp[i][0] = dp[0][i - 1] + grid[0][i]
        m, n = len(grid), len(grid[0])
        dp = [[0] * n for i in range(m)]
        dp[0][0] = grid[0][0]
        for j in range(1, n):
            dp[0][j] = dp[0][j - 1] + grid[0][j]
        for i in range(1, m):
            dp[i][0] = dp[i - 1][0] + grid[i][0]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
        return dp[m - 1][n - 1]
    # time complexity O(m * n)
    # space complexity O(m * n)
class Solution:
    def miniPath(self, grid: List[List[int]]) -> int:
      # input: [[1,3,1],[1,5,1],[4,2,1]]
      #  1   3   1
      #  1   5   1 
      #  4   2   1
        m, n = len(grid), len(grid[0]) # 3 , 3
        dp1, dp2 = [0] * n, [0] * n #[0, 0 , 0] [0, 0, 0]
        for i in range(n):
            dp1[i] = dp1[i - 1] + grid[0][i]
            #[1, 4, 5]
        for i in range(1, m):
            for j in range(n):      #dp1[1, 4, 5] # dp1 = [2, 7, 6 ]
                if j == 0:
                    dp2[j] = dp1[j] + grid[i][j]
                else:
                    dp2[j] = min(dp1[j], dp2[j - 1]) + grid[i][j]
                    # dp2 = [2, 7, 6 ] dp2 =[6, 8, 7]
            dp1 = dp2[:] #dp1= [6, 8, 7]
        return dp2[-1] #dp1= [6, 8, 7]
    # time complexity O(m * n)
    # space complexity O(n)

    #2-d 3-d
    
        

