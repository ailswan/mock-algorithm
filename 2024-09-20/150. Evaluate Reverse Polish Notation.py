from typing import List


# 150. Evaluate Reverse Polish Notation

# You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

# Evaluate the expression. Return an integer that represents the value of the expression.

# Note that:

# The valid operators are '+', '-', '*', and '/'.
# Each operand may be an integer or another expression.
# The division between two integers always truncates toward zero.
# There will not be any division by zero.
# The input represents a valid arithmetic expression in a reverse polish notation.
# The answer and all the intermediate calculations can be represented in a 32-bit integer.
 

# Example 1:

# Input: tokens = ["2","1","+","3","*"]
# Output: 9
# Explanation: ((2 + 1) * 3) = 9
# Example 2:

# Input: tokens = ["4","13","5","/","+"]
# Output: 6
# Explanation: (4 + (13 / 5)) = 6
# Example 3:

# Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
# Output: 22
# Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
# = ((10 * (6 / (12 * -11))) + 17) + 5
# = ((10 * (6 / -132)) + 17) + 5
# = ((10 * 0) + 17) + 5
# = (0 + 17) + 5
# = 17 + 5
# = 22
 

# Constraints:

# 1 <= tokens.length <= 104
# tokens[i] is either an operator: "+", "-", "*", or "/", or an integer in the range [-200, 200].
import math
class Solution:
    def polishNotation(self, tokens: List[str]) -> int:
        # stack to append numbers
        # when is operation , pop numbers and append result back
        # operation_map ={
        #     "+": math.add()
        #     "-": 
        #     "*": 
        #     "/":                    
        #     }
        #["4","13","5","/","+"]
        stack = []
        n = len(tokens) # 5
        for i in range(n):
            if tokens[i] not in {"+","-","*","/"}:          # if tokens[i] not in "+-/*":
                stack.append(int(tokens[i])) #[4, 13, 5]
            else:
                second = stack.pop() # 2
                first = stack.pop() # 4 
                if tokens[i] == "+":
                    stack.append(first + second) # [6]
                elif tokens[i] == "-":
                    stack.append(first - second)
                elif tokens[i] == "*":
                    stack.append(first * second)
                else:
                    stack.append(first // second) # 13 // 5 = 2  [4, 2]
        return stack[0] #6
# time complexity O(n)
# space complexity O(n/2) ~ O(n)   total number of numbers almost equal time operations [1 , 2, 3, 4,5,6 7]   


            
import re

def is_number(s):
    pattern = r'^-?\d+(?:\.\d+)?$'
    return bool(re.match(pattern, s))

def is_number(s):
    try:
        float(s)  # Or int(s) for checking integers only
        return True
    except ValueError:
        return False