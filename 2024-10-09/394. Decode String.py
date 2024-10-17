from typing import List

# 394. Decode String


# Given an encoded string, return its decoded string.

# The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

# You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc. Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there will not be input like 3a or 2[4].

# The test cases are generated so that the length of the output will never exceed 105.

 

# Example 1:

# Input: s = "3[a]2[bc]"
# Output: "aaabcbc"
# Example 2:

# Input: s = "3[a2[c]]"
# Output: "accaccacc"
# Example 3:

# Input: s = "2[abc]3[cd]ef"
# Output: "abcabccdcdcdef"
 

# Constraints:

# 1 <= s.length <= 30
# s consists of lowercase English letters, digits, and square brackets '[]'.
# s is guaranteed to be a valid input.
# All the integers in s are in the range [1, 300].

class Solution:
    def decode(self, s: str) -> str:
        # 3[ac2[c]]
        # "accaccacc"
        # "",   3,"acc",   2,"c" 
        # 2   c   -> cc  3 acc -> accaccacc
        #"3[a]2[bc]"
        #"[b][a]"
        #"3[cd]ef"  #["cdcdcd", ef ]
        stack = [""]
        i = 0
        n = len(s)
        #   13 [a]
        #      i
        while i < n:# 9 < 9 
            if s[i].isdigit():#  2
                c_d = 0
                while i < n and s[i].isdigit():
                    c_d = c_d * 10 + int(s[i])
                    i += 1  # 5
                stack.append(c_d) #['', 3],['aaa',2 ]
            elif s[i].isalpha():# i = 5 b
                c_s = ""
                while i < n and s[i].isalpha():
                   c_s += s[i] #'bc'
                   i += 1 # i = 8
                stack.append(c_s)   #['',3, a, ]  ['aaa',2,'bc' ]
            elif s[i] == "]":
                c_s = stack.pop()#bc
                c_n = stack.pop()#2
                c_s = c_s * c_n#bcbc
                stack[-1] = stack[-1] + c_s#['aaabcbc']
                i += 1# i = 9
            else:
                i += 1
        res = ''
        for sr in stack:
            res += sr
        return res
    
#time complexity O(n)
#space complexity O(n/4) -> O(n)    
                

                
