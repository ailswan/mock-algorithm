from typing import List

# 498. Diagonal Traverse

# Given an m x n matrix mat, return an array of all the elements of the array in a diagonal order.

 

# Example 1:

# https://assets.leetcode.com/uploads/2021/04/10/diag1-grid.jpg

# Input: mat = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,4,7,5,3,6,8,9]
# Example 2:

# Input: mat = [[1,2],[3,4]]
# Output: [1,2,3,4]

class Solution:
    def diagonalTraverse(self, mat: List[List[int]]) -> List[int]:
        # [i][j]   [i - 1][j + 1] up
        #          [i + 1][j - 1] down
        #  0  1  2  3 4  index
        #  1  2  3 / /  n + m - 1   if index is even: up      odd: down
        #        6  /
        #     8  9 
        # traverse as down . check if up: reverse the level traverse temp[]
        m, n = len(mat), len(mat[0]) # 3 , 3
        res = []
        for k in range(m + n): # k = 4 0 ~ 5
            temp = []
            #[0][j]  -> [i + 1][j - 1]
            j = k # j = 4
            for i in range(m): # i = 2  0 ~ 2 j = 2
                if j >= 0 and j < n:
                    temp.append(mat[i][j])#[9]
                j -= 1
            if k % 2 == 0:
                temp.reverse()#[9]
            res += temp #[1, 2, 4, 7, 5, 3, 6, 8, 9]
        return res
    # time complexity O((m + n) * m)
    # space complexity O(m + n)

            

