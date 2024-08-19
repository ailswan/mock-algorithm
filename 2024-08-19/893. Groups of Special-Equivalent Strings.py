from typing import List

# 893. Groups of Special-Equivalent Strings

# You are given an array of strings of the same length words.

# In one move, you can swap any two even indexed characters or any two odd indexed characters of a string words[i].

# Two strings words[i] and words[j] are special-equivalent if after any number of moves, words[i] == words[j].

# For example, words[i] = "zzxy" and words[j] = "xyzz" are special-equivalent because we may make the moves "zzxy" -> "xzzy" -> "xyzz".
# A group of special-equivalent strings from words is a non-empty subset of words such that:

# Every pair of strings in the group are special equivalent, and
# The group is the largest size possible (i.e., there is not a string words[i] not in the group such that words[i] is special-equivalent to every string in the group).
# Return the number of groups of special-equivalent strings from words.

 

# Example 1:

# Input: words = ["abcd","cdab","cbad","xyzz","zzxy","zzyx"]
# Output: 3
# Explanation: 
# One group is ["abcd", "cdab", "cbad"], since they are all pairwise special equivalent, and none of the other strings is all pairwise special equivalent to these.
# The other two groups are ["xyzz", "zzxy"] and ["zzyx"].
# Note that in particular, "zzxy" is not special equivalent to "zzyx".
# Example 2:

# Input: words = ["abc","acb","bac","bca","cab","cba"]
# Output: 3
 

# Constraints:

# 1 <= words.length <= 1000
# 1 <= words[i].length <= 20
# words[i] consist of lowercase English letters.
# All the strings are of the same length.

class Solution:
  	def groupStrings(self, ss: List[str]) -> int:
    	# use hashmap
    	# brute force -> the first word is its own group, check every word against the first group word to see if it's "special-equivalent"
      		# if special-equivalent, add it to first group, otherwise start its own group
		# as the group size increases, check each word in the input against each group
		# when a pair of words are equivalent in the same group, both words are also equivalent to all other words in the group
		# return count of groups
		groups = {
			ss[0]: 1
		}
		count = 0

		for word in ss:
			for key in groups.keys():
				if self.isEquivalent(word, key):
					groups[key] += 1
				else:
					groups[key] = 1

		count = len(groups.keys())
		return count


	# words[i] = "zzxy" and words[j] = "xyzz"
	# characters at odd indices -> check frequency of characters in odd positions
	# characters at even indices -> check freq of chars in even positions
	def isEquivalent(self, s1: str, s2: str) -> bool:
		# TODO: check if input strings are special-equivalent
		odd_chars = Counter()
		even_chars = Counter()

		for i, c1 in enumerate(s1):
			if i % 2 == 1:
				odd_chars.append(c1)
			else:
				even_chars.append(c1)

		for i, c2 in enumerate(s2):
			if i % 2 == 1:
				odd_chars.pop(c1)
			else:
				even_chars.pop(c1)  
		return len(odd_chars) == 0 and len(even_chars) == 0
# time complexity => (N^2)
# space complexity => (N)

def numSpecialEquivGroups(self, words: List[str]) -> int:
        def encode(word):
            even_chars = sorted(word[::2])  # Characters at even indices
            odd_chars = sorted(word[1::2])  # Characters at odd indices
            return ''.join(even_chars) + ''.join(odd_chars)  # Concatenate the sorted characters			# zzxy -> 
        #{'bdac':3, }
        return len({encode(word) for word in words})
# time => (NlogN)
# space => (1)

    # counter[sorted(word1) + sorted(word2)] += 1
