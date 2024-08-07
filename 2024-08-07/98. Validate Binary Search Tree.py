from typing import List
# 98. Validate Binary Search Tree
# Given the root of a binary tree, determine if it is a valid binary search tree (BST).

# A valid BST is defined as follows:

# The left 
# subtree
#  of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.
# Input: root = [2,1,3]
# Output: true
    #     2
    #   /   \
    #  1     3

# Input: root = [5,1,4,null,null,3,6]
# Output: false
# Explanation: The root node's value is 5 but its right child's value is 4.
    #      5
    #     /  \
    #    1    4
    #        /  \
    #       3    6

# Constraints:

# The number of nodes in the tree is in the range [1, 104].
# -231 <= Node.val <= 231 - 1



class Node():
    def __init__(self, val):
        self.val = val
        self.left = Node()
        self.right = Node()


class Solution():
    def valid_bst(self, root, left_min_val, right_max_val):
        # dfs
        # at every recursive call, track the root value, and check that the left child is smaller than the root val, and right child is larger than root val
        # root.left.val < root.val and root.right.val > root.val
        # return False if condition not satisfied
        # if no children, return True

# [5,4,6,null,null,3,7]
#         5
#       /  \
#      4    7
#          / \
#         6   8
        if root is None:
            return True
        

        left_min_val = min(left_min_val, root.val)
        right_max_val = max(right_max_val, root.val)
            # l   node.val   r
        if (root.left and root.left.val > left_min_val) or (root.right and root.right.val < right_max_val):
            return False
        else:
            return self.valid_bst(root.left, left_min_val, right_max_val) and self.valid_bst(root.right, left_min_val, right_max_val)


# Input: root = [2,1,3]
# check the root -> root is not None,
# root.left.val => 1 (1 > 2): False [line 50]
# root.right.val => 3 (3 < 2): False

# Input: root = [1] (left child of root)
# returns True

# Input: root = [3] (right child of root)
# returns True


#139. Word Break
#this is a template for mock questions
# class Solution:
#     def wordBreak(self, s: str, wordDict: List[str]) -> bool:
#         #dp[i]  [:i] can be separated or not
#         #dp[i] = dp[i - n] if s[i - n: i] n is the length of word
#         l = len(s)
#         dp = [False] * (l + 1)
#         dp[0] = True
#         for i in range(1, l + 1):
#             for w in wordDict:
#                 n = len(w)
#                 if s[i - n: i] == w and dp[i - n]:
#                     dp[i] = True
#                     break
#         return dp[-1]

# solution = Solution()
# s1 = "leetcode"
# wordDict1 = ["leet", "code"]
# print(solution.wordBreak(s1, wordDict1))

# s2 = "applepenapple"
# wordDict2 = ["apple", "pen"]
# print(solution.wordBreak(s2, wordDict2)) 

# s3 = "catsandog"
# wordDict3 = ["cats", "dog", "sand", "and", "cat"]
# print(solution.wordBreak(s3, wordDict3))


# # test mode
# # Test case 1
# s1 = "leetcode"
# wordDict1 = ["leet", "code"]
# assert solution.wordBreak(s1, wordDict1) == True, "Test case 1 failed"

# # Test case 2
# s2 = "applepenapple"
# wordDict2 = ["apple", "pen"]
# assert solution.wordBreak(s2, wordDict2) == True, "Test case 2 failed"

# # Test case 3
# s3 = "catsandog"
# wordDict3 = ["cats", "dog", "sand", "and", "cat"]
# assert solution.wordBreak(s3, wordDict3) == False, "Test case 3 failed"

# print("All test cases passed!")