from typing import List

# 1778. Shortest Path in a Hidden Grid

# This is an interactive problem.

# There is a robot in a hidden grid, and you are trying to get it from its starting cell to the target cell in this grid. 
# The grid is of size m x n, and each cell in the grid is either empty or blocked. It is guaranteed that the starting cell and the target cell are different, and neither of them is blocked.

# You want to find the minimum distance to the target cell. However, you do not know the grid's dimensions, the starting cell, nor the target cell.
# You are only allowed to ask queries to the GridMaster object.

# Thr GridMaster class has the following functions:

# boolean canMove(char direction) Returns true if the robot can move in that direction. Otherwise, it returns false.
# void move(char direction) Moves the robot in that direction. If this move would move the robot to a blocked cell or off the grid, the move will be ignored, and the robot will remain in the same position.
# boolean isTarget() Returns true if the robot is currently on the target cell. Otherwise, it returns false.
# Note that direction in the above functions should be a character from {'U','D','L','R'}, representing the directions up, down, left, and right, respectively.

# Return the minimum distance between the robot's initial starting cell and the target cell. If there is no valid path between the cells, return -1.

# Custom testing:

# The test input is read as a 2D matrix grid of size m x n where:

# grid[i][j] == -1 indicates that the robot is in cell (i, j) (the starting cell).
# grid[i][j] == 0 indicates that the cell (i, j) is blocked.
# grid[i][j] == 1 indicates that the cell (i, j) is empty.
# grid[i][j] == 2 indicates that the cell (i, j) is the target cell.
# There is exactly one -1 and 2 in grid. Remember that you will not have this information in your code.

 

# Example 1:
#  1   2
# -1   0
# Input: grid = [[1,2],[-1,0]]
# Output: 2
# Explanation: One possible interaction is described below:
# The robot is initially standing on cell (1, 0), denoted by the -1.
# - master.canMove('U') returns true.
# - master.canMove('D') returns false.
# - master.canMove('L') returns false.
# - master.canMove('R') returns false.
# - master.move('U') moves the robot to the cell (0, 0).
# - master.isTarget() returns false.
# - master.canMove('U') returns false.
# - master.canMove('D') returns true.
# - master.canMove('L') returns false.
# - master.canMove('R') returns true.
# - master.move('R') moves the robot to the cell (0, 1).
# - master.isTarget() returns true. 
# We now know that the target is the cell (0, 1), and the shortest path to the target cell is 2.
# Example 2:

# Input: grid = [[0,0,-1],[1,1,1],[2,0,0]]
# Output: 4
# Explanation: The minimum distance between the robot and the target cell is 4.
# Example 3:

# Input: grid = [[-1,0],[0,2]]
# Output: -1
# Explanation: There is no path from the robot to the target cell.
 

# Constraints:

# 1 <= n, m <= 500
# m == grid.length
# n == grid[i].length
# grid[i][j] is either -1, 0, 1, or 2.
# There is exactly one -1 in grid.
# There is exactly one 2 in grid.


# """
# This is GridMaster's API interface.
# You should not implement it, or speculate about its implementation
# """
#class GridMaster(object):
#    def canMove(self, direction: str) -> bool:
#        
#
#    def move(self, direction: str) -> bool:
#        
#
#    def isTarget(self) -> None:
#        
#
from collections import deque
class Solution(object):
    def findShortestPath(self, master: 'GridMaster') -> int:
        # bfs 
        # q = [(0, 0)]
        #try all directions: empty?  append cur point
        #  1   2
        # -1   0

        #0, 0, -1
        #1, 1, 1
        #2, 0, 0 
        # we are sure there is -1 in grid
        # (0, 0) can be ANY cell in grid
        # BUT (16, 4) MIGHT NOT be -1

        # 1) -1 is guaranteed to be in the grid
        
        # 2) (0, 0) is NOT guaranteed to be -1

        master.canMove("U") # returns True
        #  0 0 0
        #  0 3 0
        #  1 2 1
        #  1 1 s
        
        #  1   2    1
        #  -1   1    0
        #  0    0    0
        #master.canMove("U") return False?
  
        # visited grid
        direction = [(1,0),(-1,0),(0,1),(0,-1)]
        visited = {(3, 2)}
        q = deque([(3, 2, 0)]) # what is the value of (3,2)? Your choices are: 0, -1, 2
        reverse_move = {"D": "U", "U": "D", "R": "L", "L": "R"}
        while q:       
            x, y, step = q.popleft()#(1,-2, 3)
            if master.isTarget(): # False
                return step # 
            for di, d in enumerate(["D","U","R","L"]):# U
                if master.canMove(d):# True
                    dx, dy = direction[di]
                    cx, cy = x + dx, y + dy # 2, -2
                    if (cx, cy) not in visited:
                        master.move(d) # 
                        q.append((cx, cy, step + 1)) #(1,-2, 3)
                        visited.add((cx, cy)) #(0,0) (1, 0)(1,-1) (1,-2)
                        master.move(reverse_move[d])
        return -1
    # Time complexity O(m * n) size of matrix
    # Space complexity O(m * n) as store the visited

# solution approach:
# 1) run DFS through the hidden grid to find all the cells of which you can move
# 2) run BFS to find the shortest path

# https://leetcode.com/problems/shortest-path-in-a-hidden-grid/solutions/5285382/efficient-pathfinding-in-hidden-grids-using-dfs-with-backtracking-and-bfs-to-find-shortest-path/
# The problem involves finding the shortest path in a hidden grid where only the immediate neighbors of the current cell can be accessed.
# Given the constraints, the solution involves two main tasks: exploring the grid to reveal its structure and then finding the shortest path from the start to the target cell.
# Using Depth-First Search (DFS) helps in fully exploring the grid and identifying all reachable cells and obstacles, 
# while Breadth-First Search (BFS) is ideal for finding the shortest path in an unweighted grid once the grid's structure is known.
                    


class Solution(object):
    def findShortestPath(self, master: 'GridMaster') -> int:
        dir_x = (1, -1, 0, 0)
        dir_y = (0, 0, -1, 1)
        dirs = "UDLR"
        q = deque()
        vis = set()

        q.append((master, (0, 0)))
        vis.add((0, 0))
        step = 0

        while q:
            size = len(q)
            while size:
                robot, (x, y) = q.popleft()
                if robot.isTarget():
                    return step
                for i, j, ch in zip(dir_x, dir_y, dirs):
                    pos = (x + i, y + j)
                    if robot.canMove(ch) and pos not in vis:
                        new_rob = copy.copy(robot)
                        new_rob.move(ch)
                        vis.add(pos)
                        q.append((new_rob, pos))
                size -= 1
            step += 1
        
        return -1

                



                
                

        
    
        


        