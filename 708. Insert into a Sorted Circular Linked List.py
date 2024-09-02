from typing import List
#  708. Insert into a Sorted Circular Linked List

# Given a Circular Linked List node, which is sorted in non-descending order, write a function to insert a value insertVal into the list such that it remains a sorted circular list.
# The given node can be a reference to any single node in the list and may not necessarily be the smallest value in the circular list.

# If there are multiple suitable places for insertion, you may choose any place to insert the new value. After the insertion, the circular list should remain sorted.

# If the list is empty (i.e., the given node is null), you should create a new single circular list and return the reference to that single node.
# Otherwise, you should return the originally given node.

 
#  1  2  3  3  4   5

# Example 1:
# 1----
# |    |
# |    |
# 4<--- 3 <-- head

# Input: head = [3,4,1], insertVal = 2
# Output: [3,4,1,2]
# Explanation: In the figure above, there is a sorted circular list of three elements. You are given a reference to the node with value 3, and we need to insert 2 into the list. The new node should be inserted between node 1 and node 3. After the insertion, the list should look like this, and we should still return node 3.
#  1 ----->2
#  |       |
#  |       |
#  4 <-----3 <--- head

# Example 2:
# Input: head = [], insertVal = 1
# Output: [1]
# Explanation: The list is empty (given head is null). We create a new single circular list and return the reference to that single node.
# Example 3:

# Input: head = [1], insertVal = 0
# Output: [1,0]
 

# Constraints:

# The number of nodes in the list is in the range [0, 5 * 10^4].
# -10^6 <= Node.val, insertVal <= 10^6

class Nodes:
    def __init__(self, val: int, next: Node) -> None:
        self.val = val
        self.next = None

    def insertNode(self, head: Node, insertVal: int) -> Node:
        # check if list is empty... create new Node and return
        if head is None:
            new_node = Node(insertVal)
            new_node.next = new_node
            return new_node
        
        # starting from the head, traverse the list and look for insertion point
        # the insertion point is a location where the insertVal is larger than the previous node val
        # make sure the insertVal node is connected to the next node
        # return head
        ptr = head
        fast = head.next #  node 1
        first = None

        if ptr == fast:
            new_node = Node(insertVal)
            ptr.next = new_node
            new_node.next = ptr
            return head
        # find the "circular" point
        while ptr and fast:
            if fast.val >= ptr.val:
                fast = fast.next
                ptr = ptr.next
            else:
                first = fast
                break


        if insertVal >= fast.val:
            new_node = Node(insertVal)
            tmp = fast.next
            fast.next = new_node
            new_node.next = tmp
            return head

        ptr = first
        while True:
            if insertVal > ptr.val:
                ptr = ptr.next
            else:
                new_node = Node(insertVal)
                new_node.next = ptr.next
                ptr.next = new_node
                return head
# time => O(N) where N is the number of nodes in our circular list
# space => O(1)