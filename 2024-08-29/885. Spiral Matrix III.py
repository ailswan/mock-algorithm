from typing import List

#  885. Spiral Matrix III

# You start at the cell (rStart, cStart) of an rows x cols grid facing east.
# The northwest corner is at the first row and column in the grid, and the southeast corner is at the last row and column.

# You will walk in a clockwise spiral shape to visit every position in this grid.
# Whenever you move outside the grid's boundary, we continue our walk outside the grid (but may return to the grid boundary later.).
# Eventually, we reach all rows * cols spaces of the grid.

# Return an array of coordinates representing the positions of the grid in the order you visited them.

 

# Example 1:
# https://s3-lc-upload.s3.amazonaws.com/uploads/2018/08/24/example_1.png

# Input: rows = 1, cols = 4, rStart = 0, cStart = 0
# Output: [[0,0],[0,1],[0,2],[0,3]]
# Example 2:
# https://s3-lc-upload.s3.amazonaws.com/uploads/2018/08/24/example_2.png

# Input: rows = 5, cols = 6, rStart = 1, cStart = 4
# Output: [[1,4],[1,5],[2,5],[2,4],[2,3],[1,3],[0,3],[0,4],[0,5],[3,5],[3,4],[3,3],[3,2],[2,2],[1,2],[0,2],[4,5],[4,4],[4,3],[4,2],[4,1],[3,1],[2,1],[1,1],[0,1],[4,0],[3,0],[2,0],[1,0],[0,0]]
 

# Constraints:

# 1 <= rows, cols <= 100
# 0 <= rStart < rows
# 0 <= cStart < cols

class Solution:
    def spiralMatrix(self, rows, cols, rStart, cStart) -> List[List[int]]:
        # first move is to the right
        # second move is down
        # third is left
        # forth is up
        # update answer with the rStart,cStart
        # iterate through the directions... after going through all directions, update directions with the multiplier for the next set of indices
        # increment multiplier after every directional move

        # keep track of all visited cells
        # if I traverse through all directions (with multipliers) and don't see a cell (or come across cell in visited), that means we have completed the traversal -> return answer


        # Input: rows = 1, cols = 4, rStart = 0, cStart = 0
        # Output: [[0,0],[0,1],[0,2],[0,3]]
        # steps =>             1 1 2 2    3 3 4 4     5 5 6 6  7 7 8 8....
        # multiplier           1   1+1    3  3 + 1
        # for _ in range(multiplier):
            # 5 6  1 4 
        directions = [(0, 1), (1, 0),(0, -1),(-1, 0)]
        multiplier = 1
        ans = [[rStart, cStart]]            # [0,0]
        

        while len(ans) != (rows * cols):        # 2 != 4? T
            for r_offset, c_offset in directions[:2]:           #(1,0)
                for i in range(multiplier): #multiplier = 0 -> 2
                    rStart = r_offset + rStart              # rStart = 1 + 0
                    cStart = c_offset + cStart              # cStart = 0 + 1
                    
                    if 0 <= rStart < rows and 0 <= cStart < cols:       # 0 <= 1 < 1 and 0 <= 1 < 4? False
                        ans.append([rStart, cStart])                    # ans = [(0,0), (0, 1)]

            multiplier += 1                                         # mul = 2
            # rStart = 1
            # cStart = 1
            for r_offset, c_offset in directions[2:]:               # [(-1, 0), (0, -1)]   [1, 0]
                for i in range(multiplier): # mul = 0 -> 2: 1, 2
                    rStart = r_offset + rStart                  # rStart = -1 + 1 -> 0
                    cStart = c_offset + cStart                  # cStart = 0 + -2 -> -2
                    
                    if 0 <= rStart < rows and 0 <= cStart < cols:       # 0 <= 0 < 1 and 0 <= -2 < 4? False
                        ans.append([rStart, cStart])
            multiplier += 1
        return ans



# time => O(row * col)   O((max(R,C)) ^2) worest case
# space => O(1)

# Complexity
# Time complexity:
# O(layer ^2)
# Space complexity:
# O(rows×cols)


class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        res =[(rStart, cStart)]
        if rows * cols == 1:
            return res
        for k in range(1, 2*(rows + cols), 2):  # 1  3  5  7 
            for dx, dy, step in [(0, 1, k),(1, 0, k),(0, -1, k + 1),(-1, 0, k + 1)]:
                for i in range(step): 
                    rStart, cStart =  rStart + dx, cStart + dy
                    if 0 <= rStart < rows and 0 <= cStart < cols:
                        res.append((rStart, cStart))
                        if len(res) == rows * cols:
                            return res