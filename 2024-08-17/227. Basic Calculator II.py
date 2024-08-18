from typing import List

# 227. Basic Calculator II

# Given a string s which represents an expression, evaluate this expression and return its value. 

# The integer division should truncate toward zero.

# You may assume that the given expression is always valid. All intermediate results will be in the range of [-231, 231 - 1].

# Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

 

# Example 1:

# Input: s = "3+2*2"
# Output: 7
# Example 2:

# Input: s = " 3/2 "
# Output: 1
# Example 3:

# Input: s = " 3+5 / 2 "
# Output: 5
 

# Constraints:

# 1 <= s.length <= 3 * 10^5
# s consists of integers and operators ('+', '-', '*', '/') separated by some number of spaces.
# s represents a valid expression.
# All the integers in the expression are non-negative integers in the range [0, 231 - 1].
# The answer is guaranteed to fit in a 32-bit integer.

class Solution:
    def calculator(self, s: str) -> int:
        #"2*3 + 2*2"
        # stack track the number
        # iterate the s
        # if  '*' or '/': stack.pop() = 2 * cur     cur = 3  stack.append(6)
        # if  '+': stack.append('+')
        # if  digit : stack.append(2)
        # reach the end of s  stack[6, + , 4]
        # iterate the stack 6 + 4
        stack = [] # storing integers only
        cur_op = ""              # "(24 * 37) - (243 * 25 * 2)"
        isPositive = 1
        cur_num = 0
        n = len(s) 
        i = 0
        while i  < n:  # 0 1 2 3 4 5 6    7 
            if s[i].isdigit():
                while s[i].isdigit(): # 25    #isPositive = -1
                    cur_num = cur_num * 10 + int(s[i])			# cur_num = 37
                    i += 1    
                if cur_op == "*": #cur = 25 stack[888,  25 * -243]
                    stack.append(cur_num * stack.pop())#  stack =[888]   cur_num = 37
                    cur_op = ""
                    cur_num = 0 
                elif cur_op == "/":
                    stack.append(stack.pop() // cur_num)
                    cur_op = ""
                    cur_num = 0 
                else:
                    stack.append(isPositive * cur_num) # stack =[6, "+", 2]
                    isPositive = 1    
            if s[i] == "*" or s[i] == "/":
                cur_op = s[i] # cur_op = "*"
            if s[i] == "+":
                isPositive = 1
            if s[i] == "-":
                isPositive = -1
            i += 1

        #stack =[6, "+", 4]
        res = sum(stack)
		# iterate through stack, perform + or -
        return res
    
    #time complexity O(n)
    #space complexity O(n)
        
            
        


