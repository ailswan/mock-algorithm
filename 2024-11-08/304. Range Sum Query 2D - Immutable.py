from typing import List

# 304. Range Sum Query 2D - Immutable

# Given a 2D matrix matrix, handle multiple queries of the following type:

# Calculate the sum of the elements of matrix inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).
# Implement the NumMatrix class:

# NumMatrix(int[][] matrix) Initializes the object with the integer matrix matrix.
# int sumRegion(int row1, int col1, int row2, int col2) Returns the sum of the elements of matrix inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).
# You must design an algorithm where sumRegion works on O(1) time complexity.

 

# Example 1:

# https://assets.leetcode.com/uploads/2021/03/14/sum-grid.jpg

# Input
# ["NumMatrix", "sumRegion", "sumRegion", "sumRegion"]
# [[[[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]], [2, 1, 4, 3], [1, 1, 2, 2], [1, 2, 2, 4]]
# Output
# [null, 8, 11, 12]

# Explanation
# NumMatrix numMatrix = new NumMatrix([[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]);
# numMatrix.sumRegion(2, 1, 4, 3); // return 8 (i.e sum of the red rectangle)
# numMatrix.sumRegion(1, 1, 2, 2); // return 11 (i.e sum of the green rectangle)
# numMatrix.sumRegion(1, 2, 2, 4); // return 12 (i.e sum of the blue rectangle)
 

# Constraints:

# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 200
# -104 <= matrix[i][j] <= 104
# 0 <= row1 <= row2 < m
# 0 <= col1 <= col2 < n
# At most 104 calls will be made to sumRegion.


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
       
        m, n = len(matrix), len(matrix[0])
        self.area = [[0] * n for _ in range(m)]
 
        self.area[0][0] = matrix[0][0]
        for i in range(1, n):
            self.area[0][i] = matrix[0][i] + self.area[0][i - 1]
 
        for i in range(1, m):
            self.area[i][0] = matrix[i][0] + self.area[i - 1][0]
 
        for i in range(1, m):
            for j in range(1,n):
                self.area[i][j] = self.area[i - 1][j]  + self.area[i][j - 1] - self.area[i - 1][j - 1] + matrix[i][j]
 
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # o(1)
        # area[row2][col2] - area[row1 - 1][col2] - area[row2][col1 - 1] + area[row1 - 1][col1 - 1]
        # res = 0

        res = self.area[row2][col2] - self.area[row1 - 1][col2] - self.area[row2][col1 - 1] + self.area[row1 - 1][col1 - 1]
        #                                                     
        return res
    
        
numm = NumMatrix([[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]])
print(numm.sumRegion(2, 1, 4, 3))

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)