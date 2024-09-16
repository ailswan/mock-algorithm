from typing import List 
# 274. H-Index

# Given an array of integers citations where citations[i] is the number of citations a researcher received for their ith paper, return the researcher's h-index.

# According to the definition of h-index on Wikipedia: The h-index is defined as the maximum value of h such that the given researcher 
# has published at least h papers that have each been cited at least h times.



# Example 1:

# Input: citations = [3,0,6,1,5]
# Output: 3
# Explanation: [3,0,6,1,5] means the researcher has 5 papers in total and each of them had received 3, 0, 6, 1, 5 citations respectively.
# Since the researcher has 3 papers with at least 3 citations each and the remaining two with no more than 3 citations each, their h-index is 3.
# Example 2:

# Input: citations = [1,3,1]
# Output: 1
 

# Constraints:

# n == citations.length
# 1 <= n <= 5000
# 0 <= citations[i] <= 1000

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # find the number of papers
        # iterate through citaitons
        # the index of the list represents the number of papers written so far
        # we ensure the element (ie: citations) is GTE the index

        # use a counter to find the frequency of citations
        # iterate from 1 -> len(citations) and check if key exists in counter

        # Input: citations = [3,0,9,1,5]
        
        # h <= PaperNumber
        # h = 3 <= 3
        # h = 1 <= 4

        n = len(citations)
        freq = Counter(citations)   # {5:2, 3:1 ,0:1,1:1}
        # h-index is b/w 0 -> n
        # 
        ans = 0
        for i, count in enumerate(freq):
            if count >= n:
                freq[n] += count
                # del freq[i]
        total = 0
        for h in range(n, 0, -1):   # h-index
             # {5:2, 3:1 ,0:1,1:1}
             # h = 5  total= 2  >= 5?
             #    4   total= 2  >= 4?
             #    3   total= 3  >= 3? return 3
            if h in freq:
                total += freq[h]
            if total >= h:
                return h
        
        return ans


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        paper = [0] * (n + 1)
        for c in citations:
            paper[min(c, n)] += 1
        s, h = paper[-1], n
        while h > s:
            h -= 1
            s += paper[h]
        return h    
