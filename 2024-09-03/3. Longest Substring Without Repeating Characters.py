from typing import List

# 3. Longest Substring Without Repeating Characters

# Given a string s, find the length of the longest 
# substring
#  without repeating characters.

 

# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2:

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:

# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

# Constraints:

# 0 <= s.length <= 5 * 10^4
# s consists of English letters, digits, symbols and spaces.
import collections
class Solution:
    def longestSub(self, s: str) -> int:
        # Input: s = "abcabcbb"
        # Output: 3
        #visited = {a: 1, b: 1, c: 2}
        #"a b c a b c b b"
        # 0 1 2 3 4 5 6 7
        #         i
        # s[i] in visited: update the max res i - visited[s[i]]   
        #       update the visited[s[i]] = i
        # move i 
        # Input: s = "p w w p k e w"
        #             0 1 2 3 4 5 6
        #             s i
        # Output: 4
        # corner case if s = ""
        # s= "p"
        # s = "au"
        # s = "aab", output: 2
        res = 0
        i, n = 0, len(s)  #i = 0 3
        visited = collections.defaultdict(int)#{}
        start = 0
        if n == 1:
            return 1
        while i < n: #i = 0 < 3
            if s[i] in visited and start <= visited[s[i]]: # w  {p: 3, w: 2, k:4, e: 5,} #i = 2 {a: 1}
                start = visited[s[i]] + 1# start =  3          #start = 1
            res = max(res, i - start + 1)
            visited[s[i]] = i #{p: 3, w: 6, k:4, e: 5,}      # {a: 1, b:2}
            i += 1                                         # i =3
        # res = max(res, i - start)# res = max(1, 3 - 1)
        return res # 2
    # time complexity O(n) n is length of s
    # space complexity O(min(n, m)) where n is length of s and m is the number of unique characters 
    
