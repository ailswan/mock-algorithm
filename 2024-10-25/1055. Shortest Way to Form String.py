from typing import List
# 1055. Shortest Way to Form String

# A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

# Given two strings source and target, return the minimum number of subsequences of source such that their concatenation equals target. If the task is impossible, return -1.

 

# Example 1:

# Input: source = "abc", target = "abcbc"
# Output: 2
# Explanation: The target "abcbc" can be formed by "abc" and "bc", which are subsequences of source "abc".
# Example 2:

# Input: source = "abc", target = "acdbc"
# Output: -1
# Explanation: The target string cannot be constructed from the subsequences of source string due to the character "d" in target string.
# Example 3:

# Input: source = "xyz", target = "xz y xz"
# Output: 3
# Explanation: The target string can be constructed as follows "xz" + "y" + "xz".
 

# Constraints:

# 1 <= source.length, target.length <= 1000
# source and target consist of lowercase English letters.

class Solution:
    def shortestWayToFormString(self, source: str, target: str) -> int:
        # brute force => find all combination of subsequences and store in hashmap. Form the target string by checking if subsequences exist
        # 2 pointers, use left and right pointers to iterate through source and target...
        # backtracking

        # 1) target must be equal or longer than source
        # 2) make sure all characters in target exist in source
        # 3) convert the source input into a dictionary of <char, idx>


        # 1) Advance pointer as far as we can on the target input
        # 2) 


class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        res = i = 0
        while i < len(target):
            j = 0
            pre = i
            while i < len(target) and j < len(source):
                if target[i] == source[j]:
                    i += 1
                j += 1
            if pre == i:
                return -1
            res += 1
        return res