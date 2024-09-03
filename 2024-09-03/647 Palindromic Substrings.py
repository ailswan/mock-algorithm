from typing import List

# 647. Palindromic Substrings
# Given a string s, return the number of palindromic substrings in it.

# A string is a palindrome when it reads the same backward as forward.

# A substring is a contiguous sequence of characters within the string.

 

# Example 1:

# Input: s = "abc"
# Output: 3
# Explanation: Three palindromic strings: "a", "b", "c".
# Example 2:

# Input: s = "aaa"
# Output: 6
# Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
 

# Constraints:

# 1 <= s.length <= 1000
# s consists of lowercase English letters.

class Solution:
    def palindromicSubstrings(self, s: str) -> int:
        # individual letters are palindromes
        # need backtracking to gather all the combinations
        ans = 0
        #s = "abc"  a  b  c  d e  len  5    ab      abc     bc
        #           i
        #                      j < len(s) 

          # c a b a c  a a
            # l   r    l r
            #  mid      ^
        #res   += 1
        # for i in range(len(s)): # 0 ~ 4  i = 4
        #     for j in range(i, len(s)): #  j 4 ~ 5  j = len(s) - 1
        #         if self.isPalindrome(s[i:j + 1]):           # < len(s)
        #             ans += 1

        # check all middle's in the string
        # expand from middle to count up valid palindromes
        for i in range(len(s)):
            # i is the middle...
            ans += self.countPalindromes(s, i, i)
            ans += self.countPalindromes(s, i, i + 1)

        return ans


    def countPalindromes(self, s: str, left: int, right: int) -> int:
        total = 0
        while left >= 0 and right < len(s):
            if s[left] == s[right]:
                total += 1
                left -= 1
                right += 1
            else:
                break
        return total

# time => O(N^2) where N is the length of the string
# space => O(1)

class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        n = len(s)
        for mid in range(n * 2 - 1):
            l = mid // 2
            r = l + mid % 2
            while l >= 0 and r < n and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
        return res
            