from typing import List

# 827. Making A Large Island

# You are given an n x n binary matrix grid. You are allowed to change at most one 0 to be 1.

# Return the size of the largest island in grid after applying this operation.

# An island is a 4-directionally connected group of 1s.

 

# Example 1:

# Input: grid = [[1,0],[0,1]]
# 1  0 
# 0  1
# Output: 3
# Explanation: Change one 0 to 1 and connect two 1s, then we get an island with area = 3.
# Example 2:

# Input: grid = [[1,1],[1,0]]
# Output: 4
# Explanation: Change the 0 to 1 and make the island bigger, only one island with area = 4.
# Example 3:

# Input: grid = [[1,1],[1,1]]
# Output: 4
# Explanation: Can't change any 0 to 1, only one island with area = 4.
 

# Constraints:

# n == grid.length
# n == grid[i].length
# 1 <= n <= 500
# grid[i][j] is either 0 or 1.

class Solution:
    def largeIsland(self, grid: List[List[int]]) -> int:
        # connected the largest two 
        # dfs count the size 
        # not change grid[i][j] == 1,  dfs(i, j) find the largest one. 
        # if grid[i][j] == 0 , it can be changed  , grid[i][j] = 1 , dfs(i, j) update res
        m, n = len(grid), len(grid[0])
        visited = [[0]* n for i in range(m)]
        self.res = 0

        def dfs(i, j, grid, visited, ct): 
            visited[i][j] = 1
            if grid[i][j] == 1:       
                # ct += 1 # 3
                # self.res = max(self.res, ct) #3    
                ct = 1
            for dx, dy in [(0,1),(1,0),(-1,0),(0,-1)]:
                cx, cy = i + dx, j + dy
                if 0 <= cx < m and 0 <= cy < n and visited[cx][cy] == 0 and grid[cx][cy] == 1:
                    ct+= dfs(cx, cy, grid, visited, ct)  #1, 1 , grid,visited, 2
            return ct
            
        #[[1,1],[1,1]]
        # 1 0 
        # 0 1

        #{1} 1 
        # 0 (1)
        for i in range(m): 
            for j in range(n):  
                if grid[i][j] == 1:
                    self.res = dfs(i, j, grid, visited, 0)                     
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    visited = [[0]* n for i in range(m)]
                    grid[i][j] = 1
                    self.res = max(self.res, dfs(i, j, grid, visited, 0))
                    grid[i][j] = 0
                   
        return self.res

            
grid = [[1,0],[0,1]]
solution = Solution()
print(solution.largeIsland(grid))
            

