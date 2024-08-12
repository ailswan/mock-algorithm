from typing import List
#206. Reverse Linked List
# Given the head of a singly linked list, reverse the list, and return the reversed list.

# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]

# Input: head = [1,2]
# Output: [2,1]
# Example 3:

# Input: head = []
# Output: []
 

# Constraints:

# The number of nodes in the list is the range [0, 5000].
# -5000 <= Node.val <= 5000
 

# Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?

class Node:
  def __init__(self, val = 0, next = None) -> None:
    self.val = val
    self.next = Node
    
class Solution:
  def reverse_linked_list(self, head: Node) -> Node:
    # we start with a dummy node to point to the new head
    # at each node, we want to use a temp node to swap the direction of the pointer

                                        
    ptr = None           #  1 <-prt      2 ->3 ->4        2<-1<-ptr  3->4
    #                                    tmp

    while head and head.next:
      tmp = head.next
      head.next = ptr
      ptr = head
      head = tmp

    return ptr

# None <- 1 <- 2 <- 3 <- 4 <- 5 <- 6                            
#                                  ^
#                                  ptr
#                                 head

# time => (N)
# space -> (1)
