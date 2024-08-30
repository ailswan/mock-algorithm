from typing import List

# 13. Roman to Integer

# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

# Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

# I can be placed before V (5) and X (10) to make 4 and 9. 
# X can be placed before L (50) and C (100) to make 40 and 90. 
# C can be placed before D (500) and M (1000) to make 400 and 900.
# Given a roman numeral, convert it to an integer.

 

# Example 1:

# Input: s = "III"
# Output: 3
# Explanation: III = 3.
# Example 2:

# Input: s = "LVIII"
# Output: 58
# Explanation: L = 50, V= 5, III = 3.
# Example 3:

# Input: s = "MCMXCIV"
# Output: 1994
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
 

# Constraints:

# 1 <= s.length <= 15000000000000
# s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
# It is guaranteed that s is a valid roman numeral in the range [1, 3999].

class Solution:
    def Roman2Integer(self, s: str) -> int:
        r2i = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        # c -> int 
        # Input: s = "MCMXCIV"
        # Output: 1994
        # Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
        # C=100 M = 1000 if s[i] < s[i + 1]  r2i[s[i + 1]] M - r2i[s[i]] c
        # else  res += r2i[s[i]]
        #"III"
        # 111
        # 012
        #"MCMXCIV"
        # 0123456
        n = len(s)# 7
        if n == 0:
            return 0
        res = r2i[s[n - 1]] # 5
        for i in range(n - 2, -1, -1):# 5 - 0  0      max loop => 9 or so times
            if r2i[s[i]] < r2i[s[i + 1]]:# 1000 < 100
                res -= r2i[s[i]] #   1094-100 = 994
            else:
                res += r2i[s[i]]# 1994
        return res# 3
    #time complexity O(n) n is the length of the s
    #space complexity O(1) 






