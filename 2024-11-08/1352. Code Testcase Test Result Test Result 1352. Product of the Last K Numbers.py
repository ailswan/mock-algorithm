 
# 1352. Product of the Last K Numbers
# Design an algorithm that accepts a stream of integers and retrieves the product of the last k integers of the stream.

# Implement the ProductOfNumbers class:

# ProductOfNumbers() Initializes the object with an empty stream.
# void add(int num) Appends the integer num to the stream.
# int getProduct(int k) Returns the product of the last k numbers in the current list. You can assume that always the current list has at least k numbers.
# The test cases are generated so that, at any time, the product of any contiguous sequence of numbers will fit into a single 32-bit integer without overflowing.

 

# Example:

# Input
# ["ProductOfNumbers","add","add","add","add","add","getProduct","getProduct","getProduct","add","getProduct"]
# [[],[3],[0],[2],[5],[4],[2],[3],[4],[8],[2]]

# Output
# [null,null,null,null,null,null,20,40,0,null,32]

# Explanation
# ProductOfNumbers productOfNumbers = new ProductOfNumbers();
# productOfNumbers.add(3);        // [3]
# productOfNumbers.add(0);        // [3,0]
# productOfNumbers.add(2);        // [3,0,2]
# productOfNumbers.add(5);        // [3,0,2,5]
# productOfNumbers.add(4);        // [3,0,2,5,4]
# productOfNumbers.getProduct(2); // return 20. The product of the last 2 numbers is 5 * 4 = 20
# productOfNumbers.getProduct(3); // return 40. The product of the last 3 numbers is 2 * 5 * 4 = 40
# productOfNumbers.getProduct(4); // return 0. The product of the last 4 numbers is 0 * 2 * 5 * 4 = 0
# productOfNumbers.add(8);        // [3,0,2,5,4,8]
# productOfNumbers.getProduct(2); // return 32. The product of the last 2 numbers is 4 * 8 = 32 
 

# Constraints:

# 0 <= num <= 100
# 1 <= k <= 4 * 10^4
# At most 4 * 10^4 calls will be made to add and getProduct.
# The product of the stream at any point in time will fit in a 32-bit integer.

class ProductOfNumbers:

    # [3,0,2,5,4]

    def __init__(self):
        # we need a list to store the incoming numbers
        # store a prefix product in a dictionary
            # at every index, we know the product of all the numbers before it <idx, product_from_0_to_idx>
        # to find the product of last k elements, subtract products at n - k-th index where n is length of list

        self.nums = []
        self.size = 0      
        self.idx_to_product = {}
        self.last_zero_seen_idx = None
        # Initialize the prefix product list with an initial value of 1
        # This helps with multiplication as we always have a base product to work from
        # 'prelen' keeps track of the number of elements in 'prelst'
        self.prelst, self.prelen = [1], 1

    def add(self, num: int) -> None:
        self.nums.append(num)                   # [3, 0, 2]
        if not self.last_zero_seen_idx and num == 0:
            self.last_zero_seen_idx = self.size

        if not self.idx_to_product:
            self.idx_to_product[str(self.size)] = num    # { "0": 3 }
        else:
            self.idx_to_product[self.size] = self.idx_to_product.get(self.size, 1) * num    # {"0": 3, "1": 0, "2": 0}

        self.size += 1      # self.size = 3
        return None
    
    def getProduct(self, k: int) -> int:
        # if k
        return self.idx_to_product[self.size] / self.idx_to_product[self.size - k]


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)


class ProductOfNumbers:
    def __init__(self):
        self.prelst, self.prelen = [1], 1

    def add(self, num: int) -> None:
        if num:
            self.prelst.append(self.prelst[-1] * num)
            self.prelen += 1
        else:
            self.prelst, self.prelen = [1], 1            

    def getProduct(self, k: int) -> int:
        return self.prelst[-1] // self.prelst[- 1 - k] if k < self.prelen else 0
 