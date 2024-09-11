from typing import List

# 14. Longest Common Prefix

# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

 

# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
 

# Constraints:

# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lowercase English letters.

class Solution:
    def longestPrefix(self, strs: List[str]) -> str:
        res = ""
        # n  n is the smallest length
        # "flower","flow","flight"
        # interate element in the shortest str. checking other str
        #n = min([len(s) for s in strs])  # [6,4, 6] n = 4
        n = float('inf')
        for s in strs:
            n = min(n, len(s))

        l = len(strs) # 3
        if l == 1:
            return strs[0]
        for i in range(n): # 0 ~3 i = 2
            cur = strs[0][i] # o
            for j in range(1, l): # 1 ~ 2 j = 2
                if strs[j][i] != cur: # i != o
                    return res# fl
                if j == l - 1:# 1 == 2
                    res += cur # res = fl
        return res
    # time complexity O(n * l) 
    # space complexity O(1)

solution = Solution()
strs = ["flower","flow","flight"]
print(solution.longestPrefix(strs))

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""

        strs.sort()

        # Compare the first and last string in the sorted array
        first = strs[0]
        last = strs[-1]
        result = ""

        # Compare character by character until a mismatch is found
        for i in range(min(len(first), len(last))):
            if first[i] != last[i]:
                return result
            result += first[i]

        return result
    # O(nlogn * m)
    # O(1)


