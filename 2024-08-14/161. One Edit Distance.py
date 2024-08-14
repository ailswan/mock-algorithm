from typing import List

 #161. One Edit Distance
#  Given two strings s and t, return true if they are both one edit distance apart, otherwise return false.

# A string s is said to be one distance apart from a string t if you can:

# Insert exactly one character into s to get t.
# Delete exactly one character from s to get t.
# Replace exactly one character of s with a different character to get t.
 

# Example 1:

# Input: s = "ab", t = "acb"
# Output: true
# Explanation: We can insert 'c' into s to get t.
# Example 2:

# Input: s = "", t = ""
# Output: false
# Explanation: We cannot get t from s by only one step.
 

# Constraints:

# 0 <= s.length, t.length <= 104
# s and t consist of lowercase letters, uppercase letters, and digits.

class Solution:
  def oneEditDistance(self, s:str, t:str) -> bool:
    # 3 scenarios => add, delete, replace
    # add/delete => check the length of s and t
    # replace => every character in s has to be the same as every character in t.... EXCEPT 1
    # can use a hashmap to keep count of character in s.... when we interate through t, we decrement s_char_frequency

                 #"a"      "a"
                 #"a"      "A"
    # Input: s = "ab", t = "acb"
    # output: True
    n = len(s)      # n = 2
    m = len(t)      # m = 3

    if s == t:
      return False

    if abs(n - m) > 1:  # abs(2 - 3) = 1 > 1? False
      return False

    char_count = {}

    for c in s:
      char_count[c] = char_count.get(c, 0) + 1  # { a: 1, b: 1 }
    
    for char_t in t:                    # t = "a c b"
      if char_t in char_count:                # { a: 0, c: 1, b: 0 }
        char_count[char_t] -= 1
      else:
        char_count[char_t] = char_count.get(char_t, 0) + 1
    #char_count = 0 + 1 + 0 => 1

    #char_count = {a: 1, A: 1}
  
    # "abb"   "Abb" --> should return True

    if n == m:
      return sum(char_count.values()) == 2
  
    return sum(char_count.values()) == 1 

# time => (n + m)
# space => (n + m)