from typing import List

# 23. Merge k Sorted Lists

# You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

# Merge all the linked-lists into one sorted linked-list and return it.

 

# Example 1:

# Input: lists = [[1,4,5],[1,3,4],[2,6]]
# Output: [1,1,2,3,4,4,5,6]
# Explanation: The linked-lists are:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# merging them into one sorted list:
# 1->1->2->3->4->4->5->6
# Example 2:

# Input: lists = []
# Output: []
# Example 3:

# Input: lists = [[]]
# Output: []
 

# Constraints:

# k == lists.length
# 0 <= k <= 10^4
# 0 <= lists[i].length <= 500
# -10^4 <= lists[i][j] <= 10^4
# lists[i] is sorted in ascending order.
# The sum of lists[i].length will not exceed 10^4.
import collections
class Node:
    def __init__(self, val = None, next = None):
        self.val = val
        self.next = next

class Solution:
    def mergeK(self, lists: List[Node]) -> Node:
        # loop lists get each head's value, put them in a min heap , need to store the list index 
        # every pop the mini value from the heap to add a new node to the merged list
        # add the firts value in the same list of the pop according the index (val, i)
        #[[1,4,5],[1,3,4],[2,6]]
        merged = Node()
        heap = []
        dummy = merged
        dummy_lists = lists[:]
        for i, l in enumerate(lists):
            collections.heapq.heappush(heap,(l.val, i))
            dummy_lists[i] = dummy_lists[i].next
        # heap [(1, 0), (1, 1), (2,2)]
        while heap:#[  ,,(5, 0) (6,2)]
            val, i = collections.heapq.heappop(heap) # 2, 2
            new_node = Node(val)
            merged.next = new_node # none -> node1 -> node1-> 2-> 3->4->4->5->6
            merged = merged.next
            if lists[i]:
                collections.heapq.heappush(heap, (dummy_lists[i].val, i))
                dummy_lists[i] = dummy_lists[i].next
        return dummy.next
# time complexity O(n * m) n is number of lists, m is the longest of one list
# space complexity O(n)


