from typing import List

# 48. Rotate Image

# You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

# You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

# Example 1:

        # 1  2  3             7  4  1
        # 4  5  6             8  5  2
        # 7  8  9             9  6  3


# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [[7,4,1],[8,5,2],[9,6,3]]

# Example 2:


# Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
# Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
 

# Constraints:

# n == matrix.length == matrix[i].length
# 1 <= n <= 20
# -1000 <= matrix[i][j] <= 1000

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:  
        # 1  2  3             7  4  1
        # 4  5  6             8  5  2
        # 7  8  9             9  6  3

        # 7  8  9             7  4  1
        # 4  5  6             8  5  2
        # 1  2  3             9  6  3
        #swap up with down  horizontal - axis   matrix[i][j], matrix[i][n - j]
        #swap right-up with left-bottom   leftup - rightdown diagonal- axis matrix[i][j], matrix[j][i]
        n = len(matrix) #n 3
        for i in range(n // 2): # i = 0  range(1)
            for j in range(n): # j= 1 range(3)
                matrix[i][j], matrix[n - i - 1][j] = matrix[n - i - 1][j], matrix[i][j] # [0][2], [2][2] 3 , 9
        for i in range(1, n):# i = 2  range(1, 3)  1  2
            for j in range(i):# j= 0  range(2) 0 1 
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j] #[2][1] [1][2]  4, 8   1 , 9  2, 6
        # time complexity O(n*n)
        # space complexity O(1)
        
        # 1  2  3         n*n/2     
        # 4  5  6  


        # 7             n*(n-1)/2
        # 4  5  
        # 1  2  3            

