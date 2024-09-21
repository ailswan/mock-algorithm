from typing import List
 
#  380. Insert Delete GetRandom O(1)
# Implement the RandomizedSet class:

# RandomizedSet() Initializes the RandomizedSet object.
# bool insert(int val) Inserts an item val into the set if not present. Returns true if the item was not present, false otherwise.
# bool remove(int val) Removes an item val from the set if present. Returns true if the item was present, false otherwise.
# int getRandom() Returns a random element from the current set of elements (it's guaranteed that at least one element exists when this method is called). 
# Each element must have the same probability of being returned.
# You must implement the functions of the class such that each function works in average O(1) time complexity.

 

# Example 1:

# Input
# ["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"]
# [[], [1], [2], [2], [], [1], [2], []]
# Output
# [null, true, false, true, 2, true, false, 2]

# Explanation
# RandomizedSet randomizedSet = new RandomizedSet();
# randomizedSet.insert(1); // Inserts 1 to the set. Returns true as 1 was inserted successfully.
# randomizedSet.remove(2); // Returns false as 2 does not exist in the set.
# randomizedSet.insert(2); // Inserts 2 to the set, returns true. Set now contains [1,2].
# randomizedSet.getRandom(); // getRandom() should return either 1 or 2 randomly.
# randomizedSet.remove(1); // Removes 1 from the set, returns true. Set now contains [2].
# randomizedSet.insert(2); // 2 was already in the set, so return false.
# randomizedSet.getRandom(); // Since 2 is the only number in the set, getRandom() will always return 2.
# Constraints:

# -2^31 <= val <= 2^31 - 1
# At most 2 * 10^5 calls will be made to insert, remove, and getRandom.
# There will be at least one element in the data structure when getRandom is called.

class RandomizedSet:

    def __init__(self):
        # use hashmap to store the inserted values as key and an index as the value
        self.storage = {} # store <key, index of value in our self.arr>
        self.arr = []
        self.count = 0


    def insert(self, val: int) -> bool:
    # bool insert(int val) Inserts an item val into the set if not present. Returns true if the item was not present, false otherwise.
    # first check if val exists in our hashmap, if so, return False
    # otherwise, add the val to storage and return True
        if val in self.storage:
            return False
        else:
            self.storage[val] = self.count
            self.arr.append(val)
            self.count += 1
            return True



    def remove(self, val: int) -> bool:
    # bool remove(int val) Removes an item val from the set if present. Returns true if the item was present, false otherwise.
    # check if val exists in hashmap, if so, return True and delete the key/val pair from storage
    # otherwise return False
        if val in self.storage:
            tmp = self.storage[val]
            last_val = self.arr[-1]
            del self.storage[val]
            self.count -= 1
            self.arr[self.count], self.arr[-1] = self.arr[-1], self.arr[self.count]
            self.arr.pop()
            self.storage[last_val] = tmp
            return True
        else:
            return False

    def getRandom(self) -> int:
    # int getRandom() Returns a random element from the current set of elements (it's guaranteed that at least one element exists when this method is called).
    # we take the total number of items in storage... find a random index between 1 and total number of keys, return element of that index
        if len(self.arr) == 1:
            for k in self.storage.keys():
                return k
        # random_index = int(random.random(self.min_val, self.count + 1))
        return self.arr[random_index]
    
    random.choice(self.list)

        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

                # insert   delete    random
# list    -----    1         n          1
# dic     -----    1         1          n
# set
# linked-list
# heap
#...