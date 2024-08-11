from typing import List

# 200. Number of Islands

# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 

# Example 1:

# Input: grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# Output: 1

# Example 2:

# Input: grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# Output: 3
 

# Constraints:
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 300
# grid[i][j] is '0' or '1'.

class Solution:
    def __init__(self):
        self.m = 0
        self.n = 0 
 
    def countIsland(self, grid: List[List[str]]) -> int:
        # directions  four dirts
        # interate grid, check if "1" dfs  count+= 1
        # copy matrix to label the visited
        # if not visited and cell == 1 and inside boundary : mark as visited 
        # Input: grid = [
        #   ["1","1","0","0","0"], # 0
        #   ["1","1","0","0","0"], # 1
        #   ["0","0","1","0","0"], # 2
        #   ["0","0","0","1","1"]  # 3
        # ]                          m x
        #     0   1   2   3   4   n y
        # Output: 3

        # visited = [
        #   ["0","0","1","1","1"], # 0
        #   ["0","0","1","1","1"], # 1
        #   ["1","1","0","1","1"], # 2
        #   ["1","1","1","0","0"]  # 3
        # ]                          m x
        #     0   1   2   3   4   n y
        directions = [(0,1),(1,0),(-1,0),(0,-1)]
        def dfs(x, y, grid):# label the visited 
            self.visited[x][y] = 0 # x = 3  y= 4
            for dx, dy in range(directions):
                cx, cy = x + dx, y + dy
                if 0 <= cx < self.m and 0 <= cy < self.n and self.visited[cx][cy] and grid[cx][cy] == '1':
                    dfs(cx, cy,  grid) #cx = 3 cy = 4

        self.m, self.n = len(grid), len(grid[0]) # m = 4 n = 5 
        ct = 0
        self.visited = [[1] * self.n for _ in range(self.m)] # 1 == available 0 = visited
        for i in range(self.m):
            for j in range(self.n):
                if grid[i][j] == '1' and self.visited[i][j]:# i = 3 j = 3?
                    ct += 1  # ct = 3
                    dfs(i, j, grid)
        return ct # 3
    # time complexity O(n * m)
    # space complexity O(n * m)


                    

