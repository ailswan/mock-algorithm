from typing import List

# 143. Reorder List

# You are given the head of a singly linked-list. The list can be represented as:

# L0 → L1 → … → Ln - 1 → Ln
# Reorder the list to be on the following form:

# L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
# You may not modify the values in the list's nodes. Only nodes themselves may be changed.

 

# Example 1:

# input: 1 -> 2 -> 3 -> 4

# output: 1 -> 4 -> 2 -> 3

# Input: head = [1,2,3,4]
# Output: [1,4,2,3]

# Example 2:

# input: 1 -> 2 -> 3 -> 4 -> 5

# output: 1 -> 5 -> 2 -> 4 -> 3

# Input: head = [1,2,3,4,5]
# Output: [1,5,2,4,3]
 

# Constraints:

# The number of nodes in the list is in the range [1, 5 * 10^4].
# 1 <= Node.val <= 1000

class Node:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

class Solution:
    def reOrderList(self, head: Node) -> Node:
        # input: 1 -> 2 -> 3 -> 4
        # output: 1 -> 4 -> 2 -> 3
        #  find the mid  
        #  reverse the half linkedlist mid  4-> 3
        #  head  1 ->2 
        # merged mid and head  1 -> 4 -> 2 -> 3
        midHead = self.findMid(head)  # 1  2   3  4 5   node 3 4 5
        firstPart = self.findhalf(head)
        reversedHead = self.reverse(midHead)  # node 5 4 3
        res = Node()
        cur = res
        while reversedHead and firstPart: # reversedHead   5 4 3   firstPart   1 2   
            cur.next = firstPart # cur -> 1
            firstPart = firstPart.next#   firstPart      
            cur = cur.next # cur 1
            cur.next = reversedHead #res ->  1 ->  4
            reversedHead = reversedHead.next
            cur = cur.next # cur 4
        # 1 5 2 4  reversedHead 3   
        if reversedHead:
            cur.next = reversedHead
        return res.next 
    def findhalf(self, head): # pre   1    2        3  4 
                       #           slow              fast
        pre = Node()
        slow = head
        pre.next = slow
        fast = head
        while fast and fast.next:
            slow = slow.next
            pre = pre.next
            fast = fast.next.next
        pre.next = None
        return head

    def findMid(self, head):  # 1  2   3 4 5
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow  # slow -> 3 -> 4    5 

    def reverse(self, head):# pre 5 4 3 
        pre = None
        cur = head
        while cur:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp
        return pre
        
        
        


