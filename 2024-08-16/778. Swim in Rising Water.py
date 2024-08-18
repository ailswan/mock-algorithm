from typing import List

# 778. Swim in Rising Water

# You are given an n x n integer matrix grid where each value grid[i][j] represents the elevation at that point (i, j).

# The rain starts to fall. At time t, the depth of the water everywhere is t. You can swim from a square to another 4-directionally adjacent square if and only if the elevation of both squares individually are at most t.
# You can swim infinite distances in zero time. Of course, you must stay within the boundaries of the grid during your swim.

# Return the least time until you can reach the bottom right square (n - 1, n - 1) if you start at the top left square (0, 0).

 

# Example 1:
# --------------
# |  0   |  2  |  t = 1  0 1 t = 2 0 1 2        t = 1 (can reach cell == 1 or cell < 1)
# --------------      0 - 1- 3  time 1 + 2
 #                     0 - 2 - 3 time 2 + 1
# |  1  |  3   |
# --------------

# Input: grid = [[0,2],[1,3]]
# Output: 3
# Explanation:
# At time 0, you are in grid location (0, 0).
# You cannot go anywhere else because 4-directionally adjacent neighbors have a higher elevation than t = 0.
# You cannot reach point (1, 1) until time 3.
# When the depth of water is 3, we can swim anywhere inside the grid.
# Example 2:


# Input: grid = [[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]
# Output: 16
# Explanation: The final route is shown.
# We need to wait until time 16 so that (0, 0) and (4, 4) are connected.
 

# Constraints:

# n == grid.length
# n == grid[i].length
# 1 <= n <= 50
# 0 <= grid[i][j] < n2
# Each value grid[i][j] is unique.

class Solution:
    def swimTime(self, grid: List[List[int]]) -> int:
        # --------------
        # |  0   |  2  |  t = 1  0 1 t = 2 0 1 2        t = 1 (can reach cell == 1 or cell < 1)
        # --------------       
        #                      
        # |  1  |  3   |   labels = grid copy cells
        # --------------     
        #  four dirctions  checking:  next step <= t: labels visited & tracking the step 
        # if label[m - 1][n - 1] :return step
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        self.m, self.n = len(grid), len(grid[0])
        self.visited = [[0] * self.n for i in range(self.m) ] #0 = available num. = step
        self.grid = grid
        if self.m <= 1 and self.n <= 1:
            return 0 
    
        def dfs(x, y):#  t = 3 [1][0]
            if self.visited[x][y] == 0:
                self.visited[x][y] = self.t  # 2
            for dx, dy in directions:
                cx, cy = dx + x, dy + y
                if 0 <= cx < self.m and 0 <= cy < self.n and\
                    self.visited[cx][cy] == 0 and\
                    self.grid[cx][cy] <= self.t: # 3 <= 3
                         dfs(cx, cy) #  [0][1]

        #visited   1  2
        #          1  3 
        self.t = 0
        self.stack = []#[[][(x,y)(x1,y1)][]]
        self.visited[0][0] = 1
        while self.visited[self.m - 1][self.n - 1] == 0: #[1][1] = 3
            self.t += 1 # t = 3
            # for i in range(self.m):
            #      for j in range(self.n):
            #           if self.visited[i][j] != 0: #[0, 0] [1, 0] [0,1]
            #                dfs(i, j)
            for x, y in self.stack[self.t - 1]:
                 dfs(x, y)
                 

        return self.visited[self.m - 1][self.n - 1]
    
# You can swim infinite distances in zero time.

    # time complexity O(m^2 * n^2)
    # space complexity O(m * n)




import heapq

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        pq = [(grid[0][0], 0, 0)]
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        n = len(grid)
        visited = [[False] * n for _ in range(n)]
        #  0 2   True False 
        #  1 3   False False
        while pq: # 
            elevation, x, y = heapq.heappop(pq)# 0, 0, 0
            if visited[x][y]:
                continue
            if x == n-1 and y == n-1:  
                return elevation
            visited[x][y] = True
            for dx, dy in directions:
                X, Y = x + dx, y + dy
                if 0 <= X < n and 0 <= Y < n and not visited[X][Y]:
                    heapq.heappush(pq, (max(elevation, grid[X][Y]), X, Y)) # 1 1, 0   # max2 0 , 1 # 3, 1, 1
        
        return 0
    # NOT PATH
      # 0 2 1 1 1   output: 2
      # 1 3 4 5 1




class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        if n == m == 1:
            return grid[0][0]
        
        def get_nexts(i, j, visited):
            for x, y in ((i - 1, j),
                         (i + 1, j),
                         (i, j - 1),
                         (i, j + 1)):
                if (
                    0 <= x < n
                    and 0 <= y < m
                    and (x, y) not in visited
                ):
                    yield (x, y)

        def check(value):
            q = [(0, 0)]
            visited = {(0, 0)}
            while q:
                i, j = q.pop()
                for x, y in get_nexts(i, j, visited):
                    if grid[x][y] > value:
                        continue
                    if x == n - 1 and y == m - 1:
                        return True
                    q.append((x, y))
                    visited.add((x, y))
            return False
        
        left = max(grid[0][0], grid[-1][-1])
        right = max(max(line) for line in grid)

        if check(left):
            return left
        
        while right - left > 1:
            middle = (left + right) // 2
            if check(middle):
                right = middle
            else:
                left = middle
        
        return right
    


    class Solution:
        def swimInWater(self, grid: List[List[int]]) -> int:
            n = len(grid)
            directions = [(0,1), (0,-1), (1,0), (-1,0)]
            
            def canReach(x, y, t, visited):
                if x == n - 1 and y == n - 1:
                    return True
                visited[x][y] = True
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and grid[nx][ny] <= t:
                        if canReach(nx, ny, t, visited):
                            return True
                return False

            left, right = grid[0][0], n * n - 1
            while left < right:
                mid = (left + right) // 2
                visited = [[False] * n for _ in range(n)]
                if canReach(0, 0, mid, visited):
                    right = mid
                else:
                    left = mid + 1
            
            return left
        
        # Binary Search: O(log(maxElevation)) where maxElevation = n^2 - 1.
        # DFS: O(n^2) for each DFS attempt.
        # Overall: O(n^2 * log(n^2)), which is more efficient than the initial O(n^4) complexity