from typing import List

#234. Palindrome Linked List
# Given the head of a singly linked list, return true if it is a  palindrome or false otherwise.

#  Input: head = [1,2,2,1]
# Output: true
# 1->2->2->1

# Input: head = [1,2]
# Output: false
# 1 ->2

# Constraints:

# The number of nodes in the list is in the range [1, 10^5].
# 0 <= Node.val <= 9
 

# Follow up: Could you do it in O(n) time and O(1) space?

class Node:
  def __init__(self, val = None, next = None) -> None:
    self.val = val
    self.next = None

class Solution:
  def isPalindrome(self, head: Node) -> bool:

    # [1,2,2,1]
    # first we find the middle node using fast and slow pointers
    mid = self.findMiddle(head)
    
    mid_marker = mid

    # our fast is at the end
    
    # reverse the linked list from the middle to the end
    reversed_mid_to_end = self.reverseList(mid)

    # compare the linked list (head -> mid and end -> mid), all nodes should be the same
    return self.compareLists(head, reversed_mid_to_end)

  def findMiddle(self, head: Node) -> Node:
      slow = fast = head      # slow = 1, fast = 1    
      while fast and fast.next:             # fast = 1    fast = 2 fast.next = 1
        slow = slow.next                    # slow = 2    slow = 2
        fast = fast.next.next               # fast = 2    fast = None
      return slow  # 2

  def reverseList(self, mid: Node) -> Node: # 1 -> 2 ->             None <- 2 <- 1
                                           #                                     ^mid
      prev = None
      while mid:
        tmp = mid.next                      # tmp = 1
        mid.next = prev                     # mid.next = None
        prev = tmp                          # prev = 1
        mid = prev                          # mid = 1
      return prev

  def compareLists(self, h1: Node, h2) -> bool:    # 1 -> 2 -> 2 -> 1     # 1 -> 2 -> None
      while h1 and h2:
        if h1.val == h2.val:
          continue
        else:
          return False
      return True

# time => (N)
# space => (1)