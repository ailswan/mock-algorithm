from typing import List
# 554. Brick Wall
# There is a rectangular brick wall in front of you with n rows of bricks. 
# The ith row has some number of bricks each of the same height (i.e., one unit) but they can be of different widths. The total width of each row is the same.

# Draw a vertical line from the top to the bottom and cross the least bricks. If your line goes through the edge of a brick, then the brick is not considered as crossed. 
# You cannot draw a line just along one of the two vertical edges of the wall, in which case the line will obviously cross no bricks.

# Given the 2D array wall that contains the information about the wall, return the minimum number of crossed bricks after drawing such a vertical line.

# Input: wall = [[1,2,2,1],[3,1,2],[1,3,2],[2,4],[3,1,2],[1,3,1,1]]
# Output: 2

# [      |
#   [1,2,2,1],
#   [3,1,|2],
#   [1,3,|2],
#   [2,  4  ],
#   [3,1,|2],
#   [1,3,| 1,1]
# ]


# Example 2:

# https://assets.leetcode.com/uploads/2021/04/24/cutwall-grid.jpg


# Input: wall = [[1],[1],[1]]
# Output: 3
 

# Constraints:

# n == wall.length
# 1 <= n <= 104
# 1 <= wall[i].length <= 104
# 1 <= sum(wall[i].length) <= 2 * 104
# sum(wall[i]) is the same for each row i.
# 1 <= wall[i][j] <= 231 - 1

# return the number of crossed bricks
class Solution:
  def minCrossBricks(self, wall: List[List[int]]) -> int:
    # break up the wall into unit sized columns
    # for each col unit, find out how many rows of bricks we are "breaking"
    # keep track of the minimum rows broken


# [      |
#   [1,2,2,1], 
#   [3,1,|2],
#   [1,3,|2],
#   [2,  4  ],
#   [3,1,|2],
#   [1,3,| 1,1]
# ]
# ^

    min_broken = float("inf") # *** if looking for MINIMUM of something, start with INFINITY <float("inf")>, and vice versa ****
    max_col_size = sum(wall[0])  # 6

    for i in range(1, max_col_size):   # i = 1  # 2
      broken_walls = 0
      for j in range(len(wall)):    # j = 0
        is_crack = False
        units = i                   # units = 2
        for k in range(units, len(wall[j])):       # k = 2
          units -= wall[j][k]            # 2 - wall[j][k] => 2 - 2 = 0
          if units == 0:
            is_crack = True         #is_crack == True
            break
        if not is_crack:
          broken_walls += 1         # broken_walls = 1   # 1
      min_broken = min(min_broken, broken_walls) # 1
    
    return min_broken


# time => (N^3)
# space => (1)


from typing import List

class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        col_size = sum(wall[0])  # Total width of the wall
        min_broken = len(wall)  # Start with the worst-case scenario

        for i in range(1, col_size):  # Skip the edges (start from 1)
            broken_walls = 0
            for row in wall:
                units = i
                for brick in row:
                    units -= brick
                    if units == 0:  # If the line falls exactly at the edge
                        break
                    if units < 0:  # If the line falls inside a brick
                        broken_walls += 1
                        break
            min_broken = min(min_broken, broken_walls)

        return min_broken

# col_map = {col:gap number}  iterate matrix  {1:3}  min(len(walls) - gaps)
#  -- | -- | --
#  -- | -- | --
#  ------------
#  -- | -------
#    col1  col2
#     3     2
# n = 4  max(col_map.values())
# n * m

class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        #col_map = {col:gap number}
        col_map = defaultdict(int)
        for row in wall:
            col = 0 #[6] 
            for i in row[:-1]:
                col += i
                col_map[col] += 1
        if len(col_map) == 0:
            return len(wall)
        return len(wall) - max(col_map.values())

    