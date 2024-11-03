from typing import List

# 994. Rotting Oranges

# You are given an m x n grid where each cell can have one of three values:

# 0 representing an empty cell,
# 1 representing a fresh orange, or
# 2 representing a rotten orange.
# Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

# Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

#  https://assets.leetcode.com/uploads/2019/02/16/oranges.png

# Example 1:


# Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
# Output: 4
# Example 2:

# Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
# Output: -1
# Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
# Example 3:

# Input: grid = [[0,2]]
# Output: 0
# Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.
 

# Constraints:

# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 10
# grid[i][j] is 0, 1, or 2.

class Solution:
    def rottingOranges(self, grid: List[List[int]]) -> int:
        # [[2,2,2, 0, 1],
        #  [2,2,0, 0, 0 ],
        #  [0,2,2, 0, 0 ]]
        # [[2,1,1],[1,1,0],[0,1,1]]
        # bfs  count the level as mins
        m, n = len(grid), len(grid[0]) # 3 , 3 
        rotten = [] 
        res = 0
        oranges = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    rotten.append((i, j)) #[(0, 0)]
                if grid[i][j] == 1:
                    oranges += 1 # 6 
        if oranges == 0:
            return 0 
        while rotten: # [(0, 0)] # [(1, 0),(0, 1)]# [(1, 1),(0, 2)] #[(2, 1)]  #[(2,2)] #[]  #[]
            temp = []
            for x, y in rotten:
                for dx, dy in [(1,0),(0,1),(-1,0),(0,-1)]:
                    cx, cy = x + dx, y + dy
                    if  0 <= cx < m and 0 <= cy < n and grid[cx][cy] == 1:
                        grid[cx][cy] = 2
                        oranges -= 1 # 0
                        temp.append((cx, cy)) #temp = [(1, 0),(0, 1)] # [(1, 1),(0, 2)]#[(2, 1)] #[(2,2)]
            res += 1# 4 # 5 
            if oranges == 0: # 1 != 0
                return res
            rotten = temp #[(2,2)] #[]
        return -1


#time complexity O(m * n)
# space complexity O(m * n) 

# [[0,2]]
solution = Solution()
grid = [[2,1,1],[1,1,0],[0,1,1]]
print(solution.rottingOranges(grid))