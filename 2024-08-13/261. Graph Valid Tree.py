from typing import List
import collections
# 261. Graph Valid Tree

# You have a graph of n nodes labeled from 0 to n - 1. You are given an integer n and a list of edges where edges[i] = [ai, bi] indicates that there is an undirected edge between nodes ai and bi in the graph.

# Return true if the edges of the given graph make up a valid tree, and false otherwise.

# Input: n = 5, edges = [[0,1],[0,2],[0,3],[1,4]]
# Output: true

#     0
#   / | \
#  1  2  3
#  |
#  4

# Input: n = 5, edges = [[0,1],[1,2],[2,3],[1,3],[1,4]]
# Output: false

# 0 -- 1 -- 2  
#      | \  |   
#      |  \ | 
#      4    3

# Constraints:
# 1 <= n <= 2000
# 0 <= edges.length <= 5000
# edges[i].length == 2
# 0 <= ai, bi < n
# ai != bi
# There are no self-loops or repeated edges.

# characteristics of a tree:
# 1) if only 1 unidirected edge, then it's a leaf
# 2) there can only be connection between node and parent, no connection of nodes amongst the children nodes

# {
#   0: [1],
#   1: [2, 3, 4],
#   2: [1, 3],
#   3: [1, 2],
#   4: [1]
# }


class Node:
  def __init__(self, val, neighbors = []) -> None:
    self.val = val
    self.neighbors = neighbors

class Solution:
  def isValidTree(self, n:int, edges: List[List[int]]) -> bool:
    # start with creating an adjacency list
    # n = len(edges) + 1

  # n = 5, edges = [[0,1],[0,2],[0,3],[1,4], []]


    g = defauldict(List)
    for i in range(n):      # i = 0, n = 5
      x, y = edges[i]       # x = 0, y = 1
      if not x and not y:
        return False  
      g[x].append(y)        # g = { 0: [1] }
      g[y].append(x)        # g = { 0: [1], 1: [0] }
    visited = set()
        #     0 
        #   /        [[0,1],[2,3]] N = 4
        #  1  2   
        #     |
        #     3  
        #         
    # run dfs, see if there is a cycle in the graph
    def dfs(idx, parent):  #dfs( 4 , 1)
      if idx in visited:
        self.ans = False
        return False
      visited.add(idx) #{4, 2, 1, 0, 3}

      for child in g[idx]:    #{4:[1, 2]}
        if child != parent:
          if not dfs(child, idx):
            return False
      return True
    
    dfs(0, -1)
    return self.ans and len(visited) == n

# time => (len(edges) + N)  
# space => (N + len(edges))