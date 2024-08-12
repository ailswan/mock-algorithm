from typing import List, Optional

# 133. Clone Graph

# Given a reference of a node in a connected undirected graph.

# Return a deep copy (clone) of the graph.

# Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

# class Node {
#     public int val;
#     public List<Node> neighbors;
# }
 

# Test case format:

# For simplicity, each node's value is the same as the node's index (1-indexed).
# For example, the first node with val == 1, the second node with val == 2, and so on. The graph is represented in the test case using an adjacency list.

# An adjacency list is a collection of unordered lists used to represent a finite graph. Each list describes the set of neighbors of a node in the graph.

# The given node will always be the first node with val = 1. You must return the copy of the given node as a reference to the cloned graph.

 

# Example 1:

# Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
# Output: [[2,4],[1,3],[2,4],[1,3]]
# Explanation: There are 4 nodes in the graph.
# 1st node (val = 1)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
# 2nd node (val = 2)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
# 3rd node (val = 3)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
# 4th node (val = 4)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).

#     1 --- 2
#     |     |
#     |     |
#     4 --- 3

# Example 2:

# Input: adjList = [[]]
# Output: [[]]
# Explanation: Note that the input contains one empty list. The graph consists of only one node with val = 1 and it does not have any neighbors.

# Example 3:

# Input: adjList = []
# Output: []
# Explanation: This an empty graph, it does not have any nodes.
 

# Constraints:
# The number of nodes in the graph is in the range [0, 100].
# 1 <= Node.val <= 100
# Node.val is unique for each node.
# There are no repeated edges and no self-loops in the graph.
# The Graph is connected and all nodes can be visited starting from the given node.

# class Node {
#     public int val;
#     public List<Node> neighbors;
# }
import collections
class Node:
    def __init__(self,val,neighbors = []):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def __init__(self):
        self.node_map = defaultdict(list)      # defaultdict(Node)    <-- defaultdict  key 
    def copyGraph(self, node: Node) -> Node: # node2  map ={1:copy1} node1
        # node_map {node: copy}
        # if node in node_map: add the copy to current neighbors else create a new copy node store in the map
        #adjList = [[2,4],[1,3],[2,4],[1,3]]
        if node in self.node_map:# node2  map ={1:copy1} node1 <-- False
            return self.node_map[node] #return node 1
        else:
            copy = Node(node.val) # copy2  map ={1:copy1}
            self.node_map[node] = copy# map ={1:copy1, 2:copy2}
            copy.neighbors = [self.copyGraph(n) for n in node.neighbors] #copy.neighbors = [copy2, copy4] [2,4] [1,3] [1,3]
            return copy

 
from collections import defaultdict

class Node:
    def __init__(self, val):
        self.val = val
        self.neighbors = []

node_map = defaultdict(Node)
node1 = Node(1)

# Check if node1 is in the map (should be False initially)
print(node1 in node_map)  # Output: False

# Accessing node_map[node1] will create a new entry
node_map[node1]

# Now check again
print(node1 in node_map)  # Output: True