from typing import List
# 28. Find the Index of the First Occurrence in a String
# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack. 

# Example 1:

# Input: haystack = "sadbutsad", needle = "sad"
# Output: 0
# Explanation: "sad" occurs at index 0 and 6.
# The first occurrence is at index 0, so we return 0.
# Example 2:

# Input: haystack = "leetcode", needle = "leeto"
# Output: -1
# Explanation: "leeto" did not occur in "leetcode", so we return -1.
 

# Constraints:

# 1 <= haystack.length, needle.length <= 10^4
# haystack and needle consist of only lowercase English characters.

class Solution:
    def findIndex(self, needle: str, haystack: str) -> int:
        ans = -1 
        if len(needle) > len(haystack):
            return ans
        
        # iterate through haystack, check if the letters in needle are in haystack
        
        for i in range(len(haystack)):
            j = 0
            k = i
            while k < len(haystack) and needle[j] == haystack[k] and j < len(needle):
                j += 1
                k += 1
            if j == len(needle):
                return i

        return -1

