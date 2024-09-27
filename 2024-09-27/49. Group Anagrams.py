from typing import List

# 49. Group Anagrams
# Given an array of strings strs, group the 
# anagrams
#  together. You can return the answer in any order.

 

# Example 1:

# Input: strs = ["eat","tea","tan","ate","nat","bat"]

# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

# Explanation:

# There is no string in strs that can be rearranged to form "bat".
# The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
# The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.
# Example 2:

# Input: strs = [""]

# Output: [[""]]

# Example 3:

# Input: strs = ["a"]

# Output: [["a"]]

# Constraints:

# 1 <= strs.length <= 10^4
# 0 <= strs[i].length <= 100
# strs[i] consists of lowercase English letters.

# edge cases => no empty lists... empty string in list returns empty list of lists of empty string
# 

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # hashtable/default dictionary
        # iterate through the input and sort the letters in each word
        # if sorted letters exist as a key, append the current word to the key
        # after scanning the input, combine all the values in the defaultdict into a list and return

        groups = defaultdict(list)

        for word in strs:
            letters = sorted(word)
            groups[letters].append(word)
        
        return [x for x in groups.values()]
    
# time complexity => O(n * mlogm) where n is the total number of words in input, m is the length of the longest word
# space => O(n * m) n is the length of the dictionary, m is longest word (sorting)