from typing import List

# 9. Palindrome Number

# Given an integer x, return true if x is a 
# palindrome, and false otherwise.

 

# Example 1:

# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.

# Example 2:

# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

# Example 3:

# Input: x = 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
 

# Constraints:
# -2^31 <= x <= 2^31 - 1
 

# Follow up: Could you solve it without converting the integer to a string?

class Solution:
    def isPalindrome(self, x: int) -> bool: #input: 0
        # x = -121  x= 121
        # is negative: false
        #x -> list [1, 2, 1]
        # compare l, r
        if x < 0:
            return False
        if x == 0:
            return True
        x_list = []
        while x:#2
            x, remainder = divmod(x, 10) #0, 1
            x_list.append(remainder) #[1, 2, 1] x = 0
        l, r = 0, len(x_list) - 1 # 0 2
        while l < r:#1, 1
            if x_list[l] != x_list[r]:#1 != 1?
                return False
            l += 1
            r -= 1
        return True
    
#time complexity O(n)
#space complexity O(n)
# x= 123321

# cur= 0    
        cur_i = 0 
        while x >= 10:#x = 12321
            x = x // 10 # x = 1232
            cur_i += 1 # cur_i = 2
        #cur_i = 4  
        y = x #12321
        while y >= 10:#y = 0
            c = y // pow(10, cur_i) # 3
            y, r = divmod(y, 10) # 3 , 3
            if r != c: # 3 != 3 
                return False
            cur_i -= 1 # 0
            y -= c * pow(10, cur_i) #3 - 3 = 0
            cur_i -= 1 # -1
        return True
# time complexity O(n)
# space complexity O(1)

        
# input: 12321 --->
# x => 123
# revertedNumber => 12
        revertedNumber = 0
        while x > revertedNumber:#12321
            revertedNumber = revertedNumber * 10 + x % 10 #0 + 1
            x //= 10

