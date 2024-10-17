from typing import List

# 73. Set Matrix Zeroes

# Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

# You must do it in place.

# Example 1:
# https://assets.leetcode.com/uploads/2020/08/17/mat1.jpg

# Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
# Output: [[1,0,1],[0,0,0],[1,0,1]]
# Example 2:

# https://assets.leetcode.com/uploads/2020/08/17/mat2.jpg
# Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
# Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
 

# Constraints:

# m == matrix.length
# n == matrix[0].length
# 1 <= m, n <= 200
# -231 <= matrix[i][j] <= 231 - 1
 

# Follow up:

# A straightforward solution using O(mn) space is probably a bad idea.
# A simple improvement uses O(m + n) space, but still not the best solution.
# Could you devise a constant space solution?

class Solution:
    def setZero(self, matrix: List[List[int]]) -> None:
        # we use the first row and first col as flags to later change all the values for the given row and column
        # iterate through the matrix, if we encounter a 0, set the first value in that row and first val in that col to 0
        # there is a special case for matrix[0][0]... we use a special is_col flag for it


        # Input: matrix = [
            # [0,1,2,0],
            # [3,4,5,2],
            # [1,3,1,5]]
        # Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
        is_col = False
        n = len(matrix)         # n = 3
        m = len(matrix[0])      # m = 4

        if matrix[0][0] == 0:
            is_col = True
        
        for i in range(n):
            for j in range(1, m):
                if matrix[i][j] == 0:                           # [0,0,0,0],
                    matrix[i][0] = 0                            # [3,4,5,2],
                    matrix[0][j] = 0                            # [1,3,1,5]]
        
        for i in range(1,n):
            if matrix[i][0] == 0:
                for j in range(1, m):
                    matrix[i][j] = 0

        for j in range(1, m):
            if matrix[0][j] == 0:
                for i in range(1, n):
                    matrix[i][j] = 0
        
        if matrix[0][0] == 0:
            for i in range(m):
                matrix[0][i] = 0

        if is_col:                          # is_col = True
            for i in range(n):
                matrix[i][0] = 0

# time => O(M * N) where M is max col and N is max row
# space => in place, O(1)