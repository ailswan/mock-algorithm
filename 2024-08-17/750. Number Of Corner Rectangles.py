from typing import List

# 750. Number Of Corner Rectangles

# Given an m x n integer matrix grid where each entry is only 0 or 1, return the number of rectangles.

# A corner rectangle is four distinct 1's on the grid that forms an axis-aligned rectangle (no diamonds). Note that only the corners need to have the value 1 (edges can be 0's). Also, all four 1's used must be distinct (no double counting rectangles).

# Input: grid = [[1,0,0,1,0],[0,0,1,0,1],[0,0,0,1,0],[1,0,1,0,1]]
# Output: 1
# Explanation: There is only one corner rectangle, with corners grid[1][2], grid[1][4], grid[3][2], grid[3][4].

# 1 0 0 1 0 
# 0 0 1 0 1
# 0 0 0 1 0
# 1 0 1 0 1


# Input: grid = [[1,1,1],[1,1,1],[1,1,1]]
# Output: 9
# Explanation: There are four 2x2 rectangles, four 2x3 and 3x2 rectangles, and one 3x3 rectangle.

# Input: grid = [[1,1,1,1]]
# Output: 0
# Explanation: Rectangles must have four distinct corners.
#  1  1  1  1

# 1  1 
# 1  1


#  Constraints:

# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 200
# grid[i][j] is either 0 or 1.
# The number of 1's in the grid is in the range [1, 6000].

# corner: [0,0], [0, n - 1], [m - 1, 0], [n - 1, m - 1]; one of the corners must be at one of these indices
# directions: [(0, -1), (0, 1], (1, 0), (-1, 0)]

class Solution:
  def numberOfCornerRectangles(self, grid: List[List[int]]):
    # first we check each of the 4 corners of the grid
    # if a corner has a "1", we look for a valid rectangle
    # can use bfs to "expand" the length/width (from corner up to n - 1, m - 1) of the sides and check for valid rectangles
    # squares are also valid rectangles
    # update the answer if there exists valid rectangles
    # edge case => m and n must both be GTE 1
    rows = len(grid)
    cols = len(grid[0])
    ans = [0] # storing a single integer value to be returned

    corner_indices = [(0, 0), (rows - 1, 0), (0, cols - 1), (rows - 1, cols - 1)]
    directions = [(0, -1), (0, 1), (1, 0), (-1, 0)]
    # 9 0 9 1 1   （0，3）    1 0 0 1 0                ct+= 1
    # 0 0 1 0 1                 
    # 0 0 0 1 0                 
    # 9 0 9 0 1

    if len(grid) < 2 and len(grid[0]) < 2:
      return 0

    visited = {}

    for corner_r_index, corner_c_index in corner_indices:     #corner_indices: (0, 0)
      if grid[corner_r_index][corner_c_index] == 1:
        # expand on rectangle
        start_index = [corner_r_index, corner_c_index]
        self.updateValidRectangle(grid, rows - 1, cols - 1, start_index, ans)
    
  def updateValidRectangle(self, grid, rows, cols, start, ans):
    if start[0] == 0 and start[1] == 0:
      i = 0
      j = 0     # (&) our starting corner
      for r_offset in range(rows):            # r_offset = 2
        #row  = grid[r_offset]               # 1 0 0 1 0  (0,0) (1,3)                                             # 1 0 0 1 0 
        if grid[i + r_offset][j] == 1:          # (&) one of the corners for a potential                                          # 0 0 0 0 0
          for c_offset in range(1, cols):          # c_offset = 0                                                                    # 1 0 0 1 0
            if grid[i + r_offset][j + c_offset] == 1 and grid[i][j + c_offset] == 1:   # grid[0][3] == 1? grid[]
              ans[0] += 1

    # 9 0 0 1 9            (0,0) ------  (0,3)  
    # 0 0 1 0 1            (1,0) ------  (1,3)
    # 0 0 1 1 1            (2,0) ------  (2,3)   
    # 9 0 1 0 0  
    
    # 1 0 1    1 1
    # 1 1 1    1 1  


    if start[0] == rows - 1 and start[1] == cols - 1:
      i = start[0]
      j = start[1]
      for r_offset in range(rows - 1, -1, -1):

        for c_offset in range(cols):
          if grid[i - r_offset][j - c_offset] == 1 and grid[i][j - c_offset] == 1 and grid[i - r_offset][j] == 1:
            ans += 1

# time => (rows * cols * rows)
# space => (cols^2)

#class Solution:
    # def countCornerRectangles(self, grid: List[List[int]]) -> int:
    #     count = collections.Counter()
    #     ans = 0
    #     for row in grid:
    #         for c1, v1 in enumerate(row):
    #             if v1:
    #                 for c2 in range(c1 + 1, len(row)):
    #                     if row[c2]:
    #                         ans += count[c1, c2]
    #                         count[c1, c2] += 1
    #     return ans