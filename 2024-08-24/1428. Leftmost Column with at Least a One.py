from typing import List
# 1428. Leftmost Column with at Least a One
#  A row-sorted binary matrix means that all elements are 0 or 1 and each row of the matrix is sorted in non-decreasing order.

# Given a row-sorted binary matrix binaryMatrix, return the index (0-indexed) of the leftmost column with a 1 in it. If such an index does not exist, return -1.

# You can't access the Binary Matrix directly. You may only access the matrix using a BinaryMatrix interface:

# BinaryMatrix.get(row, col) returns the element of the matrix at index (row, col) (0-indexed).
# BinaryMatrix.dimensions() returns the dimensions of the matrix as a list of 2 elements [rows, cols], which means the matrix is rows x cols.
# Submissions making more than 1000 calls to BinaryMatrix.get will be judged Wrong Answer. Also, any solutions that attempt to circumvent the judge will result in disqualification.

# For custom testing purposes, the input will be the entire binary matrix mat. You will not have access to the binary matrix directly.

 

# Example 1:
# 0 0
# 1 1

# Input: mat = [[0,0],[1,1]]
# Output: 0
# Example 2:
# 0 0
# 0 1

# Input: mat = [[0,0],[0,1]]
# Output: 1
# Example 3:

# 0 0 
# 0 0 
# Input: mat = [[0,0],[0,0]]
# Output: -1
 

# Constraints:

# rows == mat.length
# cols == mat[i].length
# 1 <= rows, cols <= 100
# mat[i][j] is either 0 or 1.
# mat[i] is sorted in non-decreasing order.


#class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
      # get the dimensions
      # check the very last row, if there are no 1's then return -1
      # binary search the last row for the leftmost col index, set that as an anchor
      # we know that the rows are ascending order, can binary search through the row (looking at col index 0) for the target

      [
    #  \   all 1's
         \
          \
       0's \

      ]
      r, c = binaryMatrix.dimensions()
      ans = -1
      leftMost_c = float("inf")

      for i in range(c):
        if binaryMatrix.get(r - 1, i) == 1:
          leftMost_c = i
          break

      # 00111
      # 00011
      # 01111
      # check every row up to the index of the leftMost_c found so far, update leftMost_c and break if we encounter a 1

      left = 0
      right = r - 1
      while left < right:
        mid = left + (right - left) // 2
        if binaryMatrix.get(mid, leftMost_c) == 0:
          left = mid + 1
        elif binaryMatrix.get(mid, leftMost_c) == 1:
          right = mid
      
      leftMost_c = mid
      return leftMost_c if leftMost_c != float("inf") else ans   
