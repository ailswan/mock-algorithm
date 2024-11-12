# 1206. Design Skiplist
# Design a Skiplist without using any built-in libraries.

# A skiplist is a data structure that takes O(log(n)) time to add, erase and search. Comparing with treap and red-black tree which has the same function and performance, the code length of Skiplist can be comparatively short and the idea behind Skiplists is just simple linked lists.

# For example, we have a Skiplist containing [30,40,50,60,70,90] and we want to add 80 and 45 into it. The Skiplist works this way:
# https://assets.leetcode.com/uploads/2019/09/27/1506_skiplist.gif

# Artyom Kalinin [CC BY-SA 3.0], via Wikimedia Commons

# You can see there are many layers in the Skiplist. Each layer is a sorted linked list. With the help of the top layers, add, erase and search can be faster than O(n). It can be proven that the average time complexity for each operation is O(log(n)) and space complexity is O(n).

# See more about Skiplist: https://en.wikipedia.org/wiki/Skip_list

# Implement the Skiplist class:

# Skiplist() Initializes the object of the skiplist.
# bool search(int target) Returns true if the integer target exists in the Skiplist or false otherwise.
# void add(int num) Inserts the value num into the SkipList.
# bool erase(int num) Removes the value num from the Skiplist and returns true. If num does not exist in the Skiplist, do nothing and return false. If there exist multiple num values, removing any one of them is fine.
# Note that duplicates may exist in the Skiplist, your code needs to handle this situation.

 

# Example 1:

# Input
# ["Skiplist", "add", "add", "add", "search", "add", "search", "erase", "erase", "search"]
# [[], [1], [2], [3], [0], [4], [1], [0], [1], [1]]
# Output
# [null, null, null, null, false, null, true, false, true, false]

# Explanation
# Skiplist skiplist = new Skiplist();
# skiplist.add(1);
# skiplist.add(2);
# skiplist.add(3);
# skiplist.search(0); // return False
# skiplist.add(4);
# skiplist.search(1); // return True
# skiplist.erase(0);  // return False, 0 is not in skiplist.
# skiplist.erase(1);  // return True
# skiplist.search(1); // return False, 1 has already been erased.
 

# Constraints:

# 0 <= num, target <= 2 * 10^4
# At most 5 * 10^4 calls will be made to search, add, and erase.

class Node:
    def __init__(self, val, next, prev) -> None:
        self.val = val
        self.next = next
        self.prev = prev

class Skiplist:

    def __init__(self):
        # use a linked list to store the base level
        # use dictionary to store the <level, (head_ptr, tail_ptr)>
        self.l1_head = Node()
        self.l1_tail = Node()
        self.l1_head.next = self.l1_tail
        self.l1_tail.prev = self.l1_head

        self.dic = {
            "1": (self.l1_head, self.l1_tail)
        }
        

    def search(self, target: int) -> bool:
        # start from the top-most level, scan the linked list for target
        # if doesn't exist, move down to next level and search
        # 

    def add(self, num: int) -> None:
        # when a new number is added, do coin flip to see if input number should be promoted
            # if heads and next level exists... promote the number
            # if tails, do nothing
        
        ptr = self.dic["1"][0]
        while ptr.next != self.dic["1"][1]:
            if ptr.val < num:
                ptr = ptr.next
            else:
                new_node = Node(num)
                tmp_next = ptr.next
                ptr.next = new_node
                new_node.prev = ptr
                new_node.next = tmp_next
                tmp_next.prev = new_node
        
        is_promoted = self.flip_coin()
        if is_promoted and self.dic[lvl + 1] is not None:
            ptr = self.dic[lvl + 1][0]
            


    def erase(self, num: int) -> bool:
        # start from top list, remove number if it exists
        # otherwise, check all lower levels to find the number

    def flip_coin(self) -> bool:
        return choice(0, 1)
    
# Your Skiplist object will be instantiated and called as such:
# obj = Skiplist()
# param_1 = obj.search(target)
# obj.add(num)
# param_3 = obj.erase(num)



import random

MAX_LEVEL = 32
P_FACTOR = 0.25

def random_level() -> int:
    lv = 1
    while lv < MAX_LEVEL and random.random() < P_FACTOR:
        lv += 1
    return lv

class SkiplistNode:
    __slots__ = 'val', 'forward'

    def __init__(self, val: int, max_level=MAX_LEVEL):
        self.val = val
        self.forward = [None] * max_level

class Skiplist:
    def __init__(self):
        self.head = SkiplistNode(-1)
        self.level = 0

    def search(self, target: int) -> bool:
        curr = self.head
        for i in range(self.level - 1, -1, -1):
            # Find the element closest to and less than target in level i
            while curr.forward[i] and curr.forward[i].val < target:
                curr = curr.forward[i]
        curr = curr.forward[0]
        # Check if the current element's value is equal to target
        return curr is not None and curr.val == target

    def add(self, num: int) -> None:
        update = [self.head] * MAX_LEVEL
        curr = self.head
        for i in range(self.level - 1, -1, -1):
            # Find the element closest to and less than num in level i
            while curr.forward[i] and curr.forward[i].val < num:
                curr = curr.forward[i]
            update[i] = curr
        lv = random_level()
        self.level = max(self.level, lv)
        new_node = SkiplistNode(num, lv)
        for i in range(lv):
            # Update the state at level i, setting the current element's forward to the new node
            new_node.forward[i] = update[i].forward[i]
            update[i].forward[i] = new_node

    def erase(self, num: int) -> bool:
        update = [None] * MAX_LEVEL
        curr = self.head
        for i in range(self.level - 1, -1, -1):
            # Find the element closest to and less than num in level i
            while curr.forward[i] and curr.forward[i].val < num:
                curr = curr.forward[i]
            update[i] = curr
        curr = curr.forward[0]
        if curr is None or curr.val != num:  # Value does not exist
            return False
        for i in range(self.level):
            if update[i].forward[i] != curr:
                break
            # Update the state at level i, setting forward to skip the deleted node
            update[i].forward[i] = curr.forward[i]
        # Update the current level
        while self.level > 1 and self.head.forward[self.level - 1] is None:
            self.level -= 1
        return True
