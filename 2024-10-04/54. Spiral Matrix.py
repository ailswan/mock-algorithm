from typing import List

# 54. Spiral Matrix

# Given an m x n matrix, return all elements of the matrix in spiral order.

 

# Example 1:
# https://assets.leetcode.com/uploads/2020/11/13/spiral1.jpg

# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,3,6,9,8,7,4,5]
# Example 2:
# https://assets.leetcode.com/uploads/2020/11/13/spiral.jpg


# Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]
 

# Constraints:

# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 10
# -100 <= matrix[i][j] <= 100

class Solution:
    def spiralMatrix(self, matrix: List[List[int]]) -> List[int]:
        #[[1,2,3,4],[5,6,7,8],[9,10,11,12]]
        m, n = len(matrix), len(matrix[0]) #3 , 4 
        l, r, t, b = 0, n - 1, 0, m - 1 # 0, 3, 0, 2
        res = []
        i, j = 0, 0
        while True:# l = 1, r = 2, t = 1, b = 1 j = 1 i= 1
            while j <= r:# 1 <= 2
                res.append(matrix[i][j])#[1,2,3,4]  [1, 2,3,4, 8, 12, 11, 10, 9, 5, 6, 7]
                j += 1 # 3
            j -= 1# j = 2
            i += 1 # i = 2
            t += 1 # t = 2
            if i > b:# 2 > 1
                break
            while i <= b:# 1 <= 2
                res.append(matrix[i][j]) #[1][3]  [1, 2,3,4, 8, 12]
                i += 1# i = 3
            i -= 1# i = 2
            j -= 1# 2
            r -= 1# 2
            if j < l:
                break
            while j >= l:# 2 >= 0
                res.append(matrix[i][j])#[1, 2,3,4, 8, 12, 11, 10, 9 ]
                j -= 1# -1
            j += 1# 0
            b -= 1 # 1
            i -= 1 # 1
            if i < t:
                break
            while i >= t:# 2 >= 1
                res.append(matrix[i][j])#[1, 2,3,4, 8, 12, 11, 10, 9, 5 ]
                i -= 1  # i = 0
            i += 1 # i = 1
            j += 1 #j =  1
            l += 1 #l = 1
            if j > r: #1 > 2?
                break
        return res


            