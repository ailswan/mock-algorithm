from typing import List

# 221. Maximal Square
# Given an m x n binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.


# https://assets.leetcode.com/uploads/2020/11/26/max1grid.jpg
# input:matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
# output:4

# input:matrix = [["0","1"],["1","0"]]
# output:1

# input:matrix = [["0"]]

# output:0


# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 300
# matrix[i][j] is 0 or 1

class Solution:
    def findLargestSquare(self, matrix: List[List[int]]) -> int:
        # goal => find area of largest SQUARE
        # an individual cell of 1 is considered a square of area 1
        # edge case => the matrix has all 0's.... return 0
        # for each cell, look at the neighbors (4 directions of travel)
            # we expand the row and col for a given cell simultaneously
        # update the largest_area once we find a square


        # input:matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
        # output:4   0
      

        m = len(matrix)     # 4
        n = len(matrix[0])  # 5
        ans = 0

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 1:
                    # check for area of square
                    ans = max(ans, self.findArea(matrix, i, j, m, n))               # self.findArea(matrix, 1, 2, 4, 5)
        return ans
    
    def findArea(self, grid, row, col, max_row, max_col):
        # directions = [(1,0), (0,1), (0,-1), (-1,0)]
        area = 1
        anchor_r = row                  # anchor_r = 1
        anchor_c = col                  # anchor_c = 2
        
        while row < max_row and col < max_col:          # 1 < 4, 2 < 5
            row += 1                                    # row = 2
            col += 1                                    # col = 3
            # check only the new row and the new col
            for i in range(anchor_r, row):              # i -> 1 ~ 2
                if grid[i][col] == 0:                   # grid[1][2] == 0? True
                    return area
            for j in range(anchor_c, col):              # j -> 2 ~ 3
                if grid[row][j] == 0:                   # grid[2][2] == 0? True
                    return area
            area = max(area, row * col)                 # area = max(0, 1) -> 1
        return area
    

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix:return 0
        if len(matrix)==1:return int("1" in matrix[0])
        row,col=len(matrix),len(matrix[0])
        viewed=[[False]*col for _ in range(row)]
        ans=0
        def dfs(matrix:List[List[str]],row:int,col:int)->int:
            viewed[row][col]=True
            if matrix[row][col]=="0":return 0
            ans=1
            itr=1
            while (row+itr<len(matrix)) and (col+itr<len(matrix[0])):
                if helper(matrix,row,col,itr+1):
                    ans+=1
                    itr+=1
                else:break
            return ans**2
            
        def helper(matrix:List[List[str]],row:int,col:int,curr:int)->bool:
            if row+curr>len(matrix):return False
            
            target=True
            for i in range(curr):
                if matrix[row+curr-1][col+i]=="0":
                    target=False
                    break
                if matrix[row+i][col+curr-1]=="0":
                    target=False
                    break
            if target:
                for i in range(curr):
                    viewed[row][i]=True
                    viewed[i][col]=True
            return target
        
        for i in range(row):
            for j in range(col):
                #print([i,j])
                #print(ans)
                if viewed[i][j]:
                    continue
                ans=max(ans,dfs(matrix,i,j))
        #print(dfs(matrix,2,1))
        return ans

               #  2  2  2  0
               #  2  2  2  2
               #  2  2  2  1
               # min(2, 1, 3) + 1
        
# m n 
# dp[i][j] = min dp[i-1][j-1],dp[i-1][j],dp[i][j-1] + 1 if matrix[i][j] == 1 else 0
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        if m == 0:
            return 0
        n = len(matrix[0])
        if n == 0:
            return 0
        res = 0
        dp1 = [0] * (n + 1)
        dp2 = [0] * (n + 1)
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if matrix[i - 1][j - 1] == "1":
                    dp2[j] = min(dp1[j - 1], dp1[j], dp2[j - 1]) + 1
                    res = max(res, dp2[j])
                else:
                    dp2[j] = 0
            dp1 = dp2[:]
        return res * res        
        

        
        
        