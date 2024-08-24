from typing import List

# 1091. Shortest Path in Binary Matrix

# Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix. If there is no clear path, return -1.

# A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0)) to the bottom-right cell (i.e., (n - 1, n - 1)) such that:

# All the visited cells of the path are 0.
# All the adjacent cells of the path are 8-directionally connected (i.e., they are different and they share an edge or a corner).
# The length of a clear path is the number of visited cells of this path.

 

# Example 1:

# 0  1
# 1  0

# Input: grid = [[0,1],[1,0]]
# Output: 2
# Example 2:

# | 0 | 0 | 0 |       | 0 > 0 | 0 |
#                             \  
# | 1 | 1 | 0 |       | 1 | 1 | 0 |
#                               |
# | 1 | 1 | 0 |       | 1 | 1 | 0 |

# Input: grid = [[0,0,0],[1,1,0],[1,1,0]]
# Output: 4
# Example 3:

# Input: grid = [[1,0,0],[1,1,0],[1,1,0]]
# Output: -1
 
#  1  0  0
#  1  1  0 
#  1  1  0 

# Constraints:

# n == grid.length
# n == grid[i].length
# 1 <= n <= 100
# grid[i][j] is 0 or 1

class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        #start   track all possible paths and keep updating the shortest length
        #res    8 directions 
        directions =[(1,0),(0,1),(-1,0),(0,-1),(1,1),(-1,-1),(-1,1),(1,-1)]
        res = -1
        #grid = [[0,0,0],      notVisited = [1,1,3],
        #        [1,0,0],                   [0,1,0],
        #        [1,1,0]]                   [0,0,1],
        n = len(grid) 
        notVisited = [[0] * n for _ in range(n) ] #0 = available
        def dfs(x, y, step): # x = 2 y = 2 step = 3
            nonlocal res   # res = 5
            if grid[x][y] != 0:
                return
            if x == n - 1 and y == n - 1:#2 2
                res = min(res, step + 1) if res > 0 else step + 1 #4
            notVisited[x][y] = step + 1
            for dx, dy in directions:
                cx, cy = x + dx, y + dy 
                if 0 <= cx < n and 0 <= cy < n and grid[cx][cy] == 0 and notVisited[cx][cy] == 0:# [2, 2]
                    
                    dfs(cx, cy, step + 1) # 2, 2 , 3

        
        dfs(0,0,0)
        return res
    # time complexity O(n^2)
    # space complexity O(n^2)


        #grid = [[0,0,0],      
        #        [1,0,0],       
        #        [1,1,0]]       
        dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - 1], dp[i][j - 1]) + 1 if grid[i][j] == 0

        n = len(grid)
        dp1 = [float('inf')] * n
        dp2 = [float('inf')] * n
        
        if grid[0][0] == 1 or grid[n-1][n-1]:
            return -1
        else:
            dp1[0] = 1
        for i in range(1, n):
            if grid[0][i] == 0 and dp1[i - 1] != 0:
                dp1[i] = dp1[i - 1] + 1
        for i in range(n):
            dp2 = min(dp1[i], dp1[i - 1],)







class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        max_row = len(grid) - 1
        max_col = len(grid[0]) - 1
        directions = [
            (-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        
        # Helper function to find the neighbors of a given cell.
        def get_neighbours(row, col):
            for row_difference, col_difference in directions:
                new_row = row + row_difference
                new_col = col + col_difference
                if not(0 <= new_row <= max_row and 0 <= new_col <= max_col):
                    continue
                if grid[new_row][new_col] != 0:
                    continue
                yield (new_row, new_col)
        
        # Check that the first and last cells are open. 
        if grid[0][0] != 0 or grid[max_row][max_col] != 0:
            return -1
        
        # Set up the BFS.
        queue = deque()
        queue.append((0, 0))
        grid[0][0] = 1 
        
        # Carry out the BFS.
        while queue:
            row, col = queue.popleft()
            distance = grid[row][col]
            if (row, col) == (max_row, max_col):
                return distance
            for neighbour_row, neighbour_col in get_neighbours(row, col):
                grid[neighbour_row][neighbour_col] = distance + 1
                queue.append((neighbour_row, neighbour_col))
        
        # There was no path.
        return -1