from typing import List


#426. Convert Binary Search Tree to Sorted Doubly Linked List

# Convert a Binary Search Tree to a sorted Circular Doubly-Linked List in place.

# You can think of the left and right pointers as synonymous to the predecessor and successor pointers in a doubly-linked list. For a circular doubly linked list, the predecessor of the first element is the last element, and the successor of the last element is the first element.

# We want to do the transformation in place. After the transformation, the left pointer of the tree node should point to its predecessor, and the right pointer should point to its successor. You should return the pointer to the smallest element of the linked list.


# Input: root = [4,2,5,1,3]
# Output: [1,2,3,4,5]

#       4
#     /   \
#    2     5
#  /   \
# 1    3

# Explanation: The figure below shows the transformed BST. The solid line indicates the successor relationship, while the dashed line means the predecessor relationship.

# Example 2:

# Input: root = [2,1,3]
# Output: [1,2,3]
 

# Constraints:

# The number of nodes in the tree is in the range [0, 2000].
# -1000 <= Node.val <= 1000
# All the values of the tree are unique.

class Node:
	def __init__(self, val = 0, left = None, right = None) -> None:
		self.val = val
		self.left = left
		self.right = right

class Solution:
	def convertBinarySearchTree(self, root: Node) -> Node:
		# dfs, recursive, in-order
		# use a first and last pointer to keep track of the leftmost leaf node (first) and the right-most leaf (largest Node, last)
		# hook up first to last, and last to first

		if root is None:
			return None

		first, last = None, None
		def dfs(node):
			nonlocal first, last
			# in-order traversal
			if node:
				dfs(node.left)

				if last:
					node.left = last
					last.right = node
				else:
					first = node
				last = node
				dfs(node.right)

		dfs(root)
		last.right = first
		first.left = last
		return first

#time => (N)
# space => (N) or log(n) if balanced *** FOR CALL STACK ****