from typing import List

# 348. Design Tic-Tac-Toe

# Assume the following rules are for the tic-tac-toe game on an n x n board between two players:

# A move is guaranteed to be valid and is placed on an empty block.
# Once a winning condition is reached, no more moves are allowed.
# A player who succeeds in placing n of their marks in a horizontal, vertical, or diagonal row wins the game.
# Implement the TicTacToe class:

# TicTacToe(int n) Initializes the object the size of the board n.
# int move(int row, int col, int player) Indicates that the player with id player plays at the cell (row, col) of the board.
# The move is guaranteed to be a valid move, and the two players alternate in making moves. Return
# 0 if there is no winner after the move,
# 1 if player 1 is the winner after the move, or
# 2 if player 2 is the winner after the move.
 

# Example 1:

# Input
# ["TicTacToe", "move", "move", "move", "move", "move", "move", "move"]
# [[3], [0, 0, 1], [0, 2, 2], [2, 2, 1], [1, 1, 2], [2, 0, 1], [1, 0, 2], [2, 1, 1]]
# Output
# [null, 0, 0, 0, 0, 0, 0, 1]

# Explanation
# TicTacToe ticTacToe = new TicTacToe(3);
# Assume that player 1 is "X" and player 2 is "O" in the board.
# ticTacToe.move(0, 0, 1); // return 0 (no one wins)
# |X| | |
# | | | |    // Player 1 makes a move at (0, 0).
# | | | |

# ticTacToe.move(0, 2, 2); // return 0 (no one wins)
# |X| |O|
# | | | |    // Player 2 makes a move at (0, 2).
# | | | |

# ticTacToe.move(2, 2, 1); // return 0 (no one wins)
# |X| |O|
# | | | |    // Player 1 makes a move at (2, 2).
# | | |X|

# ticTacToe.move(1, 1, 2); // return 0 (no one wins)
# |X| |O|
# | |O| |    // Player 2 makes a move at (1, 1).
# | | |X|

# ticTacToe.move(2, 0, 1); // return 0 (no one wins)
# |X| |O|
# | |O| |    // Player 1 makes a move at (2, 0).
# |X| |X|

# ticTacToe.move(1, 0, 2); // return 0 (no one wins)
# |X| |O|
# |O|O| |    // Player 2 makes a move at (1, 0).
# |X| |X|

# ticTacToe.move(2, 1, 1); // return 1 (player 1 wins)
# |X| |O|
# |O|O| |    // Player 1 makes a move at (2, 1).
# |X|X|X|
 

# Constraints:

# 2 <= n <= 100
# player is 1 or 2.
# 0 <= row, col < n
# (row, col) are unique for each different call to move.
# At most n2 calls will be made to move.
 

# Follow-up: Could you do better than O(n2) per move() operation?

# [[3], [0, 0, 1], [0, 2, 2], [2, 2, 1], [1, 1, 2], [2, 0, 1], [1, 0, 2], [2, 1, 1]]


class TicTacToe:
    def __init__(self, n: int) -> None:
        self.n = n
        self.board = [[0] * n for _ in range(n)]
    def move(row: int, col: int, player: int) -> int:
        # Return 0 if there is no winner after the move, 1 if player 1 is the winner after the move, or 2 if player 2 is the winner after the move.
        if self.isWinner(row, col, player):
            return player
        else:
            self.board[row][col] = player

    def isWinner(self, r, c, p) -> bool:
        # when a player makes a move, check if the row OR col OR diagonal are the same value as the player
         # -1   1 1 1 1       
         # -1
         # -1   1 1 1 1
         # -1  0 1 1 1
         # -1
         # grid[i][j]  i == j
         # n - 1 - j = i

        if sum(self.board[r]) == self.n * p and all(self.board[r] != 0):
            return True
        colTotal = 0
        for i in range(self.n):
            colTotal += self.board[r][i]
        if colTotal == self.n * p:
            return True

        if r == c or self.n - r - 1 == c:
                if self.isDiagWin(p):
                    return True
        return False
    
    #  1  0  1
    #  1  1  0
    #  1  0  0
    def isDiagWin(self, p) -> bool:
        isLeftWin = True
        isRightWin = True
        for i in range(self.n):
            if self.board[i][i] != p:
                isLeftWin = False

        for i in range(self.n - 1, -1, -1):
            if self.board[self.n - i - 1][i] != p:
                isRightWin = False
        return isLeftWin or isRightWin

# time => O(N * N)
# space => O(N * N)


class TicTacToe:

    def __init__(self, n: int):
        self.rows = [0] * n
        self.cols = [0] * n
        self.diagonal = 0
        self.anti_diagonal = 0

    def move(self, row: int, col: int, player: int) -> int:
        current_player = 1 if player == 1 else -1
        self.rows[row] += current_player
        self.cols[col] += current_player
        if row == col:
            self.diagonal += current_player
        
        if col == len(self.cols) - row - 1:
            self.anti_diagonal += current_player

# sum(row) == len -> player1    player2 sum(row) == len*2  no 0
        n = len(self.rows)
        if(
            abs(self.rows[row]) == n
            or abs(self.cols[col]) == n
            or abs(self.diagonal) == n
            or abs(self.anti_diagonal) == n
        ):
            return player
        return 0

