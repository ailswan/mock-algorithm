from typing import List
#1033. Moving Stones Until Consecutive
# There are three stones in different positions on the X-axis. You are given three integers a, b, and c, the positions of the stones.

# In one move, you pick up a stone at an endpoint (i.e., either the lowest or highest position stone), and move it to an unoccupied position between those endpoints.

# Formally, let's say the stones are currently at positions x, y, and z with x < y < z.
# You pick up the stone at either position x or position z, and move that stone to an integer position k, with x < k < z and k != y.

# The game ends when you cannot make any more moves (i.e., the stones are in three consecutive positions).

# Return an integer array answer of length 2 where:

# answer[0] is the minimum number of moves you can play, and
# answer[1] is the maximum number of moves you can play.
# Example 1:

# Input: a = 1, b = 2, c = 5
# Output: [1,2]
# Explanation: Move the stone from 5 to 3, or move the stone from 5 to 4 to 3.
# Example 2:

# Input: a = 4, b = 3, c = 2
# Output: [0,0]
# Explanation: We cannot make any moves.
# Example 3:

# Input: a = 3, b = 5, c = 1
# Output: [1,2]
# Explanation: Move the stone from 1 to 4; or move the stone from 1 to 2 to 4.
 

# Constraints:

# 1 <= a, b, c <= 100
# a, b, and c have different values.

class Solution:
  def moveStones(self, a: int, b: int, c: int) -> List[int]:
    # goal -> find the minimum moves, also the maximum moves
    # figure out inputs in increasing order, so we can move a or c
    
    # 1 2 _ _ 5
    # check if there exists consecutive stones (a, b) or (b, c)
    # if so, move a or c next to b and store the minimum move for it is 1, maximum move is 5 -> 3 (2 )
    
    # 1 _ 3 _ 5
    # min moves (1), max (2)

    # 1 _ _ 4 _  _ 7
    # min moves (2), max (posB - posA + posC - posB)

    # 123
    # [0, 0]

    ans = [0, 0]

    # position the inputs on the line
    x, y, z = sorted([a,b,c])
    
    if x + 1 == y and y + 1 == z:
      return [0, 0]
    
    if x + 1 == y or y + 1 == z:
      ans[0] = 1
      ans[1] = max(y - x - 1, z - y - 1)
      return ans
    
    if x + 2 == y and y + 2 == z:
      return [1, 2]
    
    if x + 2 < y or y + 2 < z:
      ans[0] = 2
      ans[1] = y - x - 1 + z - y - 1
      return ans
  
  class Solution:
    def numMovesStones(self, a: int, b: int, c: int) -> List[int]:
        x, y, z = sorted([a, b, c])
        res = [2, z - x - 2]
        if ((z - y) == 1 and (y - x) == 1):
            res[0] = 0
        elif ((z - y) <= 2 or (y - x) <= 2):
            res[0] = 1
        return res    
#1040. Moving Stones Until Consecutive II