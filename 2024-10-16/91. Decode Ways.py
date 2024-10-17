from typing import List

# 91. Decode Ways

# You have intercepted a secret message encoded as a string of numbers. The message is decoded via the following mapping:

# "1" -> 'A'

# "2" -> 'B'

# ...

# "25" -> 'Y'

# "26" -> 'Z'

# However, while decoding the message, you realize that there are many different ways you can decode the message because some codes are contained in other codes ("2" and "5" vs "25").

# For example, "11106" can be decoded into:

# "AAJF" with the grouping (1, 1, 10, 6)
# "KJF" with the grouping (11, 10, 6)
# The grouping (1, 11, 06) is invalid because "06" is not a valid code (only "6" is valid).
# Note: there may be strings that are impossible to decode.

# Given a string s containing only digits, return the number of ways to decode it. If the entire string cannot be decoded in any valid way, return 0.

# The test cases are generated so that the answer fits in a 32-bit integer.

 

# Example 1:

# Input: s = "12"

# Output: 2

# Explanation:

# "12" could be decoded as "AB" (1 2) or "L" (12).

# Example 2:

# Input: s = "226"

# Output: 3

# Explanation:

# "226" could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).

# Example 3:

# Input: s = "06"

# Output: 0

# Explanation:

# "06" cannot be mapped to "F" because of the leading zero ("6" is different from "06"). In this case, the string is not a valid encoding, so return 0.

 

# Constraints:

# 1 <= s.length <= 100
# s contains only digits and may contain leading zero(s).

class Solution:
    def decode(self, s: str) -> int:
        # edge case: if first char is 0, return 0
        if s[0] == 0:
            return 0
        

        # dp
        # use 1 char or use 2 char
        # 


        # scan through the array, check if a char is a "1" or a "2"... both of these are valid individually or as a double digit number (assuming next char is between 0 ~ 6 for "2" or 0 ~ 9 for "1")
        # if a digit is greater than 2, increment the answer... this digit is a standalone
        # use i,j to process double digits


        # dp0 --> 2 step behind
        # dp1 --> 1 step behind
        # dp2 --> string up to current index

class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp0, dp1, dp2 = 0, 1, 0
        for i in range(1, n + 1):
            dp2 = 0
            if s[i - 1] != '0':
                dp2 += dp1
            if i > 1 and s[i - 2] != '0' and int(s[i - 2: i]) <= 26: # do not seperate the number direct checking the two numbers in the string
                dp2 += dp0
            dp0, dp1 = dp1, dp2
        return dp2
