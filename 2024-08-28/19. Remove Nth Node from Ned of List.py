from typing import List

# 19. Remove Nth Node from end of List

# Given the head of a linked list, remove the nth node from the end of the list and return its head.

 

# Example 1:

# input: 1 -> 2 -> 3 -> (4) -> 5

# output: 1 -> 2 -> 3 -> 5


# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]
# Example 2:

# Input: head = [1], n = 1
# Output: []
# Example 3:

# Input: head = [1,2], n = 1
# Output: [1]
 

# Constraints:

# The number of nodes in the list is sz.
# 1 <= sz <= 30
# 0 <= Node.val <= 100
# 1 <= n <= sz
 

# Follow up: Could you do this in one pass?

class LinkedNode:
    def __init__(self, val = 0, next = None) -> None:
        self.val = val
        self.next = next
class Solution:
    def removeNth(self, head: LinkedNode, n: int) -> LinkedNode:
        # input: 1 -> 2 -> 3 -> (4) -> 5  head = [1,2,3,4,5], n = 2
        #                  p1^        p2^
        # output: 1 -> 2 -> 3 -> 5
        # two pointers the space between them is n + 1
        # p1 and p2 move together and reach the end
        # p1.next = p1.next.next 
        # return head
        # 1  n = 1
        # 1 -> 2    n = 2
        # 1 -> 2    n = 1
        # p1   p2
        p2 = head #node 1
        for i in range(n): # 0  
            p2 = p2.next # Node2
        p1 = head #node1
        if p2 == p1:
            return None
        if not p2:
            return head.next
        while p2 and p2.next:
            p1 = p1.next  
            p2 = p2.next 
        p1.next = p1.next.next if p1.next else None 
        return head
        #time complexity O(n) n is the length of linked list
        #sapce complexity O(1) 




