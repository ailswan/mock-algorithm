from typing import List
# 38. Count and Say
#  The count-and-say sequence is a sequence of digit strings defined by the recursive formula:

# countAndSay(1) = "1"
# countAndSay(n) is the run-length encoding of countAndSay(n - 1).
# Run-length encoding (RLE) is a string compression method that works by replacing consecutive identical characters (repeated 2 or more times) 
# with the concatenation of the character and the number marking the count of the characters (length of the run).
# For example, to compress the string "33  222   5   1" we replace "33" with "23", replace "222" with "32", replace "5" with "15" and replace "1" with "11".
# Thus the compressed string becomes "23321511".

# Given a positive integer n, return the nth element of the count-and-say sequence.

# Example 1:

# Input: n = 4
# Output: "1211"
# Explanation:
# countAndSay(1) = "1"
# countAndSay(2) = RLE of "1" = "11"
# countAndSay(3) = RLE of "11" = "21"
# countAndSay(4) = RLE of "21" = "1211"

# Example 2:
# Input: n = 1
# Output: "1"
# Explanation:
# This is the base case.

# Constraints:
# 1 <= n <= 30
 
# Follow up: Could you solve it iteratively?


class Solution:
  def countAndSay(self, n: int) -> str:
    # always start with 1
    # loop from n -> -1
    # store the "state" of the previous iteration
    # iterate through the state string and count the number of the same digits to update the state for next iteration
    # countAndSay(1) = "1"                      i ---- n
    # countAndSay(2) = RLE of "1" = "11"        j ---- 0 -- len(crrString)-1
    # countAndSay(3) = RLE of "11" = "21"
    # countAndSay(4) = RLE of "21" = "1211"
    #             5                   111221
    #             6                   312211
    state = 1
    i = 0
    ptr = 0
    
    while i < n:          # 0       # 1
      digits = str(state)   # digits: "1"
      newState = []         
      j = 0   
      #"111221"                # j = 0
      while j < len(state):
        target = digits[j]      # target = 1
        count = 0
        while digits[j] == target and j < len(state):   # digits[0] = 1   target = 1
          count += 1                        # count = 1
          j += 1                            # j = 1
        newState.append(count, target)   # newState = [3,1]
      state = newState                   # state = [3,1,2,2,1,1]
      i += 1                            # 1
    return "".join(state)

# time complexity (N^2)
# space complexity (N)