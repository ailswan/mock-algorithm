from typing import List

#  791. Custom Sort String
# You are given two strings order and s. All the characters of order are unique and were sorted in some custom order previously.

# Permute the characters of s so that they match the order that order was sorted.
#  More specifically, if a character x occurs before a character y in order, then x should occur before y in the permuted string.

# Return any permutation of s that satisfies this property.

 

# Example 1:

# Input: order = "cba", s = "abcd"

# Output: "cbad"

# Explanation: "a", "b", "c" appear in order, so the order of "a", "b", "c" should be "c", "b", and "a".

# Since "d" does not appear in order, it can be at any position in the returned string. "dcba", "cdba", "cbda" are also valid outputs.

# Example 2:

# Input: order = "bcafg", s = "abcd"

# Output: "bcad"

# Explanation: The characters "b", "c", and "a" from order dictate the order for the characters in s. The character "d" in s does not appear in order, so its position is flexible.

# Following the order of appearance in order, "b", "c", and "a" from s should be arranged as "b", "c", "a". "d" can be placed at any position since it's not in order.
# The output "bcad" correctly follows this rule. Other arrangements like "dbca" or "bcda" would also be valid, as long as "b", "c", "a" maintain their order.

 

# Constraints:

# 1 <= order.length <= 26
# 1 <= s.length <= 200
# order and s consist of lowercase English letters.
# All the characters of order are unique.

class Solution:
    def customSort(self, order: str, s: str) -> str:
        # brute force -> iterate through order, for each char if it exists in s, add the char to the answer
            # add remaining chars in s to answer, as they don't appear in the order dictionary
        
        # if a character in s does not exist in order -> character can be anywhere in our output
        # use hashmap to map order characters with their relative index <char, idx>
        # iterate through our s input, for each char, append it to our answer at the index from the hashmap
            # use a frequency map to keep track of how many of the same chars appear in s, while keeping the relative index
        ans = ""
        freq = Counter(s)

        for char in order:
            if char in freq: #freq[c] = 2   
                ans += char * freq[char]        # "a"... "abb".... "abbop"
                freq[char] = 0
        
        for k, v in freq:
            if v > 0:
                ans += k * v
        
        return ans
    
# Input: order = "cba", s = "ed"        freq = Counter(s) freq[c] = 0  freq[a] = 0
#res   ccbaed

# time => (m + n) where m is the length of the order and n is the length of s
# space => (n) where n is length of s (for frequency map)