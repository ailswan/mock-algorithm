from typing import List

# 173. Binary Search Tree Iterator

# Implement the BSTIterator class that represents an iterator over the in-order traversal of a binary search tree (BST):

# BSTIterator(TreeNode root) Initializes an object of the BSTIterator class. The root of the BST is given as part of the constructor. The pointer should be initialized to a non-existent number smaller than any element in the BST.
# boolean hasNext() Returns true if there exists a number in the traversal to the right of the pointer, otherwise returns false.
# int next() Moves the pointer to the right, then returns the number at the pointer.
# Notice that by initializing the pointer to a non-existent smallest number, the first call to next() will return the smallest element in the BST.

# You may assume that next() calls will always be valid. That is, there will be at least a next number in the in-order traversal when next() is called.

 

# Example 1:

#               7
#             /    \
#            3      15
#                  /   \
#                 9     20

# Input
# ["BSTIterator", "next", "next", "hasNext", "next", "hasNext", "next", "hasNext", "next", "hasNext"]
# [[[7, 3, 15, null, null, 9, 20]], [], [], [], [], [], [], [], [], []]
# Output
# [null, 3, 7, true, 9, true, 15, true, 20, false]

# Explanation
# BSTIterator bSTIterator = new BSTIterator([7, 3, 15, null, null, 9, 20]);
# bSTIterator.next();    // return 3
# bSTIterator.next();    // return 7
# bSTIterator.hasNext(); // return True
# bSTIterator.next();    // return 9
# bSTIterator.hasNext(); // return True
# bSTIterator.next();    // return 15
# bSTIterator.hasNext(); // return True
# bSTIterator.next();    // return 20
# bSTIterator.hasNext(); // return False
 

# Constraints:

# The number of nodes in the tree is in the range [1, 105].
# 0 <= Node.val <= 106
# At most 105 calls will be made to hasNext, and next.
 

# Follow up:

# Could you implement next() and hasNext() to run in average O(1) time and use O(h) memory, where h is the height of the tree?



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:
#               7
#             /    \
#            3      15
#                  /   \
#                 9     20

# Input
# ["BSTIterator", "next", "next", "hasNext", "next", "hasNext", "next", "hasNext", "next", "hasNext"]
# [[[7, 3, 15, null, null, 9, 20]], [], [], [], [], [], [], [], [], []]
# Output
# [null, 3, 7, true, 9, true, 15, true, 20, false]
    def __init__(self, root: Optional[TreeNode]):
        # inorder  l - n - r
        #inorder traversal  store val in array  values = [3,7,9,15,20]
        self.values = [] #[9, 15, 20]
        if root:
            self.dfs(root) 
        self.size = 0
    
    def dfs(self, root):  # node7 node3 node15 node 9 node 20
        if root.left:
            self.dfs(root.left) 
        self.values.append(root.val)# self.values = [3, 7, 9, 15, 20]
        self.size += 1
        if root.right:  
            self.dfs(root.right)
        

    def next(self) -> int:
        #pop(0)  values[0]
        # update the size
        if self.hasNext():# True 
            self.size -= 1
            return self.values.pop(0) # 7
        # time O(1)
        
    def hasNext(self) -> bool:
        if self.size:
            return True
        else:
            return False
        # time O(1)
  #len()
     
    
    # initial the instance of the class time complexity O(n)
    # space complexity O(n) n is the number of nodes
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()