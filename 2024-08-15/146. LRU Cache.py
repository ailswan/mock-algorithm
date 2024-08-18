from typing import List
# 146. LRU Cache
# Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

# Implement the LRUCache class:

# LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
# int get(int key) Return the value of the key if the key exists, otherwise return -1.
# void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
# The functions get and put must each run in O(1) average time complexity.

 

# Example 1:

# Input
# ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
# [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
# Output
# [null, null, null, 1, null, -1, null, -1, 3, 4]

# Explanation
# LRUCache lRUCache = new LRUCache(2);
# lRUCache.put(1, 1); // cache is {1=1}
# lRUCache.put(2, 2); // cache is {1=1, 2=2}
# lRUCache.get(1);    // return 1
# lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
# lRUCache.get(2);    // returns -1 (not found)
# lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
# lRUCache.get(1);    // return -1 (not found)
# lRUCache.get(3);    // return 3
# lRUCache.get(4);    // return 4
 

# Constraints:

# 1 <= capacity <= 3000
# 0 <= key <= 104
# 0 <= value <= 105
# At most 2 * 105 calls will be made to get and put.

# LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
# int get(int key) Return the value of the key if the key exists, otherwise return -1.
# void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
# The functions get and put must each run in O(1) average time complexity.

class Node:
  def __init__(self, val: int = -1) -> None:
     self.key = val
     self.prev = None
     self.next = None


class LRUCache:

    def __init__(self, capacity: int):
      self.capacity = capacity
      self.cache = {}         # can try using orderedDictionary. Ask interviewer if it's possible
      self.head = None        #head is most frequently used, tail is least recently used
      self.tail = self.head

    def get(self, key: int) -> int:
      # first check if the key exists in our dictionary
      # if it exists, return the value
      # else return -1
      if key in self.cache:
        # rearrange the double linked list, the key goes to the head of the list
        self.moveNodeToHead(self.head, key)
        return self.cache[key]
      else:
        return -1


    def put(self, key: int, value: int) -> None:
      # if key exists in cache, replace the value
      if key in self.cache:
        self.cache[key] = value
        self.moveNodeToHead(self.head, key)
      else:
        # check if cache size is at our capacity
        if len(self.cache.keys()) > self.capacity:
          # if at capacity, we remove the tail pointer Node and remove the key/val pair from cache
          self.removeTailNode()
          # we add new key/val pair to cache
          self.cache[key] = value
          self.addNodeToHead(self.head, key)
          # update linked list tail with the new key
          self.addNodeToHead(key)


    def moveNodeToHead(self, head: Node, key: int) -> None:
      # TODO

    def moveNodeToTail(self, key: int) -> None:
      # TODO
    
    def addNodeToHead(self, key: int) -> None:
      new_head = Node(key)
      self.head.prev = new_head
      new_head.next = self.head
      self.head = new_head

    def removeTailNode(self) -> None:

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)