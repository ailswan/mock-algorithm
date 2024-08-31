from typing import List

# 79. Word Search

# Given an m x n grid of characters board and a string word, return true if word exists in the grid.

# The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.


# Example 1:

# | (A) | (B) | (C) | E |
# ----------------------
# |  S  |  F  | (C) | S |
# ----------------------
# |  A  | (D) | (E) | E |

# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
# Output: true

# Example 2:


# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
# Output: true

# Example 3:


# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
# Output: false
 

# Constraints:

# m == board.length
# n = board[i].length
# 1 <= m, n <= 6
# 1 <= word.length <= 15
# board and word consists of only lowercase and uppercase English letters.
 

# Follow up: Could you use search pruning to make your solution faster with a larger board?

class Solution:
    def wordSearch(self, board: List[List[str]], word: str) -> bool:
        # | (A) | (B) | (C) | E |
        # ----------------------
        # |  S  |  F  | (C) | S |
        # ----------------------
        # |  A  | (D) | (E) | E |

        # Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
        # DFS
        # visited = [[]]
        # isFind = False
        # interate the board :
        # if board[i][j] = word[k]:
        # four directions continue [ci][cj] !=  k + 1 if true:dfs else:return 
        # if k == len of word: return True
       


        m, n = len(board), len(board[0])
        visited = [[0] * n for _ in range(m) ] #1 = visited 0 = available
 
        #"ABCCED"
        # 012345
        # |  1   | 1   | 1| c|
        # ----------------------
        # |  S  |  F  | c | S |
        # ----------------------
        # |  A  | 1 .  | 1 | E |
        def dfs(visited, x, y, k): #   i = 2 j = 1 k = 6  
            if k == len(word):
                return True
            for dx, dy in [(1,0),(0,1),(-1,0),(0,-1)]:
                cx, cy = x + dx, y + dy
                if 0 <= cx < m and 0 <= cy < n and visited[cx][cy] == 0 and board[cx][cy] == word[k]:# cx = 2 cy = 1  D
                    visited[cx][cy] = 1
                    if dfs(visited, cx, cy, k + 1):
                        return True # 2 1 6
                    visited[cx][cy] = 0

        for i in range(m): #3
            for j in range(n): #4
                if word[0] == board[i][j]:# A   A
                    visited[i][j] = 1
                    if dfs(visited, i, j, 1): #   i = 0 j = 0 k = 1
                        return True
                    else:
                        visited[i][j] = 0
        return False
    # time complexity O(m * n * k)  m * n * 3 ^ k
    # space complexity O(m * n + k) k the length of word

                

