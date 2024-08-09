from typing import List
from collections import defaultdict

# 138. Copy List with Random Pointer

# A linked list of length n is given such that each node contains an additional random pointer, which could point to any node in the list, or null.

# Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, where each new node has its value set to the value of its corresponding original node. Both the next and random pointer of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state. None of the pointers in the new list should point to nodes in the original list.

# For example, if there are two nodes X and Y in the original list, where X.random --> Y, then for the corresponding two nodes x and y in the copied list, x.random --> y.

# Return the head of the copied linked list.

# The linked list is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:

# val: an integer representing Node.val
# random_index: the index of the node (range from 0 to n-1) that the random pointer points to, or null if it does not point to any node.
# Your code will only be given the head of the original linked list.


# Example 1:
# https://assets.leetcode.com/uploads/2019/12/18/e1.png

# Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
# Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]


# Example 2:
# https://assets.leetcode.com/uploads/2019/12/18/e2.png

# Input: head = [[1,1],[2,1]]
# Output: [[1,1],[2,1]]


# Example 3:

# Input: head = [[3,null],[3,0],[3,null]]
# Output: [[3,null],[3,0],[3,null]]


# Constraints:
# 0 <= n <= 1000
# -104 <= Node.val <= 104
# Node.random is null or is pointing to some node in the linked list.

class Node:
    def __init__(self,val = 0, next = None, random = None):
        self.val = val
        self.next = next
        self.random = random

class Solution:
    def copyLinkList(self, head: Node) -> Node:
        #head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
        # 7 -> 13 -> 11 -> 10 -> 1     dummy-> 7 -> 13 -> 11 -> 10 -> 1
        # |     |    |           |             c
        # ------      -----------
        # copy the linklist following the next pointer
        # map to store the copied node{X: x, Y: y}  {og1: cp1}
        dummy = Node()  
        curr = dummy #None                                   curr
        original = head  #node7                                     
        nodeMap = defaultdict(Node)   #dummy.next -> None
        while original: #node13
            curr.next = Node(original.val)#curr = copy13 # we need init the node before move the curr point to track it 
            nodeMap[original] = curr #{node7: copy7, node13: copy13}
            curr = curr.next# copy7 -> copy13-> cur = None
            original = original.next # node13
        #copy dummy-> 7 -> 13 -> 11 -> 10 -> 1
        curr = dummy.next
        original = head
        while original: #node 13  copy 13
            if original.random in nodeMap: # node7  [7,null]  copy7.random = None
                curr.random = nodeMap[original.random] # copy13 -> copy7  nodeMap[None]
            curr = curr.next
            original = original.next
        return dummy.next
            







