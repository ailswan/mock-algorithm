from typing import List

# 796. Rotate String

# Given two strings s and goal, return true if and only if s can become goal after some number of shifts on s.

# A shift on s consists of moving the leftmost character of s to the rightmost position.

# For example, if s = "abcde", then it will be "bcdea" after one shift.


# Example 1:

# Input: s = "abcde", goal = "cdeab"
# Output: true
# Example 2:

# Input: s = "abcde", goal = "abced"
# Output: false
 

# Constraints:

# 1 <= s.length, goal.length <= 100
# s and goal consist of lowercase English letters.
from collections import Counter
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        #"abcdea" s = "abcde", goal = 
        #              i 
        #"cde a ab"   "abced"
        #       j          s
        # if char not in s : false
        # if len != : false
        # i = 0 in s   j keep moving  when i -> end : True . else j -> end : False
        if len(s) != len(goal):
            return False
        if Counter(s) - Counter(goal) != {}:
            return False
        i, j, start = 0, 0, 0
        m, n = len(s), len(goal) # 5 5
        while start < n: #start = 5  < 5
            if s[i] != goal[start]:# a != d
                start += 1
                continue
            j = start # j = 0
            while i < m: #3 < 5 j = 3
                j = j % n
                if s[i] == goal[j]:# d == e ?
                    i += 1
                    j += 1
                else:
                    i = 0 # i = 0 
                    start += 1
                    break
            if i == m:
                return True
        return False

            
solution = Solution()
s = "abcde"
goal = "abced"
print(solution.rotateString(s, goal))


            

class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        length = len(s)

        # Try all possible rotations of the string
        for _ in range(length):
            # Perform one rotation
            s = s[1:] + s[0]
            if s == goal:
                return True
        return False
        
