from typing import List

# 286. Walls and Gates

# You are given an m x n grid rooms initialized with these three possible values.

# -1 A wall or an obstacle.
# 0 A gate.
# INF Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.
# Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.

 

# Example 1:

# https://assets.leetcode.com/uploads/2021/01/03/grid.jpg


# Input: rooms = [[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]
# Output: [[3,-1,0,1],[2,2,1,-1],[1,-1,2,-1],[0,-1,3,4]]
# Example 2:

# Input: rooms = [[-1]]
# Output: [[-1]]
 

# Constraints:

# m == rooms.length
# n == rooms[i].length
# 1 <= m, n <= 250
# rooms[i][j] is -1, 0, or 231 - 1.

class Solution:
    def findGate(self, rooms: List[list[int]]) -> None:
        # 0 is gate
        # if is a empty room  BFS
        # start from gate  to fill all room 
        empty = 2147483647
        m, n = len(rooms), len(rooms[0]) # 4, 4
        q = [] 
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:# 0, 0 
                    q.append((i, j, 0)) 
        #[(0, 2, 0), (3, 0 , 0 )]
        
        while q:
            l = len(q)# 3
            temp = []
            for i in range(l):
                x, y, level = q[i]#  0 2 level 0 # 3 0 level 0 # 0 3 level= 1#1 2 level 1 # 2 0 level1
                for dx, dy in [(1,0),(0,1),(-1,0),(0,-1)]:
                    cx, cy = x + dx, y + dy # 1 2 # 2  0 # 2 2  1, 2 # 1 0 
                    if 0 <= cx < m and 0 <= cy < n and rooms[cx][cy] == empty:
                        rooms[cx][cy] = level + 1
                        temp.append((cx, cy, level + 1))#[(2, 2 , 2), (1, 1, 2)]
            q = temp# [(0, 3, 1),(1, 2, 1),(2, 0 ,1)]
        return rooms
     

    #time complexity O(m* n)
    #space compleixty O(m * n) worst case