from typing import List

# 76. Minimum Window Substring

# Given two strings s and t of lengths m and n respectively, return the minimum window 
# substring
#  of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

# The testcases will be generated such that the answer is unique.

 

# Example 1:

# Input: s = "ADOBECODEBANC", t = "ABC"
# Output: "BANC"
# Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
# Example 2:

# Input: s = "a", t = "a"
# Output: "a"
# Explanation: The entire string s is the minimum window.
# Example 3:

# Input: s = "a", t = "aa"
# Output: ""
# Explanation: Both 'a's from t must be included in the window.
# Since the largest window of s only has one 'a', return empty string.
 

# Constraints:

# m == s.length
# n == t.length
# 1 <= m, n <= 10^5
# s and t consist of uppercase and lowercase English letters.


# Follow up: Could you find an algorithm that runs in O(m + n) time?

class Solution:
    def minWindowSubstring(self, s: str, t: str) -> str:
        # sliding window
        # confirm the length of s must be GTE t (m >= n)
        # note: upper case and lower case letters are treated as different
        # note: min window must be of length t (n) or greater

        # start our window as indices 0 ~ n - 1
        # if all the characters match, then we have found our window, return
        # otherwise, expand our right pointer
        # at some point, we move our left pointer to decrease our window size...
            # when all characters in t have been matched
        m = len(s)
        n = len(t)

        if m < n:
            return ""

        counts = {}
        window = {}
        for c in t:
            counts[c] = counts.get(c, 0) + 1

        required = len(counts.keys())
        formed = 0
        left, right = 0, 0
        ans = (float("inf"), None, None) # include the min_window, left, and right bounds

        # for i in range(left, right):
        #     char = s[i]
        #     if char in counts:
        #         counts[char] -= 1
        
        # if all(counts.values() == 0):
        #     return s[left, right + 1]
   #window_counts
   #counts
        while right < m:
            char = s[right]
            window[char] = window.get(char, 0) + 1
            if char in counts and counts[char] == window[char]:
                formed += 1
            while left <= right and formed == required:
                if right - left + 1 < ans[0]:
                    ans = (right - left + 1, left, right)
                ch = s[left]
                window[ch] -= 1
                if ch in counts and window[ch] < counts[ch]:
                    formed -= 1
                left += 1
            right += 1
        
        i, j = ans[1], ans[2]
        return s[i: j + 1] if ans[0] != float("inf") else ""
                        
# time => O(m + n) where m is the length of string s <= 2m = m level complexity
# space => O(n) window is only as large as the unique characters of string t

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        #ct = [] * 26 * 2  ct_t from t 
        # A D A C B E C 
        # l     l   r   
        #ct[0]++ ct[1]++
        # if ct_t == ct: update mini_l & start = l ; move l to next char in t  
        if len(s) < len(t) or not s or not t:
            return ""
        def f(chr):
            if 'a' <= chr <= 'z':
                return ord(chr) - ord('a') + 26
            else:
                return ord(chr) - ord('A')
        ct_t = [0] * 52
        for c in t:
            ct_t[f(c)] += 1
        l, r, n = 0, 0, len(s)
        ct = [0] * 52
        mini_l = float('inf')
        start = 0
        def contains_all(ct, ct_t):
            for i in range(52):
                if ct_t[i] > ct[i]:
                    return False
            return True
        while r < n:
            ct[f(s[r])] += 1

            while contains_all(ct, ct_t):  
                if r - l + 1 < mini_l: 
                    mini_l = r - l + 1
                    start = l
                ct[f(s[l])] -= 1
                l += 1

            r += 1
        return  s[start: start + mini_l] if mini_l != float('inf') else ""
                
                
                