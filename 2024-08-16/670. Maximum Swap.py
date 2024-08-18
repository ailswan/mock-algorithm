from typing import List

# 670. Maximum Swap
# You are given an integer num. You can swap two digits at most once to get the maximum valued number.

# Return the maximum valued number you can get.
# Example 1:

# Input: num = 2736     7632
# Output: 7236
# Explanation: Swap the number 2 and the number 7.
# Example 2:

# Input: num = 9973
# Output: 9973
# Explanation: No swap.
 

# Constraints:

# 0 <= num <= 10^8

class Solution:
  def maxSwap(self, num: int) -> int:
    # scan through the number, look for the largest digit
    # keep track of the index and the largest digit       # 2 7 3 6
    #                                                         ^
    # scan from the first digit until the largest digit:
      # if the num[i] is smaller than largest digit, swap the digits
    # keep a left pointer where it skips all the largest digits
    # 9 9         7 3
    # 7 7 2 3   7 7 3 2       87 56 23      76532     98 45 23 7       98 75 23 4
    digits = list(str(num))
    largest_digit = max(num)
    largest_digit_index = 0
    largest_so_far = 0
    # scan through the digits
    # if the digits are monotonically decreasing, continune
    # elif

    for i in range(1, len(digits)):
      if digits[i] <= digits[i - 1]:
        continue
      else:
        largest_so_far = max(digits[i], largest_so_far)
    
    for i in range(len(digits)):
      if digits[i] >= largest_so_far:
        continue
      else:
        digits[i], largest_so_far = largest_so_far, digits[i]
        break
    return int("".join(digits))
        
        


    