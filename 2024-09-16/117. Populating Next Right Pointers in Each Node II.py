from typing import List 
# 117. Populating Next Right Pointers in Each Node II
# Given a binary tree

# struct Node {
#   int val;
#   Node *left;
#   Node *right;
#   Node *next;
# }
# Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

# Initially, all next pointers are set to NULL.

#  Example 1:
#      1 -> None
#     / \
#     2 -> 3 -> None
#    /\   \
#   4-> 5 -> 7 -> None
# Input: root = [1,2,3,4,5,null,7]
# Output: [1,#,2,3,#,4,5,7,#]
# Explanation: Given the above binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. 
#  The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.
# Example 2:

# Input: root = []
# Output: []
 

# Constraints:

# The number of nodes in the tree is in the range [0, 6000].
# -100 <= Node.val <= 100
 

# Follow-up:

# You may only use constant extra space.
# The recursive approach is fine. You may assume implicit stack space does not count as extra space for this problem.

class Node:
    def __init__(self, val, left, right, next) -> None:
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def populateNextRightPointersNode(self, root: Node) -> Node:
        # BFS, level order traversal....
        
        if root is None:
            return None
        
        # root.next will always be None
        # keep a head pointer to the previous levels left-most node
        # use the head pointer as the queue, to process the children of that level's nodes

#            1 -> None
#           / \
#  head -> 2 -> 3 -> None
#           \   \
# n_head->    5 -> 7 -> None
#            cur
        root.next = None
        head = root
        hasNextLvl = False
        cur = None
        next_lvl_head = None     # None

        while head:
            if head.left:
                if next_lvl_head is None:
                    next_lvl_head = head.left
                cur = head.left
                cur = cur.next
            if head.right:
                if next_lvl_head is None:
                    next_lvl_head = head.right
                cur = head.right
                cur = cur.next
            head = head.next
            if head is None:
                head = next_lvl_head
                cur = None
                next_lvl_head = None
                
        return root

# time => O(n) where n is the number of nodes in the Tree
# space => O(1) we leverage the "next" pointers of the nodes, so constant space